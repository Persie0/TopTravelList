# TopTravelList — Worldwide Ranking Rules (v2)

This document defines the **same quality-scoring system for every country, city and sight**. It is version 2. All 1,540 destinations previously assessed under v1 are recalibrated to a worldwide reference scale. Future changes to score meanings require another version bump and a full comparison of affected records.

## What is rated?

- A **city** is a settlement visited as a destination (including towns and villages); rate its broader visitor experience, including its attractions. The folder name is an editorial grouping, not a claim about legal city status.
- A **sight** is an individual point of interest, natural attraction, landmark, or visitable area.
- All destinations use the same five core dimensions and score scale.
- Compare cities with cities and sights with sights by default. Mixed comparisons are possible but should be explicitly labeled, because a city and a single attraction are different units of experience.
- A sight can exist within a city and be scored individually. This does not prevent the city itself from being scored for the overall city experience.

## Additional mandatory instructions for city rankings

The universal core dimensions below apply to both cities and individual sights,
but a city must be rated for the **city itself**, not given the score of a
nearby world-famous temple, island, mountain, park, waterfall or excursion.
Use the detailed [city scoring guide](methodology/city-scoring-guide.md),
[cross-country benchmark ladder](methodology/city-comparison-benchmarks.md),
and [frozen city reference profiles](methodology/city-benchmark-profiles.txt)
before adding cities in any future country.

In November 2026, the 639 populated city records across AT, TH, KR, CN, VN,
and KH were jointly reviewed to correct mixed historical scoring standards;
104 named destinations received individually reviewed benchmark profiles.
The [complete audit](methodology/city-calibration-audit.md) records all changes.
The city-only migration did **not** modify universal v2 weights, and
did not change sight records at the time. A separate 2026 worldwide
sight audit subsequently recalibrated all 1,733 sights. Neither migration
establishes a geography-based future scoring multiplier. Future countries must be rated directly using
cross-country comparisons. After editing, run both
`python scripts/validate.py` and
`python scripts/check_city_benchmarks.py` and regenerate the Markdown rankings.

## Additional mandatory instructions for sight rankings

**Before scoring any new sight**, use the
[worldwide sight-scoring guide](methodology/sight-scoring-guide.md),
[cross-country sight benchmarks](methodology/sight-comparison-benchmarks.md)
and the [189 frozen worldwide sight profiles](methodology/sight-benchmark-profiles.txt).
Use the same global five dimensions, regardless of country or attraction
type. Rank a specific **sight itself**, not a gateway city, neighboring
national park or parent heritage area. A temple gate or local market does
not automatically inherit a near-100 score from its UNESCO-listed parent.

The one-time November 2026 audit of **all 1,733 previously populated
sights** corrected inconsistent prior scoring, preserving every existing
officially approved field-specific 10/10 and all site identities and GPS.
[Complete per-sight change log](methodology/sight-calibration-audit.md).
Of 1,733 sights, 189 have individually benchmarked cross-country
profiles; the remainder received a conservative numeric historical correction.
These are provisional editorial assessments, **not 1,733 individual field
visits or research-based audits**. Historical country-cohort correction
curves are **NOT** authorized for future country authoring.

For every new country, benchmark at least four international peers
(including world-best and ordinary examples), inspect every proposed 9.5+
field and compare nested attractions individually. A perfect 10 requires
a field-specific ID approval in methodology/scoring.json. No national
quotas, fixed distribution targets or percentage caps are allowed.

After sight edits run the global validator, the **city AND sight**
benchmark checkers, regenerate the relevant Markdown overviews and run
the --check mode for all registered countries. The root README describes
the exact commands.

The [ongoing evidence-referenced sight review](methodology/sight-review-2026-summary.md) now distinguishes **258 individual desk-based editorial decisions**, including **109 newly source-referenced entries**, from **1,655 records screened only by diagnostics**. This distinction is required in future summaries: citing a comparator or recording a numeric warning does not by itself qualify as independent site research. Source URLs in the individual review records are supporting references, not official score endorsements.

### New site-specific sight reassessment (22 November 2026)

