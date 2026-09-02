# V68 Root Sitemap Delta

Verdict: `PASS`.

V68 uses the V67 reconciliation definition: the authoritative population is the complete unique set of `<url><loc>` values in root `sitemap.xml`. The URL set, not a historical integer, controls the comparison.

## Baseline

- V67 canonical count definition: complete unique `<url><loc>` set in root `sitemap.xml`.
- Pre-V68 local root URLs: 315 elements, 315 unique, 0 duplicates.
- Pre-V68 deployed root URLs: 315 elements, 315 unique, 0 duplicates.
- Pre-V68 local/deployed URL sets: exactly equal.
- Pre-V68 local raw-file SHA-256: `dc7b6374e34f9aeabb8dc63de29fa9f7ba0b8d3864c144b02593fc18ee1e3c61`.
- Pre-V68 deterministic sorted-set SHA-256: `c0a0d86073e3bd6acb537386d2cffa9487313c5a54fc77c69e9c5c0160df3133`.
- Sorted-set serialization: ordinal-sorted UTF-8 URLs, one URL per LF-terminated line.

No unexplained baseline discrepancy was present; the V67 historical reconciliation was not reopened.

## Final semantic comparison

| Measure | Result |
| --- | ---: |
| Final local root URLs | 322 |
| Final deployed root URLs | 322 |
| Added Diary HTML URLs | 7 |
| Removed URLs | 0 |
| Unrelated URL loss | 0 |
| Noindex tag additions | 0 |
| Image URL additions | 0 |
| Diary JSON/machine endpoint additions | 0 |
| Other additions | 0 |

Final local and cache-busted deployed URL sets are exactly equal.

- Final local raw-file SHA-256: `37459d829f28e6a8d017b82642f81daecd423d91104c0d8d302a19eb33e18580`.
- Final deterministic local sorted-set SHA-256: `1099a543afa33c1ad335278f2af0b5a8b68984618478490365463409fcac5fc1`.
- Final deterministic deployed sorted-set SHA-256: `1099a543afa33c1ad335278f2af0b5a8b68984618478490365463409fcac5fc1`.
- Remote missing relative to local: 0.
- Remote extra relative to local: 0.

## ADDED_URLS

1. `https://ivankotov.eu/diary/ai-will-not-create-a-generation-with-no-seniors/`
2. `https://ivankotov.eu/diary/an-api-key-tells-a-provider-which-credential-made-the-call/`
3. `https://ivankotov.eu/diary/many-people-now-speak-of-disappointment-with-artificial-intelligence/`
4. `https://ivankotov.eu/diary/saturday-traffic-report-from-the-ai-highway/`
5. `https://ivankotov.eu/diary/search-advertising-largely-monetized-the-query/`
6. `https://ivankotov.eu/diary/the-most-important-point-in-jerry-tworeks-new-interview-is-not-his-estimate-that-human-researchers-may-stop-being-a-meaningful-part-of-ai-research-in-roughly-two-years/`
7. `https://ivankotov.eu/diary/who-will-need-protection-and-from-whom/`

The builder validated but did not insert these entry URLs. All seven were added through the established narrow sitemap repair. No broad regeneration or reconstruction from old report counts occurred.

## REMOVED_URLS

None.

All prior Corpus and Vision routes remain. No affected noindex tag page, image URL, Diary JSON endpoint, Corpus JSON endpoint, feed endpoint, or other machine endpoint was added by V68.
