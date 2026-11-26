import test from 'node:test';
import assert from 'node:assert/strict';
import {distanceKm,routeDistance,optimizeRoute,suggestRoute,routeLine,navigationUrl} from './routes.mjs';
const p=(id,lat,lon,overall=90)=>({id,lat,lon,overall});
test('haversine distance handles dateline and invalid coordinates',()=>{assert.ok(distanceKm(p('a',0,179),p('b',0,-179))<225);assert.equal(distanceKm(p('a',91,0),p('b',0,0)),Infinity);assert.equal(distanceKm(p('a',0,0),p('b',0,0)),0)});
test('route ordering preserves start and set and never increases distance',()=>{const a=[p('a',0,0),p('b',0,4),p('c',0,1),p('d',0,3)];const b=optimizeRoute(a);assert.equal(b[0],a[0]);assert.deepEqual(b.map(x=>x.id).sort(),a.map(x=>x.id).sort());assert.ok(routeDistance(b)<routeDistance(a))});
test('suggestions honor minimum score, leg and cap',()=>{const a=p('a',0,0),c=[a,p('b',0,.2),p('c',0,.4,60),p('d',0,5)];const r=suggestRoute(a,c,{minScore:80,maxLeg:50,maxStops:4});assert.deepEqual(r.map(x=>x.id),['a','b']);assert.equal(suggestRoute(a,c,{maxStops:1}).length,1)});
test('map line and navigation URL preserve route across dateline',()=>{const r=[p('a',0,179),p('b',0,-179),p('c',1,-178)];assert.deepEqual(routeLine(r),[[0,179],[0,181],[1,182]]);assert.equal(new URL(navigationUrl(r)).searchParams.get('waypoints'),'0,-179');assert.equal(navigationUrl(r.slice(0,1)),null)});
