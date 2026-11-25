# Country review progress

Updated: 2026-11-25. This is the independent follow-up review ledger, not the original inventory's self-reported reviews. Follow [worldwide rules](../../rules.md), [country workflow](../future-country-workflow.md) and the city/sight comparison benchmarks. Update this file after each follow-up review and confirmed merge; distinguish targeted editorial review from complete per-record fact-checking.

## Reviewed and merged

| Country | ISO | Cities | Sights | Follow-up PR | Validation | Rating changes | Remaining verification |
| --- | --- | ---: | ---: | --- | --- | --- | --- |
| San Marino | SM | 14 | 25 | [#41](https://github.com/Persie0/TopTravelList/pull/41) | [Pass](https://github.com/Persie0/Playground/actions/runs/45659557116) | Witches' Pass, Montale, Monte Cerreto Path | Individual source/GPS checks and narrower category peers |
| Bahrain | BH | 15 | 40 | [#42](https://github.com/Persie0/TopTravelList/pull/42) | [Pass](https://github.com/Persie0/Playground/actions/runs/45659557116) | Awali visitor experience and depth unassessed | Individual source/GPS checks |
| Uruguay | UY | 33 | 61 | [#43](https://github.com/Persie0/TopTravelList/pull/43) | [Pass](https://github.com/Persie0/Playground/actions/runs/45660549613) | Isla de Lobos depth 7.5 → 6.7; three other focused retain decisions | Individual source/GPS checks |
| Belize | BZ | 18 | 61 | [#44](https://github.com/Persie0/TopTravelList/pull/44) | [Pass](https://github.com/Persie0/Playground/actions/runs/45660549613) | ATM Cave depth 8.6 → 8.2; five other focused retain decisions | Individual source/GPS checks |
| Seychelles | SC | 14 | 49 | [#45](https://github.com/Persie0/TopTravelList/pull/45) | [Pass](https://github.com/Persie0/Playground/actions/runs/45661331359) | Aldabra depth 8.8 → 7.6; three focused retain decisions | Individual source/GPS and category calibration |
| El Salvador | SV | 24 | 54 | [#46](https://github.com/Persie0/TopTravelList/pull/46) | [Pass](https://github.com/Persie0/Playground/actions/runs/45661331359) | Joya de Cerén and Santa Ana Volcano retained with closer peers | Individual source/GPS and category calibration |
| Vatican City | VA | 1 | 24 | [#48](https://github.com/Persie0/TopTravelList/pull/48) | [Pass](https://github.com/Persie0/Playground/actions/runs/45661331359) | Sistine Chapel, Raphael Rooms and Gallery of Maps depth reduced; Necropolis retained | Individual source/GPS and category calibration |
| Kuwait | KW | 12 | 43 | [#50](https://github.com/Persie0/TopTravelList/pull/50) | [Pass](https://github.com/Persie0/Playground/actions/runs/45662330300) | Al-Zor settlement revised; Failaka island retained | Individual source/GPS and category calibration |
| Honduras | HN | 31 | 59 | [#53](https://github.com/Persie0/TopTravelList/pull/53) | [Pass](https://github.com/Persie0/Playground/actions/runs/45662330300) | Copán stairway experience reduced; Copán and Río Plátano retained | Individual source/GPS and category calibration |

All listed merged PRs have passed schema, generated Markdown and worldwide benchmark checks on their reviewed heads. Earlier workflow runs reported merge-operation failures after successful per-country validation; actual merge status was verified separately. The entries above mean targeted follow-up review, not comprehensive independent verification of all destination records.

## Targeted review merged — not full-country confirmation

- [Brazil (BR)](BR/sights.md), [PR #95](https://github.com/Persie0/TopTravelList/pull/95): Rio de Janeiro, Iguaçu Falls Brazilian viewpoints, Valongo Wharf; score retention with explicit limitations.
- [Benin (BJ)](BJ/sights.md), [PR #95](https://github.com/Persie0/TopTravelList/pull/95): Royal Palaces of Abomey main complex; score retention, visitor access needs further confirmation.

## Targeted follow-up reviews pending full validation

| Country | PR | Changes | Checks completed | Outstanding |
| --- | --- | --- | --- | --- |
| Suriname / Ecuador | [#101](https://github.com/Persie0/TopTravelList/pull/101) | Central Suriname reserve 90.50 → 89.50; Galápagos 98.30 → 97.80; Yasuní 92.75 → 91.85 | Arithmetic and ranking order across 82 ranked sights | Full Python validation and merge |
| Maldives | [#56](https://github.com/Persie0/TopTravelList/pull/56) | Hanifaru Bay 94.00 → 93.30; Baa Atoll 93.65 → 93.15 | Arithmetic/order across 65 ranked records; 67 original review entries and four-peer links checked | Reconcile current main, regenerate links, run global checks and merge |
| Malta | [#102](https://github.com/Persie0/TopTravelList/pull/102) (original #54 separately merged) | Hypogeum 93.00 → 92.10 | Arithmetic/order across 37 ranked sights; four current peers and operator visitor scope checked | Full Python validation and merge |
| Rwanda | [#57](https://github.com/Persie0/TopTravelList/pull/57) | Four exceptional profiles retained: Volcanoes, Nyungwe, Akagera and Kigali memorial | 63 ranked rows arithmetic/order; 65 original reviews and peer links; 4 targeted source comparisons | Reconcile main, regenerate rankings and run global checks |
| Timor-Leste | [#58](https://github.com/Persie0/TopTravelList/pull/58) | Atauro reefs and Nino Konis Santana retained with specialist peers | Two targeted source comparisons and canonical score arithmetic | Generated city/sight tables currently empty despite 62 documented entries; regenerate and run full checks |
| Costa Rica | [#59](https://github.com/Persie0/TopTravelList/pull/59) | Monteverde 92.70 → 92.10; Corcovado and Tortuguero retained | 83 ranked rows arithmetic/order; 90 original reviews and peer links; three targeted visitor-scope comparisons | Reconcile main, regenerate rankings, full Python checks and merge |
| Panama | [#62](https://github.com/Persie0/TopTravelList/pull/62) | Miraflores 90.20 → 88.30; entire canal and Coiba retained | 67 ranked rows arithmetic/order; 75 original reviews and peer links; targeted source comparisons | Reconcile main, regenerate rankings, full Python checks and merge |
| Eswatini | [#63](https://github.com/Persie0/TopTravelList/pull/63) | Ngwenya 85.35 → 86.50; Malolotja and Mkhaya retained | All 45 YAML records checked against original review totals and peer coverage; 43 ranked, 2 unassessed; reconstructed both tables with name-and-country Maps links | Reconcile main and README, verify exact output with Python generator and global checks, merge |
| Cabo Verde | [#66](https://github.com/Persie0/TopTravelList/pull/66) | Pico do Fogo, Fogo Natural Park and Santa Monica Beach retained after closer comparisons | 69 ranked rows arithmetic/order; 71 review entries and peer links; three focused source comparisons | Reconcile main, regenerate rankings and run global checks, merge |

## Automated screening only

[Detailed screening snapshot](screening-2026-11-25.md).

The [2026-11-25 screening run](https://github.com/Persie0/Playground/actions/runs/45659557116) screened recently merged country additions: JP, ID, MY, SG, BN, CZ, LA, BA, ME, LK, AL, NP, BT, LI, JO, SM, BH, MU, PY, ST, EC, LS, OM, PE, DJ, CL, BW, CO, TG, AR, MW, AM, BR, BJ (only records present at the run's snapshot). It identified 559 exceptional-score/duplicate-name flags; flags are review priorities, not proof of inflation. No bulk adjustments. The list does not imply a complete review of these countries.

## Next open PRs (oldest first at time of recording)

[#56](https://github.com/Persie0/TopTravelList/pull/56) Add Maldives worldwide city and sight rankings; [#57](https://github.com/Persie0/TopTravelList/pull/57) Add Rwanda worldwide city and sight rankings; [#58](https://github.com/Persie0/TopTravelList/pull/58) Add Timor-Leste worldwide city and sight rankings; [#59](https://github.com/Persie0/TopTravelList/pull/59) Add Costa Rica worldwide city and sight rankings; [#62](https://github.com/Persie0/TopTravelList/pull/62) Add Panama worldwide city and sight rankings; [#63](https://github.com/Persie0/TopTravelList/pull/63) Add Eswatini worldwide city and sight rankings; [#66](https://github.com/Persie0/TopTravelList/pull/66) Add Cabo Verde worldwide rankings; [#67](https://github.com/Persie0/TopTravelList/pull/67) Add Mongolia worldwide city and sight rankings; [#73](https://github.com/Persie0/TopTravelList/pull/73) Add The Gambia worldwide city and sight rankings; [#74](https://github.com/Persie0/TopTravelList/pull/74) Add Uzbekistan worldwide city and sight rankings; [#78](https://github.com/Persie0/TopTravelList/pull/78) Add Comoros worldwide city and sight rankings; [#80](https://github.com/Persie0/TopTravelList/pull/80) Add Kyrgyzstan worldwide city and sight rankings; [#86](https://github.com/Persie0/TopTravelList/pull/86) Add United Arab Emirates worldwide city and sight rankings; [#92](https://github.com/Persie0/TopTravelList/pull/92) Add Azerbaijan worldwide city and sight rankings; [#94](https://github.com/Persie0/TopTravelList/pull/94) Add Tajikistan worldwide city and sight rankings; [#96](https://github.com/Persie0/TopTravelList/pull/96) Add Kazakhstan worldwide city and sight rankings; [#97](https://github.com/Persie0/TopTravelList/pull/97) Add Turkmenistan worldwide city and sight rankings; [#98](https://github.com/Persie0/TopTravelList/pull/98) Add Bangladesh worldwide city and sight rankings; [#100](https://github.com/Persie0/TopTravelList/pull/100) Add Lebanon worldwide city and sight rankings; [#101](https://github.com/Persie0/TopTravelList/pull/101) Review Suriname and Ecuador protected-area visitor depth; [#102](https://github.com/Persie0/TopTravelList/pull/102) Review Malta Hypogeum visitor depth against worldwide peers. Re-read the live queue before each batch.

## Completion criteria

- Inspect the existing individual review and compare exact visitor scope with worldwide peers.
- Document score changes and retention decisions; verify source claims, particularly high scores.
- Preserve null versus zero, category applicability, canonical weights and approved perfect-score policy.
- Regenerate ranking Markdown, pass schema and benchmark checks, verify merge and close the PR.
- Record the reviewed revision, date, evidence limitations and remaining work here. Never label a country fully fact-checked solely because validation passed.
