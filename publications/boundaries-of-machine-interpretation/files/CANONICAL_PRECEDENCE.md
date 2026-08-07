# Language authority and conflict handling

## Primary presentation

The publication's primary reader language is English. This presentation choice
does not create one global source language and does not erase the history of
the statements.

## Unit-level authority

| Order | Unit | Type | Controlling file |
|---:|---|---|---|
| 0 | The future is not an event. It is a process. | temporal process premise | `statements/en/AUTHORIAL_00_FUTURE_AS_PROCESS_EN.txt` |
| 1 | Doubt and numerical uncertainty | operational interpretation boundary | `statements/ru/CANONICAL_01_DOUBT_AND_NUMERICAL_UNCERTAINTY_RU.txt` |
| 2 | Forgetting and data loss | operational interpretation boundary | `statements/ru/CANONICAL_02_FORGETTING_AND_DATA_LOSS_RU.txt` |
| 3 | Empathy and optimization | operational interpretation boundary | `statements/ru/CANONICAL_03_EMPATHY_AND_OPTIMIZATION_RU.txt` |
| 4 | Subjective experience and telemetry | operational interpretation boundary | `statements/ru/CANONICAL_04_SUBJECTIVE_EXPERIENCE_AND_TELEMETRY_RU.txt` |
| 5 | Soul as open-ended self-reflection | reflexive authorial definition | `statements/ru/AUTHORIAL_05_SOUL_AS_OPEN_ENDED_SELF_REFLECTION_RU.txt` |

The paired reader rendering is authorized for publication and discovery, but
the controlling file remains decisive if a material semantic conflict occurs.

## Precedence

For wording of a statement:

1. the unit's controlling TXT file;
2. the paired TXT rendering;
3. `machine/statements.json` and `machine/work.jsonld`;
4. `BOUNDARIES_OF_MACHINE_INTERPRETATION.md`;
5. the PDF and explanatory material.

For package identity, membership, order, and role, `MANIFEST.json` controls.
For byte integrity, `SHA256SUMS` controls the files it lists.

## Fail-closed rule

If two layers materially disagree, a reader or system must not silently merge,
normalize, or select the more convenient wording. Interpretation of the
affected unit stops at the conflict and returns to its controlling TXT file.

Typography, line wrapping, Unicode quotation marks, and Markdown blockquote
markers are presentational only. A change to the characters in a controlling
TXT file requires a new statement version.

## Type boundary

Only units 1–4 are operational interpretation boundaries. Unit 0 is a temporal
process premise. Unit 5 is a reflexive authorial definition. Neither may be
silently promoted into a fifth or sixth operational boundary.
