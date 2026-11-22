#!/usr/bin/env python3
"""Generate two complete Markdown rankings in every registered country folder.

Source YAML records remain authoritative. Rerun after any destination edit.
Use --check to detect missing/stale Markdown without writing changes.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from urllib.parse import quote

import pycountry
import yaml

from rank import overall_score

ROOT = Path(__file__).resolve().parents[1]
COUNTRIES = ROOT / "countries"
DIMENSIONS = ("impact", "uniqueness", "significance", "experience", "depth")
COUNTRY_NAMES = {
    "BO": "Bolivia", "BN": "Brunei", "CD": "DR Congo",
    "CN": "China", "CZ": "Czechia", "GB": "United Kingdom",
    "IR": "Iran", "KR": "South Korea", "KP": "North Korea",
    "LA": "Laos", "MD": "Moldova", "MK": "North Macedonia",
    "PS": "Palestine", "RU": "Russia", "SY": "Syria",
    "TW": "Taiwan", "TZ": "Tanzania", "US": "United States",
    "VA": "Vatican City", "VE": "Venezuela", "VN": "Vietnam",
    "XK": "Kosovo",
}
TYPE_PATTERNS = [
    (r"great wall|city wall|fortress|citadel|\bfort\b", "Fortification"),
    (r"national park|marine park|nature reserve|geopark|sanctuary", "Park / reserve"),
    (r"temple|monastery|shrine|pagoda|mosque|cathedral|church|stupa|abbey", "Religious site"),
    (r"museum|mausoleum|memorial|tombs?|grottoes|archaeological|ruins", "Museum / heritage"),
    (r"palace|castle|schloss|chateau", "Palace / castle"),
    (r"waterfall|\bfalls\b", "Waterfall"),
    (r"beach|bay|lagoon", "Beach / bay"),
    (r"island|islet", "Island"),
    (r"lake|reservoir", "Lake"),
    (r"river|canal", "River / waterway"),
    (r"\bcave\b|\bcavern\b", "Cave"),
    (r"peak|mountain|\bmount\b|volcano|glacier", "Mountain / peak"),
    (r"gorge|canyon|valley", "Valley / canyon"),
    (r"forest|jungle|rainforest", "Forest"),
    (r"garden|arboretum|botanic", "Garden"),
    (r"wetland|marsh", "Wetland"),
    (r"village|old town|ancient town|historic centre|historic center", "Historic settlement"),
    (r"tower|skyscraper|skywalk|viewpoint|observatory", "Tower / viewpoint"),
    (r"bridge", "Bridge"),
    (r"market|bazaar", "Market"),
    (r"trail|trek|plank walk", "Trail / walk"),
    (r"desert|dune", "Desert"),
    (r"historic areas|historical park", "Historic area"),
    (r"park|square|plaza", "Park / square"),
    (r"harbour|harbor|coast|cape", "Coast"),
]


def get_country_name(code):
    if code in COUNTRY_NAMES:
        return COUNTRY_NAMES[code]
    country = pycountry.countries.get(alpha_2=code)
    return country.name if country else code


def cell(s):
    return str(s).replace("|", r"\|").replace("\n", " ").replace("\r", " ").strip()


def number(value, digits=1):
    if value is None or isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        return "—"
    quantum = Decimal(1).scaleb(-digits)
    return str(Decimal(str(value)).quantize(quantum, rounding=ROUND_HALF_UP))


def get_kind(name, folder):
    if folder == "cities":
        if re.search(r"\bvillage\b", name, flags=re.I):
            return "Village"
        if re.search(r"\btown\b", name, flags=re.I):
            return "Town"
        return "City / town"
    for pattern, label in TYPE_PATTERNS:
        if re.search(pattern, name, flags=re.I):
            return label
    return "Attraction"


def get_map_location(record, code):
    loc = record.get("location")
    if not isinstance(loc, dict) or set(loc) != {"country_code", "latitude", "longitude"}:
        raise ValueError("Location does not contain precisely the three required fields: " + record["id"])
    if loc["country_code"] != code:
        raise ValueError("Wrong location country code: " + record["id"])
    lat, lon = loc["latitude"], loc["longitude"]
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) for x in (lat, lon)):
        raise ValueError("Invalid numeric coordinates: " + record["id"])
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError("Coordinates out of range: " + record["id"])
    gps = f"{lat},{lon}"
    url = "https://www.google.com/maps/search/?api=1&query=" + quote(gps, safe=",")
    return f"[{lat}, {lon}]({url})"


def list_categories(record):
    cats = record["scores"].get("categories", {})
    if not isinstance(cats, dict) or not cats:
        return "—"
    def key(item):
        _, score = item
        return (score is None, -Decimal(str(score)) if score is not None else Decimal(0), item[0])
    pieces = []
    for i, (name, score) in enumerate(sorted(cats.items(), key=key)):
        label = cell(name.replace("_", " ").title())
        value = number(score) if score is not None else "unassessed"
        item = f"{label} {value}"
        pieces.append(f"**{item}**" if i < 3 and score is not None else item)
    return ", ".join(pieces)


def core_scores(record):
    return " / ".join(number(record["scores"].get(key)) for key in DIMENSIONS)


def load_records(code, folder, weights):
    path = COUNTRIES / code / folder
    if not path.is_dir():
        raise ValueError("Missing country subdirectory: " + str(path))
    ranked, unranked, seen = [], [], set()
    for file in sorted(path.glob("*.yaml")):
        record = yaml.safe_load(file.read_text(encoding="utf-8"))
        if not isinstance(record, dict):
            raise ValueError("Malformed destination: " + str(file))
        expected = ("city" if folder == "cities" else "sight") + f"-{code.lower()}-{file.stem}"
        if record.get("id") != expected or record["id"] in seen:
            raise ValueError("Invalid or repeated destination ID in " + str(file))
        if not isinstance(record.get("name"), str) or not record["name"].strip():
            raise ValueError("Missing destination name in " + str(file))
        seen.add(record["id"])
        record["_score"] = overall_score(record, weights)
        record["_source"] = folder + "/" + file.name
        record["_map"] = get_map_location(record, code)
        (ranked if record["_score"] is not None else unranked).append(record)
    ranked.sort(key=lambda d: (-d["_score"], d["name"].casefold(), d["id"]))
    unranked.sort(key=lambda d: (d["name"].casefold(), d["id"]))
    return ranked, unranked


TABLE_HEADER = (
    "| Rank | Destination (click for YAML) | Type | Overall /100 | "
    "Categories /10 (best first) | I / U / S / E / D | GPS → Google Maps |\n"
    "| ---: | --- | --- | ---: | --- | --- | --- |"
)


def render_row(record, rank, folder):
    overall = number(record["_score"], 2)
    return (
        f"| {rank} | [{cell(record['name'])}]({record['_source']}) | "
        f"{cell(get_kind(record['name'], folder))} | **{overall}** | "
        f"{list_categories(record)} | {core_scores(record)} | {record['_map']} |"
    )


def render_country(code, folder, weights, version):
    ranked, unranked = load_records(code, folder, weights)
    title = "Cities, towns & villages" if folder == "cities" else "Sights & attractions"
    other = "sights.md" if folder == "cities" else "cities.md"
    lines = [
        "<!-- AUTO-GENERATED by scripts/generate_rankings.py; edit YAML, not this file. -->",
        "",
        f"# {get_country_name(code)} ({code}) — {title} ranking",
        "",
        f"**{len(ranked)} ranked** · **{len(unranked)} unassessed** · "
        f"**{len(ranked) + len(unranked)} total** · Worldwide scoring **v{version}**",
        "",
        f"[Other ranking]({other}) · [Worldwide scoring rules](../../rules.md) · "
        f"[Scoring weights](../../methodology/scoring.json) · [Source YAML]({folder}/)",
        "",
        "This is the **complete ranking for this country's available dataset**, "
        "using absolute worldwide scores, **not country-relative scores**. "
        "Overall scores are out of 100; category scores are out of 10 and shown "
        "highest first (the top three are bold). Types are inferred from names, "
        "not separately verified.",
        "",
        "**Core dimensions (out of 10):** I = Impact (30%), U = Uniqueness (25%), "
        "S = Significance (20%), E = Experience (15%), D = Depth (10%). "
        "Click a destination for its source YAML, or click its GPS coordinates "
        "to open **Google Maps**. Locations are approximate representative points, "
        "not necessarily entrance coordinates.",
        "",
        f"## Complete ranked list ({len(ranked)})",
        "",
    ]
    if ranked:
        lines.append(TABLE_HEADER)
        previous, rank = None, 0
        for index, rec in enumerate(ranked, 1):
            if previous is None or rec["_score"] != previous:
                rank = index
            previous = rec["_score"]
            lines.append(render_row(rec, str(rank), folder))
    else:
        lines.extend([
            f"No {title.lower()} have been assessed for **{get_country_name(code)}** yet.",
            "",
            f"Add destination YAML files in [{folder}/]({folder}/), "
            "then regenerate the overview files.",
        ])
    if unranked:
        lines.extend([
            "", f"## Not yet fully assessed ({len(unranked)})", "",
            "These destinations have no rank until all five core scores are assessed.", "",
            TABLE_HEADER,
        ])
        lines.extend(render_row(rec, "—", folder) for rec in unranked)
    lines.extend(["", "---", "",
                  "After changing a YAML record, regenerate with: python scripts/generate_rankings.py", ""])
    return "\n".join(lines), len(ranked) + len(unranked)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--country", type=str.upper, help="One two-letter registered country (default: all)")
    parser.add_argument("--check", action="store_true",
                        help="Report missing or stale generated rankings, without writing")
    args = parser.parse_args()
    codes = json.loads((COUNTRIES / "_registry.json").read_text(encoding="utf-8"))["codes"]
    if args.country and args.country not in codes:
        parser.error("Unknown country code: " + args.country)
    selected = [args.country] if args.country else codes
    metadata = json.loads((ROOT / "methodology/scoring.json").read_text(encoding="utf-8"))
    weights = {k: Decimal(str(v)) for k, v in metadata["dimensions"].items()}
    if tuple(weights) != DIMENSIONS:
        raise ValueError("Unexpected scoring dimensions")
    changed, destinations = [], 0
    for code in selected:
        for folder in ("cities", "sights"):
            output, count = render_country(code, folder, weights, metadata["version"])
            destinations += count
            target = COUNTRIES / code / (folder + ".md")
            old = target.read_text(encoding="utf-8") if target.exists() else None
            if old != output:
                changed.append(str(target.relative_to(ROOT)))
                if not args.check:
                    target.write_text(output, encoding="utf-8", newline="\n")
    if args.check and changed:
        print(f"{len(changed)} missing/stale ranking file(s):", file=sys.stderr)
        for path in changed:
            print("  " + path, file=sys.stderr)
        return 1
    print(f"{'Checked' if args.check else 'Generated'} {len(selected) * 2} "
          f"ranking files for {len(selected)} countries, {destinations} destinations; "
          f"{0 if args.check else len(changed)} files written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
