#!/usr/bin/env python3
"""Apply individually authored category decisions; never infer or adjust a score."""
from __future__ import annotations

import argparse
import collections
import copy
import json
import re
from decimal import Decimal
from pathlib import Path

import yaml
from rank import overall_score

ROOT = Path(__file__).resolve().parents[1]
FILES = ("empty-city-category-decisions-2026-11-28.json",
         "empty-sight-category-decisions-2026-11-28.json")
PEERS = {
    "history": "Pompeii (Italy), Angkor (Cambodia), Giza (Egypt), Tikal (Guatemala)",
    "architecture": "Angkor (Cambodia), Philae (Egypt), Teotihuacan (Mexico), Matera (Italy)",
    "culture": "Kyoto (Japan), Luang Prabang (Laos), Fez (Morocco), Oaxaca (Mexico)",
    "nature": "Galapagos (Ecuador), Namib Sand Sea (Namibia), Plitvice (Croatia), Cocos Island (Costa Rica)",
    "wildlife": "Serengeti (Tanzania), Okavango (Botswana), Aldabra (Seychelles), Banc d’Arguin (Mauritania)",
    "photography": "Namib Sand Sea (Namibia), Giza (Egypt), Svalbard (Norway), Zhangjiajie (China)",
    "food": "Bangkok (Thailand), Guangzhou (China), Osaka (Japan), Oaxaca (Mexico)",
    "beaches": "Seychelles, Whitehaven (Australia), Maldives, Zanzibar (Tanzania)",
    "adventure": "Baltoro Glacier (Pakistan), Wadi Rum (Jordan), Mount Roraima (Venezuela), Cocos Island (Costa Rica)",
}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write YAML and append review sections")
    args = ap.parse_args()
    meta = json.loads((ROOT / "methodology/scoring.json").read_text())
    weights = {k: Decimal(str(v)) for k, v in meta["dimensions"].items()}
    decisions = {}
    for name in FILES:
        for row in json.loads((ROOT / "methodology/reviews" / name).read_text(encoding="utf-8")):
            path = row["source"]
            if path in decisions:
                raise ValueError("Duplicate decision")
            decisions[path] = row
    if len(decisions) != 161:
        raise ValueError("Unexpected decision count")
    records = {}
    for p in (ROOT / "countries").glob("*/*/*.yaml"):
        if p.parent.name in ("cities", "sights"):
            data = yaml.safe_load(p.read_text(encoding="utf-8"))
            if not data["scores"].get("categories"):
                records[p.relative_to(ROOT).as_posix()] = data
    if set(records) != set(decisions):
        raise ValueError("Decision paths do not exactly match all current empty profiles")
    changes, reviews = {}, collections.defaultdict(list)
    count = linked = high = 0
    for path, row in sorted(decisions.items()):
        p = ROOT / path
        original = records[path]
        cats = row["categories"]
        if original["id"] != row["id"] or not cats or not row["rationale"].strip():
            raise ValueError("Invalid decision identity or rationale")
        if any(k not in meta["categories"] or type(v) not in (int, float) or not 0 <= v < 10
               for k, v in cats.items()):
            raise ValueError("Invalid category value")
        total = overall_score(original, weights)
        if total is None:
            raise ValueError("Unranked core record")
        urls = row["source_urls"]
        if (total >= 90 or any(v >= 9.5 for v in cats.values())) and not urls:
            raise ValueError("High-rated decision lacks source support: " + row["id"])
        high += total >= 90
        linked += bool(urls)
        text = p.read_text(encoding="utf-8")
        block = "  categories:\n" + "\n".join(f"    {k}: {v:.1f}" for k, v in cats.items())
        updated, n = re.subn(r"^  categories: \{\}[ \t]*$", lambda _: block, text, flags=re.M)
        if n != 1:
            raise ValueError("Unexpected source YAML representation: " + row["id"])
        expected = copy.deepcopy(original)
        expected["scores"]["categories"] = cats
        assert yaml.safe_load(updated) == expected
        assert overall_score(expected, weights) == total
        changes[p] = updated
        parts = Path(path).parts
        doc = ROOT / "methodology/reviews" / parts[1] / (parts[2] + ".md")
        label = "source-linked-unverified" if urls else "editorial-only"
        source = "Indexed source excerpts reviewed 2026-11-28: " + "; ".join(urls) if urls else "Desk-based provisional judgment, no independent factual verification."
        # These are category-level qualitative comparison leads, not new peer assessments.
        peer = PEERS[next(iter(cats))]
        scores = ", ".join(f"{k} {v:.1f}" for k, v in cats.items())
        reviews[doc].append(f"\n\n## {row['id']} — 2026-11-28 empty category profile completion\n\n"
                            f"- [YAML](../../../{path}) · **{label}** · Action: complete category profile.\n"
                            f"- Assigned: {scores}. {row['rationale']}\n"
                            f"- {source}\n"
                            f"- Qualitative comparison leads for the primary category (not individually recalibrated): {peer}.\n"
                            f"- Core overall {total:.2f}/100 retained; all other fields unchanged. Unselected categories are not asserted applicable. No current access or encounter guarantee.\n")
        count += len(cats)
    outputs = {}
    for doc, sections in reviews.items():
        old = doc.read_text(encoding="utf-8") if doc.exists() else "# Individual destination reviews\n"
        if "2026-11-28 empty category profile completion" in old:
            raise ValueError("Category completion already applied to review file")
        outputs[doc] = old.rstrip() + "".join(sections)
    if args.apply:
        for p, content in {**changes, **outputs}.items():
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
    print(json.dumps({"profiles": len(changes), "new_category_scores": count,
                      "review_files": len(outputs), "source_linked": linked,
                      "editorial_only": len(changes)-linked, "overall_90_plus": high,
                      "applied": args.apply}, sort_keys=True))


if __name__ == "__main__":
    main()
