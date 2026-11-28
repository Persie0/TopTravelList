# PR #388 — reconciliation with main

Source head 089d0f081fc4916059ea528f8734cab502cf1c4e; main e18b593249728495e771e8506efa2fae5f49b389. All 141 proposed sight YAMLs checked for IDs, country codes, coordinate ranges, numeric scores, category keys and weighted totals. New distinct records imported. Existing main assessments retained rather than overwritten. Equivalent or materially overlapping visitor scopes consolidated using the canonical main IDs below. Historical evidence and proposals remain in source reviews and backlog, with links redirected to canonical records. [Competing same-ID scores](pr-388-same-id-decisions.md).

| Country | Main before | New distinct imports | Same ID retained | Alternate IDs consolidated | After | 90+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| CL | 96 | 60 | 0 | 0 | 156 | 41 |
| CR | 135 | 5 | 19 | 21 | 140 | 25 |
| PA | 225 | 1 | 15 | 20 | 226 | 27 |

| Country | Alternate source slug | Canonical main slug |
| --- | --- | --- |
| CR | ostional-arribada | ostional-sea-turtle-arribada |
| CR | boruca-juego-diablitos | boruca-juego-de-los-diablitos |
| CR | pavones-surfing | pavones-surf-break |
| CR | nicoya-virgen-guadalupe-yeguita | nicoya-guadalupe-yeguita |
| CR | san-jose-festival-internacional-artes | festival-internacional-de-las-artes |
| CR | san-jose-festival-de-la-luz | festival-de-la-luz |
| CR | sarchi-oxcart-heritage | sarchi-oxcart-tradition |
| CR | barva-san-bartolome-mascaradas | barva-mascarada-festival |
| CR | isla-san-lucas-national-park | san-lucas-island-national-park |
| CR | tarcoles-crocodile-boat | tarcoles-crocodile-observation |
| CR | bajos-del-toro-waterfalls | catarata-del-toro-blue-falls |
| CR | las-cruces-wilson-garden | las-cruces-wilson-botanical-garden |
| CR | gandoca-manzanillo-refuge | gandoca-manzanillo-wildlife-refuge |
| CR | barra-del-colorado-refuge | barra-del-colorado-wetlands |
| CR | palmares-fiestas | palmares-civic-festival |
| CR | lake-arenal-windsurfing | lake-arenal-water-sports |
| CR | los-quetzales-national-park | san-gerardo-de-dota-quetzal-birding |
| CR | doka-coffee-estate | doka-estate-coffee-tour |
| CR | isla-tortuga | isla-tortuga-snorkeling |
| CR | hacienda-baru-refuge | hacienda-baru-wildlife-refuge |
| CR | san-jose-costa-rican-art-museum | museo-de-arte-costarricense |
| PA | la-villa-corpus-christi | corpus-christi-la-villa-de-los-santos |
| PA | portobelo-congo-festival | portobelo-diablos-congos-festival |
| PA | las-tablas-mil-polleras | mil-polleras-parade |
| PA | guarare-mejorana-festival | guarare-festival-mejorana |
| PA | las-tablas-pollera-festival | national-pollera-festival |
| PA | parara-puru-embera | chagres-embera-community-visit |
| PA | portobelo-cristo-negro | portobelo-black-christ-pilgrimage |
| PA | isla-canas-arribada | isla-canas-turtle-arribada |
| PA | pearl-islands-whale-watching | pearl-islands-humpback-whale-watching |
| PA | anton-toro-guapo | anton-toro-guapo-festival |
| PA | san-san-pond-sak | san-san-pond-sak-national-park |
| PA | punta-patino-reserve | punta-patino-nature-reserve |
| PA | boquete-flowers-coffee-fair | boquete-flower-coffee-fair |
| PA | boquete-don-pepe-coffee | boquete-geisha-coffee-circuit |
| PA | anton-cristo-esquipulas | anton-esquipulas-festival |
| PA | panama-mola-museum | museo-de-la-mola |
| PA | nata-basilica | nata-santiago-apostol-church |
| PA | cerro-gaital | cerro-gaital-natural-monument |
| PA | gualaca-cangilones | cangilones-de-gualaca |
| PA | summit-botanical-garden | summit-municipal-park |

Scope distinctions retained: Limón Grand Gala Parade (August) versus carnival (October); original Monteverde canopy operator versus Selvatura; La Pintada weaving museum/workshops versus annual hat festival. Existing main records are not removed. Full Python validation not executed in this reconciliation; structural checks used JS. No workflows manually dispatched. Ratings and coordinates are not independent factual certifications.
