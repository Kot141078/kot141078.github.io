# Visual Layer Audit

## Scope and method

- `styles.css` diff relative to baseline: empty
- `git diff --stat` relative to baseline: empty
- New public assets since baseline: none
- Live inspection method: repo HTML/CSS review plus live HTML fetches of `https://ivankotov.eu/`, `/corpus-map/`, and `/services/`
- Screenshot extraction: not performed; no browser screenshot tooling was used in this audit

## Delta result

There is no visual delta since the requested freeze baseline because `HEAD` equals the baseline commit.

Any visual characteristics described below are properties of the current frozen site state, not post-freeze changes.

## Current visual layer snapshot

- Palette: warm neutral background, light panels, muted blue accent, soft shadows
- Typography: serif headings and brand, sans-serif body, monospace for code/status labels
- Layout system: repeated bordered panels, hero + section rhythm, card grids, table wraps, dense header navigation
- Home priority: identity first, then corpus structure, then entry layers, then public works/evidence
- Canonical pages: compact and dry; they stay text-first and avoid decorative media
- Library / downloads: strong tabular and inventory-oriented treatment
- Services / use-cases / contact: practical layer uses the same card system rather than a separate visual language
- Topics: compact three-card hub with clear topic branching

## Good changes to keep in a future pass

These are current-state strengths, not new deltas:

- The visual system is consistent across canonical, practical, and topic pages.
- The site remains text-first and review-oriented rather than sales-oriented.
- Repeated card/table motifs make source surfaces and practical surfaces legible.
- The warm-neutral palette softens the site without turning it into a generic startup UI.

## Neutral changes / traits

- The palette is less austere than a strict white/gray engineering shell, but it still reads as controlled and non-marketing.
- Rounded panels and soft shadows add polish without changing the informational hierarchy.
- Different nav subsets per page reduce total clutter on subpages, even though the global home nav remains dense.

## Suspicious changes / risks

Again, these are current-state risks, not baseline deltas:

- The home navigation is broad and crowded; the site exposes many entry modes at once.
- Multiple entry surfaces overlap semantically: `About`, `Corpus map`, `Start here`, `Reading path`, `Library`, `Downloads`, `Publications`, `Evidence`, `Services`, `Use cases`, and `Topics`.
- The current visual layer does not visibly separate "canonical", "practical", and "narrative" strongly enough to offset the breadth of the nav.
- The warm, polished visual treatment is acceptable, but any additional polish pass could easily push the site away from a dry engineering tone.

## Does the visual layer break the dry engineering style?

No, not at the current frozen state.

It is slightly softer and more polished than a severe engineering shell, but the site is still dominated by text, inventory tables, compact cards, evidence/release framing, and explicit negative framing. The bigger risk is breadth and overlap, not visual softness.

## Should the current visual layer be preserved in the next pass?

Yes, with restraint.

- Preserve the current CSS and layout primitives unless integration work exposes a concrete hierarchy problem.
- Do not run a standalone visual redesign next.
- If a later cleanup pass happens, it should reduce overlap and nav pressure rather than introduce more styling.

## Reference pages used for visual inspection

- Home: `https://ivankotov.eu/`
- Canonical page: `https://ivankotov.eu/corpus-map/`
- Practical page: `https://ivankotov.eu/services/`
