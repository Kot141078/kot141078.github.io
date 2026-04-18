# Diary Content

Use this directory for real diary entries only.

- Keep each published entry in one Markdown file.
- Do not invent or pre-seed public posts.
- Keep `_template.md` as the starting structure for future imports.
- After adding or changing entries, run `python tools/build_diary.py`.

The builder skips:

- files starting with `_`
- `README.md`

Expected source format:

- front matter between `---` lines
- Markdown body after the closing `---`

Required fields:

- `title`
- `date`
- `slug`
- `summary`

Optional fields:

- `tags`
- `primary_image`
- `image_alt`
- `linkedin_url`
- `extra_images`

`date` must use ISO format: `YYYY-MM-DD`.
