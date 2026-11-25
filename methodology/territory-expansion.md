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

### Macau and Hong Kong follow-up migration — 2026-11-25

Preserve historical CN IDs in archival benchmark profiles; these active records move without numeric score changes. Mainland Zhuhai and Jiangmen remain in CN.

| Old ID | New ID |
| --- | --- |
| city-cn-macau | city-mo-macau |
| sight-cn-historic-centre-macau | sight-mo-historic-centre-macau |
| sight-cn-a-ma-temple | sight-mo-a-ma-temple |
| sight-cn-senado-square | sight-mo-senado-square |
| sight-cn-monte-fort-macau | sight-mo-monte-fort-macau |
| sight-cn-ruins-of-st-pauls | sight-mo-ruins-of-st-pauls |
| sight-cn-taipa-village | sight-mo-taipa-village |
| sight-cn-macau-tower | sight-mo-macau-tower |
| sight-cn-po-lin-monastery | sight-hk-po-lin-monastery |

Po Lin Monastery was caught by the subsequent longitude screen; moved to HK. Five additional Macau sights included. Remaining cross-registry geographic and reference audit outstanding.

### Svalbard and Jan Mayen migration — 2026-11-25

| Former ID | Active ID |
| --- | --- |
| city-no-longyearbyen | city-sj-longyearbyen |
| sight-no-svalbard | sight-sj-svalbard |
| sight-no-jan-mayen | sight-sj-jan-mayen |

Original Norway decisions archived. Whole Svalbard and Jan Mayen tentative records remain unranked. Ny-Ålesund is represented as a public heritage visitor area, Pyramiden as a historic settlement, not ordinary cities. Barentsburg remains an unranked inhabited settlement pending visitor evidence. Parent names and high-Arctic points screened; no sovereignty change implied.

### Réunion migration — 2026-11-25

| Former ID | Active ID |
| --- | --- |
| sight-fr-reunion-pitons | sight-re-reunion-pitons |
| sight-fr-reunion-park | sight-re-reunion-pitons (retired duplicate) |

