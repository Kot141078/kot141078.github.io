# Scientific Corrigenda and Regression Hardening v1.0

Ivan Kotov · 5 September 2026 · ORCID 0009-0009-6002-9845

A bounded correction supplement for ARQ M2, MOT-c and C-Calculus, plus the ownership-index and experimental-interpretation clarifications described in the corrigendum. This is not a new AI architecture and not a complete replacement release of the parent compound packages.

Read [English corrigendum](CORRIGENDUM_EN.md) or [Russian corrigendum](CORRIGENDUM_RU.md). Full corrected reading editions are in `reading_editions/`; their PDF projections are in `publication/`. Historical source snapshots remain in `source_snapshots/`. Literal edits and source hashes are in `patches/corrections.json` and `SOURCE_BINDINGS.json`.

## Reproduce the text correction and bounded checks

Python 3.10 or later, standard library only:

```sh
python tools/apply_corrections.py --output rebuilt_reading_editions
python tools/test_regressions.py
```

The output directory must not already exist. Altered source bytes, repeated edits and overwrite are rejected. The patcher does not modify the inputs. To rebuild PDF projections with Pandoc and XeLaTeX, use `python tools/build_pdfs.py`; rendering tools and fonts are external build dependencies, not runtime requirements for the corrected protocols.

## Scope and non-claims

The source bytes were obtained from the working mirror and matched against public repository checksums. Complete Zenodo deposit archives were not retrieved in this exercise. The precise ARQ M2 deposit membership remains unresolved; its exact public source commit and hash are used instead. The c[q] addendum DOI must not be substituted.

MOT-c's machine schema already contains LATENT and is not changed. No deployed Liya, Ester or Rita runtime, native continuity validator, subject-model experiment or private memory is touched. First-party regression tests do not establish independent scientific review, consciousness, identity, same-c continuity, safety certification or economic value. Old PASS results remain attached to their old inputs.

## Publication

This package is suitable for a **separate, explicitly linked corrigendum / hardening supplement**, not for replacing the files under an old DOI or uploading a partial package as a complete parent release. `ZENODO_METADATA.json` and `ZENODO_UPLOAD_RU.md` give the deposit fields. No new DOI is invented. The predecessor DOIs identify the earlier works only.

Public correction lifecycle follows the existing CCALC 07c discipline. Original release tags, original DOI payloads and historical evidence are retained. The canonical ARQ owner remains SER; this cross-corpus supplement does not transfer it to AGI.

New explanatory text: CC BY 4.0. New maintenance code: MIT. Reproduced source material retains its original attribution and applicable source license; this supplement does not relicense third-party source material. Fonts are not distributed.
