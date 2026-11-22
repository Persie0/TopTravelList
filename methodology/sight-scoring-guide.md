# Worldwide sight-scoring guide (v2)

**Mandatory for new sights in all future countries.** Read this with
[universal rules](../rules.md),
[global sight benchmarks](sight-comparison-benchmarks.md),
[189 reviewed reference profiles](sight-benchmark-profiles.txt)
and [machine-readable weights](scoring.json).

**Follow-on review:** See the [2026 item-by-item reassessment summary](sight-review-2026-summary.md) and the [full per-sight decision/diagnostic register](sight-review-2026-full-audit.md). This review distinguishes site-specific judgments from provisional records that received automated screening only. Its decisions supersede frozen 2026 benchmark profiles for revised YAML files; the historical profiles must not be reapplied.

The [incremental evidence-referenced review](sight-review-2026-summary.md) adds 379 individually sourced decisions to the original 149 explicit site corrections. The [full individual register](sight-review-2026-full-audit.md) makes the **1,272 still-unresearched sights** visible; those records retain provisional scores until independently reassessed. Category-specific excellence and historical significance must remain distinct from actual visitor impact, on-site experience and depth.

## Define the attraction and its true scale

A sight is a specific monument, museum, memorial, market, palace, temple,
beach, mountain, park, island, cave, historic complex, protected landscape,
wildlife reserve, or coherently visitable area.

**Rate the named sight, not the country, the gateway city or the entire region.**
Keep nested attractions independently rated:

- Angkor Archaeological Park is a world-defining ensemble; Angkor Wat,
  Bayon, a temple gate, a terrace and a small garden are not all
  interchangeable 99-point experiences.
- Ha Long Bay is a seascape, while one cave or beach within it is
  a smaller attraction with different depth and significance.
- The Great Wall at Jinshanling is not evidence that all nearby
  fortifications merit globally defining ratings.
- Schönbrunn Palace and Hohensalzburg Fortress deserve their own
  global comparisons; a local park or night market cannot inherit
  the maximum rating of a nearby UNESCO property.
- A solemn museum or genocide memorial can have profound worldwide
  significance even if the visit is not entertaining; evaluate
  meaningful visitor experience, not amusement alone.
- A pleasant urban beach may have a high beach category rating
  while its worldwide historical significance is comparatively low.

Separate **intrinsic long-term visitor significance** from temporary
closures, safety risks or entry restrictions. Preserve a current-access
advisory when relevant; ratings are not a claim that a site is open.

## Identical worldwide five-dimension formula

Use the existing weights in [scoring.json](scoring.json):

| Dimension | Weight | Sight-specific meaning |
| --- | ---: | --- |
| Impact | 30% | How extraordinary and memorable is this attraction versus its international peers? |
| Uniqueness | 25% | How difficult is this particular attraction to replace globally? |
| Significance | 20% | How consequential is its history, culture, architecture, natural science or ecology on a world scale? |
| Experience | 15% | How meaningful and rewarding is the actual visit, relative to its type, independent of price and temporary access? |
| Depth | 10% | How much meaningful exploration is possible at this attraction, relative to comparable attraction types? |

    overall = 10 * (0.30*impact + 0.25*uniqueness
                    + 0.20*significance + 0.15*experience
                    + 0.10*depth)

The overall is derived from source YAML and is never stored.
Use maximum one decimal for each dimension. Categories are scored
independently: nature, architecture, history, culture, food, beaches,
wildlife, adventure, nightlife, photography, family and relaxation.
A photography 9.9 does not make the overall a 99/100.
Omit inapplicable categories; unknown but applicable fields use null,
not zero. Country code, latitude and longitude are the only location fields.

## Absolute global anchors, not national percentiles

| Individual dimension | Meaning |
| ---: | --- |
| 5.0–5.9 | Ordinary visitor stop of modest distinctiveness |
| 6.0–6.9 | Worthwhile regional attraction but internationally replaceable |
| 7.0–7.9 | Strong attraction with credible worldwide-list merits |
| 8.0–8.4 | Very good internationally |
| 8.5–8.9 | Excellent relative to relevant sights around the world |
| 9.0–9.4 | Globally outstanding in that particular dimension |
| 9.5–9.9 | Rare worldwide reference attraction in that particular dimension |
| 10.0 | World-defining and explicitly approved in the exact global field/ID registry |

