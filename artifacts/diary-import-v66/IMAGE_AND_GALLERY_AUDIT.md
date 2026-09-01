# V66 Image and Gallery Audit

Verdict: `PASS`. All ten supplied source files existed, were readable, decoded successfully, and were copied without transformation. Source and destination size/SHA-256 are identical in every row.

## Image custody map

| Entry/order | Source path | Source format and dimensions | Source bytes | Source SHA-256 | Destination path | Destination format and bytes | Destination SHA-256 | Transform |
| --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| 0212/1 | `C:\Users\kotov\Downloads\1786378756096.jpg` | JPEG, 1122x1402 | 285029 | `9d41e9a2bea0b1e972048d8284b3551ae4fdfc75c65b1aa594a5f1a0a3b5a425` | `assets/diary/published-pasc-f0-gap-closure-scaffold-and-structural-templates-v0-1-1/cover.jpg` | JPEG, 285029 | `9d41e9a2bea0b1e972048d8284b3551ae4fdfc75c65b1aa594a5f1a0a3b5a425` | none |
| 0213/1 | `C:\Users\kotov\Downloads\1786486971665.jpg` | JPEG, 1672x941 | 229634 | `d25d34882785c6f1de15baaeebf33c830cf58bca95653aa4f78f5fbcf94f6f93` | `assets/diary/every-now-and-then-between-my-usual-thoughts-on-ai-infrastructure-and-machine-intelligence-the-old-pc-geek-in-me-stages-a-small-rebellion/cover.jpg` | JPEG, 229634 | `d25d34882785c6f1de15baaeebf33c830cf58bca95653aa4f78f5fbcf94f6f93` | none |
| 0214/1 | `C:\Users\kotov\Downloads\1786444189412.jpg` | JPEG, 1672x941 | 230411 | `168175f61baebec4d68d3117a9ffd0c4740c3feaa5b304c1b516a7d827dfd68b` | `assets/diary/what-do-we-really-expect-from-ai/cover.jpg` | JPEG, 230411 | `168175f61baebec4d68d3117a9ffd0c4740c3feaa5b304c1b516a7d827dfd68b` | none |
| 0215/1 | `C:\Users\kotov\Downloads\1786452670391.jpg` | JPEG, 1672x941 | 228308 | `f3662419b8987717a2cd1d243784661e92af9af19f6a8f2d0df073f275272ebf` | `assets/diary/sooner-or-later-we-will-have-to-negotiate-with-ai/cover.jpg` | JPEG, 228308 | `f3662419b8987717a2cd1d243784661e92af9af19f6a8f2d0df073f275272ebf` | none |
| 0216/1 | `C:\Users\kotov\Downloads\1786468723287.jpg` | JPEG, 1672x941 | 283825 | `376ce8fb3e5fbd0dde614a9cca434db2c88d80bdd4877c280ce6465738918876` | `assets/diary/sometimes-useful-reading-for-ai-can-be-found-in-places-where-nobody-thinks-to-look/cover.jpg` | JPEG, 283825 | `376ce8fb3e5fbd0dde614a9cca434db2c88d80bdd4877c280ce6465738918876` | none |
| 0216/2 | `C:\Users\kotov\Downloads\1786468722990.jpg` | JPEG, 1672x941 | 272878 | `4f06b653ec879d8d2fcb0f5a801da93778dbbadf4168bc3f934747f9a12f7613` | `assets/diary/sometimes-useful-reading-for-ai-can-be-found-in-places-where-nobody-thinks-to-look/image-02.jpg` | JPEG, 272878 | `4f06b653ec879d8d2fcb0f5a801da93778dbbadf4168bc3f934747f9a12f7613` | none |
| 0216/3 | `C:\Users\kotov\Downloads\1786468723662.jpg` | JPEG, 1672x941 | 357097 | `9698f7065ca723bea10f22d07cf79d9978b1592f00d0f01cefb08fc8370da8cb` | `assets/diary/sometimes-useful-reading-for-ai-can-be-found-in-places-where-nobody-thinks-to-look/image-03.jpg` | JPEG, 357097 | `9698f7065ca723bea10f22d07cf79d9978b1592f00d0f01cefb08fc8370da8cb` | none |
| 0216/4 | `C:\Users\kotov\Downloads\1786468723003.jpg` | JPEG, 1672x941 | 235785 | `47180d6913007663c7a2de3db04717e036f95bc5a2def3744f6f06b44fd8a747` | `assets/diary/sometimes-useful-reading-for-ai-can-be-found-in-places-where-nobody-thinks-to-look/image-04.jpg` | JPEG, 235785 | `47180d6913007663c7a2de3db04717e036f95bc5a2def3744f6f06b44fd8a747` | none |
| 0216/5 | `C:\Users\kotov\Downloads\1786468723247.jpg` | JPEG, 1672x941 | 279503 | `5bd18bd98358b6ff253fd96b7cbd586a5f36f27d4c6f4154b302ce503b2a4ef1` | `assets/diary/sometimes-useful-reading-for-ai-can-be-found-in-places-where-nobody-thinks-to-look/image-05.jpg` | JPEG, 279503 | `5bd18bd98358b6ff253fd96b7cbd586a5f36f27d4c6f4154b302ce503b2a4ef1` | none |
| 0217/1 | `C:\Users\kotov\Downloads\Парящий кристаллический храм над древним монолитом.png` | PNG, 1672x941 | 2624481 | `dc58c8fbc5f91a0f5598c99f81175bcf5a9f87045c513b904844536aac59d531` | `assets/diary/the-ai-system-is-not-the-model/cover.png` | PNG, 2624481 | `dc58c8fbc5f91a0f5598c99f81175bcf5a9f87045c513b904844536aac59d531` | none |

