# Worldwide missing-sights audit — pass 3 (2026-11-26)

Base commit: `de7ee3df311db8183bf16b64bd7fcaca01420896`. This is a coverage backlog, not a scoring revision. The previous passes screened 250 areas against 958 landmark terms and compared selected national park inventories. This pass targets urban, museum, cultural, leisure and visitor-experience gaps. A normalized substring comparison against canonical sight YAML filenames screened 363 terms across 54 areas, yielding 212 unmatched terms. These are NOT 212 verified distinct omissions: aliases, spelling differences, parent properties, country indexing, existing city records and prior-pass candidates require resolution. No scores, coordinates or rankings are changed.

## Priority A — source-supported standalone candidates

The following sources were inspected in search results on 2026-11-26 for identity and experience scope; this is not the complete per-record fact-check required for scoring. Each candidate still requires coordinate verification, exact name/alias check, individual five-field rationale and four worldwide comparisons.

| Area | Candidate | Scope / reason | Source |
|---|---|---|---|
| US | Metropolitan Museum of Art (Fifth Avenue) | Distinct encyclopedic art museum | [Met](https://www.metmuseum.org/tours) |
| US | National Air and Space Museum (National Mall) | Aviation and spaceflight collection, distinct from Udvar-Hazy Center | [Smithsonian](https://www.si.edu/museums/air-and-space-museum) |
| US | National Gallery of Art | Separate major art institution, not a generic Smithsonian entry | [NGA](https://www.nga.gov/visit) |
| US | National Museum of African American History and Culture | Dedicated national historical and cultural museum | [Smithsonian](https://www.si.edu/museums/african-american-museum) |
| CA | Royal Ontario Museum | Art, culture and natural history collections | [Destination Ontario](https://www.destinationontario.com/en-ca/attractions/royal-ontario-museum) |
| CA | Art Gallery of Ontario | Dedicated Canadian, Indigenous and international art collections | [Destination Ontario](https://www.destinationontario.com/en-ca/things-to-do/museums-and-art-galleries) |
| AU | National Gallery of Victoria | Distinct art institution; determine whether International and Australia campuses merit separate entries | [Tourism Australia](https://www.australia.com/en/places/melbourne-and-surrounds/best-museums-art-galleries-and-theatres.html) |
| AU | National Gallery of Australia | National collection with Aboriginal Memorial | [Tourism Australia](https://www.australia.com/en/things-to-do/arts-and-culture/australias-historical-and-cultural-experiences.html) |
| AU | Museum of Old and New Art (MONA) | Distinct contemporary and historical art experience | [Tourism Australia](https://www.australia.com/en/things-to-do/arts-and-culture/australias-historical-and-cultural-experiences.html) |
| AU | Australian War Memorial | Separately visitable Canberra museum and memorial | [Tourism Australia](https://www.australia.com/en-gb/places/canberra-and-surrounds/best-museums-art-galleries-and-theatres.html) |
| DE | Neues Museum | Separate Museum Island institution; do not inherit parent rating | [Berlin](https://www.berlin.de/en/museums/3109123-3104050-neues-museum.en.html) |
| DE | Jewish Museum Berlin | German-Jewish history and purpose-designed building | [Berlin](https://www.berlin.de/en/museums/3108776-3104050-jewish-museum-berlin.en.html) |
| DE | Topography of Terror | Historic site and documentation exhibition | [Berlin](https://www.berlin.de/en/museums/3109737-3104050-topography-of-terror.en.html) |
| IT | Galleria dell'Accademia, Florence | Michelangelo sculpture collection including David | [Visit Florence](https://www.visitflorence.com/florence-museums/accademia-gallery.html) |
| IT | Museo Egizio, Turin | Dedicated Egyptian museum | [Italia.it](https://www.italia.it/en/piedmont/turin/egyptian-museum-turin) |
| ES | Reina Sofía Museum | Modern art collection including Guernica | [Madrid tourism](https://www.esmadrid.com/en/tourist-information/reina-sofia-museum) |
| ES | Thyssen-Bornemisza National Museum | Distinct art collection and visitor experience | [Madrid tourism](https://www.esmadrid.com/en/tourist-information/thyssen-bornemisza-national-museum) |
| ES | Royal Palace of Madrid | Royal palace visitor experience | [Madrid tourism](https://www.esmadrid.com/en/madrid-top-10) |
| AT | Albertina | Museum in historic Habsburg palace, distinct from Hofburg | [Vienna tourism](https://www.wien.info/de/kunst-kultur/museen-ausstellungen/top-museen/albertina-338616) |
| MX | Frida Kahlo Museum (Casa Azul) | Artist's former home, separate from Rivera-Kahlo studio | [Visit Mexico](https://visitmexico.com/es/itinerario/4/coyoacan-centro) |

## Raw unmatched-name backlog (selected for resolution, not automatic insertion)

| Area | Unmatched search terms |
|---|---|
| US | Museum of Modern Art; American Museum of Natural History; Smithsonian (umbrella only); Art Institute of Chicago; Getty Center; Getty Villa; Kennedy Space Center; Alcatraz; Golden Gate Bridge; Empire State; Rockefeller Center; Times Square; National Mall; Lincoln Memorial; Jefferson Memorial; White House; Mount Rushmore; Space Needle; Hoover Dam; Las Vegas Strip; Disneyland; Walt Disney World; Universal Studios; Niagara Falls; Antelope Canyon; Monument Valley; Napa Valley; Pearl Harbor; Waikiki; Na Pali; Waimea Canyon; Big Sur; also priority A entries |
| CA | Montreal Museum of Fine Arts; Canadian Museum of History; Canadian Museum for Human Rights; Capilano; Parliament Hill; Hopewell Rocks; Churchill; Butchart Gardens; Granville Island; Whistler; Toronto Islands; Old Montreal; Notre-Dame Basilica; also priority A entries |
| AU | Royal Botanic Gardens; Taronga Zoo; Phillip Island; Whitehaven; Whitsunday; Fremantle Prison; Port Arthur; Broome Cable Beach; Kangaroo Island; Byron Bay; Rottnest; Blue Lake Mount Gambier; also priority A entries. Convict sites already exist as parent. |
| NZ | Auckland War Memorial Museum; Otago Museum; International Antarctic Centre; Sky Tower; Zealandia; Kaikoura; Moeraki; Doubtful Sound; Cathedral Cove; Roys Peak; Hooker Valley; Te Puia; Waimangu; Hells Gate |
| GB | Science Museum; Imperial War Museum; National Museum of Scotland; Buckingham Palace; Tower Bridge; White Cliffs of Dover; Westminster Abbey (inspect Westminster parent) |
| FR | Orangerie; Rodin; Pompidou; Invalides; Pantheon; Sainte-Chapelle; Arc de Triomphe; Disneyland; Les Baux; Carrières de Lumières |
| DE | Pergamon; Alte Nationalgalerie; Checkpoint Charlie; Deutsches Museum; BMW Welt; Porsche Museum; Mercedes-Benz Museum; Europa-Park; Phantasialand; Rakotzbrücke; also priority A entries. Check actual visitor access for Pergamon. |
| IT | Borghese; Capitoline; Brera; Blue Grotto; also priority A entries |
| ES | Picasso Museum; Dalí Theatre-Museum; City of Arts and Sciences; Bioparc; PortAventura; Caminito del Rey; Bernabéu; Camp Nou; Montserrat; also priority A entries |
| PT | National Tile Museum; Oceanário; Pico do Arieiro; Seven Hanging Valleys; 25 Fontes levada |
| NL | Kröller-Müller Museum |
| BE | Magritte Museum; Royal Museums; Train World; Autoworld |
| CH | Swiss Museum of Transport; Technorama; Creux du Van; Bernina Express (check railway parent) |
| SE | ABBA Museum; Kungsleden; High Coast Trail |
| NO | Viking Ship Museum (check redevelopment/access); Atlantic Ocean Road; Segla; Nigardsbreen |
| DK | Ny Carlsberg Glyptotek |
| FI | Kiasma; Amos Rex |
| AT | Technisches Museum; Hangar-7; Haus des Meeres; also priority A entry |
| EG | Muhammad Ali Mosque; Al-Azhar; Dahab Blue Hole |
| ZA | Zeitz MOCAA; Tsitsikamma; Chapman's Peak; Hermanus |
| BR | Oscar Niemeyer Museum |
| MX | National Museum of Anthropology; Palacio de Bellas Artes; Chapultepec Castle; Soumaya; Xcaret; also priority A entry |
| AR | Puerto Madero |
| KR | Leeum Museum |
| AE | Ferrari World; Warner Bros. World; SeaWorld Abu Dhabi |
| HK | Disneyland; Ocean Park |
| IN | National Museum Delhi; Nehru Science Centre |
| TR | Dolmabahçe Palace; Istanbul Archaeological Museums; Rahmi M. Koç Museum; Galata Tower |
| GR | Delphi Museum |
| PL | Schindler's Factory |
| CZ | National Technical Museum |
| HU | House of Terror; Hungarian National Museum |
| RO | Peleș Castle (inspect Sinaia royal residences parent) |
| IL / PS | Western Wall; check geographic registry convention and Jerusalem records before adding; no political inference |
| IS | Perlan; Kerið |
| RU | Tretyakov Gallery; St Isaac's Cathedral; Catherine Palace; Pushkin Museum |
| ID | Waterbom |

No unmatched terms in this pass's query set for JP, SG, QA, SA, TW, PE, CO, CL, EC, CR, PA, JM, TH, MY, VN or KH. This does not establish exhaustive coverage.

## Resolved filename aliases / scope cases

- GB: Victoria and Albert Museum → `victoria-albert.yaml`; Westminster Abbey → inspect `westminster.yaml` parent, not an automatic duplicate.
- FR: Dune du Pilat → `dune-pilat.yaml`; do not add again.
- DE: Miniatur Wunderland → `hamburg-miniatur.yaml` (inspect title before any addition).
- IT: Doge's Palace → `doges-palace.yaml`; St Mark's → `st-marks.yaml`; Pragser Wildsee → `lake-braies.yaml`; Egyptian Museum/Turin Egyptian/Museo Egizio are one candidate.
- ES: “serrat” and Montserrat are one search target; do not create two.
- PT: Gulbenkian → `gulbenkian.yaml`; Ponta da Piedade → `ponta-piedade.yaml`; Madeira Peaks and Madeira Levadas are broad existing records.
- EG: National Museum of Egyptian Civilization → `nmec.yaml`.
- GR: National Archaeological Museum → `national-arch-museum.yaml`.
- IE: Titanic Belfast belongs in GB and `countries/GB/sights/titanic-belfast.yaml` exists.
- US: Smithsonian as a whole is not a single attraction; use individual institutions. Niagara Falls Canadian side is already recorded in CA; assess a distinct US visitor scope only.
- CA: Churchill and Whistler are settlement/gateway names; use distinct wildlife or mountain experiences, not an automatic duplicated city.

## Next steps and guardrails

1. Process source-supported candidates first, checking exact scope and representative coordinates.
2. Add only genuinely distinct attractions. For parent/component cases record an explicit scope decision.
3. Follow AGENTS.md and existing V2 rubric without country quotas or popularity-based scores. Keep all unknown fields null until supported. Do not invent reviews or peer comparisons.
4. Regenerate rankings and run validators when actual YAML is changed. This documentation-only pass did not run validators or GitHub Actions.
