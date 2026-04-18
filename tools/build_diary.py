from __future__ import annotations

import html
import json
import re
import shutil
from dataclasses import dataclass
from datetime import date, datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content" / "diary"
DIARY_DIR = ROOT / "diary"
HOME_PATH = ROOT / "index.html"
DIARY_INDEX_JSON = ROOT / "diary-index.json"
DIARY_TAGS_JSON = ROOT / "diary-tags.json"
DIARY_LATEST_JSON = ROOT / "diary-latest.json"
DIARY_FEED_XML = ROOT / "diary-feed.xml"
HOME_SLOT_START = "<!-- diary-slot:start -->"
HOME_SLOT_END = "<!-- diary-slot:end -->"

SITE_TITLE = "Ivan Kotov — Advanced Global Intelligence, c = a + b, L4, SER"
DIARY_TITLE = "Diary — posts, notes, and visual archive | Ivan Kotov"
DIARY_DESCRIPTION = "Public archive surface for posts, notes, and linked visual materials related to the corpus."
DIARY_ARCHIVE_TITLE = "Diary archive | Ivan Kotov"
DIARY_ARCHIVE_DESCRIPTION = "Chronological archive surface for public posts and notes."
DIARY_TAGS_TITLE = "Diary tags | Ivan Kotov"
DIARY_TAGS_DESCRIPTION = "Tag-based entry into the diary archive."
SITE_URL = "https://ivankotov.eu/"
DIARY_URL = "https://ivankotov.eu/diary/"
DIARY_ARCHIVE_URL = "https://ivankotov.eu/diary/archive/"
DIARY_TAGS_URL = "https://ivankotov.eu/diary/tags/"

NON_EMPTY_FIELDS = ("title", "date", "slug", "summary")
EXPLICIT_FIELDS = ("title", "date", "slug", "summary", "tags", "primary_image", "image_alt", "linkedin_url")
OPTIONAL_FIELDS = ("extra_images",)


@dataclass(frozen=True)
class TagRef:
    name: str
    slug: str


@dataclass(frozen=True)
class Entry:
    source_path: Path
    title: str
    entry_date: date
    slug: str
    summary: str
    tags: list[TagRef]
    primary_image: str
    image_alt: str
    linkedin_url: str
    extra_images: list[str]
    body_markdown: str

    @property
    def url(self) -> str:
        return f"{DIARY_URL}{self.slug}/"

    @property
    def date_iso(self) -> str:
        return self.entry_date.isoformat()

    @property
    def feed_date(self) -> str:
        return format_datetime(
            datetime(self.entry_date.year, self.entry_date.month, self.entry_date.day, 12, 0, tzinfo=timezone.utc)
        )


@dataclass(frozen=True)
class TagInfo:
    name: str
    slug: str
    entries: list[Entry]

    @property
    def url(self) -> str:
        return f"{DIARY_TAGS_URL}{self.slug}/"

    @property
    def count(self) -> int:
        return len(self.entries)


def nav_markup(prefix: str, current: str) -> str:
    items = [
        ("Home", f"{prefix}"),
        ("Start here", f"{prefix}start-here/"),
        ("Diary", f"{prefix}diary/"),
        ("Topics", f"{prefix}topics/"),
        ("Library", f"{prefix}library/"),
        ("Services", f"{prefix}services/"),
        ("About", f"{prefix}about/"),
        ("Contact", f"{prefix}contact/"),
    ]
    links = []
    for label, href in items:
        current_attr = ' aria-current="page"' if label == current else ""
        links.append(f'        <a href="{href}"{current_attr}>{html.escape(label)}</a>')
    return "\n".join(
        [
            '    <header class="site-header">',
            f'      <a class="brand" href="{prefix}">',
            '        <span class="brand-name">Ivan Kotov</span>',
            '        <span class="brand-role">AI Systems Architect</span>',
            "      </a>",
            '      <nav class="site-nav" aria-label="Primary">',
            *links,
            "      </nav>",
            "    </header>",
        ]
    )


def load_entries() -> list[Entry]:
    entries: list[Entry] = []
    seen_slugs: set[str] = set()

    if not CONTENT_DIR.exists():
        return entries

    for path in sorted(CONTENT_DIR.glob("*.md")):
        if path.name == "README.md" or path.name.startswith("_"):
            continue
        entry = parse_entry(path)
        if entry.slug in seen_slugs:
            raise ValueError(f"Duplicate diary slug: {entry.slug}")
        seen_slugs.add(entry.slug)
        entries.append(entry)

    entries.sort(key=lambda item: (item.entry_date, item.slug), reverse=True)
    return entries


