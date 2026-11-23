# New-country and future-destination scoring workflow

This is the repeatable process for **every subsequent country** and **every newly added or revised city or sight**. It does not change [worldwide v2 rules](../rules.md), [weights and 10/10 registry](scoring.json), or the original YAML schema. The 2026 reviews are a historical starting point, not a tool to rescale new countries.

## Step 1 — Inventory before scoring

- Use the already registered two-letter country code and existing `countries/XX/cities/` and `countries/XX/sights/` directories. Keep the two source kinds separate.
- Compile an inventory from reliable geographic, heritage, conservation, tourism and visitor references, including locally important places as well as famous landmarks. Do not restrict coverage to tourist-marketing top-ten lists.
- Check whether a destination already exists under a local spelling, an English name, an umbrella park or a nearby city; avoid duplicates and artificial sub-attractions.
- Define each record's **exact scope**. City/town ratings describe the settlement's own urban and visitor experience; sight ratings describe the specified attraction. A nearby attraction is not automatically an urban merit, and the entrance gate of a complex is not the whole complex.
- Verify coordinates as an approximate representative WGS84 point, not a guaranteed entrance. Only `country_code`, `latitude`, and `longitude` belong in `location`.

## Step 2 — Research the individual destination

For **each ID separately**:

1. Confirm identity, location and scope with an actual source about that named destination, not an approximate match to the nearest town.
2. Collect concrete facts useful to scoring (e.g., architecture, heritage importance, geological distinctiveness, collections, public visitor experience, breadth of activities). Keep facts and subjective assessments distinct.
3. Record the precise URLs, publishers, dates accessed, and what each source supports. Prioritize official primary material combined with independent reporting or authoritative subject references where available. Do not invent links or claim to have opened something you did not inspect.
4. Identify uncertainty: closed sites, seasonal or restricted access, disputed claims, incomplete evidence, inconsistent official descriptions. Intrinsic scores do not become current-access promises.
5. Mark the review status according to [evidence and quality standard](evidence-and-quality-standard.md). An encyclopedia search hit by itself is not full verification.

Use the [per-record template](review-record-template.md). Store prose and URLs in `methodology/reviews/XX/{cities,sights}.md`, **never** in destination YAML. A new country can start with editorial-only entries, but those must not be counted as independently fact-checked.

## Step 3 — Compare worldwide **before** choosing numbers

For each record select at least **four named cross-country reference destinations**:
- A world-defining or global-top-tier comparison.
- Two credible same-type / comparable-scale sights or cities from other countries.
- One ordinary or regionally strong example that helps establish a realistic floor.

Prefer references spanning at least **three countries** when possible. Compare city to city and sight to sight. Compare a standalone sight with another *standalone sight of similar scope*, not the surrounding region. Existing comparison ladders are starting points, not facts that authorize a score.

Use [city scoring guide](city-scoring-guide.md) and [city comparison benchmarks](city-comparison-benchmarks.md) for urban records; [sight scoring guide](sight-scoring-guide.md) and [sight comparison benchmarks](sight-comparison-benchmarks.md) for attractions. Also inspect the current YAML scores of the peers; the frozen `.txt` benchmark profiles can be historical and must not overwrite revised YAML.

Ask per dimension: **Why would this place outrank, match, or fall below these peers in this exact dimension?** Document an actual reason, not merely the peer's name.

## Step 4 — Rate five fields independently

Use the shared worldwide anchors in [rules.md](../rules.md). Evaluate:
- **Impact (30%)** — actual memorability, visual / emotional / experiential quality.
- **Uniqueness (25%)** — rarity, difficulty of substituting the experience elsewhere.
- **Significance (20%)** — world-relevant cultural, historical, scientific or natural importance.
- **Experience (15%)** — how rewarding the visit itself is, distinct from fame, price and travel effort.
- **Depth (10%)** — meaningful exploration relative to a comparable kind of attraction or city.

