from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content" / "diary"
DIARY_DIR = ROOT / "diary"
HOME_PATH = ROOT / "index.html"
DIARY_INDEX_JSON = ROOT / "diary-index.json"
DIARY_LATEST_JSON = ROOT / "diary-latest.json"
HOME_SLOT_START = "<!-- diary-slot:start -->"
HOME_SLOT_END = "<!-- diary-slot:end -->"


@dataclass(frozen=True)
class Entry:
    source_path: Path
    title: str
    entry_date: date
    slug: str
    summary: str
    tags: list[str]
    primary_image: str
    image_alt: str
    linkedin_url: str
    extra_images: list[str]
    body_markdown: str

    @property
    def url(self) -> str:
        return f"https://ivankotov.eu/diary/{self.slug}/"

    @property
    def date_iso(self) -> str:
        return self.entry_date.isoformat()


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
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        raise ValueError(f"{path} must start with front matter")
    parts = raw.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError(f"{path} is missing a closing front matter delimiter")
    front_matter = parts[0].splitlines()[1:]
    body = parts[1].strip()

    metadata: dict[str, str] = {}
    for line in front_matter:
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"{path} has malformed front matter line: {line}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

    title = require_field(metadata, "title", path)
    date_value = require_field(metadata, "date", path)
    slug = require_field(metadata, "slug", path)
    summary = require_field(metadata, "summary", path)
    entry_date = date.fromisoformat(date_value)
    tags = split_csv(metadata.get("tags", ""))
    primary_image = metadata.get("primary_image", "")
    image_alt = metadata.get("image_alt", "")
    linkedin_url = metadata.get("linkedin_url", "")
    extra_images = split_csv(metadata.get("extra_images", ""))

    validate_slug(slug, path)
    validate_images([primary_image, *extra_images], path)

    if not body:
        raise ValueError(f"{path} must contain a body")

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
        body_markdown=body,
    )


def require_field(metadata: dict[str, str], key: str, path: Path) -> str:
    value = metadata.get(key, "").strip()
    if not value:
        raise ValueError(f"{path} is missing required field: {key}")
    return value


def split_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def validate_slug(slug: str, path: Path) -> None:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError(f"{path} has invalid slug: {slug}")


def validate_images(images: Iterable[str], path: Path) -> None:
    for image in images:
        if not image:
            continue
        candidate = ROOT / image
        if not candidate.exists():
            raise ValueError(f"{path} references a missing image: {image}")


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
        line = raw_line.rstrip()
        stripped = line.strip()

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
            code_lines.append(raw_line)
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


def diary_index_ld_json(has_entries: bool) -> str:
    graph: list[dict[str, object]] = [
        {
            "@type": "CollectionPage",
            "@id": "https://ivankotov.eu/diary/#page",
            "url": "https://ivankotov.eu/diary/",
            "name": "Diary — posts, notes, and visual archive | Ivan Kotov",
            "description": "Public archive surface for posts, notes, and linked visual materials related to the corpus.",
        },
        {
            "@type": "BreadcrumbList",
            "@id": "https://ivankotov.eu/diary/#breadcrumb",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": "https://ivankotov.eu/",
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "Diary",
                    "item": "https://ivankotov.eu/diary/",
                },
            ],
        },
    ]
    if has_entries:
        graph.append(
            {
                "@type": "ItemList",
                "@id": "https://ivankotov.eu/diary/#entries",
                "itemListOrder": "https://schema.org/ItemListOrderDescending",
            }
        )
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def render_diary_index(entries: list[Entry]) -> str:
    latest_cards = render_latest_entries(entries[:3])
    archive_cards = render_archive_entries(entries)
    tag_chips = render_tags(entries)

    empty_state = """
        <section class="section">
          <div class="section-head">
            <p class="section-label">Archive state</p>
            <h2>Prepared for batch import</h2>
          </div>
          <div class="empty-state">
            <p><strong>Diary archive is being prepared.</strong></p>
            <p>This archive is being prepared for batch import from existing post materials. No fake posts, dates, titles, or images are published in this foundation pass.</p>
          </div>
        </section>
    """ if not entries else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Diary — posts, notes, and visual archive | Ivan Kotov</title>
  <meta name="description" content="Public archive surface for posts, notes, and linked visual materials related to the corpus.">
  <link rel="canonical" href="https://ivankotov.eu/diary/">
  <meta property="og:title" content="Diary — posts, notes, and visual archive | Ivan Kotov">
  <meta property="og:description" content="Public archive surface for posts, notes, and linked visual materials related to the corpus.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://ivankotov.eu/diary/">
  <script type="application/ld+json">
  {diary_index_ld_json(bool(entries))}
  </script>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <div class="site-shell">
{nav_markup("../", "Diary")}

    <main>
      <section class="hero">
        <p class="eyebrow">Public archive surface</p>
        <h1>Diary</h1>
        <p class="lead page-lead">Public archive of posts, notes, and linked visual surfaces.</p>
        <p class="diary-note">This archive is being prepared for batch import from existing post materials.</p>
      </section>

