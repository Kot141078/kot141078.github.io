#!/usr/bin/env python3
"""Bounded ACOW publication page and existing site-index integration.
The published archive is input data, never executable code or editable source.
"""
from __future__ import annotations
import argparse
import hashlib
import html
import io
import json
from pathlib import Path
import re
import sys
import urllib.request
import zipfile

SLUG = 'shared-open-worlds-human-ai-dyads-v0-2'
ROUTE = '/publications/' + SLUG + '/'
SITE = 'https://ivankotov.eu'
PIN = 'fb6a71dc022e7d894ad49a246f3b59adaf13c55b'
REPO = 'https://github.com/Kot141078/advanced-global-intelligence/tree/' + PIN + '/publications/' + SLUG
RAW = 'https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/' + PIN + '/publications/' + SLUG + '/'
TITLE = 'Shared Open Worlds for Human–AI Dyads: Role Switching, Experience Qualification, and Cross-World Continuity Evaluation'
DOI = '10.5281/zenodo.22542470'
CONCEPT = '10.5281/zenodo.22542469'
ZIP = 'A_C_SHARED_OPEN_WORLD_EXPERIENCE_v0_2_EN_PUBLIC.zip'
PAPER = 'A_C_SHARED_OPEN_WORLD_EXPERIENCE_PAPER_v0_2_EN'
SHA = '47945ca619f65ea6788de84c22ee278d0cee29fba929ab0e7e1db5fe17cc92ce'
PDF_SHA = '59a69617fdc64092286296126d60d6331285105408ac4f54c474230240e03aee'
DATE = '2026-09-06'
EXPECTED = {PAPER+'.md', PAPER+'.pdf', PAPER+'.docx', 'CITATION.bib', 'LICENSE.md', 'EDITION_AND_SOURCE_NOTE.md', 'PUBLIC_SOURCE_SCOPE.json', 'README.md', 'SHA256SUMS.txt'}
DESC = 'A conceptual research preprint on shared human–AI gameplay, role switching, qualified experience and cross-world evaluation. No empirical result is reported.'
BOUNDARY = 'Conceptual and methodological preprint. No empirical experiment, runtime implementation, independently annotated benchmark, identity-continuity result or economic superiority is reported. English v0.2 has not undergone separate independent peer review. A separate C/B1 comparison is not planned before an actual treatment is specified.'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def exact_write(path: Path, data: bytes) -> None:
    if path.is_symlink() or (path.exists() and path.read_bytes() != data):
        raise ValueError('Refusing to replace different immutable payload: '+str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def unpack(raw: bytes) -> dict[str, bytes]:
    if len(raw) != 301436 or sha(raw) != SHA:
        raise ValueError('Published archive size or SHA-256 mismatch')
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        infos=z.infolist()
        if len(infos)!=9 or {x.filename for x in infos}!=EXPECTED:
            raise ValueError('Unexpected archive members')
        if sum(x.file_size for x in infos)>1000000 or any(x.is_dir() or (x.external_attr>>16)&0o170000==0o120000 for x in infos):
            raise ValueError('Archive exceeds its file/size boundary')
        members={x.filename:z.read(x) for x in infos}
    seen=set()
    for line in members['SHA256SUMS.txt'].decode('utf-8').splitlines():
        digest,name=line.split('  ',1)
        if name in seen or name not in members or sha(members[name])!=digest:
            raise ValueError('Internal manifest mismatch: '+name)
        seen.add(name)
    if seen != EXPECTED-{'SHA256SUMS.txt'}:
        raise ValueError('Incomplete internal manifest')
    if sha(members[PAPER+'.pdf'])!=PDF_SHA:
        raise ValueError('PDF hash mismatch')
    if 'https://creativecommons.org/licenses/by/4.0/' not in members['LICENSE.md'].decode('utf-8'):
        raise ValueError('License mismatch')
    return members


def work_json(abstract: str) -> dict:
    return {
        '@context':'https://schema.org','@type':'ScholarlyArticle',
        '@id':SITE+ROUTE+'#work','name':TITLE,'headline':TITLE,'url':SITE+ROUTE,
        'abstract':abstract,'description':DESC,'datePublished':DATE,'version':'0.2',
        'creativeWorkStatus':'Preprint','inLanguage':'en',
        'author':{'@type':'Person','name':'Ivan Kotov','sameAs':'https://orcid.org/0009-0009-6002-9845'},
        'identifier':{'@type':'PropertyValue','propertyID':'Version DOI','value':DOI,'url':'https://doi.org/'+DOI},
        'sameAs':['https://doi.org/'+DOI,'https://zenodo.org/records/22542470',REPO],
        'isPartOf':{'@type':'CreativeWorkSeries','name':'Project Ester / Advanced Global Intelligence corpus','url':SITE+'/advanced-global-intelligence/'},
        'citation':['https://doi.org/10.5281/zenodo.21751985','https://doi.org/10.5281/zenodo.22085394'],
        'license':'https://creativecommons.org/licenses/by/4.0/',
        'encoding':[{'@type':'MediaObject','encodingFormat':fmt,'contentUrl':SITE+ROUTE+'files/'+name} for fmt,name in [('application/pdf',PAPER+'.pdf'),('text/markdown',PAPER+'.md'),('application/zip',ZIP)]],
    }


def page(abstract: str, work: dict) -> str:
    e=html.escape
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(TITLE)} | Ivan Kotov</title>
<meta name="description" content="{e(DESC)}">
<link rel="canonical" href="{SITE+ROUTE}"><link rel="stylesheet" href="../../styles.css">
<meta property="og:type" content="article"><meta property="og:title" content="{e(TITLE)}"><meta property="og:description" content="{e(DESC)}"><meta property="og:url" content="{SITE+ROUTE}">
<meta name="citation_title" content="{e(TITLE)}"><meta name="citation_author" content="Ivan Kotov">
<meta name="citation_publication_date" content="{DATE}"><meta name="citation_doi" content="{DOI}"><meta name="citation_pdf_url" content="{SITE+ROUTE}files/{PAPER}.pdf">
<script type="application/ld+json">{json.dumps(work,ensure_ascii=False)}</script>
<style>.prose,.section,.section-head{{min-width:0}}.prose a,.hash{{overflow-wrap:anywhere}}.prose pre{{white-space:pre-wrap;overflow-wrap:anywhere;max-width:100%}}.publication-boundary{{border-left:3px solid currentColor;padding-left:1rem}}.hero h1{{overflow-wrap:break-word}}</style>
</head><body><div class="site-shell">
<header class="site-header"><a class="brand" href="../../"><span class="brand-name">Ivan Kotov</span><span class="brand-role">AI Systems Architect</span></a>
<nav class="site-nav" aria-label="Primary"><a href="../../">Home</a><a href="../../start-here/">Start here</a><a href="../" aria-current="page">Publications</a><a href="../../diary/">Diary</a><a href="../../library/">Library</a><a href="../../about/">About</a><a href="../../contact/">Contact</a></nav></header>
<main>
<section class="hero"><p class="eyebrow">Research preprint · English · v0.2 · 6 September 2026</p><h1>Shared Open Worlds for Human–AI Dyads</h1><p class="lead page-lead">Role Switching, Experience Qualification, and Cross-World Continuity Evaluation</p><p>Enjoyment for the human, useful learning for the system: a research proposal for cooperating, competing by agreement, and returning to cooperation across changing game worlds.</p><div class="section-links"><a href="files/{PAPER}.pdf">Read the paper (PDF)</a><a href="https://doi.org/{DOI}">Version DOI</a><a href="files/{ZIP}">Complete public package</a></div></section>
<section class="section"><div class="section-head"><p class="section-label">Publication</p><h2>Abstract</h2></div><div class="prose"><p>{e(abstract)}</p><p><strong>Author:</strong> Ivan Kotov, Independent Researcher, Brussels, Belgium · <a href="https://orcid.org/0009-0009-6002-9845">ORCID 0009-0009-6002-9845</a>.</p><p><strong>Version DOI:</strong> <a href="https://doi.org/{DOI}">{DOI}</a><br><strong>All-versions DOI:</strong> <a href="https://doi.org/{CONCEPT}">{CONCEPT}</a><br><strong>License:</strong> <a href="files/LICENSE.md">CC BY 4.0, within the published package's stated scope</a>.</p></div></section>
<section class="section"><div class="section-head"><p class="section-label">Research focus</p><h2>History, transitions and human value are different questions</h2></div><div class="prose"><p>The paper separates four contrasts: access to permitted episodic history, transition risk relative to matched controls, an explicitly specified state-organization difference, and transfer of a permitted skill to a new task. Human enjoyment and the burden of corrections are assessed separately. Correct permission handling is not by itself learning or enjoyable co-play.</p><p>The candidate uses existing memory and governance primitives. A fully equipped conventional baseline retains the same ordinary safeguards; it is not weakened to manufacture a c-specific result. If no distinct treatment remains, the shared mechanism is adopted as conventional engineering while the history and gameplay questions remain open.</p><p>Five author-constructed illustrations make the rules inspectable: retaining a current grant across a world rollback, retaining a revocation after loading an old save, ending competition without erasing useful memory, limiting skill transfer, and withholding an action when a material basis is unknown. They are explanatory examples, not experimental results or independent gold labels.</p></div></section>
<section class="section"><div class="prose publication-boundary"><h2>Evidence and publication status</h2><p>{e(BOUNDARY)}</p><p>This English edition follows the author-accepted Russian v0.2 and the source-based adjudication of three model reviews of v0.1. The earlier GTA V mod report is retained only as documentary history of the idea, not verified runtime evidence. Prior work on game companions, coordination, memory and relational agents is discussed in the paper; general priority is not claimed.</p></div></section>
<section class="section"><div class="section-head"><p class="section-label">Downloads and citation</p><h2>Exact published files</h2></div><div class="prose"><p><a href="files/{PAPER}.pdf">PDF</a> · <a href="files/{PAPER}.md">Markdown</a> · <a href="files/{PAPER}.docx">DOCX</a> · <a href="files/{ZIP}">Public ZIP</a></p><p><a href="publication.json">DOI-bound publication metadata</a> · <a href="citation.bib">Citation with the published DOI</a> · <a href="files/SHA256SUMS.txt">Original package checksums</a> · <a href="files/{ZIP}.sha256">Archive checksum</a></p><p class="hash"><strong>Public ZIP SHA-256:</strong> <code>{SHA}</code></p><p>The paper, archive and all nine original members are unchanged. New DOI metadata and this navigation page are additive records outside the deposited package. No internal reviews, private Drive locators or personal memories are published here.</p><p>Kotov, I. (2026). <em>{e(TITLE)}</em> (Version 0.2). Zenodo. <a href="https://doi.org/{DOI}">https://doi.org/{DOI}</a></p><p><a href="{REPO}">Commit-pinned GitHub publication mirror</a> · <a href="https://zenodo.org/records/22542470">Zenodo record</a></p></div></section>
<section class="section"><div class="section-head"><p class="section-label">Within the corpus</p><h2>Roles, provenance and current permissions</h2></div><div class="prose"><p><a href="../ai-social-role-separation-memory-custody-v1-0/">Social roles and memory custody</a> delimit the use of shared history. Historical-versus-operative state separates a remembered permission from one that applies now. Experience qualification and raw-locality rules distinguish learning from permission to transmit or train on a record.</p><p>A simulator save may restore a virtual crane position. It cannot restore an operator's revoked authorization. Correct interlocks, a learned skill and a useful human experience therefore remain separate evaluation targets.</p><p><strong>Related citations:</strong> <a href="https://doi.org/10.5281/zenodo.21751985">AI Social Roles and Memory Custody</a>; <a href="https://doi.org/10.5281/zenodo.22085394">World 8 / Z0-A</a> (external prior art, not coauthorship or endorsement).</p><p><a href="../../temporal-ai-presence/">Temporal AI Presence</a> · <a href="../../corpus-map/">Corpus map</a> · <a href="https://github.com/Kot141078/advanced-global-intelligence">AGI repository</a> · <a href="../">All publications</a></p></div></section>
</main><footer class="site-footer"><p>Ivan Kotov · <a href="../">Publications</a> · <a href="../../contact/">Contact</a></p></footer>
</div></body></html>
'''


def integrate(root: Path, raw: bytes, members: dict[str, bytes]) -> None:
    dest=root/ROUTE.strip('/')
    if (dest/'index.html').exists():
        raise ValueError('Publication page already exists; do not overwrite another integration')
    text=members[PAPER+'.md'].decode('utf-8')
    abstract=text.split('### Abstract\n\n',1)[1].split('\n\n**Keywords:',1)[0]
    if not abstract or len(abstract)>5000:
        raise ValueError('Abstract extraction boundary failure')
    for name,data in members.items():
        exact_write(dest/'files'/name,data)
    exact_write(dest/'files'/ZIP,raw)
    exact_write(dest/'files'/(ZIP+'.sha256'),(SHA+'  '+ZIP+'\n').encode())
    work=work_json(abstract)
    exact_write(dest/'index.html',page(abstract,work).encode())
    write_json(dest/'publication.json',{'id':SLUG,'title':TITLE,'version':'0.2','publication_date':DATE,'version_doi':DOI,'concept_doi':CONCEPT,'license':'CC-BY-4.0','canonical_url':SITE+ROUTE,'github':REPO,'source_commit':PIN,'status':'published_preprint','evidence_boundary':BOUNDARY,'archive_sha256':SHA,'archive_bytes':len(raw),'artifact_mutations':0})
    exact_write(dest/'citation.bib',f'@misc{{kotov2026sharedopenworlds,\n  author = {{Kotov, Ivan}},\n  title = {{{TITLE}}},\n  year = {{2026}},\n  version = {{0.2}},\n  publisher = {{Zenodo}},\n  doi = {{{DOI}}},\n  url = {{https://doi.org/{DOI}}}\n}}\n'.encode())
    listing=root/'publications/index.html'
    current=listing.read_text(encoding='utf-8')
    if SLUG in current:
        raise ValueError('Publication listing already contains this work')
    main=current.index('<main>')
    hero=current.index('<section class="hero">',main)
    insert=current.index('</section>',hero)+len('</section>')
    card=f'''\n\n<!-- ACOW-V0-2:BEGIN -->
