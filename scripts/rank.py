#!/usr/bin/env python3
"""Print country or worldwide rankings directly from source YAML files.

No generated rank files are created. Scores come from methodology/scoring.json.
"""
from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
COUNTRIES = ROOT / "countries"
METHODOLOGY = ROOT / "methodology" / "scoring.json"


def overall_score(data: dict[str, Any], weights: dict[str, Decimal]) -> Decimal | None:
    scores = data.get("scores")
    if not isinstance(scores, dict):
        return None
    total = Decimal("0")
    for dimension, weight in weights.items():
        value = scores.get(dimension)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return None
        total += Decimal(str(value)) * weight
    return total * 10


def category_score(data: dict[str, Any], category: str) -> Decimal | None:
    scores = data.get("scores")
    if not isinstance(scores, dict) or not isinstance(scores.get("categories"), dict):
        return None
    value = scores["categories"].get(category)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return Decimal(str(value))


def ranked_destinations(
    codes: list[str],
    kinds: list[str],
    weights: dict[str, Decimal],
    category: str | None,
) -> list[tuple[Decimal, str, str, str]]:
    results: list[tuple[Decimal, str, str, str]] = []
    for code in codes:
        for kind in kinds:
            folder = COUNTRIES / code / kind
            if not folder.is_dir():
                continue
            for path in sorted(folder.glob("*.yaml")):
                data = yaml.safe_load(path.read_text(encoding="utf-8"))
                if not isinstance(data, dict):
                    continue
                score = (category_score(data, category) if category is not None
                         else overall_score(data, weights))
                if score is None:
                    continue
                results.append((score, data["name"], code, kind))
    results.sort(key=lambda x: (-x[0], x[1].casefold(), x[2], x[3]))
    return results


def main() -> int:
    metadata = json.loads(METHODOLOGY.read_text(encoding="utf-8"))
    registry = json.loads((COUNTRIES / "_registry.json").read_text(encoding="utf-8"))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--country", type=str.upper, choices=registry["codes"],
                        help="Two-letter country code; omit to rank all populated countries")
    parser.add_argument("--kind", choices=("cities", "sights", "all"), default="all")
    parser.add_argument("--category", choices=metadata["categories"],
                        help="Rank by a category score instead of the universal overall score")
    parser.add_argument("--limit", type=int, default=25, help="Maximum displayed results (default 25)")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be at least 1")
    codes = [args.country] if args.country else registry["codes"]
    kinds = ["cities", "sights"] if args.kind == "all" else [args.kind]
    weights = {key: Decimal(str(weight)) for key, weight in metadata["dimensions"].items()}
    ranked = ranked_destinations(codes, kinds, weights, args.category)
    dimension = args.category if args.category else "overall"
    scope = args.country or "all populated countries"
    print(f"{scope} | {args.kind} | {dimension} | {len(ranked)} assessed destinations")
    previous_score: Decimal | None = None
    place = 0
    for index, (score, name, code, kind) in enumerate(ranked[:args.limit], 1):
        if previous_score is None or score != previous_score:
            place = index
        previous_score = score
        formatted = score.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        max_score = 10 if args.category else 100
        print(f"{place:>3}. {name} ({code}, {kind}) — {formatted}/{max_score}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
