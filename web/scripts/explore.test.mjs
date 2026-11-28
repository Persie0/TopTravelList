import {test} from 'node:test';
import assert from 'node:assert/strict';
import {imageSearchUrl,withinViewport,explorePreset} from './explore.mjs';
test('image search includes encoded name and country',()=>{
 const url=new URL(imageSearchUrl('Café & Park #1','Côte d’Ivoire'));
 assert.equal(url.origin,'https://www.google.com');
 assert.equal(url.searchParams.get('tbm'),'isch');
 assert.equal(url.searchParams.get('q'),'Café & Park #1, Côte d’Ivoire');
 assert.equal(new URL(imageSearchUrl('Vienna')).searchParams.get('q'),'Vienna');
});
const rows=[{id:'east',lat:10,lon:179},{id:'west',lat:10,lon:-179},{id:'outside',lat:10,lon:0},{id:'south',lat:-40,lon:179},{id:'bad',lat:NaN,lon:179}];
test('viewport handles antimeridian, repeated worlds, and latitude bounds',()=>{
 for(const [west,east] of [[170,190],[170,-170],[-190,-170],[530,550]]) assert.deepEqual(withinViewport(rows,{south:0,north:20,west,east}).map(r=>r.id),['east','west']);
 assert.deepEqual(withinViewport(rows,{south:0,north:20,west:-180,east:180}).map(r=>r.id),['east','west','outside']);
 assert.deepEqual(withinViewport(rows,{south:0,north:20,west:-20,east:20}).map(r=>r.id),['outside']);
});
test('discovery presets use ranked overall scores with exclusive limits and thresholds',()=>{
 assert.deepEqual(explorePreset('90'),{metric:'overall',sort:'score',unranked:false,min:90,top:0});
 assert.deepEqual(explorePreset('top100'),{metric:'overall',sort:'score',unranked:false,min:0,top:100});
 assert.equal(explorePreset('all').top,0);
 assert.equal(explorePreset('all').min,0);
});
