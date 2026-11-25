# Indonesia — initial editorial and evidence quality audit

Date: 2026-11-25.

| Measure | Count |
| --- | ---: |
| City records and named reviews | 79 |
| Sight records and named reviews | 343 |
| Total destination records and named reviews | 422 |
| Initial source-linked-unverified sight reviews | 63 |
| Initial editorial-only sight reviews | 280 |
| Initial editorial-only city reviews | 79 |
| Fully independently claim-by-claim fact-checked records | 0 |

All records have five scores using the unchanged v2 weights, independent category judgments and site-specific scope/strength/limitation notes. No national score multiplier, target distribution, legacy rescaling or perfect-ten registry addition. Named peer ladders are reused within comparable attraction types; they are preliminary references, not fully evidenced individual field-by-field comparisons. GPS points remain approximate, particularly for wide forests and marine areas. A [supplementary coordinate correction](coordinate-corrections-2026.md) records one published GPS check for Atuh Beach; the initial review evidence-status counts above remain historical.

## Inventory and source scope

- [UNESCO Indonesia](https://whc.unesco.org/en/statesparties/ID): ten inscribed properties on the consulted list; serial and distributed properties may be represented by their distinct components rather than a single aggregate entry. The tentative list is **not** inscription.
- [Official tourism destination directory](https://www.indonesia.travel/gb/en/destination) and [regional attractions directory](https://www.indonesia.travel/gb/en/travel-ideas/adventure/38-destinations-in-indonesia): nationwide inventory starting points, not exhaustive verification.
- [Borobudur](https://whc.unesco.org/en/list/592/), [Prambanan](https://whc.unesco.org/en/list/642), [Komodo](https://whc.unesco.org/en/list/609): dedicated sources for leading monuments and ecological landscapes.
- [Official marine overview](https://www.indonesia.travel/id/id/travel-ideas/marine/7-panorama-bawah-laut-indonesia-yang-cocok-untuk-libur-musim-panas) and [UNESCO Raja Ampat Biosphere Reserve](https://www.unesco.org/en/mab/raja-ampat): marine biodiversity context. Biosphere recognition is distinct from World Heritage inscription.

Sources were consulted for limited facts and inventory; they do not certify quality scores. Exact site identity, geographic boundaries, coordinates, current access and specific historical/ecological claims need further independent research. Inventory coverage spans major island groups but is not exhaustive. In particular, sensitive cultural villages and protected areas must not be treated as freely accessible, and natural wildlife encounters are never guaranteed.

The [targeted leading-score review](top-score-review-2026.md) compares several leaders with actual existing YAML values. Further individual peer/field review remains necessary. Preserve prior decisions and append dated changes. The historical global audit and all prior-country records are outside this change.

## Automated verification

Run `python scripts/validate.py`, both benchmark checkers, `python scripts/check_new_country_reviews.py --country ID`, `python scripts/generate_rankings.py --country ID`, and `python scripts/generate_rankings.py --check`. These test data structure and generated coverage, not historical truth or coordinate accuracy.
