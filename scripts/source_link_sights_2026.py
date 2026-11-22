#!/usr/bin/env python3
"""Collect source-verified, per-site Wikipedia evidence for remaining 1655 attractions.

This is a *research-assistance and identity-verification* pass, not 1655 human
editorial decisions. Exact article titles, country context and geographic
proximity are checked before a source can be marked verified. Ambiguous or
unavailable source matches are *not* promoted to independently researched.
No YAML rating is edited by this evidence harvester.

Source: Wikimedia Foundation's English Wikipedia, CC BY-SA 4.0:
https://en.wikipedia.org/wiki/Wikipedia:Copyrights
"""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import difflib
import html
import json
import math
import re
import sys
import threading
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
COUNTRIES = ("AT", "TH", "KR", "CN", "VN", "KH", "TW")
DECISIONS = ROOT / "methodology" / "sight-review-decisions-2026"
EVIDENCE = ROOT / "methodology" / "sight-review-2026-remaining-evidence.json"
REPORT = ROOT / "methodology" / "sight-review-2026-evidence-report.md"
API = "https://en.wikipedia.org/w/api.php"
AGENT = "TopTravelListResearchAudit/2026 (+https://github.com/Persie0/TopTravelList; encyclopedia-evidence attribution)"
COUNTRY_ALIASES = {
    "AT": ("austria", "austrian"),
    "TH": ("thailand", "thai"),
    "KR": ("south korea", "korea", "korean", "jeju"),
    "CN": ("china", "chinese", "tibet", "hong kong", "macau", "xinjiang"),
    "VN": ("vietnam", "vietnamese"),
    "KH": ("cambodia", "cambodian", "khmer"),
    "TW": ("taiwan", "taiwanese", "formosa"),
}
COUNTRY_LABELS = {
    "AT": "Austria", "TH": "Thailand", "KR": "South Korea",
    "CN": "China", "VN": "Vietnam", "KH": "Cambodia", "TW": "Taiwan",
}
STOP = set("and the at of on in near from to for a an historical historic national park forest temple island islands archaeological ancient site sites monument scenic area mountain lake river beach museum sanctuary reserve palace pagoda waterfall valley korea vietnam china austria thailand cambodia taiwan".split())
_threadlocal = threading.local()


def norm(value):
    value = unicodedata.normalize("NFKD", str(value)).casefold()
    value = "".join(x for x in value if not unicodedata.combining(x))
    value = re.sub(r"[(][^)]*[)]", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def overlap(a, b):
    aw = set(norm(a).split()) - STOP
    bw = set(norm(b).split()) - STOP
    if not aw or not bw:
        return 0.0
    return len(aw & bw) / max(len(aw), len(bw))


def similarity(a, b):
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return 0.0
    ratio = difflib.SequenceMatcher(None, na, nb).ratio()
    return max(ratio, overlap(a, b) * 0.95)


def distance_km(a_lat, a_lon, b_lat, b_lon):
    ra, rb = math.radians(float(a_lat)), math.radians(float(b_lat))
    dlat = rb - ra
    dlon = math.radians(float(b_lon) - float(a_lon))
    h = math.sin(dlat / 2)**2 + math.cos(ra) * math.cos(rb) * math.sin(dlon / 2)**2
    return 2 * 6371 * math.asin(min(1.0, math.sqrt(h)))


def get_api(params, attempts=4):
    url = API + "?" + urllib.parse.urlencode(params, doseq=True)
    last = None
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": AGENT, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=22) as resp:
                if resp.status != 200:
                    raise ValueError(f"HTTP {resp.status}")
                return json.load(resp)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
            last = str(e)
            if attempt != attempts - 1:
                time.sleep(min(15, 1 + 2 * attempt))
    raise RuntimeError(f"API fetch failed after {attempts} attempts: {last}")


def get_article(query):
    x = get_api({
        "action": "query", "titles": query, "redirects": "1",
        "prop": "extracts|coordinates|pageprops",
        "exintro": "1", "explaintext": "1", "exchars": "760",
        "colimit": "4", "format": "json", "formatversion": "2"
    })
    pages = x.get("query", {}).get("pages", [])
    good = [p for p in pages if "missing" not in p and p.get("ns", 0) == 0]
    return good[0] if good else None


def search_titles(name, country):
    q = f'"{name}" {COUNTRY_LABELS[country]}'
    x = get_api({
        "action": "query", "list": "search", "srsearch": q,
        "srlimit": "3", "srnamespace": "0", "format": "json"
    })
    found = [p.get("title") for p in x.get("query", {}).get("search", []) if p.get("title")]
    if not found:
        q = f"{name} {COUNTRY_LABELS[country]}"
        x = get_api({
            "action": "query", "list": "search", "srsearch": q,
            "srlimit": "3", "srnamespace": "0", "format": "json"
        })
        found = [p.get("title") for p in x.get("query", {}).get("search", []) if p.get("title")]
    return found


def assess(rec, page):
    title = page.get("title", "")
    extracted = html.unescape(page.get("extract", "") or "")
    coords = page.get("coordinates") or []
    expected = rec["name"]
    sim = similarity(expected, title)
    geo = None
    if coords:
        try:
            geo = round(distance_km(
                rec["latitude"], rec["longitude"],
                coords[0]["lat"], coords[0]["lon"]
            ), 1)
        except (ValueError, TypeError, KeyError):
            geo = None
    alias = any(x in extracted.casefold() or x in title.casefold() for x in COUNTRY_ALIASES[rec["country"]])
    large_area = bool(re.search(
        r"mountain|national park|valley|river|island|archipelago|lake|forest|desert|bay|coast|scenic area|reserve",
        expected, re.I))
    threshold = 110 if large_area else 32
    if sim >= 0.87 and geo is not None and geo <= threshold:
        conf = "verified_geo"
    elif sim >= 0.94 and alias and (geo is None or geo <= threshold * 2):
        conf = "verified_context"
    elif sim >= 0.80 and geo is not None and geo <= threshold / 2 and alias:
        conf = "verified_geo_context"
    elif sim >= 0.75 and geo is not None and geo <= threshold * 2:
        conf = "candidate_needs_review"
    else:
        conf = "unverified"
    if page.get("description") in ("disambiguation page",) or "may refer to" in extracted.lower()[:250]:
        conf = "unverified"
    url = "https://en.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_"), safe="()_")
    summary = re.sub(r"\s+", " ", extracted).strip()
    return {
        "status": conf, "article_title": title,
        "wikipedia_url": url, "wikidata_id": page.get("pageprops", {}).get("wikibase_item"),
        "match_score": round(sim, 3), "coord_distance_km": geo,
        "country_in_article": alias, "article_excerpt": summary[:650],
        "article_available": bool(summary),
    }


