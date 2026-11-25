# Recent-country verification — 2026-11-25

Audited snapshot: `700f8967e7cab196e839503b1e333470f96b16f2` (Albania merge). Scope: all 12 countries added since workflow PR #22, including Sri Lanka. [Public Playground audit](https://github.com/Persie0/Playground/actions/runs/45642871971); [audit workflow](https://github.com/Persie0/Playground/blob/main/.github/workflows/toptravellist-recent-audit-20261125.yml).

## Automated results

| Country | Cities | Sights | Editorial-only | Source-linked, unverified | Unassessed | Linked numeric peer references |
|---|---:|---:|---:|---:|---:|---:|
| IN | 97 | 333 | 369 | 61 | 0 | 0 |
| JP | 87 | 347 | 396 | 38 | 0 | 0 |
| ID | 79 | 343 | 359 | 63 | 0 | 0 |
| MY | 65 | 213 | 250 | 28 | 0 | 0 |
| SG | 1 | 99 | 17 | 83 | 0 | 401 |
| BN | 9 | 41 | 0 | 50 | 0 | 200 |
| CZ | 61 | 145 | 153 | 53 | 0 | 884 |
| LA | 42 | 144 | 0 | 185 | 1 | 740 |
| BA | 44 | 101 | 99 | 46 | 0 | 580 |
| ME | 33 | 94 | 64 | 63 | 0 | 508 |
| LK | 55 | 178 | 110 | 121 | 2 | 924 |
| AL | 35 | 95 | 67 | 63 | 0 | 520 |
| Total | 608 | 2133 | 1884 | 854 | 3 | 4757 |

All standard validators and generated rankings passed. 2741/2741 records have named review sections; 2738 ranked, three intentionally unranked (Phou Bia, Pidurutalagala, Ritigala Strict Natural Reserve). Zero normalized duplicate names within country/kind. All 4757 parsed linked numerical references match existing source YAML; this covers 1174 ranked records, not the complete 2738. Initial India, Japan, Indonesia and Malaysia reviews use named/unlinked comparisons; the audit did not successfully resolve those in this run, so do not claim their numerical peer evidence verified. Ten initial core vectors/totals differ from current YAML: six India changes documented in secondary calibration, Japan Nagasaki/Hiroshima/Fushimi Inari, Indonesia Lorentz, with dated reassessment records. Initial notes must remain historical. 440 current ranked records meet exceptional thresholds. The initial-review parser finds 81 missing high-score challenge markers (80 Indonesia, one Japan) and five generic markers (Japan); later reassessments exist and need separate record-level reconciliation. This is not a claim that all 86 have no later challenge. No perfect-ten approval changes or scoring weights modified.

## Geospatial screening

The Natural Earth 1:10m country polygon screen completed for all 2741 records: 2413 inside, 256 within 0.04 degrees, 66 between 0.04 and 0.25 degrees outside, 6 more than 0.25 degrees outside. Degree thresholds are not precise distance measurements. Small islands, offshore features, disputed/administrative borders and simplified polygons produce false positives; passing the screen is not a site-level coordinate check. The six larger outliers are all maritime or archipelago records: Wayag Islands, Taka Bonerate, Krakatau, Raja Ampat, Sipadan and Layang-Layang. Taka Bonerate's point falls inside [UNESCO tentative-list geographic extent](https://whc.unesco.org/en/tentativelists/2005/); Krakatau matches [Smithsonian volcanic reference](https://volcano.si.edu/volcano.cfm?bgvn=1&snum=krakatau&vn=262000); Sipadan matches [island mapping](https://mapcarta.com/Sipadan), Layang-Layang matches [KBA coordinates](https://www.keybiodiversityareas.org/en/site/factsheet/16035). Raja Ampat is a wide marine archipelago; [UNESCO biosphere profile](https://www.unesco.org/en/mab/raja-ampat?codespec=701bE00000gX7qZQAS) provides another regional reference point, not an entrance. Wayag has conflicting source hemisphere notation: [geopark](https://rajaampatgeopark.com/geopark-center/our-geosites/ra-14/) and [2022 study](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2022.815094/full) say south, while [2018 expedition survey](https://birdsheadseascape.com/download/media/Elysium-Heart-of-The-Coral-Triangle-Expedition-Report-V-Final.pdf) and [local conservation survey](https://ibcraja4.org/abiotic) report north. Preserve existing northern point pending better spatial evidence; no speculative sign change. Pangong Tso and other border locations require separate scope review. Many other near-outside sites remain to verify individually.

## Targeted coordinate corrections (scores unchanged)

