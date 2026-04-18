# Post-Deploy Check — V16

Date: 2026-04-18
Implementation commit: `7c5ed18c8040dd0c39d31ad104b311d662d6607d`
Imported slug: `agi-public-release-v1-1`
Primary domain: `https://ivankotov.eu/`

## URL status

Initial propagation check immediately after push:

- `/` -> `200`
- `/diary/` -> `200`
- `/diary/archive/` -> `200`
- `/diary/tags/` -> `200`
- `/diary/agi-public-release-v1-1/` -> `404`
- `/diary/tags/agi/` -> `404`
- `/diary/tags/ai-safety/` -> `404`
- `/diary/tags/cybernetics/` -> `404`
- `/diary/tags/decentralized-ai/` -> `404`
- `diary-index.json` -> `200`
- `diary-tags.json` -> `200`
- `diary-feed.xml` -> `200`
- `llms.txt` -> `200`
- `sitemap.xml` -> `200`

Follow-up check after propagation delay:

- `/` -> `200`
- `/diary/` -> `200`
- `/diary/archive/` -> `200`
- `/diary/tags/` -> `200`
- `/diary/agi-public-release-v1-1/` -> `200`
- `/diary/tags/agi/` -> `200`
- `/diary/tags/ai-safety/` -> `200`
- `/diary/tags/cybernetics/` -> `200`
- `/diary/tags/decentralized-ai/` -> `200`
- `diary-index.json` -> `200`
- `diary-tags.json` -> `200`
- `diary-feed.xml` -> `200`
- `llms.txt` -> `200`
- `sitemap.xml` -> `200`
- `styles.css` -> `200`

## Content assertions

- home latest-post slot title present: pass
- home latest-post slot link present: pass
- home latest-post slot has no image tag: pass
- `/diary/` shows the imported entry: pass
- `/diary/archive/` shows the imported entry: pass
- `/diary/tags/` shows AGI: pass
- `/diary/tags/` shows AI Safety: pass
- `/diary/tags/` shows Cybernetics: pass
- `/diary/tags/` shows Decentralized AI: pass
- `/diary/tags/agi/` shows the imported entry: pass
- `/diary/tags/ai-safety/` shows the imported entry: pass
- `/diary/tags/cybernetics/` shows the imported entry: pass
- `/diary/tags/decentralized-ai/` shows the imported entry: pass

## Post page assertions

- `BlogPosting` schema present: pass
- `BreadcrumbList` schema present: pass
- `mainEntityOfPage` present: pass
- `keywords` present: pass
- `LinkedIn origin trace` present: pass
- `og:image` absent: pass
- `<img>` absent: pass

## Machine-readable layer

- `diary-index.json` has `count: 1`: pass
- `diary-index.json` contains imported slug: pass
- `diary-tags.json` contains 4 tags: pass
- `diary-feed.xml` contains one `<item>`: pass
- `diary-feed.xml` contains the imported title: pass

## Sitemap and mobile-safe evidence

- `sitemap.xml` contains the imported post URL: pass
- `sitemap.xml` contains the generated AI Safety tag URL: pass
- live `styles.css` keeps `@media (max-width: 820px)`: pass
- live `styles.css` keeps `.archive-grid`: pass
- live `styles.css` keeps `.entry-list`: pass

## No fake image check

- no primary image was introduced into the source entry: pass
- no post-page image element was rendered: pass
- no latest-slot image element was rendered: pass

## Pages build trace

- GitHub commit workflow runs exposed for `7c5ed18c8040dd0c39d31ad104b311d662d6607d`: none
- Combined commit statuses exposed for `7c5ed18c8040dd0c39d31ad104b311d662d6607d`: none
- Public deploy was confirmed by live URL checks after a short propagation delay
