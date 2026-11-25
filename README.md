# TopTravelList

A consistent, worldwide ranking dataset for **cities** and **sights**.

## Repository layout

```text
countries/
  _registry.json
  AT/
    cities.md  # full computed city ranking + name/country and GPS Google Maps links
    sights.md  # full computed sights ranking + name/country and GPS Google Maps links
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

## Explore on the map

Browse every catalogued city and sight in the [interactive travel atlas](https://top-travel-list.vercel.app). Each country ranking links to the destination's source YAML, a Google Maps search for its name and country (for example, [Vienna, Austria](https://www.google.com/maps/search/?api=1&query=Vienna%2C%20Austria)), and the original representative GPS point. Country map links are also available in the directory below.

## Country directory

Every registered country has a linked folder below. The status is determined from the YAML destinations and updated whenever rankings are regenerated.

<!-- COUNTRY_DIRECTORY_START -->

**53 done · 144 not done · 197 countries total.**

**Done** means both the city and sight folders contain destination YAML records. It does not mean that every possible destination has been cataloged.

### Done (53)

| Country | Cities | Sights | Google Maps |
| --- | ---: | ---: | --- |
| [Albania](countries/AL/) (`AL`) | [35](countries/AL/cities.md) | [95](countries/AL/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Albania) |
| [Argentina](countries/AR/) (`AR`) | [40](countries/AR/cities.md) | [65](countries/AR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Argentina) |
| [Armenia](countries/AM/) (`AM`) | [20](countries/AM/cities.md) | [55](countries/AM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Armenia) |
| [Austria](countries/AT/) (`AT`) | [45](countries/AT/cities.md) | [133](countries/AT/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Austria) |
| [Bahrain](countries/BH/) (`BH`) | [15](countries/BH/cities.md) | [40](countries/BH/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bahrain) |
| [Bangladesh](countries/BD/) (`BD`) | [15](countries/BD/cities.md) | [42](countries/BD/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bangladesh) |
| [Belize](countries/BZ/) (`BZ`) | [18](countries/BZ/cities.md) | [61](countries/BZ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Belize) |
| [Benin](countries/BJ/) (`BJ`) | [18](countries/BJ/cities.md) | [34](countries/BJ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Benin) |
| [Bhutan](countries/BT/) (`BT`) | [33](countries/BT/cities.md) | [89](countries/BT/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bhutan) |
| [Bolivia](countries/BO/) (`BO`) | [33](countries/BO/cities.md) | [56](countries/BO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bolivia) |
| [Bosnia and Herzegovina](countries/BA/) (`BA`) | [44](countries/BA/cities.md) | [101](countries/BA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bosnia%20and%20Herzegovina) |
| [Botswana](countries/BW/) (`BW`) | [22](countries/BW/cities.md) | [38](countries/BW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Botswana) |
| [Brazil](countries/BR/) (`BR`) | [42](countries/BR/cities.md) | [85](countries/BR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Brazil) |
| [Brunei](countries/BN/) (`BN`) | [9](countries/BN/cities.md) | [41](countries/BN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Brunei) |
| [Cambodia](countries/KH/) (`KH`) | [72](countries/KH/cities.md) | [260](countries/KH/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Cambodia) |
| [Chile](countries/CL/) (`CL`) | [33](countries/CL/cities.md) | [67](countries/CL/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Chile) |
| [China](countries/CN/) (`CN`) | [231](countries/CN/cities.md) | [490](countries/CN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=China) |
| [Colombia](countries/CO/) (`CO`) | [46](countries/CO/cities.md) | [55](countries/CO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Colombia) |
| [Czechia](countries/CZ/) (`CZ`) | [61](countries/CZ/cities.md) | [145](countries/CZ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Czechia) |
| [Djibouti](countries/DJ/) (`DJ`) | [10](countries/DJ/cities.md) | [25](countries/DJ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Djibouti) |
| [Ecuador](countries/EC/) (`EC`) | [36](countries/EC/cities.md) | [55](countries/EC/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Ecuador) |
| [El Salvador](countries/SV/) (`SV`) | [24](countries/SV/cities.md) | [54](countries/SV/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=El%20Salvador) |
| [Guyana](countries/GY/) (`GY`) | [18](countries/GY/cities.md) | [39](countries/GY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Guyana) |
| [India](countries/IN/) (`IN`) | [97](countries/IN/cities.md) | [333](countries/IN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=India) |
| [Indonesia](countries/ID/) (`ID`) | [79](countries/ID/cities.md) | [343](countries/ID/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Indonesia) |
| [Japan](countries/JP/) (`JP`) | [87](countries/JP/cities.md) | [347](countries/JP/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Japan) |
| [Jordan](countries/JO/) (`JO`) | [21](countries/JO/cities.md) | [67](countries/JO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Jordan) |
| [Kuwait](countries/KW/) (`KW`) | [12](countries/KW/cities.md) | [43](countries/KW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Kuwait) |
| [Laos](countries/LA/) (`LA`) | [42](countries/LA/cities.md) | [144](countries/LA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Laos) |
| [Lesotho](countries/LS/) (`LS`) | [16](countries/LS/cities.md) | [38](countries/LS/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Lesotho) |
| [Liechtenstein](countries/LI/) (`LI`) | [15](countries/LI/cities.md) | [34](countries/LI/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Liechtenstein) |
| [Malawi](countries/MW/) (`MW`) | [18](countries/MW/cities.md) | [34](countries/MW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Malawi) |
| [Malaysia](countries/MY/) (`MY`) | [65](countries/MY/cities.md) | [213](countries/MY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Malaysia) |
| [Mauritius](countries/MU/) (`MU`) | [22](countries/MU/cities.md) | [63](countries/MU/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Mauritius) |
| [Montenegro](countries/ME/) (`ME`) | [33](countries/ME/cities.md) | [94](countries/ME/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Montenegro) |
| [Nepal](countries/NP/) (`NP`) | [49](countries/NP/cities.md) | [123](countries/NP/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Nepal) |
| [Oman](countries/OM/) (`OM`) | [24](countries/OM/cities.md) | [60](countries/OM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Oman) |
| [Paraguay](countries/PY/) (`PY`) | [34](countries/PY/cities.md) | [52](countries/PY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Paraguay) |
| [Peru](countries/PE/) (`PE`) | [36](countries/PE/cities.md) | [66](countries/PE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Peru) |
| [Qatar](countries/QA/) (`QA`) | [14](countries/QA/cities.md) | [55](countries/QA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Qatar) |
| [San Marino](countries/SM/) (`SM`) | [14](countries/SM/cities.md) | [25](countries/SM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=San%20Marino) |
| [Sao Tome and Principe](countries/ST/) (`ST`) | [12](countries/ST/cities.md) | [40](countries/ST/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Sao%20Tome%20and%20Principe) |
| [Seychelles](countries/SC/) (`SC`) | [14](countries/SC/cities.md) | [49](countries/SC/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Seychelles) |
| [Singapore](countries/SG/) (`SG`) | [1](countries/SG/cities.md) | [99](countries/SG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Singapore) |
| [South Korea](countries/KR/) (`KR`) | [82](countries/KR/cities.md) | [284](countries/KR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=South%20Korea) |
| [Sri Lanka](countries/LK/) (`LK`) | [55](countries/LK/cities.md) | [178](countries/LK/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Sri%20Lanka) |
| [Suriname](countries/SR/) (`SR`) | [20](countries/SR/cities.md) | [37](countries/SR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Suriname) |
| [Taiwan](countries/TW/) (`TW`) | [64](countries/TW/cities.md) | [180](countries/TW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Taiwan) |
| [Thailand](countries/TH/) (`TH`) | [69](countries/TH/cities.md) | [206](countries/TH/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Thailand) |
| [Togo](countries/TG/) (`TG`) | [16](countries/TG/cities.md) | [31](countries/TG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Togo) |
| [Uruguay](countries/UY/) (`UY`) | [33](countries/UY/cities.md) | [61](countries/UY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Uruguay) |
| [Vatican City](countries/VA/) (`VA`) | [1](countries/VA/cities.md) | [24](countries/VA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Vatican%20City) |
| [Vietnam](countries/VN/) (`VN`) | [140](countries/VN/cities.md) | [360](countries/VN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Vietnam) |

### Not done (144)

These countries have no entries in one or both destination folders yet. Their country folders already exist; follow the links to populate them.

| Country | Country | Country | Country |
| --- | --- | --- | --- |
| [Afghanistan](countries/AF/) (`AF`) · [Map](https://www.google.com/maps/search/?api=1&query=Afghanistan) | [Algeria](countries/DZ/) (`DZ`) · [Map](https://www.google.com/maps/search/?api=1&query=Algeria) | [Andorra](countries/AD/) (`AD`) · [Map](https://www.google.com/maps/search/?api=1&query=Andorra) | [Angola](countries/AO/) (`AO`) · [Map](https://www.google.com/maps/search/?api=1&query=Angola) |
| [Antigua and Barbuda](countries/AG/) (`AG`) · [Map](https://www.google.com/maps/search/?api=1&query=Antigua%20and%20Barbuda) | [Australia](countries/AU/) (`AU`) · [Map](https://www.google.com/maps/search/?api=1&query=Australia) | [Azerbaijan](countries/AZ/) (`AZ`) · [Map](https://www.google.com/maps/search/?api=1&query=Azerbaijan) | [Bahamas](countries/BS/) (`BS`) · [Map](https://www.google.com/maps/search/?api=1&query=Bahamas) |
| [Barbados](countries/BB/) (`BB`) · [Map](https://www.google.com/maps/search/?api=1&query=Barbados) | [Belarus](countries/BY/) (`BY`) · [Map](https://www.google.com/maps/search/?api=1&query=Belarus) | [Belgium](countries/BE/) (`BE`) · [Map](https://www.google.com/maps/search/?api=1&query=Belgium) | [Bulgaria](countries/BG/) (`BG`) · [Map](https://www.google.com/maps/search/?api=1&query=Bulgaria) |
| [Burkina Faso](countries/BF/) (`BF`) · [Map](https://www.google.com/maps/search/?api=1&query=Burkina%20Faso) | [Burundi](countries/BI/) (`BI`) · [Map](https://www.google.com/maps/search/?api=1&query=Burundi) | [Cabo Verde](countries/CV/) (`CV`) · [Map](https://www.google.com/maps/search/?api=1&query=Cabo%20Verde) | [Cameroon](countries/CM/) (`CM`) · [Map](https://www.google.com/maps/search/?api=1&query=Cameroon) |
| [Canada](countries/CA/) (`CA`) · [Map](https://www.google.com/maps/search/?api=1&query=Canada) | [Central African Republic](countries/CF/) (`CF`) · [Map](https://www.google.com/maps/search/?api=1&query=Central%20African%20Republic) | [Chad](countries/TD/) (`TD`) · [Map](https://www.google.com/maps/search/?api=1&query=Chad) | [Comoros](countries/KM/) (`KM`) · [Map](https://www.google.com/maps/search/?api=1&query=Comoros) |
| [Congo](countries/CG/) (`CG`) · [Map](https://www.google.com/maps/search/?api=1&query=Congo) | [Costa Rica](countries/CR/) (`CR`) · [Map](https://www.google.com/maps/search/?api=1&query=Costa%20Rica) | [Croatia](countries/HR/) (`HR`) · [Map](https://www.google.com/maps/search/?api=1&query=Croatia) | [Cuba](countries/CU/) (`CU`) · [Map](https://www.google.com/maps/search/?api=1&query=Cuba) |
| [Cyprus](countries/CY/) (`CY`) · [Map](https://www.google.com/maps/search/?api=1&query=Cyprus) | [Côte d'Ivoire](countries/CI/) (`CI`) · [Map](https://www.google.com/maps/search/?api=1&query=C%C3%B4te%20d%27Ivoire) | [Denmark](countries/DK/) (`DK`) · [Map](https://www.google.com/maps/search/?api=1&query=Denmark) | [Dominica](countries/DM/) (`DM`) · [Map](https://www.google.com/maps/search/?api=1&query=Dominica) |
| [Dominican Republic](countries/DO/) (`DO`) · [Map](https://www.google.com/maps/search/?api=1&query=Dominican%20Republic) | [DR Congo](countries/CD/) (`CD`) · [Map](https://www.google.com/maps/search/?api=1&query=DR%20Congo) | [Egypt](countries/EG/) (`EG`) · [Map](https://www.google.com/maps/search/?api=1&query=Egypt) | [Equatorial Guinea](countries/GQ/) (`GQ`) · [Map](https://www.google.com/maps/search/?api=1&query=Equatorial%20Guinea) |
| [Eritrea](countries/ER/) (`ER`) · [Map](https://www.google.com/maps/search/?api=1&query=Eritrea) | [Estonia](countries/EE/) (`EE`) · [Map](https://www.google.com/maps/search/?api=1&query=Estonia) | [Eswatini](countries/SZ/) (`SZ`) · [Map](https://www.google.com/maps/search/?api=1&query=Eswatini) | [Ethiopia](countries/ET/) (`ET`) · [Map](https://www.google.com/maps/search/?api=1&query=Ethiopia) |
| [Fiji](countries/FJ/) (`FJ`) · [Map](https://www.google.com/maps/search/?api=1&query=Fiji) | [Finland](countries/FI/) (`FI`) · [Map](https://www.google.com/maps/search/?api=1&query=Finland) | [France](countries/FR/) (`FR`) · [Map](https://www.google.com/maps/search/?api=1&query=France) | [Gabon](countries/GA/) (`GA`) · [Map](https://www.google.com/maps/search/?api=1&query=Gabon) |
| [Gambia](countries/GM/) (`GM`) · [Map](https://www.google.com/maps/search/?api=1&query=Gambia) | [Georgia](countries/GE/) (`GE`) · [Map](https://www.google.com/maps/search/?api=1&query=Georgia) | [Germany](countries/DE/) (`DE`) · [Map](https://www.google.com/maps/search/?api=1&query=Germany) | [Ghana](countries/GH/) (`GH`) · [Map](https://www.google.com/maps/search/?api=1&query=Ghana) |
| [Greece](countries/GR/) (`GR`) · [Map](https://www.google.com/maps/search/?api=1&query=Greece) | [Grenada](countries/GD/) (`GD`) · [Map](https://www.google.com/maps/search/?api=1&query=Grenada) | [Guatemala](countries/GT/) (`GT`) · [Map](https://www.google.com/maps/search/?api=1&query=Guatemala) | [Guinea](countries/GN/) (`GN`) · [Map](https://www.google.com/maps/search/?api=1&query=Guinea) |
| [Guinea-Bissau](countries/GW/) (`GW`) · [Map](https://www.google.com/maps/search/?api=1&query=Guinea-Bissau) | [Haiti](countries/HT/) (`HT`) · [Map](https://www.google.com/maps/search/?api=1&query=Haiti) | [Honduras](countries/HN/) (`HN`) · [Map](https://www.google.com/maps/search/?api=1&query=Honduras) | [Hungary](countries/HU/) (`HU`) · [Map](https://www.google.com/maps/search/?api=1&query=Hungary) |
| [Iceland](countries/IS/) (`IS`) · [Map](https://www.google.com/maps/search/?api=1&query=Iceland) | [Iran](countries/IR/) (`IR`) · [Map](https://www.google.com/maps/search/?api=1&query=Iran) | [Iraq](countries/IQ/) (`IQ`) · [Map](https://www.google.com/maps/search/?api=1&query=Iraq) | [Ireland](countries/IE/) (`IE`) · [Map](https://www.google.com/maps/search/?api=1&query=Ireland) |
| [Israel](countries/IL/) (`IL`) · [Map](https://www.google.com/maps/search/?api=1&query=Israel) | [Italy](countries/IT/) (`IT`) · [Map](https://www.google.com/maps/search/?api=1&query=Italy) | [Jamaica](countries/JM/) (`JM`) · [Map](https://www.google.com/maps/search/?api=1&query=Jamaica) | [Kazakhstan](countries/KZ/) (`KZ`) · [Map](https://www.google.com/maps/search/?api=1&query=Kazakhstan) |
| [Kenya](countries/KE/) (`KE`) · [Map](https://www.google.com/maps/search/?api=1&query=Kenya) | [Kiribati](countries/KI/) (`KI`) · [Map](https://www.google.com/maps/search/?api=1&query=Kiribati) | [Kosovo](countries/XK/) (`XK`) · [Map](https://www.google.com/maps/search/?api=1&query=Kosovo) | [Kyrgyzstan](countries/KG/) (`KG`) · [Map](https://www.google.com/maps/search/?api=1&query=Kyrgyzstan) |
| [Latvia](countries/LV/) (`LV`) · [Map](https://www.google.com/maps/search/?api=1&query=Latvia) | [Lebanon](countries/LB/) (`LB`) · [Map](https://www.google.com/maps/search/?api=1&query=Lebanon) | [Liberia](countries/LR/) (`LR`) · [Map](https://www.google.com/maps/search/?api=1&query=Liberia) | [Libya](countries/LY/) (`LY`) · [Map](https://www.google.com/maps/search/?api=1&query=Libya) |
| [Lithuania](countries/LT/) (`LT`) · [Map](https://www.google.com/maps/search/?api=1&query=Lithuania) | [Luxembourg](countries/LU/) (`LU`) · [Map](https://www.google.com/maps/search/?api=1&query=Luxembourg) | [Madagascar](countries/MG/) (`MG`) · [Map](https://www.google.com/maps/search/?api=1&query=Madagascar) | [Maldives](countries/MV/) (`MV`) · [Map](https://www.google.com/maps/search/?api=1&query=Maldives) |
| [Mali](countries/ML/) (`ML`) · [Map](https://www.google.com/maps/search/?api=1&query=Mali) | [Malta](countries/MT/) (`MT`) · [Map](https://www.google.com/maps/search/?api=1&query=Malta) | [Marshall Islands](countries/MH/) (`MH`) · [Map](https://www.google.com/maps/search/?api=1&query=Marshall%20Islands) | [Mauritania](countries/MR/) (`MR`) · [Map](https://www.google.com/maps/search/?api=1&query=Mauritania) |
| [Mexico](countries/MX/) (`MX`) · [Map](https://www.google.com/maps/search/?api=1&query=Mexico) | [Micronesia, Federated States of](countries/FM/) (`FM`) · [Map](https://www.google.com/maps/search/?api=1&query=Micronesia%2C%20Federated%20States%20of) | [Moldova](countries/MD/) (`MD`) · [Map](https://www.google.com/maps/search/?api=1&query=Moldova) | [Monaco](countries/MC/) (`MC`) · [Map](https://www.google.com/maps/search/?api=1&query=Monaco) |
| [Mongolia](countries/MN/) (`MN`) · [Map](https://www.google.com/maps/search/?api=1&query=Mongolia) | [Morocco](countries/MA/) (`MA`) · [Map](https://www.google.com/maps/search/?api=1&query=Morocco) | [Mozambique](countries/MZ/) (`MZ`) · [Map](https://www.google.com/maps/search/?api=1&query=Mozambique) | [Myanmar](countries/MM/) (`MM`) · [Map](https://www.google.com/maps/search/?api=1&query=Myanmar) |
| [Namibia](countries/NA/) (`NA`) · [Map](https://www.google.com/maps/search/?api=1&query=Namibia) | [Nauru](countries/NR/) (`NR`) · [Map](https://www.google.com/maps/search/?api=1&query=Nauru) | [Netherlands](countries/NL/) (`NL`) · [Map](https://www.google.com/maps/search/?api=1&query=Netherlands) | [New Zealand](countries/NZ/) (`NZ`) · [Map](https://www.google.com/maps/search/?api=1&query=New%20Zealand) |
| [Nicaragua](countries/NI/) (`NI`) · [Map](https://www.google.com/maps/search/?api=1&query=Nicaragua) | [Niger](countries/NE/) (`NE`) · [Map](https://www.google.com/maps/search/?api=1&query=Niger) | [Nigeria](countries/NG/) (`NG`) · [Map](https://www.google.com/maps/search/?api=1&query=Nigeria) | [North Korea](countries/KP/) (`KP`) · [Map](https://www.google.com/maps/search/?api=1&query=North%20Korea) |
| [North Macedonia](countries/MK/) (`MK`) · [Map](https://www.google.com/maps/search/?api=1&query=North%20Macedonia) | [Norway](countries/NO/) (`NO`) · [Map](https://www.google.com/maps/search/?api=1&query=Norway) | [Pakistan](countries/PK/) (`PK`) · [Map](https://www.google.com/maps/search/?api=1&query=Pakistan) | [Palau](countries/PW/) (`PW`) · [Map](https://www.google.com/maps/search/?api=1&query=Palau) |
| [Palestine](countries/PS/) (`PS`) · [Map](https://www.google.com/maps/search/?api=1&query=Palestine) | [Panama](countries/PA/) (`PA`) · [Map](https://www.google.com/maps/search/?api=1&query=Panama) | [Papua New Guinea](countries/PG/) (`PG`) · [Map](https://www.google.com/maps/search/?api=1&query=Papua%20New%20Guinea) | [Philippines](countries/PH/) (`PH`) · [Map](https://www.google.com/maps/search/?api=1&query=Philippines) |
| [Poland](countries/PL/) (`PL`) · [Map](https://www.google.com/maps/search/?api=1&query=Poland) | [Portugal](countries/PT/) (`PT`) · [Map](https://www.google.com/maps/search/?api=1&query=Portugal) | [Romania](countries/RO/) (`RO`) · [Map](https://www.google.com/maps/search/?api=1&query=Romania) | [Russia](countries/RU/) (`RU`) · [Map](https://www.google.com/maps/search/?api=1&query=Russia) |
| [Rwanda](countries/RW/) (`RW`) · [Map](https://www.google.com/maps/search/?api=1&query=Rwanda) | [Saint Kitts and Nevis](countries/KN/) (`KN`) · [Map](https://www.google.com/maps/search/?api=1&query=Saint%20Kitts%20and%20Nevis) | [Saint Lucia](countries/LC/) (`LC`) · [Map](https://www.google.com/maps/search/?api=1&query=Saint%20Lucia) | [Saint Vincent and the Grenadines](countries/VC/) (`VC`) · [Map](https://www.google.com/maps/search/?api=1&query=Saint%20Vincent%20and%20the%20Grenadines) |
| [Samoa](countries/WS/) (`WS`) · [Map](https://www.google.com/maps/search/?api=1&query=Samoa) | [Saudi Arabia](countries/SA/) (`SA`) · [Map](https://www.google.com/maps/search/?api=1&query=Saudi%20Arabia) | [Senegal](countries/SN/) (`SN`) · [Map](https://www.google.com/maps/search/?api=1&query=Senegal) | [Serbia](countries/RS/) (`RS`) · [Map](https://www.google.com/maps/search/?api=1&query=Serbia) |
| [Sierra Leone](countries/SL/) (`SL`) · [Map](https://www.google.com/maps/search/?api=1&query=Sierra%20Leone) | [Slovakia](countries/SK/) (`SK`) · [Map](https://www.google.com/maps/search/?api=1&query=Slovakia) | [Slovenia](countries/SI/) (`SI`) · [Map](https://www.google.com/maps/search/?api=1&query=Slovenia) | [Solomon Islands](countries/SB/) (`SB`) · [Map](https://www.google.com/maps/search/?api=1&query=Solomon%20Islands) |
| [Somalia](countries/SO/) (`SO`) · [Map](https://www.google.com/maps/search/?api=1&query=Somalia) | [South Africa](countries/ZA/) (`ZA`) · [Map](https://www.google.com/maps/search/?api=1&query=South%20Africa) | [South Sudan](countries/SS/) (`SS`) · [Map](https://www.google.com/maps/search/?api=1&query=South%20Sudan) | [Spain](countries/ES/) (`ES`) · [Map](https://www.google.com/maps/search/?api=1&query=Spain) |
| [Sudan](countries/SD/) (`SD`) · [Map](https://www.google.com/maps/search/?api=1&query=Sudan) | [Sweden](countries/SE/) (`SE`) · [Map](https://www.google.com/maps/search/?api=1&query=Sweden) | [Switzerland](countries/CH/) (`CH`) · [Map](https://www.google.com/maps/search/?api=1&query=Switzerland) | [Syria](countries/SY/) (`SY`) · [Map](https://www.google.com/maps/search/?api=1&query=Syria) |
| [Tajikistan](countries/TJ/) (`TJ`) · [Map](https://www.google.com/maps/search/?api=1&query=Tajikistan) | [Tanzania](countries/TZ/) (`TZ`) · [Map](https://www.google.com/maps/search/?api=1&query=Tanzania) | [Timor-Leste](countries/TL/) (`TL`) · [Map](https://www.google.com/maps/search/?api=1&query=Timor-Leste) | [Tonga](countries/TO/) (`TO`) · [Map](https://www.google.com/maps/search/?api=1&query=Tonga) |
| [Trinidad and Tobago](countries/TT/) (`TT`) · [Map](https://www.google.com/maps/search/?api=1&query=Trinidad%20and%20Tobago) | [Tunisia](countries/TN/) (`TN`) · [Map](https://www.google.com/maps/search/?api=1&query=Tunisia) | [Turkmenistan](countries/TM/) (`TM`) · [Map](https://www.google.com/maps/search/?api=1&query=Turkmenistan) | [Tuvalu](countries/TV/) (`TV`) · [Map](https://www.google.com/maps/search/?api=1&query=Tuvalu) |
| [Türkiye](countries/TR/) (`TR`) · [Map](https://www.google.com/maps/search/?api=1&query=T%C3%BCrkiye) | [Uganda](countries/UG/) (`UG`) · [Map](https://www.google.com/maps/search/?api=1&query=Uganda) | [Ukraine](countries/UA/) (`UA`) · [Map](https://www.google.com/maps/search/?api=1&query=Ukraine) | [United Arab Emirates](countries/AE/) (`AE`) · [Map](https://www.google.com/maps/search/?api=1&query=United%20Arab%20Emirates) |
| [United Kingdom](countries/GB/) (`GB`) · [Map](https://www.google.com/maps/search/?api=1&query=United%20Kingdom) | [United States](countries/US/) (`US`) · [Map](https://www.google.com/maps/search/?api=1&query=United%20States) | [Uzbekistan](countries/UZ/) (`UZ`) · [Map](https://www.google.com/maps/search/?api=1&query=Uzbekistan) | [Vanuatu](countries/VU/) (`VU`) · [Map](https://www.google.com/maps/search/?api=1&query=Vanuatu) |
| [Venezuela](countries/VE/) (`VE`) · [Map](https://www.google.com/maps/search/?api=1&query=Venezuela) | [Yemen](countries/YE/) (`YE`) · [Map](https://www.google.com/maps/search/?api=1&query=Yemen) | [Zambia](countries/ZM/) (`ZM`) · [Map](https://www.google.com/maps/search/?api=1&query=Zambia) | [Zimbabwe](countries/ZW/) (`ZW`) · [Map](https://www.google.com/maps/search/?api=1&query=Zimbabwe) |

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

## How to assess future countries and new destinations

**Every future city and sight needs its own worldwide comparison and review note, not just a generated numerical score.** Start with [agent/contributor instructions](AGENTS.md), the [step-by-step new-country workflow](methodology/future-country-workflow.md), [one-record review template](methodology/review-record-template.md), and [source-verification / quality standard](methodology/evidence-and-quality-standard.md). These supplement, rather than replace, the city/sight scoring guides above.

New decisions and later re-reviews belong under `methodology/reviews/XX/cities.md` or `methodology/reviews/XX/sights.md`. Keep source YAML as the authority, derive overall scores from the unchanged worldwide v2 weights, link at least four meaningful international peers per record, and verify factual claims separately from subjective scoring. Historical 2026 migration and audit files are retained as archival evidence, not reused for new countries. Source-linked or editorial-only decisions must not be presented as independently fact-checked.

## Additional evidence-referenced per-sight research (22 November 2026)

All **1,913 sights have distinct, individually authored editorial scoring decisions** across the seven populated countries, with five core dimensions and site-specific rationales. **632** decision rationales contain explicit external source links; the other **1,281** are desk-based judgments that still require independent source verification. **0** sights remain marked automatically screened only. The [complete per-item worldwide audit](methodology/sight-review-2026-full-audit.md) and [decision rationale summary](methodology/sight-review-2026-summary.md) preserve every review. This completes editorial scoring coverage, **not independent factual verification of all 1,913 scores**. No historical correction curves, country quotas, city-score edits or new 10/10 approvals were applied.

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