[UNESCO](https://whc.unesco.org/en/list/1317/) confirms the listed property coincides with the national park core. Keep one active visitor landscape with original 93.80 score; retire overlapping 93.65 profile, archive both [original reviews](reviews/FR/migration-history-RE.md). Add five settlements and nine individually scoped sights. Metropolitan Saint-Denis basilica stays in FR. Parent names and approximate coordinates screened; full reference and GPS audit pending.

### New Caledonia migration — 2026-11-25

| Former ID | Active ID |
| --- | --- |
| sight-fr-new-caledonia-lagoons | sight-nc-new-caledonia-lagoons |

[Original review](reviews/FR/migration-history-NC.md). Preserve partial scores; UNESCO six-cluster reef property remains unranked because combined permitted visitor scope is not established. Add four settlements and ten specifically scoped visitor sights; customary access restrictions respected. Parent names and approximate geographic points screened. Full cross-registry and coordinate audit remains outstanding.

### Åland migration — 2026-11-25

| Former ID | Active ID |
| --- | --- |
| city-fi-mariehamn | city-ax-mariehamn |
| sight-fi-kastelholm | sight-ax-kastelholm |
| sight-fi-bomarsund | sight-ax-bomarsund |

Original Finnish reviews archived. Two new villages and eight new sights; Pommern separately scoped from adjacent museum. Parent names and approximate geographic points screened. Full independent coordinate and reference audit remains outstanding.

### Guadeloupe migration — 2026-11-25

| Former ID | Active ID |
| --- | --- |
| sight-fr-guadeloupe-park | sight-gp-guadeloupe-park |

[Original France review](reviews/FR/migration-history-GP.md). Preserve 91.05 park profile; add five settlements and ten scoped sights. Pigeon Islets and Grand Cul-de-Sac Marin are specific park sectors; no aggregate sum or claim of unrestricted access. Petite-Terre Terre-de-Haut (uninhabited restricted islet) is not the inhabited Terre-de-Haut of Les Saintes. Parent names and approximate geographic points screened; full independent coordinate and reference audit remains outstanding.

### Martinique migration — 2026-11-25

| Former ID | Active ID |
| --- | --- |
| sight-fr-martinique-volcanoes | sight-mq-martinique-volcanoes |

[Original France review](reviews/FR/migration-history-MQ.md). Preserve 90.10 UNESCO serial-property profile, add four settlements and ten individually scoped sights. Mount Pelée's trail experience distinct from whole property. Parent names and approximate coordinates screened; full independent geographic and reference audit outstanding.

### French Guiana migration — 2026-11-25

| Former ID | Active ID |
| --- | --- |
| sight-fr-guyane-park | sight-gf-guyane-park |

[Original France review](reviews/FR/migration-history-GF.md). Preserve 89.05 scoped park profile; add four settlements and nine specifically scoped sights. Restricted park core and customary territories excluded from ordinary visitor experience; CNES public tour separate from museum; no Devil's Island landing. Parent names and approximate points screened. Full geographic/reference audit remains outstanding.

### Mayotte coverage — 2026-11-25

FR generated inventory screened by names and approximate coordinates; no matching parent record identified. Initial coverage: two settlements and ten sights, including eight ranked sights and two unranked heritage sites (MuMa and Tsingoni mosque). No whole marine-park score, no guarantee of post-Chido access or animal sightings. Separate geographic code does not imply a position on sovereignty. Source excerpts and approximate coordinate references checked; full factual and geographic audit remains outstanding.

### Saint Barthélemy coverage — 2026-11-25

No matching FR records identified by name and approximate coordinates in generated inventory. Add two settlements and eight scoped sights. Marine reserve sectors and documented coral heat stress treated separately; no whole marine reserve score or guaranteed pristine reef. Full independent coordinate and cross-registry audit remains outstanding.

### Saint Martin (French part) coverage — 2026-11-25

No matching FR or NL records identified by generated ranking name/approximate coordinate screen. Add two settlements and ten specifically scoped sights. Dutch-side destinations excluded (SX). Reserve site descriptions support historical permitted marine visitor scope; current access and reef condition need separate checks. No parent migration or new exact-10 scores.

### Sint Maarten (Dutch part) coverage — 2026-11-25

No matching NL records identified in generated inventory by name or approximate coordinate screening. Add two settlements and ten sights (nine ranked sights, Mullet Pond unranked). French-side sites remain MF. Maho only lawful aircraft observation; marine park rating accounts for documented coral damage, not pristine reef. Emilio Wilson Museum included in Rockland Estate scope. All coordinates and full claim verification outstanding. No exact-10 additions.

### Curaçao coverage — 2026-11-25

NL generated inventory screened by names and approximate coordinates; no matching records identified. Add two settlements and thirteen individual sights. Willemstad city and UNESCO property have separate scopes; their scores are never added. Individual marine sites do not assume pristine reefs or guaranteed wildlife. Search excerpts from UNESCO and Curaçao Tourist Board checked; independent exact GPS and claim-level verification remain outstanding.

### Aruba coverage — 2026-11-25

No matching NL records identified by generated ranking name and approximate coordinate screening. Add 2 settlements and 13 individually scoped sights. Arikok's whole-park scope and named caves/pool separately rated, not summed. ACF rules and documented ranger-managed visitor sites inform scope; no guaranteed swimming or wildlife encounters. Tourism Authority and ACF report search excerpts inspected, full independent claim and GPS verification pending. No perfect-ten scores.

### Caribbean Netherlands coverage — 2026-11-25

No matching NL parent records identified by generated name and approximate coordinate screen. Add 5 settlements and 13 sights across all three islands (Bonaire, Sint Eustatius, Saba). Individual islands retain distinct scopes and names under BQ. Marine park scores account for documented coral decline from STINAPA, CBS and Wageningen research, not historical pristine reef reputation. Source excerpts inspected; full independent coordinate and claim verification pending. No exact-10 additions.

### Bermuda coverage — 2026-11-25

No matching GB parent records identified by generated inventory name and approximate coordinate screening. Add 3 settlements and 12 scoped sights. St George town, UNESCO property and Fort St Catherine have separate scopes; no score summation. Dockyard precinct excludes separate museum collection and Keep. Lighthouse exterior only pending access confirmation. UNESCO, government, museum and tourism source excerpts inspected; full independent claim and coordinate verification remains outstanding. No exact-10 additions.

### Cayman Islands coverage — 2026-11-25

No matching GB parent records identified by generated name/coordinate screen. Add 2 settlements and 11 sights across all three islands. Reef condition accounts for DoE documented decline and CCMI mixed recovery; no pristine reef or wildlife encounter guarantee. Stingray Sandbar distinct from Stingray City dive site, no feeding or handling credited. Source excerpts inspected; exact GPS and full independent verification pending. No exact-10 additions.

### Turks and Caicos coverage — 2026-11-26

No matching GB parent records identified in generated name and approximate coordinate screen. Add 3 settlements and 12 sights. Main visitor sites across Providenciales, Grand Turk, North and Middle Caicos, South Caicos and Salt Cay. East Caicos not assumed to have ordinary established visitor routes. Marine ratings account for coral stress, no pristine reef or guaranteed wildlife. Search excerpts inspected; full independent claims, GPS and access verification pending.

### British Virgin Islands coverage — 2026-11-26

No matching GB records identified in generated ranking name/coordinate screen. Add 3 settlements and 10 sights across Tortola, Virgin Gorda, Anegada, Jost Van Dyke and Salt Island marine area. Baths and Devil's Bay combined as linked visitor experience. Regional coral heat alerts treated as context, not proof of local reef condition. Sources consulted through search excerpts; independent GPS and full claim corroboration pending. No new 10 scores.

### US Virgin Islands coverage — 2026-11-26

No matching US parent records identified by generated inventory name/coordinate screen. Add 4 settlements and 11 sights across Saint Thomas, Saint John and Saint Croix. National park and components separately scoped; Salt River visitor centre excluded, NOAA regional coral stress considered. NPS, NOAA and tourism authority search excerpts inspected; exact GPS and independent full claims outstanding. No exact-10 additions.

### Anguilla coverage — 2026-11-26

No matching GB records identified in generated name/coordinate screening. Add 3 settlements and 10 sights (9 ranked, Fountain Cavern unranked pending ordinary visitor access evidence). Tourist Board, National Trust, archaeological society and reef monitoring search excerpts inspected. Regional coral stress considered; protected sites and exterior-only heritage scope respected. Independent GPS and complete claim verification pending. No exact-10 additions.

### Montserrat coverage — 2026-11-26

No matching GB records identified by generated name and approximate coordinate screening. Add 2 settlements and 8 sights; 9 ranked and Plymouth unranked. MVO current hazard notice conflicts with tourism promotion of certified Plymouth tours; no land access assumed. Observatory viewpoint and interpretation scored instead of volcano ascent. Centre Hills incorporates Oriole Walkway. MVO, National Trust and tourism search excerpts inspected; independent GPS and complete material-claim corroboration pending. No perfect-ten additions.

### Falkland Islands (Malvinas) coverage — 2026-11-26

No matching GB or AR parent records identified by generated name and approximate coordinate screen. Add 3 settlements and 10 sights under existing ISO FK; no sovereignty determination. Government HPAI register checked: Volunteer Point declaration lifted 2 November 2026; Pebble Island and Carcass Island restrictions lifted 30 March; Sea Lion Island remains level 1 pending 30 November review. No assumed unrestricted wildlife visits. Tourism board, museum and JNCC references checked via excerpts; independent exact GPS and full claims pending. No exact-10 additions.

### South Georgia and South Sandwich Islands coverage — 2026-11-26

No matching GB, AR or AQ entries identified in generated name/coordinate screen. Zero cities (no permanent inhabitants), ten sights, nine ranked and one unranked. South Sandwich Islands closed to visitors. Government 25/26 handbook authorized site tables visually checked; no claim of current 26/27 landing availability. Whaling station prohibited areas excluded. Current HPAI and access require confirmation. Independent precise GPS and full claim verification pending. No perfect ten.

### Saint Helena, Ascension and Tristan da Cunha coverage — 2026-11-26

Four settlements and fourteen sights across the three inhabited islands, including the serial UNESCO Gough and Inaccessible Islands property (unranked, restricted visitor scope). GB and FR source filenames screened; no obvious matching parent records. The French-owned Napoleonic properties are geographically in SH; no sovereignty inference or migration is implied. Ascension entry permits and Tristan advance approval/guided access respected. Seasonal wildlife viewing is conditional; no guarantee of any individual animal sighting. Coordinates are approximate editorial anchors and complete independent fact verification and regeneration remain outstanding. No exact-10 or 9.5+ additions.
