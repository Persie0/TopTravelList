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

## Country bubbles and analytics
In destination map mode, select **Country bubbles** to see one count circle per country with matching map destinations. Circles use the country registry center (or a representative destination if no center is available), size encodes count, and color encodes the mean assessed score for the current metric. Counts include matching unassessed destinations (except when map top-N selects assessed ranks only); means exclude them. The map top-N limit applies, and nearby country circles may overlap but are never combined. Clicking a circle filters to that country and returns to ranked markers for drill-down, preserving the active destination search and score/type filters. The top-N limit is recalculated within the selected country. Directory navigation instead resets hidden destination filters. Selecting an individual destination from the list switches country bubbles to ranked markers. The selected visualization is shareable via the URL.

The **Explore the numbers** section uses all filtered results, independently of the map's top-N limit and list pagination. It shows count, country coverage, mean/median, assessment coverage, exceptional scores, leading countries by count or mean, regional counts, score distribution, city/sight composition, type-specific averages, and dimension/category averages with assessment counts. Country comparisons are descriptive, not official country rankings. In the country directory, analytics use overall scores from the countries matching the directory search/region. Destination details show overall rank and mean among assessed destinations of the same kind in that country, independent of explorer filters.

## Statistical explorer
Seven additional charts summarize the same filtered dataset: score-quality doughnut, geographic coverage, regional score box plots, interactive threshold survival curve, country count/mean scatter plot, destination-type score tiers and regional dimension heatmap. Four extra KPIs show estimated 90th percentile, interquartile range, full score range and registry coverage. Quantiles use linear interpolation on sorted assessed scores. The threshold slider explores assessed scores (inclusive threshold) without modifying destination filters. Coverage uses registered countries/territories in the selected geography (or directory search) as its denominator, with catalogued and currently represented counts shown independently. Heatmap means exclude unavailable values and include per-cell sample sizes. The scatter plot uses a logarithmic count axis and an accessible exact-data table with country drill-down. All charts use existing exported scores without modifying rankings or methodology.

### Route planner and custom statistics

The **Routes** workspace searches the same catalog of cities and sights. Select a region or country, a score threshold, maximum straight-line leg, destination type and number of stops. Start from a named destination or compare up to three suggested clusters. Add or reorder stops manually, find nearby highlights, optimize the open route with its first stop fixed, export CSV or open Google Maps directions. Routes are stored locally (no account or external routing request). Distances are great-circle estimates and do not imply road connectivity, opening hours, visas, accessibility, transport schedules or actual travel time. Google Maps may limit waypoint counts, especially on mobile.

The **Statistics** workspace retains existing atlas filters and adds a configurable comparison chart with bar and table views, selectable score measures, assessment sample threshold and grouping. Semantic score bands use green (90+), light green (80+), amber (65+), red (below 65), grey (unassessed), proportionally scaled for 10-point metrics. Counts and categorical charts use neutral colors rather than implying quality.
