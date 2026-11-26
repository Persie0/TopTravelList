import {distanceKm,routeDistance,navigationUrl} from './routes.mjs';
export const MAX_STOPS=40;
export const modes=Object.freeze({walk:{label:'Walking',speed:4,factor:1.25},bike:{label:'Cycling',speed:15,factor:1.3},car:{label:'Driving',speed:60,factor:1.35},rail:{label:'Rail / bus',speed:50,factor:1.4},flight:{label:'Flying',speed:650,factor:1.1}});
export const defaults=Object.freeze({name:'My trip',days:5,hours:8,mode:'car',currency:'EUR',people:1,daily:0,perKm:0,extra:0,start:''});
const clamp=(n,min,max,fallback)=>Number.isFinite(Number(n))&&n!==''&&n!==null?Math.max(min,Math.min(max,Number(n))):fallback;
const string=(v,max)=>typeof v==='string'?v.slice(0,max):'';
export function cleanConfig(raw={}){
 raw=raw&&typeof raw==='object'?raw:{};
 return {name:string(raw.name,100).trim()||defaults.name,days:Math.round(clamp(raw.days,1,60,5)),hours:clamp(raw.hours,1,16,8),mode:Object.hasOwn(modes,raw.mode)?raw.mode:'car',currency:['EUR','USD','GBP','CHF','JPY','AUD','CAD','INR','THB','VND'].includes(raw.currency)?raw.currency:'EUR',people:Math.round(clamp(raw.people,1,30,1)),daily:clamp(raw.daily,0,100000,0),perKm:clamp(raw.perKm,0,1000,0),extra:clamp(raw.extra,0,10000000,0),start:typeof raw.start==='string'&&/^\d{4}-\d{2}-\d{2}$/.test(raw.start)&&Number.isFinite(Date.parse(raw.start))?raw.start:''};
}
export function cleanStop(raw={},point){
 raw=raw&&typeof raw==='object'?raw:{};
 return {hours:clamp(raw.hours,.25,72,point?.kind==='cities'?4:2),priority:raw.priority===true,visited:raw.visited===true,notes:string(raw.notes,500),mode:Object.hasOwn(modes,raw.mode)?raw.mode:'',cost:clamp(raw.cost,0,1000000,0)};
}
export function tripEntries(stops,meta={},config={}){
 const c=cleanConfig(config);
 return stops.map((point,i)=>{const m=cleanStop(Object.hasOwn(meta,point.id)?meta[point.id]:{},point),distance=i?distanceKm(stops[i-1],point):0,mode=m.mode||c.mode,estimate=modes[mode],travelHours=i?distance*estimate.factor/estimate.speed+(mode==='flight'?2:0):0;return {point,...m,mode,distance,travelHours,total:m.hours+travelHours,index:i}});
}
// Exact contiguous partition minimizing squared deviation from the average workload.
// Travel belongs to the arrival stop. Empty days are explicit rest / buffer days.
export function daySchedule(entries,days){
 days=Math.max(1,Math.min(60,Math.round(Number(days)||1)));const n=entries.length,k=Math.min(days,n),result=[];
 if(k){const prefix=[0];for(const e of entries)prefix.push(prefix.at(-1)+e.total);const target=prefix[n]/k;
 const dp=Array.from({length:k+1},()=>Array(n+1).fill(Infinity)),prev=Array.from({length:k+1},()=>Array(n+1).fill(-1));dp[0][0]=0;
 for(let d=1;d<=k;d++)for(let i=d;i<=n;i++)for(let j=d-1;j<i;j++){const cost=dp[d-1][j]+(prefix[i]-prefix[j]-target)**2;if(cost<dp[d][i]){dp[d][i]=cost;prev[d][i]=j}}
 let end=n;for(let d=k;d>=1;d--){const start=prev[d][end];result.unshift(entries.slice(start,end));end=start}}
 while(result.length<days)result.push([]);
 return result.map((stops,i)=>({day:i+1,stops,visit:stops.reduce((a,b)=>a+b.hours,0),travel:stops.reduce((a,b)=>a+b.travelHours,0),distance:stops.reduce((a,b)=>a+b.distance,0),total:stops.reduce((a,b)=>a+b.total,0)}));
}
export function tripStats(entries,config){
 const c=cleanConfig(config),rated=entries.filter(e=>Number.isFinite(e.point.overall)),scores=rated.map(e=>e.point.overall).sort((a,b)=>a-b),countries=new Set(entries.map(e=>e.point.country)),distance=entries.reduce((a,b)=>a+b.distance,0),visit=entries.reduce((a,b)=>a+b.hours,0),travel=entries.reduce((a,b)=>a+b.travelHours,0),daily=c.days*c.daily*c.people,transport=distance*c.perKm,admissions=entries.reduce((a,b)=>a+b.cost*c.people,0);
 return {count:entries.length,assessed:scores.length,mean:scores.length?scores.reduce((a,b)=>a+b,0)/scores.length:null,median:scores.length?(scores[Math.floor((scores.length-1)/2)]+scores[Math.ceil((scores.length-1)/2)])/2:null,high:scores.filter(s=>s>=80).length,exceptional:scores.filter(s=>s>=90).length,visited:entries.filter(e=>e.visited).length,priority:entries.filter(e=>e.priority).length,priorityVisited:entries.filter(e=>e.priority&&e.visited).length,countries:countries.size,cities:entries.filter(e=>e.point.kind==='cities').length,sights:entries.filter(e=>e.point.kind==='sights').length,distance,visit,travel,daily,transport,admissions,total:daily+transport+admissions+c.extra,capacity:c.days*c.hours};
}
export function sanitizeTrip(raw,byId){
 if(!raw||typeof raw!=='object'||!Array.isArray(raw.ids))return null;
 const ids=[...new Set(raw.ids.filter(id=>typeof id==='string'&&byId.has(id)))].slice(0,MAX_STOPS),meta=Object.create(null);
 for(const id of ids)meta[id]=cleanStop(raw.meta&&Object.hasOwn(raw.meta,id)?raw.meta[id]:{},byId.get(id));
 return {version:2,ids,meta,config:cleanConfig(raw.config)};
}
export function directionsSegments(stops,maxStops=5){
 const result=[];for(let i=0;i<stops.length-1;i+=maxStops-1)result.push({from:i+1,to:Math.min(stops.length,i+maxStops),url:navigationUrl(stops.slice(i,i+maxStops))});return result;
}
const xml=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&apos;'}[c]));
export function gpxExport(stops,name){
 return '<?xml version="1.0" encoding="UTF-8"?>\n<gpx version="1.1" creator="TopTravelList" xmlns="http://www.topografix.com/GPX/1/1"><rte><name>'+xml(name)+'</name>'+stops.map(p=>'<rtept lat="'+p.lat+'" lon="'+p.lon+'"><name>'+xml(p.name)+'</name></rtept>').join('')+'</rte></gpx>';
}
export function routeComparison(stops){const rated=stops.filter(p=>Number.isFinite(p.overall));return {count:stops.length,mean:rated.length?rated.reduce((a,b)=>a+b.overall,0)/rated.length:null,high:rated.filter(p=>p.overall>=80).length,km:routeDistance(stops),countries:new Set(stops.map(p=>p.country)).size}}
