# TopTravelList: instructions for future contributors and AI agents

**Applies to every new country, city, sight, or scoring revision.** This is a working checklist, not a replacement for the canonical scoring specification.

## Branch workflow

- Develop directly on `main` for this repository. Do not create new audit, feature, or staging branches or pull requests unless the owner explicitly requests one.
- Before committing, fetch and verify the latest `main`; preserve concurrent changes and use non-force, fast-forward updates. Complete the required validation and regenerate rankings from authoritative YAML before publishing.
- Reconcile older ahead branches without discarding distinct work or overwriting newer validated data. Document competing rating decisions and preserved historical evidence.

## Read before editing

1. [Worldwide v2 rules](rules.md) and [weight / 10-point registry](methodology/scoring.json).
2. [Future-country workflow](methodology/future-country-workflow.md), [per-record review template](methodology/review-record-template.md), and [evidence and quality standard](methodology/evidence-and-quality-standard.md).
3. For cities: [city guide](methodology/city-scoring-guide.md), [city comparisons](methodology/city-comparison-benchmarks.md), [reference profiles](methodology/city-benchmark-profiles.txt).
4. For sights: [sight guide](methodology/sight-scoring-guide.md), [sight comparisons](methodology/sight-comparison-benchmarks.md), [reference profiles](methodology/sight-benchmark-profiles.txt).
5. Existing YAML peers and [the completed 2026 per-sight editorial audit](methodology/sight-review-2026-full-audit.md). The YAML, not the frozen historical profiles, defines the current scores.

## Non-negotiable rules

- Only `countries/XX/cities/*.yaml` and `countries/XX/sights/*.yaml` are score sources. Every record has `id`, `name`, `location` (`country_code`, `latitude`, `longitude` only), and `scores`. Never add a hand-entered `overall` or evidence metadata to a YAML destination record.
- Every score uses the **same worldwide v2 scale**, independently of the country. No national quotas, country multipliers, target percentiles, or score inflation to make a national ranking look impressive.
- Score **each destination individually** in the five core dimensions: impact, uniqueness, significance, experience, depth. Categories are independent. Do not derive the five fields from a desired overall. Inapplicable categories are omitted; unassessed applicable fields are `null`.
- Each new or changed record needs a **named, destination-specific rationale**, **at least four global comparisons** (preferably three countries, with world-leading and ordinary examples), and an explicit evidence status, using the [review template](methodology/review-record-template.md). A stock paragraph repeated for every item is not an individual review.
- Put new review notes in `methodology/reviews/XX/cities.md` and `methodology/reviews/XX/sights.md` (create as needed). Large countries may link regional `sights-*.md` files from `sights.md`, with exactly one individual decision per sight ID. Keep the historical 2026 review and migration artifacts unchanged. Never overwrite existing review history when updating a record; add a dated reassessment and link its predecessor.
- **Source-linked does not mean score-verified**. Verify the identity and factual claims of each attraction separately; an editorial rating remains subjective. Never present a geographic article match, copied URL, generated rationale, or automated checker result as independent factual verification. Mark unverifiable claims clearly.
- Evaluate the named sight's actual scope. A gateway city, small temple, gate, lookout, market or cave must not inherit the score of a wider UNESCO area, park or flagship landmark.
- Explicitly justify every **9.5+ dimension or category**, and review all computed **90+ total** outliers with international peers. An exact 10 requires an explicit destination-ID / field entry in `methodology/scoring.json` with supporting world-best comparison. Never quietly whitelist one.
- Never rerun `scripts/calibrate_worldwide.py`, `scripts/recalibrate_cities_2026.py`, `scripts/recalibrate_sights_2026.py` or historical batch review scripts on new data.

## Required completion steps

1. Check for missing major destinations, duplicates, scope errors, invalid coordinates, and missing per-record reviews. Do not invent sites or sources.
2. Run `python scripts/validate.py`, `python scripts/check_city_benchmarks.py`, and `python scripts/check_sight_benchmarks.py`.
3. Run `python scripts/generate_rankings.py --country XX` (or without the country for all); then `python scripts/generate_rankings.py --check`. Commit the regenerated `countries/XX/cities.md`, `countries/XX/sights.md`, and any generated root README directory change.
4. Run `python scripts/rank.py --kind cities --limit 60` and `python scripts/rank.py --kind sights --limit 60`; inspect new outliers against existing worldwide leaders and ordinary peers.
5. In the commit notes or audit report (and PR if explicitly requested), state changed counts, independently fact-checked / source-linked / editorial-only / unassessed counts **separately**, noteworthy 9.5+/10 choices, and the commands actually run. Never claim unexecuted tests passed.

See [future-country workflow](methodology/future-country-workflow.md) for detailed steps and the [evidence standard](methodology/evidence-and-quality-standard.md) for review thresholds.
