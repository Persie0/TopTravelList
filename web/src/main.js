import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import {feature} from 'topojson-client';
import world from 'world-atlas/countries-110m.json';
import {ranked,match,value,eligible,groupPoints,distribution,normalize,wrappedLocations,scoreBins,mapsSearchUrl,splitMapGeometry,clusterRadius,coalesceGroups} from '../scripts/model.mjs';
import './style.css';
const repo='https://github.com/Persie0/TopTravelList/blob/main/';
const $=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const title=s=>s.charAt(0).toUpperCase()+s.slice(1);
const format=(v,metric)=>v===null?'—':v.toFixed(metric==='overall'?2:1);
const color=(v,metric)=>v===null?'#9aa6a2':(metric==='overall'?v:v*10)>=90?'#b55a26':(metric==='overall'?v:v*10)>=80?'#d69b3d':(metric==='overall'?v:v*10)>=65?'#197b70':'#648c99';
const initial=new URLSearchParams(location.search);
const state={country:initial.get('country')||'',region:initial.get('region')||'',kind:initial.get('kind')==='all'?'':initial.get('kind')||'',metric:initial.get('metric')||'overall',query:initial.get('q')||'',min:Number(initial.get('min'))||0,unranked:initial.get('unranked')!=='0',view:initial.get('view')||'map',mode:initial.get('mode')||'places',sort:initial.get('sort')==='name'?'name':'score',limit:50,top:[25,100,250].includes(Number(initial.get('top')))?Number(initial.get('top')):0,display:initial.get('display')==='density'?'density':'rank',basemap:initial.get('basemap')==='outline'?'outline':'street'};
let data,map,layer,polygons,centers,tiles,selectionLayer,selected=null,visible=[],markers=new Map(),points=[],scopeKey='',scope=[],countries=[],byNumber,searchTimer,mapFrame=0,polygonKey='',page=0;
const flag=code=>code.replace(/[A-Z]/g,c=>String.fromCodePoint(127397+c.charCodeAt(0)));
function opts(items){return items.map(([v,t])=>'<option value="'+esc(v)+'">'+esc(t)+'</option>').join('')}
function sync(){const p=new URLSearchParams();for(const [k,v] of Object.entries({country:state.country,region:state.region,kind:state.kind||'all',sort:state.sort,top:state.top,display:state.display,basemap:state.basemap,metric:state.metric,q:state.query,min:state.min,unranked:state.unranked?'1':'0',view:state.view,mode:state.mode}))if(v!==''&&v!==0)p.set(k,v);history.replaceState(null,'','?'+p);}
function chooseCountry(code){state.country=code;state.region='';state.query='';state.mode='places';state.limit=50;selected=null;render(true)}
function mapLink(r){const name=r.name,country=r.kind?data.countries[r.country].name:'';return '<a class="rowmap" href="'+esc(mapsSearchUrl(name,country))+'" target="_blank" rel="noopener noreferrer" aria-label="Search Google Maps for '+esc(country?name+', '+country:name)+'">Maps ↗</a>'}
function scoreText(r){return format(value(r,state.metric),state.metric)}
function mount(){
 const n=Object.values(data.countries).filter(c=>c.cities||c.sights).length;
 $('app').innerHTML=`
<main id="main"><h1 class="sr">TopTravelList travel atlas</h1><section class="workspace" aria-label="Travel atlas explorer">
<div class="toolbar"><div class="tabs" role="group" aria-label="Browse mode"><button id="places">Destinations</button><button id="countries">Countries</button></div><div class="tabs" role="group" aria-label="View"><button id="mapView">Map + list</button><button id="listView">List only</button></div></div>
<div class="filters"><label class="search">Search destinations or countries<input id="query" type="search" placeholder="e.g. Vienna, Austria" autocomplete="off"></label><label>Region<select id="region">${opts([['','Any region'],...Array.from(new Set(Object.values(data.countries).map(c=>c.region))).sort().map(x=>[x,x])])}</select></label><label id="countryField">Country<select id="country"></select></label><div id="placeFilters" class="placefilters"><label>Type<select id="kind">${opts([['','Both types'],['sights','Sights only'],['cities','Cities only']])}</select></label><label>Rank by<select id="metric">${opts([['overall','Overall'],...data.categories.map(x=>[x,title(x)]),...Object.keys(data.dimensions).map(x=>[x,title(x)+' (dimension)'])])}</select></label></div><button id="reset" class="quiet">Reset filters</button></div>
<details id="advanced" class="advanced"><summary>More filters <span id="advancedCount"></span></summary><div class="advancedbody"><label>Minimum score <span id="scoreScale"></span><input id="min" type="number" min="0" max="100" step="1" inputmode="decimal"></label><label id="topField">Map destinations<select id="top">${opts([['0','All matches'],['25','Top 25'],['100','Top 100'],['250','Top 250']])}</select></label><label class="check"><input id="unranked" type="checkbox"> Include unassessed</label></div></details>
<div class="content" id="content"><section class="mapframe" id="mapframe" aria-label="Destination map"><div class="maptools"><div class="mapactions"><button id="fit">Fit results</button><label><span class="sr">Map visualization</span><select id="display"><option value="rank">Ranked markers</option><option value="density">Density bubbles</option></select></label><label><span class="sr">Basemap</span><select id="basemap"><option value="street">Street map</option><option value="outline">Atlas outline</option></select></label></div><div id="legend"></div></div><div id="map" role="region" aria-label="Interactive destination map. Use the results list for keyboard access."></div><div id="mapnote" class="mapnote"></div><div id="tileError" class="mapwarning" role="status" hidden>Street map unavailable. <button id="outlineFallback">Use atlas outline</button></div></section>
<section class="results" aria-label="Results"><div class="resultshead"><div><h2 id="resultTitle">Explore</h2><div class="scope" id="scope"></div><p id="count" aria-live="polite" aria-atomic="true"></p></div><label id="sortField">Sort<select id="sort">${opts([['score','Top score'],['name','Name A–Z']])}</select></label></div><div id="insights" class="insights"></div><div id="rows" class="rows"></div><div id="pager" class="pager"><button id="prev" class="more">Previous</button><span id="pageStatus" aria-live="polite"></span><button id="more" class="more">Next</button></div><aside id="detail" aria-labelledby="detailTitle" hidden></aside></section></div>
<details class="help"><summary>How to explore and interpret rankings</summary><p>Choose a country on the map or in the directory. Search by name and country, change the score category, or zoom into a cluster. Rankings compare the selected region and destination type before search or minimum-score filtering. Overall scores are out of 100; categories and dimensions are out of 10. Unassessed scores are not zero. The results list is a keyboard-accessible alternative to the map. Press / to search or Escape to close details.</p></details></section>
<footer><div class="footline"><strong>TopTravelList</strong><div class="footstats"><span><b>${Object.keys(data.countries).length}</b> countries in index</span><span><b>${n}</b> catalogued countries</span><span><b>${data.rows.length.toLocaleString()}</b> destinations</span></div><nav aria-label="Project links"><a href="${repo}rules.md" target="_blank" rel="noopener">Methodology</a><a href="https://github.com/Persie0/TopTravelList" target="_blank" rel="noopener">GitHub</a><a href="${repo}README.md" target="_blank" rel="noopener">Data &amp; advisories</a></nav></div><p>Worldwide scoring v${data.version} · Editorial ratings, not objective facts. Map locations are representative, not necessarily entrances. Ratings do not guarantee access or safety.</p></footer></main>`;
 map=L.map('map',{preferCanvas:true,worldCopyJump:true,minZoom:0,maxZoom:19,zoomSnap:.25,maxBounds:[[-85,-540],[85,540]],maxBoundsViscosity:.4}).setView([22,16],2);
 tiles=L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19,keepBuffer:1,updateWhenIdle:true,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'});
 layer=L.layerGroup().addTo(map);centers=L.layerGroup().addTo(map);selectionLayer=L.layerGroup().addTo(map);
 countries=Object.values(data.countries).sort((a,b)=>a.name.localeCompare(b.name,'en'));$('country').innerHTML=opts([['','Any country'],...countries.map(c=>[c.code,c.name+(c.cities||c.sights?'':' · not catalogued')])]);
 byNumber=new Map(Object.values(data.countries).filter(c=>c.numeric).map(c=>[String(Number(c.numeric)),c.code]));
 const geography=feature(world,world.objects.countries);for(const f of geography.features)f.geometry=splitMapGeometry(f.geometry);
 polygons=L.geoJSON(geography,{style:f=>({weight:0.7,color:'#6d8c85',fillColor:'#e5e7dc',fillOpacity:.2}),onEachFeature:(f,l)=>{let code=byNumber.get(String(Number(f.id)));if(!code&&f.properties?.name==='Kosovo')code='XK';if(code){l.countryCode=code;l.on('click',()=>chooseCountry(code));l.bindTooltip(esc(data.countries[code].name));}}}).addTo(map);
 map.on('moveend',scheduleMap);if(typeof ResizeObserver!=='undefined')new ResizeObserver(()=>{if(state.view==='map')map.invalidateSize({pan:false,debounceMoveend:true})}).observe($('map'));for(const id of ['display','basemap'])$(id).onchange=e=>{state[id]=e.target.value;renderMap();sync()};
 for(const id of ['country','region','kind','metric','sort','top'])$(id).addEventListener('change',e=>{state[id]=id==='top'?Number(e.target.value):e.target.value;if(id==='country'){state.region='';state.mode='places'}if(id==='region')state.country='';if(id==='metric')state.min=0;state.limit=50;selected=null;render(['country','region'].includes(id))});
 $('query').addEventListener('input',e=>{state.query=e.target.value;state.limit=50;selected=null;clearTimeout(searchTimer);searchTimer=setTimeout(()=>render(true),140)});
 $('min').addEventListener('change',e=>{state.min=Math.max(0,Math.min(state.metric==='overall'?100:10,Number(e.target.value)||0));state.limit=50;render(false)});
 $('unranked').addEventListener('change',e=>{state.unranked=e.target.checked;state.limit=50;render(false)});
 $('places').onclick=()=>{state.mode='places';state.limit=50;render(true)};
 $('countries').onclick=()=>{state.mode='countries';state.country='';state.query='';state.limit=50;selected=null;render(true)};
 $('mapView').onclick=()=>{if(state.view==='map')return;state.view='map';const p=page;render(false);page=p;renderList();requestAnimationFrame(()=>{map.invalidateSize();if(selected)map.setView([selected.lat,selected.lon],Math.max(map.getZoom(),state.basemap==='outline'?8:12));else fit()})};
 $('listView').onclick=()=>{if(state.view==='list')return;state.view='list';const p=page;render(false);page=p;renderList()};
 $('fit').onclick=fit;
 $('more').onclick=()=>{page++;renderList();$('rows').scrollTop=0};$('prev').onclick=()=>{page=Math.max(0,page-1);renderList();$('rows').scrollTop=0};
 $('reset').onclick=()=>{Object.assign(state,{country:'',region:'',kind:'',metric:'overall',query:'',min:0,unranked:true,mode:'places',sort:'score',top:0,display:'rank',basemap:'street',limit:50});selected=null;$('advanced').open=false;render(true)};
 if(!['overall',...data.categories,...Object.keys(data.dimensions)].includes(state.metric))state.metric='overall';
 if(!['cities','sights',''].includes(state.kind))state.kind='';
 if(!Object.hasOwn(data.countries,state.country))state.country='';
 if(!countries.some(c=>c.region===state.region))state.region='';if(state.country)state.region='';
 if(!['map','list'].includes(state.view))state.view='map';
 if(!['places','countries'].includes(state.mode))state.mode='places';
 state.min=Math.max(0,Math.min(state.metric==='overall'?100:10,state.min));
 $('advanced').open=state.min>0||!state.unranked||state.top>0;
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&selected){e.preventDefault();closeDetail()}else if(e.key==='/'&&!e.ctrlKey&&!e.metaKey&&!e.altKey&&!/INPUT|SELECT|TEXTAREA|BUTTON/.test(document.activeElement.tagName)){e.preventDefault();$('query').focus()}});
 tiles.on('tileerror',()=>{if(state.basemap==='street'&&state.view==='map')$('tileError').hidden=false});$('outlineFallback').onclick=()=>{state.basemap='outline';renderMap();sync()};
 render(true);
}
function countryMatches(){const terms=normalize(state.query).split(/[\s,]+/).filter(Boolean);return countries.filter(c=>(!state.region||c.region===state.region)&&terms.every(q=>normalize(c.name+' '+c.code).includes(q)))}
function render(shouldFit){
 clearTimeout(searchTimer);page=0;map.closePopup();$('rows').scrollTop=0;
 for(const id of ['country','region','kind','metric','query','sort','top','min'])$(id).value=state[id];
 $('min').max=state.metric==='overall'?100:10;$('min').step=state.metric==='overall'?1:.1;$('unranked').checked=state.unranked;
 $('placeFilters').hidden=state.mode==='countries';$('countryField').hidden=state.mode==='countries';$('sortField').hidden=state.mode==='countries';$('advanced').hidden=state.mode==='countries';$('topField').hidden=state.view==='list';$('scoreScale').textContent=state.metric==='overall'?'/ 100':'/ 10';const activeCount=Number(state.min>0)+Number(!state.unranked)+Number(state.top>0&&state.view==='map');$('advancedCount').textContent=activeCount?' · '+activeCount+' active':'';
 for(const [id,on] of [['places',state.mode==='places'],['countries',state.mode==='countries'],['mapView',state.view==='map'],['listView',state.view==='list']]){$(id).classList.toggle('active',on);$(id).setAttribute('aria-pressed',String(on))}
 $('mapframe').hidden=state.view==='list';$('content').classList.toggle('listmode',state.view==='list');
 // Rank inside the selected geographic and kind scope, before search or minimum filters.
 if(state.mode==='countries'){visible=[];points=[];selected=null;}else{
 const key=JSON.stringify([state.country,state.region,state.kind,state.metric]);if(key!==scopeKey){scopeKey=key;scope=ranked(eligible(match(data.rows,{country:state.country,region:state.region,kind:state.kind},data.countries),state.metric,data.categories),state.metric)}
 visible=match(scope,state,data.countries);points=state.top?visible.filter(r=>r.rank!==null).slice(0,state.top):visible;if(selected)selected=visible.find(r=>r.id===selected.id)||null;
 if(state.sort==='name')visible=[...visible].sort((a,b)=>a.name.localeCompare(b.name,'en'));}
 renderInsights();renderList();renderMap();renderDetail();sync();
 if(shouldFit&&state.view==='map')requestAnimationFrame(()=>{map.invalidateSize();fit()});
}
function renderList(){
 const c=data.countries[state.country];
 $('scope').textContent=state.mode==='countries'?'Country directory':c?c.name:state.region?state.region:'Worldwide';
 $('resultTitle').textContent=state.mode==='countries'?'Explore countries':state.kind==='cities'?'Cities & towns':state.kind==='sights'?'Sights & attractions':'Cities & sights';
 const items=state.mode==='countries'?countryMatches():visible;
 $('count').textContent=items.length.toLocaleString()+' matches'+(state.mode==='places'?' · '+items.filter(r=>r.rank!==null).length.toLocaleString()+' ranked · '+title(state.metric):'');
 $('rows').innerHTML=items.slice(page*50,page*50+50).map(r=>'<div class="resultwrap">'+(state.mode==='countries'?'<button class="result countryrow" data-country="'+r.code+'"><span class="flag">'+flag(r.code)+'</span><span class="name"><strong>'+esc(r.name)+'</strong><small>'+esc(r.region)+' · '+(r.cities+r.sights?'Catalogued':'Not yet catalogued')+'</small></span><span class="score">'+r.cities+' cities<br>'+r.sights+' sights</span></button>':'<button class="result '+(selected?.id===r.id?'selected':'')+'" data-id="'+esc(r.id)+'"><span class="rank">'+(r.rank===null?'—':'#'+r.rank)+'</span><span class="name"><strong>'+esc(r.name)+'</strong><small>'+flag(r.country)+' '+esc(data.countries[r.country].name)+' · '+esc(r.type)+' · '+(r.kind==='cities'?'City':'Sight')+'</small></span><span class="score" style="--score:'+color(value(r,state.metric),state.metric)+'">'+scoreText(r)+'<small>'+(r.rank===null?'Unassessed':state.metric==='overall'?'/ 100':'/ 10')+'</small></span></button>')+mapLink(r)+'</div>').join('')||'<div class="empty"><h3>'+(state.mode==='countries'?'No matching countries':'No matching destinations')+'</h3><p>'+(c&&c.cities+c.sights===0?'This country is in the registry but has not been catalogued yet.':'Try another search or clear your filters.')+'</p><button id="emptyReset" class="quiet">Reset filters</button></div>';
 if($('emptyReset'))$('emptyReset').onclick=()=>$('reset').click();
 $('rows').querySelectorAll('[data-country]').forEach(b=>b.onclick=()=>chooseCountry(b.dataset.country));
 $('rows').querySelectorAll('[data-id]').forEach(b=>b.onclick=()=>select(items.find(r=>r.id===b.dataset.id),true));
 $('more').disabled=(page+1)*50>=items.length;$('prev').disabled=page===0;$('pageStatus').textContent=items.length?`${page*50+1}–${Math.min(items.length,(page+1)*50)} of ${items.length.toLocaleString()}`:'0 results';
}

