#!/usr/bin/env python3
"""One-time v1 -> v2 worldwide rating migration.

Converts inflated first-pass scores into a conservative GLOBAL scale.
Run once with --apply on a v1 dataset; v2 datasets are intentionally refused.
Location, destination identity, and the original YAML field layout are preserved.
"""
from __future__ import annotations

import argparse
import json
import re
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
COUNTRIES = ROOT / "countries"
SCORING_PATH = ROOT / "methodology" / "scoring.json"
CORE = ("impact", "uniqueness", "significance", "experience", "depth")
CATEGORIES = (
    "nature", "architecture", "history", "culture", "food", "beaches",
    "wildlife", "adventure", "nightlife", "photography", "family", "relaxation",
)

# Original 10/10 no longer implies a worldwide 10/10. A worldwide 10 must
# be EXPLICITLY nominated below, with a comparison against global peers.
# Lower score anchors maintain the same relative ordering as the old scale.
# Conversion uses linear interpolation and one-decimal ROUND_HALF_UP.
CURVE = (
    ("0", "0"), ("2", "1.6"), ("4", "3.4"), ("5", "4.3"),
    ("6", "5.2"), ("7", "6.1"), ("8", "7.0"), ("8.5", "7.5"),
    ("9", "8.0"), ("9.5", "8.5"), ("10", "9.0"),
)

