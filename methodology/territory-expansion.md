# Geographic coverage expansion — 2026-11-25

The registry now contains all 249 official ISO 3166-1 alpha-2 entries and Kosovo (XK). Source: [Austrian Environment Agency ISO register](https://edm.gv.at/edm_portal/redaList.do?6578706f7274=1&d-49520-e=5&d-49520-o=2&d-49520-p=1&d-49520-s=2&entireLsq=true&seqCode=na2skv6322qsqu&ubastyle_lang=en&ubastyle_nav=true); the installed pycountry dataset is the executable reference. Geographic codes are not declarations of recognition, sovereignty, access or safety. BQ, SH, SJ and UM include multiple islands under a single ISO code. Separate individual island coverage belongs inside that code. Antarctica, Bouvet, Heard/McDonald, Chagos, French Southern Territories, South Georgia/South Sandwich and US Minor Outlying Islands are not required to have permanent civilian settlement records; do not invent cities.

## Migration policy

Do not create duplicates when an existing parent-country record belongs in a newly registered territory. Before adding each territory, inspect parent YAML coordinates, aliases and existing historical reviews. Move the existing record to the territory, preserving scores until explicitly reviewed; update location code, ID, benchmark/anchor references and active source links; append a dated migration mapping old to new ID. Preserve historical reviews as historical snapshots. Where an old link cannot be redirected, document the mapping. Run full benchmark checks and regenerate rankings for both parents and territory. Until migration, parent records remain authoritative and the territory may be empty. This PR does not move non-Greenland records.

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
