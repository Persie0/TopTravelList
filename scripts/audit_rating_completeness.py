#!/usr/bin/env python3
"""Inventory missing numeric scores without inventing ratings or exposing private data.

An omitted category is not an explicit unassessed category. Empty category
profiles are a separate review queue. Historical dispositions remain immutable.
"""
from __future__ import annotations

import argparse
import collections
import csv
import io
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DIMS = ("impact", "uniqueness", "significance", "experience", "depth")


def numeric(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and 0 <= value <= 10


def tsv(fields, rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def generate(root):
    counts = collections.Counter()
    by_category = collections.Counter()
    incomplete, categories, empty = [], [], []
    seen = set()
    for p in sorted((root / "countries").glob("*/*/*.yaml")):
        if p.parent.name not in ("cities", "sights"):
            continue
        data = yaml.safe_load(p.read_text(encoding="utf-8"))
        if data["id"] in seen:
            raise ValueError("Duplicate destination ID: " + data["id"])
        seen.add(data["id"])
        counts["destinations"] += 1
        scores = data["scores"]
        cats = scores.get("categories") or {}
        row = {"source": p.relative_to(root).as_posix(), "id": data["id"],
               "name": data["name"], "area": p.parent.parent.name, "kind": p.parent.name}
        missing = [key for key in DIMS if not numeric(scores.get(key))]
        if missing:
            incomplete.append(dict(row, fields=";".join(missing)))
            counts["incomplete_core_records"] += 1
            counts["incomplete_core_fields"] += len(missing)
        if not cats:
            empty.append(row)
            counts["empty_category_profiles"] += 1
        unresolved = [key for key, value in sorted(cats.items()) if not numeric(value)]
        if unresolved:
            counts["records_with_unassessed_categories"] += 1
            for key in unresolved:
                counts["unassessed_category_fields"] += 1
                by_category[key] += 1
                categories.append(dict(row, category=key, existing_profile=json.dumps(cats, sort_keys=True),
                                       core=";".join(str(scores.get(d)) for d in DIMS)))
    fields = ("source", "id", "name", "area", "kind")
    keys = ("destinations", "incomplete_core_records", "incomplete_core_fields",
            "records_with_unassessed_categories", "unassessed_category_fields", "empty_category_profiles")
    for key in keys:
        counts[key] += 0
    summary = ["# Live numeric rating completeness", "",
               "Generated from current destination YAML. Numerical completeness is not fact verification.",
               "Omitted categories are not automatically applicable; empty category profiles are a separate editorial queue.", ""]
    summary += [f"- {key.replace('_', ' ').capitalize()}: **{counts[key]:,}**" for key in keys]
    summary += ["", "## Explicitly unassessed categories", "", "| Category | Fields |", "| --- | ---: |"]
    summary += [f"| {key} | {count} |" for key, count in sorted(by_category.items())]
    summary += ["", "## Queues", "", "- [Incomplete core](incomplete-core.tsv)",
                "- [Explicitly unassessed categories](unassessed-categories.tsv)",
                "- [Empty category profiles](empty-category-profiles.tsv)", ""]
    return dict(counts), {"README.md": "\n".join(summary),
        "incomplete-core.tsv": tsv(fields + ("fields",), incomplete),
        "unassessed-categories.tsv": tsv(fields + ("category", "existing_profile", "core"), categories),
        "empty-category-profiles.tsv": tsv(fields, empty)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    counts, files = generate(ROOT)
    target = ROOT / "methodology/rating-completeness"
    if args.check:
        if any(not (target / name).exists() or (target / name).read_text(encoding="utf-8") != content
               for name, content in files.items()):
            raise SystemExit("Stale rating-completeness inventory")
    else:
        target.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            (target / name).write_text(content, encoding="utf-8")
    print(json.dumps(counts, sort_keys=True))


if __name__ == "__main__":
    main()