{empty_state}

      <section class="section">
        <div class="section-head">
          <p class="section-label">Latest entries</p>
          <h2>Latest surface</h2>
        </div>
{latest_cards}
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Archive</p>
          <h2>Ordered entry list</h2>
        </div>
{archive_cards}
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Tags</p>
          <h2>Prepared tag surface</h2>
        </div>
{tag_chips}
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Linked surfaces</p>
          <h2>Archive context</h2>
        </div>
        <div class="surface-links">
          <a href="../">Home</a>
          <a href="../about/">About</a>
          <a href="../topics/">Topics</a>
          <a href="../library/">Library</a>
          <a href="../contact/">Contact</a>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <p>Primary domain: <span>ivankotov.eu</span></p>
    </footer>
  </div>
</body>
</html>
"""


def render_latest_entries(entries: list[Entry]) -> str:
    if not entries:
        return """        <div class="empty-state">
          <p><strong>No diary entries are published yet.</strong></p>
          <p>The latest-entries slot is ready for future batch imports, but this pass intentionally keeps the archive empty until real source materials are provided.</p>
        </div>
"""

    cards = []
    for entry in entries:
        image_html = ""
        if entry.primary_image:
            image_html = f"""
            <div class="entry-cover">
              <img src="../{html.escape(entry.primary_image)}" alt="{html.escape(entry.image_alt or entry.title)}">
            </div>
"""
        cards.append(
            f"""          <article class="entry-card">
{image_html}            <div class="entry-meta">
              <span>{entry.date_iso}</span>
              <span>{html.escape(', '.join(entry.tags)) if entry.tags else 'untagged'}</span>
            </div>
            <h3>{html.escape(entry.title)}</h3>
            <p class="entry-summary">{html.escape(entry.summary)}</p>
            <div class="section-links">
              <a href="./{html.escape(entry.slug)}/">Open entry</a>
            </div>
          </article>"""
        )
    return "        <div class=\"archive-grid\">\n" + "\n".join(cards) + "\n        </div>\n"


def render_archive_entries(entries: list[Entry]) -> str:
    if not entries:
        return """        <div class="empty-state">
          <p><strong>Archive list is empty.</strong></p>
          <p>Entries will appear here in reverse chronological order after real batches are imported.</p>
        </div>
"""

    cards = []
    for entry in entries:
        cards.append(
            f"""          <article class="entry-card">
            <div class="entry-meta">
              <span>{entry.date_iso}</span>
              <span>{html.escape(entry.slug)}</span>
            </div>
            <h3>{html.escape(entry.title)}</h3>
            <p class="entry-summary">{html.escape(entry.summary)}</p>
            <div class="section-links">
              <a href="./{html.escape(entry.slug)}/">Open entry</a>
            </div>
          </article>"""
        )
    return "        <div class=\"entry-list\">\n" + "\n".join(cards) + "\n        </div>\n"


def render_tags(entries: list[Entry]) -> str:
    tags = sorted({tag for entry in entries for tag in entry.tags})
    if not tags:
        return """        <div class="empty-state">
          <p><strong>Tag surface is waiting for real entries.</strong></p>
          <p>Tags will only be shown after imported entries bring confirmed labels.</p>
        </div>
"""
    chips = "".join(f'          <span class="archive-chip">{html.escape(tag)}</span>\n' for tag in tags)
    return "        <div class=\"archive-chip-list\">\n" + chips + "        </div>\n"


def post_ld_json(entry: Entry) -> str:
    graph = [
        {
            "@type": "BlogPosting",
            "@id": f"{entry.url}#post",
            "headline": entry.title,
            "url": entry.url,
            "datePublished": entry.date_iso,
            "dateModified": entry.date_iso,
            "author": {
                "@type": "Person",
                "name": "Ivan Kotov",
                "url": "https://ivankotov.eu/about/",
            },
            "publisher": {
                "@type": "Person",
                "name": "Ivan Kotov",
                "url": "https://ivankotov.eu/about/",
            },
            "description": entry.summary,
            "isPartOf": {
                "@type": "CollectionPage",
                "url": "https://ivankotov.eu/diary/",
                "name": "Diary — posts, notes, and visual archive | Ivan Kotov",
            },
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"{entry.url}#breadcrumb",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": "https://ivankotov.eu/",
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "Diary",
                    "item": "https://ivankotov.eu/diary/",
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": entry.title,
                    "item": entry.url,
                },
            ],
        },
    ]
    if entry.primary_image:
        graph[0]["image"] = f"https://ivankotov.eu/{entry.primary_image}"
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def render_post_page(entry: Entry) -> str:
    image_html = ""
    if entry.primary_image:
        image_html = f"""
      <div class="entry-cover">
        <img src="../../{html.escape(entry.primary_image)}" alt="{html.escape(entry.image_alt or entry.title)}">
      </div>
