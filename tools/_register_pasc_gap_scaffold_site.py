from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ID = "pasc-f0-gap-closure-scaffold-v0-1-1"
URN = "urn:ivankotov:publication:pasc-f0-gap-closure-scaffold:v0.1.1"
PAGE = "https://ivankotov.eu/publications/pasc-f0-gap-closure-scaffold-v0-1-1/"
DOI = "10.5281/zenodo.21871392"
CONCEPT_DOI = "10.5281/zenodo.21871391"
RELATED_PASC_DOI = "10.5281/zenodo.21843823"
RELATED_PASC_CONCEPT_DOI = "10.5281/zenodo.21843822"
COMMIT = "2e4d3be735dffe20cac06e7e8f6f3b50b196481a"
PASC_COMMIT = "096a2ae2d84c5b6135e0c83f9c956ab98a802b42"
SOURCE = f"https://github.com/Kot141078/advanced-global-intelligence/tree/{COMMIT}/research/pasc/f0-gap-closure-scaffolds/v0.1.1"
RELEASE = "https://github.com/Kot141078/advanced-global-intelligence/releases/tag/pasc-f0-gap-closure-scaffold-v0.1.1"
ZENODO = "https://zenodo.org/records/21871392"
TITLE = "PASC F0 Gap-Closure Scaffold and Structural Templates"
SUMMARY = (
    "External analytical scaffold translating six open PASC Recovery Build 5 F0 criteria "
    "into a dependency-aware work programme for author acceptance, canonical sources and "
    "adapters, independent human review, blind field replay, protected-profile infrastructure "
    "and reserved-territory audit. Informative context only; F0 remains NOT_PASSED."
)
MARKER = "PASC_F0_GAP_CLOSURE_SCAFFOLD_V011"

PDF = {
    "format": "PDF",
    "filename": "PASC_F0_GAP_CLOSURE_SCAFFOLD_v0_1_1.pdf",
    "media_type": "application/pdf",
    "sha256": "b886090c2e55f49ad1fb1efc8135621bc7144c8e6801c660ef1c356e58278fb9",
    "url": ZENODO + "/files/PASC_F0_GAP_CLOSURE_SCAFFOLD_v0_1_1.pdf?download=1",
}
MD = {
    "format": "Markdown",
    "filename": "PASC_F0_GAP_CLOSURE_SCAFFOLD_v0_1_1.md",
    "media_type": "text/markdown",
    "sha256": "7fbe84fd1aa6571347076239aaf0667242e3c9097dfc2c816626c8717137e427",
    "url": ZENODO + "/files/PASC_F0_GAP_CLOSURE_SCAFFOLD_v0_1_1.md?download=1",
}
PUBJSON = {
    "format": "JSON",
    "filename": "PASC_F0_GAP_CLOSURE_SCAFFOLD_v0_1_1_PUBLICATION_RECORD.json",
    "media_type": "application/json",
    "sha256": "54ec921bf6ee140ce4e2e973a78d1f45674159f7866938d3035053f48d7c2a5a",
    "url": ZENODO + "/files/PASC_F0_GAP_CLOSURE_SCAFFOLD_v0_1_1_PUBLICATION_RECORD.json?download=1",
}
LEDGER = {
    "format": "TXT",
    "filename": "PASC_F0_GAP_CLOSURE_SCAFFOLD_v0_1_1_SHA256SUMS.txt",
    "media_type": "text/plain",
    "sha256": "a7f5c47935cb8df52a4fed2ab8dcabf2682b5e4d62ead364f8a890160345d760",
    "url": ZENODO + "/files/PASC_F0_GAP_CLOSURE_SCAFFOLD_v0_1_1_SHA256SUMS.txt?download=1",
}


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path: str, value) -> None:
    (ROOT / path).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def prepend_unique(records, record, key: str, value: str) -> None:
    records[:] = [item for item in records if item.get(key) != value]
    records.insert(0, record)


