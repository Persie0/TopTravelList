# Evidence, verification and scoring quality standard

Applies to all future cities, sights, and reviews of existing entries. Read alongside the [new-country workflow](future-country-workflow.md) and [individual decision template](review-record-template.md). This separates **individual editorial review**, **fact-checking**, and **worldwide score calibration**.

## Evidence levels (per destination, not per country)

| Status in review Markdown | Meaning | Safe claim |
| --- | --- | --- |
| `fact-checked` | Reviewer actually inspected appropriate sources about the **exact named destination**, checked material claims against them, and recorded URLs with claim-level support and access date. | Material facts used in the rationale were independently checked; the score is still editorial. |
| `source-linked-unverified` | A source link exists but the relevant claims were not fully checked, its identity/location match is ambiguous, or it does not support the specific claim. | A possible source is linked; factual verification remains open. |
| `editorial-only` | Destination has a named, individualized five-dimension judgment but no checked supporting source. | An individual editorial decision exists; not independently verified. |
| `unassessed` | Evidence is insufficient to assess at least one required core field. | Unranked or incomplete; no complete total claim. |

These statuses are **not score levels**. They do not add points. A generic Google Maps search URL, Wikipedia match, UNESCO parent-site page, place-name search result, automatically generated reason, or four unrelated comparison links does not qualify as fact-checking for a particular destination.

## What qualifies as a useful checked source?

- The source describes the correct **destination identity and geographic scope**, not just its city, broad park, neighboring temple or similarly named attraction.
- Record **publisher, direct URL, access date, factual assertion and what on the page supports it**. Explicitly state when the page does not confirm the claim.
- Prefer an official institution/site authority, relevant conservation/heritage organization, recognized geographic reference or substantive independent reporting. Where practical, triangulate with **two independent sources**, preferably one direct/primary and one independent; disclose when only one exists.
- Sources support **verifiable facts** (age, collections, trail/visit features, UNESCO coverage, geology, public access, geographic location). They **do not establish** a subjective impact, uniqueness, experience or total score.
- If official promotional material is the only source, label its limitations. Do not substitute popularity, star ratings, search-result frequency, or copied tourism slogans for evidence.
- Never invent sources, claim to have opened a URL that was not reviewed, or treat an automatic search match as a human fact-check.

## Access-independent attraction quality (owner instruction, 2026-11-27)

Rank the attraction on its normal, historical, or reasonably restored lawful visitor experience and intrinsic qualities. Temporary closures, renovations, travel advisories, security restrictions, and present-day booking or permit availability are **not** reasons to withhold or reduce quality scores. Apply this retroactively to previously deferred records. Permanent access restrictions also do not prevent an editorial ranking when intrinsic qualities can be assessed. Document restrictions independently from ranking; a rating is never a representation of current access, safety, or a forecast of reopening. Use historical evidence where possible and explicitly label hypothetical restored-access estimates as provisional/source-linked-unverified. Do not invent visitor activities, reconstruction, exhibitions, guaranteed wildlife encounters, or access to sacred/private areas. For identified destinations, the owner requires a complete numerical assessment: use a conservative provisional estimate where source or scope evidence is limited. Do not invent facts, visits or boundaries. If a purported destination cannot be identified at all or is an exact duplicate, resolve its identity or alias explicitly rather than inventing a score. Keep normal intrinsic experience limitations (scale, depth, terrain, seasonal features) separate from temporary access constraints.

## Calibration safeguards

1. **Scope** — Test what the record actually represents. UNESCO or regional prominence belongs to the correct entity and cannot be transferred to small sub-sites.
2. **Dimensions** — Significance is not experience; novelty is not depth; scenic photography is not general impact. Give each of the five fields its own rationale.
3. **World peers** — At least four individually named peers including world-leading and ordinary counterparts, preferably three countries. Explain why the new record is above/below each relevant peer; never use a country-relative scale.
4. **High marks** — Challenge every **9.5+ rating**, every surprising **90+ derived overall**, every perfect 10 and score clusters that seem implausibly high. These are flags for review, *not* automatic downgrades or per-country quotas.
5. **Category independence** — A high architecture, history or nature category can coexist with moderate depth or visitor experience. Omit irrelevant categories.
6. **Numerical completion (owner instruction, 2026-11-28)** — Complete all core fields and explicitly applicable category fields for identified destinations using individual editorial estimates where necessary. Distinguish provisional estimates from independently checked facts; do not defer a numerical assessment solely because evidence or access is limited. Omit inapplicable categories. Preserve historical dispositions and record the superseding decision.
7. **Preserve provenance** — Keep source YAML authoritative, historical 2026 logs intact, and append new dated reviews. Do not claim editorial coverage equals independent source-backed assessment.
8. **Reproducibility** — Run structural validation, both benchmark diagnostics, regenerate ranking Markdown, inspect worldwide leaders and report actual successes/failures.

## PR quality checklist

- [ ] No obvious missing major destinations, duplicate names/aliases, false scopes, or wrong representative coordinates.
- [ ] Each added/revised YAML has its **own** Markdown review entry with explicit status and non-generic reasoning.
- [ ] Each reviewed destination has four meaningful worldwide comparisons, not just a shared list of famous names.
- [ ] Every material source-backed factual claim has a checked URL; uncertain matches are flagged.
- [ ] Every 9.5+ field, unusual 90+ overall, and any new 10 is specifically documented; no implicit whitelist expansion.
- [ ] Completed, sourced-but-unverified, editorial-only and unassessed counts are separately disclosed.
- [ ] `validate.py`, both benchmark checkers and `generate_rankings.py --check` passed, or exceptions are transparently reported.
- [ ] Generated country rankings, Google Maps links, README directory, and cross-country comparisons were inspected.
- [ ] No legacy calibration/review script was rerun and no frozen 2026 audit was rewritten.