def parse_entry(path: Path) -> Entry:
    raw = path.read_text(encoding="utf-8").lstrip("\ufeff")
    front_matter, body = split_front_matter(raw, path)
    metadata = parse_front_matter(front_matter, path)

    for key in EXPLICIT_FIELDS:
        if key not in metadata:
            raise ValueError(f"{path} is missing explicit front matter key: {key}")
    for key in NON_EMPTY_FIELDS:
        if not metadata.get(key, "").strip():
            raise ValueError(f"{path} is missing required non-empty field: {key}")

    title = metadata["title"].strip()
    entry_date = date.fromisoformat(metadata["date"].strip())
    slug = metadata["slug"].strip()
    summary = metadata["summary"].strip()
    primary_image = metadata["primary_image"].strip()
    image_alt = metadata["image_alt"].strip()
    linkedin_url = metadata["linkedin_url"].strip()
    extra_images = split_csv(metadata.get("extra_images", ""))
    tags = parse_tags(metadata["tags"], path)

    validate_slug(slug, path)
    validate_linkedin_url(linkedin_url, path)
    validate_images(primary_image, image_alt, extra_images, path)

    if not body.strip():
        raise ValueError(f"{path} is missing a body")

    return Entry(
        source_path=path,
        title=title,
        entry_date=entry_date,
        slug=slug,
        summary=summary,
        tags=tags,
        primary_image=primary_image,
        image_alt=image_alt,
        linkedin_url=linkedin_url,
        extra_images=extra_images,
        body_markdown=body.strip(),
    )


def split_front_matter(raw: str, path: Path) -> tuple[str, str]:
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)\Z", raw, re.DOTALL)
    if not match:
        raise ValueError(f"{path} must use front matter delimited by ---")
    return match.group(1), match.group(2)


def parse_front_matter(front_matter: str, path: Path) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for line in front_matter.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"{path} has malformed front matter line: {line}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata


def split_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def normalize_tag_slug(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized


def parse_tags(raw_tags: str, path: Path) -> list[TagRef]:
    tags: list[TagRef] = []
    seen_slugs: set[str] = set()
    for tag in split_csv(raw_tags):
        slug = normalize_tag_slug(tag)
        if not slug:
            raise ValueError(f"{path} contains a tag that cannot be normalized into an ASCII slug: {tag}")
        if slug in seen_slugs:
            continue
        seen_slugs.add(slug)
        tags.append(TagRef(name=tag, slug=slug))
    return tags


def validate_slug(slug: str, path: Path) -> None:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError(f"{path} has invalid slug: {slug}")


def validate_linkedin_url(linkedin_url: str, path: Path) -> None:
    if linkedin_url and not linkedin_url.startswith(("http://", "https://")):
        raise ValueError(f"{path} has an invalid linkedin_url: {linkedin_url}")


def validate_images(primary_image: str, image_alt: str, extra_images: Iterable[str], path: Path) -> None:
    if primary_image:
        candidate = ROOT / primary_image
        if not candidate.exists():
            raise ValueError(f"{path} references a missing primary image: {primary_image}")
        if not image_alt:
            raise ValueError(f"{path} must provide image_alt when primary_image is present")
    elif image_alt:
        raise ValueError(f"{path} sets image_alt without a primary_image")

    for image in extra_images:
        candidate = ROOT / image
        if not candidate.exists():
            raise ValueError(f"{path} references a missing extra image: {image}")


def build_tag_index(entries: list[Entry]) -> list[TagInfo]:
    buckets: dict[str, list[Entry]] = {}
    display_names: dict[str, str] = {}

    for entry in entries:
        for tag in entry.tags:
            buckets.setdefault(tag.slug, []).append(entry)
            display_names.setdefault(tag.slug, tag.name)

    tag_infos = [
        TagInfo(name=display_names[slug], slug=slug, entries=sorted(items, key=lambda item: (item.entry_date, item.slug), reverse=True))
        for slug, items in buckets.items()
    ]
    tag_infos.sort(key=lambda tag: (tag.name.lower(), tag.slug))
    return tag_infos


def render_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)
    return escaped


