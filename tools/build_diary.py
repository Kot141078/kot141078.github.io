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
SITEMAP_PATH = ROOT / "sitemap.xml"
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
POST_TAG_LINK_LIMIT = 6
RELATED_POST_LIMIT = 4

SEMANTIC_STOP_WORDS = {
    "about",
    "after",
    "also",
    "among",
    "because",
    "being",
    "between",
    "could",
    "does",
    "from",
    "have",
    "into",
    "more",
    "most",
    "only",
    "other",
    "should",
    "that",
    "their",
    "there",
    "these",
    "they",
    "this",
    "through",
    "what",
    "when",
    "where",
    "which",
    "while",
    "with",
    "would",
}


def write_text_lf(path: Path, text: str) -> None:
    """Write deterministic UTF-8 text without platform newline drift."""
    path.write_text(text, encoding="utf-8", newline="\n")

# Exact duplicate import retained as a historical route. The non-numbered route
# is the sole indexable entity; the alias remains reachable and points to it.
DIARY_POST_CANONICAL_ALIASES = {
    "there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity-0116":
        "there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity",
}

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
    def canonical_slug(self) -> str:
        return DIARY_POST_CANONICAL_ALIASES.get(self.slug, self.slug)

    @property
    def canonical_url(self) -> str:
        return f"{DIARY_URL}{self.canonical_slug}/"

    @property
    def identifier(self) -> str:
        return f"urn:ivankotov:diary:{self.canonical_slug}"

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
class DisplayTagInfo:
    name: str
    slug: str
    count: int
    aliases: list[str]


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
        ("Vision", f"{prefix}vision/"),
        ("Publications", "/publications/"),
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


DISPLAY_TAG_FAMILIES: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    ("AI Safety", "ai-safety", ("AI Safety", "AISafety", "AIsafety")),
    ("AI Architecture", "ai-architecture", ("AI Architecture", "AIArchitecture")),
    (
        "Advanced Global Intelligence",
        "advanced-global-intelligence",
        ("Advanced Global Intelligence", "AdvancedGlobalIntelligence", "AGI"),
    ),
    ("Systems Thinking", "systems-thinking", ("Systems Thinking", "SystemsThinking")),
    (
        "Human-Centered AI",
        "human-centered-ai",
        ("HumanCenteredAI", "Human Centered AI", "Human-Centered AI", "Human Centric AI"),
    ),
    ("Long-Lived AI", "long-lived-ai", ("LongLivedAI", "Long Lived AI", "Long-Lived AI")),
    ("AI Governance", "ai-governance", ("AIGovernance", "AIgovernance", "AI Governance")),
    ("Digital Entities", "digital-entities", ("DigitalEntities", "Digital Entities")),
    ("Digital Sovereignty", "digital-sovereignty", ("DigitalSovereignty", "Digital Sovereignty")),
    ("AI Infrastructure", "ai-infrastructure", ("AIInfrastructure", "AI Infrastructure")),
    ("Human AI", "human-ai", ("HumanAI", "Human AI")),
    ("Future of AI", "future-of-ai", ("FutureOfAI", "Future of AI")),
)

DISPLAY_CONNECTOR_WORDS = {"and", "as", "by", "for", "from", "in", "of", "on", "or", "the", "to", "vs", "with"}
PROTECTED_DISPLAY_TOKENS = {
    "a6": "A6",
    "ai": "AI",
    "agi": "AGI",
    "amdr": "AMDR",
    "arq": "ARQ",
    "bcec": "BCEC",
    "ccdp": "CCDP",
    "cgam": "CGAM",
    "cpap": "CPAP",
    "d4": "D4",
    "ea": "EA",
    "eu": "EU",
    "l4": "L4",
    "la": "LA",
    "llm": "LLM",
    "pamdc": "PAMDC",
    "pf": "PF",
    "ser": "SER",
    "srlm": "SRLM",
    "vxcx": "VXCX",
    "wbgt": "WBGT",
    "wdc": "WDC",
}
DISPLAY_ACRONYMS = {"api", "gpai", "grc", "json", "mcp", "pdf", "sql", "ui", "ux", *PROTECTED_DISPLAY_TOKENS}


def display_tag_family_lookup() -> dict[str, tuple[str, str]]:
    lookup: dict[str, tuple[str, str]] = {}
    for display_name, preferred_slug, aliases in DISPLAY_TAG_FAMILIES:
        lookup[normalize_tag_slug(display_name)] = (display_name, preferred_slug)
        for alias in aliases:
            lookup[normalize_tag_slug(alias)] = (display_name, preferred_slug)
    return lookup


def protected_display_token(value: str) -> str | None:
    cleaned = value.replace("_", " ").replace("-", " ").strip()
    compact = re.sub(r"\s+", "", cleaned)
    if compact and re.fullmatch(r"[A-Za-z0-9]+", compact):
        return PROTECTED_DISPLAY_TOKENS.get(compact.lower())
    return None


