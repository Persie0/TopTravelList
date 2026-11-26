import {value} from './model.mjs';
import {quantile} from './statistics.mjs';
export function chartGroups(rows,countries,group,metric){
 const groups=new Map(),scale=metric==='overall'?100:10;
 for(const r of rows){const k=group==='country'?(countries[r.country]?.name||r.country):group==='region'?(countries[r.country]?.region||'Unknown'):group==='kind'?(r.kind==='cities'?'Cities':'Sights'):(r.type||'Other');if(!groups.has(k))groups.set(k,{name:k,count:0,scores:[]});const g=groups.get(k);g.count++;const v=value(r,metric);if(Number.isFinite(v))g.scores.push(v)}
 return [...groups.values()].map(g=>{const s=g.scores.sort((a,b)=>a-b),n=s.length;const mean=n?s.reduce((a,b)=>a+b,0)/n:null;return {name:g.name,count:g.count,assessed:n,mean,median:quantile(s,.5),p90:quantile(s,.9),sd:n?Math.sqrt(s.reduce((a,b)=>a+(b-mean)**2,0)/n):null,high:n?s.filter(v=>v>=scale*.8).length/n*100:null,coverage:n/g.count*100}})
}
