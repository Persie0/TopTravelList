# City and town scoring guide — worldwide calibration (v2)

**Use this guide for EVERY city, town, village, and settlement in every new country.**
It is a scoring method, not a national top-ten rubric. It complements
[the universal rules](../rules.md), the
[cross-country comparison benchmarks](city-comparison-benchmarks.md), and
[the frozen 104-city reference profiles](city-benchmark-profiles.txt).

## What is being scored?

Rate the **settlement as a place worth visiting**, not the country and not
the single best attraction reachable from it. A city's museums, distinctive
neighborhoods, architecture, urban character, food, and opportunities for
meaningful exploration may all contribute. Do **not** transfer the individual
score of a remotely located temple, island, mountain, national park, river
cruise, or scenic road to the gateway town.

- **Siem Reap** offers a strong cultural and traveler base, but **Angkor Wat**
  is separately rated as a sight. They are not both 99/100.
- **Ha Long City** does not inherit **Ha Long Bay's** globally exceptional
  landscape rating.
- **Ha Giang** does not inherit the full **Ha Giang Loop** route rating.
- **Koh Ker Village** does not inherit the full archaeological park rating.
- **Salzburg** is evaluated for its own preserved historic center, architecture,
  music heritage, setting and meaningful on-foot exploration.
- **Phnom Penh** is evaluated for its significant modern history, museums,
  river setting, markets, food, urban character and overall city experience,
  not for nearby temples across Cambodia.

A city can nonetheless score very highly when its internationally outstanding
historic center **is actually within** the city, as in Hội An, Salzburg,
Gyeongju or Xi'an. A city does not need to be large to have significant impact
or uniqueness, but size alone never guarantees depth or value.

## Weighted five-dimension score

Use [methodology/scoring.json](scoring.json) as the ONLY weight source:

| Dimension | Weight | City-level question |
| --- | ---: | --- |
| Impact | 30% | How compelling, iconic and memorable is the **urban/settlement** visit? |
| Uniqueness | 25% | How difficult is it to substitute the city's own character, identity and built environment worldwide? |
| Significance | 20% | How strong is the city's historical, cultural or wider world significance? |
| Experience | 15% | How rich, rewarding and engaging is actually spending time in the city, independent of cost, weather, safety, queues and accessibility? |
| Depth | 10% | How much distinct meaningful city-based exploration is available, **relative to the city type**? |

All dimensions are **0–10**, maximum one decimal. Overall (out of 100)
is calculated, NOT stored:

    overall = 10 * (0.30 * impact + 0.25 * uniqueness
                    + 0.20 * significance + 0.15 * experience
                    + 0.10 * depth)

A category, for example food or architecture, is independently rated
0–10. Categories do not enter the weighted overall. Inapplicable categories
are omitted, not assigned 0. An applicable unknown category uses null.

## Worldwide anchors — not national percentiles

| Dimension score | City interpretation |
| ---: | --- |
| 5–5.9 | Ordinary visitor destination; limited distinctive city experience |
| 6–6.9 | Modestly rewarding regional town; some interesting characteristics |
| 7–7.9 | Good city or memorable small town; has a real reason to visit |
| 8–8.4 | Very good internationally; competitive with well-regarded destinations |
| 8.5–8.9 | Excellent international city/town; several independently strong qualities |
| 9–9.4 | Globally exceptional urban destination in this specific dimension |
| 9.5–9.9 | Rare global benchmark, with concrete peer comparisons required |
| 10 | World-defining in that exact field, approved in global_ten_anchors |

**These are anchors for each individual dimension, not forced overall-score
bands, and not a country ranking quota.** Most ordinary towns should NOT have
all five dimensions above 8.0. If 20 unrelated provincial towns all reach
9.0, the scoring benchmark has almost certainly drifted. Conversely,
a small country can have a truly world-best town, and a large country can
have relatively ordinary cities. Do not enforce fixed medians.

**Do not equate "best in country" with 9+ globally.** Never give a city
9.5 merely because its country's strongest town deserves a top local rank.
Reserve 10 for an *approved* globally defining field. Every 10 requires a
documented destination ID and field in scoring.json/global_ten_anchors, and
validation. An impressive UNESCO site does NOT automatically yield a perfect
city history, significance or architecture score.

## Concrete cross-country examples (2026 review)