def humanize_tag_name(value: str) -> str:
    family = display_tag_family_lookup().get(normalize_tag_slug(value))
    if family:
        return family[0]

    protected = protected_display_token(value)
    if protected:
        return protected

    cleaned = value.replace("_", " ").replace("-", " ").strip()
    if " " in cleaned:
        parts = [part for part in cleaned.split() if part]
    else:
        parts = re.findall(r"[A-Z]+(?=[A-Z][a-z]|\d|$)|[A-Z]?[a-z]+|\d+", cleaned) or [cleaned]

    words: list[str] = []
    for index, part in enumerate(parts):
        raw = part.strip()
        lower = raw.lower()
        if lower in DISPLAY_ACRONYMS:
            words.append(lower.upper())
        elif lower in DISPLAY_CONNECTOR_WORDS and 0 < index < len(parts) - 1:
            words.append(lower)
        else:
            words.append(raw[:1].upper() + raw[1:].lower())
    return " ".join(words)


def choose_display_tag_slug(display_name: str, candidate_slug: str, tag_slug_lookup: dict[str, TagInfo]) -> str:
    family = display_tag_family_lookup().get(normalize_tag_slug(display_name))
    if family and family[1] in tag_slug_lookup:
        return family[1]
    if candidate_slug in tag_slug_lookup:
        return candidate_slug
    display_slug = normalize_tag_slug(display_name)
    if display_slug in tag_slug_lookup:
        return display_slug
    return candidate_slug or display_slug


def display_tags_for_entry(entry: Entry, tag_slug_lookup: dict[str, TagInfo]) -> list[DisplayTagInfo]:
    tags: list[DisplayTagInfo] = []
    seen: set[str] = set()
    for tag in entry.tags:
        display_name = humanize_tag_name(tag.name)
        display_key = normalize_tag_slug(display_name)
        if not display_key or display_key in seen:
            continue
        seen.add(display_key)
        tags.append(
            DisplayTagInfo(
                name=display_name,
                slug=choose_display_tag_slug(display_name, tag.slug, tag_slug_lookup),
                count=1,
                aliases=[tag.name],
            )
        )
    return tags


def build_landing_display_tags(entries: list[Entry], tags: list[TagInfo]) -> list[DisplayTagInfo]:
    tag_slug_lookup = {tag.slug: tag for tag in tags}
    counts: dict[str, set[str]] = defaultdict(set)
    aliases: dict[str, set[str]] = defaultdict(set)
    names: dict[str, str] = {}
    slugs: dict[str, str] = {}

    for entry in entries:
        per_entry_seen: set[str] = set()
        for tag in [*entry.tags, *entry.raw_tags]:
            display_name = humanize_tag_name(tag.name)
            display_key = normalize_tag_slug(display_name)
            if not display_key or display_key in per_entry_seen:
                continue
            per_entry_seen.add(display_key)
            names.setdefault(display_key, display_name)
            slugs.setdefault(display_key, choose_display_tag_slug(display_name, tag.slug, tag_slug_lookup))
            counts[display_key].add(entry.slug)
            aliases[display_key].add(tag.name)

    display_tags = [
        DisplayTagInfo(
            name=names[key],
            slug=slugs[key],
            count=len(entry_slugs),
            aliases=sorted(aliases[key], key=str.lower),
        )
        for key, entry_slugs in counts.items()
    ]
    display_tags.sort(key=lambda tag: (-tag.count, tag.name.lower(), tag.slug))
    return display_tags


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


def semantic_tokens(entry: Entry) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", f"{entry.title} {entry.summary}".casefold())
        if len(token) >= 3 and token not in SEMANTIC_STOP_WORDS
    }


def select_primary_tags(entry: Entry) -> list[TagRef]:
    """Prefer canonical tags supported by the entry title or summary."""
    context_tokens = semantic_tokens(entry)

    def relevance(item: tuple[int, TagRef]) -> tuple[int, int, int, int]:
        index, tag = item
        tag_tokens = {
            token
            for token in re.findall(r"[a-z0-9]+", f"{tag.name} {tag.slug}".casefold())
            if len(token) >= 3 and token not in SEMANTIC_STOP_WORDS
        }
        overlap = tag_tokens & context_tokens
        return (int(bool(overlap)), len(overlap), sum(len(token) for token in overlap), -index)

    ranked = sorted(enumerate(entry.tags), key=relevance, reverse=True)
    return [tag for _, tag in ranked[:POST_TAG_LINK_LIMIT]]


