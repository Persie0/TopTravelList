import {value} from './model.mjs';

export function quantile(sorted,p){if(!sorted.length)return null;const index=(sorted.length-1)*Math.max(0,Math.min(1,p)),lo=Math.floor(index),hi=Math.ceil(index);return sorted[lo]+(sorted[hi]-sorted[lo])*(index-lo)}

export function scoreSample(rows,metric='overall'){return rows.map(r=>value(r,metric)).filter(Number.isFinite).sort((a,b)=>a-b)}

export function scoreSpread(scores){return {n:scores.length,min:quantile(scores,0),q1:quantile(scores,.25),median:quantile(scores,.5),q3:quantile(scores,.75),max:quantile(scores,1),p90:quantile(scores,.9)}}

export function scoreTiers(rows,metric='overall'){const scale=metric==='overall'?100:10,counts=[0,0,0,0,0];for(const r of rows){const v=value(r,metric);if(!Number.isFinite(v))counts[4]++;else if(v>=scale*.9)counts[0]++;else if(v>=scale*.8)counts[1]++;else if(v>=scale*.65)counts[2]++;else counts[3]++}return counts}

export function countAtLeast(scores,threshold){let lo=0,hi=scores.length;while(lo<hi){const mid=(lo+hi)>>>1;if(scores[mid]<threshold)lo=mid+1;else hi=mid}return scores.length-lo}

export function coverageStats(rows,registry){const present=new Set(rows.map(r=>r.country));const groups=new Map();for(const c of registry){if(!groups.has(c.region))groups.set(c.region,{region:c.region,total:0,represented:0,catalogued:0});const g=groups.get(c.region);g.total++;if(present.has(c.code))g.represented++;if(c.catalogued??Boolean(c.cities||c.sights))g.catalogued++}return [...groups.values()].sort((a,b)=>a.region.localeCompare(b.region))}