# Explicit global cross-country exemplars, NOT country champions.
# Format: destination ID | impact,uniqueness,significance,experience,depth
#         | category overrides (optional). 10 is reserved for world-leading
# exemplars, not awarded automatically to the highest-scoring record in CN.
OVERRIDES = """
city-cn-beijing|9.8,9.8,9.9,9.7,10|architecture:9.8,history:9.9,culture:9.9
city-cn-xi-an|9.5,9.6,9.9,9.5,9.5|history:9.9
city-cn-hong-kong|9.5,9.7,9.4,9.5,9.8|architecture:9.8,photography:9.8
city-cn-lhasa|9.4,9.8,9.9,9.0,9.1|history:9.9,culture:9.9
city-cn-shanghai|9.5,9.4,9.3,9.6,9.9|architecture:9.6
city-cn-chengdu|9.3,9.2,9.3,9.6,9.8|food:9.8
city-cn-guangzhou|9.1,9.3,9.2,9.5,9.6|food:10
city-cn-suzhou|9.3,9.5,9.5,9.5,9.3|architecture:9.7
city-cn-kashgar|9.2,9.6,9.6,9.3,9.1|history:9.7,culture:9.8
city-cn-dunhuang|9.2,9.5,9.7,9.2,8.9|history:9.9
city-cn-pingyao|9.0,9.6,9.8,9.2,8.7|history:9.7
city-cn-lijiang|9.1,9.4,9.5,9.2,9.2|architecture:9.5
city-at-vienna|9.0,8.8,9.4,9.2,9.2|architecture:9.3,history:9.5,culture:9.5
city-at-salzburg|8.8,8.5,9.0,9.0,8.5|architecture:9.1
city-th-bangkok|9.3,9.3,9.2,9.6,9.8|food:10,nightlife:9.8
city-th-chiang-mai|8.9,8.8,8.9,9.2,9.2|culture:9.3
city-th-ayutthaya|9.0,9.4,9.7,9.2,8.6|history:9.7
city-kr-seoul|9.2,9.2,9.2,9.6,9.8|culture:9.7,food:9.5
city-kr-gyeongju|9.0,9.4,9.5,9.2,9.1|history:9.7
city-kr-busan|9.0,8.9,8.8,9.3,9.4|food:9.3
sight-cn-great-wall-jinshanling|10,10,10,9.8,9.2|architecture:10,history:10,photography:10
sight-cn-great-wall-mutianyu|9.9,9.8,9.9,9.8,9.1|architecture:9.9,history:9.9,photography:9.9
sight-cn-forbidden-city|9.9,9.9,10,9.8,9.5|architecture:10,history:10,culture:10
sight-cn-terracotta-army|9.9,10,10,9.7,9.1|history:10,culture:9.9
sight-cn-temple-of-heaven|9.6,9.8,9.9,9.7,9.2|architecture:9.8,history:9.9
sight-cn-summer-palace|9.6,9.8,9.9,9.7,9.4|architecture:9.8,history:9.9
sight-cn-mount-huangshan|9.9,9.9,9.6,9.8,9.3|nature:10,photography:10
sight-cn-jiuzhaigou-valley|9.8,9.7,9.4,9.8,9.0|nature:10,photography:9.9
sight-cn-zhangjiajie-national-forest-park|9.8,9.7,9.3,9.8,9.3|nature:9.9,photography:9.9
sight-cn-li-river-guilin|9.8,9.7,9.3,9.8,9.0|nature:9.9,photography:9.9
sight-cn-mogao-caves|9.8,9.9,9.9,9.6,9.4|architecture:9.9,history:9.9,culture:9.9
sight-cn-yungang-grottoes|9.7,9.8,9.9,9.6,9.2|history:9.9
sight-cn-longmen-grottoes|9.8,9.9,9.9,9.7,9.3|history:9.9,architecture:9.9
sight-cn-pingyao-ancient-city|9.3,9.5,9.7,9.5,9.1|architecture:9.6,history:9.7
sight-cn-potala-palace|9.8,9.9,9.9,9.4,9.2|architecture:9.9,history:9.9
sight-cn-mount-everest-north-base-camp|9.7,9.9,9.7,9.0,8.4|nature:9.9,adventure:9.7
sight-cn-great-wall-jiankou|9.8,9.8,9.7,9.2,8.7|architecture:9.9,history:9.7
sight-cn-wudang-mountains|9.5,9.6,9.9,9.5,9.3|history:9.9
sight-cn-fujian-tulou-yongding|9.7,9.9,9.8,9.6,9.0|architecture:9.9
sight-cn-gulangyu-island|9.4,9.6,9.5,9.6,9.4|architecture:9.5
sight-cn-dujiangyan-irrigation-system|9.5,9.9,9.9,9.6,9.3|history:9.9,architecture:9.7
sight-cn-hongyadong|9.2,9.5,8.3,9.3,8.5|architecture:9.4,photography:9.7
sight-cn-xian-city-wall|9.5,9.6,9.8,9.5,9.0|architecture:9.7
sight-cn-stone-forest-shilin|9.6,9.8,9.5,9.6,9.0|nature:9.8
sight-cn-mount-kailash|9.6,9.8,9.8,8.8,9.0|nature:9.9
sight-cn-qinghai-lake|9.5,9.5,9.2,9.3,9.3|nature:9.7
sight-cn-kanas-lake|9.5,9.7,9.2,9.5,9.1|nature:9.8
sight-cn-harbin-ice-snow-world|9.2,9.5,9.0,9.5,9.2|architecture:9.7
sight-cn-zhangye-danxia|9.6,9.8,9.0,9.6,9.0|nature:9.8
sight-cn-dazu-rock-carvings|9.6,9.9,9.9,9.4,9.2|history:9.9
sight-cn-sanxingdui-museum|9.7,9.9,9.9,9.6,9.4|history:9.9,culture:9.9
sight-cn-victoria-harbour|9.7,9.7,9.3,9.8,9.6|photography:9.9
sight-cn-historic-centre-macau|9.5,9.7,9.8,9.6,9.3|history:9.9,architecture:9.7
sight-at-schoenbrunn-palace|9.0,8.8,9.4,9.2,8.9|architecture:9.4,history:9.3
sight-at-hohe-tauern-national-park|9.2,9.0,8.9,9.5,9.4|nature:9.5,photography:9.4
sight-at-grossglockner-high-alpine-road|9.2,9.0,8.6,9.4,8.7|nature:9.4,photography:9.6
sight-th-ayutthaya-historical-park|9.4,9.5,9.8,9.5,9.4|history:9.9,architecture:9.7
sight-th-sukhothai-historical-park|9.3,9.5,9.8,9.5,9.2|history:9.9
sight-th-khao-sok-national-park|9.4,9.4,9.0,9.5,9.3|nature:9.8,adventure:9.5
sight-th-phang-nga-bay|9.4,9.4,8.7,9.5,9.2|nature:9.7,photography:9.9
sight-th-wat-phra-kaew|9.2,9.3,9.7,9.5,8.9|architecture:9.7,history:9.7
sight-th-koh-kradan|9.0,9.2,7.4,9.5,8.4|beaches:9.8
sight-kr-changdeokgung-palace|9.2,9.4,9.7,9.4,9.3|architecture:9.6,history:9.7
sight-kr-gyeongju-historic-areas|9.2,9.5,9.8,9.5,9.5|history:9.8
sight-kr-bulguksa-temple|9.2,9.5,9.8,9.5,9.1|architecture:9.6,history:9.7
sight-kr-seoraksan-national-park|9.3,9.4,8.9,9.5,9.3|nature:9.6,adventure:9.5
sight-kr-hallasan-national-park|9.3,9.4,9.2,9.5,9.2|nature:9.7
sight-kr-jeju-island|9.3,9.2,9.0,9.6,9.6|nature:9.7
""".strip()


def to_tenth(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)


def calibrate(value: int | float | None) -> int | float | None:
    if value is None:
        return None
    val = Decimal(str(value))
    anchors = [(Decimal(a), Decimal(b)) for a, b in CURVE]
    if not Decimal(0) <= val <= Decimal(10):
        raise ValueError(f"Invalid original score: {value}")
    for (x0, y0), (x1, y1) in zip(anchors, anchors[1:]):
        if x0 <= val <= x1:
            result = to_tenth(y0 + (val - x0) * (y1 - y0) / (x1 - x0))
            return float(result)
    raise AssertionError(f"Unreachable score: {value}")