def score_related_entry(
    entry: Entry,
    candidate: Entry,
    entry_themes: dict[str, list[ThemeInfo]],
    tag_frequency: Counter[str],
) -> tuple[int, int, int, int, int, int, int]:
    entry_primary_topics = {tag.slug for tag in select_primary_tags(entry)}
    candidate_primary_topics = {tag.slug for tag in select_primary_tags(candidate)}
    shared_primary_topic_slugs = entry_primary_topics & candidate_primary_topics
    shared_primary_topics = len(shared_primary_topic_slugs)
    topic_specificity = max((1_000_000 // tag_frequency[tag] for tag in shared_primary_topic_slugs), default=0)
    entry_theme_slugs = {theme.slug for theme in entry_themes.get(entry.slug, [])}
    candidate_theme_slugs = {theme.slug for theme in entry_themes.get(candidate.slug, [])}
    shared_themes = len(entry_theme_slugs & candidate_theme_slugs)
    semantic_overlap = len(semantic_tokens(entry) & semantic_tokens(candidate))
    days_apart = abs((entry.entry_date - candidate.entry_date).days)
    return (
        int(bool(shared_themes)),
        shared_themes,
        int(bool(shared_primary_topics)),
        shared_primary_topics,
        topic_specificity,
        semantic_overlap,
        -days_apart,
    )


def build_related_posts(entries: list[Entry], entry_themes: dict[str, list[ThemeInfo]]) -> dict[str, list[Entry]]:
    related: dict[str, list[Entry]] = {}
    tag_frequency: Counter[str] = Counter(tag.slug for item in entries for tag in item.tags)

    for entry in entries:
        ranked: list[tuple[int, int, int, int, int, int, int, Entry]] = []
        for candidate in entries:
            if candidate.slug == entry.slug or candidate.title == entry.title:
                continue
            score = score_related_entry(entry, candidate, entry_themes, tag_frequency)
            ranked.append((*score, candidate))

        ranked.sort(key=lambda item: (*item[:-1], item[-1].slug), reverse=True)
        selected: list[Entry] = []
        seen_signatures: set[tuple[str, ...]] = set()
        for *_, candidate in ranked:
            signature = tuple(sorted(tag.slug for tag in candidate.tags))
            if signature and signature in seen_signatures:
                continue
            selected.append(candidate)
            if signature:
                seen_signatures.add(signature)
            if len(selected) == RELATED_POST_LIMIT:
                break
        if len(selected) < RELATED_POST_LIMIT:
            for *_, candidate in ranked:
                if candidate in selected:
                    continue
                selected.append(candidate)
                if len(selected) == RELATED_POST_LIMIT:
                    break
        related[entry.slug] = selected

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
        "canonical_page": entry.canonical_url,
        "identifier": entry.identifier,
        "is_canonical": entry.url == entry.canonical_url,
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
    robots: str | None = None,
) -> str:
    og_image_line = f'\n  <meta property="og:image" content="{html.escape(og_image)}">' if og_image else ""
    robots_line = f'\n  <meta name="robots" content="{html.escape(robots)}">' if robots else ""
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
  <meta property="og:url" content="{html.escape(canonical)}">{og_image_line}{robots_line}
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


def render_entry_card(entry: Entry, *, asset_prefix: str, entry_href: str, include_image: bool) -> str:
    image_html = ""
    if include_image and entry.primary_image:
        image_html = f"""
            <div class="entry-cover">
              <img src="{html.escape(asset_prefix + entry.primary_image)}" alt="{html.escape(entry.image_alt or entry.title)}">
            </div>
"""
    return f"""          <article class="entry-card">
{image_html}            <div class="entry-meta">
              <span>{entry.date_iso}</span>
            </div>
            <h3>{html.escape(entry.title)}</h3>
            <p class="entry-summary">{html.escape(entry.summary)}</p>
            <div class="section-links">
              <a href="{html.escape(entry_href)}">Open entry</a>
            </div>
          </article>"""


def render_entry_collection(
    entries: list[Entry],
    *,
    asset_prefix: str,
    entry_prefix: str,
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
            include_image=include_image,
        )
        for entry in selected
    ]
    return f"        <div class=\"{wrapper_class}\">\n" + "\n".join(cards) + "\n        </div>\n"


def format_display_date(value: date) -> str:
    return f"{value.day} {value.strftime('%B %Y')}"


def archive_stats_text(entries: list[Entry]) -> str:
    if not entries:
        return "0 entries"
    oldest = min(entry.entry_date for entry in entries)
    newest = max(entry.entry_date for entry in entries)
    return f"{len(entries)} entries · {format_display_date(oldest)}–{format_display_date(newest)}"


def render_landing_tag_chips(entry: Entry, tag_slug_lookup: dict[str, TagInfo], *, tag_prefix: str, limit: int = 6) -> str:
    display_tags = display_tags_for_entry(entry, tag_slug_lookup)
    if not display_tags:
        return ""
    selected = display_tags[:limit]
    chips = [
        f'              <a class="landing-tag-chip" href="{html.escape(tag_prefix + tag.slug + "/")}">{html.escape(tag.name)}</a>'
        for tag in selected
    ]
    extra_count = len(display_tags) - len(selected)
    if extra_count > 0:
        chips.append(f'              <span class="landing-tag-more" aria-label="{extra_count} additional tags">+{extra_count} more</span>')
    return "            <div class=\"landing-tag-list\" aria-label=\"Display tags\">\n" + "\n".join(chips) + "\n            </div>\n"


def render_landing_entry_card(
    entry: Entry,
    *,
    asset_prefix: str,
    entry_href: str,
    tag_prefix: str,
    tag_slug_lookup: dict[str, TagInfo],
    include_image: bool,
    eager_image: bool = False,
    step_number: int | None = None,
    compact: bool = False,
) -> str:
    image_html = ""
    if include_image and entry.primary_image:
        loading = "eager" if eager_image else "lazy"
        image_html = f"""
            <div class="entry-cover landing-card-media">
              <img src="{html.escape(asset_prefix + entry.primary_image)}" alt="{html.escape(entry.image_alt or entry.title)}" loading="{loading}" decoding="async">
            </div>
"""
    step_html = ""
    if step_number is not None:
        step_html = f'            <span class="route-step" aria-label="Editorial route step {step_number:02d}">{step_number:02d}</span>\n'
    tag_links = render_landing_tag_chips(entry, tag_slug_lookup, tag_prefix=tag_prefix, limit=6)
    classes = "entry-card landing-entry-card"
    if compact:
        classes += " landing-entry-card-compact"
    return f"""          <article class="{classes}">
{image_html}            <div class="landing-card-body">
{step_html}              <div class="entry-meta">
                <span>{entry.date_iso}</span>
              </div>
              <h3>{html.escape(entry.title)}</h3>
              <p class="entry-summary">{html.escape(entry.summary)}</p>
{tag_links}              <div class="section-links landing-card-actions">
                <a href="{html.escape(entry_href)}">Open entry</a>
              </div>
            </div>
          </article>"""


