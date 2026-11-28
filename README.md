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

The registry covers **250 geographic travel entries**: all 249 official ISO 3166-1 alpha-2 entries plus Kosovo (`XK`). Countries, overseas territories, dependencies and special-status areas are indexed separately for geographic navigation, not political recognition. See [territory expansion and migration policy](methodology/territory-expansion.md).

See [rules.md](rules.md) for the universal scoring rubric and [methodology/scoring.json](methodology/scoring.json) for the machine-readable weights and categories.

## Current destination-access advisories

Cambodia: As of **22 November 2026**, border-area attractions including the UNESCO-listed **Temple of Preah Vihear** are **reported closed** due to Cambodia–Thailand border tensions. Scores represent long-term heritage and experience potential, **not a guarantee of current access or safety**. Consult the [UK Foreign Office Cambodia travel advice](https://www.gov.uk/foreign-travel-advice/cambodia) and other current government advisories before planning travel; border-area restrictions may change.

## Explore on the map

Browse every catalogued city and sight in the [interactive travel atlas](https://top-travel-list.vercel.app). Each country ranking links to the destination's source YAML, a Google Maps search for its name and country (for example, [Vienna, Austria](https://www.google.com/maps/search/?api=1&query=Vienna%2C%20Austria)), and the original representative GPS point. Country map links are also available in the directory below.

## Country directory

Every registered country has a linked folder below. The status is determined from the YAML destinations and updated whenever rankings are regenerated.

<!-- COUNTRY_DIRECTORY_START -->

**250 done · 0 not done · 250 geographic entries total.**

**Done** means the required destination folders contain YAML records; for territories without permanent civilian settlements, sight records alone suffice. It does not mean that every possible destination has been cataloged.

### Done (250)

| Country | Cities | Sights | Google Maps |
| --- | ---: | ---: | --- |
| [Afghanistan](countries/AF/) (`AF`) | [10](countries/AF/cities.md) | [23](countries/AF/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Afghanistan) |
| [Albania](countries/AL/) (`AL`) | [35](countries/AL/cities.md) | [95](countries/AL/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Albania) |
| [Algeria](countries/DZ/) (`DZ`) | [11](countries/DZ/cities.md) | [47](countries/DZ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Algeria) |
| [American Samoa](countries/AS/) (`AS`) | [7](countries/AS/cities.md) | [15](countries/AS/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=American%20Samoa) |
| [Andorra](countries/AD/) (`AD`) | [21](countries/AD/cities.md) | [47](countries/AD/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Andorra) |
| [Angola](countries/AO/) (`AO`) | [8](countries/AO/cities.md) | [17](countries/AO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Angola) |
| [Anguilla](countries/AI/) (`AI`) | [3](countries/AI/cities.md) | [10](countries/AI/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Anguilla) |
| [Antarctica](countries/AQ/) (`AQ`) | [0](countries/AQ/cities.md) | [14](countries/AQ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Antarctica) |
| [Antigua and Barbuda](countries/AG/) (`AG`) | [10](countries/AG/cities.md) | [32](countries/AG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Antigua%20and%20Barbuda) |
| [Argentina](countries/AR/) (`AR`) | [40](countries/AR/cities.md) | [202](countries/AR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Argentina) |
| [Armenia](countries/AM/) (`AM`) | [20](countries/AM/cities.md) | [55](countries/AM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Armenia) |
| [Aruba](countries/AW/) (`AW`) | [2](countries/AW/cities.md) | [13](countries/AW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Aruba) |
| [Australia](countries/AU/) (`AU`) | [12](countries/AU/cities.md) | [222](countries/AU/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Australia) |
| [Austria](countries/AT/) (`AT`) | [45](countries/AT/cities.md) | [134](countries/AT/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Austria) |
| [Azerbaijan](countries/AZ/) (`AZ`) | [16](countries/AZ/cities.md) | [40](countries/AZ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Azerbaijan) |
| [Bahamas](countries/BS/) (`BS`) | [12](countries/BS/cities.md) | [34](countries/BS/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bahamas) |
| [Bahrain](countries/BH/) (`BH`) | [15](countries/BH/cities.md) | [46](countries/BH/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bahrain) |
| [Bangladesh](countries/BD/) (`BD`) | [15](countries/BD/cities.md) | [42](countries/BD/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bangladesh) |
| [Barbados](countries/BB/) (`BB`) | [10](countries/BB/cities.md) | [35](countries/BB/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Barbados) |
| [Belarus](countries/BY/) (`BY`) | [14](countries/BY/cities.md) | [35](countries/BY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Belarus) |
| [Belgium](countries/BE/) (`BE`) | [18](countries/BE/cities.md) | [64](countries/BE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Belgium) |
| [Belize](countries/BZ/) (`BZ`) | [18](countries/BZ/cities.md) | [144](countries/BZ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Belize) |
| [Benin](countries/BJ/) (`BJ`) | [18](countries/BJ/cities.md) | [34](countries/BJ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Benin) |
| [Bermuda](countries/BM/) (`BM`) | [3](countries/BM/cities.md) | [12](countries/BM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bermuda) |
| [Bhutan](countries/BT/) (`BT`) | [33](countries/BT/cities.md) | [89](countries/BT/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bhutan) |
| [Bolivia](countries/BO/) (`BO`) | [33](countries/BO/cities.md) | [132](countries/BO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bolivia) |
| [Bonaire, Sint Eustatius and Saba](countries/BQ/) (`BQ`) | [5](countries/BQ/cities.md) | [13](countries/BQ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bonaire%2C%20Sint%20Eustatius%20and%20Saba) |
| [Bosnia and Herzegovina](countries/BA/) (`BA`) | [44](countries/BA/cities.md) | [101](countries/BA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bosnia%20and%20Herzegovina) |
| [Botswana](countries/BW/) (`BW`) | [22](countries/BW/cities.md) | [38](countries/BW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Botswana) |
| [Bouvet Island](countries/BV/) (`BV`) | [0](countries/BV/cities.md) | [1](countries/BV/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bouvet%20Island) |
| [Brazil](countries/BR/) (`BR`) | [42](countries/BR/cities.md) | [238](countries/BR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Brazil) |
| [British Indian Ocean Territory (Chagos Archipelago)](countries/IO/) (`IO`) | [0](countries/IO/cities.md) | [5](countries/IO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=British%20Indian%20Ocean%20Territory%20%28Chagos%20Archipelago%29) |
| [Brunei](countries/BN/) (`BN`) | [9](countries/BN/cities.md) | [41](countries/BN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Brunei) |
| [Bulgaria](countries/BG/) (`BG`) | [18](countries/BG/cities.md) | [46](countries/BG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Bulgaria) |
| [Burkina Faso](countries/BF/) (`BF`) | [9](countries/BF/cities.md) | [35](countries/BF/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Burkina%20Faso) |
| [Burundi](countries/BI/) (`BI`) | [12](countries/BI/cities.md) | [26](countries/BI/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Burundi) |
| [Cabo Verde](countries/CV/) (`CV`) | [24](countries/CV/cities.md) | [47](countries/CV/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Cabo%20Verde) |
| [Cambodia](countries/KH/) (`KH`) | [72](countries/KH/cities.md) | [260](countries/KH/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Cambodia) |
| [Cameroon](countries/CM/) (`CM`) | [10](countries/CM/cities.md) | [28](countries/CM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Cameroon) |
| [Canada](countries/CA/) (`CA`) | [16](countries/CA/cities.md) | [384](countries/CA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Canada) |
| [Cayman Islands](countries/KY/) (`KY`) | [2](countries/KY/cities.md) | [11](countries/KY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Cayman%20Islands) |
| [Central African Republic](countries/CF/) (`CF`) | [10](countries/CF/cities.md) | [25](countries/CF/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Central%20African%20Republic) |
| [Chad](countries/TD/) (`TD`) | [10](countries/TD/cities.md) | [25](countries/TD/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Chad) |
| [Chile](countries/CL/) (`CL`) | [33](countries/CL/cities.md) | [156](countries/CL/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Chile) |
| [China](countries/CN/) (`CN`) | [229](countries/CN/cities.md) | [467](countries/CN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=China) |
| [Christmas Island](countries/CX/) (`CX`) | [1](countries/CX/cities.md) | [13](countries/CX/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Christmas%20Island) |
| [Cocos (Keeling) Islands](countries/CC/) (`CC`) | [2](countries/CC/cities.md) | [12](countries/CC/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Cocos%20%28Keeling%29%20Islands) |
| [Colombia](countries/CO/) (`CO`) | [46](countries/CO/cities.md) | [163](countries/CO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Colombia) |
| [Comoros](countries/KM/) (`KM`) | [14](countries/KM/cities.md) | [31](countries/KM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Comoros) |
| [Congo](countries/CG/) (`CG`) | [12](countries/CG/cities.md) | [29](countries/CG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Congo) |
| [Cook Islands](countries/CK/) (`CK`) | [4](countries/CK/cities.md) | [25](countries/CK/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Cook%20Islands) |
| [Costa Rica](countries/CR/) (`CR`) | [28](countries/CR/cities.md) | [140](countries/CR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Costa%20Rica) |
| [Croatia](countries/HR/) (`HR`) | [22](countries/HR/cities.md) | [55](countries/HR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Croatia) |
| [Cuba](countries/CU/) (`CU`) | [12](countries/CU/cities.md) | [36](countries/CU/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Cuba) |
| [Curaçao](countries/CW/) (`CW`) | [2](countries/CW/cities.md) | [13](countries/CW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Cura%C3%A7ao) |
| [Cyprus](countries/CY/) (`CY`) | [16](countries/CY/cities.md) | [38](countries/CY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Cyprus) |
| [Czechia](countries/CZ/) (`CZ`) | [61](countries/CZ/cities.md) | [145](countries/CZ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Czechia) |
| [Côte d'Ivoire](countries/CI/) (`CI`) | [10](countries/CI/cities.md) | [20](countries/CI/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=C%C3%B4te%20d%27Ivoire) |
| [Denmark](countries/DK/) (`DK`) | [18](countries/DK/cities.md) | [43](countries/DK/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Denmark) |
| [Djibouti](countries/DJ/) (`DJ`) | [10](countries/DJ/cities.md) | [25](countries/DJ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Djibouti) |
| [Dominica](countries/DM/) (`DM`) | [14](countries/DM/cities.md) | [32](countries/DM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Dominica) |
| [Dominican Republic](countries/DO/) (`DO`) | [12](countries/DO/cities.md) | [34](countries/DO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Dominican%20Republic) |
| [DR Congo](countries/CD/) (`CD`) | [8](countries/CD/cities.md) | [17](countries/CD/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=DR%20Congo) |
| [Ecuador](countries/EC/) (`EC`) | [36](countries/EC/cities.md) | [132](countries/EC/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Ecuador) |
| [Egypt](countries/EG/) (`EG`) | [10](countries/EG/cities.md) | [85](countries/EG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Egypt) |
| [El Salvador](countries/SV/) (`SV`) | [24](countries/SV/cities.md) | [110](countries/SV/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=El%20Salvador) |
| [Equatorial Guinea](countries/GQ/) (`GQ`) | [13](countries/GQ/cities.md) | [26](countries/GQ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Equatorial%20Guinea) |
| [Eritrea](countries/ER/) (`ER`) | [13](countries/ER/cities.md) | [30](countries/ER/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Eritrea) |
| [Estonia](countries/EE/) (`EE`) | [15](countries/EE/cities.md) | [42](countries/EE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Estonia) |
| [Eswatini](countries/SZ/) (`SZ`) | [15](countries/SZ/cities.md) | [30](countries/SZ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Eswatini) |
| [Ethiopia](countries/ET/) (`ET`) | [8](countries/ET/cities.md) | [23](countries/ET/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Ethiopia) |
| [Falkland Islands (Malvinas)](countries/FK/) (`FK`) | [3](countries/FK/cities.md) | [10](countries/FK/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Falkland%20Islands%20%28Malvinas%29) |
| [Faroe Islands](countries/FO/) (`FO`) | [4](countries/FO/cities.md) | [7](countries/FO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Faroe%20Islands) |
| [Fiji](countries/FJ/) (`FJ`) | [7](countries/FJ/cities.md) | [26](countries/FJ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Fiji) |
| [Finland](countries/FI/) (`FI`) | [19](countries/FI/cities.md) | [53](countries/FI/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Finland) |
| [France](countries/FR/) (`FR`) | [25](countries/FR/cities.md) | [1100](countries/FR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=France) |
| [French Guiana](countries/GF/) (`GF`) | [4](countries/GF/cities.md) | [24](countries/GF/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=French%20Guiana) |
| [French Polynesia](countries/PF/) (`PF`) | [5](countries/PF/cities.md) | [40](countries/PF/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=French%20Polynesia) |
| [French Southern Territories](countries/TF/) (`TF`) | [0](countries/TF/cities.md) | [7](countries/TF/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=French%20Southern%20Territories) |
| [Gabon](countries/GA/) (`GA`) | [14](countries/GA/cities.md) | [32](countries/GA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Gabon) |
| [Gambia](countries/GM/) (`GM`) | [16](countries/GM/cities.md) | [31](countries/GM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Gambia) |
| [Georgia](countries/GE/) (`GE`) | [14](countries/GE/cities.md) | [38](countries/GE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Georgia) |
| [Germany](countries/DE/) (`DE`) | [30](countries/DE/cities.md) | [101](countries/DE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Germany) |
| [Ghana](countries/GH/) (`GH`) | [20](countries/GH/cities.md) | [50](countries/GH/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Ghana) |
| [Gibraltar](countries/GI/) (`GI`) | [1](countries/GI/cities.md) | [9](countries/GI/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Gibraltar) |
| [Greece](countries/GR/) (`GR`) | [18](countries/GR/cities.md) | [111](countries/GR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Greece) |
| [Greenland](countries/GL/) (`GL`) | [7](countries/GL/cities.md) | [12](countries/GL/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Greenland) |
| [Grenada](countries/GD/) (`GD`) | [12](countries/GD/cities.md) | [33](countries/GD/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Grenada) |
| [Guadeloupe](countries/GP/) (`GP`) | [5](countries/GP/cities.md) | [32](countries/GP/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Guadeloupe) |
| [Guam](countries/GU/) (`GU`) | [5](countries/GU/cities.md) | [17](countries/GU/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Guam) |
| [Guatemala](countries/GT/) (`GT`) | [12](countries/GT/cities.md) | [142](countries/GT/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Guatemala) |
| [Guernsey](countries/GG/) (`GG`) | [4](countries/GG/cities.md) | [22](countries/GG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Guernsey) |
| [Guinea](countries/GN/) (`GN`) | [14](countries/GN/cities.md) | [30](countries/GN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Guinea) |
| [Guinea-Bissau](countries/GW/) (`GW`) | [13](countries/GW/cities.md) | [25](countries/GW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Guinea-Bissau) |
| [Guyana](countries/GY/) (`GY`) | [18](countries/GY/cities.md) | [74](countries/GY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Guyana) |
| [Haiti](countries/HT/) (`HT`) | [12](countries/HT/cities.md) | [32](countries/HT/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Haiti) |
| [Heard Island and McDonald Islands](countries/HM/) (`HM`) | [0](countries/HM/cities.md) | [1](countries/HM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Heard%20Island%20and%20McDonald%20Islands) |
| [Honduras](countries/HN/) (`HN`) | [31](countries/HN/cities.md) | [131](countries/HN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Honduras) |
| [Hong Kong](countries/HK/) (`HK`) | [1](countries/HK/cities.md) | [36](countries/HK/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Hong%20Kong) |
| [Hungary](countries/HU/) (`HU`) | [18](countries/HU/cities.md) | [50](countries/HU/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Hungary) |
| [Iceland](countries/IS/) (`IS`) | [15](countries/IS/cities.md) | [59](countries/IS/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Iceland) |
| [India](countries/IN/) (`IN`) | [97](countries/IN/cities.md) | [333](countries/IN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=India) |
| [Indonesia](countries/ID/) (`ID`) | [79](countries/ID/cities.md) | [344](countries/ID/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Indonesia) |
| [Iran](countries/IR/) (`IR`) | [15](countries/IR/cities.md) | [55](countries/IR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Iran) |
| [Iraq](countries/IQ/) (`IQ`) | [14](countries/IQ/cities.md) | [38](countries/IQ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Iraq) |
| [Ireland](countries/IE/) (`IE`) | [20](countries/IE/cities.md) | [46](countries/IE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Ireland) |
| [Isle of Man](countries/IM/) (`IM`) | [7](countries/IM/cities.md) | [24](countries/IM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Isle%20of%20Man) |
| [Israel](countries/IL/) (`IL`) | [12](countries/IL/cities.md) | [41](countries/IL/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Israel) |
| [Italy](countries/IT/) (`IT`) | [25](countries/IT/cities.md) | [175](countries/IT/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Italy) |
| [Jamaica](countries/JM/) (`JM`) | [11](countries/JM/cities.md) | [26](countries/JM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Jamaica) |
| [Japan](countries/JP/) (`JP`) | [87](countries/JP/cities.md) | [347](countries/JP/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Japan) |
| [Jersey](countries/JE/) (`JE`) | [4](countries/JE/cities.md) | [22](countries/JE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Jersey) |
| [Jordan](countries/JO/) (`JO`) | [21](countries/JO/cities.md) | [67](countries/JO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Jordan) |
| [Kazakhstan](countries/KZ/) (`KZ`) | [18](countries/KZ/cities.md) | [59](countries/KZ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Kazakhstan) |
| [Kenya](countries/KE/) (`KE`) | [6](countries/KE/cities.md) | [44](countries/KE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Kenya) |
| [Kiribati](countries/KI/) (`KI`) | [12](countries/KI/cities.md) | [16](countries/KI/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Kiribati) |
| [Kosovo](countries/XK/) (`XK`) | [20](countries/XK/cities.md) | [38](countries/XK/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Kosovo) |
| [Kuwait](countries/KW/) (`KW`) | [12](countries/KW/cities.md) | [50](countries/KW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Kuwait) |
| [Kyrgyzstan](countries/KG/) (`KG`) | [18](countries/KG/cities.md) | [46](countries/KG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Kyrgyzstan) |
| [Laos](countries/LA/) (`LA`) | [42](countries/LA/cities.md) | [144](countries/LA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Laos) |
| [Latvia](countries/LV/) (`LV`) | [18](countries/LV/cities.md) | [38](countries/LV/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Latvia) |
| [Lebanon](countries/LB/) (`LB`) | [13](countries/LB/cities.md) | [37](countries/LB/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Lebanon) |
| [Lesotho](countries/LS/) (`LS`) | [16](countries/LS/cities.md) | [38](countries/LS/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Lesotho) |
| [Liberia](countries/LR/) (`LR`) | [14](countries/LR/cities.md) | [26](countries/LR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Liberia) |
| [Libya](countries/LY/) (`LY`) | [11](countries/LY/cities.md) | [20](countries/LY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Libya) |
| [Liechtenstein](countries/LI/) (`LI`) | [15](countries/LI/cities.md) | [34](countries/LI/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Liechtenstein) |
| [Lithuania](countries/LT/) (`LT`) | [18](countries/LT/cities.md) | [37](countries/LT/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Lithuania) |
| [Luxembourg](countries/LU/) (`LU`) | [15](countries/LU/cities.md) | [32](countries/LU/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Luxembourg) |
| [Macau](countries/MO/) (`MO`) | [1](countries/MO/cities.md) | [12](countries/MO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Macau) |
| [Madagascar](countries/MG/) (`MG`) | [6](countries/MG/cities.md) | [36](countries/MG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Madagascar) |
| [Malawi](countries/MW/) (`MW`) | [18](countries/MW/cities.md) | [34](countries/MW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Malawi) |
| [Malaysia](countries/MY/) (`MY`) | [65](countries/MY/cities.md) | [213](countries/MY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Malaysia) |
| [Maldives](countries/MV/) (`MV`) | [25](countries/MV/cities.md) | [42](countries/MV/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Maldives) |
| [Mali](countries/ML/) (`ML`) | [11](countries/ML/cities.md) | [33](countries/ML/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Mali) |
| [Malta](countries/MT/) (`MT`) | [23](countries/MT/cities.md) | [37](countries/MT/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Malta) |
| [Marshall Islands](countries/MH/) (`MH`) | [11](countries/MH/cities.md) | [25](countries/MH/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Marshall%20Islands) |
| [Martinique](countries/MQ/) (`MQ`) | [4](countries/MQ/cities.md) | [35](countries/MQ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Martinique) |
| [Mauritania](countries/MR/) (`MR`) | [10](countries/MR/cities.md) | [17](countries/MR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Mauritania) |
| [Mauritius](countries/MU/) (`MU`) | [22](countries/MU/cities.md) | [63](countries/MU/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Mauritius) |
| [Mayotte](countries/YT/) (`YT`) | [2](countries/YT/cities.md) | [20](countries/YT/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Mayotte) |
| [Mexico](countries/MX/) (`MX`) | [36](countries/MX/cities.md) | [205](countries/MX/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Mexico) |
| [Micronesia, Federated States of](countries/FM/) (`FM`) | [6](countries/FM/cities.md) | [20](countries/FM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Micronesia%2C%20Federated%20States%20of) |
| [Moldova](countries/MD/) (`MD`) | [18](countries/MD/cities.md) | [33](countries/MD/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Moldova) |
| [Monaco](countries/MC/) (`MC`) | [1](countries/MC/cities.md) | [30](countries/MC/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Monaco) |
| [Mongolia](countries/MN/) (`MN`) | [18](countries/MN/cities.md) | [50](countries/MN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Mongolia) |
| [Montenegro](countries/ME/) (`ME`) | [33](countries/ME/cities.md) | [94](countries/ME/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Montenegro) |
| [Montserrat](countries/MS/) (`MS`) | [2](countries/MS/cities.md) | [8](countries/MS/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Montserrat) |
| [Morocco](countries/MA/) (`MA`) | [12](countries/MA/cities.md) | [79](countries/MA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Morocco) |
| [Mozambique](countries/MZ/) (`MZ`) | [7](countries/MZ/cities.md) | [16](countries/MZ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Mozambique) |
| [Myanmar](countries/MM/) (`MM`) | [12](countries/MM/cities.md) | [39](countries/MM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Myanmar) |
| [Namibia](countries/NA/) (`NA`) | [7](countries/NA/cities.md) | [21](countries/NA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Namibia) |
| [Nauru](countries/NR/) (`NR`) | [6](countries/NR/cities.md) | [6](countries/NR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Nauru) |
| [Nepal](countries/NP/) (`NP`) | [49](countries/NP/cities.md) | [123](countries/NP/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Nepal) |
| [Netherlands](countries/NL/) (`NL`) | [20](countries/NL/cities.md) | [51](countries/NL/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Netherlands) |
| [New Caledonia](countries/NC/) (`NC`) | [4](countries/NC/cities.md) | [32](countries/NC/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=New%20Caledonia) |
| [New Zealand](countries/NZ/) (`NZ`) | [12](countries/NZ/cities.md) | [126](countries/NZ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=New%20Zealand) |
| [Nicaragua](countries/NI/) (`NI`) | [13](countries/NI/cities.md) | [85](countries/NI/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Nicaragua) |
| [Niger](countries/NE/) (`NE`) | [10](countries/NE/cities.md) | [26](countries/NE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Niger) |
| [Nigeria](countries/NG/) (`NG`) | [12](countries/NG/cities.md) | [25](countries/NG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Nigeria) |
| [Niue](countries/NU/) (`NU`) | [4](countries/NU/cities.md) | [18](countries/NU/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Niue) |
| [Norfolk Island](countries/NF/) (`NF`) | [1](countries/NF/cities.md) | [13](countries/NF/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Norfolk%20Island) |
| [North Korea](countries/KP/) (`KP`) | [8](countries/KP/cities.md) | [22](countries/KP/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=North%20Korea) |
| [North Macedonia](countries/MK/) (`MK`) | [14](countries/MK/cities.md) | [33](countries/MK/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=North%20Macedonia) |
| [Northern Mariana Islands](countries/MP/) (`MP`) | [4](countries/MP/cities.md) | [19](countries/MP/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Northern%20Mariana%20Islands) |
| [Norway](countries/NO/) (`NO`) | [19](countries/NO/cities.md) | [50](countries/NO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Norway) |
| [Oman](countries/OM/) (`OM`) | [24](countries/OM/cities.md) | [74](countries/OM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Oman) |
| [Pakistan](countries/PK/) (`PK`) | [14](countries/PK/cities.md) | [58](countries/PK/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Pakistan) |
| [Palau](countries/PW/) (`PW`) | [7](countries/PW/cities.md) | [27](countries/PW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Palau) |
| [Palestine](countries/PS/) (`PS`) | [10](countries/PS/cities.md) | [36](countries/PS/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Palestine) |
| [Panama](countries/PA/) (`PA`) | [22](countries/PA/cities.md) | [226](countries/PA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Panama) |
| [Papua New Guinea](countries/PG/) (`PG`) | [7](countries/PG/cities.md) | [30](countries/PG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Papua%20New%20Guinea) |
| [Paraguay](countries/PY/) (`PY`) | [34](countries/PY/cities.md) | [101](countries/PY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Paraguay) |
| [Peru](countries/PE/) (`PE`) | [36](countries/PE/cities.md) | [228](countries/PE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Peru) |
| [Philippines](countries/PH/) (`PH`) | [15](countries/PH/cities.md) | [50](countries/PH/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Philippines) |
| [Pitcairn](countries/PN/) (`PN`) | [1](countries/PN/cities.md) | [10](countries/PN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Pitcairn) |
| [Poland](countries/PL/) (`PL`) | [22](countries/PL/cities.md) | [76](countries/PL/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Poland) |
| [Portugal](countries/PT/) (`PT`) | [20](countries/PT/cities.md) | [91](countries/PT/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Portugal) |
| [Puerto Rico](countries/PR/) (`PR`) | [5](countries/PR/cities.md) | [11](countries/PR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Puerto%20Rico) |
| [Qatar](countries/QA/) (`QA`) | [14](countries/QA/cities.md) | [64](countries/QA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Qatar) |
| [Romania](countries/RO/) (`RO`) | [20](countries/RO/cities.md) | [59](countries/RO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Romania) |
| [Russia](countries/RU/) (`RU`) | [20](countries/RU/cities.md) | [43](countries/RU/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Russia) |
| [Rwanda](countries/RW/) (`RW`) | [18](countries/RW/cities.md) | [47](countries/RW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Rwanda) |
| [Réunion](countries/RE/) (`RE`) | [5](countries/RE/cities.md) | [30](countries/RE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=R%C3%A9union) |
| [Saint Barthélemy](countries/BL/) (`BL`) | [2](countries/BL/cities.md) | [10](countries/BL/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Saint%20Barth%C3%A9lemy) |
| [Saint Helena, Ascension and Tristan da Cunha](countries/SH/) (`SH`) | [4](countries/SH/cities.md) | [14](countries/SH/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Saint%20Helena%2C%20Ascension%20and%20Tristan%20da%20Cunha) |
| [Saint Kitts and Nevis](countries/KN/) (`KN`) | [11](countries/KN/cities.md) | [30](countries/KN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Saint%20Kitts%20and%20Nevis) |
| [Saint Lucia](countries/LC/) (`LC`) | [12](countries/LC/cities.md) | [27](countries/LC/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Saint%20Lucia) |
| [Saint Martin (French part)](countries/MF/) (`MF`) | [2](countries/MF/cities.md) | [13](countries/MF/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Saint%20Martin%20%28French%20part%29) |
| [Saint Pierre and Miquelon](countries/PM/) (`PM`) | [2](countries/PM/cities.md) | [15](countries/PM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Saint%20Pierre%20and%20Miquelon) |
| [Saint Vincent and the Grenadines](countries/VC/) (`VC`) | [13](countries/VC/cities.md) | [51](countries/VC/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Saint%20Vincent%20and%20the%20Grenadines) |
| [Samoa](countries/WS/) (`WS`) | [6](countries/WS/cities.md) | [28](countries/WS/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Samoa) |
| [San Marino](countries/SM/) (`SM`) | [14](countries/SM/cities.md) | [25](countries/SM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=San%20Marino) |
| [Sao Tome and Principe](countries/ST/) (`ST`) | [12](countries/ST/cities.md) | [40](countries/ST/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Sao%20Tome%20and%20Principe) |
| [Saudi Arabia](countries/SA/) (`SA`) | [18](countries/SA/cities.md) | [70](countries/SA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Saudi%20Arabia) |
| [Senegal](countries/SN/) (`SN`) | [8](countries/SN/cities.md) | [23](countries/SN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Senegal) |
| [Serbia](countries/RS/) (`RS`) | [18](countries/RS/cities.md) | [43](countries/RS/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Serbia) |
| [Seychelles](countries/SC/) (`SC`) | [14](countries/SC/cities.md) | [49](countries/SC/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Seychelles) |
| [Sierra Leone](countries/SL/) (`SL`) | [13](countries/SL/cities.md) | [33](countries/SL/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Sierra%20Leone) |
| [Singapore](countries/SG/) (`SG`) | [1](countries/SG/cities.md) | [99](countries/SG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Singapore) |
| [Sint Maarten (Dutch part)](countries/SX/) (`SX`) | [2](countries/SX/cities.md) | [10](countries/SX/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Sint%20Maarten%20%28Dutch%20part%29) |
| [Slovakia](countries/SK/) (`SK`) | [15](countries/SK/cities.md) | [61](countries/SK/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Slovakia) |
| [Slovenia](countries/SI/) (`SI`) | [18](countries/SI/cities.md) | [45](countries/SI/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Slovenia) |
| [Solomon Islands](countries/SB/) (`SB`) | [9](countries/SB/cities.md) | [20](countries/SB/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Solomon%20Islands) |
| [Somalia](countries/SO/) (`SO`) | [10](countries/SO/cities.md) | [13](countries/SO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Somalia) |
| [South Africa](countries/ZA/) (`ZA`) | [12](countries/ZA/cities.md) | [122](countries/ZA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=South%20Africa) |
| [South Georgia and the South Sandwich Islands](countries/GS/) (`GS`) | [0](countries/GS/cities.md) | [10](countries/GS/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=South%20Georgia%20and%20the%20South%20Sandwich%20Islands) |
| [South Korea](countries/KR/) (`KR`) | [82](countries/KR/cities.md) | [285](countries/KR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=South%20Korea) |
| [South Sudan](countries/SS/) (`SS`) | [10](countries/SS/cities.md) | [20](countries/SS/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=South%20Sudan) |
| [Spain](countries/ES/) (`ES`) | [22](countries/ES/cities.md) | [192](countries/ES/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Spain) |
| [Sri Lanka](countries/LK/) (`LK`) | [55](countries/LK/cities.md) | [178](countries/LK/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Sri%20Lanka) |
| [Sudan](countries/SD/) (`SD`) | [9](countries/SD/cities.md) | [26](countries/SD/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Sudan) |
| [Suriname](countries/SR/) (`SR`) | [20](countries/SR/cities.md) | [70](countries/SR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Suriname) |
| [Svalbard and Jan Mayen](countries/SJ/) (`SJ`) | [2](countries/SJ/cities.md) | [12](countries/SJ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Svalbard%20and%20Jan%20Mayen) |
| [Sweden](countries/SE/) (`SE`) | [23](countries/SE/cities.md) | [66](countries/SE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Sweden) |
| [Switzerland](countries/CH/) (`CH`) | [20](countries/CH/cities.md) | [46](countries/CH/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Switzerland) |
| [Syria](countries/SY/) (`SY`) | [10](countries/SY/cities.md) | [31](countries/SY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Syria) |
| [Taiwan](countries/TW/) (`TW`) | [64](countries/TW/cities.md) | [180](countries/TW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Taiwan) |
| [Tajikistan](countries/TJ/) (`TJ`) | [14](countries/TJ/cities.md) | [45](countries/TJ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Tajikistan) |
| [Tanzania](countries/TZ/) (`TZ`) | [5](countries/TZ/cities.md) | [30](countries/TZ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Tanzania) |
| [Thailand](countries/TH/) (`TH`) | [69](countries/TH/cities.md) | [206](countries/TH/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Thailand) |
| [Timor-Leste](countries/TL/) (`TL`) | [24](countries/TL/cities.md) | [38](countries/TL/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Timor-Leste) |
| [Togo](countries/TG/) (`TG`) | [16](countries/TG/cities.md) | [31](countries/TG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Togo) |
| [Tokelau](countries/TK/) (`TK`) | [5](countries/TK/cities.md) | [4](countries/TK/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Tokelau) |
| [Tonga](countries/TO/) (`TO`) | [7](countries/TO/cities.md) | [21](countries/TO/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Tonga) |
| [Trinidad and Tobago](countries/TT/) (`TT`) | [12](countries/TT/cities.md) | [29](countries/TT/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Trinidad%20and%20Tobago) |
| [Tunisia](countries/TN/) (`TN`) | [11](countries/TN/cities.md) | [59](countries/TN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Tunisia) |
| [Turkmenistan](countries/TM/) (`TM`) | [12](countries/TM/cities.md) | [40](countries/TM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Turkmenistan) |
| [Turks and Caicos Islands](countries/TC/) (`TC`) | [3](countries/TC/cities.md) | [12](countries/TC/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Turks%20and%20Caicos%20Islands) |
| [Tuvalu](countries/TV/) (`TV`) | [9](countries/TV/cities.md) | [15](countries/TV/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Tuvalu) |
| [Türkiye](countries/TR/) (`TR`) | [20](countries/TR/cities.md) | [168](countries/TR/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=T%C3%BCrkiye) |
| [Uganda](countries/UG/) (`UG`) | [6](countries/UG/cities.md) | [25](countries/UG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Uganda) |
| [Ukraine](countries/UA/) (`UA`) | [14](countries/UA/cities.md) | [49](countries/UA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Ukraine) |
| [United Arab Emirates](countries/AE/) (`AE`) | [14](countries/AE/cities.md) | [83](countries/AE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=United%20Arab%20Emirates) |
| [United Kingdom](countries/GB/) (`GB`) | [30](countries/GB/cities.md) | [81](countries/GB/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=United%20Kingdom) |
| [United States](countries/US/) (`US`) | [15](countries/US/cities.md) | [548](countries/US/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=United%20States) |
| [United States Minor Outlying Islands](countries/UM/) (`UM`) | [0](countries/UM/cities.md) | [9](countries/UM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=United%20States%20Minor%20Outlying%20Islands) |
| [Uruguay](countries/UY/) (`UY`) | [33](countries/UY/cities.md) | [109](countries/UY/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Uruguay) |
| [Uzbekistan](countries/UZ/) (`UZ`) | [20](countries/UZ/cities.md) | [56](countries/UZ/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Uzbekistan) |
| [Vanuatu](countries/VU/) (`VU`) | [6](countries/VU/cities.md) | [21](countries/VU/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Vanuatu) |
| [Vatican City](countries/VA/) (`VA`) | [1](countries/VA/cities.md) | [24](countries/VA/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Vatican%20City) |
| [Venezuela](countries/VE/) (`VE`) | [35](countries/VE/cities.md) | [91](countries/VE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Venezuela) |
| [Vietnam](countries/VN/) (`VN`) | [140](countries/VN/cities.md) | [360](countries/VN/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Vietnam) |
| [Virgin Islands, British](countries/VG/) (`VG`) | [3](countries/VG/cities.md) | [10](countries/VG/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Virgin%20Islands%2C%20British) |
| [Virgin Islands, U.S.](countries/VI/) (`VI`) | [4](countries/VI/cities.md) | [11](countries/VI/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Virgin%20Islands%2C%20U.S.) |
| [Wallis and Futuna](countries/WF/) (`WF`) | [4](countries/WF/cities.md) | [15](countries/WF/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Wallis%20and%20Futuna) |
| [Western Sahara](countries/EH/) (`EH`) | [4](countries/EH/cities.md) | [5](countries/EH/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Western%20Sahara) |
| [Yemen](countries/YE/) (`YE`) | [10](countries/YE/cities.md) | [34](countries/YE/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Yemen) |
| [Zambia](countries/ZM/) (`ZM`) | [5](countries/ZM/cities.md) | [20](countries/ZM/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Zambia) |
| [Zimbabwe](countries/ZW/) (`ZW`) | [6](countries/ZW/cities.md) | [20](countries/ZW/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=Zimbabwe) |
| [Åland Islands](countries/AX/) (`AX`) | [3](countries/AX/cities.md) | [10](countries/AX/sights.md) | [Map](https://www.google.com/maps/search/?api=1&query=%C3%85land%20Islands) |

### Not done (0)

These geographic entries lack required destination records. Their country folders already exist; follow the links to populate them.

| Country | Country | Country | Country |
| --- | --- | --- | --- |

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
