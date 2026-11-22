#!/usr/bin/env python3
"""One-time worldwide v2 sight rating correction across the 1733 original sights.

This corrects inconsistent historical authoring batches, explicitly calibrates
189 named worldwide peer benchmarks, and creates an old/new score audit.

Future attractions must NOT use these archived historical adjustment curves:
rate each directly against methodology/sight-scoring-guide.md instead.
The marker makes repeat application impossible. This is an editorial first
pass, not 1733 independent research-based field reviews.

Usage:
    python scripts/recalibrate_sights_2026.py          # dry-run
    python scripts/recalibrate_sights_2026.py --apply  # ONCE on pre-calibration sources
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import yaml

from rank import overall_score

ROOT = Path(__file__).resolve().parents[1]
COUNTRIES = ROOT / "countries"
SCORING = ROOT / "methodology/scoring.json"
PROFILES = ROOT / "methodology/sight-benchmark-profiles.txt"
MARKER = ROOT / "methodology/sight-calibration-2026.json"
AUDIT = ROOT / "methodology/sight-calibration-audit.md"
CORE = ("impact", "uniqueness", "significance", "experience", "depth")
COUNTS = {"AT": 133, "TH": 206, "KR": 284, "CN": 490, "VN": 360, "KH": 260}
# Historical authoring batches -- NOT rules for new countries. The three
# cohorts had different first-pass rating standards despite identical weights.
# No percentile remapping, national quotas, automatic site-type bonuses or
# future country-specific multipliers are applied.
EARLIER_CALIBRATED = frozenset(("AT", "TH", "KR"))
CHINA_FIRST_PASS = frozenset(("CN",))
VIETNAM_CAMBODIA_FIRST_PASS = frozenset(("VN", "KH"))

EARLIER_CURVE = (
    (0, 0), (4, 4), (5, 5), (6, 6.0), (7, 7.1),
    (8, 8.1), (8.5, 8.6), (9, 9.1),
    (9.5, 9.5), (9.9, 9.9), (10, 10),
)
CHINA_CURVE = (
    (0, 0), (4, 4), (5, 4.9), (6, 5.8), (7, 6.7),
    (8, 7.6), (8.5, 8.0), (9, 8.5), (9.3, 8.8),
    (9.5, 9.1), (9.8, 9.5), (9.9, 9.7), (10, 10),
)
LATE_FIRST_PASS_CURVE = (
    (0, 0), (4, 3.5), (5, 4.4), (6, 5.3),
    (7, 6.2), (8, 7.0), (8.5, 7.4), (9, 7.9),
    (9.3, 8.3), (9.5, 8.6), (9.7, 9.0),
    (9.8, 9.2), (9.9, 9.5), (10, 10),
)
D = Decimal


def transform(value, anchors):
    """Deterministic, monotone decimal interpolation, rounded to 0.1."""
    if value is None:
        return None
    if (isinstance(value, bool) or not isinstance(value, (int, float))
            or not 0 <= value <= 10):
        raise ValueError(f"Invalid original score: {value!r}")
    x = D(str(value))
    for (x0, y0), (x1, y1) in zip(anchors, anchors[1:]):
        a, b = D(str(x0)), D(str(x1))
        if a <= x <= b:
            v = D(str(y0)) + (x - a) * (D(str(y1)) - D(str(y0))) / (b - a)
            return float(v.quantize(D("0.1"), rounding=ROUND_HALF_UP))
    raise AssertionError(f"Unreachable original score: {value}")


def parse_profiles(categories):
    result = {}
    for line in PROFILES.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("|")
        if len(parts) != 3:
            raise ValueError(f"Invalid profile format: {line}")
        reference, core_text, category_text = parts
        country, slug = reference.split("/")
        if country not in COUNTS or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError(f"Unknown country or slug: {reference}")
        ident = f"sight-{country.lower()}-{slug}"
        if ident in result:
            raise ValueError(f"Duplicate profile: {ident}")
        nums = [float(t) for t in core_text.split(",")]
        cats = {}
        for pair in filter(None, category_text.split(",")):
            k, v = pair.split(":")
            if k in cats:
                raise ValueError(f"Repeated category override {ident}/{k}")
            cats[k] = float(v)
        all_values = [*nums, *cats.values()]
        if (len(nums) != 5 or not set(cats).issubset(categories) or
                any(not 0 <= n <= 10 or n * 10 != round(n * 10) for n in all_values)):
            raise ValueError(f"Invalid score/profile: {ident}")
        result[ident] = (dict(zip(CORE, nums)), cats)
    if len(result) != 189:
        raise ValueError(f"Expected 189 approved sight profiles, got {len(result)}")
    return result


def replace_score_lines(old_text, scores):
    """Only update numeric scores. Keep name, ID, coordinates, YAML layout."""
    out, saw_core, saw_categories = [], set(), set()
    in_categories = False
    for line in old_text.splitlines(keepends=True):
        if line.startswith("  categories:"):
            in_categories = True
            out.append(line)
            continue
        cm = re.fullmatch(
            r"(  (impact|uniqueness|significance|experience|depth): )([^\r\n]+)(\r?\n?)", line
        )
        km = (re.fullmatch(r"(    ([a-z]+): )([^\r\n]+)(\r?\n?)", line)
              if in_categories else None)
        match = cm or km
        if match:
            key = match.group(2)
            vals = scores if cm else scores["categories"]
            if key not in vals:
                raise ValueError(f"Unexpected source category {key}")
            value = vals[key]
            out.append(match.group(1) +
                       ("null" if value is None else f"{value:.1f}") +
                       match.group(4))
            (saw_core if cm else saw_categories).add(key)
        else:
            out.append(line)
    if saw_core != set(CORE) or not in_categories:
        raise ValueError(f"YAML missing dimensions or categories: {saw_core}")
    if not out[-1].endswith("\n"):
        out[-1] += "\n"
    for key, value in scores["categories"].items():
        if key not in saw_categories:
            out.append(f"    {key}: {'null' if value is None else f'{value:.1f}'}\n")
    return "".join(out)


def report(rows, profiles):
    grouped = defaultdict(list)
    for row in rows:
        grouped[row["country"]].append(row)
    lines = [
        "# Worldwide sight-score calibration audit — 22 November 2026",
        "",
        "**One-time editorial calibration:** 1,733 previously assessed sights, "
        "including **189 individually specified world-benchmark profiles**. "
        "The other 1,544 sights received a transparent conservative correction "
        "to the historical scoring batches. This is NOT 1,733 independently "
        "researched on-site evaluations and remains open to future evidence-based revision.",
        "",
        "All 639 existing city records and their values are unchanged. All sight "
        "names, IDs, source GPS coordinates, country codes, original category "
        "applicability, worldwide weights and existing 10/10 registry approvals "
        "are preserved; explicitly reviewed profiles may add an applicable category.",
        "",
        "No country quotas or percentile ranking targets were used. Earlier "
        "AT/TH/KR records were already conservatively scored; CN was less "
        "conservative; VN/KH were very generously rated. The three distinct "
        "original authoring batches require a **one-time historical** correction. "
        "These archived curves MUST NEVER be applied to any future country.",
        "",
        "See the mandatory [sight scoring guide](sight-scoring-guide.md), "
        "[global sight comparison benchmarks](sight-comparison-benchmarks.md), "
        "and [189 frozen profiles](sight-benchmark-profiles.txt).",
        "",
        "## Country diagnostics (not country quotas)",
        "",
        "| Country | Sights | Old mean | New mean | Old median | New median | 90+ before | 90+ after |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for code in sorted(grouped):
        grp = grouped[code]
        old = [r["old"] for r in grp]
        new = [r["new"] for r in grp]
        lines.append(f"| {code} | {len(grp)} | {statistics.mean(old):.2f} | "
                     f"{statistics.mean(new):.2f} | {statistics.median(old):.2f} | "
                     f"{statistics.median(new):.2f} | "
                     f"{sum(x >= 90 for x in old)} | {sum(x >= 90 for x in new)} |")
    lines.extend([
        "",
        "## Selected global-reference comparisons",
        "",
        "| Sight | Before /100 | After /100 |",
        "| --- | ---: | ---: |",
    ])
    anchors = (
        ("AT", "schoenbrunn-palace"),
        ("AT", "hohensalzburg-fortress"),
        ("AT", "hofburg-palace"),
        ("TH", "ayutthaya-historical-park"),
        ("KR", "gyeongju-historic-areas"),
        ("CN", "great-wall-jinshanling"),
        ("CN", "forbidden-city"),
        ("VN", "ha-long-bay"),
        ("VN", "phong-nha-ke-bang-national-park"),
        ("VN", "cu-chi-tunnels"),
        ("KH", "angkor-wat"),
        ("KH", "angkor-archaeological-park"),
        ("KH", "siem-reap-royal-gardens"),
        ("KH", "made-in-cambodia-market"),
    )
    indexed = {(r["country"], r["slug"]): r for r in rows}
    for country, slug in anchors:
        r = indexed[(country, slug)]
        lines.append(f"| [{r['name']}](../countries/{country}/sights/{slug}.yaml) "
                     f"({country}) | {r['old']:.2f} | **{r['new']:.2f}** |")
    lines.extend([
        "",
        "## Full before/after audit: all 1,733 records",
        "",
        "| Country | Sight (source YAML) | Before /100 | After /100 | Change | Individually benchmarked |",
        "| --- | --- | ---: | ---: | ---: | --- |",
    ])
    for r in sorted(rows, key=lambda x: (x["country"], x["slug"])):
        method = "Yes" if r["id"] in profiles else "Historic curve only"
        lines.append(f"| {r['country']} | "
                     f"[{r['name']}](../countries/{r['country']}/sights/{r['slug']}.yaml) "
                     f"| {r['old']:.2f} | {r['new']:.2f} | "
                     f"{r['new'] - r['old']:+.2f} | {method} |")
    lines.extend([
        "",
        "## Scope and limitations",
        "",
        "- Same pre-existing worldwide v2 weights and all approved field-specific "
        "10/10 scores; no new tens or automatic UNESCO bonuses.",
        "- Historic authoring curves are **not a universal score calculator**, "
        "future-country multiplier, or replacement for direct comparative judgment.",
        "- An attraction that is a nested component of a larger park may be "
        "ranked separately, but it must be assessed for its own merits. "
        "Do not duplicate the park's near-perfect score automatically.",
        "- Visitor access, safety, opening hours and temporary closures are "
        "separate from long-term intrinsic quality; follow specific advisory text.",
        "- This editorial ranking is subjective and may be refined where "
        "verifiable historical, cultural, geographic or visitor evidence warrants it.",
        "",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true",
                        help="Apply the historical calibration exactly once")
    args = parser.parse_args()
    if MARKER.exists():
        raise SystemExit("Sight scores already calibrated: refusing second application.")
    metadata = json.loads(SCORING.read_text(encoding="utf-8"))
    if metadata.get("version") != 2:
        raise ValueError("Expected worldwide calibration version 2")
    weights = {k: D(str(v)) for k, v in metadata["dimensions"].items()}
    if tuple(weights) != CORE:
        raise ValueError("Unexpected weighted dimensions")
    profile_map = parse_profiles(set(metadata["categories"]))
    approved = {(k, ident) for k, ids in metadata["global_ten_anchors"].items()
                for ident in ids}
    seen, rows, pending = set(), [], []
    approved_existing = set()
    approved_after = set()
    for country, expected in COUNTS.items():
        paths = sorted((COUNTRIES / country / "sights").glob("*.yaml"))
        if len(paths) != expected:
            raise ValueError(f"Historical source mismatch {country}: {len(paths)} != {expected}")
        adjustment = (EARLIER_CURVE if country in EARLIER_CALIBRATED else
                      CHINA_CURVE if country in CHINA_FIRST_PASS else
                      LATE_FIRST_PASS_CURVE)
        for path in paths:
            old_text = path.read_text(encoding="utf-8")
            original = yaml.safe_load(old_text)
            ident = original["id"]
            if ident != f"sight-{country.lower()}-{path.stem}":
                raise ValueError(f"Unexpected source ID: {ident}")
            prev = original["scores"]
            source_ratings = {**{k: prev[k] for k in CORE}, **prev["categories"]}
            approved_existing.update((k, ident) for k, v in source_ratings.items()
                                     if v == 10)
            scores = {k: transform(prev[k], adjustment) for k in CORE}
            scores["categories"] = {
                k: transform(v, adjustment) for k, v in prev["categories"].items()
            }
            if ident in profile_map:
                explicit_core, explicit_cats = profile_map[ident]
                scores.update(explicit_core)
                scores["categories"].update(explicit_cats)
                seen.add(ident)
            revised_ratings = {**{k: scores[k] for k in CORE},
                               **scores["categories"]}
            for k, v in revised_ratings.items():
                if v == 10:
                    if (k, ident) not in approved:
                        raise ValueError(f"Unapproved global ten {ident}/{k}")
                    approved_after.add((k, ident))
            after = original.copy()
            after["scores"] = scores
            new_text = replace_score_lines(old_text, scores)
            if yaml.safe_load(new_text) != after:
                raise ValueError(f"Unexpected change to record identity/location: {ident}")
            was = overall_score(original, weights)
            now = overall_score(after, weights)
            if was is None or now is None or now > 100:
                raise ValueError(f"Invalid overall sight rating: {ident}")
            rows.append({
                "id": ident, "country": country, "slug": path.stem,
                "name": original["name"], "old": float(was), "new": float(now)
            })
            pending.append((path, new_text))
    if len(rows) != 1733 or len(profile_map) != 189 or set(profile_map) != seen:
        raise ValueError(f"Incomplete historical audit: {len(rows)} rows, "
                         f"{len(seen)} of {len(profile_map)} explicit profiles")
    approved_sight_tens = {(k, ident) for k, ident in approved if ident.startswith("sight-")}
    if approved_existing != approved_sight_tens or approved_after != approved_sight_tens:
        raise ValueError(f"Lost/gained approved worldwide tens: "
                         f"{sorted(approved_existing ^ approved_after)}")
    indexed = {r["id"]: D(str(r["new"])) for r in rows}
    required = (
        ("sight-cn-great-wall-jinshanling", "sight-at-schoenbrunn-palace", 3),
        ("sight-kh-angkor-wat", "sight-at-hohensalzburg-fortress", 5),
        ("sight-at-hohensalzburg-fortress", "sight-kh-made-in-cambodia-market", 12),
        ("sight-at-hofburg-palace", "sight-kh-siem-reap-royal-gardens", 15),
        ("sight-vn-ha-long-bay", "sight-vn-nha-trang-beach", 8),
        ("sight-th-ayutthaya-historical-park", "sight-kh-made-in-cambodia-market", 15),
    )
    for a, b, gap in required:
        if indexed[a] - indexed[b] < D(gap):
            raise ValueError(f"Required cross-country comparison failed: {a} vs {b}")
    print(f"Audited {len(rows)} sight YAMLs, {len(seen)} named benchmark profiles, "
          f"{len(approved_sight_tens)} pre-approved 10/10 fields.")
    for key in ("sight-at-schoenbrunn-palace", "sight-at-hohensalzburg-fortress",
                "sight-cn-great-wall-jinshanling", "sight-vn-ha-long-bay",
                "sight-kh-angkor-wat", "sight-kh-made-in-cambodia-market"):
        r = next(x for x in rows if x["id"] == key)
        print(f"  {r['id']}: {r['old']:.2f} -> {r['new']:.2f}")
    if not args.apply:
        print("Dry-run only. Pass --apply exactly once to change 1733 YAML records.")
        return
    for path, content in pending:
        path.write_text(content, encoding="utf-8", newline="\n")
    AUDIT.write_text(report(rows, profile_map), encoding="utf-8", newline="\n")
    MARKER.write_text(json.dumps({
        "review_date": "2026-11-22",
        "scoring_version": 2,
        "sights_recalibrated": 1733,
        "individually_benchmarked": 189,
        "original_country_counts": COUNTS,
        "historic_only": True,
        "guide": "methodology/sight-scoring-guide.md",
        "audit": "methodology/sight-calibration-audit.md",
    }, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Changed all {len(pending)} sights; wrote complete audit and rerun marker.")


if __name__ == "__main__":
    main()
