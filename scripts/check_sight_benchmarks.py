#!/usr/bin/env python3
"""Cross-country sight score regression diagnostics and approved benchmark pairs.

No national average quotas, rank-percentile quotas or automatic score edits.
Stable named examples guard against accidental re-introduction of
the 2026 over-inflation of ordinary attractions.
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
# Names are permanent editorial reference comparisons, not automated
# constraints on future NEW sites. Changes need explicit editorial review.
PAIRS = (
    ("CN", "great-wall-jinshanling", "AT", "schoenbrunn-palace", "3.0"),
    ("KH", "angkor-archaeological-park", "KH", "angkor-wat", "0.4"),
    ("KH", "angkor-wat", "AT", "hohensalzburg-fortress", "5.0"),
    ("AT", "hohensalzburg-fortress", "KH", "made-in-cambodia-market", "12.0"),
    ("AT", "hofburg-palace", "KH", "siem-reap-royal-gardens", "15.0"),
    ("VN", "ha-long-bay", "VN", "nha-trang-beach", "8.0"),
    ("TH", "ayutthaya-historical-park", "KH", "made-in-cambodia-market", "15.0"),
    ("KR", "gyeongju-historic-areas", "VN", "nha-trang-beach", "10.0"),
)


def main() -> int:
    scoring = json.loads(SCORING.read_text(encoding="utf-8"))
    weights = {key: Decimal(str(w)) for key, w in scoring["dimensions"].items()}
    registry = json.loads((COUNTRIES / "_registry.json").read_text(encoding="utf-8"))
    scores, grouped = {}, defaultdict(list)
    for code in registry["codes"]:
        for file in sorted((COUNTRIES / code / "sights").glob("*.yaml")):
            rec = yaml.safe_load(file.read_text(encoding="utf-8"))
            val = overall_score(rec, weights)
            if val is None:
                continue
            scores[code, file.stem] = val
            grouped[code].append(float(val))
    if not scores:
        raise SystemExit("No assessed sights found")
    print(f"Global sight comparison check: {len(scores)} assessed sights")
    for code, arr in sorted(grouped.items()):
        n90 = sum(x >= 90 for x in arr)
        print(f"  {code}: n={len(arr)}, mean={statistics.mean(arr):.2f}, "
              f"median={statistics.median(arr):.2f}, >=90={n90} "
              f"({n90/len(arr)*100:.1f}%)")
        if len(arr) >= 40 and n90 / len(arr) > 0.35:
            print(f"  REVIEW ADVISED: {code} has over 35% of assessed sights >=90. "
                  "This is NOT a cap or failing quota; verify site-type peers and "
                  "individual ratings to rule out batch inflation.")
    problems = []
    for lc, ls, rc, rs, minimum in PAIRS:
        a, b = scores.get((lc, ls)), scores.get((rc, rs))
        if a is None or b is None:
            problems.append(f"Missing documented anchor {lc}/{ls} or {rc}/{rs}")
            continue
        gap = a-b
        print(f"  {lc}/{ls}={a:.2f} vs {rc}/{rs}={b:.2f}: gap {gap:+.2f}")
        if gap < Decimal(minimum):
            problems.append(f"Worldwide sight peer comparison drift: "
                            f"{lc}/{ls} vs {rc}/{rs}, gap {gap:.2f} < {minimum}. "
                            "Reassess both sites and update benchmarks deliberately "
                            "when evidence supports changing the peer judgment.")
    if problems:
        for error in problems:
            print("ERROR: "+error, file=sys.stderr)
        return 1
    print("PASS: worldwide sight comparison benchmarks are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
