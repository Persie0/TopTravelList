export function imageSearchUrl(name,country=''){return 'https://www.google.com/search?tbm=isch&q='+encodeURIComponent([name,country].filter(Boolean).join(', '))}

export function withinViewport(rows,{south,north,west,east}){if(east<west)east+=360*Math.ceil((west-east)/360);return rows.filter(r=>Number.isFinite(r.lat)&&Number.isFinite(r.lon)&&r.lat>=south&&r.lat<=north&&r.lon+360*Math.ceil((west-r.lon)/360)<=east)}

export function explorePreset(preset){const thresholds={80:80,90:90,95:95};const top={top25:25,top100:100,top250:250};return {metric:'overall',sort:'score',unranked:false,min:thresholds[preset]??0,top:top[preset]??0}}
