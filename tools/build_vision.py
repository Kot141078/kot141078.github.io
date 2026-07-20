#!/usr/bin/env python3
"""Build the public Vision v0.1 page from the verified source projection."""

from __future__ import annotations

import csv
import hashlib
import html
import json
import re
from pathlib import Path


SITE_URL = "https://ivankotov.eu"
ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "content" / "vision" / "v0.1"
OUT_DIR = ROOT / "vision"
ROUTE = "/vision/"
CANONICAL_URL = SITE_URL + ROUTE
EXPECTED_ZIP_SHA256 = "73cd954062956a4d143b4ca4b2b77f00bba6b5e0817b020559a85e7d2210a02f"
EXPECTED_NONCLAIM_NOTE = (
    "No change to Baseline B0, Theoretical Core, protocol, implementation, "
    "test, replication, validation, empirical, legal, consciousness, "
    "personhood, or entity-classification status."
)

SOURCE_FILES = {
    "VISION_PAGE_COPY_EN_v0_1.md": "6dc7cf171edeb2880cd058e3685f13de8104e6d01d48e99ae1bf357a3750757f",
    "VISION_PAGE_DATA_v0_1.json": "2e015c494d045d054d78f13443b3b2933cf9a9273eb463bcc19aabcec9e8bfab",
    "VISION_PAGE_SCHEMAORG_v0_1.jsonld": "7dbf119aa2cf99d11415479838a1fb80d8ff750caea79774ceeff1aec75ec123",
    "VISION_PAGE_SECTION_MAP_v0_1.csv": "bc7336255d82d2b83b020afa097f47641f7d8af0c588e26785b6ea9a8dee4087",
}

