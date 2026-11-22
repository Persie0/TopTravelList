#!/usr/bin/env python3
"""Regression guard for cross-country city scoring benchmarks.

Does not set scores, enforce national quotas, or restrict a future exceptional
city from outranking reference cities. Checks a few review-approved comparison
pairs to catch accidental benchmark drift and reports city-score distribution.
"""
from __future__ import annotations

import json
import statistics
import sys
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

import yaml
from rank import overall_score

ROOT = Path(__file__).resolve().parents[1]
COUNTRIES = ROOT / "countries"
SCORING = ROOT / "methodology/scoring.json"
PAIRS = (
    ("AT", "vienna", "AT", "salzburg", 1.0),
    ("AT", "salzburg", "KH", "phnom-penh", 5.0),
    ("CN", "beijing", "AT", "vienna", 1.0),
    ("KH", "siem-reap", "KH", "phnom-penh", 5.0),
    ("VN", "hoi-an", "KH", "phnom-penh", 5.0),
    ("KR", "gyeongju", "KH", "phnom-penh", 5.0),
)


def main() -> int:
    weights = {k: Decimal(str(v)) for k, v in
               json.loads(SCORING.read_text(encoding="utf-8"))["dimensions"].items()}
    registry = json.loads((COUNTRIES / "_registry.json").read_text(encoding="utf-8"))
    scores, by_country = {}, defaultdict(list)
    for country in registry["codes"]:
        for path in sorted((COUNTRIES / country / "cities").glob("*.yaml")):
            rec = yaml.safe_load(path.read_text(encoding="utf-8"))
            value = overall_score(rec, weights)
            if value is None:
                continue
            scores[(country,path.stem)] = value
            by_country[country].append(float(value))
    if not scores:
        raise SystemExit("No assessed city scores")
    print(f"Worldwide city review: {len(scores)} assessed records")
    print("Country means and medians below are DIAGNOSTICS ONLY; they are not quota targets:")
    for country, values in sorted(by_country.items()):
        print(f"  {country}: n={len(values)}, mean={statistics.mean(values):.2f}, "
              f"median={statistics.median(values):.2f}, >=90={sum(v>=90 for v in values)}")
        if len(values)>=15 and statistics.mean(values)>84:
            print(f"  REVIEW RECOMMENDED: {country} mean >84 for {len(values)} records; "
                  "confirm global peer comparisons, not country-relative scoring")
    errors=[]
    for left_code,left_slug,right_code,right_slug,min_gap in PAIRS:
        left=scores.get((left_code,left_slug))
        right=scores.get((right_code,right_slug))
        if left is None or right is None:
            errors.append(f"Missing reference: {left_code}/{left_slug} or {right_code}/{right_slug}")
            continue
        gap=left-right
        print(f"  {left_code}/{left_slug} {float(left):.2f} vs "
              f"{right_code}/{right_slug} {float(right):.2f} "
              f"(gap {float(gap):+.2f})")
        if gap<Decimal(str(min_gap)):
            errors.append(f"Benchmark drift: {left_code}/{left_slug} should exceed "
                          f"{right_code}/{right_slug} by at least {min_gap}. "
                          "Review the editorial comparison, and update the benchmark "
                          "documentation deliberately if it genuinely changed.")
    if errors:
        for error in errors:
            print("ERROR: "+error,file=sys.stderr)
        return 1
    print("PASS: explicit cross-country benchmark comparisons hold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
