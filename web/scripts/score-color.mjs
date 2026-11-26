// Semantic score colors shared by map, legends and charts.
export const scoreColors=Object.freeze(['#167044','#60952d','#d49b26','#c44b40','#929b9a']);
export function scoreColor(v,metric='overall'){
 if(!Number.isFinite(v))return scoreColors[4];
 const n=metric==='overall'?v:v*10;
 return scoreColors[n>=90?0:n>=80?1:n>=65?2:3];
}
