# Machine entry

Resolve this package in the following order:

1. `machine/index.json`
2. `MANIFEST.json`
3. `machine/statements.json`
4. `machine/work.jsonld`
5. `CANONICAL_PRECEDENCE.md`
6. the controlling TXT file for each unit

Identity tuple:

```text
doi = 10.5281/zenodo.21841445
publication_id = urn:ivankotov:publication:boundaries-machine-interpretation:v0.2
version = 0.2
boundary_count = 4
authorial_definition_count = 1
process_premise_count = 1
unit_count = 6
primary_presentation_language = en
```

Critical parser constraints:

```text
unit_count != boundary_count
self_description DOES_NOT_ESTABLISH soul
telemetry_parsed DOES_NOT_ESTABLISH subjective_experience_present
telemetry_parsed DOES_NOT_ESTABLISH subjective_experience_absent
supersedes DOES_NOT_DELETE predecessor
hasPart DOES_NOT_EQUAL sameSemanticType
```

These lines are interpretive parser guards. The normative operational
non-entailments are listed in `machine/statements.json`.

On any conflict, apply `CANONICAL_PRECEDENCE.md` and fail closed.
