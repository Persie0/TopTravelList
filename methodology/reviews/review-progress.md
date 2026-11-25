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

All four merged PRs have passed schema, generated Markdown and worldwide benchmark checks on their reviewed heads. The overall workflow runs reported failure after successful per-country validation (merge/PR operation issues); actual merge status verified separately. The entries above mean targeted follow-up review, not comprehensive independent verification of all 267 destinations.

## Targeted review merged — not full-country confirmation

- [Brazil (BR)](BR/sights.md), [PR #95](https://github.com/Persie0/TopTravelList/pull/95): Rio de Janeiro, Iguaçu Falls Brazilian viewpoints, Valongo Wharf; score retention with explicit limitations.
- [Benin (BJ)](BJ/sights.md), [PR #95](https://github.com/Persie0/TopTravelList/pull/95): Royal Palaces of Abomey main complex; score retention, visitor access needs further confirmation.

## Automated screening only

[Detailed screening snapshot](screening-2026-11-25.md).

The [2026-11-25 screening run](https://github.com/Persie0/Playground/actions/runs/45659557116) screened recently merged country additions: JP, ID, MY, SG, BN, CZ, LA, BA, ME, LK, AL, NP, BT, LI, JO, SM, BH, MU, PY, ST, EC, LS, OM, PE, DJ, CL, BW, CO, TG, AR, MW, AM, BR, BJ (only records present at the run's snapshot). It identified 559 exceptional-score/duplicate-name flags; flags are review priorities, not proof of inflation. No bulk adjustments. The list does not imply a complete review of these countries.

## Next open PRs (oldest first at time of recording)

VA #48; KW #50; SR #49; HN #53; MT #54; MV #56; RW #57; TL #58; CR #59; LU #61; PA #62; SZ #63; BO #64; MK #65; CV #66; MN #67; GM #73; UZ #74; KM #78; KG #80; VE #81; AE #86; AZ #92; TJ #94. Re-read the live queue before each batch.

## Completion criteria

- Inspect the existing individual review and compare exact visitor scope with worldwide peers.
- Document score changes and retention decisions; verify source claims, particularly high scores.
- Preserve null versus zero, category applicability, canonical weights and approved perfect-score policy.
- Regenerate ranking Markdown, pass schema and benchmark checks, verify merge and close the PR.
- Record the reviewed revision, date, evidence limitations and remaining work here. Never label a country fully fact-checked solely because validation passed.