function renderInsights(){
 const el=$('insights');el.hidden=state.mode==='countries';if(el.hidden)return;
 const d=distribution(visible,state.metric), max=Math.max(1,...d.bins),labels=scoreBins(state.metric);
 el.innerHTML='<div class="insighttop"><span><i class="citykey"></i> <b>'+d.cities.toLocaleString()+'</b> cities</span><span><i class="sightkey"></i> <b>'+d.sights.toLocaleString()+'</b> sights</span><span><b>'+d.ranked.toLocaleString()+'</b> ranked</span></div><div class="hist" role="img" aria-label="'+esc(d.bins.map((n,i)=>labels[i]+': '+n).join(', ')+' scores')+'">'+d.bins.map((n,i)=>'<div title="'+labels[i]+': '+n+'" style="--h:'+Math.max(n?8:0,n/max*100)+'%;--bar:'+color(i*10+5,'overall')+'"></div>').join('')+'</div><div class="histlabels"><span>0</span><span>Score distribution</span><span>'+(state.metric==='overall'?'100':'10')+'</span></div>';
}
function scheduleMap(){if(mapFrame)return;mapFrame=requestAnimationFrame(()=>{mapFrame=0;drawPoints()})}
function renderMap(){
 $('display').value=state.display;$('basemap').value=state.basemap;
 if(state.view==='list'){if(map.hasLayer(tiles))map.removeLayer(tiles);layer.clearLayers();centers.clearLayers();selectionLayer.clearLayers();markers.clear();return}
 if(state.basemap==='street'&&!map.hasLayer(tiles))tiles.addTo(map);else if(state.basemap==='outline'&&map.hasLayer(tiles))map.removeLayer(tiles);
 $('map').classList.toggle('outline',state.basemap==='outline');if(state.basemap==='outline')$('tileError').hidden=true;
 const matches=state.mode==='countries'?countryMatches():[], countrySet=new Set(matches.map(c=>c.code));$('display').disabled=state.mode==='countries';
 const key=JSON.stringify([state.mode,state.country,state.region,state.mode==='countries'?state.query:'',state.basemap]);
 if(key!==polygonKey){polygonKey=key;polygons.setStyle(f=>{const code=byFeature(f),c=data.countries[code],count=(c?.cities||0)+(c?.sights||0),active=state.mode==='countries'?countrySet.has(code):!!state.country&&state.country===code;return {weight:active?1.6:.65,color:active?'#146c63':'#85988b',fillColor:count?'#68a894':'#dddcd0',fillOpacity:state.mode==='countries'?(active?(count?Math.min(.85,.28+Math.log1p(count)/12):.25):.08):state.basemap==='outline'?(active?.8:.55):active?.27:.035}})}
 centers.clearLayers();
 if(state.mode==='countries'){
  layer.clearLayers();selectionLayer.clearLayers();markers.clear();
  for(const c of matches)if(c.center){const count=c.cities+c.sights;centers.addLayer(L.circleMarker(c.center,{radius:count?4+Math.min(10,Math.sqrt(count)/2):3,color:'#fff',weight:1.4,fillColor:count?'#18776b':'#9aa6a2',fillOpacity:.9}).bindTooltip(esc(c.name)+' · '+count+' places').on('click',()=>chooseCountry(c.code)))}
  $('legend').textContent='Country coverage · Larger circles = more catalogued destinations';$('mapnote').textContent='Select a country to explore its destinations.';return;
 }
 $('legend').innerHTML='<span class="citykey"></span> City <span class="sightkey"></span> Sight <span class="dot high"></span>'+(state.metric==='overall'?'90+':'9+')+' <span class="dot good"></span>'+(state.metric==='overall'?'80+':'8+')+' <span class="dot mid"></span>'+(state.metric==='overall'?'65+':'6.5+')+' <span class="dot low"></span>Lower <span class="dot none"></span>Unassessed';
 scheduleMap();
}
function drawPoints(){
 if(state.view==='list'||state.mode!=='places')return;
 layer.clearLayers();markers.clear();
 const z=map.getZoom(), bounds=map.getPixelBounds(), size=state.display==='density'?88:z<1.5?40:z<5?56:z<10?42:30;
 let groups=groupPoints(points,r=>map.project([r.lat,r.lon],z),{minX:bounds.min.x-size,maxX:bounds.max.x+size,minY:bounds.min.y-size,maxY:bounds.max.y+size},size,256*2**z);if(z<5)groups=coalesceGroups(groups,size);
 for(const g of groups){
  const r=g.rows[0],v=value(r,state.metric), normalized=v===null?0:state.metric==='overall'?v:v*10;
  const latlng=map.unproject([g.x/g.rows.length,g.y/g.rows.length],z);
  if(g.rows.length===1&&state.display==='rank'){
   const m=L.circleMarker(latlng,{radius:v===null?4:4+normalized/25,weight:r.kind==='cities'?2.5:1.2,color:r.kind==='cities'?'#193d63':'#fff',fillColor:color(v,state.metric),fillOpacity:.92}).bindTooltip(esc(r.name)+' · '+(r.rank===null?'Unassessed':'#'+r.rank+' · '+scoreText(r))+' · '+(r.kind==='cities'?'City':'Sight')).on('click',()=>select(r,false));
   layer.addLayer(m);markers.set(r.id,m);continue;
  }
  const n=g.rows.length,cities=g.rows.filter(x=>x.kind==='cities').length, radius=clusterRadius(n,size), diameter=radius*2;
  const icon=L.divIcon({className:'atlas-cluster',html:'<span style="--cluster:'+color(v,state.metric)+';--city:'+Math.round(cities/n*100)+'%">'+n+'</span>',iconSize:[diameter,diameter],iconAnchor:[radius,radius]});
  const m=L.marker(latlng,{icon,keyboard:true,title:n+' destinations, '+cities+' cities and '+(n-cities)+' sights',alt:n+' destinations; zoom or open group'}).bindTooltip(n+' destinations · '+cities+' cities · '+(n-cities)+' sights').on('click',()=>{
   if(z<14&&n>1&&g.rows.some(x=>x.lat!==r.lat||x.lon!==r.lon)){map.setView(latlng,Math.min(14,z+2));return}
   if(n===1){select(r,false);return}
   const box=document.createElement('div');box.className='clusterlist';const heading=document.createElement('strong');heading.textContent=n+' destinations here';box.append(heading);const entries=document.createElement('div');box.append(entries);let offset=0;const next=document.createElement('button');next.textContent='Show more';const append=()=>{for(const row of g.rows.slice(offset,offset+50)){const b=document.createElement('button');b.textContent=row.name+' · '+scoreText(row);b.onclick=()=>{map.closePopup();select(row,false)};entries.append(b)}offset+=50;next.hidden=offset>=n};next.onclick=append;box.append(next);append();
   L.popup({maxHeight:240}).setLatLng(latlng).setContent(box).openOn(map);
  });layer.addLayer(m);
 }
 drawSelection();
 $('mapnote').textContent=points.length.toLocaleString()+' map destinations · '+groups.length+' visible groups'+(state.display==='density'?' · Bubble size = count':' · Zoom to explore')+' · Ring shows city share';
}
function drawSelection(){selectionLayer.clearLayers();if(!selected||state.view!=='map'||state.mode!=='places')return;const lon=selected.lon+360*Math.round((map.getCenter().lng-selected.lon)/360);L.circleMarker([selected.lat,lon],{radius:13,weight:3,color:'#193d63',fill:false,interactive:false}).addTo(selectionLayer).bringToFront();}
function byFeature(f){if(!f)return '';if(f.properties?.name==='Kosovo')return 'XK';return byNumber.get(String(Number(f.id)))||''}
function fitWorld(){map.fitBounds([[-58,-180],[78,180]],{padding:[8,8],maxZoom:2,animate:false})}
function fit(){if(state.view==='list')return;if(state.mode==='countries'){const pts=countryMatches().map(c=>c.center).filter(Boolean);if((state.region||state.query)&&pts.length)map.fitBounds(pts,{padding:[35,35],maxZoom:5});else fitWorld();return}if(points.length){if(!state.country&&!state.region&&!state.query&&points.length>1000){fitWorld();return}map.fitBounds(wrappedLocations(points),{padding:[32,32],maxZoom:12})}else if(data.countries[state.country]?.center)map.setView(data.countries[state.country].center,5);else fitWorld()}
function select(r,focusMap){if(!r)return;selected=r;const index=visible.findIndex(x=>x.id===r.id);if(index>=0)page=Math.floor(index/50);renderList();renderDetail();if(state.view==='map'){if(focusMap){const lon=r.lon+360*Math.round((map.getCenter().lng-r.lon)/360);map.setView([r.lat,lon],Math.max(map.getZoom(),state.basemap==='outline'?8:12));scheduleMap()}drawSelection()}$('detailTitle').focus({preventScroll:true});if(window.matchMedia('(max-width: 800px)').matches)$('detail').scrollIntoView({block:'nearest',behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'})}
function closeDetail(){const id=selected?.id;selected=null;drawSelection();renderDetail();renderList();const button=Array.from($('rows').querySelectorAll('[data-id]')).find(b=>b.dataset.id===id);(button||$('query')).focus()}
function renderDetail(){const d=$('detail');d.hidden=!selected;$('rows').hidden=!!selected;$('pager').hidden=!!selected;$('insights').hidden=!!selected||state.mode==='countries';if(!selected)return;const r=selected;d.innerHTML='<button id="closeDetail" class="quiet">Back to results</button><div class="detailhead"><div><h2 id="detailTitle" tabindex="-1">'+esc(r.name)+'</h2><div class="scope">'+esc(data.countries[r.country].name)+' · '+esc(r.type)+'</div></div></div><p class="detailScore">'+format(r.overall,'overall')+' <small>/ 100 overall</small></p><p class="detailRank">'+(r.rank===null?'Unassessed for '+esc(title(state.metric)):'#'+r.rank+' in '+esc(title(state.metric))+' ranking'+(state.metric==='overall'?'':' · '+scoreText(r)+'/10'))+'</p><a class="primaryMap" href="'+esc(mapsSearchUrl(r.name,data.countries[r.country].name))+'" target="_blank" rel="noopener noreferrer">Open in Google Maps</a><h3>Core score breakdown</h3><div class="breakdown">'+Object.entries(data.dimensions).map(([k,w])=>'<div><span>'+title(k)+' · '+Math.round(w*100)+'%</span><b>'+format(r.scores[k]??null,k)+'</b>'+(r.scores[k]==null?'<span class="missingScore">Unassessed</span>':'<progress aria-label="'+esc(title(k))+'" max="10" value="'+r.scores[k]+'"></progress>')+'</div>').join('')+'</div><h3>Category ratings</h3><div class="chips">'+Object.entries(r.scores.categories||{}).sort((a,b)=>(b[1]??-1)-(a[1]??-1)).map(([k,v])=>'<span>'+title(k)+' <b>'+format(v,k)+'</b></span>').join('')+'</div><p class="detailLinks"><a href="'+esc(mapsSearchUrl(r.lat+','+r.lon))+'" target="_blank" rel="noopener noreferrer">GPS point ↗</a><a href="'+repo+esc(r.source)+'" target="_blank" rel="noopener">Source YAML ↗</a><a href="'+repo+'countries/'+r.country+'/'+r.kind+'.md" target="_blank" rel="noopener">Country ranking ↗</a></p><p class="muted">Representative coordinates: '+r.lat+', '+r.lon+'</p>';$('closeDetail').onclick=closeDetail}
fetch(import.meta.env.BASE_URL+'atlas.json').then(r=>{if(!r.ok)throw Error('HTTP '+r.status);return r.json()}).then(d=>{data=d;mount()}).catch(e=>{$('app').innerHTML='<main class="empty" role="alert"><h1>Atlas unavailable</h1><p>Could not load the destination index. Check your connection and try again.</p><button id="retry" class="quiet">Try again</button></main>';$('retry').onclick=()=>location.reload();console.error(e)});