def site_records():
    already = set()
    for c in COUNTRIES:
        for line in (DECISIONS / f"{c}.tsv").read_text(encoding="utf-8").splitlines():
            if line and not line.startswith("#"):
                already.add(f"{c}/{line.split('|', 1)[0]}")
    all_records = []
    for c in COUNTRIES:
        for p in sorted((ROOT / "countries" / c / "sights").glob("*.yaml")):
            key = f"{c}/{p.stem}"
            if key in already:
                continue
            item = yaml.safe_load(p.read_text(encoding="utf-8"))
            loc = item["location"]
            all_records.append({
                "key": key, "country": c,
                "name": item["name"],
                "latitude": loc["latitude"], "longitude": loc["longitude"],
                "core": {s: item["scores"][s] for s in ("impact", "uniqueness", "significance", "experience", "depth")},
                "categories": item["scores"]["categories"],
            })
    assert len(all_records) == 1655, f"Expected exactly 1655 remaining sights, got {len(all_records)}"
    return all_records


def fetch_one(rec):
    candidates = []
    queries = [rec["name"]]
    base = re.sub(r"\([^)]*\)", "", rec["name"]).strip()
    if base != rec["name"] and base:
        queries.append(base)
    for q in queries[:2]:
        try:
            page = get_article(q)
            if page:
                candidates.append(assess(rec, page))
                if candidates[-1]["status"].startswith("verified_"):
                    break
        except Exception as exc:
            candidates.append({"status": "lookup_error", "error": str(exc)[:100]})
    if not any(x.get("status", "").startswith("verified_") for x in candidates):
        try:
            hits = search_titles(rec["name"], rec["country"])
            for title in hits[:3]:
                page = get_article(title)
                if page:
                    candidates.append(assess(rec, page))
                    if candidates[-1]["status"].startswith("verified_"):
                        break
        except Exception as exc:
            candidates.append({"status": "lookup_error", "error": str(exc)[:100]})
    order = {"verified_geo": 4, "verified_geo_context": 3, "verified_context": 2,
             "candidate_needs_review": 1, "unverified": 0, "lookup_error": -1}
    candidates.sort(key=lambda x: (order.get(x["status"], -1), x.get("match_score", 0)), reverse=True)
    best = candidates[0] if candidates else {"status": "lookup_error", "error": "No candidate"}
    return rec["key"], {
        "name": rec["name"],
        "country": rec["country"],
        "latitude": rec["latitude"], "longitude": rec["longitude"],
        **best, "candidate_count": len(candidates),
    }