Rate the five fields separately on the 0–10 scale (at most one decimal), **then** derive the total as `10 × (0.30×impact + 0.25×uniqueness + 0.20×significance + 0.15×experience + 0.10×depth)`. The total is calculated by scripts; it is not stored.

Only rate categories actually applicable to the named place. A high `history` category does not force high impact, experience or depth. Distinguish major heritage ensembles from small nested features; compare their visits independently.

Use `null` when a required dimension or applicable category cannot responsibly be assessed. An incomplete record stays unranked; never use `0` as a placeholder for unknown information.

## Step 5 — Challenge inflated and exceptional results

- Audit **every 9.5+ individual field** against current worldwide exemplars, with a specific explanation in its review note. A 9.5 is an extraordinary field-specific claim, not a normal national high score.
- Audit **every computed 90+ overall**, any surprisingly high ordinary attraction, and mismatches between small scope and high experience/depth. Review lower-rated outliers too; do not only cut scores.
- A **10.0** is allowed only when the destination's exact ID has been explicitly approved for that exact field under `global_ten_anchors` in [scoring.json](scoring.json). Propose a new entry only with a documented world-best argument, comparison with currently approved and not-yet-cataloged peers, and a review of existing anchors.
- Compare the strongest new cities to Beijing, Vienna, Salzburg and other strong **cities**, and new sights to the worldwide **sight** ladder. Don't borrow city excellence from Angkor Wat, the Great Wall, a bay, mountain or temple next door.
- Review score distributions as warnings of possible drift; **never** force equal country averages, fixed 90+ percentages, national quotas or automatic multipliers. A small country may genuinely outperform a larger country on a field.

## Step 6 — Write sources and an auditable decision

Source of truth:
- `countries/XX/cities/<slug>.yaml` (ID `city-xx-<slug>`)
- `countries/XX/sights/<slug>.yaml` (ID `sight-xx-<slug>`)

For a new or revised record, append its own dated, structured Markdown decision under `methodology/reviews/XX/cities.md` or `methodology/reviews/XX/sights.md`. Use the [template](review-record-template.md), linking the YAML file, naming the four peers, listing each dimension with rationale, reporting evidence status and checked source links, and recording missing evidence. Revision entries should include before/after values and a link to earlier rationale. Never erase earlier dated decisions.

**Do not edit the completed [2026 full audit](sight-review-2026-full-audit.md), [2026 summary](sight-review-2026-summary.md), one-time migrations or frozen comparison profiles to claim that new countries were included in 2026.** New records belong in new dated review files.

## Step 7 — Validate, generate and report

```bash
python -m pip install -r requirements.txt
python scripts/validate.py
python scripts/check_city_benchmarks.py
python scripts/check_sight_benchmarks.py
python scripts/generate_rankings.py --country XX
python scripts/generate_rankings.py --check
python scripts/rank.py --kind cities --limit 60
python scripts/rank.py --kind sights --limit 60
```

Use `python scripts/generate_rankings.py` to regenerate all countries when appropriate. Both generated country Markdown rankings include GPS-based Google Maps links. Do not edit generated rankings by hand. If you add a country's first city or first sight, ensure the generator's root README Done / Not done directory updates.

Before opening/merging a PR, inspect the generated country rankings and cross-country top lists. For each changed country report: total city/sight YAML records, number of new or changed entries, count with per-record Markdown reviews, count with independently checked factual sources, count with sources that have **not** been checked for the specific fact, count editorial-only, count left unassessed, and list all 9.5+ and 10.0 justifications. Explicitly disclose any missing documentation or failed checks. A passed script validates structure, **not factual correctness**.

## Future research backlog

The 2026 audit has **1,913/1,913 sight-specific editorial decisions**, but only **632 source-linked rationales** and **1,281 editorial-only rationales**. Those historical figures must not be conflated with full independent fact-checking. Researching existing unverified records is a separate, record-by-record task: link the original decision and append a new verification outcome without silently reclassifying the original audit.
