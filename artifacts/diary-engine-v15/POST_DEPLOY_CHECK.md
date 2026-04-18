# Post-Deploy Check — V15

Date: 2026-04-18
Implementation commit: `ece05b9231ee772184bbe46a048407882981e5c4`
Primary domain: `https://ivankotov.eu/`

## URL status

- `/` -> `200`
- `/diary/` -> `200`
- `/diary/archive/` -> `200`
- `/diary/tags/` -> `200`
- `/diary-index.json` -> `200`
- `/diary-tags.json` -> `200`
- `/diary-feed.xml` -> `200`
- `/llms.txt` -> `200`
- `/sitemap.xml` -> `200`
- `/styles.css` -> `200`

## Content assertions

### Home

- `Archive slot` present: pass
- `Diary archive is being prepared.` present: pass
- archive link present: pass
- tags link present: pass

### Diary

- `Blog` schema present: pass
- `BreadcrumbList` schema present: pass
- `Prepared for batch import` text present: pass
- archive link present: pass
- tags link present: pass

### Diary archive

- `CollectionPage` schema present: pass
- `BreadcrumbList` schema present: pass
- `Archive chronology is empty.` present: pass
- tags link present: pass

### Diary tags

- `CollectionPage` schema present: pass
- `BreadcrumbList` schema present: pass
- `No tag pages exist yet.` present: pass
- archive link present: pass

### Machine-readable layer

- `diary-index.json` contains `"count": 0`: pass
- `diary-index.json` contains `"latest": null`: pass
- `diary-index.json` contains `"items": []`: pass
- `diary-tags.json` contains diary tags page URL: pass
- `diary-tags.json` contains empty tags list: pass
- `diary-feed.xml` contains valid RSS root: pass
- `diary-feed.xml` contains canonical diary link: pass
- `llms.txt` contains `/diary/archive/`: pass
- `llms.txt` contains `/diary/tags/`: pass
- `llms.txt` contains `/diary-feed.xml`: pass
- `sitemap.xml` contains `/diary/archive/`: pass
- `sitemap.xml` contains `/diary/tags/`: pass

### Mobile-safe evidence

- live `styles.css` still contains `@media (max-width: 820px)`: pass
- live `styles.css` still contains `.site-nav`: pass
- live `styles.css` still contains `.archive-grid`: pass
- live `styles.css` still contains `.entry-list`: pass
- live `styles.css` still contains `.surface-grid`: pass

## No fake posts check

- `diary-index.json` reports `count: 0`: pass
- generated public diary tree contains only `/diary/`, `/diary/archive/`, and `/diary/tags/` in this pass: pass
- no fake per-post pages were published: pass

## Pages build trace

- GitHub commit workflow runs exposed for `ece05b9231ee772184bbe46a048407882981e5c4`: none
- Combined commit statuses exposed for `ece05b9231ee772184bbe46a048407882981e5c4`: none
- GitHub Pages latest build API for this repo returned `404 Not Found`
- Live URL checks confirm the deployed public surface is serving the V15 diary engine outputs
