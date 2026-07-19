#!/usr/bin/env python3
"""Finalize ESTHER-RP-001 v0.8.1 in the site's shared public indexes."""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

DOI = "10.5281/zenodo.21443105"
CONCEPT_DOI = "10.5281/zenodo.21443104"
PAGE = "https://ivankotov.eu/publications/esther-rp-001/"
ZENODO = "https://zenodo.org/records/21443105"
REPO = "https://github.com/Kot141078/ester-theoretical-core"
RELEASE = "https://github.com/Kot141078/ester-theoretical-core/releases/tag/esther-rp-001-v0.8.1"
ARCHIVE = "ESTHER_RP001_v0_8_1_ENGLISH_DOI_RELEASE_2026-07-19.zip"
SHA256 = "83e71e2fab938e3110293a61967a85440969d8d7eb78a69bf4c1ae40afd4a9d7"


def update_publications_html() -> None:
    path = Path("publications/index.html")
    text = path.read_text(encoding="utf-8")

    script_match = re.search(
        r'(<script type="application/ld\+json">\s*)(.*?)(\s*</script>)',
        text,
        re.S,
    )
    if script_match is None:
        raise RuntimeError("JSON-LD block not found in publications/index.html")

    data = json.loads(script_match.group(2))
    item_list = next(node for node in data["@graph"] if node.get("@type") == "ItemList")
    entries = item_list["itemListElement"]
    already_indexed = any(
        entry.get("item", {}).get("identifier") in {DOI, f"https://doi.org/{DOI}"}
        for entry in entries
    )
    if not already_indexed:
        entries.append(
            {
                "@type": "ListItem",
                "position": max(entry.get("position", 0) for entry in entries) + 1,
                "item": {
                    "@type": "ScholarlyArticle",
                    "name": "ESTHER-RP-001 v0.8.1: Centered Agency Under Persistent Uncertainty",
                    "url": PAGE,
                    "sameAs": [f"https://doi.org/{DOI}", ZENODO, REPO, RELEASE],
                    "identifier": f"https://doi.org/{DOI}",
                    "datePublished": "2026-07-19",
                    "version": "0.8.1",
                    "inLanguage": "en",
                    "description": (
                        "English DOI-bound working paper and bounded executable review package "
                        "on causal memory, selective operational commitment, temporal witness, "
                        "obligation continuity, and auditable substrate interaction."
                    ),
                },
            }
        )
        rendered = json.dumps(data, ensure_ascii=False, indent=2)
        text = text[: script_match.start(2)] + rendered + text[script_match.end(2) :]

    card_marker = "<!-- esther-rp-001-v0.8.1:card -->"
    if card_marker not in text:
        grid_marker = '<div class="card-grid">'
        insertion = text.find(grid_marker)
        if insertion < 0:
            raise RuntimeError("First publication card grid not found")
        insertion += len(grid_marker)
        card = f'''
          {card_marker}
          <article class="card">
            <p class="eyebrow">DOI-backed working paper / bounded executable review package</p>
            <h3>ESTHER-RP-001 v0.8.1</h3>
            <p><strong>Centered Agency Under Persistent Uncertainty.</strong> Causal memory, selective operational commitment, temporal witness, obligation continuity, auditable substrate interaction, and a falsifiable matched-control programme.</p>
            <p class="status-note">Published <code>2026-07-19</code>. Version DOI: <a href="https://doi.org/{DOI}">{DOI}</a>. Concept DOI: <a href="https://doi.org/{CONCEPT_DOI}">{CONCEPT_DOI}</a>. Independent Windows reproduction: PASS. Sixth blind conceptual review: <code>NO_CANDIDATE_BLOCKERS_FOUND</code>. This is not human peer review and does not establish consciousness, personhood, AGI, empirical continuity, production security, or quantum necessity.</p>
            <div class="section-links">
              <a href="./esther-rp-001/">Site page</a>
              <a href="https://doi.org/{DOI}">DOI</a>
              <a href="{ZENODO}">Zenodo record</a>
              <a href="{REPO}">GitHub repository</a>
              <a href="{RELEASE}">GitHub release</a>
            </div>
          </article>
'''
        text = text[:insertion] + card + text[insertion:]

    path.write_text(text, encoding="utf-8")


def update_works_index() -> None:
    path = Path("works-index.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not any(item.get("id") == "esther-rp-001-v0-8-1" for item in data["works"]):
        data["works"].insert(
            0,
            {
                "id": "esther-rp-001-v0-8-1",
                "title": "ESTHER-RP-001 v0.8.1: Centered Agency Under Persistent Uncertainty",
                "type": "working paper and bounded executable research package",
                "role": "causal memory / selective operational commitment / open external review",
                "primary_url": PAGE,
                "doi": DOI,
                "doi_url": f"https://doi.org/{DOI}",
                "concept_doi": CONCEPT_DOI,
                "concept_doi_url": f"https://doi.org/{CONCEPT_DOI}",
                "zenodo_record": ZENODO,
                "github": REPO,
                "release": RELEASE,
                "date": "2026-07-19",
                "version": "0.8.1",
                "language": "en",
                "archive": ARCHIVE,
                "archive_sha256": SHA256,
                "status": "published; human conceptual review and endpoint-rater pilot open",
                "license_docs": "CC BY 4.0",
                "license_code": "MIT",
            },
        )
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_llms() -> None:
    path = Path("llms.txt")
    text = path.read_text(encoding="utf-8")
    line = (
        f"- ESTHER-RP-001 v0.8.1: {PAGE} — DOI https://doi.org/{DOI} — "
        f"Zenodo {ZENODO} — GitHub release {RELEASE} — English DOI-bound working "
        "paper and bounded executable review package; Windows reproduction PASS; "
        "sixth blind conceptual review found no candidate blockers; human review remains open."
    )
    if line not in text:
        marker = "Public works and evidence:\n"
        if marker not in text:
            raise RuntimeError("llms.txt public works marker not found")
        text = text.replace(marker, marker + line + "\n", 1)
    path.write_text(text, encoding="utf-8")


def update_sitemap() -> None:
    path = Path("sitemap.xml")
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", namespace)
    tree = ET.parse(path)
    root = tree.getroot()
    locs = {node.text for node in root.findall(f"{{{namespace}}}url/{{{namespace}}}loc")}
    if PAGE not in locs:
        url = ET.SubElement(root, f"{{{namespace}}}url")
        ET.SubElement(url, f"{{{namespace}}}loc").text = PAGE
        ET.SubElement(url, f"{{{namespace}}}lastmod").text = "2026-07-19"
    tree.write(path, encoding="UTF-8", xml_declaration=True)


def main() -> None:
    update_publications_html()
    update_works_index()
    update_llms()
    update_sitemap()
    print("ESTHER-RP-001 shared indexes finalized")


if __name__ == "__main__":
    main()
