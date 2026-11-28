#!/usr/bin/env python3
"""Reconcile the historical incomplete inventory with current source YAML.

Historical batch documents are immutable research snapshots, not a live queue.
This script never edits source records or asserts that a score is fact-checked.
"""
from __future__ import annotations
import argparse
import collections
import csv
import io
import json
import re
import subprocess
from decimal import Decimal
from pathlib import Path

import yaml
from rank import overall_score

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "d69bfe1532605e1136ab38f9b268f92809ba0109"
BATCH = re.compile(r"\.\./countries/([A-Z]{2}/(?:cities|sights)/[^)]+\.yaml)")
FIELDS = ("source", "id", "name", "area", "kind", "missing_core",
          "current_status", "overall", "historical_batch", "historical_disposition")


def historical_inventory(root):
    paths = sorted((root / "methodology").glob("worldwide-incomplete-batch-100*-2026-11-26.md"))
    paths += [root / "methodology/worldwide-incomplete-batch-final-90-pass23-2026-11-26.md"]
    if len(paths) != 16:
        raise ValueError(f"Expected 16 original batches, got {len(paths)}")
    found = {}
    for path in paths:
        count = 0
        for line in path.read_text(encoding="utf-8").splitlines():
            match = BATCH.search(line)
            if not match:
                continue
            source = "countries/" + match.group(1)
            cells = line.strip().strip("|").split("|")
            if len(cells) < 5 or not line.startswith("|"):
                raise ValueError(f"Unrecognized row: {path.name}: {line}")
            if source in found:
                raise ValueError(f"Duplicate original record: {source}")
            found[source] = (path.name, cells[4].strip())
            count += 1
        expected = 90 if "final-90" in path.name else 100
        if count != expected:
            raise ValueError(f"{path.name}: {count} rows, expected {expected}")
    if len(found) != 1590:
        raise ValueError(f"Expected 1590 original records, got {len(found)}")
    return found


def verify_baseline(root, inventory):
    raw = subprocess.check_output(
        ["git", "show", BASELINE + ":methodology/worldwide-diagnostics/records.tsv"],
        cwd=root, text=True,
    )
    baseline = {
        row["source"] for row in csv.DictReader(io.StringIO(raw), delimiter="\t")
        if "incomplete-core" in row["flags"].split(";")
    }
    if set(inventory) != baseline:
        raise ValueError("Historical batches do not match the original diagnostic")


