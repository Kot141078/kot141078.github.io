# Living Corpus Entry Layer V62 Report

Date: 2026-07-19

## Verdict

V62 public projection implemented without status elevation.

The first V62 attempt stopped before writes. This run recovered and verified the authoritative Step 3 package, used the verified Step 1/2/3 inputs, and did not reconstruct Step 3 from transcript, summary, memory, filenames, or counts.

## Step 3 Recovery

- Recovered ZIP path: `C:\Users\kotov\Downloads\333\CONSOLIDATION_STEP_3_REGISTERS_v0_1.zip`
- Recovered ZIP SHA-256: `1cb6d492501b98bfd778b058787c54b2e232b1ddce942be28e80c547ffff8784`
- ZIP hash verdict: PASS
- Selected Step 3 source directory: `C:\Users\kotov\Downloads\333\CONSOLIDATION_STEP_3_VERIFIED`
- Step 3 internal manifest verdict: PASS
- SHA256SUMS-covered files verified: 11/11 PASS
- ZIP membership vs extracted directory: PASS
- Duplicate filename with differing bytes: none observed

## Verified Counts

- Protocol families mapped: 17
- Failure/non-confirmation records: 18
- Open problems: 24
- Open-problem severity distribution: Critical 10, High 13, Medium 1
- Adequately evidenced runtime failure events in selected B0 set: 0
- Invented failures: 0
- Independent reproduction: not identified
- External validation: not identified
- Strict matched profile-control: not identified

## Implemented Surface

New HTML routes:

- `/corpus/`
- `/corpus/protocol-map/`
- `/corpus/current-state/`
- `/corpus/open-problems/`
- `/corpus/failures/`
- `/corpus/changes/`

Updated route:

- `/start-here/`

New public JSON endpoints:

- `/corpus-index.json`
- `/corpus-current.json`
- `/corpus-protocol-map.json`
- `/corpus-open-problems.json`
- `/corpus-failures.json`
- `/corpus-changes.json`
- `/corpus-canonical-sources.json`

Canonical source data:

- `content/corpus/baseline-b0.json`
- `content/corpus/current-state.json`
- `content/corpus/protocol-map.json`
- `content/corpus/open-problems.json`
- `content/corpus/failure-register.json`
- `content/corpus/delta-log.json`
- `content/corpus/canonical-sources.json`
- `content/corpus/entry-copy.json`

Builder:

- `tools/build_corpus.py`

## Validation

- `python` resolved to `C:\Python310\python.exe`, Python 3.10.11.
- `python tools/build_corpus.py`: PASS
- `python tools/build_diary.py`: PASS; incidental Diary output churn was byte-restored to HEAD and excluded.
- Second `python tools/build_corpus.py` SHA-256 idempotence: PASS
- Public HTML/JSON privacy scan for local Windows paths, recovery paths, incoming paths, paid package paths, private repo markers, raw prompts, secrets, and API-key tokens: PASS
- JSON parse and envelope check for all 7 endpoints: PASS
- HTTP 200 route check for existing control routes and all new corpus routes: PASS
- Sitemap count: 804 total URLs, exactly 6 new corpus HTML URLs, 0 corpus JSON URLs added.
- Start-here section order: PASS
- Preserved Diary count: 206
- Preserved Diary latest item: 2026-07-18, `the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time`
- Preserved homepage V60 markers: PASS
- Preserved Diary V59 marker: PASS
- Preserved ESTHER-RP-001 V61 markers: PASS

## Visual Receipts

Receipt directory:

- `C:\Users\kotov\Downloads\111\living-corpus-v62-visual`

Generated after receipts:

- `after-start-here-desktop-1440x900.png`
- `after-start-here-mobile-390x844.png`
- `after-start-here-full-page.png`
- `after-start-here-print-a4.pdf`
- `after-corpus-overview-desktop-1440x900.png`
- `after-corpus-open-problems-mobile-390x844.png`
- `after-visual-overflow-checks.json`

Global horizontal overflow check:

- `/start-here/`: desktop PASS, mobile PASS
- `/corpus/`: desktop PASS, mobile PASS
- `/corpus/protocol-map/`: desktop PASS, mobile PASS
- `/corpus/current-state/`: desktop PASS, mobile PASS
- `/corpus/open-problems/`: desktop PASS, mobile PASS
- `/corpus/failures/`: desktop PASS, mobile PASS
- `/corpus/changes/`: desktop PASS, mobile PASS

## Public File SHA-256 Receipts

- `start-here/index.html`: `b17ce21a1821ace44caaaf3db9a5e87d5ef94e15789b9cf53fc549b0f03cc382`
- `corpus/index.html`: `bcea6f0fbbcaa549ad80cc756d52f372ae105cea29d91a9b0875e97fc1a5f6d8`
- `corpus/protocol-map/index.html`: `857ca4d5263cb55b55cca05c86c1cbfff96b4bdb37bd474e6dfe653eb43e3948`
- `corpus/current-state/index.html`: `89a77c7e673422a6bb4c6d5fbc44238bcccc0af6419bace0bdfae567677367e3`
- `corpus/open-problems/index.html`: `476fe8cdda073c5714dfb3e2e4e5ea5aed3873d9618d772ad020f3d70a0c15c1`
- `corpus/failures/index.html`: `2b39b064880ee9b3a12c2deda075103e0f6c1ae5d1b79ff4e6a8e050edd78cd9`
- `corpus/changes/index.html`: `e7ab16e148485791f7ef981bd52d53ddfd3919477cfc127a8ea1548f7dad8640`
- `corpus-index.json`: `43ba7b69e9fcbc3805a5ae4a60383574ac80b2a5c9ebad713e81b2a2fcbd56b6`
- `corpus-current.json`: `51578e272c7f8ca95f886c05e44cbe83b632ae2253ee1c0aa6446f0162ed8d11`
- `corpus-protocol-map.json`: `6c411092db701a537584db898eb3c2f0a9def342ed8e3e83406355b29c22c9c1`
- `corpus-open-problems.json`: `757beeabf454a3324a9c5fbb4182b1dc07fc8af50f562f77f4bc0463d9dee69e`
- `corpus-failures.json`: `62acd9433131d7486fa7b1aaa2a11b5792b028ccce494adf590b61d06a1f55f5`
- `corpus-changes.json`: `ec687490e1d1973e216e5100deeb2444d12c54b4e2075ce0a2f320bfd48891f1`
- `corpus-canonical-sources.json`: `8cfd5bd8a557699265c19e8d45f2013be1c4fd833cce3e3f304a7b7e80f75bfc`
- `sitemap.xml`: `62573ec7f0bd9eeb796e1112513b2971af86cec319eda5a8c4857fa5a07b5ca0`

## Boundary

This V62 layer is a website projection over verified consolidation registers. It does not modify Diary content, DOI archives, ESTHER-RP-001 content, Theoretical Core content, protocol repositories, reference extraction, or original source packages.

