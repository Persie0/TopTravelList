#!/usr/bin/env python3
"""One-time 2026 global audit of 639 existing city records, NOT a future scoring script.

Run --apply once on the pre-calibration dataset. Future cities must instead be
rated directly using methodology/city-scoring-guide.md. Source IDs, names,
GPS coordinates and all sight records are preserved.
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

ROOT = Path(__file__).resolve().parents[1]
COUNTRIES = ROOT / "countries"
MARKER = ROOT / "methodology/city-calibration-2026.json"
REPORT = ROOT / "methodology/city-calibration-audit.md"
PROFILES = ROOT / "methodology/city-benchmark-profiles.txt"
CORE = ("impact", "uniqueness", "significance", "experience", "depth")
COUNTS = {"AT":45, "TH":69, "KR":82, "CN":231, "VN":140, "KH":72}
LEGACY = frozenset(("AT","TH","KR","CN"))
# Historical authoring cohorts, NOT multipliers for new countries. All
# dimensions and applicable categories use the same numeric curve per cohort.
LEGACY_CURVE = ((0,0),(4,4),(5,5),(6,5.9),(7,6.9),(8,7.9),
                (8.5,8.35),(9,8.85),(9.5,9.35),(9.9,9.75),(10,10))
EARLY_DIRECT_CURVE = ((0,0),(4,3.4),(5,4.2),(6,5.1),(7,5.9),
                      (7.5,6.4),(8,6.9),(8.5,7.4),(9,7.9),
                      (9.5,8.4),(9.9,8.8),(10,9.0))
D = Decimal


def convert(value, anchors):
    if value is None:
        return None
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not 0<=value<=10:
        raise ValueError(f"Invalid score: {value!r}")
    x=D(str(value))
    for (x0,y0),(x1,y1) in zip(anchors,anchors[1:]):
        a,b=D(str(x0)),D(str(x1))
        if a<=x<=b:
            val=D(str(y0))+(x-a)*(D(str(y1))-D(str(y0)))/(b-a)
            return float(val.quantize(D(".1"),rounding=ROUND_HALF_UP))
    raise AssertionError("Score outside curve")


def profiles(category_keys):
    result={}
    for line in PROFILES.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        place, dimensions, categories=line.split("|")
        code, slug=place.split("/")
        assert code in COUNTS and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",slug)
        ident=f"city-{code.lower()}-{slug}"
        if ident in result:
            raise ValueError(f"Duplicate override {ident}")
        vals=[float(v) for v in dimensions.split(",")]
        cats={key:float(val) for key,val in (piece.split(":") for piece in categories.split(",") if piece)}
        if len(vals)!=5 or not set(cats)<=category_keys or any(not 0<=v<=10 or v*10!=round(v*10) for v in [*vals,*cats.values()]):
            raise ValueError(f"Bad override for {ident}")
        result[ident]=(dict(zip(CORE,vals)),cats)
    if len(result)!=104:
        raise ValueError(f"Expected 104 city profiles, got {len(result)}")
    return result


def weighted(scores,weights):
    return 10*sum((D(str(scores[k]))*weights[k] for k in CORE),D("0"))


def rewrite_ratings(text, scores):
    """Rewrite score scalars only. Add an explicitly reviewed applicable category if new."""
    out, seen_core, seen_cat=[],set(),set()
    for line in text.splitlines(keepends=True):
        core=re.fullmatch(r"(  (impact|uniqueness|significance|experience|depth): )([^\r\n]+)(\r?\n?)",line)
        cat=re.fullmatch(r"(    ([a-z]+): )([^\r\n]+)(\r?\n?)",line)
        if core or cat:
            m=core or cat
            key=m.group(2)
            value=scores[key] if core else scores["categories"][key]
            out.append(m.group(1)+("null" if value is None else f"{value:.1f}")+m.group(4))
            (seen_core if core else seen_cat).add(key)
        else:
            out.append(line)
    if seen_core!=set(CORE):
        raise ValueError("Missing a required core score line")
    for key,value in scores["categories"].items():
        if key not in seen_cat:
            if value is None:
                out.append(f"    {key}: null\n")
            else:
                out.append(f"    {key}: {value:.1f}\n")
    return "".join(out)


def report(rows,profiles_map):
    lines=[
        "# One-time worldwide city calibration — 2026-11-22", "",
        "**Scope:** all 639 previously populated cities/towns/villages; all original sights untouched. "
        "A transparent conservative cohort correction plus **104 individually reviewed benchmark "
        "profiles**; not 639 independently researched site visits.",
        "",
        "The original authoring cohorts differed: AT/TH/KR/CN were converted from v1, whereas "
        "VN/KH were scored directly but too generously. These historic cohort curves are **not** "
        "rules for new countries and are never applied again.",
        "",
        "Future ratings: [city scoring guide](city-scoring-guide.md) and "
        "[cross-country benchmarks](city-comparison-benchmarks.md). "
        "Frozen 104 reference profiles: [text data](city-benchmark-profiles.txt).",
        "",
        "## Country-level diagnostics (not quotas)", "",
        "| Country | City records | Mean before | Mean after | Median before | Median after |",
        "| --- | ---: | ---: | ---: | ---: | ---: |"
    ]
    groups=defaultdict(list)
    for r in rows:
        groups[r["country"]].append(r)
    for country in sorted(groups):
        group=groups[country]
        o=[r["old"] for r in group]
        n=[r["new"] for r in group]
        lines.append(f"| {country} | {len(group)} | {statistics.mean(o):.2f} | {statistics.mean(n):.2f} | "
                     f"{statistics.median(o):.2f} | {statistics.median(n):.2f} |")
    lines.extend(["","## Complete 639-city change log","",
                  "Before and after use the existing weighted five-dimension overall /100. "
                  "The six country directories keep their same destinations and GPS coordinates.","",
                  "| Country | City source YAML | Before | After | Difference | Individual profile |",
                  "| --- | --- | ---: | ---: | ---: | --- |"])
    for r in sorted(rows,key=lambda r:(r["country"],r["slug"])):
        custom="Yes" if r["id"] in profiles_map else "Common curve"
        lines.append(f"| {r['country']} | [{r['name']}](../countries/{r['country']}/cities/{r['slug']}.yaml) "
                     f"| {r['old']:.2f} | {r['new']:.2f} | {r['new']-r['old']:+.2f} | {custom} |")
    lines.extend(["","**Limitations:** These remain provisional editorial comparisons, not "
                  "verified objective measurements. No country's percentile or population "
                  "determines a score. No sightseeing site automatically transfers its high "
                  "score to a nearby town. Only existing explicitly approved 10/10 "
                  "benchmarks in methodology/scoring.json are permitted.",""])
    return "\n".join(lines)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--apply",action="store_true",help="Write the one-time corrected city YAMLs and audit")
    args=p.parse_args()
    if MARKER.exists():
        raise SystemExit("Already calibrated: refusing to run the historic conversion twice.")
    meta=json.loads((ROOT/"methodology/scoring.json").read_text(encoding="utf-8"))
    if meta["version"]!=2:
        raise ValueError("Expected unchanged worldwide v2 scoring.")
    weights={k:D(str(v)) for k,v in meta["dimensions"].items()}
    if tuple(weights)!=CORE:
        raise ValueError("Unexpected scoring dimensions or order")
    custom=profiles(set(meta["categories"]))
    approved={(k,ident) for k,ids in meta["global_ten_anchors"].items() for ident in ids}
    rows,changes,seen=[],[],set()
    for country,expected in COUNTS.items():
        paths=sorted((COUNTRIES/country/"cities").glob("*.yaml"))
        if len(paths)!=expected:
            raise ValueError(f"Source dataset changed: {country} has {len(paths)} instead of {expected}")
        anchors=LEGACY_CURVE if country in LEGACY else EARLY_DIRECT_CURVE
        for path in paths:
            before_text=path.read_text(encoding="utf-8")
            before=yaml.safe_load(before_text)
            ident=f"city-{country.lower()}-{path.stem}"
            if before["id"]!=ident:
                raise ValueError(f"ID mismatch: {path}")
            old=before["scores"]
            revised={k:convert(old[k],anchors) for k in CORE}
            revised["categories"]={k:convert(v,anchors) for k,v in old["categories"].items()}
            if ident in custom:
                core,cats=custom[ident]
                revised.update(core)
                revised["categories"].update(cats)
                seen.add(ident)
            for k,v in {**{k:revised[k] for k in CORE},**revised["categories"]}.items():
                if v==10 and (k,ident) not in approved:
                    raise ValueError(f"Unapproved perfect 10: {ident}/{k}")
            after=before.copy()
            after["scores"]=revised
            result=rewrite_ratings(before_text,revised)
            if yaml.safe_load(result)!=after:
                raise ValueError(f"Unexpected non-rating data edit: {ident}")
            oldscore=weighted(old,weights)
            newscore=weighted(revised,weights)
            rows.append(dict(id=ident,country=country,slug=path.stem,
                             name=before["name"],old=float(oldscore),new=float(newscore)))
            changes.append((path,result))
    if len(rows)!=639 or set(custom)!=seen:
        raise ValueError(f"Incomplete audit: {len(rows)} records / {len(seen)} profiles")
    rated={r["id"]:r["new"] for r in rows}
    for a,b in (("city-at-vienna","city-at-salzburg"),
                ("city-at-salzburg","city-kh-phnom-penh"),
                ("city-kh-siem-reap","city-kh-phnom-penh"),
                ("city-vn-hoi-an","city-kh-phnom-penh"),
                ("city-cn-beijing","city-at-vienna"),
                ("city-kr-gyeongju","city-kh-phnom-penh")):
        if rated[a]<=rated[b]:
            raise ValueError(f"Cross-country anchor comparison failed: {a} <= {b}")
    for city in ("city-at-vienna","city-at-salzburg","city-cn-beijing",
                 "city-vn-hoi-an","city-kh-siem-reap","city-kh-phnom-penh"):
        row=next(r for r in rows if r["id"]==city)
        print(f"{city}: {row['old']:.2f} -> {row['new']:.2f}")
    print(f"Checked {len(rows)} cities and {len(seen)} individual comparison profiles.")
    if not args.apply:
        print("Dry-run: no writes. Use --apply only once.")
        return
    for path,data in changes:
        path.write_text(data,encoding="utf-8",newline="\n")
    REPORT.write_text(report(rows,custom),encoding="utf-8",newline="\n")
    MARKER.write_text(json.dumps({
        "review_date":"2026-11-22","scoring_version":2,"cities_reviewed":639,
        "manually_compared_benchmarks":104,"original_counts":COUNTS,
        "type":"irreversible historic one-time calibration; do not run for future data",
        "guide":"methodology/city-scoring-guide.md",
        "audit":"methodology/city-calibration-audit.md"
    },indent=2)+"\n",encoding="utf-8",newline="\n")
    print("Wrote 639 city YAML scores, complete audit and one-time guard marker.")


if __name__=="__main__":
    main()
