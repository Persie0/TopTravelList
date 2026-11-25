import test from 'node:test';
import assert from 'node:assert/strict';
import {summarize,groupBy,countryBubbles,metricProfile,bubbleRadius} from './analytics.mjs';
import {match} from './model.mjs';

const rows=[
 {id:'a',name:'A',country:'AT',kind:'cities',type:'City',lat:48,lon:16,overall:90,scores:{impact:9,categories:{nature:4}}},
 {id:'b',name:'B',country:'AT',kind:'sights',type:'Sight',lat:48,lon:16,overall:70,scores:{impact:7,categories:{nature:null}}},
 {id:'c',name:'C',country:'SK',kind:'sights',type:'Sight',lat:48,lon:16,overall:null,scores:{impact:null}},
 {id:'d',name:'D',country:'SK',kind:'cities',type:'City',lat:48,lon:16,overall:80,scores:{impact:8,categories:{nature:6}}}
];
const countries={AT:{name:'Austria',center:[47,14],region:'Europe'},SK:{name:'Slovakia',center:[49,19],region:'Europe'}};

test('one group per country even with identical destination coordinates',()=>{
 const groups=countryBubbles(rows,countries);
 assert.equal(groups.length,2);
 assert.deepEqual(groups.map(g=>[g.key,g.count,g.mean,g.center]),[['AT',2,80,[47,14]],['SK',2,80,[49,19]]]);
 assert.equal(groups.reduce((a,g)=>a+g.count,0),rows.length);
 assert.deepEqual(countryBubbles(rows,{}).map(g=>g.center),[[48,16],[48,16]]);
});
test('country groups reflect filters, including score and type',()=>{
 const filtered=match(rows,{kind:'sights',min:60},countries);
 const groups=countryBubbles(filtered,countries);
 assert.deepEqual(groups.map(g=>[g.key,g.count]),[['AT',1]]);
 assert.deepEqual(countryBubbles([],countries),[]);
});
test('mean and median exclude null but preserve zero; counts include null',()=>{
 const zero={...rows[0],id:'zero',overall:0};
 const s=summarize([...rows,zero]);
 assert.equal(s.count,5);assert.equal(s.ranked,4);assert.equal(s.unassessed,1);
 assert.equal(s.mean,60);assert.equal(s.median,75);assert.equal(s.high,1);
 assert.equal(s.best.id,'a');
 assert.equal(summarize([rows[2]]).mean,null);assert.equal(summarize([]).median,null);
});
test('category profile distinguishes assessed from missing and unassessed',()=>{
 const [impact,nature]=metricProfile(rows,['impact','nature']);
 assert.equal(impact.mean,8);assert.equal(impact.ranked,3);
 assert.equal(nature.mean,5);assert.equal(nature.ranked,2);
 assert.equal(summarize(rows,'impact').high,1);
});
test('grouped regional counts and bubble size are bounded',()=>{
 assert.equal(groupBy(rows,r=>countries[r.country].region)[0].count,4);
 assert.ok(bubbleRadius(10)>bubbleRadius(1));
 assert.equal(bubbleRadius(100000),30);
});
