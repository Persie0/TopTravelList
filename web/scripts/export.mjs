import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {parse} from 'yaml';
import {overall} from './overall.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const web=path.join(root,'web');
const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const registry=read(path.join(root,'countries/_registry.json'));
const scoring=read(path.join(root,'methodology/scoring.json'));
const world=read(path.join(web,'node_modules/world-countries/countries.json'));
const names=new Intl.DisplayNames(['en'],{type:'region'});
const overrides={BO:'Bolivia',BN:'Brunei',CD:'DR Congo',CN:'China',CZ:'Czechia',GB:'United Kingdom',IR:'Iran',KR:'South Korea',KP:'North Korea',LA:'Laos',MD:'Moldova',MK:'North Macedonia',PS:'Palestine',RU:'Russia',SY:'Syria',TW:'Taiwan',TZ:'Tanzania',US:'United States',VA:'Vatican City',VE:'Venezuela',VN:'Vietnam',XK:'Kosovo'};
const countries={}, rows=[], seen=new Set();
const patterns=[[/great wall|city wall|fortress|citadel|\bfort\b/i,'Fortification'],[/national park|marine park|nature reserve|geopark|sanctuary/i,'Park / reserve'],[/temple|monastery|shrine|pagoda|mosque|cathedral|church|stupa|abbey/i,'Religious site'],[/museum|mausoleum|memorial|tombs?|grottoes|archaeological|ruins/i,'Museum / heritage'],[/palace|castle|schloss|chateau/i,'Palace / castle'],[/waterfall|\bfalls\b/i,'Waterfall'],[/beach|bay|lagoon/i,'Beach / bay'],[/island|islet/i,'Island'],[/lake|reservoir/i,'Lake'],[/river|canal/i,'River / waterway'],[/\bcave\b|\bcavern\b/i,'Cave'],[/peak|mountain|\bmount\b|volcano|glacier/i,'Mountain / peak'],[/gorge|canyon|valley/i,'Valley / canyon'],[/forest|jungle|rainforest/i,'Forest'],[/garden|arboretum|botanic/i,'Garden'],[/wetland|marsh/i,'Wetland'],[/village|old town|ancient town|historic centre|historic center/i,'Historic settlement'],[/tower|skyscraper|skywalk|viewpoint|observatory/i,'Tower / viewpoint'],[/bridge/i,'Bridge'],[/market|bazaar/i,'Market'],[/trail|trek|plank walk/i,'Trail / walk'],[/desert|dune/i,'Desert'],[/historic areas|historical park/i,'Historic area'],[/park|square|plaza/i,'Park / square'],[/harbour|harbor|coast|cape/i,'Coast']];
for(const code of registry.codes){
  const geo=world.find(c=>c.cca2===code);
  const c=countries[code]={code,name:overrides[code]||names.of(code),region:geo?.region||'Other',numeric:geo?.ccn3||null,center:geo?.latlng||null,cities:0,sights:0};
  for(const kind of ['cities','sights']){
    const dir=path.join(root,'countries',code,kind);
    for(const file of fs.readdirSync(dir).filter(f=>f.endsWith('.yaml')).sort()){
      const r=parse(fs.readFileSync(path.join(dir,file),'utf8'));
      const loc=r.location;
      if(seen.has(r.id)||loc.country_code!==code||!Number.isFinite(loc.latitude)||!Number.isFinite(loc.longitude)||Math.abs(loc.latitude)>90||Math.abs(loc.longitude)>180) throw Error('Invalid destination '+file);
      seen.add(r.id);c[kind]++;
      const type=kind==='cities'?(/\bvillage\b/i.test(r.name)?'Village':/\btown\b/i.test(r.name)?'Town':'City / town'):(patterns.find(([re])=>re.test(r.name))?.[1]||'Attraction');
      rows.push({id:r.id,name:r.name,country:code,kind,type,lat:loc.latitude,lon:loc.longitude,scores:r.scores,overall:overall(r.scores,scoring.dimensions),source:'countries/'+code+'/'+kind+'/'+file});
    }
  }
}
fs.mkdirSync(path.join(web,'public'),{recursive:true});
fs.writeFileSync(path.join(web,'public/atlas.json'),JSON.stringify({countries,rows,dimensions:scoring.dimensions,categories:scoring.categories,version:scoring.version}));
console.log('Atlas: '+Object.keys(countries).length+' countries, '+rows.length+' destinations.');
