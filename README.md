# TopTravelList

A consistent, worldwide ranking dataset for **cities** and **sights**.

## Repository layout

```text
countries/
  _registry.json
  AT/
    cities/
    sights/
  ...
methodology/
  scoring.json
schemas/
  city.schema.json
  sight.schema.json
  location.schema.json
  scoring.schema.json
scripts/
  generate_countries.py
  validate.py
  rank.py
rules.md
requirements.txt
```

Every destination is stored as an individual YAML file in its country's `cities/` or `sights/` directory. Location data contains **only** `country_code`, `latitude`, and `longitude`.

## Get started

```bash
python -m pip install -r requirements.txt
python scripts/generate_countries.py
python scripts/validate.py
python scripts/rank.py --country AT --kind cities --limit 20
python scripts/rank.py --country AT --kind sights --limit 20
python scripts/rank.py --country AT --kind sights --category nature --limit 20
python scripts/rank.py --country TH --kind cities --limit 20
python scripts/rank.py --country TH --kind sights --limit 20
python scripts/rank.py --country TH --kind sights --category beaches --limit 20
python scripts/rank.py --country KR --kind cities --limit 20
python scripts/rank.py --country KR --kind sights --limit 20
python scripts/rank.py --country KR --kind sights --category history --limit 20
python scripts/rank.py --country CN --kind cities --limit 30
python scripts/rank.py --country CN --kind sights --limit 30
python scripts/rank.py --country CN --kind sights --category nature --limit 30
python scripts/rank.py --country CN --kind sights --category history --limit 30
```

The registry covers **197 travel-country entries**: the 193 United Nations member states, the Holy See and Palestine (UN observer states), plus Taiwan and Kosovo as separately listed travel destinations. Kosovo uses the commonly used, user-assigned code `XK`, not an official ISO 3166-1 code. This is a geographic organization convention, not a statement on political recognition. Territories are not included.

See [rules.md](rules.md) for the universal scoring rubric and [methodology/scoring.json](methodology/scoring.json) for the machine-readable weights and categories.

## Populated countries

- **Austria (`AT`)**: 45 city/town/village destinations and 133 sights.
- **Thailand (`TH`)**: 69 city/town/village destinations and 206 sights, including islands, historic parks, temples, waterfalls, and national parks.
- **South Korea (`KR`)**: 82 city/town/village destinations and 284 sights, including palaces, royal heritage, Buddhist temples, national parks, islands, Jeju volcanic sites, and beaches.
- **China (`CN`)**: 231 cities, towns and villages and 490 sights, including historic capitals, ancient towns, UNESCO heritage sites, major mountain and river landscapes, and important destinations across China's regions. For this country grouping, Hong Kong and Macau are included under `CN`; Taiwan remains in the separately registered `TW` folder.

All destination records contain the same five core scoring dimensions and applicable category ratings. The scores are **provisional editorial assessments**, not objective facts or definitive worldwide standings. Since the current rubric allows multiple top scores, exceptional destinations can tie. Coordinates identify approximate representative points and should not be used as precise navigation destinations; large parks, rivers, lakes, and regions are not represented by entrance coordinates.

Use `scripts/rank.py` for sorted comparisons; it computes the overall score and category rankings directly from source YAML without generating additional files. Each category is independently rated on the 0–10 scale, as described in `rules.md`.

## Destination file examples

`countries/AT/cities/vienna.yaml`:

```yaml
id: city-at-vienna
name: Vienna
location:
  country_code: AT
  latitude: 48.2082
  longitude: 16.3738
scores:
  impact: 9.6
  uniqueness: 9.1
  significance: 9.8
  experience: 9.4
  depth: 9.7
  categories:
    architecture: 9.8
    history: 9.7
    culture: 9.9
    food: 9.1
    nightlife: 8.5
    photography: 9.1
```

`countries/AT/sights/schoenbrunn-palace.yaml`:

```yaml
id: sight-at-schoenbrunn-palace
name: Schönbrunn Palace
location:
  country_code: AT
  latitude: 48.1845
  longitude: 16.3122
scores:
  impact: 9.3
  uniqueness: 8.9
  significance: 9.5
  experience: 9.3
  depth: 9.2
  categories:
    architecture: 9.8
    history: 9.6
    culture: 9.5
    photography: 9.5
```

Coordinates are approximate representative points, not verified entrance locations. Null means *not assessed*, not zero. Do not assign rankings to incomplete assessments.

## Notes

- Valid location fields: `country_code`, `latitude`, `longitude` only.
- Only the two requested destination kinds are stored: cities and sights.
- Overall scores are computed from assessed core dimensions; do not store redundant, manually edited totals.
- The country folders are created once by the generator, with `.gitkeep` files to keep empty directories in Git.
