#!/usr/bin/env python3
"""Focused document and mathematical-example regressions; no model/runtime calls."""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
import importlib.util
import itertools
import json
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location('apply_corrections', ROOT / 'tools/apply_corrections.py')
patcher = importlib.util.module_from_spec(_SPEC)
assert _SPEC and _SPEC.loader
_SPEC.loader.exec_module(patcher)
SPEC = json.loads((ROOT / 'patches/corrections.json').read_text(encoding='utf-8'))
MOT_EN = 'MOT_c_Foundation_Theory_v0_1_EN.md'
MOT_RU = MOT_EN.replace('_EN', '_RU')
ARQ = 'ARQ_System_Models_and_Assumptions_v0.2.md'
CCALC = '04_C_CONTINUITY_METRIC_AND_EQUIVALENCE_SEMANTICS_v0_1_2.md'

def source(name: str) -> bytes:
    return (ROOT / 'source_snapshots' / name).read_bytes()

def edition(name: str) -> str:
    return (ROOT / 'reading_editions' / patcher.corrected_name(name)).read_text(encoding='utf-8')

def section(text: str, number: int) -> str:
    m = re.search(rf'^## {number}\. .*?(?=^## \d+\.|\Z)', text, re.M | re.S)
    if not m:
        raise ValueError(f'Missing section {number}')
    return m.group()

def appendix_states(text: str) -> list[str]:
    m = re.search(r'^    state: (.*?)^    changed_at:', text, re.M | re.S)
    if not m:
        raise ValueError('Appendix state field not found')
    return re.findall(r'\b[A-Z][A-Z_]+\b', m.group(1))

def lifecycle_states(text: str) -> list[str]:
    return re.findall(r'^\| `([A-Z_]+)` \|', section(text, 7), re.M)

def check_mot(text: str) -> None:
    a, b = appendix_states(text), lifecycle_states(text)
    if len(a) != len(set(a)) or a != b or len(a) != 15:
        raise ValueError('MOT_STATE_VOCABULARY_MISMATCH')

def cap(budget: int | Fraction, minimum_cost: int | Fraction) -> int:
    if isinstance(budget, bool) or isinstance(minimum_cost, bool):
        raise ValueError('Booleans are not resource quantities')
    budget, minimum_cost = Fraction(budget), Fraction(minimum_cost)
    if budget < 0 or minimum_cost <= 0:
        raise ValueError('Invalid resource budget or cost')
    return budget // minimum_cost

def adjacency(events: list[str], alphabet: list[str]) -> dict:
    if len(alphabet) != len(set(alphabet)) or any(not isinstance(x, str) for x in alphabet):
        raise ValueError('Alphabet must contain unique labels')
    if any(x not in alphabet for x in events):
        raise ValueError('Unknown observed label')
    pairs = Counter(zip(events, events[1:]))
    origins = Counter(events[:-1])
    return {i: None if not origins[i] else {j: Fraction(pairs[i, j], origins[i]) for j in alphabet}
            for i in alphabet}

