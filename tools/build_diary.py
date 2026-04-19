from __future__ import annotations

import html
import json
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass, replace
from datetime import date, datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content" / "diary"
CURATION_PATH = CONTENT_DIR / "_curation.json"
DIARY_DIR = ROOT / "diary"
HOME_PATH = ROOT / "index.html"
DIARY_INDEX_JSON = ROOT / "diary-index.json"
DIARY_TAGS_JSON = ROOT / "diary-tags.json"
DIARY_LATEST_JSON = ROOT / "diary-latest.json"
DIARY_FEED_XML = ROOT / "diary-feed.xml"
DIARY_START_HERE_JSON = ROOT / "diary-start-here.json"
DIARY_THEMES_JSON = ROOT / "diary-themes.json"
DIARY_CORNERSTONES_JSON = ROOT / "diary-cornerstones.json"
DIARY_TAG_MAP_JSON = ROOT / "diary-tag-map.json"
HOME_SLOT_START = "<!-- diary-slot:start -->"
HOME_SLOT_END = "<!-- diary-slot:end -->"

SITE_TITLE = "Ivan Kotov — Advanced Global Intelligence, c = a + b, L4, SER"
DIARY_TITLE = "Diary — posts, notes, and visual archive | Ivan Kotov"
DIARY_DESCRIPTION = "Public archive surface for posts, notes, and linked visual materials related to the corpus."
DIARY_ARCHIVE_TITLE = "Diary archive | Ivan Kotov"
DIARY_ARCHIVE_DESCRIPTION = "Chronological archive surface for public posts and notes."
DIARY_TAGS_TITLE = "Diary tags | Ivan Kotov"
DIARY_TAGS_DESCRIPTION = "Tag-based entry into the diary archive."
DIARY_START_HERE_TITLE = "Diary start here | Ivan Kotov"
DIARY_START_HERE_DESCRIPTION = "Curated entry path into the diary archive for first-time readers."
DIARY_THEMES_TITLE = "Diary themes | Ivan Kotov"
DIARY_THEMES_DESCRIPTION = "Topic-based reading paths through the diary archive."
SITE_URL = "https://ivankotov.eu/"
DIARY_URL = "https://ivankotov.eu/diary/"
DIARY_ARCHIVE_URL = "https://ivankotov.eu/diary/archive/"
DIARY_TAGS_URL = "https://ivankotov.eu/diary/tags/"
DIARY_START_HERE_URL = "https://ivankotov.eu/diary/start-here/"
DIARY_THEMES_URL = "https://ivankotov.eu/diary/themes/"

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
    raw_tags: list[TagRef]
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
    aliases: list[str]

    @property
    def url(self) -> str:
        return f"{DIARY_TAGS_URL}{self.slug}/"

    @property
    def count(self) -> int:
        return len(self.entries)


@dataclass(frozen=True)
class TagAlias:
    name: str
    slug: str
    canonical_name: str
    canonical_slug: str
    entry_count: int

    @property
    def url(self) -> str:
        return f"{DIARY_TAGS_URL}{self.slug}/"

    @property
    def canonical_url(self) -> str:
        return f"{DIARY_TAGS_URL}{self.canonical_slug}/"


@dataclass(frozen=True)
class ThemeConfig:
    slug: str
    title: str
    description: str
    entry_slugs: list[str]

    @property
    def url(self) -> str:
        return f"{DIARY_THEMES_URL}{self.slug}/"


@dataclass(frozen=True)
class ThemeInfo:
    slug: str
    title: str
    description: str
    entries: list[Entry]

    @property
    def url(self) -> str:
        return f"{DIARY_THEMES_URL}{self.slug}/"

    @property
    def count(self) -> int:
        return len(self.entries)


@dataclass(frozen=True)
class CanonicalTagConfig:
    name: str
    slug: str
    aliases: list[str]


@dataclass(frozen=True)
class CurationConfig:
    start_here_slugs: list[str]
    cornerstone_slugs: list[str]
    themes: list[ThemeConfig]
    tag_aliases: list[CanonicalTagConfig]


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
    raw_tags = parse_tags(metadata["tags"], path)

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
        raw_tags=raw_tags,
        tags=raw_tags,
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


