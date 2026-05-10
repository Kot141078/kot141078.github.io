# Post Deploy Check V47

Implementation commit checked: `e3007ed120f8c8254ee3a0e41a35a75e384d924f`

Deployment target: `https://ivankotov.eu`

## Remote HTTP Results

- Entry URLs: 4 checked, 4 returned 200.
- Asset URLs: 4 checked, 4 returned 200.
- Affected tag URLs: 35 checked, 0 non-200.
- Diary home: 200.
- Diary archive: 200.
- Site home: 200.
- `diary-index.json`: 200.
- `diary-feed.xml`: 200.
- `sitemap.xml`: 200.

## Remote Data Results

- `diary-index.json` count: 145.
- `diary-index.json` latest: `2026-05-11` / `ai-is-leaving-the-text-box`.
- Home latest-post points to `ai-is-leaving-the-text-box`.
- Top remote ordering:
  - `2026-05-11` / `ai-is-leaving-the-text-box`
  - `2026-05-10` / `most-public-conversations-about-quantum-computing-still-begin-with-fear`
  - `2026-05-09` / `the-next-ai-risk-may-not-look-like-rebellion`
  - `2026-05-09` / `one-of-the-most-damaging-habits-in-technical-culture-is-the-assumption-that-every-pause-means-failure`
  - `2026-05-09` / `ai-is-not-a-toy-for-clever-podcast-lines`
- Sitemap contains all four new entry URLs and affected tag URLs checked in this pass.

## Contract-Specific Checks

- V23 date-only meta fix: intact on all four new entries.
- V28 five-entry preview fix: intact, latest section has 5 entry cards.
- 0140 raw/effective date: `09-04-2026` -> `2026-05-09`.
- 0141 effective date: `2026-05-09`.
- 0142 effective date: `2026-05-10`.
- 0143 no explicit source date line -> `2026-05-11`.
- Same-date ordering: 0141 appears before 0140.
- Duplicate guard: no pre-existing Diary duplicate found before import; each supplied LinkedIn URL appears exactly once in `content/diary` after import.

## Remote Entry URLs

- https://ivankotov.eu/diary/ai-is-not-a-toy-for-clever-podcast-lines/
- https://ivankotov.eu/diary/one-of-the-most-damaging-habits-in-technical-culture-is-the-assumption-that-every-pause-means-failure/
- https://ivankotov.eu/diary/most-public-conversations-about-quantum-computing-still-begin-with-fear/
- https://ivankotov.eu/diary/ai-is-leaving-the-text-box/
