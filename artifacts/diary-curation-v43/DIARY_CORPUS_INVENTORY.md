# DIARY_CORPUS_INVENTORY

## Scope

- Contract: `SITE_DIARY_CURATION_AND_DISCOVERY_V43`
- Repo: `C:\Users\kotov\Desktop\AGI\kot141078.github.io`
- Corpus source of truth used for counting: generated `diary-index.json` plus preserved `raw_tags` payloads from the builder
- Scan intent: inventory only; no post texts were rewritten during this scan

## Corpus Totals

- Total diary entries detected: `117`
- Earliest entry date: `2026-01-02`
- Latest entry date: `2026-04-18`
- Image-backed entries: `106`
- Image-less entries: `11`

## Calendar Coverage

- `2026-01`: `45` entries
- `2026-02`: `12` entries
- `2026-03`: `26` entries
- `2026-04`: `34` entries

## Raw Tag Surface

- Raw unique tag count before display-layer normalization: `289`
- Tag surface is broad and already rich enough for curation; the problem was not lack of tags, but semantic spread and alias drift
- The most visible raw recurrence clusters are:
  - `Cybernetics`: `80`
  - `L4`: `69`
  - `AI Architecture`: `68`
  - `Advanced Global Intelligence`: `53`
  - `AI Safety`: `53`
  - `AI`: `32`
  - `AGI`: `32`
  - `Systems Thinking`: `31`
  - `Human Centered AI`: `18`
  - `Long Lived AI`: `18`
  - `Deep Tech`: `17`
  - `Local AI`: `17`
  - `Future of AI`: `16`
  - `SER`: `14`
  - `Sovereign AI`: `14`
  - `L4 Boundary`: `14`

## Obvious Duplicate / Alias Pressure

- The corpus clearly contained display-level drift around these clusters:
  - `AGI` vs `Advanced Global Intelligence`
  - `AI` vs `Artificial Intelligence`
  - `L4` vs `L4 Boundary` vs `L4 Witness` vs `Reality Boundary` variants
  - `SER` vs `SER FED`
  - `Human Centered AI` vs `Human Centric AI`
  - `Local AI` vs `Local First` vs `On Prem AI`
  - `AI Infrastructure` vs truncated `AIInfrast`
  - `AI Act` vs `EU AI Act`
  - `Continuity` vs `Digital Continuity`
  - `Long Lived AI` vs `Long Lived Systems`
  - `AI Governance` vs `Governance`
  - `GRC` vs `Governance Risk Compliance`
  - `Witness Trail` vs truncated `WitnessTra`
  - `Systems Architecture` vs truncated `SystemArchitec`
  - `Trust` vs `Trusts`

## Top Recurring Themes Inferred From Titles And Tags

- AGI as continuity / coexistence / bounded subjecthood
- L4, SER, review layers, protocol discipline, and governance under constraints
- Local-first AI, private compute, racks at home, and post-cloud infrastructure
- Evidence, provenance, auditability, review, and public verification surfaces
- Books and adjacent narrative layer around `Qubit of Hope`
- Home robots, domestic infrastructure, and embodied or presence-oriented AI

## Pages That Currently Power Diary

- Primary landing page: `/diary/`
- Chronological surface: `/diary/archive/`
- Tag surface: `/diary/tags/`
- Start-here discovery page: `/diary/start-here/`
- Theme index: `/diary/themes/`
- Theme pages: `/diary/themes/<theme-slug>/`
- Per-post pages: `/diary/<post-slug>/`
- Machine-readable surfaces:
  - `/diary-index.json`
  - `/diary-latest.json`
  - `/diary-tags.json`
  - `/diary-start-here.json`
  - `/diary-themes.json`
  - `/diary-cornerstones.json`
  - `/diary-tag-map.json`
  - `/diary-feed.xml`

## Inventory Conclusion

- The corpus is already large enough that a flat archive is no longer a sufficient discovery surface.
- The archive supports real curation because the tag/title distribution shows stable topic clusters across four months.
- The main V43 need was structural: entry points, grouping, tag normalization, and related navigation.