Summary:

- Source images expected/found: 10/10.
- Destination assets: 10.
- Distinct V66 hashes: 10.
- Transformed images: 0.
- Placeholder/substitution/reuse: none.
- V66 hash collision with baseline assets: none.

## ENTRY 0216 authored order and cover rule

The canonical `extra_images` field already existed before V66. The source declares the four non-cover assets in this order:

1. `cover.jpg` from `1786468723287.jpg` - lead and card cover.
2. `image-02.jpg` from `1786468722990.jpg`.
3. `image-03.jpg` from `1786468723662.jpg`.
4. `image-04.jpg` from `1786468723003.jpg`.
5. `image-05.jpg` from `1786468723247.jpg`.

The first supplied image is the primary article image and the landing/archive card cover. This follows the contract's fallback rule and the existing builder's primary-image projection behavior. Open Graph, JSON-LD, and `diary-index.json` continue to expose only this primary image; the canonical source and article page preserve the ordered gallery.

## Gallery DOM and builder path

Gallery support existed before V66: **yes**. Builder renderer changed for gallery: **yes**.

The backwards-compatible renderer hardening produces:

```html
<figure class="entry-cover diary-gallery-lead">...</figure>
<section class="section diary-gallery" aria-label="Entry image gallery">
  <div class="archive-grid diary-gallery-grid">
    <figure class="entry-cover diary-gallery-item">...</figure>
    <figure class="entry-cover diary-gallery-item">...</figure>
    <figure class="entry-cover diary-gallery-item">...</figure>
    <figure class="entry-cover diary-gallery-item">...</figure>
  </div>
</section>
```

- Lead figures are used only when `extra_images` is non-empty.
- Existing single-image entries retain their legacy `<div class="entry-cover">` structure.
- Image-less entries remain image-less.
- Images 2-5 use `loading="lazy"` and `decoding="async"`.
- There are no `figcaption` elements and no invented captions.
- There is no carousel script or external dependency.

Alt sequence:

1. `Pavel Bazhov reading image 1 of 5.`
2. `Pavel Bazhov reading image 2 of 5`
3. `Pavel Bazhov reading image 3 of 5`
4. `Pavel Bazhov reading image 4 of 5`
5. `Pavel Bazhov reading image 5 of 5`

No person, edition, location, character, or depicted narrative was inferred beyond the source-safe generic label.

## Responsive and print result

Desktop:

- Lead image is visually distinct above the text.
- Remaining four images form a balanced 2x2 grid.
- Gallery element measured 1080x753 CSS pixels during local validation.
- All four thumbnails loaded at 1672x941; no distortion and no horizontal overflow.

Mobile:

- At 390x844, the gallery becomes one column.
- Document/client widths are 390/390; gallery links and images do not overflow.
- All five images load at their 1672x941 natural dimensions.

Print:

- Gallery figures use `break-inside: avoid` and `page-break-inside: avoid`.
- Gallery remains two-column in print.
- A separately rendered four-page A4 ENTRY 0216 probe places all four gallery images together in a readable 2x2 grid; there is no gallery image-only blank page.
- The required Diary landing A4 artifact is seven pages at 595.92x841.92 points; trailing blank pagination was eliminated.

## Legacy-entry regression result

- Baseline entries with gallery data: 0/211; V66 gallery selectors therefore apply to only ENTRY 0216.
- `we-are-building-a-partner` single-image fixture: full page byte-identical.
- `geoffrey-hinton-is-right-ai-is-immortal` single-image fixture: entry core and hero byte-identical; only builder-recomputed related cards changed.
- `agi-public-release-v1-1` image-less fixture: full page byte-identical.
- All 211 baseline entry cores, hero behavior, and tails remain unchanged.
- 193/211 complete pages are byte-identical; 18/211 differ only within related-post cards because the six new entries participate in normal related-entry selection.

## Remote image result

All ten cache-busted asset URLs returned HTTP 200 after Pages deployment. Every remote byte stream matched the source/destination SHA-256 above. JPEG responses used `image/jpeg`; ENTRY 0217 used `image/png` and began with the valid PNG signature `89 50 4e 47 0d 0a 1a 0a`.

Final verdicts:

- ENTRY 0216 five-image count/order: `PASS`.
- ENTRY 0216 cover selection: `PASS`.
- Responsive gallery: `PASS`.
- Print gallery: `PASS`.
- Old single-image entry: `PASS`.
- Old image-less entry: `PASS`.
- ENTRY 0217 genuine PNG: `PASS`.
