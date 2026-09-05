#!/usr/bin/env python3
"""Bounded build of the author-authorized correction supplement.
Uses exact public source pins. Never alters historical DOI payloads or tags.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import urllib.request
import zipfile
ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
AGI_PIN = '77cdc6632d7385ba3be374d257b833ab4790f935'
PREFIX = 'https://raw.githubusercontent.com/Kot141078/'

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def read_public(url: str, maximum: int = 2000000) -> bytes:
    if not url.startswith(PREFIX) or '/main/' in url or '/master/' in url:
        raise ValueError('Only exact pinned public source URLs are permitted')
    req = urllib.request.Request(url, headers={'User-Agent':'Kotov-Scientific-Corrigenda/1.0'})
    with urllib.request.urlopen(req, timeout=90) as response:
        data = response.read(maximum + 1)
    if len(data) > maximum:
        raise ValueError('Source exceeds bounded read size')
    return data

def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def prepare_sources(spec: dict) -> None:
    folder = ROOT / 'source_snapshots'; folder.mkdir(exist_ok=True)
    for binding in spec['source_bindings']:
        name = binding['filename']
        url = binding['source_url'].replace('https://github.com/', 'https://raw.githubusercontent.com/').replace('/blob/', '/')
        data = read_public(url)
        if digest(data) != binding['sha256'] or len(data) != binding['size_bytes']:
            raise ValueError(f'SOURCE_MISMATCH: {name}')
        target = folder / name
        if target.exists() and target.read_bytes() != data:
            raise ValueError(f'Refusing to replace a different source snapshot: {name}')
        target.write_bytes(data)
    write_json(ROOT / 'SOURCE_BINDINGS.json', spec['source_bindings'])

def prepare_figures() -> None:
    import fitz
    out = ROOT / 'reading_editions/figures'; out.mkdir(parents=True, exist_ok=True)
    records = []
    for language, expected, refs in [
        ('EN','2346fb43875e7fb137ef7408126ff5cf3f66c02099c8d0d293089d136318801b',[420,422,424]),
        ('RU','4a50e6a8d8444b7960715ae4035d3e5ad6fe58c21000066d48f4d45f880384a5',[427,429,431])]:
        basename = f'MOT_c_Foundation_Theory_v0_1_{language}.pdf'
        url = PREFIX + f'advanced-global-intelligence/{AGI_PIN}/publications/motivational-formation-c-v0-1/release/{basename}'
        raw = read_public(url)
        if digest(raw) != expected:
            raise ValueError('MOT_PDF_SOURCE_MISMATCH')
        with fitz.open(stream=raw, filetype='pdf') as doc:
            for stem, xref in zip(['formation_cycle','motivational_field','privacy_witness_boundary'],refs):
                name = f'mot_c_{stem}_{language.lower()}.png'
                fitz.Pixmap(doc,xref).save(out/name)
                records.append({'figure':name,'source_pdf':basename,'source_url':url,
                    'source_pdf_sha256':expected,'embedded_xref':xref,
                    'png_sha256':digest((out/name).read_bytes()),
                    'qualification':'embedded source-PDF image re-encoded as PNG; not original PNG-byte identity'})
    write_json(ROOT / 'evidence/FIGURE_PROVENANCE.json', records)

def current_navigation() -> None:
    mdpath = REPO / 'CANONICAL_OWNERSHIP_AND_BOUNDARIES.md'
    jpath = REPO / 'CANONICAL_OWNERSHIP_AND_BOUNDARIES.json'
    md = mdpath.read_text(encoding='utf-8')
    old = '| `O12` | Personality Formation and Time-Shaped Continuity Profile v0.1 |'
    new = old.replace('`O12`','`O13`',1)
    if md.count(old) == 1 and md.count(new) == 0:
        md = md.replace(old,new,1)
    elif md.count(old) != 0 or md.count(new) != 1:
        raise ValueError('OWNERSHIP_SOURCE_CHANGED')
    marker = '## Ownership ID correction — 5 September 2026'
    if marker not in md:
        md += '\n'+marker+'\n\nO12 remains corpus-control, its meaning before the Personality Formation insertion. Personality Formation is O13. Historical O12 references require the source revision and row title; no blanket redirect applies. The independent O12 objection number is unchanged. See `hardening/scientific_corrigenda_v1_0/CORRIGENDUM_EN.md`.\n'
    obj = json.loads(jpath.read_text(encoding='utf-8'))
    entries = obj['entries']
    found = [x for x in entries if x['id']=='O12']
    if len(found)!=1 or not found[0]['layer'].startswith('corpus-control'):
        raise ValueError('HISTORICAL_O12_OWNER_MISMATCH')
    entry = {'id':'O13','layer':'Personality Formation and Time-Shaped Continuity Profile v0.1',
        'canonical_home_repo':'advanced-global-intelligence',
        'adjacent_repos':['sovereign-entity-recursion','ester-reality-bound','ester-clean-code'],
        'allowed_non_owner_role':['pointer','contextual mention','implementation or review bridge'],
        'disallowed_drift':'adjacent repos presenting personality formation as local authority, consciousness proof, or legal status grant',
        'read_next':['protocols/personality/personality_formation_time_shaped_continuity_v0_1/README.md']}
    existing = [x for x in entries if x['id']=='O13']
    if not existing:
        entries.append(entry)
    elif existing != [entry]:
        raise ValueError('O13_ALREADY_ASSIGNED_DIFFERENTLY')
    ids = re.findall(r'^\| `(O\d+)` \|',md,re.M)
    if len(ids)!=len(set(ids)) or set(ids)!={x['id'] for x in entries}:
        raise ValueError('OWNERSHIP_MD_JSON_MISMATCH')
    obj['date']='2026-09-05'
    mdpath.write_text(md,encoding='utf-8'); write_json(jpath,obj)
    notices = {
      'publications/motivational-formation-c-v0-1/README.md':
        'The Appendix A example in both Foundation Theory languages omitted LATENT. The machine JSON schema already contains LATENT and is unchanged. Read the corrected editions and SC-02; the old DOI payload remains the historical release.',
      'publications/ccalc-full-stack-v0-1/README.md':
        'Document 04 sections 18 and 21 have a finite-adjacency and relation-taxonomy correction. Admission algorithms and the historical component archives are unchanged. Read the corrected edition and SC-03.',
      'protocols/recognition/origin_neutral_recognition_and_provisional_care_v0_1/README.md':
        'Interpret section 10 with SC-05: a bounded-summary control measures replacement/compression cost and does not by itself establish information parity or a formation-path residual. The clarification reports no new experiment.'}
    for name, text in notices.items():
        path = REPO/name
        if not path.is_file():
            raise ValueError(f'Missing expected public entry: {name}')
        contents = path.read_text(encoding='utf-8')
        marker='## Scientific correction — 5 September 2026'
        if marker not in contents:
            contents+='\n'+marker+'\n\n'+text+'\n\n[Scientific Corrigenda and Regression Hardening v1.0](https://github.com/Kot141078/advanced-global-intelligence/tree/main/hardening/scientific_corrigenda_v1_0).\n'
            path.write_text(contents,encoding='utf-8')
    write_json(ROOT/'evidence/OWNERSHIP_CHECK.json',{'status':'PASS','md_ids':ids,
      'json_ids':[x['id'] for x in entries], 'old_O12_owner_retained':True,
      'history_before_insertion':'7bb19aa6d9c2606f8e9366ba009ab74cef9fc5d5',
      'unrelated_objection_numbers_modified':False})

def finalize() -> None:
    import fitz
    boundary=[]
    for p in sorted((ROOT/'publication').glob('*.pdf')):
        with fitz.open(p) as doc:
            violations=[]
            for i,page in enumerate(doc):
                for block in page.get_text('dict')['blocks']:
                    for line in block.get('lines',[]):
                        for span in line.get('spans',[]):
                            a,b,c,d=span['bbox']
                            if a<5 or b<5 or c>page.rect.width-5 or d>page.rect.height-5:
                                violations.append({'page':i+1,'text':span['text'][:80]})
            boundary.append({'pdf':p.name,'pages':len(doc),'page_boundary_outliers':violations})
            if violations:
                raise ValueError(f'PDF_BOUNDARY_FAILURE: {p.name}')
    write_json(ROOT/'evidence/PDF_GEOMETRY_CHECK.json',boundary)
    write_json(ROOT/'evidence/BUILD_SCOPE.json',{'source_download':'exact pinned public GitHub bytes',
       'direct_zenodo_archive_downloads':0,'native_runtime_tests':0,'subject_model_runs':0,
       'independent_scientific_review':False,'old_publication_payload_mutations':0})
    rows=[]
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts and p.name!='SHA256SUMS.txt':
            rows.append(f'{digest(p.read_bytes())}  {p.relative_to(ROOT).as_posix()}')
    (ROOT/'SHA256SUMS.txt').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    archive=ROOT.parent/'SCIENTIFIC_CORRIGENDA_HARDENING_v1_0.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts:
                info=zipfile.ZipInfo('SCIENTIFIC_CORRIGENDA_HARDENING_v1_0/'+p.relative_to(ROOT).as_posix(),(2026,9,5,0,0,0))
                info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=0o100644<<16
                z.writestr(info,p.read_bytes())
    archive.with_suffix('.zip.sha256').write_text(f'{digest(archive.read_bytes())}  {archive.name}\n',encoding='utf-8')

def main() -> None:
    spec=json.loads((ROOT/'patches/corrections.json').read_text(encoding='utf-8'))
    prepare_sources(spec)
    module_spec=importlib.util.spec_from_file_location('apply_corrections',ROOT/'tools/apply_corrections.py')
    patcher=importlib.util.module_from_spec(module_spec); module_spec.loader.exec_module(patcher)
    output=ROOT/'reading_editions'
    if output.exists():
        for b in spec['source_bindings']:
            target=output/patcher.corrected_name(b['filename'])
            expected=patcher.apply_text((ROOT/'source_snapshots'/b['filename']).read_bytes(),b['filename'],spec)
            if not target.is_file() or target.read_bytes()!=expected:
                raise ValueError('Existing reading edition differs; stop, do not overwrite')
    else:
        patcher.build(ROOT/'source_snapshots',output,spec)
    prepare_figures()
    log=subprocess.run([sys.executable,str(ROOT/'tools/test_regressions.py')],capture_output=True)
    (ROOT/'evidence/REGRESSION_TESTS.txt').write_bytes(log.stdout+log.stderr)
    if log.returncode:
        raise ValueError('Document regression failed')
    subprocess.run([sys.executable,str(ROOT/'tools/build_pdfs.py')],check=True)
    current_navigation(); finalize()
    print('CORRECTION_BUILD_COMPLETE; historical DOI payloads unchanged')

if __name__=='__main__':
    try:
        main()
    except (OSError,ValueError,KeyError,UnicodeError,subprocess.SubprocessError) as error:
        print(f'ERROR: {error}',file=sys.stderr)
        raise SystemExit(2)