The [follow-on sight review](methodology/sight-review-2026-summary.md) records explicit changes to named site profiles and an [exhaustive one-row-per-sight screening register](methodology/sight-review-2026-full-audit.md). Automatically screened records **have not** received independently researched re-evaluations. The 189 frozen calibration profiles remain historical evidence, not active authoritative scores; updated YAML is authoritative. Do not rerun any archival correction curve.

## Core dimensions and weights

| Dimension | Weight | Question |
| --- | ---: | --- |
| **Impact** | **30%** | How memorable, beautiful, or extraordinary is the destination for a visitor? |
| **Uniqueness** | **25%** | How distinct or hard to substitute is this destination worldwide? |
| **Significance** | **20%** | How important is it historically, culturally, scientifically or naturally? |
| **Experience** | **15%** | How rewarding and engaging is an actual visit, independently of price or distance? |
| **Depth** | **10%** | How much meaningful exploration or discovery does the destination offer relative to its type? |

These ratings are **editorial judgments**, not objective measurements. Early country scores are provisional first-pass assessments and may be recalibrated against worldwide benchmarks as the database grows.

Each dimension is rated from **0 to 10**; decimal values are allowed. Apply the same anchors regardless of country, popularity, or local alternatives:

| Score | Meaning |
| ---: | --- |
| 0 | Virtually no value on this dimension |
| 2 | Very weak |
| 4 | Below average |
| 5 | Average |
| 6 | Above average |
| 8 | Excellent on a worldwide scale (strong destination, not a global pinnacle) |
| 9 | Internationally outstanding, comparable with elite peers |
| 9.5 | Among the rare global reference experiences |
| 10 | Reserved for a globally defining benchmark of this exact dimension; requires a documented whitelist entry |

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

## Worldwide calibration: version 2 (mandatory for all new countries)

**A rating of 10 is not “the best in the country.”** It means world-leading quality against the strongest examples anywhere on Earth, whether the destination is in a large or small country. **Never assign a 10 simply because a country lacks better competitors.** The Great Wall, Angkor Wat, Taj Mahal, Machu Picchu, Grand Canyon and other globally iconic peers should form the reference set even before their countries appear in this repository. Naming a peer does not automatically grant that peer 10/10: each dimension needs its own assessment.

Use the following global calibration anchors. They are *examples*, not an automatic ranking or an exhaustive world top list.

| Score | Comparative threshold | Practical meaning |
| ---: | --- | --- |
| 5.0 | Average worldwide tourist stop | Moderate interest, fairly replaceable |
| 6.0 | Worth considering | Some memorable qualities, still replaceable |
| 7.0 | Good worldwide attraction | Strong experience and clear merit |
| 8.0 | Excellent worldwide destination | Would stand out across many countries |
| 9.0 | Globally outstanding | Strong peer to internationally celebrated destinations |
| 9.5 | Elite world-class destination | Rare even across a large global dataset |
| 9.9 | Almost unmatched | Exceptional cross-continental case |
| 10.0 | Global defining benchmark | Requires comparison with world-best peers and explicit registry approval |

**Core-dimension peer comparisons:**

- `impact`: Is the emotional, visual or experiential effect in the world's absolute top tier (e.g. the Great Wall on its best stretches), or just outstanding within one region?
- `uniqueness`: Is the experience globally difficult to substitute? Ancient imperial sites, singular landforms and radically distinctive cultural places may qualify; a locally distinctive old town usually does not.
- `significance`: Compare worldwide historical, scientific, cultural and ecological consequence; UNESCO recognition alone does **not** imply 10.
- `experience`: Judge an actual visit on its own merits. A globally famous landmark with an underwhelming or restricted visit may score lower here.
- `depth`: Compare the discovery possible **relative to type**. A museum, city, fortress or mountain needs depth matching the strongest worldwide peers of that type, not a score proportional to its physical size.

**Category comparisons:** A 10 in `architecture` should rival the world's iconic built environments, not the best building in its city. A 10 in `nature` should compare to global flagship landscapes rather than the best park in one country. Apply equivalent global peers to beaches, history, culture, food, wildlife, adventure, nightlife, photography, family and relaxation. Leave room for places not yet cataloged; no category is guaranteed a 10.

