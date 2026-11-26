#!/usr/bin/env python3
"""Read-only worldwide diagnostic, never an automatic score adjustment.

Every registered area and every YAML is included. Name/type/profile matches
are research leads, not proof of duplication or bias. Existing review labels
are recorded as declared, not independently verified.
"""
from __future__ import annotations
import argparse
import collections
import csv
import json
import math
import re
import statistics
import unicodedata
from decimal import Decimal
from pathlib import Path
import yaml
from rank import overall_score
from generate_rankings import get_kind

ROOT = Path(__file__).resolve().parents[1]
DIMS = ("impact", "uniqueness", "significance", "experience", "depth")
HEAD = re.compile(r"^#{2,4}\s+(?:\[)?((?:city|sight)-[a-z]{2}-[a-z0-9-]+)\s*(?:\]|[—–-]|$)", re.M)
STATUSES = ("fact-checked", "source-linked-unverified", "editorial-only", "unassessed")
STATUS = re.compile(r"\b(?:fact-checked|source-linked-unverified|editorial-only|unassessed)\b")
SMALL = re.compile(r"\b(?:gate|viewpoint|lookout|terrace|pier|statue|market|square|garden|bridge|tower|chapel|visitor cent(?:er|re))\b", re.I)

def normal(name):
    return " ".join(re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()))

