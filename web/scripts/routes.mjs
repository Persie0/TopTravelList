const rad=x=>x*Math.PI/180;
export const validPoint=p=>Boolean(p&&Number.isFinite(p.lat)&&Number.isFinite(p.lon)&&Math.abs(p.lat)<=90&&Math.abs(p.lon)<=180);
export function distanceKm(a,b){
 if(!validPoint(a)||!validPoint(b))return Infinity;
 const h=Math.sin(rad(b.lat-a.lat)/2)**2+Math.cos(rad(a.lat))*Math.cos(rad(b.lat))*Math.sin(rad(b.lon-a.lon)/2)**2;
 return 6371*2*Math.asin(Math.sqrt(Math.max(0,Math.min(1,h))));
}
export function routeDistance(stops){return stops.slice(1).reduce((sum,p,i)=>sum+distanceKm(stops[i],p),0)}
export function uniqueStops(stops){const ids=new Set();return stops.filter(p=>validPoint(p)&&!ids.has(p.id)&&ids.add(p.id))}
export function optimizeRoute(stops){
 const original=uniqueStops(stops);if(original.length<3)return original;
 const result=[original[0]],remaining=original.slice(1);
 while(remaining.length){let best=0;for(let i=1;i<remaining.length;i++)if(distanceKm(result.at(-1),remaining[i])<distanceKm(result.at(-1),remaining[best]))best=i;result.push(remaining.splice(best,1)[0])}
 // Open path, fixed first stop. Improve the nearest-neighbor order with bounded 2-opt.
 for(let pass=0;pass<10;pass++){let changed=false;for(let i=1;i<result.length-1;i++)for(let j=i+1;j<result.length;j++){
 const before=distanceKm(result[i-1],result[i])+(j+1<result.length?distanceKm(result[j],result[j+1]):0);
 const after=distanceKm(result[i-1],result[j])+(j+1<result.length?distanceKm(result[i],result[j+1]):0);
 if(after+1e-7<before){result.splice(i,j-i+1,...result.slice(i,j+1).reverse());changed=true}
 }if(!changed)break}
 return routeDistance(result)<=routeDistance(original)?result:original;
}
export function suggestRoute(anchor,candidates,{minScore=80,maxLeg=150,maxStops=8,style='balanced'}={}){
 if(!validPoint(anchor))return [];
 const penalty=style==='compact'?55:style==='highlights'?8:24;
 const stops=[anchor],remaining=uniqueStops(candidates).filter(p=>p.id!==anchor.id&&Number.isFinite(p.overall)&&p.overall>=minScore);
 // Score and proximity compete; restrict every leg to the requested radius.
 while(stops.length<maxStops){const last=stops.at(-1);let best=-1,bestUtility=-Infinity;
 for(let i=0;i<remaining.length;i++){const d=distanceKm(last,remaining[i]);if(d>maxLeg)continue;const utility=remaining[i].overall-penalty*d/Math.max(1,maxLeg);if(utility>bestUtility){best=i;bestUtility=utility}}
 if(best<0)break;stops.push(remaining.splice(best,1)[0]);}
 return stops;
}
export function routeLine(stops){
 const out=[];for(const p of stops){const last=out.at(-1);out.push([p.lat,last?p.lon+360*Math.round((last[1]-p.lon)/360):p.lon])}return out;
}
export function navigationUrl(stops){if(stops.length<2)return null;const pts=stops.map(p=>p.lat+','+p.lon);const q=new URLSearchParams({api:'1',origin:pts[0],destination:pts.at(-1)});if(pts.length>2)q.set('waypoints',pts.slice(1,-1).join('|'));return 'https://www.google.com/maps/dir/?'+q}

export function nearbyStops(stops,candidates,{minScore=80,maxDistance=150,limit=12}={}){
 const selected=new Set(stops.map(p=>p.id));
 if(!stops.length)return [];
 return uniqueStops(candidates).filter(p=>!selected.has(p.id)&&Number.isFinite(p.overall)&&p.overall>=minScore).map(p=>({point:p,distance:Math.min(...stops.map(s=>distanceKm(s,p)))})).filter(r=>r.distance<=maxDistance).sort((a,b)=>(b.point.overall-24*b.distance/Math.max(1,maxDistance))-(a.point.overall-24*a.distance/Math.max(1,maxDistance))||a.distance-b.distance||a.point.id.localeCompare(b.point.id)).slice(0,limit);
}
export function regionalRecommendations(candidates,options={}){
 const ranked=uniqueStops(candidates).filter(p=>Number.isFinite(p.overall)&&p.overall>=(options.minScore??80)).sort((a,b)=>b.overall-a.overall||a.id.localeCompare(b.id));const seeds=[];for(const p of ranked){if(seeds.length>=12)break;if(seeds.every(s=>distanceKm(s,p)>Math.max(15,(options.maxLeg??150)/2)))seeds.push(p)}if(!seeds.length&&ranked.length)seeds.push(ranked[0]);
 const seen=new Set(),routes=[];
 for(const seed of seeds){const route=suggestRoute(seed,candidates,options),key=route.map(p=>p.id).sort().join('|');if(seen.has(key))continue;seen.add(key);routes.push(route)}
 const penalty=options.style==='compact'?55:options.style==='highlights'?8:24;const utility=r=>r.reduce((n,p)=>n+p.overall,0)-penalty*routeDistance(r)/Math.max(1,options.maxLeg??150);
 return routes.sort((a,b)=>utility(b)-utility(a)||routeDistance(a)-routeDistance(b)).slice(0,3);
}
