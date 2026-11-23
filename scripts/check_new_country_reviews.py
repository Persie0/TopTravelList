#!/usr/bin/env python3
"""Assert destination YAML has one individually named Markdown review, not fact-check claims."""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADER = re.compile(r"^## (city|sight)-([a-z]{2})-([a-z0-9]+(?:-[a-z0-9]+)*)\s+[—-]\s+", re.M)
STATUS = ("fact-checked", "source-linked-unverified", "editorial-only", "unassessed")
PEER = ("worldwide peer", "Worldwide peer", "worldwide comparators", "international score comparison",
        "international benchmark", "cross-country peers", "world peers", "Four worldwide", "Four international")

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--country", required=True, type=str.upper)
    code = p.parse_args().country
    if not re.fullmatch(r"[A-Z]{2}", code):
        p.error("country must be a two-letter code")
    base = ROOT / "countries" / code
    notes = ROOT / "methodology" / "reviews" / code
    errors = []
    for folder, prefix in (("cities", "city"), ("sights", "sight")):
        source = {prefix + "-" + code.lower() + "-" + f.stem for f in (base / folder).glob("*.yaml")}
        docs = [notes / "cities.md"] if folder == "cities" else sorted(notes.glob("sights-*.md"))
        if folder == "sights" and not docs:
            docs = [notes / "sights.md"]
        seen = set()
        for path in docs:
            if not path.is_file():
                errors.append(f"missing {path}")
                continue
            data = path.read_text(encoding="utf-8")
            matches = list(HEADER.finditer(data))
            for i, m in enumerate(matches):
                ident = "-".join(m.groups())
                section = data[m.end():(matches[i+1].start() if i+1<len(matches) else len(data))]
                if ident in seen:
                    errors.append(f"duplicate review: {ident}")
                seen.add(ident)
                if m.group(1) != prefix or m.group(2).upper() != code:
                    errors.append(f"bad review kind/country: {ident}")
                if not any(t in section for t in STATUS):
                    errors.append(f"evidence status missing: {ident}")
                if not all(t in section for t in ("Impact", "Uniqueness", "Significance", "Experience", "Depth")):
                    errors.append(f"five field rationales missing: {ident}")
                if not any(t in section for t in PEER):
                    errors.append(f"international peers missing: {ident}")
        missing, extra = source-seen, seen-source
        if missing:
            errors.append(f"{folder}: {len(missing)} unreviewed: {sorted(missing)[:10]}")
        if extra:
            errors.append(f"{folder}: {len(extra)} unpaired reviews: {sorted(extra)[:10]}")
        print(f"{code} {folder}: {len(source)} YAML / {len(seen)} named reviews")
    if errors:
        for err in errors:
            print("ERROR:", err, file=sys.stderr)
        return 1
    print("PASS: reviews cover every source record; factual verification not checked.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
