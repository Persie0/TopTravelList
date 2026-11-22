# Cross-country city comparisons and reference ladder

**Mandatory peer reference for future city/town scores.**
Read this together with [city-scoring-guide.md](city-scoring-guide.md),
[the worldwide scoring rules](../rules.md), and the
[frozen 104-city dimension profiles](city-benchmark-profiles.txt).

These are **editorial travel-quality benchmarks**, not objective or permanent
judgments and not political/economic rankings. Rate a city's own visitor
experience and do not inherit the score of a landmark in its vicinity.

## Shared reference ladder (not a quota)

| City | Worldwide city-level emphasis | Reviewed 2026 overall /100 |
| --- | --- | ---: |
| Beijing, China | World-defining historic and cultural depth | 97.40 |
| Lhasa, China | Exceptionally distinctive urban/cultural identity | 95.40 |
| Xi'an, China | Rare ancient capital and urban archaeological depth | 95.20 |
| Gyeongju, South Korea | Exceptional concentrated historic city experience | 93.10 |
| Hong Kong, China | Outstanding urban setting and deep city-based exploration | 92.75 |
| Vienna, Austria | World-class history, architecture and sustained urban exploration | 92.30 |
| Seoul, South Korea | Highly engaging, deep major-city experience | 91.90 |
| Bangkok, Thailand | Globally significant city experience and food scene | 91.85 |
| Ayutthaya, Thailand | Outstanding urban heritage, separate from a single monument | 91.80 |
| Hội An, Vietnam | Compact but exceptional historic-town experience | 90.65 |
| Siem Reap, Cambodia | Strong visitor base, with Angkor rated separately | 90.20 |
| Salzburg, Austria | World-recognized historic urban setting and music legacy | 88.95 |
| Hà Nội, Vietnam | Significant layered city culture and exploration | 88.30 |
| Phnom Penh, Cambodia | Historically significant, less globally exceptional as a city | 80.40 |

The rating of the **individual Angkor Wat** sight is not the city rating of
Siem Reap. The same separation applies to the Great Wall vs Beijing, Ha Long
Bay vs Ha Long City, Trang An vs Ninh Binh, Phuket's beaches vs Phuket Town,
and national parks vs nearby gateway settlements.

## Dimensional cross-comparison

Use destination pairs as questions, NOT automatic scoring rules:

| Dimension | Strong global examples | Calibration trap |
| --- | --- | --- |
| Impact | Beijing, Vienna, Gyeongju, Salzburg, Hội An | Spectacular nearby landscape mistaken for the town's own impact |
| Uniqueness | Lhasa, Hong Kong, Hội An, Salzburg | Unique *in the province* mistakenly treated as globally singular |
| Significance | Beijing, Xi'an, Gyeongju, Vienna, Hue | A nearby UNESCO site counted as evidence of whole-city uniqueness |
| Experience | Bangkok, Seoul, Vienna, Hội An, Chiang Mai | Easy travel logistics, low prices, safety or popularity counted as intrinsic quality |
| Depth | Beijing, Seoul, Hong Kong, Vienna, Hanoi | Large urban footprint treated as synonymous with meaningful discovery |
| Architecture | Vienna, Salzburg, Gyeongju, Hội An, Suzhou | One photogenic building automatically giving a whole city 9.9 |
| Food | Bangkok, Guangzhou, Hanoi, Ho Chi Minh City | High nightlife or street-food quality overriding history score |
| Nature / beaches | Seogwipo, Da Nang, Da Lat, Koh Rong | Coastal island or a park *outside* town double-counted as the town itself |

A strong city may beat another on an individual dimension but still
have a lower weighted overall. A few examples:
- **Salzburg vs Phnom Penh:** Salzburg is more globally distinguished in
  citywide built heritage, urban identity and the visit itself. Phnom Penh
  retains meaningful historic significance and depth, but does not inherit
  near-perfect scores from its museums and the country's other heritage.
- **Vienna vs Siem Reap:** Vienna has extraordinary variety and depth within
  the city; Siem Reap's proximity to Angkor strengthens its destination
  role but Angkor Wat itself must retain a separate sight score.
- **Hội An vs the nearby Da Nang / Huế city centers:** the historic town
  forms the subject of the Hội An city rating. Each city receives its own
  independent architectural, cultural, historical and experiential rating.
- **Beijing vs provincial towns:** Beijing's rare global citywide depth
  does not require all Chinese towns to be scored highly, and no median
  or national-quota bonus applies.

## New country intake — required comparison review

For **every added country**, include in the PR description:
1. One locally famous city vs a **strong historic city** in another country.
2. One regional city vs an **ordinary** town across borders.
3. One gateway city vs its **separately ranked high-scoring sight**.
4. One spot-check of **any city core dimension or category 9.5+** against
   relevant world-best peers. If the claim is not convincingly supported,
   reduce that individual score.
5. The top five newly added cities, with their five numeric dimensions,
   weighted score, and country-independent rationale.

Open the worldwide city ranking using

    python scripts/rank.py --kind cities --limit 60

and compare the inserted country both above and below the new entries.
**No fixed national percentiles, median caps, or quotas.** A strong
reference is a comparison point, not an upper bound. New records should be
rated directly against the current v2 reference scale, not passed through
the archived 2026 adjustment curves.

The [complete 639-city audit](city-calibration-audit.md) lists source YAML
links and every change from the one-time 2026 calibration. Those changes
were first-pass corrections of mixed authoring cohorts, not evidence of
a comprehensive independent visit-based evaluation.