| City | Core scores (I / U / S / E / D) | Overall /100 | What differentiates it |
| --- | --- | ---: | --- |
| Beijing (CN) | 9.7 / 9.7 / 9.9 / 9.5 / 10.0 | 97.40 | Deep, globally exceptional historical city with multiple independent world landmarks |
| Vienna (AT) | 9.2 / 9.0 / 9.5 / 9.2 / 9.4 | 92.30 | Extraordinary city-scale architecture, culture, urban heritage, museums and exploration |
| Siem Reap (KH) | 8.8 / 9.0 / 9.3 / 9.0 / 9.2 | 90.20 | A major cultural and exploration base, but Angkor's separate sight rating is not transferred |
| Hội An (VN) | 9.0 / 9.3 / 9.1 / 9.0 / 8.7 | 90.65 | Its historic town is itself the urban destination |
| Salzburg (AT) | 9.0 / 8.9 / 9.0 / 8.8 / 8.5 | 88.95 | Distinctive internationally important historic city despite smaller scale |
| Hà Nội (VN) | 8.7 / 8.8 / 8.9 / 8.8 / 9.2 | 88.30 | Cultural variety and urban depth; below globally singular heritage benchmarks |
| Phnom Penh (KH) | 7.9 / 7.6 / 8.6 / 8.0 / 8.5 | 80.40 | Significant history and worthwhile culture but less globally exceptional citywide experience |

These are **editorial reference profiles**, not objective universal city
quality measurements. They are intended to expose *inconsistent use of the
scale*. Review new destinations against multiple examples, not just one.

See the [comparison benchmarks](city-comparison-benchmarks.md) for
regional and thematic peer choices.

## How to score a newly added city

1. **Define the geographic subject.** A city, small town, village, historic
   settlement, beach-resort village and destination region are not interchangeable.
   Decide what meaningful experiences are truly in the settlement itself.
2. **List at least three concrete reasons to visit** and the city's distinct
   strengths and limitations. Do not need to store prose in source YAML, but
   use it during editorial review.
3. **Choose at least four cross-country comparisons**: one very strong city,
   one similar-sized or similar-purpose city, one regionally comparable
   historic/cultural counterpart, and one ordinary town. Examples from at
   least three *different countries* should inform the review when possible.
4. **Assign five individual dimension values.** Do not choose a desired total
   first, then reverse-engineer arbitrary scores to fit.
5. **Rate applicable categories separately**, against global category exemplars.
   A city's high food score need not inflate its history or overall score.
6. **Run the world-view comparison**: would this city still earn those scores
   if its country were hidden? Does a 9.4 compete with Beijing, Salzburg,
   Xi'an, Vienna, Gyeongju or similar international cities on that *dimension*?
7. **Audit proximity inflation:** if the main reason to visit is a nearby
   temple, island, mountain, national park, or boat trip, ensure that the
   gateway town's score is not borrowed from the separately rated sight.
8. **Check outliers**: if a provincial town exceeds Vienna or Salzburg
   overall, write down exactly what city-based merits justify it. This is
   not automatically impossible, but requires explicit cross-country review.
9. **Use YAML only for data** and store just country_code, latitude, longitude
   for location. Do not add addresses, visitor numbers, place types, opinions
   or total scores to the YAML schema.
10. **Run scripts and regenerate outputs** (commands below) and inspect the
    new country against cross-country ranked results.

## Required commands before every country/rating PR

    python scripts/validate.py
    python scripts/check_city_benchmarks.py
    python scripts/generate_rankings.py --country XX
    python scripts/generate_rankings.py --check
    python scripts/rank.py --kind cities --limit 40

Omit --country to regenerate all 197 country overview pairs. The generator
also refreshes the root Done/Not done directory and GPS Google Maps links.

If you add a destination with all scores at 9.5, stop and benchmark it:
9.5 across five dimensions is an extraordinary worldwide claim. No
destination gets a score based on a percentile quota, a country quota,
a tourism-arrival count, the number of records in the country, or a
fixed additive correction.

## Historic correction — DO NOT REUSE

The [2026 calibration audit](city-calibration-audit.md) documents a one-time
first-pass correction of all 639 existing city records. Its historic cohort
conversion script, scripts/recalibrate_cities_2026.py, creates a marker and
**refuses to rerun**. It is *not* an authoring recipe, not a global formula
for future countries, and not a country multiplier. New cities are scored
directly with the comparisons in this guide. If future evidence changes a
score, edit that city YAML and regenerate, leaving the other country scores
untouched unless an actual global rebenchmark is justified.
