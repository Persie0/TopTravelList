export const value = (row, metric) => metric === 'overall' ? row.overall : (row.scores[metric] ?? row.scores.categories?.[metric] ?? null);
export function ranked(rows, metric='overall') {
  const sorted = [...rows].sort((a,b) => (value(b,metric) ?? -Infinity)-(value(a,metric) ?? -Infinity) || a.name.localeCompare(b.name,'en') || a.id.localeCompare(b.id));
  let previous=null, rank=null;
  return sorted.map((row,i) => {const v=value(row,metric); if(v===null) return {...row,rank:null}; if(v!==previous || i===0) rank=i+1; previous=v; return {...row,rank};});
}
const searchIndex=new WeakMap();
export const normalize=s=>s.normalize('NFD').replace(/\p{Diacritic}/gu,'').toLowerCase();
export function eligible(rows,metric,categories){return categories.includes(metric)?rows.filter(r=>Object.hasOwn(r.scores.categories||{},metric)):rows}
export function distribution(rows,metric){const d={cities:0,sights:0,ranked:0,bins:Array(10).fill(0)};for(const r of rows){d[r.kind]++;const v=value(r,metric);if(v!==null){d.ranked++;d.bins[Math.max(0,Math.min(9,Math.floor(v/(metric==='overall'?10:1))))]++}}return d}
export function groupPoints(rows,project,bounds,size,worldWidth){
 const groups=new Map(),center=(bounds.minX+bounds.maxX)/2;
 for(const row of rows){const p=project(row),x=p.x+Math.round((center-p.x)/worldWidth)*worldWidth,y=p.y;if(x<bounds.minX||x>bounds.maxX||y<bounds.minY||y>bounds.maxY)continue;const key=Math.floor(x/size)+':'+Math.floor(y/size);let g=groups.get(key);if(!g){g={x:0,y:0,rows:[]};groups.set(key,g)}g.x+=x;g.y+=y;g.rows.push(row)}
 return [...groups.values()]
}
export function match(rows,{country='',region='',kind='',metric='overall',query='',min=0,unranked=true}={},countries={}) {
  const q=query.normalize('NFD').replace(/\p{Diacritic}/gu,'').toLowerCase().trim();
  const norm=r=>{let entry=searchIndex.get(r);const countryName=countries[r.country]?.name||'';if(!entry||entry.countryName!==countryName){entry={countryName,text:normalize([r.name,countryName,r.country,r.type].join(' '))};searchIndex.set(r,entry)}return entry.text};
  return rows.filter(r=>{const c=countries[r.country];const v=value(r,metric);return (!country||r.country===country)&&(!region||c?.region===region)&&(!kind||r.kind===kind)&&(!q||norm(r).includes(q))&&(v===null?unranked&&min===0:v>=min);});
}

export function scoreBins(metric){const step=metric==='overall'?10:1;return Array.from({length:10},(_,i)=>i===9?String(i*step)+'–'+String(10*step):String(i*step)+' to under '+String((i+1)*step))}
export function wrappedLocations(rows){
 if(!rows.length)return [];
 const lons=rows.map(r=>((r.lon%360)+360)%360).sort((a,b)=>a-b);let gap=-1,start=lons[0];
 for(let i=0;i<lons.length;i++){const next=i===lons.length-1?lons[0]+360:lons[i+1];if(next-lons[i]>gap){gap=next-lons[i];start=next%360}}
 const span=360-gap, shift=360*Math.floor((start+span/2+180)/360);
 return rows.map(r=>{let lon=((r.lon%360)+360)%360;if(lon<start-1e-9)lon+=360;return [r.lat,lon-shift]})
}

export function mapsSearchUrl(name, country){
 const query=country ? name+', '+country : name;
 return 'https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(query).replace(/[!'()*]/g,c=>'%'+c.charCodeAt(0).toString(16).toUpperCase());
}
