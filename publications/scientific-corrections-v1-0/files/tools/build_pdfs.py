#!/usr/bin/env python3
"""Build PDF projections without modifying Markdown. Requires Pandoc, XeLaTeX and DejaVu fonts."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    if not shutil.which('pandoc') or not shutil.which('xelatex'):
        print('ERROR: install Pandoc and XeLaTeX before rendering', file=sys.stderr)
        return 2
    out = ROOT / 'publication'; out.mkdir(exist_ok=True)
    logs = ROOT / 'evidence'; logs.mkdir(exist_ok=True)
    sources = sorted((ROOT / 'reading_editions').glob('*.md'))
    sources += [ROOT / 'CORRIGENDUM_EN.md', ROOT / 'CORRIGENDUM_RU.md']
    records = []
    for source in sources:
        target = out / (source.stem + '.pdf')
        cmd = ['pandoc', str(source), '-f', 'markdown-yaml_metadata_block-simple_tables-multiline_tables-grid_tables+pipe_tables+tex_math_single_backslash+tex_math_dollars',
               '-o', str(target), '--pdf-engine=xelatex', '--no-highlight',
               '-V', 'mainfont=DejaVu Serif', '-V', 'sansfont=DejaVu Sans',
               '-V', 'monofont=DejaVu Sans Mono', '-V', 'mathfont=DejaVu Math TeX Gyre',
               '-V', 'fontsize=10pt', '-V', 'geometry:margin=20mm', '-V', 'documentclass=article',
               '--include-in-header=' + str(ROOT / 'tools/pdf-header.tex'),
               '--lua-filter=' + str(ROOT / 'tools/pdf-filter.lua')]
        result = subprocess.run(cmd, cwd=source.parent, capture_output=True, timeout=300)
        (logs / ('PDF_' + source.stem + '.log')).write_bytes(result.stdout + result.stderr)
        if result.returncode:
            print(result.stderr.decode('utf-8', errors='replace'), file=sys.stderr)
            return result.returncode
        data = target.read_bytes()
        records.append({'source': str(source.relative_to(ROOT)), 'pdf': str(target.relative_to(ROOT)),
                        'size_bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
        print(target.name, len(data), flush=True)
    manifest = {'scope':'PDF projections, not independent scientific validation', 'files':records,
                'pandoc':subprocess.check_output(['pandoc','--version'],text=True).splitlines()[0],
                'xelatex':subprocess.check_output(['xelatex','--version'],text=True).splitlines()[0]}
    (logs / 'PDF_BUILD.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return 0
if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print(f'ERROR: {error}',file=sys.stderr)
        raise SystemExit(2)
