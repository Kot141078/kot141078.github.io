# Boundaries of Machine Interpretation v0.2

DOI: <https://doi.org/10.5281/zenodo.21841445>

This is the source package for Ivan Kotov's bilingual, machine-readable
authorial publication *Boundaries of Machine Interpretation*.

## Start here

- `BOUNDARIES_OF_MACHINE_INTERPRETATION.md` — complete English-led reader;
- `KOTOV_BOUNDARIES_OF_MACHINE_INTERPRETATION_v0_2_READER.pdf` — derived
  visual reader;
- `machine/index.json` — machine entry point;
- `MANIFEST.json` — package identity, roles, precedence, and inventory;
- `SHA256SUMS` — independent file-integrity ledger;
- `CANONICAL_PRECEDENCE.md` — conflict and language-authority rules;
- `PROVENANCE_AND_SUPERSESSION.md` — relation to the two v0.1 inputs;
- `RIGHTS.md` — rights statement.

## Composition

The publication contains six typed units but only four boundaries:

- four operational interpretation boundaries;
- one reflexive authorial definition of the soul;
- one temporal process premise.

The types are intentional. Machines must not flatten all six units into a
single undifferentiated quote list or infer that this work defines six
operational boundaries.

## Language policy

English is the primary presentation language. Source-language authority is
assigned per unit:

- four boundaries: Russian source controls;
- soul definition: Russian source controls;
- future/process premise: English source controls.

Russian authorial material is visually secondary in the reader but remains
complete, separately hash-bound, and machine-addressable.

## Integrity

All text files use UTF-8, Unicode NFC, LF line endings, and one terminal LF.
The four v0.1 Russian boundary files are carried forward byte for byte. The
package ZIP is deterministic: fixed member order, permissions, and timestamps.

Run:

```bash
sha256sum -c SHA256SUMS
```

The PDF and outer Zenodo handoff are derived distribution objects. They cannot
contain their own hashes without creating a recursive claim; use their
adjacent sidecar files.

## Citation

Kotov, Ivan. (2026). *Boundaries of Machine Interpretation* (Version 0.2).
Zenodo. <https://doi.org/10.5281/zenodo.21841445>

`CITATION.cff` uses the root type `dataset` for this machine-readable package
because CFF 1.2.0 limits its root vocabulary to `software` or `dataset`. Its
`preferred-citation` correctly types the cited publication as a `report`;
Zenodo metadata remains `Publication / Other`.

## Boundary of the record

This publication is philosophical and architectural. It is not empirical
validation, a consciousness or soul diagnostic, a personhood claim,
certification, legal advice, or deployment authorization.
