# TopTravelList

A consistent, worldwide ranking dataset for **cities** and **sights**.

## Repository layout

```text
countries/
  _registry.json
  AT/
    cities.md  # full computed city ranking + GPS Google Maps links
    sights.md  # full computed sights ranking + GPS Google Maps links
    cities/
    sights/
  ...
methodology/
  scoring.json
schemas/
  city.schema.json
  sight.schema.json
  location.schema.json
  scoring.schema.json
scripts/
  generate_countries.py
  validate.py
  rank.py
  generate_rankings.py
rules.md
requirements.txt
```

Every destination is stored as an individual YAML file in its country's `cities/` or `sights/` directory. Location data contains **only** `country_code`, `latitude`, and `longitude`.

## Get started

```bash
python -m pip install -r requirements.txt
python scripts/generate_countries.py
python scripts/validate.py
python scripts/check_city_benchmarks.py
python scripts/check_sight_benchmarks.py
python scripts/generate_rankings.py
python scripts/generate_rankings.py --check
python scripts/rank.py --country AT --kind cities --limit 20
python scripts/rank.py --country AT --kind sights --limit 20
python scripts/rank.py --country AT --kind sights --category nature --limit 20
python scripts/rank.py --country TH --kind cities --limit 20
python scripts/rank.py --country TH --kind sights --limit 20
python scripts/rank.py --country TH --kind sights --category beaches --limit 20
python scripts/rank.py --country KR --kind cities --limit 20
python scripts/rank.py --country KR --kind sights --limit 20
python scripts/rank.py --country KR --kind sights --category history --limit 20
python scripts/rank.py --country CN --kind cities --limit 30
python scripts/rank.py --country CN --kind sights --limit 30
python scripts/rank.py --country CN --kind sights --category nature --limit 30
python scripts/rank.py --country CN --kind sights --category history --limit 30
python scripts/rank.py --country VN --kind cities --limit 30
python scripts/rank.py --country VN --kind sights --limit 40
python scripts/rank.py --country VN --kind sights --category nature --limit 30
python scripts/rank.py --country VN --kind sights --category history --limit 30
python scripts/rank.py --country KH --kind cities --limit 25
python scripts/rank.py --country KH --kind sights --limit 40
python scripts/rank.py --country KH --kind sights --category history --limit 30
python scripts/rank.py --country KH --kind sights --category nature --limit 30
```

The registry covers **197 travel-country entries**: the 193 United Nations member states, the Holy See and Palestine (UN observer states), plus Taiwan and Kosovo as separately listed travel destinations. Kosovo uses the commonly used, user-assigned code `XK`, not an official ISO 3166-1 code. This is a geographic organization convention, not a statement on political recognition. Territories are not included.

See [rules.md](rules.md) for the universal scoring rubric and [methodology/scoring.json](methodology/scoring.json) for the machine-readable weights and categories.

## Current destination-access advisories

