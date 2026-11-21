#!/usr/bin/env python3
"""Validate country folders and each city/sight YAML file against JSON Schema."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
COUNTRIES = ROOT / "countries"
SCHEMAS = ROOT / "schemas"
SCORING = ROOT / "methodology" / "scoring.json"


def main() -> int:
    errors: list[str] = []
    countries = json.loads((COUNTRIES / "_registry.json").read_text(encoding="utf-8"))
    codes = countries["codes"]

    if len(codes) != 197 or len(codes) != len(set(codes)):
        errors.append("Registry must contain exactly 197 unique codes")
    if codes != sorted(codes) or any(not re.fullmatch(r"[A-Z]{2}", code) for code in codes):
        errors.append("Registry codes must be sorted, uppercase alpha-2 identifiers")

    actual_dirs = {p.name for p in COUNTRIES.iterdir() if p.is_dir()}
    if actual_dirs != set(codes):
        errors.append(f"Country directory mismatch: missing={sorted(set(codes) - actual_dirs)} "
                      f"unexpected={sorted(actual_dirs - set(codes))}")

    scoring = json.loads(SCORING.read_text(encoding="utf-8"))
    weights = scoring["dimensions"]
    if set(weights) != {"impact", "uniqueness", "significance", "experience", "depth"}:
        errors.append("Scoring dimensions differ from rules.md")
    if abs(sum(weights.values()) - 1.0) > 1e-9:
        errors.append("Scoring weights must sum to 1.0")

    schemas = {p.name: json.loads(p.read_text(encoding="utf-8"))
               for p in SCHEMAS.glob("*.schema.json")}
    resources = [(schema["$id"], Resource.from_contents(schema)) for schema in schemas.values()]
    reference_registry = Registry().with_resources(resources)
    for schema in schemas.values():
        Draft202012Validator.check_schema(schema)

    score_props = schemas["scoring.schema.json"]["properties"]
    if set(score_props) != set(weights) | {"categories"}:
        errors.append("Scoring schema dimensions differ from scoring.json")
    if score_props["categories"]["propertyNames"]["enum"] != scoring["categories"]:
        errors.append("Category taxonomy does not match scoring schema")

    validators = {
        "cities": Draft202012Validator(schemas["city.schema.json"], registry=reference_registry),
        "sights": Draft202012Validator(schemas["sight.schema.json"], registry=reference_registry),
    }
    used_ids: set[str] = set()
    file_count = 0
    for code in codes:
        for kind, validator in validators.items():
            folder = COUNTRIES / code / kind
            if not folder.is_dir():
                errors.append(f"Missing destination folder: {folder.relative_to(ROOT)}")
                continue
            for file in sorted(folder.iterdir()):
                if file.name == ".gitkeep":
                    continue
                if not file.is_file() or file.suffix not in (".yaml", ".yml"):
                    errors.append(f"Unexpected destination file: {file.relative_to(ROOT)}")
                    continue
                file_count += 1
                try:
                    data = yaml.safe_load(file.read_text(encoding="utf-8"))
                except yaml.YAMLError as exc:
                    errors.append(f"{file.relative_to(ROOT)}: invalid YAML: {exc}")
                    continue

                for issue in validator.iter_errors(data):
                    prop = ".".join(str(p) for p in issue.absolute_path) or "<root>"
                    errors.append(f"{file.relative_to(ROOT)}:{prop}: {issue.message}")

                if not isinstance(data, dict):
                    continue
                expected_id = f"{'city' if kind == 'cities' else 'sight'}-{code.lower()}-{file.stem}"
                if data.get("id") != expected_id:
                    errors.append(f"{file.relative_to(ROOT)}: expected id {expected_id}")
                if data.get("location", {}).get("country_code") != code:
                    errors.append(f"{file.relative_to(ROOT)}: location.country_code must be {code}")
                if data.get("id") in used_ids:
                    errors.append(f"{file.relative_to(ROOT)}: duplicate destination id")
                used_ids.add(data.get("id"))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed: {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print(f"Valid: {len(codes)} country folders, {file_count} destination files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
