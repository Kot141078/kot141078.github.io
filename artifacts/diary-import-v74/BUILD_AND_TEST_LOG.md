# V74 full local machine-readability gate

```text
+ C:\Python310\python.exe tools/build_beacon_v0_1_site_surfaces.py
Built Beacon Profile v0.1 site routing surfaces.
+ C:\Python310\python.exe tools/build_diary.py
+ C:\Python310\python.exe tools/build_corpus.py
Built living corpus layer: 15 files
HTML routes: 7
JSON endpoints: 7
Sitemap additions required: 6
+ C:\Python310\python.exe tools/build_machine_layer.py
Machine layer built: 7 files
+ C:\Python310\python.exe tools/check_machine_readability.py
PASS check_generated_outputs
PASS check_schema_documents
PASS check_works
PASS check_terms
PASS check_bridges
PASS check_repositories
PASS check_mot_c_source_pinning
PASS check_protocol_map
PASS check_machine_index
PASS check_json_files
PASS check_html_pages
PASS check_internal_html_links
PASS check_discovery_files
PASS check_diary_canonical_aliases
PASS machine readability gate (14 checks)
+ C:\Python310\python.exe tools/validate_search_indexability.py
PASS search indexability gate (356 sitemap URLs, 0 tag URLs, 619 noindex tag pages, 31 index-intended fixtures, 257 bounded Diary posts, 1028 related cards, 25 protected post-content hashes, 5105 non-empty section-links containers, 533 unique canonical tags, 85 retained legacy tag pages, 2615 canonical tag memberships across 257 entries, 2213 canonical-only tag links, 20 contextual priority links)
+ C:\Python310\python.exe tools/check_tap_surface.py
TAP_R4_CLAIM_CONSISTENCY_PASS
+ C:\Python310\python.exe tools/validate_beacon_v0_1_site.py
PASS Beacon v0.1 site validator PASS
+ C:\Users\kotov\AppData\Roaming\npm\npm.CMD exec --yes --package=ajv-cli@5.0.0 --package=ajv-formats@3.0.1 -- ajv validate --spec=draft2020 -c ajv-formats -s schemas/machine-index-v1.schema.json -d machine-index.json
machine-index.json valid
+ C:\Users\kotov\AppData\Roaming\npm\npm.CMD exec --yes --package=ajv-cli@5.0.0 --package=ajv-formats@3.0.1 -- ajv validate --spec=draft2020 -c ajv-formats -s schemas/scientific-corpus-index-v1.schema.json -d scientific-corpus-index.json
scientific-corpus-index.json valid
+ C:\Users\kotov\AppData\Roaming\npm\npm.CMD exec --yes --package=ajv-cli@5.0.0 --package=ajv-formats@3.0.1 -- ajv validate --spec=draft2020 -c ajv-formats -s schemas/term-registry-v1.schema.json -d term-registry.json
term-registry.json valid
+ C:\Users\kotov\AppData\Roaming\npm\npm.CMD exec --yes --package=ajv-cli@5.0.0 --package=ajv-formats@3.0.1 -- ajv validate --spec=draft2020 -c ajv-formats -s schemas/semantic-bridges-v1.schema.json -d semantic-bridges.json
semantic-bridges.json valid
+ C:\Users\kotov\AppData\Roaming\npm\npm.CMD exec --yes --package=ajv-cli@5.0.0 --package=ajv-formats@3.0.1 -- ajv validate --spec=draft2020 -c ajv-formats -s schemas/public-repositories-v1.schema.json -d public-repositories.json
public-repositories.json valid
+ git diff --check
PASS full machine-readability gate (8 Python steps, 5 schema contracts)

```

Second stabilization build: zero changes across 896 generated files. Full first-build callback evidence is in BUILDER_READONLY_FIX_AUDIT.md. Six bounded cleanup fixture tests passed before touching the real generated tree.