def render_landing_entry_collection(
    entries: list[Entry],
    *,
    asset_prefix: str,
    entry_prefix: str,
    tag_prefix: str,
    tag_slug_lookup: dict[str, TagInfo],
    include_image: bool,
    limit: int | None,
    wrapper_class: str,
    numbered: bool = False,
    compact: bool = False,
    eager_image_count: int = 1,
) -> str:
    selected = entries if limit is None else entries[:limit]
    cards = [
        render_landing_entry_card(
            entry,
            asset_prefix=asset_prefix,
            entry_href=f"{entry_prefix}{entry.slug}/",
            tag_prefix=tag_prefix,
            tag_slug_lookup=tag_slug_lookup,
            include_image=include_image,
            eager_image=index < eager_image_count,
            step_number=index + 1 if numbered else None,
            compact=compact,
        )
        for index, entry in enumerate(selected)
    ]
    return f"        <div class=\"{wrapper_class}\">\n" + "\n".join(cards) + "\n        </div>\n"


def render_latest_entries(entries: list[Entry], tag_slug_lookup: dict[str, TagInfo]) -> str:
    if not entries:
        return render_empty_state(
            "No diary entries are published yet.",
            "The latest-entries slot is ready for future batch imports, but this pass intentionally keeps the archive empty until real source materials are provided.",
        )
    return render_landing_entry_collection(
        entries[:5],
        asset_prefix="../",
        entry_prefix="./",
        tag_prefix="./tags/",
        tag_slug_lookup=tag_slug_lookup,
        include_image=True,
        limit=5,
        wrapper_class="diary-latest-grid",
        compact=True,
        eager_image_count=5,
    )


def render_cornerstones(entries: list[Entry], tag_slug_lookup: dict[str, TagInfo]) -> str:
    if not entries:
        return render_empty_state("No cornerstone entries were configured.", "Cornerstones appear only when the curation config selects real diary entries.")
    return render_landing_entry_collection(
        entries,
        asset_prefix="../",
        entry_prefix="./",
        tag_prefix="./tags/",
        tag_slug_lookup=tag_slug_lookup,
        include_image=False,
        limit=None,
        wrapper_class="diary-compact-card-grid",
        compact=True,
    )