REQUIRED_LINKS = [
    "/start-here/",
    "/c-a-plus-b/",
    "/l4/",
    "/ser/",
    "/what-is-running/",
    "/publications/",
    "/qubit-of-hope/",
    "/corpus/current-state/",
    "/advanced-global-intelligence/",
    "/distinctions/",
    "/evidence/",
    "/corpus-map/",
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def slugify(value: str) -> str:
    text = re.sub(r"<[^>]+>", "", value.lower())
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "section"


def validate_sources() -> tuple[dict, dict, dict, list[dict[str, str]], str]:
    missing = [name for name in SOURCE_FILES if not (SOURCE_DIR / name).exists()]
    if missing:
        raise RuntimeError(f"missing Vision source files: {missing}")

    receipt_path = SOURCE_DIR / "SOURCE_RECEIPT.json"
    if not receipt_path.exists():
        raise RuntimeError("missing content/vision/v0.1/SOURCE_RECEIPT.json")
    receipt = load_json(receipt_path)
    if receipt.get("source_zip_sha256") != EXPECTED_ZIP_SHA256:
        raise RuntimeError("Vision source ZIP SHA-256 mismatch in SOURCE_RECEIPT.json")
    if receipt.get("source_boundary") != "public_candidate_only":
        raise RuntimeError("Vision source boundary must be public_candidate_only")
    if receipt.get("public_entry_count") != 51 or receipt.get("mapped_entry_count") != 51:
        raise RuntimeError("Vision public/mapped entry counts must be 51/51")
    if receipt.get("internal_first_count") != 0:
        raise RuntimeError("Vision internal-first source count must be 0")

    for name, expected in SOURCE_FILES.items():
        actual = sha256_file(SOURCE_DIR / name)
        if actual != expected:
            raise RuntimeError(f"Vision source hash mismatch for {name}: {actual}")
        if receipt.get("imported_file_sha256", {}).get(name) != expected:
            raise RuntimeError(f"Vision receipt hash mismatch for {name}")

    data = load_json(SOURCE_DIR / "VISION_PAGE_DATA_v0_1.json")
    schema = load_json(SOURCE_DIR / "VISION_PAGE_SCHEMAORG_v0_1.jsonld")
    copy = (SOURCE_DIR / "VISION_PAGE_COPY_EN_v0_1.md").read_text(encoding="utf-8")
    with (SOURCE_DIR / "VISION_PAGE_SECTION_MAP_v0_1.csv").open("r", encoding="utf-8", newline="") as handle:
        section_map = list(csv.DictReader(handle))

    meta = data.get("metadata", {})
    if meta.get("route") != ROUTE or meta.get("canonical_url") != CANONICAL_URL:
        raise RuntimeError("Vision route/canonical mismatch")
    if meta.get("language") != "en" or meta.get("status") != "public_draft":
        raise RuntimeError("Vision metadata language/status mismatch")
    if meta.get("source_boundary") != "public_candidate_only":
        raise RuntimeError("Vision data source boundary mismatch")
    if data.get("sections", [{}])[0].get("slug") != "hero":
        raise RuntimeError("Vision data section 0 must be hero")
    expected_orders = list(range(0, 11))
    actual_orders = [item.get("order") for item in data.get("sections", [])]
    if actual_orders != expected_orders:
        raise RuntimeError(f"Vision section order mismatch: {actual_orders}")
    if schema.get("mainEntityOfPage") != CANONICAL_URL:
        raise RuntimeError("Vision schema mainEntityOfPage mismatch")
    if "VISION_PAGE_COPY_RU" in receipt_path.read_text(encoding="utf-8"):
        raise RuntimeError("receipt must not import the RU copy")

    return receipt, data, schema, section_map, copy


def strip_front_matter(markdown: str) -> str:
    if not markdown.startswith("---\n"):
        return markdown
    end = markdown.find("\n---\n", 4)
    if end == -1:
        raise RuntimeError("unterminated Vision front matter")
    return markdown[end + 5 :].lstrip()


def split_markdown(markdown: str) -> tuple[list[str], list[tuple[str, list[str]]]]:
    lines = strip_front_matter(markdown).splitlines()
    h2_indices = [idx for idx, line in enumerate(lines) if line.startswith("## ")]
    if not h2_indices:
        raise RuntimeError("Vision copy has no h2 sections")
    hero_lines = lines[: h2_indices[0]]
    sections: list[tuple[str, list[str]]] = []
    for pos, start in enumerate(h2_indices):
        end = h2_indices[pos + 1] if pos + 1 < len(h2_indices) else len(lines)
        title = lines[start][3:].strip()
        body = lines[start + 1 : end]
        sections.append((title, body))
    return hero_lines, sections


def inline(text: str) -> str:
    protected = "Agents are instruments of `c`; `c` are participants in society."
    text = e(text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{e(m.group(2))}">{m.group(1)}</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    if protected in html.unescape(text):
        return text
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def flush_paragraph(buffer: list[str], parts: list[str]) -> None:
    if not buffer:
        return
    paragraph = " ".join(item.strip() for item in buffer).strip()
    if paragraph:
        parts.append(f"          <p>{inline(paragraph)}</p>")
    buffer.clear()


def render_markdown_blocks(lines: list[str]) -> str:
    parts: list[str] = []
    paragraph: list[str] = []
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        stripped = line.strip()
        if not stripped:
            flush_paragraph(paragraph, parts)
            idx += 1
            continue
        if stripped == "---":
            flush_paragraph(paragraph, parts)
            parts.append('          <hr class="vision-divider">')
            idx += 1
            continue
        if stripped.startswith("> "):
            flush_paragraph(paragraph, parts)
            quotes: list[str] = []
            while idx < len(lines) and lines[idx].strip().startswith("> "):
                quotes.append(lines[idx].strip()[2:].strip())
                idx += 1
            parts.append(f"          <blockquote><p>{inline(' '.join(quotes))}</p></blockquote>")
            continue
        if stripped.startswith("- "):
            flush_paragraph(paragraph, parts)
            items: list[str] = []
            while idx < len(lines) and lines[idx].strip().startswith("- "):
                items.append(f"            <li>{inline(lines[idx].strip()[2:].strip())}</li>")
                idx += 1
            parts.append("          <ul>\n" + "\n".join(items) + "\n          </ul>")
            continue
        if stripped.startswith("|"):
            flush_paragraph(paragraph, parts)
            table_lines: list[str] = []
            while idx < len(lines) and lines[idx].strip().startswith("|"):
                table_lines.append(lines[idx].strip())
                idx += 1
            parts.append(render_table(table_lines))
            continue
        if stripped.startswith("```"):
            flush_paragraph(paragraph, parts)
            code: list[str] = []
            idx += 1
            while idx < len(lines) and not lines[idx].strip().startswith("```"):
                code.append(lines[idx])
                idx += 1
            if idx == len(lines):
                raise RuntimeError("unterminated Vision code block")
            idx += 1
            parts.append(f"          <pre><code>{e(chr(10).join(code))}</code></pre>")
            continue
        paragraph.append(line)
        idx += 1
    flush_paragraph(paragraph, parts)
    return "\n".join(parts)


def render_table(lines: list[str]) -> str:
    rows = [[cell.strip() for cell in line.strip("|").split("|")] for line in lines]
    if len(rows) < 2:
        raise RuntimeError("invalid Vision markdown table")
    header = rows[0]
    body_rows = [row for row in rows[2:] if len(row) == len(header)]
    head_html = "".join(f"<th>{inline(cell)}</th>" for cell in header)
    body_html = []
    for row in body_rows:
        body_html.append("              <tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in row) + "</tr>")
    return (
        '          <div class="vision-table-wrap">\n'
        '            <table class="matrix-table vision-table">\n'
        f"              <thead><tr>{head_html}</tr></thead>\n"
        "              <tbody>\n"
        + "\n".join(body_html)
        + "\n              </tbody>\n"
        "            </table>\n"
        "          </div>"
    )


def render_hero(hero_lines: list[str], data: dict) -> str:
    lines = [line for line in hero_lines if line.strip()]
    if not lines or lines[0].strip() != data["hero"]["eyebrow"]:
        raise RuntimeError("Vision hero eyebrow mismatch")
    h1 = next((line[2:].strip() for line in lines if line.startswith("# ")), "")
    if h1 != data["hero"]["title"]:
        raise RuntimeError("Vision hero h1 mismatch")
    quote = data["hero"]["quote"]
    if quote not in "\n".join(hero_lines):
        raise RuntimeError("Vision hero quote mismatch")

    first_h1 = next(idx for idx, line in enumerate(hero_lines) if line.startswith("# "))
    body_lines = hero_lines[first_h1 + 1 :]
    rendered_intro = render_markdown_blocks(body_lines)
    lens_cards = "\n".join(
        f"""          <article class="vision-lens-card">
            <span>{e(item["label"])}</span>
            <p>{e(item["text"])}</p>
          </article>"""
        for item in data["reading_lenses"]
    )
    return f"""      <section class="hero vision-hero" id="vision-top">
        <p class="eyebrow">{e(data["hero"]["eyebrow"])}</p>
        <h1>{e(data["hero"]["title"])}</h1>
        <div class="vision-hero-prose">
{rendered_intro}
        </div>
        <div class="vision-lens-grid" aria-label="Vision reading lenses">
{lens_cards}
        </div>
      </section>"""


def diagram_role_binding() -> str:
    return """          <figure class="vision-diagram" aria-labelledby="vision-diagram-role-title">
            <figcaption id="vision-diagram-role-title">Role separation and governed binding</figcaption>
            <div class="vision-diagram-grid vision-diagram-grid-four">
              <div><strong>Model</strong><span>Capability surface</span></div>
              <div><strong>Agent</strong><span>Bounded delegated worker</span></div>
              <div><strong>b</strong><span>Replaceable substrate</span></div>
              <div><strong>c</strong><span>Continuity-bearing trajectory</span></div>
            </div>
            <p>Capability enters authority only through governed binding, reviewable limits, and an accountable anchor boundary.</p>
          </figure>"""


def diagram_reality_chain() -> str:
    return """          <figure class="vision-diagram" aria-labelledby="vision-diagram-reality-title">
            <figcaption id="vision-diagram-reality-title">Reality before rhetoric</figcaption>
            <div class="vision-chain" role="list" aria-label="L3 to L4 chain">
              <span role="listitem">Rule</span>
              <span role="listitem">Permission</span>
              <span role="listitem">Witness</span>
              <span role="listitem">L4 consequence</span>
              <span role="listitem">Review</span>
            </div>
            <p>A claim remains weak until the record survives real cost, custody, latency, failure, and consequence.</p>
          </figure>"""


def diagram_experience_chain() -> str:
    return """          <figure class="vision-diagram" aria-labelledby="vision-diagram-experience-title">
            <figcaption id="vision-diagram-experience-title">From token output to verified experience</figcaption>
            <div class="vision-chain vision-chain-wide" role="list" aria-label="Experience chain">
              <span role="listitem">Situated event</span>
              <span role="listitem">Selective artifact</span>
              <span role="listitem">Authority boundary</span>
              <span role="listitem">Reviewable value</span>
            </div>
            <p>The valuable object is not private raw life. It is bounded uncertainty reduction with provenance and consent.</p>
          </figure>"""


def diagram_ecology() -> str:
    return """          <figure class="vision-diagram" aria-labelledby="vision-diagram-ecology-title">
            <figcaption id="vision-diagram-ecology-title">Distributed intelligence ecology</figcaption>
            <div class="vision-ecology">
              <span>Humans</span>
              <span>Local c-nodes</span>
              <span>Institutions</span>
              <span>Robots</span>
              <span>Public evidence</span>
              <span>Repairable infrastructure</span>
            </div>
            <p>No central throne is required. The architecture points toward many bounded intelligences sharing reality.</p>
          </figure>"""


def render_section(title: str, lines: list[str], data_sections: dict[str, dict]) -> str:
    title_clean = re.sub(r"^\d+\.\s*", "", title).replace("`", "")
    matched_slug = None
    for slug, item in data_sections.items():
        if item.get("title_en") == title_clean:
            matched_slug = slug
            break
    section_id = matched_slug or slugify(title)
    label = "Section" if matched_slug else "Boundary"
    role = data_sections.get(section_id, {}).get("role", "")
    lead = f'\n          <p class="section-intro">{e(role)}</p>' if role else ""
    body = render_markdown_blocks(lines)
    diagram = ""
    if section_id == "from-agents-to-c":
        diagram = "\n" + diagram_role_binding()
    elif section_id == "reality-before-rhetoric":
        diagram = "\n" + diagram_reality_chain()
    elif section_id == "experience-economy":
        diagram = "\n" + diagram_experience_chain()
    elif section_id == "advanced-global-intelligence":
        diagram = "\n" + diagram_ecology()
    return f"""      <section class="section vision-section" id="{e(section_id)}">
        <div class="section-head">
          <p class="section-label">{label}</p>
          <h2>{inline(title)}</h2>{lead}
        </div>
        <div class="prose vision-prose">
{body}{diagram}
        </div>
      </section>"""


def nav_html() -> str:
    items = [
        ("/", "Home"),
        ("/start-here/", "Start here"),
        ("/vision/", "Vision"),
        ("/install-c/", "How to install c"),
        ("/publications/", "Publications"),
        ("/diary/", "Diary"),
        ("/topics/", "Topics"),
        ("/library/", "Library"),
        ("/services/", "Services"),
        ("/about/", "About"),
        ("/contact/", "Contact"),
    ]
    return "\n        ".join(
        f'<a href="{href}"{" aria-current=" + chr(34) + "page" + chr(34) if href == ROUTE else ""}>{e(text)}</a>'
        for href, text in items
    )


def breadcrumb_json(title: str) -> str:
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": CANONICAL_URL + "#page",
                "url": CANONICAL_URL,
                "name": title,
                "isPartOf": {"@id": SITE_URL + "/#website"},
            },
            {
                "@type": "BreadcrumbList",
                "@id": CANONICAL_URL + "#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
                    {"@type": "ListItem", "position": 2, "name": "Vision", "item": CANONICAL_URL},
                ],
            },
        ],
    }
    return json.dumps(graph, ensure_ascii=False, indent=2)


