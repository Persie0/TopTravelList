import test from 'node:test';
import assert from 'node:assert/strict';
import {groupBy} from './analytics.mjs';
import {renderStatistics} from '../src/statistical-explorer.js';

const countries={
 AT:{name:'Austria & <test>',code:'AT',region:'Europe',catalogued:true},
 SK:{name:'Slovakia',code:'SK',region:'Europe',catalogued:true}
};
const rows=[
 {id:'a',country:'AT',name:'A',type:'Museum',kind:'sights',overall:90,scores:{impact:9}},
 {id:'b',country:'SK',name:'B',type:'City',kind:'cities',overall:null,scores:{impact:null}},
 {id:'c',country:'AT',name:'C',type:'Museum',kind:'sights',overall:0,scores:{impact:0}}
];
function mockRoot(){
 const nodes=new Map();
 return {innerHTML:'',querySelector(key){
  if(!this.innerHTML.includes(key.slice(1,-1)))return null;
  if(!nodes.has(key))nodes.set(key,key.includes('range')?{
   value:Number(this.innerHTML.match(/data-lab-range[^>]*value="([^"]+)"/)[1]),
   addEventListener(event,callback){this[event]=callback}
  }:{textContent:'',setAttribute(k,v){this[k]=v}});
  return nodes.get(key);
 }};
}
function render(selected,metric='overall'){
 const root=mockRoot();
 renderStatistics(root,{rows:selected,metric,regions:groupBy(selected,r=>countries[r.country].region,metric),
  byCountry:groupBy(selected,r=>r.country,metric),registry:Object.values(countries),
  countryNames:countries,dimensions:['impact']});
 return root;
}
test('all statistical panels render with escaped country names and valid numeric output',()=>{
 const root=render(rows);
 for(const title of ['Score quality mix','Geographic coverage','Regional score spread','Score threshold explorer','Country count vs. mean score','Destination types by score mix','Regional dimension heatmap'])assert.ok(root.innerHTML.includes(title));
 assert.ok(root.innerHTML.includes('Austria &amp; &lt;test&gt;'));
 assert.doesNotMatch(root.innerHTML,/NaN|Infinity|undefined/);
});
test('empty and unassessed datasets do not produce invalid charts or controls',()=>{
 for(const sample of [[],[rows[1]]]){
  const root=render(sample);
  assert.doesNotMatch(root.innerHTML,/NaN|Infinity|undefined/);
  assert.equal(root.querySelector('[data-lab-range]'),null);
  assert.match(root.innerHTML,/No matching assessed scores/);
 }
});
test('threshold interaction includes tied scores and excludes unassessed rows',()=>{
 const root=render(rows);
 const input=root.querySelector('[data-lab-range]');
 input.value=90;input.input();
 assert.match(root.querySelector('[data-lab-result]').textContent,/1 of 2 assessed/);
 input.value=0;input.input();
 assert.match(root.querySelector('[data-lab-result]').textContent,/2 of 2 assessed/);
});
test('category thresholds preserve decimal precision and use the ten-point scale',()=>{
 const root=render(rows,'impact');
 assert.match(root.innerHTML,/max="10" step="0.01"/);
 const input=root.querySelector('[data-lab-range]');
 input.value=9.01;input.input();
 assert.equal(root.querySelector('[data-lab-threshold]').textContent,'9.01');
 assert.match(root.querySelector('[data-lab-result]').textContent,/0 of 2 assessed/);
});