def numeric(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def collect(root, historical):
    metadata = json.loads((root / "methodology/scoring.json").read_text(encoding="utf-8"))
    weights = {key: Decimal(str(value)) for key, value in metadata["dimensions"].items()}
    records = []
    sources = {}
    ids = set()
    for path in sorted((root / "countries").glob("*/*/*.yaml")):
        if path.parent.name not in {"cities", "sights"}:
            continue
        source = path.relative_to(root).as_posix()
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if data["id"] in ids:
            raise ValueError(f"Duplicate source ID: {data['id']}")
        ids.add(data["id"])
        scores = data.get("scores") or {}
        missing = [key for key in weights if not numeric(scores.get(key))]
        overall = overall_score(data, weights)
        if (overall is None) != bool(missing):
            raise ValueError(f"Ranking and missing-field logic disagree: {source}")
        batch, disposition = historical.get(source, ("", ""))
        row = dict(source=source, id=data["id"], name=data["name"],
                   area=path.parent.parent.name, kind=path.parent.name,
                   missing_core=";".join(missing),
                   current_status="incomplete" if missing else "complete",
                   overall="" if overall is None else f"{overall:.2f}",
                   historical_batch=batch, historical_disposition=disposition)
        sources[source] = row
        records.append(row)
    absent = set(historical) - set(sources)
    if absent:
        raise ValueError(f"Original source paths missing; reconcile moves explicitly: {sorted(absent)}")
    return records


def outputs(records, historical):
    original = [row for row in records if row["source"] in historical]
    pending = [row for row in records if row["current_status"] == "incomplete"]
    resolved = [row for row in original if row["current_status"] == "complete"]
    original_pending = [row for row in pending if row["source"] in historical]
    new_pending = len(pending) - len(original_pending)
    stale = [row for row in resolved if
             any(word in row["historical_disposition"].lower()
                 for word in ("deferred", "retain unranked"))]
    area_counts = collections.Counter(row["area"] for row in pending)
    dim_counts = collections.Counter(dim for row in pending for dim in row["missing_core"].split(";"))
    by_batch = collections.defaultdict(collections.Counter)
    for row in original:
        by_batch[row["historical_batch"]][row["current_status"]] += 1

    lines = [
        "# Live worldwide incomplete-rating backlog", "",
        "Generated from current source YAML and the original historical batch inventory.",
        "A complete numeric rating is not proof of independent fact-checking.",
        "Historical dispositions are retained verbatim; overlapping scopes still require editorial review.", "",
        f"- Current source records: **{len(records):,}**",
        f"- Complete core ratings: **{len(records)-len(pending):,}**",
        f"- All incomplete core ratings: **{len(pending):,}**",
        f"- Original inventory resolved: **{len(resolved):,} / {len(historical):,}**",
        f"- Original inventory still incomplete: **{len(original_pending):,}**",
        f"- Incomplete outside original inventory: **{new_pending:,}**",
        f"- Complete records historically labeled deferred or retain unranked: **{len(stale):,}**", "",
        "Use [remaining.tsv](remaining.tsv) as the current research queue.",
        "Use [original-inventory.tsv](original-inventory.tsv) to reconcile historical labels.",
        "Use [historical-deferral-review.tsv](historical-deferral-review.tsv) for completed records with historical deferrals, ordered by descending current score.",
        "This is a triage list, not a determination that the current evidence status is stale or incorrect.",
        "The latter does not change historical review decisions or certify public access.", "",
        "## Remaining by area", "", "| Area | Incomplete |", "| --- | ---: |",
    ]
    lines += [f"| {area} | {count} |" for area, count in sorted(area_counts.items(), key=lambda x: (-x[1], x[0]))]
    lines += ["", "## Missing scoring fields", "", "| Dimension | Missing |", "| --- | ---: |"]
    lines += [f"| {dim} | {count} |" for dim, count in sorted(dim_counts.items())]
    lines += ["", "## Original batches", "", "| Batch | Complete now | Incomplete now |", "| --- | ---: | ---: |"]
    lines += [f"| {batch} | {counts['complete']} | {counts['incomplete']} |" for batch, counts in sorted(by_batch.items())]
    def tsv(rows):
        stream = io.StringIO(newline="")
        writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
        return stream.getvalue()
    return {"README.md": "\n".join(lines) + "\n",
            "remaining.tsv": tsv(pending),
            "original-inventory.tsv": tsv(original),
            "historical-deferral-review.tsv": tsv(sorted(stale, key=lambda row: (-Decimal(row["overall"]), row["source"])))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files differ")
    parser.add_argument("--verify-baseline", action="store_true", help="compare to original Git snapshot")
    args = parser.parse_args()
    historical = historical_inventory(ROOT)
    if args.verify_baseline:
        verify_baseline(ROOT, historical)
    generated = outputs(collect(ROOT, historical), historical)
    target = ROOT / "methodology/worldwide-backlog"
    if args.check:
        different = [name for name, value in generated.items()
                     if not (target / name).exists() or (target / name).read_text(encoding="utf-8") != value]
        if different:
            raise SystemExit("Stale or missing generated files: " + ", ".join(different))
    else:
        target.mkdir(parents=True, exist_ok=True)
        for name, value in generated.items():
            (target / name).write_text(value, encoding="utf-8")
    print(generated["README.md"].split("## Remaining by area")[0])


if __name__ == "__main__":
    main()
