# Template — one review entry per new or revised destination

Copy the appropriate heading below into **`methodology/reviews/XX/cities.md`** or **`methodology/reviews/XX/sights.md`** (or regional `sights-*.md` files indexed there). Replace placeholders for each record; never publish a placeholder as an assessment. Keep reviews separate from the strict YAML schema.

The 2026 `sight-review-decisions-2026/*.tsv` and `sight-review-2026-*.md` files are historical and must not be repurposed for future countries.

## File heading template

```markdown
# XX — [Country name] [cities or sights]: individual worldwide reviews

- Scoring rules: [Worldwide v2](../../../rules.md)
- Workflow: [Future-country workflow](../../future-country-workflow.md)
- Scope: only newly added / revised destination IDs in this file
- Reviews are editorial judgments. Factual evidence status is recorded per item.
```

## Individual entry template

```markdown
### [sight|city]-xx-[slug] — [destination name] — YYYY-MM-DD

- YAML: [source](../../../countries/XX/[sights|cities]/[slug].yaml)
- Action: new | rescore | fact-check-only
- Precise subject: [what is included and excluded; parent/child sight or gateway-town relationship]
- Location check: [source and representative coordinates, or unresolved]
- Evidence status: fact-checked | source-linked-unverified | editorial-only | unassessed
- Independently checked factual claims:
  - [claim] — [URL, publisher, date accessed, exact support]
  - [claim] — [second URL, publisher, date accessed, exact support]
- Missing or uncertain facts: [specific gaps, or none]

#### Worldwide peer comparisons
| Peer destination (country) | Why this is the right comparison | Relative strengths / weaknesses |
| --- | --- | --- |
| [world-leading peer, country] | [same type or field; scope distinction] | [specific comparison] |
| [similar-type peer, country] | [...] | [...] |
| [second comparable peer, country] | [...] | [...] |
| [ordinary / regional peer, country] | [...] | [...] |

#### Scoring decisions
| Field | Before (when rescore) | New rating | Individual justification |
| --- | ---: | ---: | --- |
| impact | — | [0.0–10.0 or null] | [visitor-specific reason and peer] |
| uniqueness | — | [...] | [...] |
| significance | — | [...] | [...] |
| experience | — | [...] | [...] |
| depth | — | [...] | [...] |

- Applicable category scores: [category: score, ...; omit inapplicable categories]
- Computed worldwide overall: [derived from complete five-field YAML only, /100; otherwise unranked]
- High-score challenge: [explain each 9.5+ field and any 90+ overall, or "not applicable"]
- Approved 10 registry: [exact field/ID and rationale, or "none"]
- Final decision: [why this ranking is fair relative to worldwide peers, including limitations]
- Earlier decision (for revisions): [link or "none"]
- Verification still needed: [clear next fact-check, or "none"]
```

## How to use it

1. Review **every new or edited YAML record** separately. One actual decision per ID, not one blanket decision per country.
2. Use at least four **specific peers** across three countries when possible; the peer table must say *why* they are comparable, not just name them. Avoid copying the same sentence for a hundred sights.
3. Record the **individual five-dimensional justification** even if a score stays unchanged. A category value is separate from the core total.
4. Record only factual claims you actually checked. If a URL is offered but not checked for the stated claim, use `source-linked-unverified`, not `fact-checked`. `editorial-only` means no per-item supporting source checked or provided.
5. A review can legitimately remain `unassessed` with `null` dimensions if evidence is inadequate. Never guess to fill a ranking.
6. If a later pass changes a score, **append** a new dated entry. Do not rewrite the historical decision or erase the older before/after trail.
7. Counts and evidence statuses in PR summaries must come from actual entries, not assumptions about the number of YAML files.

## Distinguishing factual verification from scoring

A source may support that a building is ancient, that a site has certain collections, or that a mountain has a particular geological feature. It **does not prove** that the site deserves an impact of 9.1 or a worldwide total of 93. The rating is still a justified editorial comparison. An official listing, UNESCO inscription or Wikipedia article does not automatically mean the visit is world-leading.