No country receives a fixed quota of 90+ or 95+ scores, and no
country's median must equal another. UNESCO status, visitor numbers and
being the best nationally never imply 9.5 or 10 by themselves.
**Each 10 belongs to one exact destination ID AND rating field
approved in scoring.json/global_ten_anchors.** Never introduce an
unapproved 10; validation rejects it.

## Concrete cross-country reference ratings (2026 editorial review)

| Attraction | Core fields: impact / uniqueness / significance / experience / depth | Overall /100 |
| --- | --- | ---: |
| Angkor Archaeological Park (KH) | 10 / 10 / 10 / 9.8 / 10 | 99.70 |
| Angkor Wat (KH) | 10 / 10 / 10 / 9.8 / 9.5 | 99.20 |
| Great Wall at Jinshanling (CN) | 10 / 10 / 10 / 9.8 / 9.2 | 98.90 |
| Ha Long Bay (VN) | 9.8 / 9.9 / 9.7 / 9.8 / 9.6 | 97.85 |
| Gyeongju Historic Areas (KR) | 9.5 / 9.6 / 9.8 / 9.5 / 9.8 | 96.15 |
| Ayutthaya Historical Park (TH) | 9.6 / 9.5 / 9.8 / 9.4 / 9.5 | 95.75 |
| Schönbrunn Palace (AT) | 9.4 / 9.3 / 9.6 / 9.5 / 9.3 | 94.20 |
| Hofburg Palace (AT) | 9.3 / 9.3 / 9.6 / 9.3 / 9.6 | 93.90 |
| Hohensalzburg Fortress (AT) | 9.1 / 9.1 / 9.3 / 9.4 / 8.9 | 91.65 |
| Nha Trang Beach (VN) | 8.3 / 8.1 / 7.6 / 8.8 / 8.4 | 81.95 |
| Made in Cambodia Market (KH) | 7.1 / 7.7 / 7.5 / 8.2 / 7.4 | 75.25 |
| Royal Gardens Siem Reap (KH) | 6.5 / 6.8 / 6.4 / 7.5 / 7.5 | 68.05 |

These are subjective editorial comparisons, not objective truth or
site-visit research. Read the
[global sight comparison ladder](sight-comparison-benchmarks.md)
before assigning any 9.5+ dimension.

## Checklist for EVERY new country and future sight update

1. Identify the precise attraction, its scope, and whether it should
   actually be entered as a city/town instead of a sight.
2. Identify concrete historical, natural, architectural or cultural
   facts, distinguishing independently verified significance from
   your qualitative editorial judgment.
3. Choose **at least four international reference comparisons**:
   two sights of similar type from other countries, one
   world-leading exemplar and one ordinary sight; draw from
   at least three different countries when possible.
4. Score all five dimensions independently before computing the
   overall; do not aim for a target weighted result.
5. Score applicable categories independently; do not raise impact,
   history or uniqueness just because the scenery photographs well.
6. Check overlapping/nested sights for duplicated significance,
   depth and experience; do not copy the parent's score.
7. Review EACH 9.5+ core or category field against actual global
   peers at that field and explain unusually high scores.
8. Propose a 10 only with explicit, documented worldwide comparisons
   and exact field/ID approval in methodology/scoring.json.
9. Ensure source YAML has only country_code, latitude and longitude
   for location and has no stored overall score.
10. Validate and regenerate, then compare new-country sights against
    **all existing countries' top and ordinary sights**.

For every new-country PR, include five leading sights with complete
five-dimension scores and the reason for their placement, two
cross-country comparisons (including one ordinary site), and a
review of any newly proposed 9.5+ field.

## Commands to run after every future addition/edit

    python scripts/validate.py
    python scripts/check_city_benchmarks.py
    python scripts/check_sight_benchmarks.py
    python scripts/generate_rankings.py --country XX
    python scripts/generate_rankings.py --check
    python scripts/rank.py --kind sights --limit 60

Regenerating without --country updates all 197 countries' two
Markdown ranking pages and the root README country directory, while
keeping linked GPS coordinates synchronized with YAML.

## One-time 2026 migration — do NOT reuse

The [complete 1733-sight before/after audit](sight-calibration-audit.md)
and [frozen 189 profiles](sight-benchmark-profiles.txt) document a
historic correction of inconsistent authoring batches.
**Only 189 sight records were individually benchmarked against peers.**
The other 1544 got a deterministic conservative correction rather than
an individual research assessment. The archived migration script has
a marker guard and refuses to rerun on updated data. Never apply those
country-cohort curves to future countries; rate future sights
DIRECTLY against the worldwide comparisons in this guide.
