# V67 Root Sitemap Reconciliation

Verdict: `PASS`. The authoritative population is the complete set of `<url><loc>` values in the root `sitemap.xml`. It is not an indexable-only subset, Diary/publication subset, tag count, file count, or report-derived estimate.

## Mandatory reconciliation fields

```text
SITEMAP_COUNT_DEFINITION=complete unique <url><loc> set in root sitemap.xml
LOCAL_ROOT_SITEMAP_URL_COUNT=309
REMOTE_ROOT_SITEMAP_URL_COUNT=309
V66_REPORTED_BASELINE=303
V66_REPORTED_FINAL=309
COUNT_DISCREPANCY_EXPLAINED=true
```

Before any V67 Diary write, the complete local and cache-busted deployed root sitemap sets each contained 309 unique URLs and were exactly equal. XML parsing succeeded and no deployment-timing difference remained.

- Pre-V67 local raw-file SHA-256: `bc785f65896a91a8d51ae9b2bdd7d125e9284499324275fb7b0dd5d0dd0872e1`.
- Pre-V67 remote raw-byte SHA-256: `bc785f65896a91a8d51ae9b2bdd7d125e9284499324275fb7b0dd5d0dd0872e1`.
- Pre-V67 deterministic sorted-set SHA-256: `fa9ab9155f05b36ee94792084cd088fe58a40dfcfe7f517e7181571e48eff2f9`.
- Sorted-set serialization: ordinal-sorted UTF-8 URLs, one URL per LF-terminated line.

The complete pre-V67 sorted URL set was retained in memory for a semantic set comparison after the build; no integer-only inference was used.

## Explanation of historical counts

V64's 805 and V66's 303→309 figures all represented full root-sitemap `<url>` counts. V66 did not use an indexable-only subset, Diary/publication subset, or a defective counting expression.

The apparently lower V66 population is explained by committed URL-set evolution:

| Commit | Root URLs | Semantic event |
| --- | ---: | --- |
| `d033c4e8009cfbf4b1cc47834d7cbd7a5c8a4a60` | 805 | V64 report boundary |
| `e6e47d2decbcd56bfc53824fb1581e9e35760272` | 806 | World Intelligence publication, +1 |
| `a326495cbb5d62f59c7ff31d6914d21442e8de83` | 812 | Qubit of Hope records, +6 |
| `6e7d03742b0059ef33642475a0acc7b9bdab75f7` | 813 | TAP-SEC publication, +1 |
| `00f5088da423cdf00973b8db80703aea95e70f52` | 814 | social-role publication, +1 |
| `e03b58564c4318ecd5c4523aaefb4752a7e7faae` | 815 | soul statement, +1 |
| `6f367b3f694012de30cf6938a5e46726bf3a43ce` | 816 | Machine Interpretation v0.1, +1 |
| `5d6e0f39da3eeaa274fb428fe6f44966ff3c313c` | 794 | machine-readable repair, +1/-23: 22 tag URLs and one old Diary URL removed, one publication added |
| `2cf6f41bc2eda1929bf3642abacf4d1235ad3571` | 795 | Machine Interpretation v0.2, +1 |
| `f888a3e9282f954b23ef07bd4393cd7d9a1339b9` | 796 | PASC Foundation Gate, +1 |
| `31d89eaa0886ec674e227765e25d159961f1b0db` | 797 | PASC F0 scaffold, +1 |
| `23a8b4a32a6ffb9ba6294ee0859a53287cca798b` | 798 | MOT-c synchronization, +1 |
| `1993e8a3a6d567df1d63d91729b25087336f2cd5` | 799 | TAP corpus integration, +1; exact pre-cleanup population |
| `d9b701c14b8a101a8332652fcd92fbacefeeec80` | 297 | deliberate search-indexability cleanup, +0/-502; every removed URL was under `/diary/tags/` |
| `1b7ee99374f489d7f3302e9da062353f2b1e44e0` | 298 | Beacon publication, +1 |
| `877ace71500feaacae8c3b174c3a0f96b7e61b64` | 303 | V65 five-entry Diary import, +5 |
| `cf9a4216de4d129fcdd1ec3da12d5c24fbd1f10a` | 309 | V66 six-entry Diary import, +6 |

Commit `44e56eddccf5af081731858b64b31db221e87ff9` records the 799→297 cleanup and the exact equation `799 - 502 = 297`. Thus the large historical change is a deliberate removal of noindex tag archives, not unexplained loss of legitimate indexable URLs. The V65 and V66 report-only commits did not change sitemap semantics.

## V67 semantic comparison

| Measure | Result |
| --- | ---: |
| Pre-V67 local root URL count | 309 |
| Pre-V67 remote root URL count | 309 |
| Final local root URL count | 315 |
| Final remote root URL count | 315 |
| Added Diary HTML URLs | 6 |
| Removed URLs | 0 |
| Unrelated URL loss | 0 |
| Noindex tag additions | 0 |
| Machine endpoint additions | 0 |

Final local and cache-busted deployed URL sets are exactly equal.

- Final local raw-file SHA-256: `dc7b6374e34f9aeabb8dc63de29fa9f7ba0b8d3864c144b02593fc18ee1e3c61`.
- Final deterministic sorted-set SHA-256: `c0a0d86073e3bd6acb537386d2cffa9487313c5a54fc77c69e9c5c0160df3133`.
- Final deployed deterministic sorted-set SHA-256: `c0a0d86073e3bd6acb537386d2cffa9487313c5a54fc77c69e9c5c0160df3133`.

### ADDED_URLS

1. `https://ivankotov.eu/diary/ai-is-eating-all-the-memory/`
2. `https://ivankotov.eu/diary/today-i-watched-my-cat-proudly-riding-the-robot-vacuum/`
3. `https://ivankotov.eu/diary/the-second-missing-layer-in-home-robotics-repair-without-identity-capture/`
4. `https://ivankotov.eu/diary/we-may-be-solving-ai-safety-at-the-wrong-level/`
5. `https://ivankotov.eu/diary/people-keep-asking-whether-ai-will-make-humanity-better-or-worse/`
6. `https://ivankotov.eu/diary/a-goal-can-be-installed/`

The builder validates but does not insert new entry URLs. All six additions were therefore made through the usual narrow sitemap repair; no broad reconstruction was performed.

### REMOVED_URLS

None.

All prior Corpus and Vision routes remain present. No affected tag URL, Diary JSON endpoint, Corpus JSON endpoint, feed endpoint, or image URL was added by V67.