def distance(a,b):
    lat1,lon1=map(math.radians,a); lat2,lon2=map(math.radians,b)
    h=math.sin((lat2-lat1)/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin((lon2-lon1)/2)**2
    return 6371*2*math.asin(min(1,math.sqrt(h)))

def provenance(root):
    notes=collections.defaultdict(set)
    for p in sorted((root/"methodology/reviews").rglob("*.md")):
        s=p.read_text(encoding="utf-8")
        heads=list(HEAD.finditer(s))
        for i,m in enumerate(heads):
            section=s[m.end():heads[i+1].start() if i+1<len(heads) else len(s)]
            # Last explicitly declared status wins within the individual section;
            # do not infer evidence from incidental mentions in prose.
            labels=re.findall(r"\*\*(fact-checked|source-linked-unverified|editorial-only|unassessed)\*\*",section)
            if not labels:
                labels=re.findall(r"(?im)^[-* ]*Evidence status\s*:\s*\x60?(fact-checked|source-linked-unverified|editorial-only|unassessed)\b",section)
            notes[m.group(1)].add((str(p.relative_to(root)),labels[-1] if labels else "named-review-status-unclear"))
    return notes

def historical(root):
    ids=set()
    for name in ("city-calibration-audit.md","sight-review-2026-full-audit.md"):
        p=root/"methodology"/name
        if not p.exists(): continue
        text=p.read_text(encoding="utf-8")
        for code,kind,slug in re.findall(r"countries/([A-Z]{2})/(cities|sights)/([a-z0-9-]+)\.yaml",text):
            ids.add(("city" if kind=="cities" else "sight")+"-"+code.lower()+"-"+slug)
        ids.update(re.findall(r"\b(?:city|sight)-[a-z]{2}-[a-z0-9-]+\b",text))
    return ids

def examine(root):
    meta=json.loads((root/"methodology/scoring.json").read_text())
    codes=json.loads((root/"countries/_registry.json").read_text())["codes"]
    weights={k:Decimal(str(v)) for k,v in meta["dimensions"].items()}
    notes=provenance(root); history=historical(root); rows=[]
    for code in codes:
        for kind in ("cities","sights"):
            for p in sorted((root/"countries"/code/kind).glob("*.yaml")):
                data=yaml.safe_load(p.read_text(encoding="utf-8"))
                scores=data["scores"]; core=tuple(scores.get(k) for k in DIMS)
                cats=scores.get("categories",{})
                loc=data["location"]
                fields={**dict(zip(DIMS,core)),**cats}
                high=[k for k,v in fields.items() if v is not None and v>=9.5]
                record_notes=sorted(notes.get(data["id"],()))
                statuses=sorted({s for _,s in record_notes})
                flags=set()
                total=overall_score(data,weights)
                if total is None: flags.add("incomplete-core")
                if high: flags.add("field-9.5-plus")
                if total is not None and total>=90: flags.add("overall-90-plus")
                if total is not None and total>=95: flags.add("overall-95-plus")
                if total is not None and total>=90 and kind=="sights" and SMALL.search(data["name"]): flags.add("small-scope-high-total")
                if not record_notes: flags.add("historical-review-only" if data["id"] in history else "no-recognized-review-heading")
                if record_notes and not statuses==["fact-checked"]: flags.add("evidence-review")
                if len(statuses)>1: flags.add("conflicting-declared-status")
                rows.append(dict(id=data["id"],name=data["name"],code=code,kind=kind,type=get_kind(data["name"],kind),path=str(p.relative_to(root)),core=core,cats=cats,total=total,high=high,loc=(loc["latitude"],loc["longitude"]),notes=record_notes,statuses=statuses,flags=flags,related=set()))
    # Repeated core profiles within a cohort: a diagnostic, not an automatic error.
    profiles=collections.defaultdict(list); names=collections.defaultdict(list); gps=collections.defaultdict(list)
    for r in rows:
        if r["total"] is not None: profiles[r["code"],r["kind"],r["core"]].append(r)
        n=normal(r["name"])
        if n: names[r["kind"],n].append(r)
        gps[r["kind"],tuple(round(v,4) for v in r["loc"])].append(r)
    for group in profiles.values():
        if len(group)>1:
            for r in group: r["flags"].add("repeated-core-profile")
    for group in names.values():
        if len(group)>1:
            for i,a in enumerate(group):
                for b in group[i+1:]:
                    if distance(a["loc"],b["loc"])<=15:
                        for x,y in ((a,b),(b,a)):
                            x["flags"].add("near-identical-name-nearby")
                            x["related"].add(y["id"])
    for group in gps.values():
        if len(group)>1:
            for a in group:
                a["flags"].add("shared-representative-gps")
                a["related"].update(b["id"] for b in group if b is not a)
    # Compare distribution only to like-kind and inferred-type worldwide cohort.
    # Type is inferred from name, so generic Attraction bucket remains separate.
    cohorts=collections.defaultdict(list)
    for r in rows:
        if r["total"] is not None: cohorts[r["kind"],r["type"]].append(r["total"])
    stats={k:(statistics.median(v),len(v)) for k,v in cohorts.items()}
    for r in rows:
        med,n=stats.get((r["kind"],r["type"]),(None,0))
        r["type_median"]=med; r["type_n"]=n
        if n>=20 and r["total"] is not None and abs(r["total"]-med)>=15:
            r["flags"].add("type-score-distance-15-plus")
    return codes,rows

def fmt(x):
    return "" if x is None else f"{x:.2f}"

def write_reports(out,codes,rows):
    out.mkdir(parents=True,exist_ok=True)
    columns=["id","country","kind","name","inferred_type","overall",*DIMS,"high_fields","declared_review_status","review_files","type_median","type_sample","flags","related_ids","source"]
    counts=collections.Counter(f for r in rows for f in r["flags"])
    with (out/"records.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n"); w.writerow(columns)
        for r in sorted(rows,key=lambda r:r["id"]):
            w.writerow([r["id"],r["code"],r["kind"],r["name"],r["type"],fmt(r["total"]),*("" if v is None else v for v in r["core"]),";".join(r["high"]),";".join(r["statuses"]),";".join(p for p,_ in r["notes"]),fmt(r["type_median"]),r["type_n"],";".join(sorted(r["flags"])),";".join(sorted(r["related"])),r["path"]])
    def cell(s): return str(s).replace("|","\\|").replace("\n"," ")
    lines=["# Worldwide record-level diagnostic","",f"**{len(codes)} registered areas; {len(rows)} source records screened.**",f"Ranked: {sum(r['total'] is not None for r in rows)}; unassessed: {sum(r['total'] is None for r in rows)}.","","This is an automatically regenerated diagnostic, not an individual editorial reassessment or proof of bias. No scores are changed. Type is inferred from names; missing review headings may be parser limitations. Declared evidence statuses are not independent checks. Shared GPS and nearby names may denote legitimate nested attractions. Country medians depend on selection and are not country quality scores.","","## Flags","","| Flag | Records |","| --- | ---: |"]
    lines.extend(f"| {k} | {v} |" for k,v in sorted(counts.items()))
    lines.extend(["","## All areas — cities and sights separately","","| Area | Kind | Total | Ranked | Median | 90+ | 95+ | High field | Named review | Top 3 (ranked) |","| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |"])
    group=collections.defaultdict(list)
    for r in rows: group[r["code"],r["kind"]].append(r)
    for code in codes:
        for kind in ("cities","sights"):
            rr=group[code,kind]; ranked=sorted((r for r in rr if r["total"] is not None),key=lambda r:(-r["total"],r["id"]))
            med=statistics.median(r["total"] for r in ranked) if ranked else None
            leaders="; ".join(f"[{cell(r['name'])}](../../{r['path']}) {fmt(r['total'])}" for r in ranked[:3])
            lines.append(f"| {code} | {kind} | {len(rr)} | {len(ranked)} | {fmt(med)} | {sum(r['total']>=90 for r in ranked)} | {sum(r['total']>=95 for r in ranked)} | {sum(bool(r['high']) for r in rr)} | {sum(bool(r['notes']) for r in rr)} | {leaders} |")
    lines.extend(["","## Review queue: nearby exact normalized names","","Same-kind records with equal normalized names within 15 km. These are candidates only; never delete automatically.","","| Record | Area | Score | Related IDs |","| --- | --- | ---: | --- |"])
    for r in sorted(rows,key=lambda r:r["id"]):
        if "near-identical-name-nearby" in r["flags"]:
            lines.append(f"| [{cell(r['name'])}](../../{r['path']}) | {r['code']} | {fmt(r['total'])} | {', '.join(sorted(r['related']))} |")
    lines.extend(["","## Review queue: small-scope 90+ records","","Name heuristic, not a determination of scope or inflated rating.","","| Record | Area | Score |","| --- | --- | ---: |"])
    for r in sorted((r for r in rows if "small-scope-high-total" in r["flags"]),key=lambda r:(-r["total"],r["id"])):
        lines.append(f"| [{cell(r['name'])}](../../{r['path']}) | {r['code']} | {fmt(r['total'])} |")
    lines.extend(["","The complete [record-by-record TSV](records.tsv) contains every source ID, five core fields, review references, high fields, type cohort and flags. No unflagged record is certified accurate. Use the individual review template before adjusting any score.",""])
    (out/"README.md").write_text("\n".join(lines),encoding="utf-8")
    print(f"SCREENED {len(codes)} areas, {len(rows)} destinations; ranked {sum(r['total'] is not None for r in rows)}")
    print("FLAGS",json.dumps(dict(sorted(counts.items()))))
    for r in sorted(rows,key=lambda r:r["id"]):
        if "near-identical-name-nearby" in r["flags"]: print("DUPLICATE CANDIDATE",r["id"],";".join(sorted(r["related"])))
    for r in sorted((r for r in rows if "small-scope-high-total" in r["flags"]),key=lambda r:(-r["total"],r["id"]))[:40]:
        print("SCOPE CANDIDATE",r["id"],fmt(r["total"]))
    return counts

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=ROOT/"methodology"/"worldwide-diagnostics")
    args=parser.parse_args()
    codes,rows=examine(ROOT)
    assert len({r["id"] for r in rows})==len(rows)
    assert set(r["code"] for r in rows)<=set(codes)
    write_reports(args.output,codes,rows)

if __name__=="__main__": main()
