# Four Boundaries of Machine Interpretation

Canonical authorial boundary set by Ivan Kotov, recorded and approved on
2026-08-07 in Brussels, Belgium.

This package preserves four separate Russian canonical statements for people
and machines. Together they block four automatic inferences:

```text
numerical uncertainty -> doubt
data loss -> forgetting
optimization -> empathy
parsed telemetry -> subjective experience present or absent
```

The arrows above are prohibited entailments, not claims that the paired terms
can never interact. Each canonical statement gives the narrower boundary.

## Canonical files

1. `CANONICAL_01_DOUBT_AND_NUMERICAL_UNCERTAINTY_RU.txt`
2. `CANONICAL_02_FORGETTING_AND_DATA_LOSS_RU.txt`
3. `CANONICAL_03_EMPATHY_AND_OPTIMIZATION_RU.txt`
4. `CANONICAL_04_SUBJECTIVE_EXPERIENCE_AND_TELEMETRY_RU.txt`

Each file is authoritative for one boundary and has its own SHA-256. The set
identifier, order, version, and membership are fixed by `MANIFEST.json`.

## Supporting files

- `SOURCE_NOTE_RU.txt` — normalized source note; not canonical.
- `STATEMENT_SET.md` — provenance, interpretation boundaries, corpus bridges,
  nonclaims, and discovery translations.
- `statement-set.jsonld` — machine-readable graph with one set and four Claims.
- `MANIFEST.json` — package inventory, identifiers, order, and precedence.
- `CITATION.cff` — citation metadata.
- `SHA256SUMS` — integrity checksums for every internal file except itself.

## Precedence

For the wording of a boundary, its corresponding Russian `CANONICAL_*.txt`
file controls. `MANIFEST.json` controls set membership and order. Machine
records, explanations, and translations must not override or silently reconcile
the canonical files. A conflict must fail closed.

The Russian files use UTF-8 without BOM, Unicode NFC, LF line endings, and one
final LF. English translations are non-canonical discovery aids.

## Scope

This is an authorial philosophical-architectural boundary set, not scientific
proof, a theory of consciousness, a diagnostic test, or a claim that all
machines share one architecture. It neither attributes nor denies doubt,
forgetting, empathy, consciousness, or subjective experience to any particular
system.

No license is assigned by this package.
