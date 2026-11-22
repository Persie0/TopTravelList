# Cross-country sight calibration benchmark ladder (v2)

**Use for every future sight-scoring batch** together with
[sight-scoring-guide.md](sight-scoring-guide.md),
[the worldwide rules](../rules.md) and
[frozen 189 reference profiles](sight-benchmark-profiles.txt).

Scores represent subjective, revisable worldwide travel-quality
judgments. Do not mistake them for facts, accessibility guarantees,
country quotas or official UNESCO grades.

## International reference ladder

| Attraction | Scope and comparator type | Reviewed score /100 |
| --- | --- | ---: |
| Angkor Archaeological Park (KH) | Entire world-defining Khmer archaeological ensemble | 99.70 |
| Angkor Wat (KH) | Single world-defining temple within the park | 99.20 |
| Great Wall at Jinshanling (CN) | Global benchmark in monumental fortifications | 98.90 |
| Ha Long Bay (VN) | Globally extraordinary natural seascape | 97.85 |
| Gyeongju Historic Areas (KR) | Exceptional coherent historic landscape | 96.15 |
| Ayutthaya Historical Park (TH) | World-class ancient royal-city ensemble | 95.75 |
| Schönbrunn Palace (AT) | World-class imperial palace and gardens | 94.20 |
| Hofburg Palace (AT) | Exceptional historic urban palace/museum ensemble | 93.90 |
| Hohensalzburg Fortress (AT) | Internationally significant preserved fortification | 91.65 |
| Nha Trang Beach (VN) | Enjoyable city beach, less exceptional worldwide | 81.95 |
| Made in Cambodia Market (KH) | Worthwhile market without global heritage significance | 75.25 |
| Royal Gardens Siem Reap (KH) | Pleasant but replaceable urban park | 68.05 |

The ladder does not impose a universal upper limit on a future
destination. A new country can contain numerous genuinely
world-defining attractions, but an ordinary site cannot receive 9.9
just because it is well liked in its own country.

## Compare like with like, while still using global anchors

| Sight type | Important comparison set | Common inflation failure |
| --- | --- | --- |
| Archaeological landscape | Angkor Archaeological Park, Ayutthaya, Gyeongju, Koh Ker | Transferring the whole park's 99.7 to each gate, chapel or courtyard |
| Temple/palace | Angkor Wat, Forbidden City, Schönbrunn, Bulguksa, Wat Phra Kaew | Assuming any local temple or palace has unique world-level architecture |
| Fortification | Great Wall at Jinshanling, Hohensalzburg, Xi'an walls, Suwon Hwaseong | Doubling historical importance because there is a famous city nearby |
| Museums/memorials | Kunsthistorisches, National Museum of Korea, Tuol Sleng, War Remnants Museum | Overstating visitor depth or entertainment, confusing solemn significance with leisure |
| Protected landscapes | Huangshan, Phong Nha, Hohe Tauern, Khao Sok, Hallasan | Scoring one viewpoint at the full landscape's worldwide scale |
| Seascapes/islands | Ha Long Bay, Jeju, Koh Rong, Phang Nga Bay, Con Dao | Assigning identical near-perfect significance to every adjacent beach |
| Cave | Son Doong, Phong Nha, Eisriesenwelt, Manjanggul | Claiming all caves in the same national park share top-tier uniqueness |
| Beach | Nha Trang, Railay, Sokha Beach, Nai Yang | A nice shoreline treated as globally irreplaceable |
| Market/garden | Made in Cambodia Market, Royal Gardens Siem Reap, Ben Thanh Market | A pleasant local stop given 9.5+ historical significance |

## Selected comparison fixes

- **Hohensalzburg Fortress vs Made in Cambodia Market:** a
  world-significant medieval fortress outranks a local market
  overall, even though the market may deserve a good food score.
- **Hofburg Palace vs Royal Gardens Siem Reap:** the first is
  a major imperial heritage ensemble; the second is a pleasant
  ordinary urban garden. The same worldwide impact, uniqueness,
  significance and depth standards must apply to both.
- **Great Wall vs Schönbrunn:** both are exceptional; the
  Great Wall has separately approved global-defining exact
  fields, while Schönbrunn excels in architecture, heritage
  and a rewarding palace visit without automatic 10/10.
- **Angkor Archaeological Park vs Angkor Wat vs Bayon:**
  the parent ensemble has greater breadth; one component
  cannot inherit all of that experience and depth.
- **Ha Long Bay vs Nha Trang Beach:** both are scenic, but
  one is a globally exceptional karst seascape and the other
  a broadly replaceable enjoyable city beach.
- **Preah Vihear:** historical rank is not evidence of
  current admission; retain separate access/safety advisory.

## Required future batch review

For each newly added country, explicitly inspect:

1. Its finest cultural or historical site against **two**
   historic sites in other countries.
2. Its finest natural sight against **two** natural sites
   in other countries.
3. An ordinary local market, park, urban viewpoint or beach
   against the same type abroad.
4. Every 9.5+ core dimension and category separately against
   a global reference in that field.
5. Every nested pair of sights for score duplication.
6. Every proposed 10 against the exact ID and field in
   scoring.json/global_ten_anchors.
7. The top global rankings after adding the country, not
   just the country's top-five list.

Check:

    python scripts/validate.py
    python scripts/check_sight_benchmarks.py
    python scripts/generate_rankings.py --check
    python scripts/rank.py --kind sights --limit 60

**Never rerun the 2026 sight calibration curves on future records.**
The [one-time audit](sight-calibration-audit.md) documents their
historic purpose, and new sights are scored directly against
worldwide peers from the outset.
