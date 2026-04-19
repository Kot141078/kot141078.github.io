# TAG_NORMALIZATION_AUDIT

## Scope

- Contract: `SITE_DIARY_CURATION_AND_DISCOVERY_V43`
- Normalization layer implemented in the diary builder, not by mass-rewriting historical source entries
- Raw historical tags remain preserved in post payloads as `raw_tags`

## Source Surface

- Raw unique tag count: `289`
- Canonical normalized display-tag count after V43: `268`
- Net reduction at the public taxonomy layer: `21` raw labels absorbed into canonical display tags

## Normalization Rules

- Keep historical raw source tags intact in content files and JSON payloads.
- Generate canonical display tags at build time.
- Surface canonical tags on:
  - `/diary/`
  - `/diary/tags/`
  - canonical tag pages
  - per-post tag chips
  - related-post scoring
- Preserve discoverability for old/raw labels through alias pages that point to the canonical page.
- Do not invent merges when the corpus does not provide enough evidence.

## Canonical Groups Added

### Confirmed duplicate / near-duplicate groups

- `AI`
  - aliases: `AI`, `Artificial Intelligence`
- `Advanced Global Intelligence`
  - aliases: `Advanced Global Intelligence`, `AGI`, `AdvancedGlobalIntelligencefety`
- `L4`
  - aliases: `L4`, `L4 Boundary`, `L4 Witness`, `Reality Bound`, `Reality Bound AI`, `Reality Boundary`
- `SER`
  - aliases: `SER`, `SER FED`
- `Human-Centered AI`
  - aliases: `Human Centered AI`, `Human Centric AI`
- `Local-first AI`
  - aliases: `Local AI`, `Local First`, `On Prem AI`
- `AI Infrastructure`
  - aliases: `AI Infrastructure`, `AIInfrast`
- `AI Act`
  - aliases: `AI Act`, `EU AI Act`
- `Continuity`
  - aliases: `Continuity`, `Digital Continuity`
- `Long-Lived AI`
  - aliases: `Long Lived AI`, `Long Lived Systems`
- `AI Governance`
  - aliases: `AI Governance`, `Governance`
- `GRC`
  - aliases: `GRC`, `Governance Risk Compliance`
- `Witness Trail`
  - aliases: `Witness Trail`, `WitnessTra`
- `Systems Architecture`
  - aliases: `Systems Architecture`, `SystemArchitec`
- `Trust`
  - aliases: `Trust`, `Trusts`

## Groups Explicitly Reviewed But Not Force-Merged

- `Qubit of Hope`, `Book Release`, and `English Edition` were left as distinct tags because they describe different surfaces of the book layer rather than a clear alias collision.
- `AI Safety` already appeared in clean form; no `AISafety` raw label was found in the current corpus, so no synthetic merge was introduced.
- `Cybernetics`, `AI Architecture`, `Systems Thinking`, and several other high-frequency tags were already consistent enough to stay canonical as-is.

## Public Display Effect

- `/diary/tags/` now shows canonical display tags instead of raw-noise clutter.
- Canonical tag pages carry the main public taxonomy.
- Raw alias URLs remain available as thin alias pages with canonical pointers, so old or guessed tag URLs still resolve cleanly.
- Per-post pages now display canonical tags while preserving raw history inside machine-readable payloads.

## Builder-Level Consequences

- Related-post scoring now uses canonical normalized tags rather than raw tag drift.
- Theme grouping can rely on stable tag semantics instead of raw alias variance.
- Public tag counts now represent grouped meaning rather than fragmented label variants.

## Audit Conclusion

- The V43 taxonomy pass stayed fail-closed: it cleaned public display without silently rewriting archive history.
- The normalization map is deliberately explicit and narrow; it solves real alias pressure that the corpus actually exhibits.
