#!/usr/bin/env python3
"""Publish one verified correction bundle and update existing static-site entry points.

No old DOI payload, historical PDF, source snapshot or publication identifier is
replaced. Network input is one exact commit-pinned archive, checked by SHA-256.
"""
from __future__ import annotations
import hashlib
import html
import io
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://ivankotov.eu'
SLUG = 'scientific-corrections-v1-0'
ROUTE = '/publications/' + SLUG + '/'
PAGE = ROOT / ROUTE.strip('/')
PIN = '78bce9419de6006a21fdfd8fcf1aee35c383205c'
BUNDLE = 'SCIENTIFIC_CORRIGENDA_HARDENING_v1_0.zip'
SHA = 'ca1e741f7d4f2dbf76a4a66fed7a5d83cf37e599e0fc4552bbca5aaa59b4ffde'
SOURCE = f'https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/{PIN}/hardening/{BUNDLE}'
GITHUB = f'https://github.com/Kot141078/advanced-global-intelligence/tree/{PIN}/hardening/scientific_corrigenda_v1_0'
TITLE = 'Scientific Corrigenda and Regression Hardening for ARQ M2, MOT-c and C-Calculus'
DATE = '2026-09-05'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_write(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def place_exact(path: Path, data: bytes) -> None:
    if path.is_symlink() or (path.exists() and path.read_bytes() != data):
        raise ValueError(f'Refusing to overwrite different correction payload: {path}')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def acquire() -> dict[str, bytes]:
    req = urllib.request.Request(SOURCE, headers={'User-Agent': 'Kotov-Corrigendum-Publisher/1.0'})
    with urllib.request.urlopen(req, timeout=90) as response:
        raw = response.read(5000001)
    if len(raw) > 5000000 or sha(raw) != SHA:
        raise ValueError('CORRECTION_ARCHIVE_HASH_MISMATCH')
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        if len(z.infolist()) > 100 or sum(x.file_size for x in z.infolist()) > 20000000:
            raise ValueError('Archive exceeds declared bounded package size')
        members = {}
        for info in z.infolist():
            parts = PurePosixPath(info.filename).parts
            if len(parts) < 2 or parts[0] != 'SCIENTIFIC_CORRIGENDA_HARDENING_v1_0' or '..' in parts or info.filename.startswith('/'):
                raise ValueError('Unsafe or unexpected archive member')
            name = '/'.join(parts[1:])
            if name in members or (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError('Duplicate or symlink archive member')
            members[name] = z.read(info)
    checks = members['SHA256SUMS.txt'].decode('utf-8').splitlines()
    checked = set()
    for line in checks:
        expected, name = line.split('  ', 1)
        if name in checked or name not in members or sha(members[name]) != expected:
            raise ValueError(f'Internal manifest mismatch: {name}')
        checked.add(name)
    if checked != set(members) - {'SHA256SUMS.txt'}:
        raise ValueError('Incomplete internal manifest')
    for name, data in members.items():
        place_exact(PAGE / 'files' / name, data)
    place_exact(PAGE / 'files' / BUNDLE, raw)
    place_exact(PAGE / 'files' / (BUNDLE + '.sha256'), f'{SHA}  {BUNDLE}\n'.encode())
    return members


def page_html(members: dict[str, bytes]) -> str:
    downloads = []
    for name in sorted(members):
        if not name.startswith('publication/') or not name.endswith('.pdf'):
            continue
        label = Path(name).stem.replace('_CORRECTED_20260905', '').replace('_', ' ')
        downloads.append(f'<li><a href="files/{html.escape(name)}">{html.escape(label)}</a></li>')
    work = {'@context': 'https://schema.org', '@type': 'TechArticle',
        'name': TITLE, 'url': SITE + ROUTE, 'datePublished': DATE, 'version': '1.0',
        'inLanguage': ['en', 'ru'], 'author': {'@type': 'Person', 'name': 'Ivan Kotov',
            'sameAs': 'https://orcid.org/0009-0009-6002-9845'},
        'license': 'https://creativecommons.org/licenses/by/4.0/',
        'description': 'Author-issued scientific correction supplement with four corrected reading editions, source-bound patches and focused first-party regression tests. No DOI for this supplement is assigned yet.',
        'isBasedOn': ['https://doi.org/10.5281/zenodo.22060517', 'https://doi.org/10.5281/zenodo.21205427',
                     'https://github.com/Kot141078/sovereign-entity-recursion/blob/94dcab585b5c179cf4f4e0da4ebf63261c7fb984/protocol/arq/v0.2/ARQ_System_Models_and_Assumptions_v0.2.md'],
        'encoding': [{'@type': 'MediaObject', 'encodingFormat': 'application/zip', 'contentUrl': SITE + ROUTE + 'files/' + BUNDLE}]}
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} | Ivan Kotov</title>
<meta name="description" content="Author-issued corrections to ARQ M2, the EN/RU MOT-c examples and C-Calculus relation semantics. Full corrected editions, exact source hashes and 29 focused regression tests.">
<link rel="canonical" href="{SITE + ROUTE}">
<link rel="stylesheet" href="../../styles.css">
<meta property="og:type" content="article">
<meta property="og:title" content="{TITLE}">
<meta property="og:url" content="{SITE + ROUTE}">
<meta name="citation_title" content="{TITLE}">
<meta name="citation_author" content="Ivan Kotov">
<meta name="citation_publication_date" content="2026-09-05">
<meta name="citation_pdf_url" content="{SITE + ROUTE}files/publication/CORRIGENDUM_EN.pdf">
<script type="application/ld+json">{json.dumps(work, ensure_ascii=False)}</script>
<style>.prose,.section,.section-head{{min-width:0}} .prose a,.hash{{overflow-wrap:anywhere}} .correction-notice{{border-left:4px solid currentColor;padding-left:1rem}} .prose pre{{white-space:pre-wrap;overflow-wrap:anywhere;max-width:100%}}</style>
</head>
<body><div class="site-shell">
<header class="site-header"><a class="brand" href="../../"><span class="brand-name">Ivan Kotov</span><span class="brand-role">AI Systems Architect</span></a>
<nav class="site-nav" aria-label="Primary"><a href="../../">Home</a><a href="../../start-here/">Start here</a><a href="../" aria-current="page">Publications</a><a href="../../diary/">Diary</a><a href="../../library/">Library</a><a href="../../about/">About</a><a href="../../contact/">Contact</a></nav></header>
<main>
<section class="hero"><p class="eyebrow">Scientific corrigendum / reproducible hardening / bilingual</p><h1>Scientific Corrigenda and Regression Hardening</h1><p class="lead page-lead">ARQ M2, MOT-c and C-Calculus. Version 1.0, 5 September 2026.</p></section>
<section class="section"><div class="prose correction-notice"><h2>Corrected editions, preserved history</h2>
<p>This author-issued supplement corrects three scientific-document families. It includes four complete corrected reading editions, their PDF projections, unchanged source snapshots, exact edits and 29 focused first-party regression tests.</p>
<p><strong>The earlier DOI files and release identifiers remain unchanged.</strong> This is not a complete new version of either parent compound package. A Zenodo DOI for this correction supplement has not yet been assigned.</p>
<p><strong>Author:</strong> Ivan Kotov · <a href="https://orcid.org/0009-0009-6002-9845">ORCID 0009-0009-6002-9845</a>. New explanatory text: CC BY 4.0; new maintenance code: MIT; reproduced sources retain their original attribution and licenses.</p>
</div></section>
<section class="section"><div class="section-head"><p class="section-label">Corrections</p><h2>What changed</h2></div><div class="prose">
<h3>ARQ M2: initial state and resource accounting</h3><p>The retention expression now includes the initial retained state. The irreversibility term is divided by its positive minimum per-commit cost. Each included budget term must constrain the same counted set; finite rewritable storage is not a lifetime update-count limit.</p>
<h3>MOT-c: LATENT in the English and Russian examples</h3><p>Appendix A now represents all fifteen lifecycle states. The separate machine schema already included LATENT and has not been changed. LATENT is not suspension, abandonment or archiving.</p>
<h3>C-Calculus: relation types and finite traces</h3><p>Snapshot equivalence, lineage, directed continuation and threshold resemblance are not all mathematical equivalence relations. The observed-adjacency denominator now explicitly excludes the terminal event without a successor. Hard guards, unknown-value handling and admission algorithms are unchanged.</p>
<h3>Two accompanying clarifications</h3><p>O12 remains assigned to corpus-control; Personality Formation receives O13 in the text and machine index. The bounded-summary substitution test measures replacement/compression costs, not a formation-path effect under unproved information parity.</p>
</div></section>
<section class="section"><div class="section-head"><p class="section-label">Download</p><h2>Complete correction package</h2></div><div class="prose">
<p><a href="files/{BUNDLE}">Complete ZIP: corrected documents, PDFs, sources and checks</a> · <a href="files/{BUNDLE}.sha256">ZIP SHA-256</a></p>
<p class="hash"><strong>Archive SHA-256:</strong> <code>{SHA}</code></p>
<ul>{''.join(downloads)}</ul>
<p><a href="files/CORRIGENDUM_EN.md">English Markdown corrigendum</a> · <a href="files/CORRIGENDUM_RU.md">Русская ведомость исправлений</a> · <a href="files/SOURCE_BINDINGS.json">Exact source bindings</a> · <a href="files/patches/corrections.json">Literal edits</a> · <a href="files/evidence/REGRESSION_TESTS.txt">Regression test output</a></p>
<p><a href="{GITHUB}">Commit-pinned public repository package</a> · <a href="https://github.com/Kot141078/sovereign-entity-recursion/blob/5132db5c3119fe070182e9e975600304e60f7f4c/protocol/arq/corrections/20260905/README.md">SER-owned ARQ correction notice</a></p>
</div></section>
<section class="section"><div class="section-head"><p class="section-label">Source and claim boundary</p><h2>What the checks establish</h2></div><div class="prose">
<p>The final build obtained exact commit-pinned public GitHub source bytes and matched their recorded sizes and SHA-256 values. Full Zenodo deposit archives were not retrieved in this correction exercise. Exact ARQ M2 membership in a particular deposit remains unresolved; the c[q] addendum DOI is not substituted.</p>
<p>These are first-party document and example regressions, not independent scientific peer review, production runtime validation, a native 07c checker result or a c-versus-baseline experiment. No new consciousness, identity, same-c continuity, safety certification, c-specific effect or economic-value result is claimed.</p>
<p>Historical works: <a href="../motivational-formation-c-v0-1/">MOT-c v0.1</a> · <a href="../ccalc-full-stack-v0-1/">C-Calculus full stack v0.1</a> · <a href="../origin-neutral-recognition-provisional-care-v0-1/">Origin-Neutral Recognition note</a>. Cite their old versions for historical wording and this supplement for the corrections.</p>
</div></section>
<section class="section" lang="ru"><div class="section-head"><p class="section-label">По-русски</p><h2>Что исправлено</h2></div><div class="prose">
<p>В ARQ восстановлено начальное состояние и согласованы единицы бюджета. В обоих приложениях MOT-c возвращено существующее состояние LATENT; правильная машинная схема не менялась. В C-Calculus разведены разные математические отношения и уточнён учёт конечной трассы.</p>
<p>Это прозрачное исправление опубликованного корпуса, а не переписывание прошлого. Старые DOI и их файлы сохранены. Архив содержит полные исправленные тексты и PDF, а не только список замечаний. Новый DOI дополнения пока не назначен.</p>
<p>На стройке новая редакция чертежа не меняет задним числом старый акт осмотра. Здесь тот же принцип: точная старая версия, явная поправка, проверяемый новый файл.</p>
</div></section>
</main><footer class="site-footer"><p>Ivan Kotov · <a href="../../publications/">Publications</a> · <a href="../../contact/">Contact</a></p></footer>
</div></body></html>
'''


def add_notice(path: Path, body: str) -> None:
    text = path.read_text(encoding='utf-8')
    marker = '<!-- SCIENTIFIC-CORRECTION-20260905 -->'
    if marker in text:
        return
    if text.count('<main>') != 1:
        raise ValueError(f'Ambiguous main element: {path}')
    notice = f'\n{marker}\n<section class="section" aria-label="Scientific correction"><div class="prose"><h2>Scientific correction · 5 September 2026</h2><p>{body}</p><p><a href="{ROUTE}">Read the corrigendum and full corrected editions</a>. Historical DOI files and citation metadata remain unchanged.</p></div></section>\n'
    path.write_text(text.replace('<main>', '<main>' + notice, 1), encoding='utf-8')


def main() -> None:
    members = acquire()
    (PAGE / 'index.html').write_text(page_html(members), encoding='utf-8')
    notices = {
      'motivational-formation-c-v0-1': 'Appendix A in both languages omitted LATENT. The corrected examples align with the existing fifteen-state lifecycle; the machine schema was already correct and is unchanged.',
      'ccalc-full-stack-v0-1': 'Document 04 sections 18 and 21 now distinguish relation types and specify finite observed-adjacency counting. Hard invariants, admission algorithms and historical component evidence are unchanged.',
      'origin-neutral-recognition-provisional-care-v0-1': 'Section 10 uses a bounded-summary control. Interpret its result as replacement/compression cost unless relevant information parity and the strong matched baseline are independently established. No new experimental result is reported.'}
    for slug, text in notices.items():
        add_notice(ROOT / 'publications' / slug / 'index.html', text)
    add_notice(ROOT / 'publications/index.html', 'A source-bound corrigendum and regression-hardening supplement is available for ARQ M2, MOT-c and C-Calculus.')
    index_path = ROOT / 'works-index.json'
    index = json.loads(index_path.read_text(encoding='utf-8'))
    if any(x['id'] == SLUG for x in index['works']):
        raise ValueError('Correction work already registered; do not overwrite it')
    artifacts = []
    for name in sorted(members):
        if name.startswith('publication/') and name.endswith('.pdf'):
            artifacts.append({'format': 'PDF', 'filename': name, 'media_type': 'application/pdf',
                'sha256': sha(members[name]), 'url': SITE + ROUTE + 'files/' + name})
    entry = {'id': SLUG, 'title': TITLE, 'type': 'publication', 'subtype': 'scientific_corrigendum',
        'role': 'source-bound scientific corrections and reproducible document regression hardening',
        'primary_url': SITE + ROUTE, 'github': GITHUB, 'commit': PIN, 'date': DATE, 'version': '1.0',
        'status': 'published_repository_correction_zenodo_deposit_pending', 'languages': ['en', 'ru'],
        'license': 'CC BY 4.0; source material retains original licenses', 'license_code': 'MIT',
        'summary': 'Corrections to ARQ M2 initial-state and resource-accounting formulas, EN/RU MOT-c Appendix A LATENT examples and C-Calculus relation taxonomy/finite adjacency. Four complete corrected reading editions and 29 focused first-party tests.',
        'archive_url': SITE + ROUTE + 'files/' + BUNDLE, 'archive_sha256': SHA,
        'manifest_url': SITE + ROUTE + 'files/SHA256SUMS.txt',
        'sha256sums_url': SITE + ROUTE + 'files/' + BUNDLE + '.sha256',
        'canonical_artifacts': artifacts,
        'non_claims': ['not a complete replacement of the parent compound releases',
            'no new DOI assigned yet', 'not independent scientific peer review', 'not deployed runtime validation',
            'no c-specific effect, identity, consciousness or economic-value result']}
    index['works'].insert(0, entry)
    for record in index['works']:
        if record['id'] in notices:
            record['correction_url'] = SITE + ROUTE
            record['correction_date'] = DATE
    json_write(index_path, index)
    sitemap = ROOT / 'sitemap.xml'
    text = sitemap.read_text(encoding='utf-8')
    if SITE + ROUTE not in text:
        if text.count('</urlset>') != 1:
            raise ValueError('Unexpected sitemap shape')
        text = text.replace('</urlset>', f'  <url><loc>{SITE + ROUTE}</loc><lastmod>{DATE}</lastmod></url>\n</urlset>')
        sitemap.write_text(text, encoding='utf-8')
    for name in ['llms.txt', 'llms-full.txt']:
        path = ROOT / name; text = path.read_text(encoding='utf-8')
        if SITE + ROUTE not in text:
            path.write_text(text + f'\n## Scientific corrections — 5 September 2026\n\n- {SITE + ROUTE}\nSource-bound ARQ M2, MOT-c and C-Calculus corrigendum, corrected reading editions and regression checks. Historical DOI payloads retained; the correction supplement has no DOI assigned yet.\n', encoding='utf-8')
    subprocess.run([sys.executable, str(ROOT / 'tools/build_machine_layer.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'tools/check_machine_readability.py')], check=True)
    import check_machine_readability as check
    for name in ['index.html', *[f'../{s}/index.html' for s in notices]]:
        p = PAGE / name
        parser = check.PageParser(); parser.feed(p.read_text(encoding='utf-8'))
        if not parser.doctype or parser.h1_count != 1 or not parser.canonicals:
            raise ValueError('Invalid publication HTML structure')
    receipt = {'status': 'PASS_STATIC_CORRECTION_PUBLICATION_BUILD', 'source_commit': PIN,
        'archive_sha256': SHA, 'archive_bytes': len((PAGE/'files'/BUNDLE).read_bytes()),
        'internal_manifest_entries': len(members)-1, 'old_doi_payload_changes': 0,
        'site_machine_generator': 'existing tools/build_machine_layer.py',
        'site_checks': 'existing tools/check_machine_readability.py',
        'new_page': SITE + ROUTE, 'live_deployment_verified': False}
    out = ROOT / 'evidence/scientific-corrections-20260905'; out.mkdir(parents=True, exist_ok=True)
    json_write(out / 'BUILD_RECEIPT.json', receipt)
    print(json.dumps(receipt, indent=2))

if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, UnicodeError, zipfile.BadZipFile, subprocess.SubprocessError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        raise SystemExit(2)