def collect(limit, workers):
    records = site_records()
    if limit:
        records = records[:limit]
    print(f"Collecting {len(records)} independently source-checked article candidates (workers={workers})", flush=True)
    results = {}
    with futures.ThreadPoolExecutor(max_workers=workers) as pool:
        queue = {pool.submit(fetch_one, rec): rec["key"] for rec in records}
        for i, future in enumerate(futures.as_completed(queue), 1):
            try:
                key, val = future.result()
                results[key] = val
            except Exception as exc:
                key = queue[future]
                rec = next(r for r in records if r["key"] == key)
                results[key] = {"name": rec["name"], "country": rec["country"],
                                "status": "lookup_error", "error": str(exc)[:180]}
            if i % 100 == 0:
                ct = Counter(r["status"] for r in results.values())
                print(f"Processed {i}/{len(records)}; {dict(ct)}", flush=True)
    obj = {
        "title": "TopTravelList source-linked remaining sight audit",
        "source": "English Wikipedia via live MediaWiki API, 22 November 2026",
        "license": "Wikipedia text CC BY-SA 4.0; article links and Wikimedia attribution included",
        "method": "Title and identity comparison with independent lat/lon plus country context; auto-matched identities are not human score judgments",
        "expected_missing_prior_editorial_decisions": 1655,
        "records": {key: results[key] for key in sorted(results)},
    }
    EVIDENCE.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8", newline="\n")
    report(obj, check=False)
    count = Counter(x["status"] for x in results.values())
    print(f"PASS collected {len(results)}. Result distribution: {dict(count)}", flush=True)


def report(obj, check):
    rows = obj["records"]
    by_country = defaultdict(Counter)
    for key, x in rows.items():
        by_country[key[:2]][x["status"]] += 1
    out = [
        "# Source cross-check of previously unresearched worldwide sights",
        "",
        "**Source:** English Wikipedia through MediaWiki API (November 2026).",
        "Article excerpts are attributed to Wikipedia contributors, CC BY-SA 4.0.",
        "",
        "**IMPORTANT:** A verified article match confirms an encyclopedia source for a",
        "specific destination identity, **not** an independently researched or verified",
        "destination quality rating. It does not automatically authorize a changed score.",
        "Ambiguous geolocations and similar names remain open for editorial review.",
        "",
        "| Country | Sights checked | Geographic/context match | Candidate requiring human verification | No validated article |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for c in COUNTRIES:
        ctr = by_country[c]
        good = sum(v for k, v in ctr.items() if k.startswith("verified_"))
        cand = ctr["candidate_needs_review"]
        no = sum(v for k, v in ctr.items() if k in ("unverified", "lookup_error"))
        out.append(f"| {c} | {sum(ctr.values())} | {good} | {cand} | {no} |")
    out.extend(["", "## One row per checked sight", "",
                "| Sight | Source match | Source title | Coordinates separation (km) | Evidence URL |",
                "| --- | --- | --- | ---: | --- |"])
    for key, rec in rows.items():
        c, slug = key.split("/")
        name = rec["name"].replace("|", "/")
        url = rec.get("wikipedia_url")
        mdlink = f"[Article]({url})" if url else "—"
        source_title = rec.get("article_title", "—").replace("|", "/")
        separation = rec.get("coord_distance_km")
        out.append(f"| [{name}](../countries/{c}/sights/{slug}.yaml) | {rec['status']} | "
                   f"{source_title} | {separation if separation is not None else '—'} | {mdlink} |")
    content = "\n".join(out) + "\n"
    if check:
        assert REPORT.read_text(encoding="utf-8") == content
    else:
        REPORT.write_text(content, encoding="utf-8", newline="\n")


def verify():
    all_expected = {r["key"] for r in site_records()}
    obj = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    rows = obj["records"]
    assert set(rows) == all_expected, f"Missing evidence rows: {len(all_expected - set(rows))}"
    for key, x in rows.items():
        assert x["country"] == key[:2]
        if x["status"].startswith("verified_"):
            assert x["wikipedia_url"].startswith("https://en.wikipedia.org/wiki/")
            assert x["article_available"]
            assert x["match_score"] >= 0.8
            if x["status"] == "verified_geo":
                assert x["coord_distance_km"] is not None
    report(obj, check=True)
    print(f"PASS: 1655 individual records have source-match assessment; "
          f"{sum(x['status'].startswith('verified_') for x in rows.values())} "
          f"verified article identities. No source rating changes made.", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--collect", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=5)
    args = parser.parse_args()
    if args.collect == args.check or (args.check and args.limit):
        parser.error("Choose --collect or --check; --limit applies only to --collect")
    collect(args.limit, args.workers) if args.collect else verify()
