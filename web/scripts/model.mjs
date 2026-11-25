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
export function match(rows,{country='',region='',kind='',metric='overall',query='',min=0,unranked=true}={},countries={}) {
  const q=query.normalize('NFD').replace(/\p{Diacritic}/gu,'').toLowerCase().trim();
  const norm=s=>s.normalize('NFD').replace(/\p{Diacritic}/gu,'').toLowerCase();
  return rows.filter(r=>{const c=countries[r.country];const v=value(r,metric);return (!country||r.country===country)&&(!region||c?.region===region)&&(!kind||r.kind===kind)&&(!q||norm([r.name,c?.name||'',r.country,r.type].join(' ')).includes(q))&&(v===null?unranked&&min===0:v>=min);});
}
