# Worldwide bias review — 26 November 2026 (first correction pass)

Scope: the 197 registered country entries, 4,169 city YAMLs and 11,391 sight YAMLs on base commit becddd271e08db22e6e4a8c5758ffdb619577c52. This pass does not claim 15,560 independently researched judgments. No quota, national multiplier or change to V2 weights is applied. The initial country screening is performed by [Playground audit run](https://github.com/Persie0/Playground/actions/runs/45730315422). Its statistical output is diagnostic, not proof of bias. Country means depend on what was selected for inclusion and cannot be interpreted as national travel-quality scores.

Four individual corrections: [Dunhuang](reviews/CN/cities.md), [Siem Reap](reviews/KH/cities.md), [Golden Temple](reviews/IN/sights-north.md), [Srirangam](reviews/IN/sights-tamil-andhra-telangana.md). Each contains separately justified fields, checked scope sources and worldwide peers. The historical city benchmark documents are snapshots and not silently rewritten. A second pass explicitly revises the legacy perfect-score registry. Before the change every approved 10 belonged to CN, KH or TH. This is a historical geographic coverage artifact and a reason to reopen comparisons, not a reason to award 10 by country quota. Giza (significance), Taj Mahal (architecture), Grand Canyon (impact) and Galápagos (significance) independently qualify on documented field-specific merits. Jinshanling retains visual impact and photography 10, but loses the four parent-scope 10s in uniqueness, significance, architecture and history. See the dated reassessments in [China](reviews/CN/sights.md), [Egypt](reviews/EG/sights.md), [India](reviews/IN/sights-north.md), [United States](reviews/US/sights.md) and [Ecuador](reviews/EC/sights.md). Historical benchmark values remain labeled historical; V2 dimensions and weights are unchanged. Further high score and low score review remains outstanding; no blanket adjustment is authorized.

## Baseline worldwide screen (before corrections)

The completed run scanned 15560 YAMLs (14033 ranked; 1527 unassessed), with 1766 overall 90+ and 160 overall 95+ records. Both benchmark scripts passed. Their existing diagnostic thresholds identified these country cohorts:

- Cities, mean above 84 with at least 15 assessed: BE, CH, DE, ES, FR, GB, GR, HR, HU, IT, NL, PL, PT, RO, SK, US.
- Sights, over 35% of assessed 90+ with at least 40 assessed: CH, CN, DE, ES, FR, GB, GR, IN, IT, PT.

The geographic pattern is a priority for deeper same-type research; differences in inventory selection may also explain it. Do not normalize by nation. The top 100 cities and top 100 sights are in the linked run logs; those names were inspected for obvious scope and rating issues, not all independently fact-checked. The full country diagnostic below is the reproducible baseline, not the post-correction ranking.

| Code | City total/ranked | City median | Cities 90+/95+/97+ | Sight total/ranked | Sight median | Sights 90+/95+/97+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| AD | 18/18 | 72.125 | 0/0/0 | 38/37 | 80.050 | 0/0/0 |
| AE | 14/14 | 75.300 | 1/0/0 | 57/46 | 82.150 | 3/0/0 |
| AF | 10/3 | 80.100 | 0/0/0 | 23/7 | 85.200 | 0/0/0 |
| AG | 10/10 | 72.325 | 0/0/0 | 32/31 | 79.200 | 1/0/0 |
| AL | 35/35 | 77.150 | 0/0/0 | 95/95 | 83.000 | 5/0/0 |
| AM | 20/20 | 74.650 | 0/0/0 | 55/51 | 84.850 | 7/0/0 |
| AO | 8/6 | 78.900 | 0/0/0 | 17/13 | 85.050 | 1/0/0 |
| AR | 40/40 | 75.475 | 1/0/0 | 65/61 | 86.100 | 10/3/0 |
| AT | 45/45 | 69.750 | 1/0/0 | 133/133 | 81.350 | 13/0/0 |
| AU | 12/12 | 79.775 | 0/0/0 | 39/36 | 88.500 | 11/1/0 |
| AZ | 16/16 | 78.700 | 0/0/0 | 40/30 | 83.675 | 1/0/0 |
| BA | 44/44 | 73.775 | 1/0/0 | 101/101 | 82.200 | 2/0/0 |
| BB | 10/10 | 75.500 | 0/0/0 | 35/33 | 80.250 | 0/0/0 |
| BD | 15/13 | 74.000 | 0/0/0 | 42/33 | 82.950 | 1/0/0 |
| BE | 18/18 | 84.100 | 3/0/0 | 64/52 | 86.750 | 5/0/0 |
| BF | 9/3 | 76.300 | 0/0/0 | 35/11 | 83.250 | 1/0/0 |
| BG | 18/18 | 82.675 | 0/0/0 | 46/43 | 86.750 | 6/0/0 |
| BH | 15/14 | 68.075 | 0/0/0 | 40/38 | 77.975 | 0/0/0 |
| BI | 12/12 | 65.275 | 0/0/0 | 26/23 | 77.150 | 0/0/0 |
| BJ | 18/17 | 72.900 | 0/0/0 | 34/22 | 80.200 | 0/0/0 |
| BN | 9/9 | 65.200 | 0/0/0 | 41/41 | 75.400 | 1/0/0 |
| BO | 33/33 | 74.650 | 1/0/0 | 56/52 | 84.975 | 12/1/0 |
| BR | 42/42 | 77.875 | 2/0/0 | 85/72 | 86.975 | 15/2/0 |
| BS | 12/12 | 71.350 | 0/0/0 | 34/24 | 81.600 | 1/0/0 |
| BT | 33/33 | 77.850 | 0/0/0 | 89/85 | 85.050 | 12/0/0 |
| BW | 22/21 | 67.200 | 0/0/0 | 38/35 | 81.550 | 5/1/1 |
| BY | 14/14 | 81.350 | 0/0/0 | 35/27 | 85.650 | 3/0/0 |
| BZ | 18/18 | 71.150 | 0/0/0 | 61/58 | 81.150 | 5/0/0 |
| CA | 16/16 | 81.925 | 0/0/0 | 51/48 | 87.450 | 12/1/0 |
| CD | 8/3 | 77.400 | 0/0/0 | 17/10 | 87.475 | 4/0/0 |
| CF | 10/2 | 71.025 | 0/0/0 | 25/8 | 79.475 | 3/0/0 |
| CG | 12/12 | 68.000 | 0/0/0 | 29/21 | 80.500 | 4/0/0 |
| CH | 20/20 | 85.175 | 0/0/0 | 45/42 | 88.850 | 17/0/0 |
| CI | 10/7 | 79.400 | 0/0/0 | 20/12 | 85.675 | 1/0/0 |
| CL | 33/33 | 74.900 | 0/0/0 | 67/64 | 85.875 | 8/2/0 |
| CM | 10/7 | 79.100 | 0/0/0 | 28/14 | 88.000 | 3/0/0 |
| CN | 231/231 | 78.950 | 12/3/1 | 490/490 | 88.975 | 179/20/8 |
| CO | 46/44 | 74.175 | 1/0/0 | 55/48 | 85.050 | 9/0/0 |
| CR | 28/28 | 73.525 | 0/0/0 | 62/55 | 84.000 | 5/1/0 |
| CU | 12/12 | 79.625 | 1/0/0 | 36/29 | 82.600 | 3/0/0 |
| CV | 24/24 | 73.675 | 0/0/0 | 47/46 | 79.325 | 2/0/0 |
| CY | 16/16 | 77.025 | 0/0/0 | 38/31 | 83.150 | 0/0/0 |
| CZ | 61/61 | 79.400 | 1/0/0 | 145/145 | 86.050 | 13/0/0 |
| DE | 30/30 | 87.900 | 3/0/0 | 97/86 | 89.750 | 36/0/0 |
| DJ | 10/10 | 68.375 | 0/0/0 | 25/21 | 79.800 | 2/0/0 |
| DK | 18/18 | 81.875 | 1/0/0 | 43/43 | 86.450 | 3/0/0 |
| DM | 14/14 | 73.100 | 0/0/0 | 32/32 | 81.325 | 1/0/0 |
| DO | 12/12 | 74.475 | 0/0/0 | 34/23 | 83.450 | 1/0/0 |
| DZ | 11/11 | 83.100 | 0/0/0 | 25/15 | 88.550 | 7/1/0 |
| EC | 36/36 | 71.525 | 1/0/0 | 55/52 | 84.350 | 7/1/1 |
| EE | 15/15 | 74.150 | 0/0/0 | 42/38 | 82.600 | 1/0/0 |
| EG | 10/10 | 82.700 | 1/0/0 | 35/30 | 92.450 | 21/6/2 |
| ER | 13/10 | 69.425 | 1/0/0 | 30/25 | 80.350 | 1/0/0 |
| ES | 22/22 | 88.575 | 7/1/0 | 113/95 | 89.700 | 40/4/0 |
| ET | 8/8 | 80.275 | 0/0/0 | 23/17 | 89.900 | 8/2/1 |
| FI | 20/20 | 80.100 | 0/0/0 | 55/52 | 85.575 | 5/0/0 |
| FJ | 7/7 | 73.150 | 0/0/0 | 18/16 | 84.100 | 4/0/0 |
| FM | 6/5 | 71.550 | 0/0/0 | 14/12 | 84.550 | 2/0/0 |
| FR | 25/25 | 87.700 | 3/1/1 | 107/87 | 90.550 | 54/3/0 |
| GA | 14/14 | 68.275 | 0/0/0 | 32/22 | 83.425 | 3/0/0 |
| GB | 30/30 | 85.125 | 5/1/0 | 78/77 | 88.950 | 33/0/0 |
| GD | 12/12 | 72.175 | 0/0/0 | 33/27 | 81.000 | 0/0/0 |
| GE | 14/14 | 78.775 | 0/0/0 | 38/37 | 82.300 | 1/0/0 |
| GH | 20/20 | 72.275 | 0/0/0 | 50/45 | 79.450 | 2/0/0 |
| GM | 16/16 | 69.950 | 0/0/0 | 31/28 | 77.125 | 0/0/0 |
| GN | 14/14 | 70.650 | 0/0/0 | 30/18 | 77.925 | 0/0/0 |
| GQ | 13/13 | 71.350 | 0/0/0 | 26/18 | 79.350 | 0/0/0 |
| GR | 18/18 | 87.000 | 2/0/0 | 65/59 | 89.350 | 27/1/0 |
| GT | 12/12 | 79.325 | 1/0/0 | 37/32 | 82.925 | 3/0/0 |
| GW | 13/13 | 71.700 | 0/0/0 | 25/17 | 77.900 | 2/0/0 |
| GY | 18/18 | 69.225 | 0/0/0 | 39/33 | 79.250 | 2/0/0 |
| HN | 31/31 | 74.450 | 0/0/0 | 59/56 | 81.250 | 4/1/0 |
| HR | 22/22 | 85.675 | 2/0/0 | 55/52 | 88.000 | 12/0/0 |
| HT | 12/12 | 71.950 | 0/0/0 | 32/20 | 81.300 | 2/0/0 |
| HU | 18/18 | 84.125 | 1/0/0 | 50/44 | 87.600 | 6/0/0 |
| ID | 79/79 | 75.550 | 1/0/0 | 343/343 | 85.550 | 52/4/3 |
| IE | 20/20 | 80.950 | 0/0/0 | 46/43 | 87.550 | 5/0/0 |
| IL | 12/12 | 80.200 | 0/0/0 | 41/30 | 86.425 | 4/0/0 |
| IN | 97/97 | 81.750 | 5/0/0 | 333/333 | 89.550 | 150/29/12 |
| IQ | 14/11 | 78.450 | 0/0/0 | 38/21 | 85.100 | 3/0/0 |
| IR | 15/3 | 87.750 | 0/0/0 | 55/17 | 86.150 | 2/0/0 |
| IS | 15/15 | 80.200 | 0/0/0 | 56/47 | 87.450 | 15/1/0 |
| IT | 25/25 | 89.850 | 12/3/1 | 134/111 | 90.950 | 76/7/1 |
| JM | 11/11 | 77.150 | 0/0/0 | 26/24 | 81.325 | 1/0/0 |
| JO | 21/21 | 73.050 | 0/0/0 | 67/63 | 82.650 | 7/2/1 |
| JP | 87/87 | 80.100 | 4/2/0 | 347/347 | 86.450 | 53/5/0 |
| KE | 6/6 | 82.500 | 0/0/0 | 44/29 | 88.850 | 8/1/0 |
| KG | 18/18 | 71.350 | 0/0/0 | 46/34 | 83.800 | 5/0/0 |
| KH | 72/72 | 76.025 | 1/0/0 | 260/260 | 84.750 | 27/7/2 |
| KI | 12/8 | 66.225 | 0/0/0 | 13/12 | 76.350 | 0/0/0 |
| KM | 14/14 | 73.500 | 0/0/0 | 31/29 | 81.050 | 1/0/0 |
| KN | 11/11 | 72.600 | 0/0/0 | 30/27 | 78.650 | 1/0/0 |
| KP | 8/1 | 81.900 | 0/0/0 | 22/7 | 78.100 | 0/0/0 |
| KR | 82/82 | 73.800 | 2/0/0 | 284/284 | 84.650 | 26/1/0 |
| KW | 12/12 | 67.925 | 0/0/0 | 43/36 | 75.950 | 0/0/0 |
| KZ | 18/18 | 74.025 | 0/0/0 | 59/41 | 84.300 | 4/0/0 |
| LA | 42/42 | 71.525 | 1/0/0 | 144/143 | 80.050 | 9/0/0 |
| LB | 13/8 | 80.375 | 0/0/0 | 37/20 | 85.250 | 4/1/0 |
| LC | 12/12 | 74.600 | 0/0/0 | 27/26 | 81.275 | 1/0/0 |
| LI | 15/15 | 70.400 | 0/0/0 | 34/34 | 75.975 | 0/0/0 |
| LK | 55/55 | 74.600 | 2/0/0 | 178/176 | 82.325 | 21/2/0 |
| LR | 14/14 | 70.750 | 0/0/0 | 26/18 | 76.300 | 0/0/0 |
| LS | 16/16 | 68.900 | 0/0/0 | 38/33 | 78.650 | 1/0/0 |
| LT | 18/18 | 78.100 | 1/0/0 | 37/37 | 84.050 | 3/0/0 |
| LU | 15/15 | 76.550 | 0/0/0 | 32/32 | 81.850 | 1/0/0 |
| LV | 18/18 | 77.100 | 1/0/0 | 38/38 | 83.075 | 1/0/0 |
| LY | 11/4 | 82.525 | 0/0/0 | 20/15 | 87.400 | 5/1/0 |
| MA | 12/12 | 85.825 | 2/0/0 | 32/24 | 88.650 | 7/0/0 |
| MC | 1/1 | 84.200 | 0/0/0 | 29/27 | 78.350 | 0/0/0 |
| MD | 18/15 | 69.300 | 0/0/0 | 33/30 | 80.375 | 0/0/0 |
| ME | 33/33 | 75.350 | 0/0/0 | 94/94 | 82.250 | 7/0/0 |
| MG | 6/5 | 79.250 | 0/0/0 | 29/19 | 90.350 | 11/1/0 |
| MH | 11/7 | 70.250 | 0/0/0 | 22/10 | 76.750 | 1/0/0 |
| MK | 14/14 | 77.200 | 0/0/0 | 33/32 | 86.075 | 2/0/0 |
| ML | 11/7 | 79.300 | 1/0/0 | 33/11 | 87.200 | 3/0/0 |
| MM | 12/7 | 73.000 | 0/0/0 | 39/17 | 84.850 | 2/0/0 |
| MN | 18/18 | 68.325 | 0/0/0 | 50/36 | 82.700 | 4/0/0 |
| MR | 10/5 | 72.350 | 0/0/0 | 17/10 | 84.650 | 1/0/0 |
| MT | 23/23 | 76.550 | 1/0/0 | 37/37 | 83.600 | 6/0/0 |
| MU | 22/22 | 70.975 | 0/0/0 | 63/59 | 79.450 | 1/0/0 |
| MV | 25/25 | 72.350 | 0/0/0 | 42/40 | 81.350 | 6/0/0 |
| MW | 18/18 | 72.575 | 0/0/0 | 34/29 | 81.000 | 2/0/0 |
| MX | 36/36 | 81.850 | 1/0/0 | 111/82 | 85.675 | 9/1/0 |
| MY | 65/65 | 70.250 | 1/0/0 | 213/213 | 81.500 | 15/1/0 |
| MZ | 7/4 | 81.000 | 0/0/0 | 16/11 | 87.300 | 4/0/0 |
| NA | 7/7 | 78.850 | 0/0/0 | 21/17 | 89.650 | 8/1/0 |
| NE | 10/5 | 78.150 | 0/0/0 | 26/8 | 85.000 | 1/0/0 |
| NG | 12/10 | 80.675 | 0/0/0 | 25/14 | 85.425 | 2/0/0 |
| NI | 13/13 | 74.000 | 0/0/0 | 30/26 | 83.250 | 1/0/0 |
| NL | 20/20 | 84.725 | 1/0/0 | 51/50 | 86.625 | 8/1/0 |
| NO | 20/20 | 82.500 | 1/0/0 | 49/41 | 88.450 | 12/0/0 |
| NP | 49/49 | 78.650 | 3/0/0 | 123/123 | 85.900 | 35/5/2 |
| NR | 6/4 | 61.200 | 0/0/0 | 6/6 | 66.450 | 0/0/0 |
| NZ | 12/12 | 80.400 | 0/0/0 | 24/22 | 88.375 | 7/0/0 |
| OM | 24/24 | 75.800 | 0/0/0 | 60/54 | 82.200 | 2/0/0 |
| PA | 22/22 | 73.800 | 0/0/0 | 53/45 | 83.000 | 4/1/0 |
| PE | 36/36 | 72.325 | 1/0/0 | 66/63 | 86.500 | 16/1/1 |
| PG | 7/7 | 73.750 | 0/0/0 | 19/13 | 85.700 | 2/0/0 |
| PH | 15/15 | 76.400 | 0/0/0 | 50/36 | 86.400 | 3/0/0 |
| PK | 14/13 | 76.750 | 1/0/0 | 58/36 | 84.800 | 3/0/0 |
| PL | 22/22 | 84.000 | 3/0/0 | 76/59 | 88.500 | 15/1/0 |
| PS | 10/4 | 80.100 | 0/0/0 | 36/11 | 86.000 | 1/0/0 |
| PT | 20/20 | 85.250 | 2/0/0 | 48/44 | 90.150 | 23/0/0 |
| PW | 7/5 | 72.550 | 0/0/0 | 22/16 | 83.575 | 2/0/0 |
| PY | 34/34 | 69.850 | 0/0/0 | 52/46 | 78.850 | 1/0/0 |
| QA | 14/13 | 67.650 | 0/0/0 | 55/51 | 76.450 | 3/0/0 |
| RO | 20/20 | 84.200 | 0/0/0 | 58/47 | 88.700 | 11/0/0 |
| RS | 18/18 | 82.125 | 0/0/0 | 43/40 | 87.425 | 4/0/0 |
| RU | 20/20 | 81.450 | 2/0/0 | 43/15 | 89.250 | 6/0/0 |
| RW | 18/18 | 69.375 | 0/0/0 | 47/45 | 80.400 | 3/1/0 |
| SA | 18/16 | 74.375 | 0/0/0 | 49/33 | 82.800 | 1/0/0 |
| SB | 9/9 | 66.550 | 0/0/0 | 16/13 | 79.600 | 1/0/0 |
| SC | 14/14 | 68.525 | 0/0/0 | 49/46 | 80.475 | 3/0/0 |
| SD | 9/5 | 79.250 | 0/0/0 | 26/13 | 90.150 | 7/0/0 |
| SE | 23/23 | 81.350 | 1/0/0 | 64/63 | 86.350 | 10/0/0 |
| SG | 1/1 | 92.200 | 1/0/0 | 99/99 | 81.250 | 2/0/0 |
| SI | 18/18 | 82.725 | 0/0/0 | 45/42 | 88.050 | 9/0/0 |
| SK | 15/15 | 84.300 | 0/0/0 | 61/54 | 87.425 | 6/0/0 |
| SL | 13/13 | 70.100 | 0/0/0 | 33/27 | 80.050 | 0/0/0 |
| SM | 14/14 | 68.725 | 0/0/0 | 25/25 | 77.950 | 1/0/0 |
| SN | 8/6 | 83.575 | 0/0/0 | 23/18 | 88.225 | 3/0/0 |
| SO | 10/3 | 74.800 | 0/0/0 | 13/5 | 79.800 | 1/0/0 |
| SR | 20/19 | 67.050 | 0/0/0 | 37/30 | 80.850 | 0/0/0 |
| SS | 10/1 | 71.550 | 0/0/0 | 20/6 | 72.125 | 0/0/0 |
| ST | 12/12 | 69.125 | 0/0/0 | 40/38 | 80.550 | 2/0/0 |
| SV | 24/24 | 73.325 | 0/0/0 | 54/50 | 79.875 | 0/0/0 |
| SY | 10/7 | 80.800 | 0/0/0 | 31/19 | 87.300 | 3/0/0 |
| SZ | 15/15 | 68.100 | 0/0/0 | 30/29 | 78.300 | 0/0/0 |
| TD | 10/5 | 72.200 | 0/0/0 | 25/14 | 88.275 | 6/1/0 |
| TG | 16/14 | 72.575 | 0/0/0 | 31/28 | 77.150 | 1/0/0 |
| TH | 69/69 | 70.900 | 2/0/0 | 206/206 | 83.750 | 16/2/0 |
| TJ | 14/14 | 72.875 | 0/0/0 | 45/32 | 82.975 | 5/0/0 |
| TL | 24/24 | 73.125 | 0/0/0 | 38/36 | 78.275 | 2/0/0 |
| TM | 12/11 | 69.100 | 0/0/0 | 40/23 | 82.200 | 1/0/0 |
| TN | 11/11 | 79.950 | 0/0/0 | 30/19 | 87.700 | 6/0/0 |
| TO | 7/6 | 69.850 | 0/0/0 | 18/16 | 79.375 | 0/0/0 |
| TR | 20/20 | 84.025 | 1/0/0 | 48/40 | 87.900 | 6/0/0 |
| TT | 12/12 | 72.800 | 0/0/0 | 29/28 | 80.075 | 0/0/0 |
| TV | 9/4 | 67.700 | 0/0/0 | 14/5 | 78.200 | 0/0/0 |
| TW | 64/64 | 76.150 | 1/0/0 | 180/180 | 84.200 | 11/0/0 |
| TZ | 5/5 | 82.600 | 1/0/0 | 27/18 | 91.200 | 13/3/1 |
| UA | 14/11 | 85.050 | 2/0/0 | 49/19 | 88.550 | 5/0/0 |
| UG | 6/5 | 79.200 | 0/0/0 | 25/17 | 89.850 | 7/1/0 |
| US | 15/15 | 85.800 | 2/0/0 | 60/60 | 86.575 | 14/3/0 |
| UY | 33/33 | 71.700 | 0/0/0 | 61/59 | 78.500 | 0/0/0 |
| UZ | 20/20 | 77.250 | 3/0/0 | 56/51 | 84.300 | 8/1/0 |
| VA | 1/1 | 93.800 | 1/0/0 | 24/24 | 88.100 | 9/3/1 |
| VC | 13/13 | 72.250 | 0/0/0 | 51/31 | 80.150 | 1/0/0 |
| VE | 35/34 | 71.175 | 0/0/0 | 43/38 | 82.250 | 4/1/0 |
| VN | 140/140 | 75.825 | 1/0/0 | 360/360 | 85.000 | 34/5/2 |
| VU | 6/5 | 68.400 | 0/0/0 | 15/13 | 81.400 | 1/0/0 |
| WS | 6/6 | 67.850 | 0/0/0 | 22/19 | 79.650 | 0/0/0 |
| XK | 20/20 | 71.075 | 0/0/0 | 38/37 | 80.550 | 3/0/0 |
| YE | 10/2 | 70.225 | 0/0/0 | 34/13 | 85.200 | 2/0/0 |
| ZA | 12/12 | 81.375 | 1/0/0 | 31/24 | 90.025 | 13/1/0 |
| ZM | 5/3 | 76.300 | 0/0/0 | 20/12 | 91.350 | 8/1/0 |
| ZW | 6/5 | 77.650 | 0/0/0 | 20/17 | 88.950 | 7/1/1 |

Remaining work: individual re-review of flagged cohorts, high category scores, nested properties and low/underassessed sites. Statistical coverage is not equivalent to independently verified editorial coverage. Nine revised destination reviews in this pass checked material factual claims with source limitations disclosed; there are no other newly fact-checked records in this pass.

## Second correction pass — independent scope and peer comparisons

Seven additional records: three Indian temples, the Panama Canal and three cities in Egypt, the United States and South Africa. This corrects both upward and downward; scope, not geography or target rank, determines the changes. In particular, Luxor is not just a gateway: major temples are integrated into the living east-bank city. No new perfect scores or weights changed.

| Destination | Before | After |
| --- | ---: | ---: |
| [Kailasa Temple Ellora](../countries/IN/sights/kailasa-temple-ellora.yaml) | 97.45 | 96.30 |
| [Vittala Temple Hampi](../countries/IN/sights/vittala-temple-hampi.yaml) | 96.85 | 93.45 |
| [Meenakshi Amman Temple](../countries/IN/sights/meenakshi-amman-temple.yaml) | 97.85 | 95.80 |
| [Panama Canal (visitor transit and lock experience)](../countries/PA/sights/panama-canal-visitor-transit-and-lock-experience.yaml) | 96.40 | 93.70 |
| [Luxor](../countries/EG/cities/luxor.yaml) | 85.70 | 92.15 |
| [New York City](../countries/US/cities/new-york-city.yaml) | 94.95 | 96.45 |
| [Cape Town](../countries/ZA/cities/cape-town.yaml) | 91.55 | 93.30 |

Each updated original review contains the dated reassessment with four actual peer links, five separate reasons and material source checks. Across both passes: 16 revised records, not 16,000 independent re-reviews. Earlier baseline table remains a snapshot. Source coverage and GPS limitations remain explicit. No automatic rating changes.

## Third correction pass — targeted review of scope outliers

Full registry integration and validation run [45731932469](https://github.com/Persie0/Playground/actions/runs/45731932469): 250 areas, 16,269 records, 14,679 ranked and 1,590 unassessed. The [record-level diagnostic](worldwide-diagnostics/README.md) and TSV contain all source records, not individual verification. Of 36 small-scope heuristic flags, six additional records were individually reassessed. The Gornergrat flag was checked and retained: its scope includes a railway and multiple view opportunities, comparable to Aiguille du Midi (91.90), not simply a viewing platform. No automatic country corrections.

| Destination | Before | After |
| --- | ---: | ---: |
| [Statue of Unity](../countries/IN/sights/statue-of-unity.yaml) | 90.05 | 88.80 |
| [Charles Bridge](../countries/CZ/sights/charles-bridge.yaml) | 91.65 | 89.05 |
| [Zhaozhou Bridge](../countries/CN/sights/zhaozhou-bridge.yaml) | 91.25 | 88.60 |
| [Tiananmen Square](../countries/CN/sights/tiananmen-square.yaml) | 91.00 | 87.80 |
| [Yumen Pass (Jade Gate)](../countries/CN/sights/yumen-pass.yaml) | 90.70 | 85.55 |
| [Kala Patthar Viewpoint](../countries/NP/sights/kala-patthar-viewpoint.yaml) | 90.30 | 89.90 |

All six decisions have four specific peer links, five reasons, source excerpt limitations and explicit high-field explanations. 22 records revised across three passes; full individual review remains outstanding.

## Fourth correction pass — international garden calibration

Seven named gardens in China, Japan and South Africa reassessed against four specific worldwide peers each. Four score revisions and three explicit retain decisions; institutional estate and visitor scope distinguished. Source claims were checked in accessible full text or clearly identified excerpts, with independent corroboration and GPS unresolved. No new 10 anchors or weight changes.

| Destination | Before | After | Decision |
| --- | ---: | ---: | --- |
| Xishuangbanna Tropical Botanical Garden | 92.45 | 91.10 | revised |
| Lion Grove Garden | 90.35 | 87.90 | revised |
| Lingering Garden Suzhou | 91.40 | 89.90 | revised |
| Humble Administrator's Garden | 91.55 | 91.15 | revised |
| Kenrokuen Garden | 91.60 | 91.60 | retained |
| Ritsurin Garden | 90.85 | 90.85 | retained |
| Kirstenbosch National Botanical Garden | 90.15 | 90.15 | retained |

Cumulative: 26 score revisions and three additional retained garden decisions; earlier Gornergrat retain decision also remains. Diagnostic and generated ranking files must be refreshed before merging.

## Fifth correction pass — complete initial small-scope queue

Reviewed the 22 remaining flags in the refreshed 28-item queue (the other six already have garden or Gornergrat decisions). Six rescores and 16 retained ratings. All 36 original small-scope flags now have individual decisions across passes 3–5, including records still above 90. This closes the scope-heuristic queue, not the entire worldwide editorial or incomplete-core queue. Sources checked at excerpt level only. No country multiplier or new perfect score.

| Destination | Before | After | Decision |
| --- | ---: | ---: | --- |
| Registan | 96.15 | 96.15 | retained |
| Sistine Chapel | 95.70 | 95.70 | retained |
| Nongriat Double Decker Living Root Bridge | 94.60 | 90.75 | revised |
| Saint Peter's Square | 94.25 | 92.35 | revised |
| Tower of London | 93.75 | 93.75 | retained |
| Shravanabelagola Bahubali Statue | 93.75 | 91.70 | revised |
| Saint Mark's Basilica and square | 93.50 | 93.50 | retained |
| Eiffel Tower | 93.30 | 93.30 | retained |
| Walled City of Baku | 93.05 | 93.05 | retained |
| Patan Durbar Square | 92.90 | 92.90 | retained |
| Kremlin and Red Square | 92.85 | 92.85 | retained |
| Historic Centre of Oporto | 92.45 | 92.45 | retained |
| Lumbini Sacred Garden | 92.30 | 90.50 | revised |
| Jerónimos Monastery and Belém Tower | 92.15 | 92.15 | retained |
| Bhaktapur Durbar Square | 92.10 | 92.10 | retained |
| Kathmandu Durbar Square | 92.05 | 92.05 | retained |
| Guangji Bridge | 91.15 | 89.10 | revised |
| Old Town Square Prague | 90.70 | 89.25 | revised |
| Mostar Old Bridge Area | 90.60 | 90.60 | retained |
| Garden Kingdom of Dessau-Wörlitz | 90.40 | 90.40 | retained |
| Kröller-Müller Museum and sculpture garden | 90.25 | 90.25 | retained |
| Garden Route National Park | 90.25 | 90.25 | retained |

The total number of score revisions in the worldwide PR is now 32. Generated files require regeneration.

## Sixth correction pass — individual incomplete-core decisions

Five records reviewed against specific sources and worldwide peers. Three formerly incomplete ratings can now be ranked based on documented visitor routes and interpretation. Two remain unranked because a partial accessible component does not establish the visit scope of the named property. This is not completion of the 1,590-record incomplete queue. The original coordinates and all category ratings were retained; no new perfect scores.

| Destination | Before | After | Decision |
| --- | ---: | ---: | --- |
| Material Testimonies of the Construction of the Pyrenean State (Andorran components) | unranked | 84.95 | completed |
| Lower German Limes (Dutch components) | unranked | 84.65 | completed |
| The Rise of Systematic Biology (Swedish tentative components) | unranked | 85.85 | completed |
| David Gareji Monasteries and Hermitage | unranked | unranked | unranked retained |
| East Atlantic Flyway: England East Coast Wetlands (tentative) | unranked | unranked | unranked retained |

## Seventh pass — Italian incomplete-core review

Ten individual decisions: nine missing-core profiles completed; one retained unranked due to overlapping Asinara visitor scope. Source excerpts inspected; independent full-text checks and GPS remain outstanding. Original coordinates and categories retained, no new 10 anchors. Remaining Italian incomplete queue: 14 records after regeneration.

| Destination ID suffix | Result | Decision |
| --- | ---: | --- |
| sacri-monti | 89.75 | completed |
| longobards | 90.40 | completed |
| medici-villas | 91.20 | completed |
| venetian-defences | 89.95 | completed |
| via-appia | 90.70 | completed |
| via-francigena | 90.20 | completed |
| evaporitic-karst | 89.75 | completed |
| domus-de-janas | 88.80 | completed |
| pelagos | 89.00 | completed |
| asinara-island | unranked | retained unranked |

## Eighth pass — 100-record incomplete-core batch

[Batch register](worldwide-incomplete-batch-100-2026-11-26.md): 100 distinct sights, 6 new complete profiles and 94 retained incomplete with case-specific evidence targets. Only the six source-assisted decisions in France and Spain constitute completed rating reassessments. Other records are triaged, not independently fact-checked or finished. Exact coordinates and category ratings unchanged. Newly complete scores: sight-fr-le-corbusier: 90.80; sight-fr-santiago-routes: 90.10; sight-fr-vauban: 90.30; sight-fr-vezere-caves: 90.65; sight-es-mudejar-aragon: 90.80; sight-es-risco-caido: 90.75.