**Explicit approval for every 10.** `methodology/scoring.json` maintains `global_ten_anchors`, a whitelist of destination IDs for each core dimension or category. A 10 is valid **only** for a listed destination *and* dimension/category; `scripts/validate.py` rejects undocumented 10s. To add a genuinely world-leading new destination, compare it with current and missing global peers, set a substantiated 10 only for the deserved dimension, update its exact ID under `global_ten_anchors`, and review whether an older anchor should be downgraded. There are **no per-country quotas**, and a small country can have the best example in a specific dimension.

**Global comparability is independent of coverage.** Do not fill all 197 countries before calibrating: preserve the same global bar from day one. Reassess benchmarks as additional continents enter the database; do not rescale existing records automatically by country population, country counts, visitor numbers or percentile. No country should receive a default 10. A computed overall score of 100/100 is exceptionally unlikely because a destination would need to independently earn 10 in all five dimensions; an ordinary world-famous place need not receive 100.

### Historical migration (do not apply to new data)

The legacy v1 scores were inflated: many countries' leading sights were awarded 10/10 independently. Version 2 converted each legacy rating with an **absolute, monotone, conservative curve**:

| v1 rating | v2 baseline |
| ---: | ---: |
| 5.0 | 4.3 |
| 6.0 | 5.2 |
| 7.0 | 6.1 |
| 8.0 | 7.0 |
| 9.0 | 8.0 |
| 9.5 | 8.5 |
| 10.0 | 9.0 |

Intermediate values were interpolated, rounded to one decimal. A small set of manually reviewed worldwide reference destinations received explicit scores above this baseline; only explicitly approved benchmarks can receive 10. This is a conservative correction of **unverified first-pass editorial judgments**, not a claim that every individual rating has been professionally audited. The one-time reproducible converter is `scripts/calibrate_worldwide.py`; it deliberately rejects a second run after the metadata version becomes 2.

**For every new destination going forward:** rate it directly using this v2 worldwide scale and peer comparisons. **Do not run the v1-to-v2 conversion on future data.** If information is insufficient, leave the dimension `null`; do not guess. A 9.5 is already extraordinarily strong. Country coverage and local top-ten placement confer no scoring bonus.

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

## Country ranking overview files (mandatory after any data changes)

Each registered country's folder must contain **two generated Markdown overview files**: `cities.md` and `sights.md` (not inside the subfolders). They display the **full actual ranking** from the source YAML, not a curated top 10 and not country-relative scores. Every ranked entry shows its position, overall score /100, rating breakdown, assessed category scores, destination type derived from its name, and a clickable **Google Maps link built from the exact latitude/longitude**. The destination name links to the corresponding YAML. Empty countries still get two overview files explaining that no destinations have been rated. Missing core scores appear in a separate unranked section.

The root `README.md` also contains an automatically maintained **Done / Not done** index, linking to every registered country folder. A country is Done when both `cities/` and `sights/` contain at least one destination YAML; this is a population-status indicator, not a guarantee of exhaustive sightseeing coverage. Regenerating the rankings also refreshes this root directory, and `--check` detects stale README index entries.

The only canonical editable sources remain `countries/XX/cities/*.yaml` and `countries/XX/sights/*.yaml`. Generated Markdown files are **not** the source of truth and must not be manually scored.

After **every** new country, destination, location change, or score change:

1. Run `python scripts/validate.py` for the worldwide scoring/structure rules.
2. Run `python scripts/generate_rankings.py --country XX` for each affected country, or omit the flag to refresh all 197 countries.
3. Run `python scripts/generate_rankings.py --check` and commit the source YAML **and** refreshed Markdown rankings together.

The generator uses the exact worldwide v2 weighting in `methodology/scoring.json`, stable sorting, and tied ranks. It does **not** recalibrate scores, add source fields, or assign a 10/10 to any destination. Google Maps search links use numeric WGS84 coordinates; they are for locating representative points, not necessarily navigation to a park entrance.

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