<section class="section" id="{SLUG}"><div class="section-head"><p class="section-label">Published research preprint · 6 September 2026</p><h2>Shared Open Worlds for Human–AI Dyads</h2></div><div class="card-grid"><article class="card"><p class="eyebrow">English · v0.2 · CC BY 4.0</p><h3>Co-play, role switching and cross-world history</h3><p>A research proposal for a person and a long-lived candidate AI line cooperating, competing by agreement and returning to joint activity. Shared-history utility, useful learning and human enjoyment remain distinct from correct permission handling.</p><p class="status-note">Conceptual and methodological preprint. No empirical experiment or runtime implementation; five author-constructed illustrations are not an independently annotated benchmark.</p><div class="section-links"><a href="{SLUG}/">Publication page</a><a href="https://doi.org/{DOI}">Version DOI</a><a href="{SLUG}/files/{PAPER}.pdf">English PDF</a><a href="{SLUG}/files/{ZIP}">Public package</a><a href="{REPO}">GitHub source</a></div></article></div></section>
<!-- ACOW-V0-2:END -->\n'''
    current=current[:insert]+card+current[insert:]
    pattern=re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)',re.S)
    changed=0
    def update_ld(match):
        nonlocal changed
        data=json.loads(match.group(2))
        for item in data.get('@graph',[]):
            if item.get('@id')==SITE+'/publications/#works':
                entries=item['itemListElement']
                entries.insert(0,{'@type':'ListItem','position':1,'item':{k:v for k,v in work.items() if k!='@context'}})
                for pos,entry in enumerate(entries,1): entry['position']=pos
                changed+=1
                return match.group(1)+'\n'+json.dumps(data,ensure_ascii=False,indent=2)+'\n'+match.group(3)
        return match.group(0)
    current=pattern.sub(update_ld,current)
    if changed!=1:
        raise ValueError('Expected exactly one publication ItemList')
    listing.write_text(current,encoding='utf-8')
    index_path=root/'works-index.json'
    index=json.loads(index_path.read_text(encoding='utf-8'))
    if any(x.get('id')==SLUG for x in index['works']):
        raise ValueError('Work is already registered')
    index['works'].insert(0,{'id':SLUG,'title':TITLE,'type':'research_paper','subtype':'preprint','role':'conceptual human–AI co-play and cross-world evaluation proposal','primary_url':SITE+ROUTE,'github':REPO,'commit':PIN,'date':DATE,'version':'0.2','version_doi':DOI,'concept_doi':CONCEPT,'doi_role':'version','status':'published_preprint','languages':['en'],'license':'CC BY 4.0','summary':DESC,'archive_url':SITE+ROUTE+'files/'+ZIP,'archive_sha256':SHA,'manifest_url':SITE+ROUTE+'files/SHA256SUMS.txt','sha256sums_url':SITE+ROUTE+'files/'+ZIP+'.sha256','canonical_artifacts':[{'format':'PDF','filename':PAPER+'.pdf','media_type':'application/pdf','sha256':PDF_SHA,'url':SITE+ROUTE+'files/'+PAPER+'.pdf'}],'related_dois':['10.5281/zenodo.21751985','10.5281/zenodo.22085394'],'non_claims':['no empirical experiment or runtime implementation','not independently peer reviewed in English v0.2','no independently annotated benchmark','no distinct C/B1 treatment established','no identity-continuity, consciousness, new-AI-class or economic-superiority result']})
    write_json(index_path,index)
    sitemap=root/'sitemap.xml'
    current=sitemap.read_text(encoding='utf-8')
    if SITE+ROUTE in current or current.count('</urlset>')!=1:
        raise ValueError('Unexpected sitemap or duplicate route')
    sitemap.write_text(current.replace('</urlset>',f'  <url><loc>{SITE+ROUTE}</loc><lastmod>{DATE}</lastmod></url>\n</urlset>'),encoding='utf-8')
    for name in ['llms.txt','llms-full.txt']:
        p=root/name
        current=p.read_text(encoding='utf-8')
        if SITE+ROUTE in current:
            raise ValueError('Duplicate machine-reading route')
        p.write_text(current+f'\n## Shared Open Worlds for Human–AI Dyads — v0.2\n\n- {SITE+ROUTE}\n- Version DOI: https://doi.org/{DOI}\n- Exact repository mirror: {REPO}\nConceptual English preprint, CC BY 4.0. Shared-history utility, role switching, experience qualification and human enjoyment; no empirical game result, independently annotated benchmark or distinct C/B1 treatment.\n',encoding='utf-8')
    for name,data in members.items():
        if (dest/'files'/name).read_bytes()!=data:
            raise ValueError('Payload changed during site integration')
    write_json(root/'evidence/acow-publication-20260906/BUILD_RECEIPT.json',{'status':'STATIC_INTEGRATION_BUILT_GATE_PENDING','source_commit':PIN,'version_doi':DOI,'archive_sha256':SHA,'archive_bytes':len(raw),'members':9,'checksum_rows':8,'deposited_payload_mutations':0,'canonical_page':SITE+ROUTE,'full_site_gate':'NOT_YET_RUN','live_deployment':'NOT_YET_VERIFIED'})


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--local-zip',type=Path)
    args=parser.parse_args()
    if args.local_zip:
        raw=args.local_zip.read_bytes()
    else:
        req=urllib.request.Request(RAW+ZIP,headers={'User-Agent':'Kotov-ACOW-Site-Publisher/0.2'})
        with urllib.request.urlopen(req,timeout=90) as response:
            if response.status!=200: raise ValueError('Source HTTP status')
            raw=response.read(301437)
    integrate(args.root,raw,unpack(raw))
    print('PASS scoped static ACOW integration; full existing site gate remains mandatory')

if __name__=='__main__':
    try:
        main()
    except (OSError,ValueError,KeyError,IndexError,UnicodeError,zipfile.BadZipFile) as error:
        print('FAIL: '+str(error),file=sys.stderr)
        raise SystemExit(2)