def render_start_here_cards(
    entries: list[Entry],
    *,
    asset_prefix: str,
    entry_prefix: str,
    tag_prefix: str | None = None,
    tag_slug_lookup: dict[str, TagInfo] | None = None,
) -> str:
    if not entries:
        return render_empty_state("No start-here entries were configured.", "The start-here surface appears only after curated entry slugs are selected.")
    if tag_slug_lookup is not None:
        if tag_prefix is None:
            raise ValueError("Landing start-here cards require a tag prefix")
        return render_landing_entry_collection(
            entries,
            asset_prefix=asset_prefix,
            entry_prefix=entry_prefix,
            tag_prefix=tag_prefix,
            tag_slug_lookup=tag_slug_lookup,
            include_image=True,
            limit=None,
            wrapper_class="diary-start-grid",
            numbered=True,
            compact=True,
        )
    return render_entry_collection(
        entries,
        asset_prefix=asset_prefix,
        entry_prefix=entry_prefix,
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


def render_landing_tag_preview(display_tags: list[DisplayTagInfo]) -> str:
    if not display_tags:
        return render_empty_state(
            "Tag surface is waiting for real entries.",
            "Tags will only be shown after imported entries bring confirmed labels.",
        )
    selected = display_tags[:16]
    chips = [
        f'<a class="archive-chip landing-tag-chip" href="./tags/{html.escape(tag.slug)}/">{html.escape(tag.name)} ({tag.count})</a>'
        for tag in selected
    ]
    return "        <div class=\"archive-chip-list landing-top-tag-list\">\n          " + "\n          ".join(chips) + "\n        </div>\n"


def render_browse_search() -> str:
    return """      <section class="section diary-browse-search" id="browse-search" data-diary-section="browse-search">
        <div class="section-head">
          <p class="section-label">Browse and search</p>
          <h2>Find a route into the archive</h2>
          <p class="diary-note">Search stays local to this public archive index and uses no external service, analytics, or tracking.</p>
        </div>
        <div class="diary-browse-grid">
          <div class="section-links diary-browse-links" aria-label="Browse Diary routes">
            <a href="./archive/">Browse full archive</a>
            <a href="./themes/">Browse by theme</a>
            <a href="./tags/">Browse tags</a>
          </div>
          <form class="diary-search" role="search" action="./archive/" data-diary-search-form>
            <label for="diary-search-input">Search the Diary</label>
            <div class="diary-search-row">
              <input id="diary-search-input" name="q" type="search" autocomplete="off" placeholder="Search title, summary, date, or tag" aria-controls="diary-search-results" aria-expanded="false" data-diary-search-input>
            </div>
            <p class="diary-search-status" id="diary-search-status" role="status" aria-live="polite" data-diary-search-status></p>
            <div class="diary-search-results" id="diary-search-results" role="listbox" hidden data-diary-search-results></div>
            <noscript>
              <p class="diary-note">Search requires JavaScript. Archive, theme, and tag links remain available.</p>
            </noscript>
          </form>
        </div>
      </section>
"""


def render_diary_search_script() -> str:
    return """      <script>
        (() => {
          const form = document.querySelector("[data-diary-search-form]");
          const input = document.querySelector("[data-diary-search-input]");
          const results = document.querySelector("[data-diary-search-results]");
          const status = document.querySelector("[data-diary-search-status]");
          if (!form || !input || !results || !status) return;

          let entries = [];
          let activeIndex = -1;
          let debounceTimer = 0;
          const maxResults = 10;

          const escapeHTML = (value) => String(value || "").replace(/[&<>"']/g, (char) => ({
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#39;"
          })[char]);

          const clearResults = () => {
            activeIndex = -1;
            results.hidden = true;
            results.innerHTML = "";
            input.setAttribute("aria-expanded", "false");
            status.textContent = "";
          };

          const setActive = (index) => {
            const links = Array.from(results.querySelectorAll("a"));
            links.forEach((link) => link.classList.remove("is-active"));
            if (!links.length) {
              activeIndex = -1;
              return;
            }
            activeIndex = Math.max(0, Math.min(index, links.length - 1));
            links[activeIndex].classList.add("is-active");
            links[activeIndex].scrollIntoView({ block: "nearest" });
          };

          const searchableText = (item) => [
            item.title,
            item.summary,
            item.date,
            ...(Array.isArray(item.tags) ? item.tags : []),
            ...(Array.isArray(item.raw_tags) ? item.raw_tags : [])
          ].filter(Boolean).join(" ").toLocaleLowerCase();

          const render = () => {
            const query = input.value.trim().toLocaleLowerCase();
            if (!query) {
              clearResults();
              return;
            }
            const matches = entries
              .filter((item) => searchableText(item).includes(query))
              .slice(0, maxResults);
            results.innerHTML = matches.map((item, index) => `
              <a href="${escapeHTML(item.page)}" role="option" data-result-index="${index}">
                <span>${escapeHTML(item.date)}</span>
                <strong>${escapeHTML(item.title || "Untitled entry")}</strong>
                ${item.summary ? `<em>${escapeHTML(item.summary)}</em>` : ""}
              </a>
            `).join("");
            results.hidden = matches.length === 0;
            input.setAttribute("aria-expanded", matches.length ? "true" : "false");
            status.textContent = matches.length ? `${matches.length} result${matches.length === 1 ? "" : "s"}` : "No results";
            activeIndex = -1;
          };

          form.addEventListener("submit", (event) => event.preventDefault());
          input.addEventListener("input", () => {
            window.clearTimeout(debounceTimer);
            debounceTimer = window.setTimeout(render, 140);
          });
          input.addEventListener("keydown", (event) => {
            const links = Array.from(results.querySelectorAll("a"));
            if (event.key === "Escape") {
              input.value = "";
              clearResults();
              return;
            }
            if (event.key === "ArrowDown" && links.length) {
              event.preventDefault();
              setActive(activeIndex < 0 ? 0 : activeIndex + 1);
              return;
            }
            if (event.key === "ArrowUp" && links.length) {
              event.preventDefault();
              setActive(activeIndex < 0 ? links.length - 1 : activeIndex - 1);
              return;
            }
            if (event.key === "Enter" && activeIndex >= 0 && links[activeIndex]) {
              event.preventDefault();
              links[activeIndex].click();
            }
          });
          results.addEventListener("mousemove", (event) => {
            const link = event.target.closest("a[data-result-index]");
            if (link) setActive(Number(link.dataset.resultIndex));
          });

          fetch("../diary-index.json", { cache: "no-store" })
            .then((response) => response.ok ? response.json() : Promise.reject(new Error("Diary index unavailable")))
            .then((payload) => { entries = Array.isArray(payload.items) ? payload.items : []; })
            .catch(() => { status.textContent = "Search index unavailable"; });
        })();
      </script>
"""


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


def render_archive_groups(entries: list[Entry], *, asset_prefix: str, entry_prefix: str) -> str:
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
            alias_note = f"\n            <p>Normalized from {len(tag.aliases)} raw source labels.</p>"
        cards.append(
            f"""          <article class="surface-group">
            <h3>{html.escape(tag.name)}</h3>
            <p>{tag.count} linked entr{'y' if tag.count == 1 else 'ies'} in the archive.</p>{alias_note}
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


def render_related_posts(related_entries: list[Entry]) -> str:
    if not related_entries:
        return ""
    cards = [
        render_entry_card(
            item,
            asset_prefix="../../",
            entry_href=f"../{item.slug}/",
            include_image=False,
        )
        for item in related_entries[:RELATED_POST_LIMIT]
    ]
    return f"""
      <section class="section">
        <div class="section-head">
          <p class="section-label">Related posts</p>
          <h2>Continue from here</h2>
          <p class="diary-note">Curated themes and canonical topics lead; semantic fit follows, with chronology used only as a fallback.</p>
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
            "@id": f"{entry.canonical_url}#post",
            "headline": entry.title,
            "identifier": entry.identifier,
            "url": entry.canonical_url,
            "mainEntityOfPage": entry.canonical_url,
            "datePublished": entry.date_iso,
            "dateModified": entry.date_iso,
            "author": {"@type": "Person", "name": "Ivan Kotov", "url": "https://ivankotov.eu/about/"},
            "publisher": {"@type": "Person", "name": "Ivan Kotov", "url": "https://ivankotov.eu/about/"},
            "description": entry.summary,
            "isPartOf": {"@type": "Blog", "url": DIARY_URL, "name": DIARY_TITLE},
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"{entry.canonical_url}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL},
                {"@type": "ListItem", "position": 2, "name": "Diary", "item": DIARY_URL},
                {"@type": "ListItem", "position": 3, "name": entry.title, "item": entry.canonical_url},
            ],
        },
    ]
    if entry.tags:
        graph[0]["keywords"] = ", ".join(tag.name for tag in entry.tags)
    if entry.primary_image:
        graph[0]["image"] = f"{SITE_URL}{entry.primary_image}"
    if entry.linkedin_url:
        graph[0]["sameAs"] = entry.linkedin_url
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def render_diary_index(
    entries: list[Entry],
    tags: list[TagInfo],
    start_here_entries: list[Entry],
    cornerstone_entries: list[Entry],
    themes: list[ThemeInfo],
) -> str:
    tag_slug_lookup = {tag.slug: tag for tag in tags}
    display_tags = build_landing_display_tags(entries, tags)
    stats = archive_stats_text(entries)
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

    body_html = f"""      <div class="diary-landing">
      <section class="hero diary-landing-hero" data-diary-section="hero">
        <p class="eyebrow">Curated archive surface</p>
        <h1>Diary</h1>
        <p class="lead page-lead">Public archive of posts, notes, and linked visual surfaces, with latest posts first and curated routes available when a structured reading path helps.</p>
        <p class="diary-archive-stat">{html.escape(stats)}</p>
        <div class="section-links diary-hero-actions" aria-label="Primary Diary actions">
          <a href="./archive/">Browse full archive</a>
          <a href="./themes/">Browse by theme</a>
          <a href="./tags/">Browse tags</a>
          <a href="./start-here/" class="secondary-action">Start here</a>
        </div>
      </section>

{empty_state}
      <section class="section diary-latest-section" data-diary-section="latest">
        <div class="section-head">
          <p class="section-label">Latest entries</p>
          <h2>Latest from the Diary</h2>
        </div>
{render_latest_entries(entries, tag_slug_lookup)}
        <div class="section-links">
          <a href="./archive/">Open archive</a>
          <a href="./start-here/">Open Start here</a>
        </div>
      </section>

{render_browse_search()}
      <section class="section diary-start-section" data-diary-section="start-here">
        <div class="section-head">
          <p class="section-label">Curated entry path</p>
          <h2>Start here</h2>
          <p class="diary-note">These are not the newest posts and not a ranking. They form an editorial reading path through the archive.</p>
        </div>
{render_start_here_cards(start_here_entries, asset_prefix='../', entry_prefix='./', tag_prefix='./tags/', tag_slug_lookup=tag_slug_lookup)}
        <div class="section-links">
          <a href="./start-here/">Open Start here</a>
          <a href="./themes/">Open themes</a>
          <a href="./tags/">Open tags</a>
        </div>
      </section>

      <section class="section diary-themes-section" data-diary-section="themes">
        <div class="section-head">
          <p class="section-label">Themes</p>
          <h2>Topic-based reading paths</h2>
        </div>
{render_theme_cards(themes, link_prefix='./themes/')}
        <div class="section-links">
          <a href="./themes/">Open all themes</a>
        </div>
      </section>

      <section class="section diary-cornerstones-section" data-diary-section="cornerstones">
        <div class="section-head">
          <p class="section-label">Cornerstones</p>
          <h2>Posts that carry the structure</h2>
          <p class="diary-note">A wider set of anchor posts across releases, architecture, infrastructure, continuity, and the book layer.</p>
        </div>
{render_cornerstones(cornerstone_entries, tag_slug_lookup)}
        <div class="section-links">
          <a href="./archive/">Browse full archive</a>
          <a href="./themes/">Browse by theme</a>
        </div>
      </section>

      <section class="section diary-tags-section" data-diary-section="tags">
        <div class="section-head">
          <p class="section-label">Tags</p>
          <h2>Normalized tag surface</h2>
          <p class="diary-note">Canonical display tags reduce alias clutter on this landing page while preserving historical raw labels and existing tag URLs in the source corpus.</p>
        </div>
{render_landing_tag_preview(display_tags)}
        <div class="section-links">
          <a href="./tags/">Open tag index</a>
          <a href="./archive/">Open archive</a>
        </div>
      </section>
{render_diary_search_script()}
      </div>
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

{render_archive_groups(entries, asset_prefix='../../', entry_prefix='../')}
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
        robots="noindex, follow",
    )


def render_tag_page(tag: TagInfo) -> str:
    alias_note_html = ""
    if len(tag.aliases) > 1:
        alias_note_html = f'        <p class="diary-note">This canonical tag currently absorbs {len(tag.aliases)} raw source labels.</p>\n'
    body_html = f"""      <section class="hero">
        <p class="eyebrow">Diary tag</p>
        <h1>{html.escape(tag.name)}</h1>
        <p class="lead page-lead">Canonical diary tag page generated from normalized source tags.</p>
        <p class="diary-note">{tag.count} linked entr{'y' if tag.count == 1 else 'ies'} currently in the archive.</p>
{alias_note_html}      </section>

      <section class="section">
        <div class="section-head">
          <p class="section-label">Tagged entries</p>
          <h2>Entries linked to {html.escape(tag.name)}</h2>
        </div>
        <div class="entry-list">
{chr(10).join(render_entry_card(entry, asset_prefix='../../../', entry_href='../../' + entry.slug + '/', include_image=False) for entry in tag.entries)}
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
        robots="noindex, follow",
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
        robots="noindex, follow",
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
{render_start_here_cards(entries, asset_prefix='../../', entry_prefix='../')}
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
{render_entry_collection(theme.entries, asset_prefix='../../../', entry_prefix='../../', include_image=False, limit=None, wrapper_class='entry-list')}
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
        items = "".join(
            f'          <a href="../tags/{html.escape(tag.slug)}/">{html.escape(tag.name)}</a>\n'
            for tag in select_primary_tags(entry)
        )
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
{render_related_posts(related_entries)}"""

    return render_document(
        title=f"{entry.title} | Diary | Ivan Kotov",
        description=entry.summary,
        canonical=entry.canonical_url,
        og_type="article",
        og_image=f"{SITE_URL}{entry.primary_image}" if entry.primary_image else None,
        stylesheet_href="../../styles.css",
        nav_prefix="../../",
        nav_current="Diary",
        ld_json=post_ld_json(entry),
        body_html=body_html,
        robots="noindex,follow" if entry.url != entry.canonical_url else None,
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
    previous = previous_alias_orders()
    return {
        "site": SITE_URL,
        "page": DIARY_TAGS_URL,
        "canonical_tags": [
            {
                "tag": tag.name,
                "slug": tag.slug,
                "count": tag.count,
                "page": tag.url,
                "aliases": preserve_alias_order(tag.slug, tag.aliases, previous),
            }
            for tag in tags
        ],
    }


def make_tags_payload(tags: list[TagInfo]) -> dict[str, object]:
    previous = previous_alias_orders()
    return {
        "site": SITE_URL,
        "page": DIARY_TAGS_URL,
        "tags": [
            {
                "name": tag.name,
                "slug": tag.slug,
                "count": tag.count,
                "page": tag.url,
                "aliases": preserve_alias_order(tag.slug, tag.aliases, previous),
            }
            for tag in tags
        ],
    }


def previous_alias_orders() -> dict[str, list[str]]:
    if not DIARY_TAGS_JSON.exists():
        return {}
    try:
        payload = json.loads(DIARY_TAGS_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    orders: dict[str, list[str]] = {}
    for item in payload.get("tags", []):
        slug = item.get("slug")
        aliases = item.get("aliases")
        if isinstance(slug, str) and isinstance(aliases, list):
            orders[slug] = [alias for alias in aliases if isinstance(alias, str)]
    return orders


def preserve_alias_order(slug: str, aliases: list[str], previous: dict[str, list[str]]) -> list[str]:
    current = set(aliases)
    ordered = [alias for alias in previous.get(slug, []) if alias in current]
    remaining = [alias for alias in aliases if alias not in set(ordered)]
    return ordered + sorted(remaining, key=lambda value: (value.lower(), value))


def existing_feed_header() -> tuple[str, str] | None:
    if not DIARY_FEED_XML.exists():
        return None
    text = DIARY_FEED_XML.read_text(encoding="utf-8", errors="ignore")
    build_match = re.search(r"<lastBuildDate>([^<]+)</lastBuildDate>", text)
    guid_match = re.search(r"<guid>([^<]+)</guid>", text)
    if build_match and guid_match:
        return build_match.group(1), guid_match.group(1)
    return None


def write_feed(entries: list[Entry]) -> None:
    previous = existing_feed_header()
    if previous and entries and previous[1] == entries[0].url:
        build_date = previous[0]
    elif entries:
        build_date = entries[0].feed_date
    else:
        build_date = format_datetime(datetime(1970, 1, 1, tzinfo=timezone.utc))
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
    write_text_lf(DIARY_FEED_XML, rss)


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

    write_text_lf(
        DIARY_DIR / "index.html",
        render_diary_index(entries, tags, start_here_entries, cornerstone_entries, themes),
    )

    archive_dir = DIARY_DIR / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    write_text_lf(archive_dir / "index.html", render_archive_page(entries))

    start_here_dir = DIARY_DIR / "start-here"
    start_here_dir.mkdir(parents=True, exist_ok=True)
    write_text_lf(start_here_dir / "index.html", render_start_here_page(start_here_entries))

    themes_dir = DIARY_DIR / "themes"
    themes_dir.mkdir(parents=True, exist_ok=True)
    write_text_lf(themes_dir / "index.html", render_themes_index(themes))
    for theme in themes:
        theme_dir = themes_dir / theme.slug
        theme_dir.mkdir(parents=True, exist_ok=True)
        write_text_lf(theme_dir / "index.html", render_theme_page(theme))

    tags_dir = DIARY_DIR / "tags"
    tags_dir.mkdir(parents=True, exist_ok=True)
    write_text_lf(tags_dir / "index.html", render_tags_index(tags))

    for tag in tags:
        tag_dir = tags_dir / tag.slug
        tag_dir.mkdir(parents=True, exist_ok=True)
        write_text_lf(tag_dir / "index.html", render_tag_page(tag))

    for tag_alias in tag_aliases:
        tag_dir = tags_dir / tag_alias.slug
        tag_dir.mkdir(parents=True, exist_ok=True)
        write_text_lf(tag_dir / "index.html", render_tag_alias_page(tag_alias))

    for entry in entries:
        target_dir = DIARY_DIR / entry.slug
        target_dir.mkdir(parents=True, exist_ok=True)
        write_text_lf(target_dir / "index.html", render_post_page(entry, related_posts.get(entry.slug, [])))


def write_machine_readable(
    entries: list[Entry],
    tags: list[TagInfo],
    start_here_entries: list[Entry],
    cornerstone_entries: list[Entry],
    themes: list[ThemeInfo],
) -> None:
    index_payload = make_index_payload(entries)
    write_text_lf(DIARY_INDEX_JSON, json.dumps(index_payload, ensure_ascii=False, indent=2) + "\n")

    latest_payload = {
        "site": SITE_URL,
        "page": DIARY_URL,
        "item": index_payload["latest"],
    }
    write_text_lf(DIARY_LATEST_JSON, json.dumps(latest_payload, ensure_ascii=False, indent=2) + "\n")

    tags_payload = make_tags_payload(tags)
    write_text_lf(DIARY_TAGS_JSON, json.dumps(tags_payload, ensure_ascii=False, indent=2) + "\n")

    write_text_lf(
        DIARY_START_HERE_JSON,
        json.dumps(make_start_here_payload(start_here_entries), ensure_ascii=False, indent=2) + "\n",
    )
    write_text_lf(
        DIARY_THEMES_JSON,
        json.dumps(make_themes_payload(themes), ensure_ascii=False, indent=2) + "\n",
    )
    write_text_lf(
        DIARY_CORNERSTONES_JSON,
        json.dumps(make_cornerstones_payload(cornerstone_entries), ensure_ascii=False, indent=2) + "\n",
    )
    write_text_lf(
        DIARY_TAG_MAP_JSON,
        json.dumps(make_tag_map_payload(tags), ensure_ascii=False, indent=2) + "\n",
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
          <div class="entry-cover home-latest-cover">
            <img src="./{html.escape(primary_image.removeprefix(SITE_URL))}" alt="{html.escape(image_alt)}" loading="eager" decoding="async">
          </div>
"""
    return f"""      <section class="section home-latest-section">
        <div class="section-head">
          <p class="section-label">Latest post</p>
          <h2>Latest post</h2>
        </div>
        <article class="entry-card home-latest-card">
{image_html}          <div class="entry-meta">
            <span>{html.escape(str(latest_item.get('date', '')))}</span>
          </div>
          <h3>{html.escape(str(latest_item.get('title', 'Latest diary entry')))}</h3>
          <p class="entry-summary">{html.escape(str(latest_item.get('summary', '')))}</p>
          <div class="section-links">
            <a href="./diary/{html.escape(str(latest_item.get('slug', '')))}/">Open latest post</a>
            <a href="./diary/">Open Diary</a>
            <a href="./diary/archive/">Browse Diary archive</a>
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
    write_text_lf(HOME_PATH, updated)


def sitemap_url_pattern(url: str) -> re.Pattern[str]:
    return re.compile(
        rf"(?P<indent>^[ \t]*)<url>\s*<loc>{re.escape(url)}</loc>"
        rf"(?:\s*<lastmod>[^<]+</lastmod>)?\s*</url>",
        flags=re.MULTILINE,
    )


def update_diary_sitemap(entries: list[Entry], tag_aliases: list[TagAlias]) -> None:
    sitemap = SITEMAP_PATH.read_text(encoding="utf-8")
    for entry in entries:
        pattern = sitemap_url_pattern(entry.url)
        if entry.url != entry.canonical_url:
            sitemap, count = pattern.subn("", sitemap)
            if count > 1:
                raise ValueError(f"Duplicate sitemap alias URL: {entry.url}")
            continue
        match = pattern.search(sitemap)
        if match is None:
            raise ValueError(f"Canonical diary post is missing from sitemap: {entry.url}")
        indent = match.group("indent")
        replacement = (
            f"{indent}<url>\n"
            f"{indent}  <loc>{entry.url}</loc>\n"
            f"{indent}  <lastmod>{entry.date_iso}</lastmod>\n"
            f"{indent}</url>"
        )
        sitemap, count = pattern.subn(replacement, sitemap)
        if count != 1:
            raise ValueError(f"Unexpected sitemap entry count for {entry.url}: {count}")

    for tag_alias in tag_aliases:
        sitemap, count = sitemap_url_pattern(tag_alias.url).subn("", sitemap)
        if count > 1:
            raise ValueError(f"Duplicate sitemap tag alias URL: {tag_alias.url}")

    # Tag archives remain public navigation surfaces, but they are deliberately
    # not index-intended. Remove the index and every canonical/legacy tag page
    # from the sitemap in one source-level, idempotent pass.
    tag_surface_pattern = re.compile(
        rf"^[ \t]*<url>\s*<loc>{re.escape(DIARY_TAGS_URL)}[^<]*</loc>"
        rf"(?:\s*<lastmod>[^<]+</lastmod>)?\s*</url>[ \t]*(?:\r?\n|$)",
        flags=re.MULTILINE,
    )
    sitemap = tag_surface_pattern.sub("", sitemap)

    write_text_lf(SITEMAP_PATH, sitemap)


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
    update_diary_sitemap(entries, tag_aliases)


if __name__ == "__main__":
    main()
