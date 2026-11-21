#!/usr/bin/env python3
"""Create the country/cities and country/sights folders from the registry."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "countries" / "_registry.json"


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    codes = registry["codes"]
    if len(codes) != 197 or len(codes) != len(set(codes)):
        raise ValueError("Expected 197 unique country codes in the registry")
    if codes != sorted(codes) or any(not re.fullmatch(r"[A-Z]{2}", c) for c in codes):
        raise ValueError("Country codes must be sorted uppercase alpha-2 strings")

    for code in codes:
        for kind in ("cities", "sights"):
            folder = ROOT / "countries" / code / kind
            folder.mkdir(parents=True, exist_ok=True)
            marker = folder / ".gitkeep"
            if not marker.exists():
                marker.write_text("", encoding="utf-8")

    print(f"Country folders ready: {len(codes)} countries, {len(codes) * 2} destination folders")


if __name__ == "__main__":
    main()
