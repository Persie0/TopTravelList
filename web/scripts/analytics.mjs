import {value} from './model.mjs';

// Counts include unassessed matches; score summaries exclude them.
export function summarize(rows, metric='overall'){
 const scores=[];let cities=0,sights=0,best=null;
 for(const r of rows){
  if(r.kind==='cities')cities++;else if(r.kind==='sights')sights++;
  const v=value(r,metric);
  if(v===null||!Number.isFinite(v))continue;
  scores.push(v);
  if(best===null||v>value(best,metric)||(v===value(best,metric)&&r.id<best.id))best=r;
 }
 scores.sort((a,b)=>a-b);
 const n=scores.length,mid=Math.floor(n/2);
 return {count:rows.length,cities,sights,ranked:n,unassessed:rows.length-n,
  mean:n?scores.reduce((a,b)=>a+b,0)/n:null,
  median:n?(n%2?scores[mid]:(scores[mid-1]+scores[mid])/2):null,
  high:scores.filter(v=>v>=(metric==='overall'?90:9)).length,best};
}
export function groupBy(rows,key,metric='overall'){
 const groups=new Map();
 for(const r of rows){const k=key(r);if(!k)continue;if(!groups.has(k))groups.set(k,[]);groups.get(k).push(r)}
 return [...groups].map(([key,rows])=>({key,rows,...summarize(rows,metric)}));
}
// Exactly one group per matching country, irrespective of screen distance.
export function countryBubbles(rows,countries,metric='overall'){
 return groupBy(rows,r=>r.country,metric).map(g=>{
  const c=countries[g.key],first=g.rows.find(r=>validCenter([r.lat,r.lon]));
  const center=c?.center;
  const valid=validCenter(center);
  return {...g,name:c?.name||g.key,center:valid?center:first?[first.lat,first.lon]:null};
 }).filter(g=>g.center!==null);
}
export function metricProfile(rows,metrics){
 return metrics.map(metric=>({metric,...summarize(rows,metric)}));
}
export function bubbleRadius(count){return Math.min(30,10+Math.sqrt(count)*1.05)}

function validCenter(center){return Array.isArray(center)&&center.length===2&&center.every(Number.isFinite)&&Math.abs(center[0])<=90&&Math.abs(center[1])<=180}

// A directory selection is country navigation, not a hidden destination filter.
// A bubble/chart selection in destination mode preserves the visible match criteria.
export function countryDrilldown(state,code,{markers=false}={}){
 const directory=state.mode==='countries';
 return {...state,country:code,region:'',mode:'places',limit:50,
  ...(directory?{query:'',kind:'',metric:'overall',min:0,unranked:true,top:0,sort:'score'}:{}),
  ...(markers?{display:'rank'}:{})};
}
