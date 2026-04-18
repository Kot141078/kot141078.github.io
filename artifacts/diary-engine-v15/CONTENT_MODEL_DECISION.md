# Content Model Decision

## Decision

Use one Markdown file per diary entry with:

- YAML-like front matter between `---` delimiters
- one Markdown body after the closing delimiter

## Why this format

- Simple to parse with Python stdlib only.
- Stable for batch imports through Codex.
- Explicit enough to prevent hidden assumptions about dates, tags, slugs, and images.
- Easy to diff in git.
- Easy to review before publication.
- Does not require a CMS or framework.

## Required front matter keys

- `title`
- `date`
- `slug`
- `summary`
- `tags`
- `primary_image`
- `image_alt`
- `linkedin_url`

## Optional front matter keys

- `extra_images`

## Required body rule

- The Markdown body is required after the closing `---`.

## Validation stance

- `title`, `date`, `slug`, and `summary` must be non-empty.
- `tags`, `primary_image`, `image_alt`, and `linkedin_url` must remain explicit keys even when empty.
- `date` must normalize to ISO `YYYY-MM-DD`.
- `slug` must be lowercase ASCII plus hyphens.
- image paths must resolve to real files if they are provided.

## Why not a more exotic format

- No custom parser is needed.
- No opaque serialization is introduced.
- No HTML hand-editing is required for future imports.
- No dependency on external tooling or admin interfaces is introduced.
