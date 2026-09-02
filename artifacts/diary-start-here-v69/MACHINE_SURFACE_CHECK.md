# V69 Machine Surface Check

Machine compatibility verdict: `PASS`.

## Canonical configuration

`content/diary/_curation.json` retains the existing Diary-slug field and adds one optional bounded field:

- `start_here`: 5 Diary slugs.
- `start_here_external`: 1 route with `kind: book`, `source_json: world-intelligence.json`, canonical local URL, existing image, CTA, and page role.

No fake Diary slug or LinkedIn source was created.

## Generated JSON

`diary-start-here.json` preserves the established `items` meaning:

| Field | Count | Meaning |
| --- | ---: | --- |
| `items` | 5 | Real Diary entries only |
| `external_routes` | 1 | Explicit external first-party route |

The single external record has:

- `position`: 6
- `kind`: `book`
- `title`: `World Intelligence`
- `subtitle`: `Humans, c, and Temporal AI Presence Beyond the Age of Agents`
- `version`: `1.1.0`
- `release_tag`: `v1.1.0`
- `publication_date`: `2026-07-24`
- `page_role`: `complete multilingual book`
- `page`: `https://ivankotov.eu/world-intelligence/`
- `cta`: `Open book`
- `source_json`: `https://ivankotov.eu/world-intelligence.json`

Title, subtitle, version, release tag, and publication date are loaded by the builder from the canonical source JSON. The curation layer does not maintain a competing metadata copy.

## JSON-LD and human routes

- `/diary/`: six ordered cards.
- `/diary/start-here/`: six ordered cards.
- Embedded `ItemList`: six items with positions 1-6.
- Position 6 URL: `https://ivankotov.eu/world-intelligence/`.
- World Intelligence fabricated Diary URLs: 0.
- World Intelligence Diary identifier, tags, raw tags, LinkedIn URL, or fake Diary date: 0.

The external route is absent from:

- `diary-index.json`;
- Diary archive records;
- Diary feed entries;
- Diary tag counts/pages;
- Diary search corpus;
- Diary count and latest projections.

## Parser and compatibility checks

- Local `diary-start-here.json`: parse pass; `items=5`, `external_routes=1`.
- Remote `diary-start-here.json`: parse pass; same cardinality, order, and external metadata.
- Embedded JSON-LD on both human surfaces: parse pass.
- JSON-LD position 6 canonical URL: pass.
- `python tools/check_machine_readability.py`: 14/14 pass.
- Diary count/latest: 230 / ENTRY 0230 / 2026-09-01, unchanged.