def render_link_lists() -> str:
    links = [
        ("Start here", "/start-here/"),
        ("Current state", "/corpus/current-state/"),
        ("Advanced Global Intelligence", "/advanced-global-intelligence/"),
        ("Distinctions", "/distinctions/"),
        ("Evidence", "/evidence/"),
        ("Corpus map", "/corpus-map/"),
    ]
    return "\n".join(f'          <a href="{href}">{e(label)}</a>' for label, href in links)


def render_html(data: dict, schema: dict, copy: str) -> str:
    hero_lines, sections = split_markdown(copy)
    data_sections = {item["slug"]: item for item in data["sections"] if item["slug"] != "hero"}
    rendered = [render_hero(hero_lines, data)]

    rendered.append(
        f"""      <section class="section vision-context" aria-labelledby="vision-context-title">
        <div class="section-head">
          <p class="section-label">Page role</p>
          <h2 id="vision-context-title">Living authorial vision</h2>
          <p class="section-intro">This page is a personal vision, not a validation claim.</p>
        </div>
        <div class="vision-receipt-grid">
          <p><strong>Version</strong><span>{e(data["metadata"]["version"])}</span></p>
          <p><strong>Last revised</strong><span>{e(data["metadata"]["last_revised"])}</span></p>
          <p><strong>Source boundary</strong><span>{e(data["metadata"]["source_boundary"])}</span></p>
          <p><strong>Current evidence/status map</strong><span><a href="/corpus/current-state/">Living corpus B0 status remains unchanged</a></span></p>
        </div>
        <p class="vision-boundary-note">Derived from Vision Ledger v0.1 - public-candidate entries only. {EXPECTED_NONCLAIM_NOTE}</p>
      </section>"""
    )

    toc_links = "\n".join(
        f'          <a href="#{e(item["slug"])}">{e(item["order"])}. {e(item["title_en"])}</a>'
        for item in data["sections"]
        if item["slug"] != "hero"
    )
    rendered.append(
        f"""      <nav class="section vision-toc" aria-label="Vision sections">
        <p class="section-label">Sections</p>
        <div class="section-links">
{toc_links}
        </div>
      </nav>"""
    )

    for title, lines in sections:
        rendered.append(render_section(title, lines, data_sections))

    rendered.append(
        f"""      <section class="section vision-section" id="related-corpus-routes">
        <div class="section-head">
          <p class="section-label">Routes</p>
          <h2>Related corpus routes</h2>
        </div>
        <div class="section-links">
{render_link_lists()}
        </div>
      </section>"""
    )

    page_json = breadcrumb_json(data["metadata"]["title"])
    article_json = json.dumps(schema, ensure_ascii=False, indent=2)
    body = "\n\n".join(rendered)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(data["metadata"]["title"])} | Ivan Kotov</title>
  <meta name="description" content="{e(data["metadata"]["description"])}">
  <link rel="canonical" href="{CANONICAL_URL}">
  <meta property="og:title" content="{e(data["metadata"]["title"])} | Ivan Kotov">
  <meta property="og:description" content="{e(data["metadata"]["description"])}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{CANONICAL_URL}">
  <script type="application/ld+json">
{page_json}
  </script>
  <script type="application/ld+json">
{article_json}
  </script>
  <link rel="stylesheet" href="../styles.css">
