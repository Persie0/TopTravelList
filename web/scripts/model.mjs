import Decimal from 'decimal.js';
export function overall(scores, weights) {
  if (!Object.keys(weights).every(k => Number.isFinite(scores[k]))) return null;
  return Object.entries(weights).reduce((sum,[k,w]) => sum.plus(new Decimal(scores[k]).times(w)),new Decimal(0)).times(10).toNumber();
}
export const value = (row, metric) => metric === 'overall' ? row.overall : (row.scores[metric] ?? row.scores.categories?.[metric] ?? null);
export function ranked(rows, metric='overall') {
  const sorted = [...rows].sort((a,b) => (value(b,metric) ?? -Infinity)-(value(a,metric) ?? -Infinity) || a.name.localeCompare(b.name,'en') || a.id.localeCompare(b.id));
  let previous=null, rank=null;
  return sorted.map((row,i) => {const v=value(row,metric); if(v===null) return {...row,rank:null}; if(v!==previous || i===0) rank=i+1; previous=v; return {...row,rank};});
}
const searchIndex=new WeakMap();
const normalize=s=>s.normalize('NFD').replace(/\p{Diacritic}/gu,'').toLowerCase();
export function eligible(rows,metric,categories){return categories.includes(metric)?rows.filter(r=>Object.hasOwn(r.scores.categories||{},metric)):rows}
export function distribution(rows,metric){const d={cities:0,sights:0,ranked:0,bins:Array(10).fill(0)};for(const r of rows){d[r.kind]++;const v=value(r,metric);if(v!==null){d.ranked++;d.bins[Math.max(0,Math.min(9,Math.floor(v/(metric==='overall'?10:1))))]++}}return d}
export function groupPoints(rows,project,bounds,size,worldWidth){
 const groups=new Map(),center=(bounds.minX+bounds.maxX)/2;
 for(const row of rows){const p=project(row),x=p.x+Math.round((center-p.x)/worldWidth)*worldWidth,y=p.y;if(x<bounds.minX||x>bounds.maxX||y<bounds.minY||y>bounds.maxY)continue;const key=Math.floor(x/size)+':'+Math.floor(y/size);let g=groups.get(key);if(!g){g={x:0,y:0,rows:[]};groups.set(key,g)}g.x+=x;g.y+=y;g.rows.push(row)}
 return [...groups.values()]
}
export function match(rows,{country='',region='',kind='',metric='overall',query='',min=0,unranked=true}={},countries={}) {
  const q=query.normalize('NFD').replace(/\p{Diacritic}/gu,'').toLowerCase().trim();
  const norm=r=>{let s=searchIndex.get(r);if(s===undefined){s=normalize([r.name,countries[r.country]?.name||'',r.country,r.type].join(' '));searchIndex.set(r,s)}return s};
  return rows.filter(r=>{const c=countries[r.country];const v=value(r,metric);return (!country||r.country===country)&&(!region||c?.region===region)&&(!kind||r.kind===kind)&&(!q||norm(r).includes(q))&&(v===null?unranked&&min===0:v>=min);});
}
