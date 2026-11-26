import test from 'node:test';
import assert from 'node:assert/strict';
import {chartGroups} from './chart-builder.mjs';
import {scoreColor,scoreColors} from './score-color.mjs';
test('score colors share equivalent 10 and 100 point boundaries',()=>{for(const [v,i] of [[90,0],[80,1],[65,2],[64.9,3],[null,4]]){assert.equal(scoreColor(v),scoreColors[i]);assert.equal(scoreColor(v===null?null:v/10,'impact'),scoreColors[i])}});
test('custom chart measures exclude missing scores and preserve coverage',()=>{const rows=[80,100,null].map(overall=>({country:'AT',kind:'sights',overall,scores:{}}));const [g]=chartGroups(rows,{AT:{name:'Austria'}},'country','overall');assert.equal(g.mean,90);assert.equal(g.median,90);assert.equal(g.sd,10);assert.equal(g.high,100);assert.equal(g.assessed,2);assert.equal(g.count,3);assert.ok(Math.abs(g.coverage-200/3)<1e-9)});