Cambodia: As of **22 November 2026**, border-area attractions including the UNESCO-listed **Temple of Preah Vihear** are **reported closed** due to Cambodia–Thailand border tensions. Scores represent long-term heritage and experience potential, **not a guarantee of current access or safety**. Consult the [UK Foreign Office Cambodia travel advice](https://www.gov.uk/foreign-travel-advice/cambodia) and other current government advisories before planning travel; border-area restrictions may change.

## Country directory

Every registered country has a linked folder below. The status is determined from the YAML destinations and updated whenever rankings are regenerated.

<!-- COUNTRY_DIRECTORY_START -->

**7 done · 190 not done · 197 countries total.**

**Done** means both the city and sight folders contain destination YAML records. It does not mean that every possible destination has been cataloged.

### Done (7)

| Country | Cities | Sights |
| --- | ---: | ---: |
| [Austria](countries/AT/) (`AT`) | 45 | 133 |
| [Cambodia](countries/KH/) (`KH`) | 72 | 260 |
| [China](countries/CN/) (`CN`) | 231 | 490 |
| [South Korea](countries/KR/) (`KR`) | 82 | 284 |
| [Taiwan](countries/TW/) (`TW`) | 64 | 180 |
| [Thailand](countries/TH/) (`TH`) | 69 | 206 |
| [Vietnam](countries/VN/) (`VN`) | 140 | 360 |

### Not done (190)

These countries have no entries in one or both destination folders yet. Their country folders already exist; follow the links to populate them.

| Country | Country | Country | Country |
| --- | --- | --- | --- |
| [Afghanistan](countries/AF/) (`AF`) | [Albania](countries/AL/) (`AL`) | [Algeria](countries/DZ/) (`DZ`) | [Andorra](countries/AD/) (`AD`) |
| [Angola](countries/AO/) (`AO`) | [Antigua and Barbuda](countries/AG/) (`AG`) | [Argentina](countries/AR/) (`AR`) | [Armenia](countries/AM/) (`AM`) |
| [Australia](countries/AU/) (`AU`) | [Azerbaijan](countries/AZ/) (`AZ`) | [Bahamas](countries/BS/) (`BS`) | [Bahrain](countries/BH/) (`BH`) |
| [Bangladesh](countries/BD/) (`BD`) | [Barbados](countries/BB/) (`BB`) | [Belarus](countries/BY/) (`BY`) | [Belgium](countries/BE/) (`BE`) |
| [Belize](countries/BZ/) (`BZ`) | [Benin](countries/BJ/) (`BJ`) | [Bhutan](countries/BT/) (`BT`) | [Bolivia](countries/BO/) (`BO`) |
| [Bosnia and Herzegovina](countries/BA/) (`BA`) | [Botswana](countries/BW/) (`BW`) | [Brazil](countries/BR/) (`BR`) | [Brunei](countries/BN/) (`BN`) |
| [Bulgaria](countries/BG/) (`BG`) | [Burkina Faso](countries/BF/) (`BF`) | [Burundi](countries/BI/) (`BI`) | [Cabo Verde](countries/CV/) (`CV`) |
| [Cameroon](countries/CM/) (`CM`) | [Canada](countries/CA/) (`CA`) | [Central African Republic](countries/CF/) (`CF`) | [Chad](countries/TD/) (`TD`) |
| [Chile](countries/CL/) (`CL`) | [Colombia](countries/CO/) (`CO`) | [Comoros](countries/KM/) (`KM`) | [Congo](countries/CG/) (`CG`) |
| [Costa Rica](countries/CR/) (`CR`) | [Croatia](countries/HR/) (`HR`) | [Cuba](countries/CU/) (`CU`) | [Cyprus](countries/CY/) (`CY`) |
| [Czechia](countries/CZ/) (`CZ`) | [Côte d'Ivoire](countries/CI/) (`CI`) | [Denmark](countries/DK/) (`DK`) | [Djibouti](countries/DJ/) (`DJ`) |
| [Dominica](countries/DM/) (`DM`) | [Dominican Republic](countries/DO/) (`DO`) | [DR Congo](countries/CD/) (`CD`) | [Ecuador](countries/EC/) (`EC`) |
| [Egypt](countries/EG/) (`EG`) | [El Salvador](countries/SV/) (`SV`) | [Equatorial Guinea](countries/GQ/) (`GQ`) | [Eritrea](countries/ER/) (`ER`) |
| [Estonia](countries/EE/) (`EE`) | [Eswatini](countries/SZ/) (`SZ`) | [Ethiopia](countries/ET/) (`ET`) | [Fiji](countries/FJ/) (`FJ`) |
| [Finland](countries/FI/) (`FI`) | [France](countries/FR/) (`FR`) | [Gabon](countries/GA/) (`GA`) | [Gambia](countries/GM/) (`GM`) |
| [Georgia](countries/GE/) (`GE`) | [Germany](countries/DE/) (`DE`) | [Ghana](countries/GH/) (`GH`) | [Greece](countries/GR/) (`GR`) |
| [Grenada](countries/GD/) (`GD`) | [Guatemala](countries/GT/) (`GT`) | [Guinea](countries/GN/) (`GN`) | [Guinea-Bissau](countries/GW/) (`GW`) |
| [Guyana](countries/GY/) (`GY`) | [Haiti](countries/HT/) (`HT`) | [Honduras](countries/HN/) (`HN`) | [Hungary](countries/HU/) (`HU`) |
| [Iceland](countries/IS/) (`IS`) | [India](countries/IN/) (`IN`) | [Indonesia](countries/ID/) (`ID`) | [Iran](countries/IR/) (`IR`) |
| [Iraq](countries/IQ/) (`IQ`) | [Ireland](countries/IE/) (`IE`) | [Israel](countries/IL/) (`IL`) | [Italy](countries/IT/) (`IT`) |
| [Jamaica](countries/JM/) (`JM`) | [Japan](countries/JP/) (`JP`) | [Jordan](countries/JO/) (`JO`) | [Kazakhstan](countries/KZ/) (`KZ`) |
| [Kenya](countries/KE/) (`KE`) | [Kiribati](countries/KI/) (`KI`) | [Kosovo](countries/XK/) (`XK`) | [Kuwait](countries/KW/) (`KW`) |
| [Kyrgyzstan](countries/KG/) (`KG`) | [Laos](countries/LA/) (`LA`) | [Latvia](countries/LV/) (`LV`) | [Lebanon](countries/LB/) (`LB`) |
| [Lesotho](countries/LS/) (`LS`) | [Liberia](countries/LR/) (`LR`) | [Libya](countries/LY/) (`LY`) | [Liechtenstein](countries/LI/) (`LI`) |
| [Lithuania](countries/LT/) (`LT`) | [Luxembourg](countries/LU/) (`LU`) | [Madagascar](countries/MG/) (`MG`) | [Malawi](countries/MW/) (`MW`) |
| [Malaysia](countries/MY/) (`MY`) | [Maldives](countries/MV/) (`MV`) | [Mali](countries/ML/) (`ML`) | [Malta](countries/MT/) (`MT`) |
| [Marshall Islands](countries/MH/) (`MH`) | [Mauritania](countries/MR/) (`MR`) | [Mauritius](countries/MU/) (`MU`) | [Mexico](countries/MX/) (`MX`) |
| [Micronesia, Federated States of](countries/FM/) (`FM`) | [Moldova](countries/MD/) (`MD`) | [Monaco](countries/MC/) (`MC`) | [Mongolia](countries/MN/) (`MN`) |
| [Montenegro](countries/ME/) (`ME`) | [Morocco](countries/MA/) (`MA`) | [Mozambique](countries/MZ/) (`MZ`) | [Myanmar](countries/MM/) (`MM`) |
| [Namibia](countries/NA/) (`NA`) | [Nauru](countries/NR/) (`NR`) | [Nepal](countries/NP/) (`NP`) | [Netherlands](countries/NL/) (`NL`) |
| [New Zealand](countries/NZ/) (`NZ`) | [Nicaragua](countries/NI/) (`NI`) | [Niger](countries/NE/) (`NE`) | [Nigeria](countries/NG/) (`NG`) |
| [North Korea](countries/KP/) (`KP`) | [North Macedonia](countries/MK/) (`MK`) | [Norway](countries/NO/) (`NO`) | [Oman](countries/OM/) (`OM`) |
| [Pakistan](countries/PK/) (`PK`) | [Palau](countries/PW/) (`PW`) | [Palestine](countries/PS/) (`PS`) | [Panama](countries/PA/) (`PA`) |
| [Papua New Guinea](countries/PG/) (`PG`) | [Paraguay](countries/PY/) (`PY`) | [Peru](countries/PE/) (`PE`) | [Philippines](countries/PH/) (`PH`) |
| [Poland](countries/PL/) (`PL`) | [Portugal](countries/PT/) (`PT`) | [Qatar](countries/QA/) (`QA`) | [Romania](countries/RO/) (`RO`) |
| [Russia](countries/RU/) (`RU`) | [Rwanda](countries/RW/) (`RW`) | [Saint Kitts and Nevis](countries/KN/) (`KN`) | [Saint Lucia](countries/LC/) (`LC`) |
| [Saint Vincent and the Grenadines](countries/VC/) (`VC`) | [Samoa](countries/WS/) (`WS`) | [San Marino](countries/SM/) (`SM`) | [Sao Tome and Principe](countries/ST/) (`ST`) |
| [Saudi Arabia](countries/SA/) (`SA`) | [Senegal](countries/SN/) (`SN`) | [Serbia](countries/RS/) (`RS`) | [Seychelles](countries/SC/) (`SC`) |
| [Sierra Leone](countries/SL/) (`SL`) | [Singapore](countries/SG/) (`SG`) | [Slovakia](countries/SK/) (`SK`) | [Slovenia](countries/SI/) (`SI`) |
| [Solomon Islands](countries/SB/) (`SB`) | [Somalia](countries/SO/) (`SO`) | [South Africa](countries/ZA/) (`ZA`) | [South Sudan](countries/SS/) (`SS`) |
| [Spain](countries/ES/) (`ES`) | [Sri Lanka](countries/LK/) (`LK`) | [Sudan](countries/SD/) (`SD`) | [Suriname](countries/SR/) (`SR`) |
| [Sweden](countries/SE/) (`SE`) | [Switzerland](countries/CH/) (`CH`) | [Syria](countries/SY/) (`SY`) | [Tajikistan](countries/TJ/) (`TJ`) |
| [Tanzania](countries/TZ/) (`TZ`) | [Timor-Leste](countries/TL/) (`TL`) | [Togo](countries/TG/) (`TG`) | [Tonga](countries/TO/) (`TO`) |
| [Trinidad and Tobago](countries/TT/) (`TT`) | [Tunisia](countries/TN/) (`TN`) | [Turkmenistan](countries/TM/) (`TM`) | [Tuvalu](countries/TV/) (`TV`) |
| [Türkiye](countries/TR/) (`TR`) | [Uganda](countries/UG/) (`UG`) | [Ukraine](countries/UA/) (`UA`) | [United Arab Emirates](countries/AE/) (`AE`) |
| [United Kingdom](countries/GB/) (`GB`) | [United States](countries/US/) (`US`) | [Uruguay](countries/UY/) (`UY`) | [Uzbekistan](countries/UZ/) (`UZ`) |
| [Vanuatu](countries/VU/) (`VU`) | [Vatican City](countries/VA/) (`VA`) | [Venezuela](countries/VE/) (`VE`) | [Yemen](countries/YE/) (`YE`) |
| [Zambia](countries/ZM/) (`ZM`) | [Zimbabwe](countries/ZW/) (`ZW`) |  |  |

<!-- COUNTRY_DIRECTORY_END -->

All destination records contain the same five core scoring dimensions and applicable category ratings. The scores are **provisional editorial assessments**, not objective facts or definitive worldwide standings. Since the current rubric allows multiple top scores, exceptional destinations can tie. Coordinates identify approximate representative points and should not be used as precise navigation destinations; large parks, rivers, lakes, and regions are not represented by entrance coordinates.

### Per-country rankings, with Google Maps links

Run `python scripts/generate_rankings.py` to create **exactly two Markdown overview files in each registered country folder**: `countries/XX/cities.md` and `countries/XX/sights.md` (197 countries, 394 files). These are generated views; edit only the original YAML data.

Each overview lists **every destination**, ordered by its globally calibrated total (out of 100), with equal scores sharing a rank. It also shows the type (inferred from its name), the complete set of rated categories (highest first), all five core dimension scores, a source-YAML link, and a **Google Maps link using that record's exact GPS latitude and longitude**. Missing or incomplete scores are shown unranked, not treated as zero. Countries without destinations have two explanatory overview files.

```bash
python scripts/generate_rankings.py                   # write/update all 394 overviews
python scripts/generate_rankings.py --country AT      # refresh only Austria
python scripts/generate_rankings.py --country CN      # refresh only China
python scripts/generate_rankings.py --check           # fail on stale overviews or country directory
```

**Whenever you add or change destinations, regenerate the affected country's overviews and the root README country directory, and run --check before committing.** The Markdown rankings are fully deterministic, use the same weighted formula as `scripts/rank.py`, and contain no independently maintained scores.

Use `scripts/rank.py` for ad-hoc sorted comparisons across countries and category-specific rankings. Each category is independently rated on the 0–10 scale, as described in `rules.md`.

## Consistent worldwide city ranking — 2026 review

The **639 cities, towns and villages across all six populated countries** were rebenchmarked on the same worldwide scale, including a direct comparison of **Salzburg vs Phnom Penh**. The 1,733 sight records were subsequently recalibrated in a separate worldwide sight review (details below). All 639 city scores and applicable categories were revisited through a conservative historical calibration; **104 cities** received explicit, individual benchmark profiles. This is a **provisional editorial dataset**, not a site-by-site research or on-the-ground verification.

For **every future country**, first use:
- [City scoring guide](methodology/city-scoring-guide.md) — dimension definitions, international scoring bands, what counts as the city vs a nearby sight, how to assign a score, and the mandatory future-country checklist.
- [Cross-country city benchmarks](methodology/city-comparison-benchmarks.md) — named reference cities from six countries, city-versus-sight safeguards, and required cross-country comparisons.
- [Frozen 104 reference profiles](methodology/city-benchmark-profiles.txt) — explicit five-dimension and selected category profiles reviewed in 2026.
- [Complete 639-city calibration audit](methodology/city-calibration-audit.md) — every old/new score, source YAML link and diagnostics.

New cities **must be scored directly** against world-class and ordinary counterparts across borders. Do **not** apply the archived [one-time conversion script](scripts/recalibrate_cities_2026.py) to future countries; it refuses to rerun. The review is not a national multiplier and does not impose a country quota or median target.

After creating or editing city YAML records, run:

```bash
python scripts/validate.py
python scripts/check_city_benchmarks.py
python scripts/generate_rankings.py --country XX
python scripts/generate_rankings.py --check
python scripts/rank.py --kind cities --limit 60
```

## Worldwide sight ranking — 1,733-attraction calibration (2026)

**All 1,733 previously added sight YAML records across AT, TH, KR, CN, VN and KH have been recalibrated** under the same worldwide v2 five-dimension weights. This one-time review corrects inconsistent historical scoring batches without changing any of the 639 city records, original attraction identities or GPS coordinates. **189 important sights** have explicit, individually reviewed world-peer benchmark profiles; the other **1,544** received a deterministic, conservative first-pass correction. Scores remain provisional editorial judgments, not 1,733 independently researched on-site evaluations.

Before adding **any future country or sight**, read and apply:

- [Mandatory sight-scoring guide](methodology/sight-scoring-guide.md) — five core fields, worldwide thresholds, exact attraction-vs-park scope, category consistency, 9.5+/10 rules, new-country checklist.
- [Cross-country sight benchmarks](methodology/sight-comparison-benchmarks.md) — global landmark, temple, nature, museum, beach, market and garden comparison ladder.
- [189 frozen sight benchmark profiles](methodology/sight-benchmark-profiles.txt) — individually reviewed five-dimensional and category reference values.
- [Complete 1,733-sight calibration audit](methodology/sight-calibration-audit.md) — every sight's old/new total, country diagnostics and direct YAML link.
- [Future sight comparison checker](scripts/check_sight_benchmarks.py) — verifies named global comparisons and reports distribution warnings (not country quotas).

The existing [worldwide 10/10 registry](methodology/scoring.json) remains unchanged: no new 10/10 scores were approved during this sight recalibration. New sights must be rated **directly** against global peers. Do **not** rerun the [archived one-time sight correction script](scripts/recalibrate_sights_2026.py); its guard prevents a second application.

After adding or updating attractions:

```bash
python scripts/validate.py
python scripts/check_city_benchmarks.py
python scripts/check_sight_benchmarks.py
python scripts/generate_rankings.py --country XX
python scripts/generate_rankings.py --check
python scripts/rank.py --kind sights --limit 60
```

## Additional evidence-referenced per-sight research (22 November 2026)

An additional **266 named sights** have received individual desk research and explicit source-linked comparison notes, bringing the total to **415 site-specific editorial decisions** across the seven populated countries. **1,498** other sight records remain flagged as **automatically screened only**; this is a partial, documented research pass, not a claim that all 1,913 sights have been independently investigated. Every score modification is traceable in the [current per-item worldwide register](methodology/sight-review-2026-full-audit.md), with [supporting rationale](methodology/sight-review-2026-summary.md). No historical correction curves, country quotas, city-score edits or new 10/10 approvals were applied.

## Follow-on per-sight review (22 November 2026)

[New worldwide 1,913-sight reassessment summary](methodology/sight-review-2026-summary.md) · [Complete per-item change and diagnostic register](methodology/sight-review-2026-full-audit.md) · [149 site-specific decisions](methodology/sight-review-decisions-2026/).

The follow-on review explicitly separates individual desk-based score revisions from **automated screening only**. The latter is not a claim of independent research into each site. It corrects conspicuous inflated experience/depth and nested heritage comparisons without reopening the frozen one-time 2026 calibration scripts. Site-specific YAML remains canonical.

## Absolute worldwide calibration (v2)

The 1,540 legacy destinations (Austria, Thailand, South Korea and China) were conservatively recalibrated to worldwide v2; Vietnam's 500 and Cambodia's 332 destinations were rated directly using v2. All populated destinations follow the same globally calibrated 0–10 rubric. Local or national excellence is not sufficient for a 10: only the globally defining examples for that exact scoring dimension can attain 10. Each such approval is listed in `methodology/scoring.json` under `global_ten_anchors`; `scripts/validate.py` enforces it.

**For new countries:** score directly against the worldwide comparators in [rules.md](rules.md). The legacy `scripts/calibrate_worldwide.py` is a one-time v1→v2 migration, *not* a script for converting newly authored ratings. A global 10 requires reviewing worldwide peers and explicitly adding the destination ID to the approved benchmark list. Smaller countries can still earn 10 where they genuinely represent the world's best in a given category. Do not rescale scores separately by country.

## Destination file examples

`countries/AT/cities/vienna.yaml`:

```yaml
id: city-at-vienna
name: Vienna
location:
  country_code: AT
  latitude: 48.2082
  longitude: 16.3738
scores:
  impact: 9.0
  uniqueness: 8.8
  significance: 9.4
  experience: 9.2
  depth: 9.2
  categories:
    architecture: 9.3
    history: 9.5
    culture: 9.5
    food: 8.1
    nightlife: 7.5
    photography: 8.1
```

`countries/AT/sights/schoenbrunn-palace.yaml`:

```yaml
id: sight-at-schoenbrunn-palace
name: Schönbrunn Palace
location:
  country_code: AT
  latitude: 48.1845
  longitude: 16.3122
scores:
  impact: 9.0
  uniqueness: 8.8
  significance: 9.4
  experience: 9.2
  depth: 8.9
  categories:
    architecture: 9.4
    history: 9.3
    culture: 8.5
    photography: 8.5
```

Coordinates are approximate representative points, not verified entrance locations. Null means *not assessed*, not zero. Do not assign rankings to incomplete assessments.

## Notes

- Valid location fields: `country_code`, `latitude`, `longitude` only.
- Only the two requested destination kinds are stored: cities and sights.
- Overall scores are computed from assessed core dimensions; do not store redundant, manually edited totals.
- Give 10 only to a worldwide benchmark that is explicitly listed in `methodology/scoring.json`, and run `python scripts/validate.py` after editing scores.
- The country folders are created once by the generator, with `.gitkeep` files to keep empty directories in Git.
