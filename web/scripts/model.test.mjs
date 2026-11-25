import {test} from 'node:test';
import assert from 'node:assert/strict';
import {overall,ranked,match} from './model.mjs';
const w={impact:.3,uniqueness:.25,significance:.2,experience:.15,depth:.1};
test('canonical weighted score and incomplete records',()=>{assert.equal(overall({impact:9.7,uniqueness:9.7,significance:9.3,experience:9.4,depth:8.8},w),94.85);assert.equal(overall({impact:null},w),null);assert.equal(overall(Object.fromEntries(Object.keys(w).map(k=>[k,0])),w),0)});
const row=(id,name,overall,nature)=>({id,name,overall,country:'AT',kind:'sights',type:'Park',scores:{categories:{nature}}});
test('competition ties, null and zero',()=>{const rows=[row('a','A',90,0),row('b','B',90,9),row('c','C',80,null),row('d','D',null,8)];assert.deepEqual(ranked(rows).map(r=>r.rank),[1,1,3,null]);assert.deepEqual(ranked(rows,'nature').map(r=>[r.id,r.rank]),[['b',1],['d',2],['a',3],['c',null]])});
test('search and category filters',()=>{const rows=[row('a','Österreich',90,0),row('b','B',80,null)];assert.equal(match(rows,{query:'osterreich'}).length,1);assert.equal(match(rows,{metric:'nature',min:1}).length,0);assert.equal(match(rows,{metric:'nature',unranked:false}).length,1);assert.equal(match(rows,{region:'Europe'},{AT:{region:'Europe'}}).length,2)});
