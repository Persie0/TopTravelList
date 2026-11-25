# TopTravelList web atlas

A static Vite/Leaflet application. The build reads every registered country's source YAML and methodology/scoring.json, calculates overall scores using decimal arithmetic, and exports the browser index. No scores are maintained independently. Country polygons are Natural Earth (world-atlas); small countries have centroid markers. The OpenStreetMap basemap requires a network connection and attribution is displayed. No API key or database is needed.

## Local
From web/: npm install, npm test, npm run dev, npm run build. Build output: dist/.

## Vercel
Link Persie0/TopTravelList, Root Directory web, enable Include source files outside of the Root Directory, disable skipping unaffected projects so country data changes trigger builds. Vite preset, build command npm run test && npm run build, output dist. Git integration automatically rebuilds from main; no GitHub Actions are needed.

## Interpretation
Ranks are competition ranks within the selected country/region and city/sight scope, computed before search and minimum-score filtering. Overall scores use the canonical weighted sum (0–100); categories and dimensions use 0–10. Explicit null ratings remain unassessed; omitted categories are inapplicable and excluded from category rankings. Country coverage is not a country score. Map borders are geographic reference only; coordinates are representative. City/sight types are inferred from names. The original YAML and ranking Markdown are linked from destination details.

The combined city/sight view is the default. See [performance and visualization notes](README-performance.md). Exact decimal arithmetic is build-only; the client uses exported scores.

Every result and destination detail has a Google Maps search link using the destination name and country. Detail views retain a separate representative GPS link; country-directory results search the country name.