def unique_strings(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    items: list[str] = []
    for value in values:
        cleaned = value.strip()
        if not cleaned or cleaned in seen:
            continue
        seen.add(cleaned)
        items.append(cleaned)
    return items


def validate_entry_slug_list(name: str, slugs: list[str], entry_lookup: dict[str, Entry]) -> list[str]:
    ordered = unique_strings(slugs)
    if not ordered:
        raise ValueError(f"Curation field {name} must not be empty")
    missing = [slug for slug in ordered if slug not in entry_lookup]
    if missing:
        raise ValueError(f"Curation field {name} references missing entry slugs: {', '.join(missing)}")
    return ordered


def load_curation(entries: list[Entry]) -> CurationConfig:
    if not CURATION_PATH.exists():
        raise ValueError("Diary curation config is missing")

    raw = json.loads(CURATION_PATH.read_text(encoding="utf-8"))
    entry_lookup = {entry.slug: entry for entry in entries}
    raw_tag_lookup = {tag.name: tag.slug for entry in entries for tag in entry.raw_tags}

    start_here_slugs = validate_entry_slug_list("start_here", raw.get("start_here", []), entry_lookup)
    cornerstone_slugs = validate_entry_slug_list("cornerstones", raw.get("cornerstones", []), entry_lookup)

    themes: list[ThemeConfig] = []
    theme_slugs_seen: set[str] = set()
    for item in raw.get("themes", []):
        slug = str(item.get("slug", "")).strip()
        title = str(item.get("title", "")).strip()
        description = str(item.get("description", "")).strip()
        if not slug or not title or not description:
            raise ValueError("Each theme in _curation.json must define slug, title, and description")
        validate_slug(slug, CURATION_PATH)
        if slug in theme_slugs_seen:
            raise ValueError(f"Duplicate theme slug in _curation.json: {slug}")
        theme_slugs_seen.add(slug)
        theme_entries = validate_entry_slug_list(f"theme:{slug}", item.get("entries", []), entry_lookup)
        themes.append(ThemeConfig(slug=slug, title=title, description=description, entry_slugs=theme_entries))

    alias_owner: dict[str, str] = {}
    tag_aliases: list[CanonicalTagConfig] = []
    for item in raw.get("tag_aliases", []):
        name = str(item.get("tag", "")).strip()
        if not name:
            raise ValueError("Each tag alias entry must define tag")
        slug = normalize_tag_slug(name)
        if not slug:
            raise ValueError(f"Canonical tag cannot be normalized: {name}")
        aliases = unique_strings(item.get("aliases", []))
        if not aliases:
            raise ValueError(f"Canonical tag {name} must define aliases")
        for alias in aliases:
            alias_slug = normalize_tag_slug(alias)
            if not alias_slug:
                raise ValueError(f"Alias cannot be normalized: {alias}")
            if alias not in raw_tag_lookup:
                raise ValueError(f"Alias {alias} from _curation.json does not exist in the diary corpus")
            previous = alias_owner.get(alias_slug)
            if previous and previous != slug:
                raise ValueError(f"Alias slug {alias_slug} is assigned to multiple canonical tags")
            alias_owner[alias_slug] = slug
        tag_aliases.append(CanonicalTagConfig(name=name, slug=slug, aliases=aliases))

    if len(themes) < 4:
        raise ValueError("V43 curation requires at least 4 themes")

    return CurationConfig(
        start_here_slugs=start_here_slugs,
        cornerstone_slugs=cornerstone_slugs,
        themes=themes,
        tag_aliases=tag_aliases,
    )


def build_tag_alias_map(curation: CurationConfig) -> dict[str, TagRef]:
    alias_map: dict[str, TagRef] = {}
    for item in curation.tag_aliases:
        canonical = TagRef(name=item.name, slug=item.slug)
        for alias in item.aliases:
            alias_map[normalize_tag_slug(alias)] = canonical
    return alias_map


def normalize_entry_tags(entries: list[Entry], alias_map: dict[str, TagRef]) -> list[Entry]:
    normalized_entries: list[Entry] = []
    for entry in entries:
        tags: list[TagRef] = []
        seen: set[str] = set()
        for raw_tag in entry.raw_tags:
            canonical = alias_map.get(raw_tag.slug, raw_tag)
            if canonical.slug in seen:
                continue
            seen.add(canonical.slug)
            tags.append(canonical)
        normalized_entries.append(replace(entry, tags=tags))
    return normalized_entries


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


def build_tag_index(entries: list[Entry], alias_map: dict[str, TagRef]) -> tuple[list[TagInfo], list[TagAlias]]:
    buckets: dict[str, list[Entry]] = {}
    display_names: dict[str, str] = {}
    aliases: dict[str, set[str]] = defaultdict(set)
    alias_slugs: dict[str, dict[str, str]] = defaultdict(dict)

    for entry in entries:
        for tag in entry.tags:
            buckets.setdefault(tag.slug, []).append(entry)
            display_names.setdefault(tag.slug, tag.name)
        for raw_tag in entry.raw_tags:
            canonical = alias_map.get(raw_tag.slug, raw_tag)
            aliases[canonical.slug].add(raw_tag.name)
            alias_slugs[canonical.slug][raw_tag.slug] = raw_tag.name

    tag_infos = [
        TagInfo(
            name=display_names[slug],
            slug=slug,
            entries=sorted(items, key=lambda item: (item.entry_date, item.slug), reverse=True),
            aliases=sorted(aliases.get(slug, {display_names[slug]}), key=str.lower),
        )
        for slug, items in buckets.items()
    ]
    tag_infos.sort(key=lambda tag: (-tag.count, tag.name.lower(), tag.slug))

    canonical_lookup = {tag.slug: tag for tag in tag_infos}
    tag_aliases: list[TagAlias] = []
    for canonical_slug, raw_variants in alias_slugs.items():
        canonical = canonical_lookup[canonical_slug]
        for raw_slug, raw_name in raw_variants.items():
            if raw_slug == canonical_slug:
                continue
            tag_aliases.append(
                TagAlias(
                    name=raw_name,
                    slug=raw_slug,
                    canonical_name=canonical.name,
                    canonical_slug=canonical.slug,
                    entry_count=canonical.count,
                )
            )
    tag_aliases.sort(key=lambda item: (item.name.lower(), item.slug))
    return tag_infos, tag_aliases


def build_theme_index(entries: list[Entry], curation: CurationConfig) -> tuple[list[ThemeInfo], dict[str, list[ThemeInfo]]]:
    entry_lookup = {entry.slug: entry for entry in entries}
    themes: list[ThemeInfo] = []
    membership: dict[str, list[ThemeInfo]] = defaultdict(list)

    for theme in curation.themes:
        theme_entries = [entry_lookup[slug] for slug in theme.entry_slugs]
        info = ThemeInfo(slug=theme.slug, title=theme.title, description=theme.description, entries=theme_entries)
        themes.append(info)
        for entry in theme_entries:
            membership[entry.slug].append(info)

    return themes, membership


def score_related_entry(entry: Entry, candidate: Entry, entry_themes: dict[str, list[ThemeInfo]]) -> tuple[int, int, int, int]:
    entry_tags = {tag.slug for tag in entry.tags}
    candidate_tags = {tag.slug for tag in candidate.tags}
    shared_tags = len(entry_tags & candidate_tags)
    entry_theme_slugs = {theme.slug for theme in entry_themes.get(entry.slug, [])}
    candidate_theme_slugs = {theme.slug for theme in entry_themes.get(candidate.slug, [])}
    shared_themes = len(entry_theme_slugs & candidate_theme_slugs)
    days_apart = abs((entry.entry_date - candidate.entry_date).days)
    time_score = 4 if days_apart == 0 else 3 if days_apart <= 3 else 2 if days_apart <= 14 else 1 if days_apart <= 45 else 0
    score = shared_tags * 12 + shared_themes * 8 + time_score
    return score, shared_tags, shared_themes, time_score


def build_related_posts(entries: list[Entry], entry_themes: dict[str, list[ThemeInfo]]) -> dict[str, list[Entry]]:
    related: dict[str, list[Entry]] = {}

    for entry in entries:
        ranked: list[tuple[int, int, int, int, Entry]] = []
        for candidate in entries:
            if candidate.slug == entry.slug or candidate.title == entry.title:
                continue
            score, shared_tags, shared_themes, time_score = score_related_entry(entry, candidate, entry_themes)
            if score <= 0:
                continue
            ranked.append((score, shared_tags, shared_themes, time_score, candidate))

        ranked.sort(key=lambda item: (item[0], item[1], item[2], item[3], item[4].entry_date, item[4].slug), reverse=True)
        selected: list[Entry] = []
        seen_signatures: set[tuple[str, ...]] = set()
        for _, _, _, _, candidate in ranked:
            signature = tuple(sorted(tag.slug for tag in candidate.tags))
            if signature and signature in seen_signatures:
                continue
            selected.append(candidate)
            if signature:
                seen_signatures.add(signature)
            if len(selected) == 4:
                break
        related[entry.slug] = selected[:4]

    return related


def entry_payload(entry: Entry) -> dict[str, object]:
    payload = {
        "title": entry.title,
        "date": entry.date_iso,
        "slug": entry.slug,
        "summary": entry.summary,
        "tags": [tag.name for tag in entry.tags],
        "raw_tags": [tag.name for tag in entry.raw_tags],
        "page": entry.url,
    }
    if entry.primary_image:
        payload["primary_image"] = f"{SITE_URL}{entry.primary_image}"
    if entry.image_alt:
        payload["image_alt"] = entry.image_alt
    if entry.linkedin_url:
        payload["linkedin_url"] = entry.linkedin_url
    return payload


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
            </div>
            <h3>{html.escape(entry.title)}</h3>
            <p class="entry-summary">{html.escape(entry.summary)}</p>
{tag_links}            <div class="section-links">
              <a href="{html.escape(entry_href)}">Open entry</a>
            </div>
          </article>"""


def render_entry_collection(
    entries: list[Entry],
    *,
    asset_prefix: str,
    entry_prefix: str,
    tag_prefix: str,
    include_image: bool,
    limit: int | None = None,
    wrapper_class: str = "entry-list",
) -> str:
    selected = entries if limit is None else entries[:limit]
    cards = [
        render_entry_card(
            entry,
            asset_prefix=asset_prefix,
            entry_href=f"{entry_prefix}{entry.slug}/",
            tag_prefix=tag_prefix,
            include_image=include_image,
        )
        for entry in selected
    ]
    return f"        <div class=\"{wrapper_class}\">\n" + "\n".join(cards) + "\n        </div>\n"


def render_latest_entries(entries: list[Entry]) -> str:
    if not entries:
        return render_empty_state(
            "No diary entries are published yet.",
            "The latest-entries slot is ready for future batch imports, but this pass intentionally keeps the archive empty until real source materials are provided.",
        )
    return render_entry_collection(
        entries,
        asset_prefix="../",
        entry_prefix="./",
        tag_prefix="./tags/",
        include_image=False,
        limit=5,
        wrapper_class="entry-list",
    )


def render_cornerstones(entries: list[Entry]) -> str:
    if not entries:
        return render_empty_state("No cornerstone entries were configured.", "Cornerstones appear only when the curation config selects real diary entries.")
    return render_entry_collection(
        entries,
        asset_prefix="../",
        entry_prefix="./",
        tag_prefix="./tags/",
        include_image=False,
        limit=None,
        wrapper_class="entry-list",
    )


def render_start_here_cards(entries: list[Entry], *, asset_prefix: str, entry_prefix: str, tag_prefix: str) -> str:
    if not entries:
        return render_empty_state("No start-here entries were configured.", "The start-here surface appears only after curated entry slugs are selected.")
    return render_entry_collection(
        entries,
        asset_prefix=asset_prefix,
        entry_prefix=entry_prefix,
        tag_prefix=tag_prefix,
        include_image=True,
        limit=None,
        wrapper_class="archive-grid",
    )


def render_theme_cards(themes: list[ThemeInfo], *, link_prefix: str) -> str:
    if not themes:
        return render_empty_state("No themes are configured.", "Theme cards appear only after the curation layer defines real diary groupings.")
    cards = []
    for theme in themes:
        cards.append(
            f"""          <article class="surface-group">
            <h3>{html.escape(theme.title)}</h3>
            <p>{html.escape(theme.description)}</p>
            <p>{theme.count} curated entr{'y' if theme.count == 1 else 'ies'}.</p>
            <div class="surface-links">
              <a href="{html.escape(link_prefix + theme.slug + "/")}">Open theme</a>
            </div>
          </article>"""
        )
    return "        <div class=\"surface-grid\">\n" + "\n".join(cards) + "\n        </div>\n"


def render_tag_chips(tags: list[TagInfo], *, link_prefix: str, limit: int | None = None) -> str:
    if not tags:
        return ""
    selected = tags if limit is None else tags[:limit]
    chips = [
        f'<a class="archive-chip" href="{html.escape(link_prefix + tag.slug + "/")}">{html.escape(tag.name)} ({tag.count})</a>'
        for tag in selected
    ]
    return "        <div class=\"archive-chip-list\">\n          " + "\n          ".join(chips) + "\n        </div>\n"


def render_tag_preview(tags: list[TagInfo]) -> str:
    if not tags:
        return render_empty_state(
            "Tag surface is waiting for real entries.",
            "Tags will only be shown after imported entries bring confirmed labels.",
        )
    return render_tag_chips(tags[:12], link_prefix="./tags/")


def group_entries_by_month(entries: list[Entry]) -> list[tuple[str, list[Entry]]]:
    groups: dict[tuple[int, int], list[Entry]] = {}
    for entry in entries:
        groups.setdefault((entry.entry_date.year, entry.entry_date.month), []).append(entry)
    ordered = sorted(groups.items(), reverse=True)
    labeled: list[tuple[str, list[Entry]]] = []
    for (year, month), items in ordered:
        label = datetime(year, month, 1).strftime("%B %Y")
        labeled.append((label, items))
    return labeled


def render_archive_groups(entries: list[Entry], *, asset_prefix: str, entry_prefix: str, tag_prefix: str) -> str:
    if not entries:
        return render_empty_state(
            "Archive chronology is empty.",
            "Chronological archive groups will appear here after the first real batch import.",
        )

    groups = []
    for label, month_entries in group_entries_by_month(entries):
        cards = [
            render_entry_card(
                entry,
                asset_prefix=asset_prefix,
                entry_href=f"{entry_prefix}{entry.slug}/",
                tag_prefix=tag_prefix,
                include_image=False,
            )
            for entry in month_entries
        ]
        groups.append(
            f"""        <section class="section">
          <div class="section-head">
            <p class="section-label">Archive month</p>
            <h2>{html.escape(label)}</h2>
            <p class="diary-note">{len(month_entries)} entr{'y' if len(month_entries) == 1 else 'ies'} in this group.</p>
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
    featured = tags[:18]
    cards = []
    for tag in featured:
        alias_note = ""
        if len(tag.aliases) > 1:
            alias_note = f"<p>Normalized from {len(tag.aliases)} raw source labels.</p>"
        cards.append(
            f"""          <article class="surface-group">
            <h3>{html.escape(tag.name)}</h3>
            <p>{tag.count} linked entr{'y' if tag.count == 1 else 'ies'} in the archive.</p>
            {alias_note}
            <div class="surface-links">
              <a href="{html.escape(link_prefix + tag.slug + "/")}">Open tag page</a>
            </div>
          </article>"""
        )
    chip_list = render_tag_chips(tags, link_prefix=link_prefix, limit=None)
    return (
        "        <div class=\"surface-grid\">\n" + "\n".join(cards) + "\n        </div>\n"
        + "\n        <div class=\"section-head\">\n          <p class=\"section-label\">All canonical tags</p>\n          <h3>Full normalized tag list</h3>\n        </div>\n"
        + chip_list
    )


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


def render_related_posts(entry: Entry, related_entries: list[Entry]) -> str:
    if not related_entries:
        return ""
    cards = [
        render_entry_card(
            item,
            asset_prefix="../../",
            entry_href=f"../{item.slug}/",
            tag_prefix="../tags/",
            include_image=False,
        )
        for item in related_entries[:4]
    ]
    return f"""
      <section class="section">
        <div class="section-head">
          <p class="section-label">Related posts</p>
          <h2>Continue from here</h2>
          <p class="diary-note">Related by normalized tags, curated themes, and nearby chronology.</p>
        </div>
        <div class="entry-list">
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


def collection_itemlist_ld_json(
    page_url: str,
    page_title: str,
    description: str,
    breadcrumb: list[tuple[str, str]],
    items: list[tuple[str, str]],
) -> str:
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
        {
            "@type": "ItemList",
            "@id": f"{page_url}#items",
            "itemListElement": [
                {"@type": "ListItem", "position": index, "name": name, "url": item}
                for index, (name, item) in enumerate(items, start=1)
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


def render_diary_index(
    entries: list[Entry],
    tags: list[TagInfo],
    start_here_entries: list[Entry],
    cornerstone_entries: list[Entry],
    themes: list[ThemeInfo],
) -> str:
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
        <p class="eyebrow">Curated archive surface</p>
        <h1>Diary</h1>
        <p class="lead page-lead">Public archive of posts, notes, and linked visual surfaces, now with curated entry paths for first-time readers.</p>
        <p class="diary-note">Use Start here and Themes before dropping into the full archive if you want the shortest route into the corpus.</p>
      </section>

{empty_state}
      <section class="section">
        <div class="section-head">
          <p class="section-label">Curated entry path</p>
          <h2>Start here</h2>
          <p class="diary-note">These are not “best posts”, but a practical path into the archive.</p>
        </div>
{render_start_here_cards(start_here_entries, asset_prefix='../', entry_prefix='./', tag_prefix='./tags/')}
        <div class="section-links">
          <a href="./start-here/">Open Start here</a>
          <a href="./themes/">Open themes</a>
          <a href="./tags/">Open tags</a>
        </div>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Themes</p>
          <h2>Topic-based reading paths</h2>
        </div>
{render_theme_cards(themes, link_prefix='./themes/')}
        <div class="section-links">
          <a href="./themes/">Open all themes</a>
        </div>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Latest entries</p>
          <h2>Recent archive movement</h2>
        </div>
{render_latest_entries(entries)}
        <div class="section-links">
          <a href="./archive/">Open archive</a>
          <a href="./start-here/">Open Start here</a>
        </div>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Cornerstones</p>
          <h2>Posts that carry the structure</h2>
          <p class="diary-note">A wider set of anchor posts across releases, architecture, infrastructure, continuity, and the book layer.</p>
        </div>
{render_cornerstones(cornerstone_entries)}
        <div class="section-links">
          <a href="./archive/">Browse full archive</a>
          <a href="./themes/">Browse by theme</a>
        </div>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Tags</p>
          <h2>Normalized tag surface</h2>
          <p class="diary-note">Canonical display tags reduce alias clutter while preserving the historical raw labels in the source corpus.</p>
        </div>
{render_tag_preview(tags)}
        <div class="section-links">
          <a href="./tags/">Open tag index</a>
          <a href="./archive/">Open archive</a>
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
        <p class="lead page-lead">Chronological archive surface for public posts and notes, grouped by month for faster scanning on mobile.</p>
        <p class="diary-note">Use this page for direct chronological browsing when the curated start-here and theme paths are not enough.</p>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Chronology</p>
          <h2>Reverse-chronological archive</h2>
        </div>
        <div class="section-links">
          <a href="../">Back to Diary</a>
          <a href="../start-here/">Open Start here</a>
          <a href="../themes/">Open themes</a>
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
        <p class="lead page-lead">Canonical tag-based entry into the diary archive.</p>
        <p class="diary-note">Public display uses a normalized taxonomy layer on top of the historical raw source tags.</p>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Tags</p>
          <h2>Normalized tag index</h2>
        </div>
{render_tag_grid(tags, link_prefix='./')}
        <div class="section-links">
          <a href="../">Back to Diary</a>
          <a href="../themes/">Open themes</a>
          <a href="../start-here/">Open Start here</a>
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
    alias_note = ""
    if len(tag.aliases) > 1:
        alias_note = f'<p class="diary-note">This canonical tag currently absorbs {len(tag.aliases)} raw source labels.</p>'
    body_html = f"""      <section class="hero">
        <p class="eyebrow">Diary tag</p>
        <h1>{html.escape(tag.name)}</h1>
        <p class="lead page-lead">Canonical diary tag page generated from normalized source tags.</p>
        <p class="diary-note">{tag.count} linked entr{'y' if tag.count == 1 else 'ies'} currently in the archive.</p>
        {alias_note}
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
          <a href="../../themes/">Open themes</a>
          <a href="../../archive/">Open archive</a>
          <a href="../../">Back to Diary</a>
        </div>
      </section>
"""

    return render_document(
        title=f"Diary tag — {tag.name} | Ivan Kotov",
        description=f"Curated diary entries grouped under the canonical tag {tag.name}.",
        canonical=tag.url,
        og_type="website",
        og_image=None,
        stylesheet_href="../../../styles.css",
        nav_prefix="../../../",
        nav_current="Diary",
        ld_json=collection_ld_json(
            tag.url,
            f"Diary tag — {tag.name} | Ivan Kotov",
            f"Curated diary entries grouped under the canonical tag {tag.name}.",
            [("Home", SITE_URL), ("Diary", DIARY_URL), ("Tags", DIARY_TAGS_URL), (tag.name, tag.url)],
        ),
        body_html=body_html,
    )


def render_tag_alias_page(tag_alias: TagAlias) -> str:
    body_html = f"""      <section class="hero">
        <p class="eyebrow">Diary tag alias</p>
        <h1>{html.escape(tag_alias.name)}</h1>
        <p class="lead page-lead">This historical raw tag now resolves under the normalized canonical tag <strong>{html.escape(tag_alias.canonical_name)}</strong>.</p>
        <p class="diary-note">{tag_alias.entry_count} linked entr{'y' if tag_alias.entry_count == 1 else 'ies'} are available under the canonical tag page.</p>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Canonical mapping</p>
          <h2>Use the normalized tag page</h2>
        </div>
        <div class="section-links">
          <a href="../{html.escape(tag_alias.canonical_slug)}/">Open {html.escape(tag_alias.canonical_name)}</a>
          <a href="../">Back to tags</a>
          <a href="../../">Back to Diary</a>
        </div>
      </section>
"""

    return render_document(
        title=f"Diary tag alias — {tag_alias.name} | Ivan Kotov",
        description=f"Historical diary tag alias for {tag_alias.name}, normalized under {tag_alias.canonical_name}.",
        canonical=tag_alias.canonical_url,
        og_type="website",
        og_image=None,
        stylesheet_href="../../../styles.css",
        nav_prefix="../../../",
        nav_current="Diary",
        ld_json=collection_ld_json(
            tag_alias.canonical_url,
            f"Diary tag alias — {tag_alias.name} | Ivan Kotov",
            f"Historical diary tag alias for {tag_alias.name}, normalized under {tag_alias.canonical_name}.",
            [("Home", SITE_URL), ("Diary", DIARY_URL), ("Tags", DIARY_TAGS_URL), (tag_alias.canonical_name, tag_alias.canonical_url)],
        ),
        body_html=body_html,
    )


def render_start_here_page(entries: list[Entry]) -> str:
    body_html = f"""      <section class="hero">
        <p class="eyebrow">Curated diary entry</p>
        <h1>Start here in the Diary</h1>
        <p class="lead page-lead">A short curated entry into the diary archive.</p>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Starting posts</p>
          <h2>First path into the archive</h2>
        </div>
{render_start_here_cards(entries, asset_prefix='../../', entry_prefix='../', tag_prefix='../tags/')}
        <p class="diary-note">These are not “best posts”, but a practical entry path into the archive.</p>
        <div class="section-links">
          <a href="../archive/">Open archive</a>
          <a href="../themes/">Open themes</a>
          <a href="../tags/">Open tags</a>
        </div>
      </section>
"""

    return render_document(
        title=DIARY_START_HERE_TITLE,
        description=DIARY_START_HERE_DESCRIPTION,
        canonical=DIARY_START_HERE_URL,
        og_type="website",
        og_image=None,
        stylesheet_href="../../styles.css",
        nav_prefix="../../",
        nav_current="Diary",
        ld_json=collection_itemlist_ld_json(
            DIARY_START_HERE_URL,
            DIARY_START_HERE_TITLE,
            DIARY_START_HERE_DESCRIPTION,
            [("Home", SITE_URL), ("Diary", DIARY_URL), ("Start here", DIARY_START_HERE_URL)],
            [(entry.title, entry.url) for entry in entries],
        ),
        body_html=body_html,
    )


def render_themes_index(themes: list[ThemeInfo]) -> str:
    body_html = f"""      <section class="hero">
        <p class="eyebrow">Topic-based entry</p>
        <h1>Diary themes</h1>
        <p class="lead page-lead">Topic-based reading paths through the diary archive.</p>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Themes</p>
          <h2>Curated reading paths</h2>
        </div>
{render_theme_cards(themes, link_prefix='./')}
        <div class="section-links">
          <a href="../start-here/">Open Start here</a>
          <a href="../archive/">Open archive</a>
          <a href="../tags/">Open tags</a>
        </div>
      </section>
"""

    return render_document(
        title=DIARY_THEMES_TITLE,
        description=DIARY_THEMES_DESCRIPTION,
        canonical=DIARY_THEMES_URL,
        og_type="website",
        og_image=None,
        stylesheet_href="../../styles.css",
        nav_prefix="../../",
        nav_current="Diary",
        ld_json=collection_itemlist_ld_json(
            DIARY_THEMES_URL,
            DIARY_THEMES_TITLE,
            DIARY_THEMES_DESCRIPTION,
            [("Home", SITE_URL), ("Diary", DIARY_URL), ("Themes", DIARY_THEMES_URL)],
            [(theme.title, theme.url) for theme in themes],
        ),
        body_html=body_html,
    )


def render_theme_page(theme: ThemeInfo) -> str:
    body_html = f"""      <section class="hero">
        <p class="eyebrow">Diary theme</p>
        <h1>{html.escape(theme.title)}</h1>
        <p class="lead page-lead">{html.escape(theme.description)}</p>
        <p class="diary-note">{theme.count} curated entr{'y' if theme.count == 1 else 'ies'} in this reading path.</p>
      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Theme entries</p>
          <h2>{html.escape(theme.title)}</h2>
        </div>
{render_entry_collection(theme.entries, asset_prefix='../../../', entry_prefix='../../', tag_prefix='../../tags/', include_image=False, limit=None, wrapper_class='entry-list')}
        <div class="section-links">
          <a href="../">Back to themes</a>
          <a href="../../start-here/">Open Start here</a>
          <a href="../../archive/">Open archive</a>
        </div>
      </section>
"""

    page_title = f"Diary theme — {theme.title} | Ivan Kotov"
    page_description = f"Curated diary entries grouped under {theme.title}."
    return render_document(
        title=page_title,
        description=page_description,
        canonical=theme.url,
        og_type="website",
        og_image=None,
        stylesheet_href="../../../styles.css",
        nav_prefix="../../../",
        nav_current="Diary",
        ld_json=collection_itemlist_ld_json(
            theme.url,
            page_title,
            page_description,
            [("Home", SITE_URL), ("Diary", DIARY_URL), ("Themes", DIARY_THEMES_URL), (theme.title, theme.url)],
            [(entry.title, entry.url) for entry in theme.entries],
        ),
        body_html=body_html,
    )


def render_post_page(entry: Entry, related_entries: list[Entry]) -> str:
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
{render_gallery(entry)}
{render_related_posts(entry, related_entries)}"""

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
    items = [entry_payload(entry) for entry in entries]
    latest_payload = entry_payload(latest) if latest is not None else None
    return {
        "site": SITE_URL,
        "page": DIARY_URL,
        "count": len(entries),
        "latest": latest_payload,
        "items": items,
    }


def make_start_here_payload(entries: list[Entry]) -> dict[str, object]:
    return {
        "site": SITE_URL,
        "page": DIARY_START_HERE_URL,
        "items": [entry_payload(entry) for entry in entries],
    }


def make_cornerstones_payload(entries: list[Entry]) -> dict[str, object]:
    return {
        "site": SITE_URL,
        "page": DIARY_URL,
        "items": [entry_payload(entry) for entry in entries],
    }


def make_themes_payload(themes: list[ThemeInfo]) -> dict[str, object]:
    return {
        "site": SITE_URL,
        "page": DIARY_THEMES_URL,
        "themes": [
            {
                "title": theme.title,
                "slug": theme.slug,
                "description": theme.description,
                "count": theme.count,
                "page": theme.url,
                "items": [entry_payload(entry) for entry in theme.entries],
            }
            for theme in themes
        ],
    }


def make_tag_map_payload(tags: list[TagInfo]) -> dict[str, object]:
    return {
        "site": SITE_URL,
        "page": DIARY_TAGS_URL,
        "canonical_tags": [
            {"tag": tag.name, "slug": tag.slug, "count": tag.count, "page": tag.url, "aliases": tag.aliases}
            for tag in tags
        ],
    }


def make_tags_payload(tags: list[TagInfo]) -> dict[str, object]:
    return {
        "site": SITE_URL,
        "page": DIARY_TAGS_URL,
        "tags": [
            {"name": tag.name, "slug": tag.slug, "count": tag.count, "page": tag.url, "aliases": tag.aliases}
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


def write_diary_outputs(
    entries: list[Entry],
    tags: list[TagInfo],
    tag_aliases: list[TagAlias],
    start_here_entries: list[Entry],
    cornerstone_entries: list[Entry],
    themes: list[ThemeInfo],
    related_posts: dict[str, list[Entry]],
) -> None:
    wipe_generated_diary_tree()

    (DIARY_DIR / "index.html").write_text(
        render_diary_index(entries, tags, start_here_entries, cornerstone_entries, themes), encoding="utf-8"
    )

    archive_dir = DIARY_DIR / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    (archive_dir / "index.html").write_text(render_archive_page(entries), encoding="utf-8")

    start_here_dir = DIARY_DIR / "start-here"
    start_here_dir.mkdir(parents=True, exist_ok=True)
    (start_here_dir / "index.html").write_text(render_start_here_page(start_here_entries), encoding="utf-8")

    themes_dir = DIARY_DIR / "themes"
    themes_dir.mkdir(parents=True, exist_ok=True)
    (themes_dir / "index.html").write_text(render_themes_index(themes), encoding="utf-8")
    for theme in themes:
        theme_dir = themes_dir / theme.slug
        theme_dir.mkdir(parents=True, exist_ok=True)
        (theme_dir / "index.html").write_text(render_theme_page(theme), encoding="utf-8")

    tags_dir = DIARY_DIR / "tags"
    tags_dir.mkdir(parents=True, exist_ok=True)
    (tags_dir / "index.html").write_text(render_tags_index(tags), encoding="utf-8")

    for tag in tags:
        tag_dir = tags_dir / tag.slug
        tag_dir.mkdir(parents=True, exist_ok=True)
        (tag_dir / "index.html").write_text(render_tag_page(tag), encoding="utf-8")

    for tag_alias in tag_aliases:
        tag_dir = tags_dir / tag_alias.slug
        tag_dir.mkdir(parents=True, exist_ok=True)
        (tag_dir / "index.html").write_text(render_tag_alias_page(tag_alias), encoding="utf-8")

    for entry in entries:
        target_dir = DIARY_DIR / entry.slug
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "index.html").write_text(
            render_post_page(entry, related_posts.get(entry.slug, [])),
            encoding="utf-8",
        )


def write_machine_readable(
    entries: list[Entry],
    tags: list[TagInfo],
    start_here_entries: list[Entry],
    cornerstone_entries: list[Entry],
    themes: list[ThemeInfo],
) -> None:
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

    DIARY_START_HERE_JSON.write_text(
        json.dumps(make_start_here_payload(start_here_entries), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    DIARY_THEMES_JSON.write_text(
        json.dumps(make_themes_payload(themes), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    DIARY_CORNERSTONES_JSON.write_text(
        json.dumps(make_cornerstones_payload(cornerstone_entries), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    DIARY_TAG_MAP_JSON.write_text(
        json.dumps(make_tag_map_payload(tags), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    write_feed(entries)


def render_home_slot_from_state(latest_item: dict[str, object] | None) -> str:
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
            <a href="./diary/start-here/">Start here</a>
            <a href="./diary/archive/">Open archive</a>
          </div>
        </div>
      </section>"""

    image_html = ""
    primary_image = latest_item.get("primary_image")
    if isinstance(primary_image, str) and primary_image.startswith(SITE_URL):
        image_alt = str(latest_item.get("image_alt", "")).strip() or str(latest_item.get("title", "Latest diary entry"))
        image_html = f"""
          <div class="entry-cover">
            <img src="./{html.escape(primary_image.removeprefix(SITE_URL))}" alt="{html.escape(image_alt)}">
          </div>
"""
    return f"""      <section class="section">
        <div class="section-head">
          <p class="section-label">Diary</p>
          <h2>Latest post</h2>
        </div>
        <article class="entry-card">
{image_html}          <div class="entry-meta">
            <span>{html.escape(str(latest_item.get('date', '')))}</span>
          </div>
          <h3>{html.escape(str(latest_item.get('title', 'Latest diary entry')))}</h3>
          <p class="entry-summary">{html.escape(str(latest_item.get('summary', '')))}</p>
          <div class="section-links">
            <a href="./diary/{html.escape(str(latest_item.get('slug', '')))}/">Open latest post</a>
            <a href="./diary/">Open Diary</a>
            <a href="./diary/start-here/">Start here</a>
          </div>
        </article>
      </section>"""


def update_home_slot() -> None:
    home = HOME_PATH.read_text(encoding="utf-8")
    if HOME_SLOT_START not in home or HOME_SLOT_END not in home:
        raise ValueError("Home page is missing diary slot markers")

    latest_payload = json.loads(DIARY_LATEST_JSON.read_text(encoding="utf-8"))
    slot_html = render_home_slot_from_state(latest_payload.get("item"))

    replacement = HOME_SLOT_START + "\n" + slot_html + "\n      " + HOME_SLOT_END
    pattern = re.compile(re.escape(HOME_SLOT_START) + r".*?" + re.escape(HOME_SLOT_END), re.DOTALL)
    updated = pattern.sub(replacement, home, count=1)
    HOME_PATH.write_text(updated, encoding="utf-8")


def main() -> None:
    entries = load_entries()
    curation = load_curation(entries)
    alias_map = build_tag_alias_map(curation)
    entries = normalize_entry_tags(entries, alias_map)
    tags, tag_aliases = build_tag_index(entries, alias_map)
    themes, entry_themes = build_theme_index(entries, curation)
    related_posts = build_related_posts(entries, entry_themes)
    entry_lookup = {entry.slug: entry for entry in entries}
    start_here_entries = [entry_lookup[slug] for slug in curation.start_here_slugs]
    cornerstone_entries = [entry_lookup[slug] for slug in curation.cornerstone_slugs]
    write_diary_outputs(entries, tags, tag_aliases, start_here_entries, cornerstone_entries, themes, related_posts)
    write_machine_readable(entries, tags, start_here_entries, cornerstone_entries, themes)
    update_home_slot()


if __name__ == "__main__":
    main()