</head>
<body class="vision-page">
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="site-shell">
    <header class="site-header">
      <a class="brand" href="../">
        <span class="brand-name">Ivan Kotov</span>
        <span class="brand-role">AI Systems Architect</span>
      </a>
      <nav class="site-nav" aria-label="Primary">
        {nav_html()}
      </nav>
    </header>

    <main id="main" tabindex="-1">
      <div class="breadcrumb"><a href="../">Home</a> / <span>Vision</span></div>
{body}
    </main>

    <footer class="site-footer">
      <p>Primary domain: <span>ivankotov.eu</span></p>
    </footer>
  </div>
</body>
</html>
"""


def render_index_json(data: dict, receipt: dict) -> dict:
    return {
        "schema_version": "vision-route-index-v0.1",
        "route": ROUTE,
        "canonical_url": CANONICAL_URL,
        "title": data["metadata"]["title"],
        "description": data["metadata"]["description"],
        "status": data["metadata"]["status"],
        "language": "en",
        "version": data["metadata"]["version"],
        "last_revised": data["metadata"]["last_revised"],
        "page_role": "living_authorial_vision",
        "source_boundary": data["metadata"]["source_boundary"],
        "derived_from": data["metadata"]["derived_from"],
        "source_zip_sha256": receipt["source_zip_sha256"],
        "public_entry_count": receipt["public_entry_count"],
        "mapped_entry_count": receipt["mapped_entry_count"],
        "internal_first_count": receipt["internal_first_count"],
        "sections": data["sections"],
        "deep_links": data["deep_links"]
        + [
            {"label": "Current state", "href": "/corpus/current-state/"},
            {"label": "Advanced Global Intelligence", "href": "/advanced-global-intelligence/"},
            {"label": "Distinctions", "href": "/distinctions/"},
            {"label": "Evidence", "href": "/evidence/"},
            {"label": "Corpus map", "href": "/corpus-map/"},
        ],
        "nonclaims": data["nonclaims"],
        "status_effect": "editorial_only",
        "status_note": EXPECTED_NONCLAIM_NOTE,
    }


def write_sitemap() -> None:
    sitemap_path = ROOT / "sitemap.xml"
    text = sitemap_path.read_text(encoding="utf-8")
    loc = f"  <url>\n    <loc>{CANONICAL_URL}</loc>\n  </url>\n"
    if f"<loc>{CANONICAL_URL}</loc>" in text:
        return
    anchor = "  <url>\n    <loc>https://ivankotov.eu/start-here/</loc>\n  </url>\n"
    if anchor not in text:
        raise RuntimeError("sitemap start-here anchor not found")
    text = text.replace(anchor, anchor + loc, 1)
    if f"<loc>{CANONICAL_URL}index.json</loc>" in text or f"<loc>{CANONICAL_URL}schemaorg.jsonld</loc>" in text:
        raise RuntimeError("Vision JSON endpoints must not be in sitemap")
    sitemap_path.write_text(text, encoding="utf-8")


def validate_rendered(html_text: str) -> None:
    if html_text.count('class="vision-diagram"') != 4:
        raise RuntimeError("Vision page must contain exactly four main diagrams")
    for link in REQUIRED_LINKS:
        if f'href="{link}"' not in html_text:
            raise RuntimeError(f"Vision page missing outbound link {link}")
    if "Vision Ledger" in html_text and "public-candidate entries only" not in html_text:
        raise RuntimeError("Vision Ledger mention must be public-candidate bounded")
    forbidden = [
        "Baseline B0 is revised",
        "Theoretical Core is revised",
        "proof of consciousness",
        "legal personhood is established",
        "validated entity classification",
    ]
    for phrase in forbidden:
        if phrase.lower() in html_text.lower():
            raise RuntimeError(f"forbidden Vision claim phrase: {phrase}")
    if '<meta name="robots" content="noindex' in html_text.lower():
        raise RuntimeError("Vision page must not be noindex")


def validate_outputs() -> None:
    html_text = (OUT_DIR / "index.html").read_text(encoding="utf-8")
    validate_rendered(html_text)
    json.loads((OUT_DIR / "index.json").read_text(encoding="utf-8"))
    json.loads((OUT_DIR / "schemaorg.jsonld").read_text(encoding="utf-8"))
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if sitemap.count(f"<loc>{CANONICAL_URL}</loc>") != 1:
        raise RuntimeError("sitemap must contain Vision exactly once")
    if "vision/index.json" in sitemap or "vision/schemaorg.jsonld" in sitemap:
        raise RuntimeError("sitemap must not contain Vision JSON endpoints")


def main() -> None:
    receipt, data, schema, section_map, copy = validate_sources()
    if not section_map:
        raise RuntimeError("Vision section map is empty")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    html_text = render_html(data, schema, copy)
    validate_rendered(html_text)
    (OUT_DIR / "index.html").write_text(html_text, encoding="utf-8")

    index_json = render_index_json(data, receipt)
    (OUT_DIR / "index.json").write_text(json.dumps(index_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    schema["mainEntityOfPage"] = CANONICAL_URL
    (OUT_DIR / "schemaorg.jsonld").write_text(json.dumps(schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    write_sitemap()
    validate_outputs()
    print("Vision v0.1 build complete")


if __name__ == "__main__":
    main()
