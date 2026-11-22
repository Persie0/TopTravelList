#!/usr/bin/env python3
"""Reassess named sight profiles without country multipliers or reusing migration curves.

Every single sight is enumerated with a baseline snapshot, current core dimensions,
category ratings, peer class, and diagnostic flags. Explicit editorial changes are
stored in methodology/sight-review-decisions-2026/*.tsv with site-specific reasons.
Unchanged records are AUTOMATICALLY SCREENED ONLY, not independently desk-researched.
The generated exhaustive audit intentionally distinguishes these two review levels.
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
COUNTRIES = ROOT / "countries"
DECISIONS = ROOT / "methodology" / "sight-review-decisions-2026"
BASELINE = ROOT / "methodology" / "sight-review-2026-baseline.json"
AUDIT = ROOT / "methodology" / "sight-review-2026-full-audit.md"
SUMMARY = ROOT / "methodology" / "sight-review-2026-summary.md"
FIELDS = ("impact", "uniqueness", "significance", "experience", "depth")
WEIGHTS = tuple(Decimal(s) for s in ("0.30", "0.25", "0.20", "0.15", "0.10"))
COUNTRY_CODES = ("AT", "TH", "KR", "CN", "VN", "KH", "TW")

PEER_GROUPS = {
    "railway / civil engineering": (
        "AT/semmering-railway", "TW/alishan-forest-railway",
        "CN/dujiangyan-irrigation-system", "VN/golden-bridge-ba-na-hills"),
    "museum / memorial": (
        "TW/national-palace-museum", "CN/sanxingdui-museum",
        "AT/kunsthistorisches-museum", "KH/national-museum-cambodia"),
    "temple / historic religious site": (
        "KH/angkor-wat", "TH/wat-phra-kaew",
        "KR/bulguksa-temple", "VN/po-nagar-cham-towers"),
    "palace / castle": (
        "CN/forbidden-city", "AT/schoenbrunn-palace",
        "KR/changdeokgung-palace", "KH/royal-palace-phnom-penh"),
    "reserve / protected landscape": (
        "CN/jiuzhaigou-valley", "VN/phong-nha-ke-bang-national-park",
        "AT/hohe-tauern-national-park", "TW/yushan-national-park"),
    "wetland / wildlife": (
        "TH/huai-kha-khaeng-wildlife-sanctuary",
        "KH/keo-seima-wildlife-sanctuary",
        "VN/tram-chim-national-park", "KR/suncheon-bay-wetland-reserve"),
    "beach / resort shoreline": (
        "TH/railay-beach", "VN/nha-trang-beach",
        "KH/sokha-beach", "TW/fulong-beach"),
    "cave / grotto": (
        "VN/son-doong-cave", "AT/eisriesenwelt-werfen",
        "KR/manjanggul-lava-tube", "CN/mogao-caves"),
    "island / seascape": (
        "VN/ha-long-bay", "TH/phang-nga-bay",
        "KR/jeju-island", "TW/penghu-islands"),
    "market / commercial street": (
        "KH/made-in-cambodia-market", "VN/cai-rang-floating-market",
        "TW/raohe-street-night-market", "CN/hongyadong"),
    "historic ensemble / fortification": (
        "CN/great-wall-jinshanling", "KH/angkor-archaeological-park",
        "KR/gyeongju-historic-areas", "AT/hohensalzburg-fortress"),
    "singular small landmark": (
        "TW/taipei-101", "CN/victoria-harbour",
        "VN/golden-bridge-ba-na-hills", "KH/siem-reap-royal-gardens"),
    "waterfall / river": (
        "AT/krimml-waterfalls", "VN/ban-gioc-waterfall",
        "TW/shifen-waterfall", "VN/mekong-delta"),
}

def peer_class(name: str, cats: dict) -> str:
    n = name.casefold()
    if re.search(r"railway|railroad|rail line|irrigation system", n):
        return "railway / civil engineering"
    if re.search(r"museum|memorial|mausoleum|genocid|library|birthplace|exhibition", n):
        return "museum / memorial"
    if re.search(r"palace|castle|chateau|schloss", n):
        return "palace / castle"
    if re.search(r"temple|shrine|pagoda|monastery|stupa|cathedral|abbey|buddha|church|mosque", n):
        return "temple / historic religious site"
    if re.search(r"wetland|wildlife|sanctuary|biosphere|dolphin|bird|butterfly", n):
        return "wetland / wildlife"
    if re.search(r"cave|grotto|cavern|lava tube|ice cave", n):
        return "cave / grotto"
    if re.search(r"beach|strand", n):
        return "beach / resort shoreline"
    if re.search(r"island|islands|archipelago|marine park|bay", n):
        return "island / seascape"
    if re.search(r"waterfall|falls|river|delta", n):
        return "waterfall / river"
    if re.search(r"national park|forest|reserve|mountain|mount|peak|valley|geopark|gorge", n):
        return "reserve / protected landscape"
    if re.search(r"market|old street|night market|bazaar|pedestrian district", n):
        return "market / commercial street"
    if re.search(r"archaeological|historic|historical|fortress|citadel|great wall|old town|ancient", n):
        return "historic ensemble / fortification"
    if re.search(r"tower|viewpoint|bridge|pagoda|obelisk|monument|statue|terrace|square|garden", n):
        return "singular small landmark"
    if cats.get("nature", 0) and cats["nature"] >= 8:
        return "reserve / protected landscape"
    if cats.get("history", 0) and cats["history"] >= 8.5:
        return "historic ensemble / fortification"
    return "singular small landmark"


def score(rec: dict) -> Decimal:
    vals = [Decimal(str(rec["scores"][k])) for k in FIELDS]
    return (sum((w * v for w, v in zip(WEIGHTS, vals)), Decimal(0)) * 10).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )


def fmt(v) -> str:
    return str(Decimal(str(v)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


def read_decisions() -> dict:
    decisions = {}
    for code in COUNTRY_CODES:
        src = DECISIONS / f"{code}.tsv"
        if not src.exists():
            raise ValueError(f"Missing site-specific decisions: {src}")
        for line_number, line in enumerate(src.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip() or line.startswith("#"):
                continue
            sections = line.split("|")
            if len(sections) != 4:
                raise ValueError(f"Decision syntax at {src}:{line_number}")
            slug, scores_csv, cats_csv, reason = sections
            key = f"{code}/{slug}"
            if key in decisions:
                raise ValueError(f"Duplicate decision {key}")
            numbers = [Decimal(s) for s in scores_csv.split(",")]
            if len(numbers) != 5 or any(v < 0 or v > Decimal("9.9") or v.as_tuple().exponent < -1 for v in numbers):
                raise ValueError(f"Invalid dimension scores for {key}")
            categories = {}
            if cats_csv != "-":
                for assignment in cats_csv.split(","):
                    cat, value = assignment.split("=", 1)
                    v = Decimal(value)
                    if v < 0 or v > Decimal("9.9") or v.as_tuple().exponent < -1:
                        raise ValueError(f"Invalid category score {key}/{cat}")
                    categories[cat] = v
            if len(reason) < 60 or "\n" in reason:
                raise ValueError(f"Site-specific review reason missing: {key}")
            decisions[key] = (numbers, categories, reason)
    return decisions


def walk():
    for code in COUNTRY_CODES:
        for path in sorted((COUNTRIES / code / "sights").glob("*.yaml")):
            rec = yaml.safe_load(path.read_text(encoding="utf-8"))
            assert rec["id"] == f"sight-{code.lower()}-{path.stem}"
            yield f"{code}/{path.stem}", path, rec


def record_baseline(records):
    return {
        key: {
            "name": rec["name"],
            "overall": str(score(rec)),
            "core": {k: rec["scores"][k] for k in FIELDS},
            "categories": dict(rec["scores"]["categories"]),
        }
        for key, _, rec in records
    }


def write_checked(path: Path, content: str, check: bool):
    if check:
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            raise AssertionError(f"Generated audit needs regeneration: {path}")
    elif not path.exists() or path.read_text(encoding="utf-8") != content:
        path.write_text(content, encoding="utf-8", newline="\n")


def update_record(path: Path, rec: dict, nums: list[Decimal], cats: dict):
    txt = path.read_text(encoding="utf-8")
    new_txt = txt
    for dim, num in zip(FIELDS, nums):
        original = rec["scores"][dim]
        if Decimal(str(original)) == num:
            continue
        pattern = rf"(?m)^(  {re.escape(dim)}:\s*)[-+]?[0-9]+(?:\.[0-9]+)?\s*$"
        new_txt, n = re.subn(pattern, lambda m: m.group(1) + fmt(num), new_txt)
        if n != 1:
            raise AssertionError(f"Cannot replace {dim} in {path}")
    for cat, num in cats.items():
        if cat not in rec["scores"]["categories"]:
            raise ValueError(f"Category {cat} absent in {path}")
        if Decimal(str(rec["scores"]["categories"][cat])) == num:
            continue
        pattern = rf"(?m)^(    {re.escape(cat)}:\s*)[-+]?[0-9]+(?:\.[0-9]+)?\s*$"
        new_txt, n = re.subn(pattern, lambda m: m.group(1) + fmt(num), new_txt)
        if n != 1:
            raise AssertionError(f"Cannot replace category {cat} in {path}")
    if new_txt != txt:
        path.write_text(new_txt, encoding="utf-8", newline="\n")
    return new_txt != txt


def flags(rec: dict, peer: str) -> list[str]:
    s = rec["scores"]
    total = score(rec)
    out = []
    if total >= 95:
        out.append("95+ overall; elite peer evidence needed")
    elif total >= 90:
        out.append("90+ overall; verify world-class comparison")
    if s["significance"] >= 9.2 and peer in {
        "market / commercial street", "singular small landmark",
        "beach / resort shoreline", "railway / civil engineering",
    }:
        out.append("standalone significance vs world peers")
    if s["depth"] >= 9.0 and peer in {
        "singular small landmark", "temple / historic religious site",
        "market / commercial street", "beach / resort shoreline",
        "railway / civil engineering",
    }:
        out.append("short visit vs whole complex")
    if s["experience"] >= 9.3 and peer == "wetland / wildlife":
        out.append("ecosystem significance vs visitor experience")
    if any(Decimal(str(v)) >= Decimal("9.5") for k, v in s.items() if k in FIELDS):
        out.append("9.5+ core field")
    if any(v is not None and Decimal(str(v)) >= Decimal("9.5") for v in s["categories"].values()):
        out.append("9.5+ category field")
    return out


def make_reports(records, baseline, decisions):
    by_country = {c: [] for c in COUNTRY_CODES}
    details = []
    for key, path, rec in records:
        code, slug = key.split("/")
        old = Decimal(baseline[key]["overall"])
        new = score(rec)
        delta = new - old
        cls = peer_class(rec["name"], rec["scores"]["categories"])
        diagnostic = flags(rec, cls)
        targeted = key in decisions
        label = "Explicit desk-based reassessment" if targeted else "Automated screening only"
        reason = decisions[key][2] if targeted else (
            "No new site-specific evidence adjudicated; current score retained pending independent research."
        )
        details.append((key, rec["name"], old, new, delta, label, cls, diagnostic, reason))
        by_country[code].append((old, new, targeted, bool(diagnostic)))

    total = len(details)
    targeted_count = sum(x[5] == "Explicit desk-based reassessment" for x in details)
    changed = sum(x[2] != x[3] for x in details)
    flags_count = sum(bool(x[7]) for x in details)
    high_unchanged = sum(x[3] >= 90 and x[5] == "Automated screening only" for x in details)
    header = [
        "# Worldwide sight reassessment — individual decision register",
        "",
        "**Audit date: 22 November 2026.** This is a follow-on quality-control pass to the "
        "historic 1,733-sight migration. The earlier frozen benchmark profiles remain "
        "historical records, not current instructions to overwrite the newly revised YAML.",
        "",
        f"**{total} records individually enumerated and diagnostically screened**, including "
        f"**{targeted_count} sight-specific desk-based editorial reassessments**, "
        f"**{changed} numeric score changes**, and "
        f"**{total-targeted_count} automatically screened, unchanged records**.",
        "",
        "### Important limitation",
        "",
        "**Automated screening is not an independently researched individual assessment.** "
        "The user requested an item-by-item worldwide re-review; this audit records every "
        "item and applies all documented sight-specific judgments that could be completed. "
        "Sites marked `Automated screening only` retain provisional pre-existing scores and "
        "**still require individually researched verification**. "
        "No claim of 1,913 fresh independently researched destination reviews is made.",
        "",
        "All core scores use the existing worldwide v2 five-dimension weights. No national "
        "score quotas, country-specific multipliers, 2026 migration curves, or newly approved "
        "10/10 fields were used. Long-term significance does not imply admission or safety today.",
        "",
        "## Country diagnostics (not quotas)",
        "",
        "| Country | Sights | Site-specific reassessments | Numeric revisions | Before mean | After mean | 90+ before | 90+ after | Diagnostic alerts |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for code, scores in by_country.items():
        b = [float(x[0]) for x in scores]
        a = [float(x[1]) for x in scores]
        header.append(
            f"| {code} | {len(scores)} | {sum(x[2] for x in scores)} | "
            f"{sum(x[0] != x[1] for x in scores)} | {statistics.mean(b):.2f} | "
            f"{statistics.mean(a):.2f} | {sum(x >= 90 for x in b)} | "
            f"{sum(x >= 90 for x in a)} | {sum(x[3] for x in scores)} |"
        )

    header.extend([
        "",
        "## Review decisions and safeguards",
        "",
        "A decision is entered only for a named attraction with five explicit updated core "
        "dimensions and a site-specific reason. These revised values are **subjective desk-based "
        "editorial judgments**, not proven facts or a replacement for future individual research.",
        "",
        "Comparators are four published global ladder **starting points per sight type**, not "
        "proof that each individual destination has been independently investigated. "
        "The detailed site-specific rationale for targeted entries is shown for transparency.",
        "",
        f"**Open verification backlog:** {total-targeted_count} automatically screened sights, "
        f"including {high_unchanged} still scoring 90+.",
        "",
        "### Site-specific score decisions",
        "",
        "| Sight | Before | After | Change | Dimensions I / U / S / E / D | Reason |",
        "| --- | ---: | ---: | ---: | --- | --- |",
    ])
    for key, name, old, new, delta, label, cls, diagnostics, reason in details:
        if key not in decisions:
            continue
        code, slug = key.split("/")
        link = f"[{name}](../countries/{code}/sights/{slug}.yaml)"
        scores_text = " / ".join(fmt(v) for v in decisions[key][0])
        header.append(
            f"| {link} | {old:.2f} | **{new:.2f}** | {delta:+.2f} | "
            f"{scores_text} | {reason.replace('|','/')} |"
        )
    footer = [
        "",
        "## Detailed per-record table — all destinations",
        "",
        "Each sight's line gives its status. A retained score following automated triage "
        "is **not** an endorsement of its current international rank.",
        "",
        "| Country | Sight / source YAML | Before | After | Delta | Review level | Global comparison class | Flags / rationale |",
        "| --- | --- | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for key, name, old, new, delta, label, cls, diagnostic, reason in details:
        code, slug = key.split("/")
        note = reason if key in decisions else ("; ".join(diagnostic) if diagnostic else "Numeric and schema screening only; no fresh site research")
        note = note.replace("|", "/").replace("\n", " ")
        footer.append(
            f"| {code} | [{name}](../countries/{code}/sights/{slug}.yaml) | "
            f"{old:.2f} | **{new:.2f}** | {delta:+.2f} | {label} | {cls} | {note} |"
        )
    footer.append("")
    summary = "\n".join(header) + "\n"
    full = "\n".join(header + footer) + "\n"
    return summary, full, {
        "records": total,
        "targeted": targeted_count,
        "changed": changed,
        "screened_only": total-targeted_count,
        "flagged": flags_count,
        "remaining_high90": high_unchanged,
        "by_country": {c: {
            "total": len(vals), "reviewed": sum(x[2] for x in vals),
            "changed": sum(x[0]!=x[1] for x in vals),
            "high90_before": sum(x[0] >= 90 for x in vals),
            "high90_after": sum(x[1] >= 90 for x in vals),
        } for c, vals in by_country.items()},
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="Apply named judgments and generate audit")
    ap.add_argument("--check", action="store_true", help="Verify targeted values, reports and item coverage")
    args = ap.parse_args()
    if args.apply == args.check:
        ap.error("Select exactly one of --apply or --check")
    scoring = json.loads((ROOT / "methodology/scoring.json").read_text(encoding="utf-8"))
    assert tuple(scoring["dimensions"]) == FIELDS
    assert tuple(Decimal(str(v)) for v in scoring["dimensions"].values()) == WEIGHTS

    decisions = read_decisions()
    records = list(walk())
    keys = {key for key, _, _ in records}
    if len(keys) != len(records):
        raise AssertionError("Repeated sight record")
    if keys != (keys & set(f"{c}/{p.stem}" for c in COUNTRY_CODES for p in (COUNTRIES/c/"sights").glob("*.yaml"))):
        raise AssertionError("Invalid sight record indexing")
    missing = sorted(set(decisions) - keys)
    if missing:
        raise AssertionError(f"Decisions for unknown sights: {missing}")
    expected_count = 1913
    if len(records) != expected_count:
        raise AssertionError(f"Expected {expected_count} sights for this review, found {len(records)}")
    if args.apply and not BASELINE.exists():
        BASELINE.write_text(
            json.dumps(record_baseline(records), ensure_ascii=False, sort_keys=True, indent=2) + "\n",
            encoding="utf-8", newline="\n",
        )
    if not BASELINE.exists():
        raise AssertionError("Missing snapshot; run --apply first")
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    if set(baseline) != keys:
        raise AssertionError("Baseline and current records diverged; do not silently recalibrate")

    modified = 0
    for key, path, rec in records:
        if key not in decisions:
            continue
        nums, cats, _ = decisions[key]
        if args.apply:
            modified += update_record(path, rec, nums, cats)
        else:
            for field, target in zip(FIELDS, nums):
                if Decimal(str(rec["scores"][field])) != target:
                    raise AssertionError(f"Drift in reviewed {key}/{field}")
            for cat, target in cats.items():
                if Decimal(str(rec["scores"]["categories"][cat])) != target:
                    raise AssertionError(f"Drift in reviewed {key}/{cat}")

    updated = list(walk())
    summary, full, stats = make_reports(updated, baseline, decisions)
    write_checked(SUMMARY, summary, args.check)
    write_checked(AUDIT, full, args.check)
    stats_file = ROOT / "methodology" / "sight-review-2026-stats.json"
    write_checked(stats_file, json.dumps(stats, indent=2, sort_keys=True) + "\n", args.check)
    assert stats["targeted"] == len(decisions) == 149
    assert stats["screened_only"] == 1764
    if args.check:
        assert modified == 0
    print(
        f"PASS: {stats['records']} sight records screened, {stats['targeted']} site-specific "
        f"editorial decisions, {stats['changed']} revisions vs frozen snapshot, "
        f"{stats['flagged']} diagnostic flags; files edited in this run: {modified}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
