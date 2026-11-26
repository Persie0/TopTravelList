# Worldwide audit pass 102 — live backlog reconciliation

Historical batch tables are snapshots, not a live queue. The new reconciliation script checks original paths against the baseline diagnostic, derives the current queue from source YAML, and distinguishes completed records with historical deferred labels from genuinely incomplete ones. No historical disposition or rating is overwritten.

## Retained research deferrals

| Source | Reason | Evidence |
| --- | --- | --- |
| [Musée de Mayotte](../countries/YT/sights/muma.yaml) | Historic barracks closed for structural repairs, with additional cyclone damage; off-site programming is not the same as the museum visit. | https://www.fondation-patrimoine.org/les-projets/ancienne-caserne-de-dzaoudzi/60301 ; https://www.mayotte.fr/actualite/la-caserne-de-dzaoudzi |
| [Dlaboka Reka beech forest component](../countries/MK/sights/dlaboka-reka-beech-forest-component.yaml) | Strict protection zone; broader waterfall hike does not prove permitted access to the exact inscribed forest stand. | https://www.europeanbeechforests.org/world-heritage-beech-forests/north-macedonia/dlaboka-reka |
| [Alpes de la Méditerranée, Monaco component](../countries/MC/sights/les-alpes-de-la-mediterranee-monaco-component.yaml) | Tentative marine property; do not substitute land attractions or the oceanographic museum for the actual nominated area. | https://whc.unesco.org/en/tentativelists/6180/ |
| [Kasama](../countries/ZM/cities/kasama.yaml) | Government district page describes regional waterfalls and rock paintings; insufficient city-specific visitor experience to fill the missing scores. | https://www.nor.gov.zm/?page_id=1608 |
| [Phillip Island](../countries/NF/sights/phillip-island.yaml) | Parks Australia states it is not currently leading or coordinating tours for safety reasons; tourism authority states no guided tours. | https://norfolkislandnationalpark.gov.au/discover/phillip-island/ ; https://www.norfolkisland.com.au/things-to-do/nature/national-parks-reserves/phillip-island/ |

Source checks: 2026-11-26. No public access guarantee is implied.

## Usage

From the repository root, with requirements installed:

```sh
python scripts/reconcile_worldwide_backlog.py --verify-baseline
python scripts/reconcile_worldwide_backlog.py --check
```

Use the generated remaining.tsv rather than the historical batch labels for future research passes. A historical retain-unranked decision that now has a numeric rating remains an editorial conflict for review, not a reason to automatically change a rating.
