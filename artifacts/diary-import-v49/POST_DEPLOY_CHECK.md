# V49 Post Deploy Check

Implementation commit checked: `e8a68ea9a3b7f485791d00fbba0ce42372ad7850`

## Remote Results

- Entry URLs: 8 checked, 8 returned HTTP 200.
- Asset URLs: 7 checked, 7 returned HTTP 200.
- Affected tag pages: 52 checked, 52 returned HTTP 200.
- `https://ivankotov.eu/diary-index.json`: HTTP 200, count 159, latest `llms-are-not-the-ai`.
- `https://ivankotov.eu/diary-feed.xml`: HTTP 200.
- `https://ivankotov.eu/sitemap.xml`: HTTP 200 and includes new entry URLs.
- `https://ivankotov.eu/`: HTTP 200 and latest-post points to ENTRY 0157.

## Behavioral Checks

- V23 date-only meta fix: intact.
- V28 five-entry preview fix: intact.
- ENTRY 0154: untagged rendering verified.
- ENTRY 0155: image-less rendering verified without placeholder.
- ENTRY 0150 links: verified.
- ENTRY 0154 links: verified.
- ENTRY 0155 links: verified.
- Duplicate guard result: clean.

## Manual Remainder

Send URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V49.md` to Search Console.