"""
    tag_html = ""
    if entry.tags:
        tags = "".join(f'          <span class="archive-chip">{html.escape(tag)}</span>\n' for tag in entry.tags)
        tag_html = "        <div class=\"archive-chip-list\">\n" + tags + "        </div>\n"
    linkedin_html = ""
    if entry.linkedin_url:
        linkedin_html = f'          <a href="{html.escape(entry.linkedin_url)}">Linked original</a>\n'
    body_html = markdown_to_html(entry.body_markdown)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(entry.title)} | Diary | Ivan Kotov</title>
  <meta name="description" content="{html.escape(entry.summary)}">
  <link rel="canonical" href="{entry.url}">
  <meta property="og:title" content="{html.escape(entry.title)} | Diary | Ivan Kotov">
  <meta property="og:description" content="{html.escape(entry.summary)}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{entry.url}">
  <script type="application/ld+json">
  {post_ld_json(entry)}
  </script>
  <link rel="stylesheet" href="../../styles.css">
</head>
<body>
  <div class="site-shell">
{nav_markup("../../", "Diary")}

    <main>
      <section class="hero">
        <p class="eyebrow">Diary entry</p>
        <h1>{html.escape(entry.title)}</h1>
        <div class="entry-meta">
          <span>{entry.date_iso}</span>
          <span>{html.escape(entry.slug)}</span>
        </div>
        <p class="lead page-lead">{html.escape(entry.summary)}</p>
{tag_html}      </section>

      <section class="section">
{image_html}        <div class="post-content">
          {body_html}
        </div>
        <div class="section-links">
          <a href="../">Back to Diary</a>
{linkedin_html}          <a href="../../about/">About</a>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <p>Primary domain: <span>ivankotov.eu</span></p>
    </footer>
  </div>
</body>
</html>
"""


def write_diary_outputs(entries: list[Entry]) -> None:
    DIARY_DIR.mkdir(parents=True, exist_ok=True)
    (DIARY_DIR / "index.html").write_text(render_diary_index(entries), encoding="utf-8")

    for entry in entries:
        target_dir = DIARY_DIR / entry.slug
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "index.html").write_text(render_post_page(entry), encoding="utf-8")

    diary_index = {
        "site": "https://ivankotov.eu/",
        "page": "https://ivankotov.eu/diary/",
        "items": [
            {
                "title": entry.title,
                "date": entry.date_iso,
                "slug": entry.slug,
                "summary": entry.summary,
                "tags": entry.tags,
                "page": entry.url,
                **({"primary_image": f"https://ivankotov.eu/{entry.primary_image}"} if entry.primary_image else {}),
                **({"linkedin_url": entry.linkedin_url} if entry.linkedin_url else {}),
            }
            for entry in entries
        ],
    }
    DIARY_INDEX_JSON.write_text(json.dumps(diary_index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    latest = entries[0] if entries else None
    latest_payload = {
        "site": "https://ivankotov.eu/",
        "page": "https://ivankotov.eu/diary/",
        "item": None if latest is None else {
            "title": latest.title,
            "date": latest.date_iso,
            "slug": latest.slug,
            "summary": latest.summary,
            "tags": latest.tags,
            "page": latest.url,
            **({"primary_image": f"https://ivankotov.eu/{latest.primary_image}"} if latest.primary_image else {}),
            **({"linkedin_url": latest.linkedin_url} if latest.linkedin_url else {}),
        },
    }
    DIARY_LATEST_JSON.write_text(json.dumps(latest_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def render_home_slot(entries: list[Entry]) -> str:
    if not entries:
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
          </div>
        </div>
      </section>"""

    latest = entries[0]
    image_html = ""
    if latest.primary_image:
        image_html = f"""
          <div class="entry-cover">
            <img src="./{html.escape(latest.primary_image)}" alt="{html.escape(latest.image_alt or latest.title)}">
          </div>
"""
    return f"""      <section class="section">
        <div class="section-head">
          <p class="section-label">Diary</p>
          <h2>Latest post</h2>
        </div>
        <article class="entry-card">
{image_html}          <div class="entry-meta">
            <span>{latest.date_iso}</span>
            <span>{html.escape(', '.join(latest.tags)) if latest.tags else 'untagged'}</span>
          </div>
          <h3>{html.escape(latest.title)}</h3>
          <p class="entry-summary">{html.escape(latest.summary)}</p>
          <div class="section-links">
            <a href="./diary/{html.escape(latest.slug)}/">Open latest post</a>
            <a href="./diary/">Open Diary</a>
          </div>
        </article>
      </section>"""


def update_home_slot(entries: list[Entry]) -> None:
    home = HOME_PATH.read_text(encoding="utf-8")
    if HOME_SLOT_START not in home or HOME_SLOT_END not in home:
        raise ValueError("Home page is missing diary slot markers")
    replacement = HOME_SLOT_START + "\n" + render_home_slot(entries) + "\n      " + HOME_SLOT_END
    pattern = re.compile(re.escape(HOME_SLOT_START) + r".*?" + re.escape(HOME_SLOT_END), re.DOTALL)
    updated = pattern.sub(replacement, home, count=1)
    HOME_PATH.write_text(updated, encoding="utf-8")


def main() -> None:
    entries = load_entries()
    write_diary_outputs(entries)
    update_home_slot(entries)


if __name__ == "__main__":
    main()