Sources checked 2026-11-25. These are representative map points, not access/entrance guarantees. Prior review files remain historical.

| Record | Before (lat, lon) | After (lat, lon) | Evidence and rationale |
|---|---|---|---|
| [that-phon-stupa](../countries/LA/sights/that-phon-stupa.yaml) | 16.135, 104.96 | 16.36749, 105.02781 | [Coordinate source](https://www.asiaphotos.org/LAOS/PROVINCES/SAVANNAKHET/PHOTOS/Wat%20Phra%20That%20Phon/indexb.html) — Named-site GPS corroborated by Ban Phonthat village and https://www.tourismlaos.org/2026/02/04/that-phon-stupa-heuan-hin-recognized-as-national-heritage-sites-in-savannakhet/. Original point was substantially south/west. |
| [heuan-hin-stone-house](../countries/LA/sights/heuan-hin-stone-house.yaml) | 16.13, 104.95 | 16.21427, 105.03129 | [Coordinate source](https://www.asiaphotos.org/LAOS/PROVINCES/SAVANNAKHET/PHOTOS/Huen%20Hin/indexb.html) — Named-site GPS corroborated by https://evendo.com/locations/laos/savannakhet-province/attraction/huen-hin; separate from That Phon. |
| [phou-den-din-national-protected-area](../countries/LA/sights/phou-den-din-national-protected-area.yaml) | 21.83, 102.68 | 21.951984, 102.422338 | [Coordinate source](https://en.wikipedia.org/wiki/Phou_Den_Din_National_Protected_Area) — Published representative point falls within the older geographic extent reported at https://www.ecotourismlaos.com/directory/protected_areas/phoudaendin. Conflicting national-report extents mean this remains approximate; not an entrance. |
| [st-teresa-catholic-church-savannakhet](../countries/LA/sights/st-teresa-catholic-church-savannakhet.yaml) | 16.558, 104.75 | 16.55718, 104.74885 | [Coordinate source](https://www.asiaphotos.org/LAOS/PROVINCES/SAVANNAKHET/PHOTOS/St%20Theresa%20s%20Catholic%20Church/indexb.html) — Named building point separates church from general old-town representative point; corroborating https://www.wikidata.org/wiki/Q25041111 (slightly different point). |
| [bharatpur-beach-shaheed-dweep](../countries/IN/sights/bharatpur-beach-shaheed-dweep.yaml) | 11.8268, 93.0460 | 11.83787, 93.03267 | [Coordinate source](https://mapcarta.com/W639633488) — Named beach mapping, OpenStreetMap way 639633488. |
| [kondoi-beach](../countries/JP/sights/kondoi-beach.yaml) | 24.3240, 124.0680 | 24.32537, 124.07702 | [Coordinate source](https://mapcarta.com/W737451274) — Named beach mapping, OpenStreetMap way 737451274. |
| [benesse-house-museum](../countries/JP/sights/benesse-house-museum.yaml) | 34.4468, 133.9911 | 34.44523, 133.99066 | [Coordinate source](https://mapcarta.com/36389896) — Named museum building point, OpenStreetMap way 1357191882. |
| [jizera-mountain-beech-forests](../countries/CZ/sights/jizera-mountain-beech-forests.yaml) | 50.8580, 15.1900 | 50.86, 15.16 | [Coordinate source](https://whc.unesco.org/en/list/1133/maps/) — UNESCO Jizera Mountains component representative point N50 51 36 E15 9 36, converted to decimal. |

Bangaram's approximate point is consistent with [government tourism location](https://lakshadweep.gov.in/islands/bangaram/) and [island mapping](https://mapcarta.com/14896806). Albania's two beech forest components and Bosnia's Janj were checked against the [UNESCO component register](https://whc.unesco.org/en/list/1133/maps/); Montenegro's three stećci component coordinates and Bosnia's Radimlja, Boljuni and Dugo Polje were checked against the [stećci component register](https://whc.unesco.org/en/list/1504/maps/). These targeted checks do not change the original evidence classifications or certify every other claim.

## Remaining factual and scoring work

No destination has full independent claim-by-claim fact verification recorded. Most precise positions, access claims, identities/aliases, factual rationale claims, category-specific comparisons and completeness of each inventory still need individual external research. Prioritize named location anomalies, all 440 exceptional records (reconcile later reviews before changing scores), and the 1564 ranked records without parsed linked numeric peers. The first two audit attempts failed due to the supplementary parser's handling of punctuation and null score fields; those audit-code errors were fixed before the completed run. The completed run does not verify source-link reachability for every URL or compare all peer types for quality. No claim of comprehensive factual completion.