class CorrectionTests(unittest.TestCase):
    def test_01_source_bindings(self):
        for b in SPEC['source_bindings']:
            with self.subTest(name=b['filename']):
                data = source(b['filename'])
                self.assertEqual(len(data), b['size_bytes'])
                self.assertEqual(patcher.sha256(data), b['sha256'])

    def test_02_replay_exact_editions(self):
        for b in SPEC['source_bindings']:
            name = b['filename']
            with self.subTest(name=name):
                self.assertEqual(patcher.apply_text(source(name), name, SPEC),
                                 (ROOT / 'reading_editions' / patcher.corrected_name(name)).read_bytes())

    def test_03_changed_source_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'SOURCE_MISMATCH'):
            patcher.apply_text(source(ARQ) + b'\n', ARQ, SPEC)

    def test_04_repeated_patch_is_rejected(self):
        bad = json.loads(json.dumps(SPEC))
        bad['patches'].append(dict(bad['patches'][0]))
        with self.assertRaisesRegex(ValueError, 'PATCH_OCCURRENCE_MISMATCH'):
            patcher.apply_text(source(ARQ), ARQ, bad)

    def test_05_no_output_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'exists'; out.mkdir()
            (out / 'keep').write_text('unchanged')
            with self.assertRaises(FileExistsError):
                patcher.build(ROOT / 'source_snapshots', out, SPEC)
            self.assertEqual((out / 'keep').read_text(), 'unchanged')

    def test_06_bad_input_creates_no_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / 'sources'; src.mkdir(); out = Path(tmp) / 'editions'
            for b in SPEC['source_bindings']:
                (src / b['filename']).write_bytes(source(b['filename']))
            (src / ARQ).write_bytes(b'corrupted')
            with self.assertRaises(ValueError):
                patcher.build(src, out, SPEC)
            self.assertFalse(out.exists())

    def test_07_successful_fresh_rebuild(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'editions'
            result = patcher.build(ROOT / 'source_snapshots', out, SPEC)
            self.assertEqual(len(result['files']), 4)
            for item in result['files']:
                self.assertEqual((out / item['filename']).read_bytes(),
                                 (ROOT / 'reading_editions' / item['filename']).read_bytes())

    def test_08_mot_en_vocabulary(self):
        check_mot(edition(MOT_EN))

    def test_09_mot_ru_vocabulary(self):
        check_mot(edition(MOT_RU))

    def test_10_old_en_defect_detected(self):
        with self.assertRaisesRegex(ValueError, 'VOCABULARY'):
            check_mot(source(MOT_EN).decode())

    def test_11_old_ru_defect_detected(self):
        with self.assertRaisesRegex(ValueError, 'VOCABULARY'):
            check_mot(source(MOT_RU).decode())

    def test_12_mot_duplicate_state_detected(self):
        with self.assertRaises(ValueError):
            check_mot(edition(MOT_EN).replace('CANDIDATE | LATENT |', 'CANDIDATE | LATENT | LATENT |'))

    def test_13_lifecycle_semantics_unchanged(self):
        for name in (MOT_EN, MOT_RU):
            self.assertEqual(section(edition(name), 7), section(source(name).decode(), 7))

    def test_14_initial_eight_bits_no_new_commit(self):
        initial, final, n, maximum_delta = 8, 8, 0, 4
        self.assertFalse(final <= n * maximum_delta)
        self.assertLessEqual(final - initial, n * maximum_delta)
        self.assertIn('H_{retained}(T) - H_{retained}(0)', section(edition(ARQ), 8))

    def test_15_budget_normalization(self):
        self.assertEqual(cap(8, 2), 4)
        self.assertIn('\\frac{I_{max}(T)}{i_{commit,min}}', section(edition(ARQ), 8))

    def test_16_unit_scale_invariance(self):
        for factor in (Fraction(1, 1000), Fraction(1, 3), 1, 1000):
            self.assertEqual(cap(8 * factor, 2 * factor), 4)

    def test_17_floor_and_zero_budget(self):
        self.assertEqual(cap(9, 2), 4)
        self.assertEqual(cap(0, 2), 0)

    def test_18_invalid_charge_rejected(self):
        for budget, charge in ((1, 0), (1, -1), (-1, 2), (True, 1)):
            with self.assertRaises(ValueError):
                cap(budget, charge)

    def test_19_subset_costs_cannot_bound_all_commits(self):
        self.assertGreater(cap(8, 2) + cap(8, 2), min(cap(8, 2), cap(8, 2)))
        self.assertIn('same full set of counted commits', edition(ARQ))

    def test_20_finite_memory_not_lifetime_count(self):
        bit = 0
        for _ in range(100):
            bit ^= 1
        self.assertEqual(bit, 0)
        self.assertGreater(100, 1)
        self.assertIn('non-recycled persistent headroom', edition(ARQ))

    def test_21_empty_and_singleton_trace(self):
        for events in ([], ['A']):
            self.assertEqual(adjacency(events, ['A', 'B']), {'A': None, 'B': None})

    def test_22_terminal_origin_excluded(self):
        self.assertEqual(adjacency(['A', 'B', 'A'], ['A', 'B']),
                         {'A': {'A': 0, 'B': 1}, 'B': {'A': 1, 'B': 0}})

    def test_23_defined_row_sums_exhaustive_small_traces(self):
        for n in range(6):
            for events in itertools.product(('A', 'B'), repeat=n):
                for row in adjacency(list(events), ['A', 'B']).values():
                    if row is not None:
                        self.assertEqual(sum(row.values()), 1)

    def test_24_no_implicit_terminal_self_loop(self):
        self.assertEqual(adjacency(['A', 'B'], ['A', 'B'])['B'], None)

    def test_25_unknown_labels_rejected(self):
        with self.assertRaises(ValueError):
            adjacency(['A', 'C'], ['A', 'B'])

    def test_26_resemblance_nontransitive(self):
        a, b, c, threshold = map(Fraction, ('0', '0.6', '1.2', '1'))
        self.assertLessEqual(abs(a - b), threshold)
        self.assertLessEqual(abs(b - c), threshold)
        self.assertGreater(abs(a - c), threshold)
        self.assertNotIn('### 21.4 Resemblance equivalence', edition(CCALC))

    def test_27_directed_path_not_symmetric(self):
        edges = {('A', 'B'), ('B', 'C')}
        self.assertIn(('A', 'B'), edges)
        self.assertNotIn(('B', 'A'), edges)
        self.assertIn('### 21.3 Directed operational continuity', edition(CCALC))

    def test_28_admission_algorithms_unchanged(self):
        for n in (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 19, 20, 22, 23, 24, 25, 26):
            with self.subTest(section=n):
                try:
                    a, b = section(edition(CCALC), n), section(source(CCALC).decode(), n)
                except ValueError:
                    if n == 26:
                        continue
                    raise
                self.assertEqual(a, b)

    def test_29_source_doi_not_assigned_to_new_bytes(self):
        for name in (MOT_EN, MOT_RU):
            text = edition(name)
            self.assertIn('**Predecessor version DOI:**', text)
            self.assertNotIn('**DOI:**', text)
            self.assertIn('they do not assign its DOI to these changed bytes', text)

if __name__ == '__main__':
    unittest.main(verbosity=2)