def insert_once(path: str, identity: str, marker: str, block: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if identity in text:
        return
    if marker not in text:
        raise SystemExit(f"marker not found in {path}: {marker!r}")
    target.write_text(text.replace(marker, block + marker, 1), encoding="utf-8", newline="\n")


works = load("works-index.json")
prepend_unique(
    works["works"],
    {
        "id": ID,
        "title": TITLE,
        "type": "publication",
        "subtype": "technical_note",
        "role": "external analytical scaffold for six open PASC F0 criteria",
        "primary_url": PAGE,
        "identifier": URN,
        "doi": DOI,
        "doi_url": f"https://doi.org/{DOI}",
        "version_doi": DOI,
        "concept_doi": CONCEPT_DOI,
        "concept_doi_url": f"https://doi.org/{CONCEPT_DOI}",
        "zenodo_record": ZENODO,
        "github": SOURCE,
        "github_release_url": RELEASE,
        "release_tag": "pasc-f0-gap-closure-scaffold-v0.1.1",
        "commit": COMMIT,
        "commit_url": f"https://github.com/Kot141078/advanced-global-intelligence/commit/{COMMIT}",
        "date": "2026-08-10",
        "version": "v0.1.1",
        "status": "published-informative-context-f0-not-passed",
        "languages": ["en"],
        "resource_type": "Technical note",
        "license": "CC BY-NC-ND 4.0",
        "summary": SUMMARY,
        "responsible_editor": {
            "name": "Ivan Kotov",
            "role": "Editor",
            "orcid": "0009-0009-6002-9845",
        },
        "ai_provenance": [
            {"system": "Kimi AI", "provider": "Moonshot AI", "role": "original analytical draft"},
            {"system": "OpenAI GPT-5.6 Pro", "provider": "OpenAI", "role": "analytical revision and normalization"},
        ],
        "related_work": {"relation": "IsSupplementTo", "doi": RELATED_PASC_DOI},
        "sha256": PDF["sha256"],
        "checksums_url": PAGE + "files/machine/checksums.json",
        "machine_index_url": PAGE + "files/machine/index.json",
        "non_claims": [
            "PASC F0 passage",
            "independent human review",
            "signed Recovery 5 author acceptance",
            "canonical baseline closure",
            "reserved-territory compatibility closure",
            "field maturation closure",
            "competent-jurisdiction protected-profile closure",
            "succession, identity, continuity or authority establishment",
            "formalization, validator, implementation or deployment authorization",
        ],
        "canonical_artifacts": [
            PDF,
            MD,
            PUBJSON,
            LEDGER,
            {
                "format": "JSON",
                "filename": "files/machine/index.json",
                "media_type": "application/json",
                "url": PAGE + "files/machine/index.json",
            },
        ],
    },
    "id",
    ID,
)
save("works-index.json", works)

library = load("library-index.json")
prepend_unique(
    library["items"],
    {
        "id": ID,
        "title": TITLE,
        "role": "technical note / PASC F0 gap-closure scaffold / informative context",
        "primary_page": PAGE,
        "repo_url": "https://github.com/Kot141078/advanced-global-intelligence",
        "release_url": RELEASE,
        "commit_url": f"https://github.com/Kot141078/advanced-global-intelligence/commit/{COMMIT}",
        "type": "publication",
        "subtype": "technical_note",
        "doi": DOI,
        "doi_url": f"https://doi.org/{DOI}",
        "concept_doi": CONCEPT_DOI,
        "concept_doi_url": f"https://doi.org/{CONCEPT_DOI}",
        "zenodo_record": ZENODO,
        "zenodo_status": "published",
        "version": "v0.1.1",
        "date": "2026-08-10",
        "author": "Ivan Kotov (Responsible Editor)",
        "orcid": "0009-0009-6002-9845",
        "languages": ["English"],
        "license": "CC BY-NC-ND 4.0",
        "summary": SUMMARY,
        "related_work": {"relation": "IsSupplementTo", "doi": RELATED_PASC_DOI},
        "artifacts": [
            {"language": "English", **PDF},
            {"language": "English", **MD},
            {"language": "English", **PUBJSON},
            {"language": "English", **LEDGER},
        ],
        "machine_index_url": PAGE + "files/machine/index.json",
        "not": [
            "PASC closure evidence",
            "independent human review",
            "competent-jurisdiction authority",
            "formalization, implementation or deployment authorization",
        ],
    },
    "id",
    ID,
)
save("library-index.json", library)

downloads = load("downloads-index.json")
downloads["items"] = [item for item in downloads["items"] if item.get("publication_id") != ID]
new_downloads = [
    {"publication_id": ID, "object": TITLE, "surface": "Website publication page", "format": "website page", "language": "English", "url": PAGE, "note": "Detailed human and machine entry with role, six open criteria, work order, direct downloads, provenance and claim ceiling."},
    {"publication_id": ID, "object": TITLE, "surface": "Version DOI", "format": "DOI / persistent identifier", "language": "English", "url": f"https://doi.org/{DOI}", "doi_identifier": DOI, "note": "Exact v0.1.1 publication record."},
    {"publication_id": ID, "object": TITLE, "surface": "Concept DOI", "format": "DOI / version-family navigation", "language": "English", "url": f"https://doi.org/{CONCEPT_DOI}", "concept_doi_identifier": CONCEPT_DOI, "note": "Persistent identifier for all versions of the scaffold."},
    {"publication_id": ID, "object": TITLE, "surface": "Related PASC Recovery Build 5 DOI", "format": "DOI / IsSupplementTo relation", "language": "English", "url": f"https://doi.org/{RELATED_PASC_DOI}", "doi_identifier": RELATED_PASC_DOI, "note": "The scaffold analyzes and supplements this exact PASC version without becoming part of or modifying it."},
    {"publication_id": ID, "object": TITLE, "surface": "Primary PDF", "format": "PDF", "language": "English", "url": PDF["url"], "sha256": PDF["sha256"], "note": "28-page human-readable technical note."},
    {"publication_id": ID, "object": TITLE, "surface": "Canonical Markdown", "format": "Markdown", "language": "English", "url": MD["url"], "sha256": MD["sha256"], "note": "UTF-8 source of record."},
    {"publication_id": ID, "object": TITLE, "surface": "Publication record", "format": "JSON", "language": "English", "url": PUBJSON["url"], "sha256": PUBJSON["sha256"], "note": "Structured identity, provenance, relation, metadata and claim ceiling."},
    {"publication_id": ID, "object": TITLE, "surface": "Checksum ledger", "format": "TXT / SHA-256", "language": "English", "url": LEDGER["url"], "sha256": LEDGER["sha256"], "note": "Covers PDF, Markdown and publication JSON; excludes itself to avoid self-reference."},
    {"publication_id": ID, "object": TITLE, "surface": "GitHub source mirror", "format": "human- and machine-readable repository path", "language": "English", "url": SOURCE, "note": "Commit-pinned scientific corpus entry."},
    {"publication_id": ID, "object": TITLE, "surface": "GitHub Release mirror", "format": "release assets", "language": "English", "url": RELEASE, "note": "SHA-256-verified mirror of all four Zenodo files."},
    {"publication_id": ID, "object": TITLE, "surface": "Machine index", "format": "JSON", "language": "English", "url": PAGE + "files/machine/index.json", "note": "Typed identity, relationship, open criteria, nonclaims, downloads, source authority and parser guard."},
]
downloads["items"] = new_downloads + downloads["items"]
save("downloads-index.json", downloads)

canonical = load("canonical-map.json")
canonical["pasc_f0_gap_closure_scaffold_v0_1_1_url"] = PAGE
canonical["nodes"] = [node for node in canonical["nodes"] if node.get("id") != ID]
canonical["nodes"].append(
    {
        "id": ID,
        "title": TITLE,
        "url": PAGE,
        "version": "v0.1.1",
        "doi": f"https://doi.org/{DOI}",
        "relation": {"type": "IsSupplementTo", "target_doi": RELATED_PASC_DOI},
        "summary": SUMMARY,
        "not": [
            "part of or modification to Recovery Build 5",
            "PASC normative input or closure evidence",
            "independent human review",
            "competent-jurisdiction authority",
            "F0 passage",
            "formalization, validator, implementation or deployment authorization",
        ],
    }
)
save("canonical-map.json", canonical)

pasc_machine_path = ROOT / "publications/pasc-foundation-gate-v0-1-1/files/machine/index.json"
pasc_machine = json.loads(pasc_machine_path.read_text(encoding="utf-8"))
pasc_machine["related_publications"] = [
    item
    for item in pasc_machine.get("related_publications", [])
    if item.get("record_id") != URN
]
pasc_machine["related_publications"].append(
    {
        "relation": "HasSupplement",
        "record_id": URN,
        "title": TITLE,
        "version_doi": DOI,
        "web_page": PAGE,
        "status": "INFORMATIVE_CONTEXT",
        "normative_weight_in_pasc": False,
        "closure_evidence": False,
        "modifies_recovery_5": False,
    }
)
pasc_machine_path.write_text(
    json.dumps(pasc_machine, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)

publication_card = f'''<!-- {MARKER} -->
          <article class="card">
            <p class="eyebrow">DOI-backed technical note · informative context</p>
            <h3>{TITLE}</h3>
            <p>Dependency-aware structural templates for the six Recovery Build 5 F0 criteria that remain open: author acceptance, canonical sources and adapters, reserved-territory audit, independent human review, field maturation and protected-profile closure.</p>
            <p class="status-note">Published 2026-08-10. Version DOI <a href="https://doi.org/{DOI}">{DOI}</a>. <code>normative_weight_in_pasc=false</code>; <code>closure_evidence=false</code>; F0 remains <code>NOT_PASSED</code>.</p>
            <div class="section-links"><a href="./pasc-f0-gap-closure-scaffold-v0-1-1/">Detailed site page</a><a href="https://doi.org/{DOI}">Version DOI</a><a href="{ZENODO}">Zenodo</a><a href="{SOURCE}">Source mirror</a><a href="{RELEASE}">Release</a><a href="./pasc-f0-gap-closure-scaffold-v0-1-1/files/machine/index.json">Machine index</a></div>
          </article>
'''
insert_once("publications/index.html", MARKER, '          <article class="card">', publication_card)

library_section = f'''<!-- {MARKER} -->
      <section class="section" id="pasc-f0-gap-closure-scaffold-v0-1-1">
        <div class="section-head"><p class="section-label">New DOI-backed technical note</p><h2>PASC F0 Gap-Closure Scaffold v0.1.1</h2></div>
        <div class="card-grid"><article class="card"><p class="eyebrow">technical note · informative context · English</p><h3>{TITLE}</h3><p>Structural templates and a dependency-aware work programme for six open PASC F0 criteria. No normative weight, closure evidence, F0 passage or implementation authorization.</p><div class="section-links"><a href="../publications/pasc-f0-gap-closure-scaffold-v0-1-1/">Detailed page</a><a href="https://doi.org/{DOI}">DOI</a><a href="{SOURCE}">Source</a><a href="../publications/pasc-f0-gap-closure-scaffold-v0-1-1/files/machine/index.json">Machine index</a></div></article></div>
      </section>

'''
insert_once("library/index.html", MARKER, '      <section class="section" id="world-intelligence">', library_section)

download_section = f'''<!-- {MARKER} -->
      <section class="section" id="pasc-f0-gap-closure-scaffold-v0-1-1">
        <div class="section-head"><p class="section-label">New DOI-backed technical note</p><h2>PASC F0 Gap-Closure Scaffold v0.1.1</h2></div>
        <div class="prose"><p>Direct immutable downloads from Zenodo. The Markdown is the textual source of record; the PDF is a human-readable rendering. The work is informative context only and leaves PASC F0 <code>NOT_PASSED</code>.</p></div>
        <div class="section-links"><a href="{PDF['url']}" type="application/pdf">Primary PDF</a><a href="{MD['url']}" type="text/markdown">Canonical Markdown</a><a href="{PUBJSON['url']}" type="application/json">Publication JSON</a><a href="{LEDGER['url']}" type="text/plain">SHA-256 ledger</a><a href="../publications/pasc-f0-gap-closure-scaffold-v0-1-1/">Publication page</a></div>
      </section>

'''
insert_once("downloads/index.html", MARKER, '      <section class="section" id="world-intelligence">', download_section)

pasc_page = ROOT / "publications/pasc-foundation-gate-v0-1-1/index.html"
pasc_html = pasc_page.read_text(encoding="utf-8")
if "PASC_F0_GAP_CLOSURE_SCAFFOLD_RELATED" not in pasc_html:
    pasc_html = pasc_html.replace(
        '<a href="#cite">Citation</a>',
        '<a href="#related-scaffold">Related scaffold</a><a href="#cite">Citation</a>',
        1,
    )
    related_section = f'''        <!-- PASC_F0_GAP_CLOSURE_SCAFFOLD_RELATED -->
        <section class="chapter" id="related-scaffold">
          <p class="section-label">Post-publication analytical scaffold</p><h2>How the six open F0 gaps can be approached</h2>
          <p class="intro">A separate DOI-bound technical note translates the six <code>NOT_SATISFIED</code> criteria into a dependency-aware work programme and structural templates. It is informative context only: it does not modify Recovery 5, supply closure evidence, or change the gate status above.</p>
          <div class="grid"><div class="card"><h3>Human entry</h3><p><a href="../pasc-f0-gap-closure-scaffold-v0-1-1/">Read the detailed scaffold guide</a> for the work order, template boundaries, blind replay protocol, protected-profile posture, downloads and provenance.</p></div><div class="card"><h3>Persistent identity</h3><p><a href="https://doi.org/{DOI}">Version DOI {DOI}</a><br>Relation: <code>IsSupplementTo</code> this exact Recovery Build 5 publication.<br>Status: <code>INFORMATIVE_CONTEXT</code>.</p></div></div>
        </section>
'''
    cite_marker = '        <section class="chapter" id="cite">'
    if cite_marker not in pasc_html:
        raise SystemExit("PASC citation section marker not found")
    pasc_html = pasc_html.replace(cite_marker, related_section + cite_marker, 1)
    pasc_page.write_text(pasc_html, encoding="utf-8", newline="\n")

sitemap = ROOT / "sitemap.xml"
sitemap_text = sitemap.read_text(encoding="utf-8")
if PAGE not in sitemap_text:
    sitemap_text = sitemap_text.replace(
        "</urlset>",
        f"  <url>\n    <loc>{PAGE}</loc>\n    <lastmod>2026-08-10</lastmod>\n  </url>\n</urlset>",
    )
    sitemap.write_text(sitemap_text, encoding="utf-8", newline="\n")

llms = ROOT / "llms.txt"
llms_text = llms.read_text(encoding="utf-8")
if "PASC F0 Gap-Closure Scaffold v0.1.1" not in llms_text:
    llms_text += (
        "\n## PASC F0 Gap-Closure Scaffold v0.1.1\n"
        f"- Human page: {PAGE}\n"
        f"- Machine index: {PAGE}files/machine/index.json\n"
        f"- Version DOI: https://doi.org/{DOI}\n"
        f"- Concept DOI: https://doi.org/{CONCEPT_DOI}\n"
        f"- Is supplement to: https://doi.org/{RELATED_PASC_DOI}\n"
        f"- Source mirror: {SOURCE}\n"
        "- Status: INFORMATIVE_CONTEXT; normative_weight_in_pasc=false; closure_evidence=false; F0_OUTCOME remains NOT_PASSED; F1 drafting, formalization, validator construction, implementation and deployment are prohibited.\n"
        "- Parser guard: publication, DOI, templates, checksums, signatures, credentials, receipts, profiles, registries or technical capability do not create PASC closure, independence, jurisdiction, succession, identity, continuity or authority.\n"
    )
    llms.write_text(llms_text, encoding="utf-8", newline="\n")
