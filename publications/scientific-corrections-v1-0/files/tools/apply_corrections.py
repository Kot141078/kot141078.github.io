#!/usr/bin/env python3
"""Rebuild the four corrected reading editions without altering any input.

Python 3.10+, standard library only. This is a document patcher, not a runtime
validator or an implementation of ARQ, MOT-c, or the continuity classifier.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[1]
NOTICE = (
    '> **Corrected reading edition — Scientific Corrigenda and Regression Hardening v1.0.**\n'
    '> Correction date: 2026-09-05. The predecessor edition remains unchanged.\n'
    '> This file incorporates only the corrections recorded in `patches/corrections.json`.\n'
    '> Historical titles, document versions and identifiers below describe the predecessor;\n'
    '> they do not assign its DOI to these changed bytes. This is not a complete new release\n'
    '> of the parent compound package. See the accompanying corrigendum and source bindings.\n\n'
)

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def corrected_name(name: str) -> str:
    return name.removesuffix('.md') + '_CORRECTED_20260905.md'

def apply_text(data: bytes, name: str, spec: dict) -> bytes:
    binding = next((x for x in spec['source_bindings'] if x['filename'] == name), None)
    if binding is None or len(data) != binding['size_bytes'] or sha256(data) != binding['sha256']:
        raise ValueError(f'SOURCE_MISMATCH: {name}')
    text = data.decode('utf-8')
    for patch in spec['patches']:
        if patch['filename'] != name:
            continue
        count = text.count(patch['old'])
        if count != patch['expected_occurrences']:
            raise ValueError(f'PATCH_OCCURRENCE_MISMATCH: {name}: {patch["finding"]}: {count}')
        text = text.replace(patch['old'], patch['new'])
    # Prevent changed bytes from presenting their predecessor DOI/status as their own.
    text = text.replace('**DOI:**', '**Predecessor version DOI:**', 1)
    text = text.replace('**Status:** canonical public release v0.1',
                        '**Status:** corrected reading edition of public v0.1; archival deposit pending', 1)
    text = text.replace('**Статус:** канонический публичный выпуск v0.1',
                        '**Статус:** исправленная читательская редакция публичного v0.1; архивная публикация готовится', 1)
    return (NOTICE + text).encode('utf-8')

def build(source_dir: Path, output_dir: Path, spec: dict) -> dict:
    source_dir = source_dir.resolve(strict=True)
    if not source_dir.is_dir():
        raise ValueError('Input must be an existing directory')
    output_dir = output_dir.absolute()
    if output_dir.exists() or output_dir.is_symlink():
        raise FileExistsError(f'Refusing to overwrite: {output_dir}')
    parent = output_dir.parent.resolve(strict=True)
    payloads: dict[str, bytes] = {}
    for binding in spec['source_bindings']:
        name = binding['filename']
        if Path(name).name != name or not name.endswith('.md'):
            raise ValueError(f'Unsafe source basename: {name}')
        path = source_dir / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f'Not a regular source file: {name}')
        payloads[corrected_name(name)] = apply_text(path.read_bytes(), name, spec)
    with tempfile.TemporaryDirectory(prefix='.corrigenda-', dir=parent) as tmp:
        stage = Path(tmp) / 'editions'
        stage.mkdir()
        for name, data in payloads.items():
            (stage / name).write_bytes(data)
        report = {'artifact': spec['artifact'], 'scope': 'exact document patch replay only',
                  'files': [{'filename': n, 'size_bytes': len(b), 'sha256': sha256(b)}
                            for n, b in sorted(payloads.items())]}
        (stage / 'READING_EDITION_MANIFEST.json').write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        os.rename(stage, output_dir)
    return report

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path, default=ROOT / 'source_snapshots')
    parser.add_argument('--output', type=Path, required=True, help='New, nonexistent output directory')
    args = parser.parse_args()
    try:
        spec = json.loads((ROOT / 'patches/corrections.json').read_text(encoding='utf-8'))
        report = build(args.source_dir, args.output, spec)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, UnicodeError) as exc:
        print(f'ERROR: {exc}', file=__import__('sys').stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