def parse_overrides() -> dict[str, tuple[list[float], dict[str, float]]]:
    result: dict[str, tuple[list[float], dict[str, float]]] = {}
    for line in OVERRIDES.splitlines():
        if not line.strip() or "placeholder" in line:
            continue
        ident, core_text, cats_text = line.split("|")
        if ident in result:
            raise ValueError("Repeated override: " + ident)
        core = [float(s) for s in core_text.split(",")]
        cats = {}
        for part in filter(None, cats_text.split(",")):
            name, score = part.split(":")
            if name not in CATEGORIES:
                raise ValueError(f"Unknown category {name} in {ident}")
            cats[name] = float(score)
        if len(core) != len(CORE) or any(not 0 <= n <= 10 for n in [*core, *cats.values()]):
            raise ValueError("Invalid override: " + ident)
        result[ident] = core, cats
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write the one-time migration")
    args = parser.parse_args()

    metadata = json.loads(SCORING_PATH.read_text(encoding="utf-8"))
    if metadata.get("version") != 1:
        raise SystemExit("Only v1 source files can be migrated. Refusing to rerun on v2.")
    overrides = parse_overrides()
    pending = []
    anchored: dict[str, set[str]] = {k: set() for k in (*CORE, *CATEGORIES)}
    count = 0
    observed = set()
    original_tens = 0

    for folder in sorted(COUNTRIES.glob("[A-Z][A-Z]")):
        for kind in ("cities", "sights"):
            for path in sorted((folder / kind).glob("*.yaml")):
                text = path.read_text(encoding="utf-8")
                record = yaml.safe_load(text)
                ident = record["id"]
                expected = ("city" if kind == "cities" else "sight") + "-" + folder.name.lower() + "-" + path.stem
                if ident != expected or ident in observed:
                    raise ValueError(f"Bad or repeated ID in {path}: {ident}")
                observed.add(ident)
                count += 1
                scores = record["scores"]
                core_ratings = {k: calibrate(scores[k]) for k in CORE}
                category_ratings = {k: calibrate(v) for k, v in scores["categories"].items()}
                original_tens += sum(scores[k] == 10 for k in CORE)
                original_tens += sum(v == 10 for v in scores["categories"].values())
                if ident in overrides:
                    custom_core, custom_cats = overrides[ident]
                    core_ratings.update(zip(CORE, custom_core))
                    for k, v in custom_cats.items():
                        if k not in category_ratings:
                            raise ValueError(f"Override references absent category: {ident}/{k}")
                        category_ratings[k] = v
                # No accidental 10s: only explicitly named global benchmark overrides.
                for k, v in {**core_ratings, **category_ratings}.items():
                    if v == 10:
                        anchored[k].add(ident)
                lines = text.splitlines(keepends=True)
                changes = set()
                new_lines = []
                for line in lines:
                    m_core = re.fullmatch(r"(  (impact|uniqueness|significance|experience|depth): )([^\r\n]+)(\r?\n?)", line)
                    m_cat = re.fullmatch(r"(    ([a-z]+): )([^\r\n]+)(\r?\n?)", line)
                    match = m_core or m_cat
                    if match:
                        key = match.group(2)
                        target = (core_ratings if m_core else category_ratings)
                        if key not in target:
                            raise ValueError(f"Unexpected rating key {key} in {path}")
                        new_val = target[key]
                        formatted = "null" if new_val is None else f"{new_val:.1f}"
                        new_lines.append(match.group(1) + formatted + match.group(4))
                        changes.add(("core" if m_core else "category", key))
                    else:
                        new_lines.append(line)
                expect_changes = {("core", k) for k in CORE} | {("category", k) for k in category_ratings}
                if changes != expect_changes:
                    raise ValueError(f"Could not match all scores in {path}: {expect_changes - changes}")
                new_text = "".join(new_lines)
                updated = yaml.safe_load(new_text)
                if updated["location"] != record["location"] or updated["name"] != record["name"] or updated["id"] != ident:
                    raise ValueError(f"Unintended identity/location change in {path}")
                pending.append((path, new_text))
    if count != 1540:
        raise ValueError(f"Expected 1540 existing destinations before migration, found {count}")
    if not set(overrides).issubset(observed):
        raise ValueError("Missing benchmark destinations: " + ", ".join(sorted(set(overrides) - observed)))

    metadata["version"] = 2
    metadata["global_ten_anchors"] = {k: sorted(ids) for k, ids in anchored.items() if ids}
    # For review: every 10 must belong to the explicit override list.
    if any(not ids.issubset(overrides) for ids in anchored.values()):
        raise ValueError("Non-benchmark 10 found")
    print(f"Files: {count}; original 10/10 fields: {original_tens}")
    print("New worldwide 10/10 benchmark assignments:")
    for key, ids in anchored.items():
        if ids:
            print(f"  {key}: {', '.join(sorted(ids))}")
    if not args.apply:
        print("Dry run; no files changed. Pass --apply to execute.")
        return 0
    for path, new_content in pending:
        path.write_text(new_content, encoding="utf-8")
    SCORING_PATH.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Migrated {count} destination files; global scoring version is now 2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
