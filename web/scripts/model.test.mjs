import {test} from 'node:test';
import assert from 'node:assert/strict';
import {ranked,match,scoreBins,wrappedLocations} from './model.mjs';
import {overall} from './overall.mjs';
const w={impact:.3,uniqueness:.25,significance:.2,experience:.15,depth:.1};
test('canonical weighted score and incomplete records',()=>{assert.equal(overall({impact:9.7,uniqueness:9.7,significance:9.3,experience:9.4,depth:8.8},w),94.85);assert.equal(overall({impact:null},w),null);assert.equal(overall(Object.fromEntries(Object.keys(w).map(k=>[k,0])),w),0)});
const row=(id,name,overall,nature)=>({id,name,overall,country:'AT',kind:'sights',type:'Park',scores:{categories:{nature}}});
test('competition ties, null and zero',()=>{const rows=[row('a','A',90,0),row('b','B',90,9),row('c','C',80,null),row('d','D',null,8)];assert.deepEqual(ranked(rows).map(r=>r.rank),[1,1,3,null]);assert.deepEqual(ranked(rows,'nature').map(r=>[r.id,r.rank]),[['b',1],['d',2],['a',3],['c',null]])});
test('search and category filters',()=>{const rows=[row('a','Österreich',90,0),row('b','B',80,null)];assert.equal(match(rows,{query:'osterreich'}).length,1);assert.equal(match(rows,{metric:'nature',min:1}).length,0);assert.equal(match(rows,{metric:'nature',unranked:false}).length,1);assert.equal(match(rows,{region:'Europe'},{AT:{region:'Europe'}}).length,2)});

import {eligible,groupPoints,distribution} from './model.mjs';
test('combined view and explicit null versus missing categories',()=>{const a=row('a','A',91,null),b={...row('b','B',80,8),kind:'cities'},c={...row('c','C',70,3),scores:{categories:{}}};assert.equal(match([a,b,c]).length,3);assert.deepEqual(eligible([a,b,c],'nature',['nature']).map(r=>r.id),['a','b']);assert.equal(distribution([a,b,c],'overall').cities,1);assert.equal(distribution([a,b,c],'overall').bins[9],1)});
test('viewport clustering preserves members and wraps longitude',()=>{const rows=[{id:1,x:5,y:10},{id:2,x:8,y:12},{id:3,x:200,y:10},{id:4,x:252,y:10}];const groups=groupPoints(rows,r=>r,{minX:-20,maxX:40,minY:0,maxY:40},20,256);assert.deepEqual(groups.flatMap(g=>g.rows.map(r=>r.id)).sort(),[1,2,4]);assert.equal(groups.find(g=>g.rows.length===2).rows.length,2)});

test('category histogram labels use the native scale',()=>{assert.equal(scoreBins('nature')[9],'9–10');assert.equal(scoreBins('overall')[9],'90–100')});
test('fit bounds takes the short route across the date line',()=>{const p=wrappedLocations([{lat:-16,lon:179},{lat:-17,lon:-179}]);assert.equal(Math.abs(p[0][1]-p[1][1]),2);assert.deepEqual(wrappedLocations([{lat:48,lon:16}]),[[48,16]])});
test('cached search adapts when a country name is available later',()=>{const a=row('a','A',90,5);assert.equal(match([a],{query:'austria'}).length,0);assert.equal(match([a],{query:'austria'},{AT:{name:'Austria'}}).length,1)});

import {mapsSearchUrl} from './model.mjs';
test('Google Maps searches preserve names, countries and punctuation',()=>{
 for(const [name,country] of [['Vienna','Austria'],['Schönbrunn Palace','Austria'],["St. John's (A&B)",'Antigua and Barbuda'],['東京','Japan']]){
   const u=new URL(mapsSearchUrl(name,country));
   assert.equal(u.origin,'https://www.google.com');
   assert.equal(u.pathname,'/maps/search/');
   assert.equal(u.searchParams.get('api'),'1');
   assert.equal(u.searchParams.get('query'),name+', '+country);
 }
 assert.equal(new URL(mapsSearchUrl('Austria')).searchParams.get('query'),'Austria');
});

test('search accepts map-style name and country queries',()=>{const a={...row('a','Vienna',92,5),kind:'cities'},b=row('b','Vienna Woods',80,8);assert.equal(match([a,b],{query:'Vienna, Austria'},{AT:{name:'Austria'}}).length,2);assert.equal(match([a,b],{query:'Vienna, Germany'},{AT:{name:'Austria'}}).length,0)});

import {splitMapGeometry,coalesceGroups} from './model.mjs';
test('dateline geometry splits into short edges on both sides',()=>{
 const g=splitMapGeometry({type:'Polygon',coordinates:[[[179,10],[-179,10],[-179,12],[179,12],[179,10]]]});
 assert.equal(g.coordinates.length,2);
 for(const [ring] of g.coordinates){assert.deepEqual(ring[0],ring.at(-1));assert.ok(ring.every((p,i)=>!i||Math.abs(p[0]-ring[i-1][0])<=2));assert.ok(ring.every(p=>Math.abs(p[0])<=180))}
});
test('overlapping cluster labels merge without losing ranked members',()=>{
 const groups=coalesceGroups([{x:0,y:0,rows:[{id:'a',rank:3}]},{x:10,y:0,rows:[{id:'b',rank:1}]},{x:100,y:0,rows:[{id:'c',rank:2}]}],40);
 assert.equal(groups.length,2);assert.deepEqual(groups[0].rows.map(r=>r.id),['b','a']);assert.equal(groups[0].x,10);
});

import {parseMinimumScore} from './model.mjs';
test('minimum score supports dot and comma, boundaries and empty input',()=>{
 for(const [raw,expected] of [['90.75',90.75],['90,75',90.75],['0',0],['100',100],['',0],['.5',.5],[',5',.5],['90.',90]])assert.equal(parseMinimumScore(raw),expected);
 for(const raw of ['101','-1','90,7.5','NaN','Infinity','1e2','abc'])assert.equal(parseMinimumScore(raw),null);
 assert.equal(parseMinimumScore('8,7','nature'),8.7);assert.equal(parseMinimumScore('10.01','nature'),null);
});
test('decimal threshold is inclusive for overall and category scores',()=>{
 const rows=[row('below','Below',90.74,8.6),row('equal','Equal',90.75,8.7),row('above','Above',90.76,8.8),row('unknown','Unknown',null,null)];
 assert.deepEqual(match(rows,{min:parseMinimumScore('90,75')}).map(r=>r.id),['equal','above']);
 assert.deepEqual(match(rows,{metric:'nature',min:parseMinimumScore('8.7','nature')}).map(r=>r.id),['equal','above']);
 assert.equal(match(rows,{min:parseMinimumScore('')}).length,4);
});