def markdown_to_html(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    chunks: list[str] = []
    paragraph: list[str] = []
    list_buffer: list[str] = []
    list_kind: str | None = None
    in_code = False
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            text = " ".join(line.strip() for line in paragraph)
            chunks.append(f"<p>{render_inline(text)}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_buffer, list_kind
        if list_buffer and list_kind:
            items = "".join(f"<li>{render_inline(item)}</li>" for item in list_buffer)
            chunks.append(f"<{list_kind}>{items}</{list_kind}>")
            list_buffer = []
            list_kind = None

    for raw_line in lines:
        stripped = raw_line.strip()

        if stripped.startswith("```"):
            flush_paragraph()
            flush_list()
            if in_code:
                code_html = html.escape("\n".join(code_lines))
                chunks.append(f"<pre><code>{code_html}</code></pre>")
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_lines.append(raw_line.rstrip("\n"))
            continue

        if not stripped:
            flush_paragraph()
            flush_list()
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            flush_list()
            chunks.append(f"<h3>{render_inline(stripped[4:])}</h3>")
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            flush_list()
            chunks.append(f"<h2>{render_inline(stripped[3:])}</h2>")
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            flush_list()
            chunks.append(f"<h1>{render_inline(stripped[2:])}</h1>")
            continue

        unordered = re.match(r"^-\s+(.*)$", stripped)
        ordered = re.match(r"^\d+\.\s+(.*)$", stripped)
        if unordered:
            flush_paragraph()
            if list_kind not in (None, "ul"):
                flush_list()
            list_kind = "ul"
            list_buffer.append(unordered.group(1))
            continue
        if ordered:
            flush_paragraph()
            if list_kind not in (None, "ol"):
                flush_list()
            list_kind = "ol"
            list_buffer.append(ordered.group(1))
            continue

        flush_list()
        paragraph.append(stripped)

    flush_paragraph()
    flush_list()
    if in_code:
        raise ValueError("Unclosed code fence in diary markdown")
    return "\n          ".join(chunks)


def render_document(
    *,
    title: str,
    description: str,
    canonical: str,
    og_type: str,
    og_image: str | None,
    stylesheet_href: str,
    nav_prefix: str,
    nav_current: str,
    ld_json: str,
    body_html: str,
) -> str:
    og_image_line = f'\n  <meta property="og:image" content="{html.escape(og_image)}">' if og_image else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
  <link rel="canonical" href="{html.escape(canonical)}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:type" content="{html.escape(og_type)}">
  <meta property="og:url" content="{html.escape(canonical)}">{og_image_line}
  <script type="application/ld+json">
  {ld_json}
  </script>
  <link rel="stylesheet" href="{html.escape(stylesheet_href)}">
</head>
<body>
  <div class="site-shell">
{nav_markup(nav_prefix, nav_current)}

    <main>
{body_html}
    </main>

    <footer class="site-footer">
      <p>Primary domain: <span>ivankotov.eu</span></p>
    </footer>
  </div>
</body>
</html>
"""


def render_empty_state(title: str, text: str) -> str:
    return f"""        <div class="empty-state">
          <p><strong>{html.escape(title)}</strong></p>
          <p>{html.escape(text)}</p>
        </div>
"""


def render_entry_card(entry: Entry, *, asset_prefix: str, entry_href: str, tag_prefix: str, include_image: bool) -> str:
    image_html = ""
    if include_image and entry.primary_image:
        image_html = f"""
            <div class="entry-cover">
              <img src="{html.escape(asset_prefix + entry.primary_image)}" alt="{html.escape(entry.image_alt or entry.title)}">
            </div>
"""
    tag_links = ""
    if entry.tags:
        tag_items = "".join(
            f'              <a href="{html.escape(tag_prefix + tag.slug + "/")}">{html.escape(tag.name)}</a>\n'
            for tag in entry.tags
        )
        tag_links = "            <div class=\"section-links\">\n" + tag_items + "            </div>\n"
    return f"""          <article class="entry-card">
{image_html}            <div class="entry-meta">
              <span>{entry.date_iso}</span>
              <span>{html.escape(entry.slug)}</span>
            </div>
            <h3>{html.escape(entry.title)}</h3>
            <p class="entry-summary">{html.escape(entry.summary)}</p>
{tag_links}            <div class="section-links">
              <a href="{html.escape(entry_href)}">Open entry</a>
            </div>
          </article>"""


def render_latest_entries(entries: list[Entry]) -> str:
    if not entries:
        return render_empty_state(
            "No diary entries are published yet.",
            "The latest-entries slot is ready for future batch imports, but this pass intentionally keeps the archive empty until real source materials are provided.",
        )
    cards = [
        render_entry_card(entry, asset_prefix="../", entry_href=f"./{entry.slug}/", tag_prefix="./tags/", include_image=True)
        for entry in entries[:3]
    ]
    return "        <div class=\"archive-grid\">\n" + "\n".join(cards) + "\n        </div>\n"


def render_archive_preview(entries: list[Entry]) -> str:
    if not entries:
        return render_empty_state(
            "Archive list is empty.",
            "Entries will appear here in reverse chronological order after real batches are imported.",
        )
    cards = [
        render_entry_card(entry, asset_prefix="../", entry_href=f"./{entry.slug}/", tag_prefix="./tags/", include_image=False)
        for entry in entries[:4]
    ]
    return "        <div class=\"entry-list\">\n" + "\n".join(cards) + "\n        </div>\n"


def render_tag_preview(tags: list[TagInfo]) -> str:
    if not tags:
        return render_empty_state(
            "Tag surface is waiting for real entries.",
            "Tags will only be shown after imported entries bring confirmed labels.",
        )
    cards = [
        f"""          <article class="surface-group">
            <h3>{html.escape(tag.name)}</h3>
            <p>{tag.count} linked entr{'y' if tag.count == 1 else 'ies'}.</p>
            <div class="surface-links">
              <a href="./tags/{html.escape(tag.slug)}/">Open tag page</a>
            </div>
          </article>"""
        for tag in tags
    ]
    return "        <div class=\"surface-grid\">\n" + "\n".join(cards) + "\n        </div>\n"


def group_entries_by_year(entries: list[Entry]) -> list[tuple[int, list[Entry]]]:
    groups: dict[int, list[Entry]] = {}
    for entry in entries:
        groups.setdefault(entry.entry_date.year, []).append(entry)
    ordered = sorted(groups.items(), key=lambda item: item[0], reverse=True)
    return [(year, items) for year, items in ordered]


def render_archive_groups(entries: list[Entry], *, asset_prefix: str, entry_prefix: str, tag_prefix: str) -> str:
    if not entries:
        return render_empty_state(
            "Archive chronology is empty.",
            "Chronological archive groups will appear here after the first real batch import.",
        )

    groups = []
    for year, year_entries in group_entries_by_year(entries):
        cards = [
            render_entry_card(
                entry,
                asset_prefix=asset_prefix,
                entry_href=f"{entry_prefix}{entry.slug}/",
                tag_prefix=tag_prefix,
                include_image=False,
            )
            for entry in year_entries
        ]
        groups.append(
            f"""        <section class="section">
          <div class="section-head">
            <p class="section-label">Archive year</p>
            <h2>{year}</h2>
          </div>
          <div class="entry-list">
{chr(10).join(cards)}
          </div>
        </section>"""
        )
    return "\n".join(groups)


def render_tag_grid(tags: list[TagInfo], *, link_prefix: str) -> str:
    if not tags:
        return render_empty_state(
            "No tag pages exist yet.",
            "Tag pages will be generated only after imported diary entries bring confirmed tags.",
        )
    cards = []
    for tag in tags:
        cards.append(
            f"""          <article class="surface-group">
            <h3>{html.escape(tag.name)}</h3>
            <p>{tag.count} linked entr{'y' if tag.count == 1 else 'ies'} in the archive.</p>
            <div class="surface-links">
              <a href="{html.escape(link_prefix + tag.slug + "/")}">Open tag page</a>
            </div>
          </article>"""
        )
    return "        <div class=\"surface-grid\">\n" + "\n".join(cards) + "\n        </div>\n"


def render_gallery(entry: Entry) -> str:
    if not entry.extra_images:
        return ""
    cards = [
        f"""          <div class="entry-cover">
            <img src="../../{html.escape(image)}" alt="{html.escape(entry.title)} gallery image">
          </div>"""
        for image in entry.extra_images
    ]
    return f"""
        <section class="section">
          <div class="section-head">
            <p class="section-label">Gallery</p>
            <h2>Linked visual surfaces</h2>
          </div>
          <div class="archive-grid">
{chr(10).join(cards)}
          </div>
        </section>
"""


def diary_blog_ld_json(entries: list[Entry]) -> str:
    blog: dict[str, object] = {
        "@type": "Blog",
        "@id": f"{DIARY_URL}#blog",
        "url": DIARY_URL,
        "name": DIARY_TITLE,
        "description": DIARY_DESCRIPTION,
    }
    if entries:
        blog["blogPost"] = [{"@id": f"{entry.url}#post"} for entry in entries]
    graph = [
        blog,
        {
            "@type": "BreadcrumbList",
            "@id": f"{DIARY_URL}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL},
                {"@type": "ListItem", "position": 2, "name": "Diary", "item": DIARY_URL},
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def collection_ld_json(page_url: str, page_title: str, description: str, breadcrumb: list[tuple[str, str]]) -> str:
    graph = [
        {
            "@type": "CollectionPage",
            "@id": f"{page_url}#page",
            "url": page_url,
            "name": page_title,
            "description": description,
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"{page_url}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": index, "name": name, "item": item}
                for index, (name, item) in enumerate(breadcrumb, start=1)
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def post_ld_json(entry: Entry) -> str:
    graph = [
        {
            "@type": "BlogPosting",
            "@id": f"{entry.url}#post",
            "headline": entry.title,
            "url": entry.url,
            "mainEntityOfPage": entry.url,
            "datePublished": entry.date_iso,
            "dateModified": entry.date_iso,
            "author": {"@type": "Person", "name": "Ivan Kotov", "url": "https://ivankotov.eu/about/"},
            "publisher": {"@type": "Person", "name": "Ivan Kotov", "url": "https://ivankotov.eu/about/"},
            "description": entry.summary,
            "isPartOf": {"@type": "Blog", "url": DIARY_URL, "name": DIARY_TITLE},
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"{entry.url}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL},
                {"@type": "ListItem", "position": 2, "name": "Diary", "item": DIARY_URL},
                {"@type": "ListItem", "position": 3, "name": entry.title, "item": entry.url},
            ],
        },
    ]
    if entry.tags:
        graph[0]["keywords"] = ", ".join(tag.name for tag in entry.tags)
    if entry.primary_image:
        graph[0]["image"] = f"{SITE_URL}{entry.primary_image}"
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def render_diary_index(entries: list[Entry], tags: list[TagInfo]) -> str:
    empty_state = ""
    if not entries:
        empty_state = f"""
      <section class="section">
        <div class="section-head">
          <p class="section-label">Archive state</p>
          <h2>Prepared for batch import</h2>
        </div>
{render_empty_state('Diary archive is being prepared.', 'This archive is being prepared for batch import from existing post materials. No fake posts, dates, titles, tags, or images are published in this engine pass.')}
      </section>
"""

    body_html = f"""      <section class="hero">
        <p class="eyebrow">Public archive surface</p>
        <h1>Diary</h1>
        <p class="lead page-lead">Public archive of posts, notes, and linked visual surfaces.</p>
        <p class="diary-note">This archive is prepared for batch-imported posts and visual entries.</p>
      </section>

{empty_state}
      <section class="section">
        <div class="section-head">
          <p class="section-label">Latest entries</p>
          <h2>Latest surface</h2>
        </div>
{render_latest_entries(entries)}
        <div class="section-links">
          <a href="./archive/">Open archive</a>
          <a href="./tags/">Open tags</a>
        </div>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Archive</p>
          <h2>Archive preview</h2>
        </div>
{render_archive_preview(entries)}
        <div class="section-links">
          <a href="./archive/">Open full archive</a>
        </div>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Tags</p>
          <h2>Tag surface</h2>
        </div>
{render_tag_preview(tags)}
        <div class="section-links">
          <a href="./tags/">Open tag index</a>
        </div>
      </section>
"""

    return render_document(
        title=DIARY_TITLE,
        description=DIARY_DESCRIPTION,
        canonical=DIARY_URL,
        og_type="website",
        og_image=None,
        stylesheet_href="../styles.css",
        nav_prefix="../",
        nav_current="Diary",
        ld_json=diary_blog_ld_json(entries),
        body_html=body_html,
    )


def render_archive_page(entries: list[Entry]) -> str:
    body_html = f"""      <section class="hero">
        <p class="eyebrow">Chronological surface</p>
        <h1>Diary archive</h1>
        <p class="lead page-lead">Chronological archive surface for public posts and notes.</p>
        <p class="diary-note">This archive is ready for batch imports and remains empty until real diary entries are provided.</p>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Chronology</p>
          <h2>Reverse-chronological archive</h2>
        </div>
        <div class="section-links">
          <a href="../">Back to Diary</a>
          <a href="../tags/">Open tags</a>
        </div>
      </section>

{render_archive_groups(entries, asset_prefix='../../', entry_prefix='../', tag_prefix='../tags/')}
"""

    return render_document(
        title=DIARY_ARCHIVE_TITLE,
        description=DIARY_ARCHIVE_DESCRIPTION,
        canonical=DIARY_ARCHIVE_URL,
        og_type="website",
        og_image=None,
        stylesheet_href="../../styles.css",
        nav_prefix="../../",
        nav_current="Diary",
        ld_json=collection_ld_json(
            DIARY_ARCHIVE_URL,
            DIARY_ARCHIVE_TITLE,
            DIARY_ARCHIVE_DESCRIPTION,
            [("Home", SITE_URL), ("Diary", DIARY_URL), ("Archive", DIARY_ARCHIVE_URL)],
        ),
        body_html=body_html,
    )


def render_tags_index(tags: list[TagInfo]) -> str:
    body_html = f"""      <section class="hero">
        <p class="eyebrow">Tag surface</p>
        <h1>Diary tags</h1>
        <p class="lead page-lead">Tag-based entry into the diary archive.</p>
        <p class="diary-note">Tag pages are generated from explicit diary entry tags only.</p>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Tags</p>
          <h2>Generated tag index</h2>
        </div>
{render_tag_grid(tags, link_prefix='./')}
        <div class="section-links">
          <a href="../">Back to Diary</a>
          <a href="../archive/">Open archive</a>
        </div>
      </section>
"""

    return render_document(
        title=DIARY_TAGS_TITLE,
        description=DIARY_TAGS_DESCRIPTION,
        canonical=DIARY_TAGS_URL,
        og_type="website",
        og_image=None,
        stylesheet_href="../../styles.css",
        nav_prefix="../../",
        nav_current="Diary",
        ld_json=collection_ld_json(
            DIARY_TAGS_URL,
            DIARY_TAGS_TITLE,
            DIARY_TAGS_DESCRIPTION,
            [("Home", SITE_URL), ("Diary", DIARY_URL), ("Tags", DIARY_TAGS_URL)],
        ),
        body_html=body_html,
    )


def render_tag_page(tag: TagInfo) -> str:
    body_html = f"""      <section class="hero">
        <p class="eyebrow">Diary tag</p>
        <h1>{html.escape(tag.name)}</h1>
        <p class="lead page-lead">Generated tag page for diary entries linked to this explicit tag.</p>
        <p class="diary-note">{tag.count} linked entr{'y' if tag.count == 1 else 'ies'} currently in the archive.</p>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Tagged entries</p>
          <h2>Entries linked to {html.escape(tag.name)}</h2>
        </div>
        <div class="entry-list">
{chr(10).join(render_entry_card(entry, asset_prefix='../../../', entry_href='../../' + entry.slug + '/', tag_prefix='../', include_image=False) for entry in tag.entries)}
        </div>
        <div class="section-links">
          <a href="../">Back to tags</a>
          <a href="../../archive/">Open archive</a>
          <a href="../../">Back to Diary</a>
        </div>
      </section>
"""

    return render_document(
        title=f"Diary tag: {tag.name} | Ivan Kotov",
        description=f"Diary entries tagged {tag.name}.",
        canonical=tag.url,
        og_type="website",
        og_image=None,
        stylesheet_href="../../../styles.css",
        nav_prefix="../../../",
        nav_current="Diary",
        ld_json=collection_ld_json(
            tag.url,
            f"Diary tag: {tag.name} | Ivan Kotov",
            f"Diary entries tagged {tag.name}.",
            [("Home", SITE_URL), ("Diary", DIARY_URL), ("Tags", DIARY_TAGS_URL), (tag.name, tag.url)],
        ),
        body_html=body_html,
    )


def render_post_page(entry: Entry) -> str:
    image_html = ""
    if entry.primary_image:
        image_html = f"""
      <div class="entry-cover">
        <img src="../../{html.escape(entry.primary_image)}" alt="{html.escape(entry.image_alt or entry.title)}">
      </div>
"""
    tag_links = ""
    if entry.tags:
        items = "".join(f'          <a href="../tags/{html.escape(tag.slug)}/">{html.escape(tag.name)}</a>\n' for tag in entry.tags)
        tag_links = "        <div class=\"section-links\">\n" + items + "        </div>\n"
    linkedin_html = ""
    if entry.linkedin_url:
        linkedin_html = f'          <a href="{html.escape(entry.linkedin_url)}">LinkedIn origin trace</a>\n'

    body_html = f"""      <section class="hero">
        <p class="eyebrow">Diary entry</p>
        <h1>{html.escape(entry.title)}</h1>
        <div class="entry-meta">
          <span>{entry.date_iso}</span>
          <span>{html.escape(entry.slug)}</span>
        </div>
        <p class="lead page-lead">{html.escape(entry.summary)}</p>
{tag_links}      </section>

      <section class="section">
{image_html}        <div class="post-content">
          {markdown_to_html(entry.body_markdown)}
        </div>
        <div class="section-links">
          <a href="../">Diary</a>
          <a href="../archive/">Archive</a>
{linkedin_html}          <a href="../../about/">About</a>
        </div>
      </section>
{render_gallery(entry)}"""

    return render_document(
        title=f"{entry.title} | Diary | Ivan Kotov",
        description=entry.summary,
        canonical=entry.url,
        og_type="article",
        og_image=f"{SITE_URL}{entry.primary_image}" if entry.primary_image else None,
        stylesheet_href="../../styles.css",
        nav_prefix="../../",
        nav_current="Diary",
        ld_json=post_ld_json(entry),
        body_html=body_html,
    )


def make_index_payload(entries: list[Entry]) -> dict[str, object]:
    latest = entries[0] if entries else None
    items = [
        {
            "title": entry.title,
            "date": entry.date_iso,
            "slug": entry.slug,
            "summary": entry.summary,
            "tags": [tag.name for tag in entry.tags],
            "page": entry.url,
            **({"primary_image": f"{SITE_URL}{entry.primary_image}"} if entry.primary_image else {}),
            **({"linkedin_url": entry.linkedin_url} if entry.linkedin_url else {}),
        }
        for entry in entries
    ]
    latest_payload = None
    if latest is not None:
        latest_payload = {
            "title": latest.title,
            "date": latest.date_iso,
            "slug": latest.slug,
            "summary": latest.summary,
            "tags": [tag.name for tag in latest.tags],
            "page": latest.url,
            **({"primary_image": f"{SITE_URL}{latest.primary_image}"} if latest.primary_image else {}),
            **({"linkedin_url": latest.linkedin_url} if latest.linkedin_url else {}),
        }
    return {
        "site": SITE_URL,
        "page": DIARY_URL,
        "count": len(entries),
        "latest": latest_payload,
        "items": items,
    }


def make_tags_payload(tags: list[TagInfo]) -> dict[str, object]:
    return {
        "site": SITE_URL,
        "page": DIARY_TAGS_URL,
        "tags": [
            {"name": tag.name, "slug": tag.slug, "count": tag.count, "page": tag.url}
            for tag in tags
        ],
    }


def write_feed(entries: list[Entry]) -> None:
    build_date = format_datetime(datetime.now(timezone.utc))
    items = []
    for entry in entries:
        items.append(
            "\n".join(
                [
                    "    <item>",
                    f"      <title>{html.escape(entry.title)}</title>",
                    f"      <link>{html.escape(entry.url)}</link>",
                    f"      <guid>{html.escape(entry.url)}</guid>",
                    f"      <pubDate>{entry.feed_date}</pubDate>",
                    f"      <description>{html.escape(entry.summary)}</description>",
                    "    </item>",
                ]
            )
        )
    rss = "\n".join(
        [
            '<?xml version="1.0" encoding="UTF-8"?>',
            "<rss version=\"2.0\">",
            "  <channel>",
            f"    <title>{html.escape(DIARY_TITLE)}</title>",
            f"    <link>{html.escape(DIARY_URL)}</link>",
            f"    <description>{html.escape(DIARY_DESCRIPTION)}</description>",
            "    <language>en</language>",
            f"    <lastBuildDate>{build_date}</lastBuildDate>",
            *items,
            "  </channel>",
            "</rss>",
            "",
        ]
    )
    DIARY_FEED_XML.write_text(rss, encoding="utf-8")


def wipe_generated_diary_tree() -> None:
    if DIARY_DIR.exists():
        shutil.rmtree(DIARY_DIR)
    DIARY_DIR.mkdir(parents=True, exist_ok=True)


def write_diary_outputs(entries: list[Entry], tags: list[TagInfo]) -> None:
    wipe_generated_diary_tree()

    (DIARY_DIR / "index.html").write_text(render_diary_index(entries, tags), encoding="utf-8")

    archive_dir = DIARY_DIR / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    (archive_dir / "index.html").write_text(render_archive_page(entries), encoding="utf-8")

    tags_dir = DIARY_DIR / "tags"
    tags_dir.mkdir(parents=True, exist_ok=True)
    (tags_dir / "index.html").write_text(render_tags_index(tags), encoding="utf-8")

    for tag in tags:
        tag_dir = tags_dir / tag.slug
        tag_dir.mkdir(parents=True, exist_ok=True)
        (tag_dir / "index.html").write_text(render_tag_page(tag), encoding="utf-8")

    for entry in entries:
        target_dir = DIARY_DIR / entry.slug
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "index.html").write_text(render_post_page(entry), encoding="utf-8")


def write_machine_readable(entries: list[Entry], tags: list[TagInfo]) -> None:
    index_payload = make_index_payload(entries)
    DIARY_INDEX_JSON.write_text(json.dumps(index_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    latest_payload = {
        "site": SITE_URL,
        "page": DIARY_URL,
        "item": index_payload["latest"],
    }
    DIARY_LATEST_JSON.write_text(json.dumps(latest_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    tags_payload = make_tags_payload(tags)
    DIARY_TAGS_JSON.write_text(json.dumps(tags_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    write_feed(entries)


def render_home_slot_from_state(count: int, latest_item: dict[str, object] | None) -> str:
    if not latest_item:
        return """      <section class="section">
        <div class="section-head">
          <p class="section-label">Diary</p>
          <h2>Archive slot</h2>
        </div>
        <div class="empty-state">
          <p><strong>Diary archive is being prepared.</strong></p>
          <p>The public archive will be populated in future batches from real post materials and linked visual surfaces.</p>
          <div class="section-links">
            <a href="./diary/">Open Diary</a>
            <a href="./diary/archive/">Open archive</a>
            <a href="./diary/tags/">Open tags</a>
          </div>
        </div>
      </section>"""

    image_html = ""
    primary_image = latest_item.get("primary_image")
    if isinstance(primary_image, str) and primary_image.startswith(SITE_URL):
        image_html = f"""
          <div class="entry-cover">
            <img src="./{html.escape(primary_image.removeprefix(SITE_URL))}" alt="{html.escape(str(latest_item.get('title', 'Latest diary entry')))}">
          </div>
"""
    tags = latest_item.get("tags") or []
    tags_text = ", ".join(str(tag) for tag in tags) if tags else "untagged"
    return f"""      <section class="section">
        <div class="section-head">
          <p class="section-label">Diary</p>
          <h2>Latest post</h2>
        </div>
        <article class="entry-card">
{image_html}          <div class="entry-meta">
            <span>{html.escape(str(latest_item.get('date', '')))}</span>
            <span>{html.escape(tags_text)}</span>
            <span>{count} entr{'y' if count == 1 else 'ies'} total</span>
          </div>
          <h3>{html.escape(str(latest_item.get('title', 'Latest diary entry')))}</h3>
          <p class="entry-summary">{html.escape(str(latest_item.get('summary', '')))}</p>
          <div class="section-links">
            <a href="./diary/{html.escape(str(latest_item.get('slug', '')))}/">Open latest post</a>
            <a href="./diary/archive/">Open archive</a>
            <a href="./diary/tags/">Open tags</a>
          </div>
        </article>
      </section>"""


def update_home_slot() -> None:
    home = HOME_PATH.read_text(encoding="utf-8")
    if HOME_SLOT_START not in home or HOME_SLOT_END not in home:
        raise ValueError("Home page is missing diary slot markers")

    latest_payload = json.loads(DIARY_LATEST_JSON.read_text(encoding="utf-8"))
    index_payload = json.loads(DIARY_INDEX_JSON.read_text(encoding="utf-8"))
    slot_html = render_home_slot_from_state(int(index_payload["count"]), latest_payload.get("item"))

    replacement = HOME_SLOT_START + "\n" + slot_html + "\n      " + HOME_SLOT_END
    pattern = re.compile(re.escape(HOME_SLOT_START) + r".*?" + re.escape(HOME_SLOT_END), re.DOTALL)
    updated = pattern.sub(replacement, home, count=1)
    HOME_PATH.write_text(updated, encoding="utf-8")


def main() -> None:
    entries = load_entries()
    tags = build_tag_index(entries)
    write_diary_outputs(entries, tags)
    write_machine_readable(entries, tags)
    update_home_slot()


if __name__ == "__main__":
    main()
