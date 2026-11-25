// Accept either decimal separator independently of the browser's locale.
export function parseMinimumScore(input,metric='overall'){
 const text=String(input??'').trim();
 if(!text)return 0;
 if(!/^(?:\d+(?:[.,]\d*)?|[.,]\d+)$/.test(text))return null;
 const n=Number(text.replace(',','.'));
 return Number.isFinite(n)&&n>=0&&n<=(metric==='overall'?100:10)?n:null;
}
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
  const terms=normalize(query).split(/[\s,]+/).filter(Boolean);
  const norm=r=>{let entry=searchIndex.get(r);const countryName=countries[r.country]?.name||'';if(!entry||entry.countryName!==countryName){entry={countryName,text:normalize([r.name,countryName,r.country,r.type].join(' '))};searchIndex.set(r,entry)}return entry.text};
  return rows.filter(r=>{const c=countries[r.country];const v=value(r,metric);return (!country||r.country===country)&&(!region||c?.region===region)&&(!kind||r.kind===kind)&&terms.every(q=>norm(r).includes(q))&&(v===null?unranked&&min===0:v>=min);});
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

// Render dateline-crossing polygons as clipped pieces on either side of the map.
// A ring winding around a pole is already defined by its geographic boundary;
// leave it unchanged rather than inventing a new polar boundary.
function unwrapRing(ring,reference){
 if(!ring.length)return ring;
 const first=ring[0][0]+(reference===undefined?0:360*Math.round((reference-ring[0][0])/360));
 const out=[[first,ring[0][1]]];
 for(let i=1;i<ring.length;i++){const [x,y]=ring[i],previous=out[i-1][0];out.push([x+360*Math.round((previous-x)/360),y])}
 return out
}
function clipRing(ring,bound,keepRight){
 if(ring.length<4)return [];
 const out=[],inside=p=>keepRight?p[0]>=bound:p[0]<=bound;
 let a=ring[ring.length-2],was=inside(a);
 for(const b of ring.slice(0,-1)){
   const now=inside(b);
   if(now!==was){const t=(bound-a[0])/(b[0]-a[0]);out.push([bound,a[1]+t*(b[1]-a[1])])}
   if(now)out.push(b);
   a=b;was=now;
 }
 if(out.length<3)return [];
 out.push(out[0]);return out;
}
export function splitMapGeometry(geometry){
 if(!geometry||!['Polygon','MultiPolygon'].includes(geometry.type))return geometry;
 const polygons=geometry.type==='Polygon'?[geometry.coordinates]:geometry.coordinates, result=[];
 for(const polygon of polygons){
  if(!polygon.length||!polygon[0].length)continue;
  const exterior=unwrapRing(polygon[0]);
  if(Math.abs(exterior.at(-1)[0]-exterior[0][0])>1e-6){result.push(polygon);continue}
  const xs=exterior.map(p=>p[0]),lo=Math.min(...xs),hi=Math.max(...xs);
  if(lo>=-180&&hi<=180&&polygon[0].every((p,i)=>!i||Math.abs(p[0]-polygon[0][i-1][0])<=180)){result.push(polygon);continue}
  const rings=[exterior,...polygon.slice(1).map(r=>unwrapRing(r,(lo+hi)/2))];
  for(let k=Math.floor((lo+180)/360);k<=Math.floor((hi+180)/360);k++){
   const clipped=rings.map(r=>clipRing(clipRing(r,-180+360*k,true),180+360*k,false));
   if(!clipped[0].length)continue;
   result.push(clipped.filter(r=>r.length).map(r=>r.map(([x,y])=>[x-360*k,y])));
  }
 }
 return {type:'MultiPolygon',coordinates:result};
}
export function clusterRadius(n,size){return Math.min(size*.37,8+Math.sqrt(n)*1.3)}
export function coalesceGroups(groups,size){
 // At broad zooms, merge colliding labels across cell boundaries. The weighted
 // centroid and every member are retained; the best-ranked member remains first.
 const out=groups.map(g=>({...g,rows:[...g.rows]}));
 for(let i=0;i<out.length;i++){
  const a=out[i];
  for(let j=i+1;j<out.length;){
   const b=out[j],an=a.rows.length,bn=b.rows.length;
   if(Math.hypot(a.x/an-b.x/bn,a.y/an-b.y/bn)<clusterRadius(an,size)+clusterRadius(bn,size)+2){
    a.x+=b.x;a.y+=b.y;a.rows.push(...b.rows);out.splice(j,1);i=-1;break;
   }else j++;
  }
 }
 for(const g of out)g.rows.sort((a,b)=>(a.rank??Infinity)-(b.rank??Infinity));
 return out;
}
