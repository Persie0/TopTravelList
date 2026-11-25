"""Shared geographic registry validation and coverage semantics."""
import pycountry

def registry_errors(registry):
    codes = registry.get("codes", [])
    expected = {country.alpha_2 for country in pycountry.countries} | {"XK"}
    errors = []
    if registry.get("version") != 2:
        errors.append("Expected geographic registry version 2")
    if len(codes) != len(set(codes)) or codes != sorted(codes) or set(codes) != expected:
        errors.append(f"Registry must contain the complete ISO alpha-2 set plus XK; missing={sorted(expected-set(codes))}, unexpected={sorted(set(codes)-expected)}")
    territories = registry.get("territories", {})
    if not isinstance(territories, dict) or len(territories) != 53 or not set(territories) <= expected:
        errors.append("Expected metadata for the 53 additional geographic entries")
    else:
        for code, metadata in territories.items():
            if not isinstance(metadata, dict) or type(metadata.get("settlements_required")) is not bool:
                errors.append(f"Invalid territory metadata: {code}")
    return errors

def complete(registry, code, cities, sights):
    return bool(sights and (cities or not registry.get("territories", {}).get(code, {}).get("settlements_required", True)))
