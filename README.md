# kot141078.github.io

Static user-site repository for `ivankotov.eu`.

## What this is

This repository serves a minimal public entry page for:

- `advanced-global-intelligence`
- `sovereign-entity-recursion`
- `ester-reality-bound`
- `ester-clean-code`

It also includes canonical layer hardening through:

- `c = a + b`
- `L4`
- `SER`
- `Qubit of Hope — Volume I`
- `glossary`
- `reading-path`
- `llms.txt`
- `canonical-map.json`

Current semantic layer: `v0.3`.

It is a plain static site: HTML + CSS + JSON/JSON-LD only, no build step, no package manager, no framework.

## Primary domain

- Primary custom domain: `ivankotov.eu`
- GitHub Pages source: branch `main`, path `/`

## Canonical pages

- `index.html`
- `advanced-global-intelligence/index.html`
- `c-a-plus-b/index.html`
- `l4/index.html`
- `ser/index.html`
- `qubit-of-hope/index.html`
- `glossary/index.html`
- `reading-path/index.html`

## Machine-readable layer

- `llms.txt` — compact machine-facing site guide
- `canonical-map.json` — simple node map and reading order

## Updating content

1. Edit the static files in the repository root or canonical subdirectories.
2. Keep canonical wording aligned with the public corpus; do not add new theories or unsupported claims.
3. Commit changes on `main`.
4. Push to `origin`.

## Secondary domain

`advancedglobalintelligence.eu` is not connected as a second GitHub Pages custom domain.

Use the redirect plan in `REDIRECT_PLAN_ADVANCEDGLOBALINTELLIGENCE_EU.md` and configure a manual `301` redirect in OVH to:

`https://ivankotov.eu/advanced-global-intelligence/`
