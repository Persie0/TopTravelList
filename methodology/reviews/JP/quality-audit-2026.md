# Japan — first-pass editorial quality and evidence audit

Date: 2026-11-25.

| Measure | Count |
| --- | ---: |
| City YAML and individual city reviews | 87 |
| Sight YAML and individual sight reviews | 347 |
| Total destinations and individual decisions | 434 |
| Source-linked-unverified sight records | 38 |
| Editorial-only sight records | 309 |
| Editorial-only city records | 87 |
| Fully claim-by-claim fact-checked records | 0 |

## Method and limitations

The five worldwide v2 dimensions (impact 30%, uniqueness 25%, significance 20%, experience 15%, depth 10%) and category taxonomy are unchanged. No new perfect-10 approvals, country multipliers, country score quotas or legacy correction curves were used. Individual scores are subjective judgments, with meaningful strengths and limits recorded for each destination. Four named international peers are recorded per entry; common attraction-type ladders are starting points, not evidence of an individually checked peer relationship for every field. Detailed per-dimension peer reasoning and exact coordinates remain a further quality task.

Inventory research used the [JNTO regional guide](https://www.japan.travel/en/destinations/), [UNESCO Japan list](https://whc.unesco.org/en/statesparties/JP/), [national park directory](https://www.japan.travel/national-parks/parks/) and selected dedicated JNTO pages. The UNESCO inventory lists 27 properties at review time, including the 2026 inscription of Asuka and Fujiwara. Catalogued components are not equivalent to entire serial properties, and the inventory is not exhaustive. URLs attached to individual entries are limited source context, not independent comprehensive verification. Some coordinates are approximate regional centers and must not be used as entrance instructions.

The [highest-score calibration review](top-score-review-2026.md) checks several leading entries against existing YAML benchmarks. All exceptionally high field values and claims beyond those comparisons remain provisional. Future research must record actual claim-level sources, precise geographic scope, and independent comparisons per record; it must append dated decisions rather than overwrite original review history.

## Validation

Use `python scripts/validate.py`, both benchmark checkers, `python scripts/check_new_country_reviews.py --country JP`, `python scripts/generate_rankings.py --country JP` and `python scripts/generate_rankings.py --check`. These checks establish structure, coverage and generated-list consistency, not factual correctness.
