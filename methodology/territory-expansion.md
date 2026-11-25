# Geographic coverage expansion — 2026-11-25

The registry now contains all 249 official ISO 3166-1 alpha-2 entries and Kosovo (XK). Source: [Austrian Environment Agency ISO register](https://edm.gv.at/edm_portal/redaList.do?6578706f7274=1&d-49520-e=5&d-49520-o=2&d-49520-p=1&d-49520-s=2&entireLsq=true&seqCode=na2skv6322qsqu&ubastyle_lang=en&ubastyle_nav=true); the installed pycountry dataset is the executable reference. Geographic codes are not declarations of recognition, sovereignty, access or safety. BQ, SH, SJ and UM include multiple islands under a single ISO code. Separate individual island coverage belongs inside that code. Antarctica, Bouvet, Heard/McDonald, Chagos, French Southern Territories, South Georgia/South Sandwich and US Minor Outlying Islands are not required to have permanent civilian settlement records; do not invent cities.

## Migration policy

Do not create duplicates when an existing parent-country record belongs in a newly registered territory. Before adding each territory, inspect parent YAML coordinates, aliases and existing historical reviews. Move the existing record to the territory, preserving scores until explicitly reviewed; update location code, ID, benchmark/anchor references and active source links; append a dated migration mapping old to new ID. Preserve historical reviews as historical snapshots. Where an old link cannot be redirected, document the mapping. Run full benchmark checks and regenerate rankings for both parents and territory. Until migration, parent records remain authoritative and the territory may be empty. Completed migrations are recorded in the log below.

## Initial migration/research queue (not exhaustive)

| Territory | Existing candidate records under parent |
| --- | --- |
| HK, MO | CN city and sight records including Hong Kong, Macau, Historic Centre of Macau, Macau Tower, Man Mo Temple, Hong Kong Palace Museum, Monte Fort |
| AX | FI Mariehamn and possible Åland-area sights |
| SJ | NO Longyearbyen, Svalbard, Jan Mayen |
| GP, MQ, NC, RE | FR Guadeloupe park, Martinique volcanoes, New Caledonia lagoons, Réunion park/pitons and other geographically associated records |
| PR | US San Juan National Historic Site and any nearby records |
| EH | Dakhla tentative property noted in Morocco PR #231; do not duplicate or imply sovereignty |
| GL | Denmark's UNESCO inventory has three Greenland properties; no matching Danish YAML filenames at initial audit. New Greenland records below. |

All other added codes start as empty research backlog; inspect both names and geographic coordinates before cataloguing. No invented coverage claims. ISO code expansion does not replace future subnational region coverage (Canaries, Azores, Madeira, Hawaii, Alaska, Galápagos, etc.). Do not assign perfect tens without existing V2 anchor procedure. The unchanged scoring weights apply to territories.

## Migration log — 2026-11-25

| Former ID | Active ID | Decision |
| --- | --- | --- |
| sight-fr-taputapuatea | sight-pf-taputapuatea | Move to PF, preserve scores and location; original review archived. |
| sight-fr-marquesas | sight-pf-marquesas | Move to PF, preserve partial scores; remains unranked. |

Original decisions: [France migration history](reviews/FR/migration-history-PF.md). Old YAML links are historical; active sources are under `countries/PF/sights/`. Parent inventory names checked; exhaustive coordinate and external link audit remains outstanding.

### Puerto Rico migration — 2026-11-25

| Former ID | Active ID | Decision |
| --- | --- | --- |
| sight-us-san-juan-national-historic-site | sight-pr-san-juan-national-historic-site | Preserve 88.55 score and original approximate point; migrate public NPS fortification component only. |

[Original US review](reviews/US/migration-history-PR.md). No separate duplicate fort or La Fortaleza record created. Parent ranking names checked; exhaustive coordinate and reference audit pending.

### Antarctica coverage — 2026-11-25

AQ has no permanent civilian settlement records. Initial coverage prioritizes named Antarctic Treaty visitor zones and documented vessel-based scenic sites, not blanket continent, peninsula, or island-wide scores. Protected huts at Cape Evans and Cape Royds remain unranked pending ordinary permitted visitor scope. No sovereignty claims or fictional cities are implied. Full cross-registry coordinate and alias audit remains pending.

### Hong Kong migration — 2026-11-25

The historic benchmark profiles and 2026 audits retain their original CN IDs as immutable provenance. The following new HK IDs are authoritative for current rankings. Shenzhen, Wutong Mountain and Dapeng Fortress remain in CN. No sovereignty inference is intended. Scores and coordinates retained for all migrated records unless a later review explicitly changes them.

| Old ID | New ID |
| --- | --- |
| city-cn-hong-kong | city-hk-hong-kong |
| sight-cn-victoria-harbour | sight-hk-victoria-harbour |
| sight-cn-sai-kung-geopark | sight-hk-sai-kung-geopark |
| sight-cn-hong-kong-palace-museum | sight-hk-hong-kong-palace-museum |
| sight-cn-lantau-island | sight-hk-lantau-island |
| sight-cn-tian-tan-buddha | sight-hk-tian-tan-buddha |
| sight-cn-west-kowloon-cultural-district | sight-hk-west-kowloon-cultural-district |
| sight-cn-victoria-peak | sight-hk-victoria-peak |
| sight-cn-man-mo-temple-hong-kong | sight-hk-man-mo-temple-hong-kong |
| sight-cn-star-ferry | sight-hk-star-ferry |
| sight-cn-tai-o-fishing-village | sight-hk-tai-o-fishing-village |
| sight-cn-wong-tai-sin-temple | sight-hk-wong-tai-sin-temple |
| sight-cn-dragons-back-trail | sight-hk-dragons-back-trail |
| sight-cn-lamma-island | sight-hk-lamma-island |
| sight-cn-ngong-ping-360 | sight-hk-ngong-ping-360 |
| sight-cn-temple-street-night-market | sight-hk-temple-street-night-market |

Parent ranking names and representative points screened; broader reference audit still needed. Five additional sights included: M+, Tai Kwun, Chi Lin/Nan Lian, Cheung Chau, Wetland Park. All initial assessments source-linked-unverified.
