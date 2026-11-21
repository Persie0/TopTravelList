# TopTravelList — Worldwide Ranking Rules (v1)

This document defines the **same quality-scoring system for every country, city and sight**. It is version 1; changes that alter existing scores require a new rubric version and re-evaluation.

## What is rated?

- A **city** is a destination visited as a city (its broader city experience, including its attractions).
- A **sight** is an individual point of interest, natural attraction, landmark, or visitable area.
- All destinations use the same five core dimensions and score scale.
- Compare cities with cities and sights with sights by default. Mixed comparisons are possible but should be explicitly labeled, because a city and a single attraction are different units of experience.
- A sight can exist within a city and be scored individually. This does not prevent the city itself from being scored for the overall city experience.

## Core dimensions and weights

| Dimension | Weight | Question |
| --- | ---: | --- |
| **Impact** | **30%** | How memorable, beautiful, or extraordinary is the destination for a visitor? |
| **Uniqueness** | **25%** | How distinct or hard to substitute is this destination worldwide? |
| **Significance** | **20%** | How important is it historically, culturally, scientifically or naturally? |
| **Experience** | **15%** | How rewarding and engaging is an actual visit, independently of price or distance? |
| **Depth** | **10%** | How much meaningful exploration or discovery does the destination offer relative to its type? |

Each dimension is rated from **0 to 10**; decimal values are allowed. Apply the same anchors regardless of country, popularity, or local alternatives:

| Score | Meaning |
| ---: | --- |
| 0 | Virtually no value on this dimension |
| 2 | Very weak |
| 4 | Below average |
| 5 | Average |
| 6 | Above average |
| 8 | Exceptional |
| 10 | Among the world's very best in this dimension |

The total (out of 100) is:

```text
overall = 10 * (
    impact * 0.30 +
    uniqueness * 0.25 +
    significance * 0.20 +
    experience * 0.15 +
    depth * 0.10
)
```

A score may be calculated **only when all five core dimensions are assessed**. In YAML, `null` means unassessed, **not zero**. Do not write or edit an `overall` field in the source file; derive it from the dimension scores. Never fill unknown ratings with placeholder numbers or claim an unassessed destination has a rank.

## Category scores

A separate score (also 0–10) can be assigned to each applicable category:

| Key | What it measures |
| --- | --- |
| `nature` | Natural surroundings and landscapes |
| `architecture` | Buildings, built environment, and design |
| `history` | Historical interest, preservation, and interpretation |
| `culture` | Arts, museums, traditions, and cultural experiences |
| `food` | Food experiences at a destination |
| `beaches` | Beach quality and overall beach experience |
| `wildlife` | Opportunities to observe fauna responsibly |
| `adventure` | Active outdoor and exploratory experiences |
| `nightlife` | Evening entertainment and nightlife |
| `photography` | Visual appeal and photographic opportunities |
| `family` | Family-oriented experiences |
| `relaxation` | Peaceful and restful experiences |

Only add a category where it is **applicable**. Omit inapplicable categories entirely. Use `null` only for an applicable but unassessed category; it is not ranked. Never treat an omitted category as zero. Category scores do **not** change the universal overall score, and should use worldwide, not country-relative, standards.

## What the score does *not* measure

Keep these outside the universal quality score: prices, safety advisories, travel distance, accessibility, weather, crowds, visas, transport quality, and popularity. They may matter for itinerary decisions, but should not distort global quality rankings. Do not add these data fields during the foundation phase.

## Location rule

Each destination has exactly one `location` object with **only**:
- `country_code`: an uppercase two-letter code in `countries/_registry.json`.
- `latitude`: WGS84 decimal degrees, -90 through 90.
- `longitude`: WGS84 decimal degrees, -180 through 180.

Use a representative center point for a city or sight. Do not add addresses, nearest cities, regions, entrance locations, time zones, polygons, or map links. A country folder uses the same code as the destination's location. Kosovo uses the practical, unofficial `XK` code.

## Global comparability and quality control

1. Benchmark against exceptional and average destinations **worldwide**, not merely within the country.
2. Score the destination itself, not how affordable or easy it is to reach.
3. Apply the same definition of each dimension for cities and sights; interpret `depth` relative to the destination type.
4. Use explicit unassessed values until there is enough evidence to evaluate the destination.
5. Rank by overall score descending only if every core dimension is non-null.
6. Rank by a category score descending only if that category has a non-null score.
7. Handle ties with the same numeric rank; use destination ID alphabetically only for stable display order.
8. Display the size of the rated population and avoid labeling partial coverage as an exhaustive world ranking.
9. Never modify score weights or category definitions without updating the rubric version and reviewing affected ratings.

Machine-readable weights and categories are in [methodology/scoring.json](methodology/scoring.json). The schemas and validator enforce their structure.
