import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import {feature} from 'topojson-client';
import world from 'world-atlas/countries-110m.json';
import {ranked,match,value} from '../scripts/model.mjs';
import './style.css';
const repo='https://github.com/Persie0/TopTravelList/blob/main/';
const $=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const title=s=>s.charAt(0).toUpperCase()+s.slice(1);
const format=(v,metric)=>v===null?'—':v.toFixed(metric==='overall'?2:1);
const color=(v,metric)=>v===null?'#9aa6a2':(metric==='overall'?v:v*10)>=90?'#b55a26':(metric==='overall'?v:v*10)>=80?'#d69b3d':(metric==='overall'?v:v*10)>=65?'#197b70':'#648c99';
const initial=new URLSearchParams(location.search);
const state={country:initial.get('country')||'',region:initial.get('region')||'',kind:initial.get('kind')||'sights',metric:initial.get('metric')||'overall',query:initial.get('q')||'',min:Number(initial.get('min'))||0,unranked:initial.get('unranked')!=='0',view:initial.get('view')||'map',mode:initial.get('mode')||'places',sort:'score',limit:50,top:0};
let data,map,layer,polygons,centers,selected=null,visible=[],markers=new Map();
const flag=code=>code.replace(/[A-Z]/g,c=>String.fromCodePoint(127397+c.charCodeAt(0)));
function opts(items){return items.map(([v,t])=>'<option value="'+esc(v)+'">'+esc(t)+'</option>').join('')}
function sync(){const p=new URLSearchParams();for(const [k,v] of Object.entries({country:state.country,region:state.region,kind:state.kind,metric:state.metric,q:state.query,min:state.min,unranked:state.unranked?'1':'0',view:state.view,mode:state.mode}))if(v!==''&&v!==0)p.set(k,v);history.replaceState(null,'','?'+p);}
function chooseCountry(code){state.country=code;state.region='';state.query='';state.mode='places';state.limit=50;selected=null;render(true)}
function scoreText(r){return format(value(r,state.metric),state.metric)}
function mount(){
 const n=Object.values(data.countries).filter(c=>c.cities&&c.sights).length;
 $('app').innerHTML='<header><a class="brand" href="./"><span class="brandmark">◎</span><span>TopTravelList<small>THE TRAVEL ATLAS</small></span></a><nav><a href="'+repo+'rules.md" target="_blank" rel="noopener">Methodology ↗</a><a href="https://github.com/Persie0/TopTravelList" target="_blank" rel="noopener">GitHub ↗</a></nav></header><main><section class="intro"><div><div class="eyebrow">A WORLDWIDE TRAVEL INDEX</div><h1>Find your next <em>extraordinary</em> place.</h1><p>Explore destinations geographically or compare their worldwide editorial scores.</p></div><div class="stats"><div><b>'+Object.keys(data.countries).length+'</b><span>Countries in index</span></div><div><b>'+n+'</b><span>Catalogued countries</span></div><div><b>'+data.rows.length.toLocaleString()+'</b><span>Destinations</span></div></div></section><section class="workspace"><div class="toolbar"><div class="tabs" aria-label="Browse mode"><button id="places">Destinations</button><button id="countries">Countries</button></div><div class="tabs" aria-label="View"><button id="mapView">Map + list</button><button id="listView">List only</button></div></div><div class="filters"><label class="search">Search<input id="query" type="search" placeholder="Search places or countries…"></label><label>Region<select id="region">'+opts([['','All regions'],...Array.from(new Set(Object.values(data.countries).map(c=>c.region))).sort().map(x=>[x,x])])+'</select></label><label>Country<select id="country"></select></label><div id="placeFilters" class="placefilters"><label>Type<select id="kind">'+opts([['sights','Sights'],['cities','Cities'],['','All destinations']])+'</select></label><label>Rank by<select id="metric">'+opts([['overall','Overall'],...data.categories.map(x=>[x,title(x)]),...Object.keys(data.dimensions).map(x=>[x,title(x)+' (dimension)'])])+'</select></label><label>Minimum score<input id="min" type="number" min="0" max="100" step="1"></label><label>Map points<select id="top">'+opts([['0','All matches'],['25','Top 25'],['100','Top 100'],['250','Top 250']])+'</select></label><label class="check"><input id="unranked" type="checkbox"> Include unassessed</label></div><button id="reset" class="quiet">Reset filters</button></div><div class="content" id="content"><section class="mapframe" id="mapframe"><div id="map" aria-label="Interactive destination map"></div><div class="maptools"><button id="fit">Fit results</button><div id="legend"></div></div><div id="mapnote" class="mapnote"></div></section><section class="results" aria-label="Results"><div class="resultshead"><div><div class="eyebrow" id="scope"></div><h2 id="resultTitle">Explore</h2><p id="count" aria-live="polite"></p></div><label>Sort<select id="sort">'+opts([['score','Highest score'],['name','Name A–Z']])+'</select></label></div><div id="rows" class="rows"></div><button id="more" class="more">Show more</button></section></div><aside id="detail" hidden></aside></section><footer>Worldwide scoring v'+data.version+' · Provisional editorial ratings, not objective facts. Map locations are representative, not necessarily entrances. Ratings do not guarantee access or safety. <a href="'+repo+'README.md" target="_blank" rel="noopener">Data & advisories ↗</a></footer></main>';
 map=L.map('map',{preferCanvas:true,worldCopyJump:true,minZoom:2,maxZoom:19}).setView([22,16],2);
 L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(map);
 layer=L.layerGroup().addTo(map);centers=L.layerGroup().addTo(map);
 const byNumber=new Map(Object.values(data.countries).filter(c=>c.numeric).map(c=>[String(Number(c.numeric)),c.code]));
 polygons=L.geoJSON(feature(world,world.objects.countries),{style:f=>({weight:0.7,color:'#6d8c85',fillColor:'#e5e7dc',fillOpacity:.2}),onEachFeature:(f,l)=>{let code=byNumber.get(String(Number(f.id)));if(!code&&f.properties?.name==='Kosovo')code='XK';if(code){l.countryCode=code;l.on('click',()=>chooseCountry(code));l.bindTooltip(esc(data.countries[code].name));}}}).addTo(map);
 for(const id of ['country','region','kind','metric','sort','top'])$(id).addEventListener('change',e=>{state[id]=id==='top'?Number(e.target.value):e.target.value;if(id==='country'){state.region='';state.mode='places'}if(id==='region')state.country='';if(id==='metric')state.min=0;state.limit=50;selected=null;render(['country','region'].includes(id))});
 $('query').addEventListener('input',e=>{state.query=e.target.value;state.limit=50;selected=null;render(false)});
 $('min').addEventListener('input',e=>{state.min=Math.max(0,Math.min(state.metric==='overall'?100:10,Number(e.target.value)||0));state.limit=50;render(false)});
 $('unranked').addEventListener('change',e=>{state.unranked=e.target.checked;state.limit=50;render(false)});
 $('places').onclick=()=>{state.mode='places';state.limit=50;render(true)};
 $('countries').onclick=()=>{state.mode='countries';state.country='';state.query='';state.limit=50;selected=null;render(true)};
 $('mapView').onclick=()=>{state.view='map';render(false);requestAnimationFrame(()=>{map.invalidateSize();fit()})};
 $('listView').onclick=()=>{state.view='list';render(false)};
 $('fit').onclick=fit;
 $('more').onclick=()=>{state.limit+=50;renderList()};
 $('reset').onclick=()=>{Object.assign(state,{country:'',region:'',kind:'sights',metric:'overall',query:'',min:0,unranked:true,mode:'places',sort:'score',top:0,limit:50});selected=null;render(true)};
 if(!['overall',...data.categories,...Object.keys(data.dimensions)].includes(state.metric))state.metric='overall';
 if(!['cities','sights',''].includes(state.kind))state.kind='sights';
 if(!data.countries[state.country])state.country='';
 if(!['map','list'].includes(state.view))state.view='map';
 if(!['places','countries'].includes(state.mode))state.mode='places';
 state.min=Math.max(0,Math.min(state.metric==='overall'?100:10,state.min));
 render(true);
}
function countryMatches(){const q=state.query.toLowerCase().trim();return Object.values(data.countries).filter(c=>(!state.region||c.region===state.region)&&(!q||(c.name+' '+c.code).toLowerCase().includes(q))).sort((a,b)=>a.name.localeCompare(b.name,'en'))}
function render(shouldFit){
 const countries=Object.values(data.countries).sort((a,b)=>a.name.localeCompare(b.name,'en'));
 $('country').innerHTML=opts([['','All countries'],...countries.map(c=>[c.code,c.name+(c.cities||c.sights?'':' · not catalogued')])]);
 for(const id of ['country','region','kind','metric','query','sort','top','min'])$(id).value=state[id];
 $('min').max=state.metric==='overall'?100:10;$('min').step=state.metric==='overall'?1:.1;$('unranked').checked=state.unranked;
 $('placeFilters').hidden=state.mode==='countries';$('country').disabled=state.mode==='countries';$('sort').disabled=state.mode==='countries';
 for(const [id,on] of [['places',state.mode==='places'],['countries',state.mode==='countries'],['mapView',state.view==='map'],['listView',state.view==='list']]){$(id).classList.toggle('active',on);$(id).setAttribute('aria-pressed',String(on))}
 $('mapframe').hidden=state.view==='list';$('content').classList.toggle('listmode',state.view==='list');
 // Rank inside the selected geographic and kind scope, before search or minimum filters.
 const scope=ranked(match(data.rows,{country:state.country,region:state.region,kind:state.kind},data.countries),state.metric);
 visible=match(scope,state,data.countries);if(state.sort==='name')visible.sort((a,b)=>a.name.localeCompare(b.name,'en'));
 renderList();renderMap();renderDetail();sync();
 if(shouldFit&&state.view==='map')requestAnimationFrame(()=>{map.invalidateSize();fit()});
}
function renderList(){
 const c=data.countries[state.country];
 $('scope').textContent=state.mode==='countries'?'COUNTRY DIRECTORY':c?c.name.toUpperCase():state.region?state.region.toUpperCase():'WORLDWIDE';
 $('resultTitle').textContent=state.mode==='countries'?'Explore countries':state.kind==='cities'?'Cities & towns':state.kind==='sights'?'Sights & attractions':'All destinations';
 const items=state.mode==='countries'?countryMatches():visible;
 $('count').textContent=items.length.toLocaleString()+' matches'+(state.mode==='places'?' · '+items.filter(r=>r.rank!==null).length.toLocaleString()+' ranked':'');
 $('rows').innerHTML=items.slice(0,state.limit).map(r=>state.mode==='countries'?'<button class="result countryrow" data-country="'+r.code+'"><span class="flag">'+flag(r.code)+'</span><span class="name"><strong>'+esc(r.name)+'</strong><small>'+esc(r.region)+' · '+(r.cities+r.sights?'Catalogued':'Not yet catalogued')+'</small></span><span class="score">'+r.cities+' cities<br>'+r.sights+' sights</span></button>':'<button class="result '+(selected?.id===r.id?'selected':'')+'" data-id="'+esc(r.id)+'"><span class="rank">'+(r.rank===null?'—':'#'+r.rank)+'</span><span class="name"><strong>'+esc(r.name)+'</strong><small>'+flag(r.country)+' '+esc(data.countries[r.country].name)+' · '+esc(r.type)+'</small></span><span class="score" style="--score:'+color(value(r,state.metric),state.metric)+'">'+scoreText(r)+'<small>'+(r.rank===null?'Unassessed':state.metric==='overall'?'/ 100':'/ 10')+'</small></span></button>').join('')||'<div class="empty"><h3>No matching destinations</h3><p>'+(c&&c.cities+c.sights===0?'This country is in the registry but has not been catalogued yet.':'Try another search or clear your filters.')+'</p></div>';
 $('rows').querySelectorAll('[data-country]').forEach(b=>b.onclick=()=>chooseCountry(b.dataset.country));
 $('rows').querySelectorAll('[data-id]').forEach(b=>b.onclick=()=>select(items.find(r=>r.id===b.dataset.id),true));
 $('more').hidden=items.length<=state.limit;
}
function renderMap(){
 layer.clearLayers();centers.clearLayers();markers.clear();
 const countrySet=new Set(countryMatches().map(c=>c.code));
 polygons.setStyle(f=>{const code=byFeature(f),c=data.countries[code];const active=state.mode==='countries'?countrySet.has(code):state.country===code;return {weight:active?1.6:.6,color:active?'#146c63':'#879990',fillColor:c?.cities+c?.sights?'#2d9684':'#b8c4b7',fillOpacity:state.mode==='countries'?(active?(c?.cities+c?.sights?.valueOf()? .46:.15):.03):active?.27:.035}});
 if(state.mode==='countries'){
  for(const c of countryMatches())if(c.center){const m=L.circleMarker(c.center,{radius:5,color:'#fff',weight:1.4,fillColor:c.cities+c.sights?'#18776b':'#9aa6a2',fillOpacity:1}).bindTooltip(esc(c.name)+' · '+(c.cities+c.sights)+' places').on('click',()=>chooseCountry(c.code));centers.addLayer(m)}
  $('legend').textContent='Green: catalogued · Gray: awaiting data';$('mapnote').textContent='Select a country to explore its destinations.';return;
 }
 let points=[...visible].sort((a,b)=>(a.rank??Infinity)-(b.rank??Infinity));if(state.top)points=points.filter(r=>r.rank!==null).slice(0,state.top);
 for(const r of points){const v=value(r,state.metric);const normalized=v===null?0:state.metric==='overall'?v:v*10;const m=L.circleMarker([r.lat,r.lon],{radius:v===null?4:4+normalized/25,weight:1,color:'#fff',fillColor:color(v,state.metric),fillOpacity:.87});m.bindTooltip(esc(r.name)+' · '+scoreText(r));m.on('click',()=>select(r,false));layer.addLayer(m);markers.set(r.id,m)}
 $('legend').innerHTML='<span class="dot high"></span>90+ <span class="dot good"></span>80–89 <span class="dot mid"></span>65–79 <span class="dot low"></span>Below 65 <span class="dot none"></span>Unassessed';if(state.metric!=='overall')$('legend').innerHTML=$('legend').innerHTML.replace('90+','9+').replace('80–89','8–8.9').replace('65–79','6.5–7.9').replace('Below 65','Below 6.5');
 $('mapnote').textContent=points.length.toLocaleString()+' map points · Color and size indicate '+(state.metric==='overall'?'overall score':state.metric+' score')+'.';
}
function byFeature(f){if(!f)return '';if(f.properties?.name==='Kosovo')return 'XK';return Object.values(data.countries).find(c=>c.numeric&&Number(c.numeric)===Number(f.id))?.code||''}
function fit(){if(state.view==='list')return;if(state.mode==='countries'){const pts=countryMatches().map(c=>c.center).filter(Boolean);if(state.region&&pts.length)map.fitBounds(pts,{padding:[35,35],maxZoom:5});else map.setView([22,16],2);return}const pts=[...markers.values()].map(m=>m.getLatLng());if(pts.length)map.fitBounds(pts,{padding:[32,32],maxZoom:12});else if(data.countries[state.country]?.center)map.setView(data.countries[state.country].center,5);else map.setView([22,16],2)}
function select(r,focusMap){if(!r)return;selected=r;renderList();renderDetail();if(state.view==='map'&&focusMap){map.setView([r.lat,r.lon],Math.max(map.getZoom(),8));markers.get(r.id)?.openTooltip()}$('detail').scrollIntoView({block:'nearest',behavior:'smooth'})}
function renderDetail(){const d=$('detail');d.hidden=!selected;if(!selected)return;const r=selected;d.innerHTML='<div class="detailhead"><div><div class="eyebrow">'+esc(data.countries[r.country].name)+' · '+esc(r.type)+'</div><h2>'+esc(r.name)+'</h2></div><button id="closeDetail" aria-label="Close destination details">×</button></div><p class="detailScore">'+format(r.overall,'overall')+' <small>/ 100 overall</small> · '+(r.rank===null?'Unassessed for selected metric':'#'+r.rank+' in current ranking scope')+'</p><div class="breakdown">'+Object.entries(data.dimensions).map(([k,w])=>'<div><span>'+title(k)+' · '+Math.round(w*100)+'%</span><b>'+format(r.scores[k]??null,k)+'</b><progress max="10" value="'+(r.scores[k]??0)+'"></progress></div>').join('')+'</div><h3>Category ratings</h3><div class="chips">'+Object.entries(r.scores.categories||{}).sort((a,b)=>(b[1]??-1)-(a[1]??-1)).map(([k,v])=>'<span>'+title(k)+' <b>'+format(v,k)+'</b></span>').join('')+'</div><p class="detailLinks"><a href="https://www.google.com/maps/search/?api=1&query='+r.lat+','+r.lon+'" target="_blank" rel="noopener">Open in Google Maps ↗</a><a href="'+repo+esc(r.source)+'" target="_blank" rel="noopener">Source YAML ↗</a><a href="'+repo+'countries/'+r.country+'/'+r.kind+'.md" target="_blank" rel="noopener">Country ranking ↗</a></p><p class="muted">Representative coordinates: '+r.lat+', '+r.lon+'</p>';$('closeDetail').onclick=()=>{selected=null;renderDetail();renderList()}}
fetch(import.meta.env.BASE_URL+'atlas.json').then(r=>{if(!r.ok)throw Error('HTTP '+r.status);return r.json()}).then(d=>{data=d;mount()}).catch(e=>{$('app').innerHTML='<main class="empty"><h1>Atlas unavailable</h1><p>Could not load the destination index. Reload to try again.</p><button id="retry">Reload</button></main>';$('retry').onclick=()=>location.reload();console.error(e)});
