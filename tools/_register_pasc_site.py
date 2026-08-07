from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ID = "pasc-foundation-gate-v0-1-1-recovery-5"
PAGE = "https://ivankotov.eu/publications/pasc-foundation-gate-v0-1-1/"
DOI = "10.5281/zenodo.21843823"
CONCEPT_DOI = "10.5281/zenodo.21843822"
COMMIT = "096a2ae2d84c5b6135e0c83f9c956ab98a802b42"
SOURCE = f"https://github.com/Kot141078/advanced-global-intelligence/tree/{COMMIT}/official/pasc/foundation-gate/v0.1.1-recovery.5"
RELEASE = "https://github.com/Kot141078/advanced-global-intelligence/releases/tag/pasc-foundation-gate-v0.1.1-recovery.5"
ZENODO = "https://zenodo.org/records/21843823"
TITLE = "Post-Anchor Succession and Custody (PASC): Foundation Gate v0.1.1"
SUMMARY = "Negative-only foundation gate for exact post-anchor risk reduction, preservation and revocation without manufacturing successor identity, continuity, custody, keyholding, provider/jurisdiction authority, recovery roots, release, reactivation or Runtime Authority."


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path: str, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prepend_unique(records, record, key, value):
    records[:] = [item for item in records if item.get(key) != value]
    records.insert(0, record)


works = load("works-index.json")
prepend_unique(works["works"], {
    "id": ID,
    "title": TITLE,
    "type": "publication",
    "subtype": "technical_note",
    "role": "negative-only post-anchor admissibility foundation gate",
    "primary_url": PAGE,
    "identifier": "urn:ivankotov:publication:pasc-foundation-gate:v0.1.1-recovery.5",
    "doi": DOI,
    "doi_url": f"https://doi.org/{DOI}",
    "version_doi": DOI,
    "concept_doi": CONCEPT_DOI,
    "concept_doi_url": f"https://doi.org/{CONCEPT_DOI}",
    "zenodo_record": ZENODO,
    "github": SOURCE,
    "github_release_url": RELEASE,
    "release_tag": "pasc-foundation-gate-v0.1.1-recovery.5",
    "commit": COMMIT,
    "commit_url": f"https://github.com/Kot141078/advanced-global-intelligence/commit/{COMMIT}",
    "date": "2026-08-07",
    "version": "v0.1.1-recovery.5",
    "status": "published-research-candidate-f0-not-passed",
    "languages": ["en"],
    "resource_type": "Technical note",
    "license": "CC BY-NC-ND 4.0",
    "summary": SUMMARY,
    "archive_sha256": "640f2a66109cad6105fd22f33d76e0c062bede01a40474d408dbe601ec4c1888",
    "sha256": "ca0b1920b72ca59d9cf569b816091a3e70093fc52497d3557834ee070a198acf",
    "checksums_url": PAGE + "files/machine/checksums.json",
    "machine_index_url": PAGE + "files/machine/index.json",
    "non_claims": [
        "F0 passage",
        "locked foundation semantics",
        "conformance certification",
        "legal advice or legal succession",
        "identity or continuity establishment",
        "custody, keyholding, provider or jurisdiction authority",
        "recovery root, release, reactivation or Runtime Authority",
        "formalization, validator, implementation or deployment authorization"
    ],
    "canonical_artifacts": [
        {"format": "PDF", "filename": "PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.pdf", "media_type": "application/pdf", "sha256": "ca0b1920b72ca59d9cf569b816091a3e70093fc52497d3557834ee070a198acf", "url": ZENODO + "/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.pdf?download=1"},
        {"format": "PDF", "filename": "PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.pdf", "media_type": "application/pdf", "sha256": "ef3e3d7ad4f96222fb1d9ff928957cdcc0e269d8168fb966433c942d9fcdb151", "url": ZENODO + "/files/PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.pdf?download=1"},
        {"format": "ZIP", "filename": "PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.zip", "media_type": "application/zip", "sha256": "640f2a66109cad6105fd22f33d76e0c062bede01a40474d408dbe601ec4c1888", "url": ZENODO + "/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.zip?download=1"},
        {"format": "JSON", "filename": "files/machine/index.json", "media_type": "application/json", "url": PAGE + "files/machine/index.json"}
    ]
}, "id", ID)
save("works-index.json", works)

library = load("library-index.json")
prepend_unique(library["items"], {
    "id": ID,
    "title": TITLE,
    "role": "technical note / post-anchor governance / negative-only authority",
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
    "version": "v0.1.1-recovery.5",
    "date": "2026-08-07",
    "author": "Ivan Kotov",
    "orcid": "0009-0009-6002-9845",
    "languages": ["English"],
    "license": "CC BY-NC-ND 4.0",
    "summary": SUMMARY,
    "artifacts": [
        {"language": "English", "format": "PDF", "filename": "PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.pdf", "media_type": "application/pdf", "sha256": "ca0b1920b72ca59d9cf569b816091a3e70093fc52497d3557834ee070a198acf", "url": ZENODO + "/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.pdf?download=1"},
        {"language": "English", "format": "PDF supplement", "filename": "PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.pdf", "media_type": "application/pdf", "sha256": "ef3e3d7ad4f96222fb1d9ff928957cdcc0e269d8168fb966433c942d9fcdb151", "url": ZENODO + "/files/PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.pdf?download=1"},
        {"language": "English", "format": "ZIP", "filename": "PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.zip", "media_type": "application/zip", "sha256": "640f2a66109cad6105fd22f33d76e0c062bede01a40474d408dbe601ec4c1888", "url": ZENODO + "/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.zip?download=1"}
    ],
    "machine_index_url": PAGE + "files/machine/index.json"
}, "id", ID)
save("library-index.json", library)

downloads = load("downloads-index.json")
downloads["items"] = [item for item in downloads["items"] if item.get("publication_id") != ID]
new_downloads = [
    {"publication_id": ID, "object": TITLE, "surface": "Website publication page", "format": "website page", "language": "English", "url": PAGE, "note": "Detailed human and machine entry with reading order, status, direct downloads and source authority."},
    {"publication_id": ID, "object": TITLE, "surface": "Version DOI", "format": "DOI / persistent identifier", "language": "English", "url": f"https://doi.org/{DOI}", "doi_identifier": DOI, "note": "Exact Recovery Build 5 publication record."},
    {"publication_id": ID, "object": TITLE, "surface": "Concept DOI", "format": "DOI / version-family navigation", "language": "English", "url": f"https://doi.org/{CONCEPT_DOI}", "concept_doi_identifier": CONCEPT_DOI, "note": "Persistent identifier for all versions."},
    {"publication_id": ID, "object": TITLE, "surface": "Primary PDF", "format": "PDF", "language": "English", "url": ZENODO + "/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.pdf?download=1", "sha256": "ca0b1920b72ca59d9cf569b816091a3e70093fc52497d3557834ee070a198acf", "note": "83-page integrated report."},
    {"publication_id": ID, "object": TITLE, "surface": "Inventory supplement", "format": "PDF", "language": "English", "url": ZENODO + "/files/PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.pdf?download=1", "sha256": "ef3e3d7ad4f96222fb1d9ff928957cdcc0e269d8168fb966433c942d9fcdb151", "note": "61-page canonical baseline inventory supplement."},
    {"publication_id": ID, "object": TITLE, "surface": "Canonical source archive", "format": "ZIP", "language": "English", "url": ZENODO + "/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.zip?download=1", "sha256": "640f2a66109cad6105fd22f33d76e0c062bede01a40474d408dbe601ec4c1888", "note": "Source-of-record Markdown/JSON and release controls."},
    {"publication_id": ID, "object": TITLE, "surface": "GitHub source mirror", "format": "human- and machine-readable repository path", "language": "English", "url": SOURCE, "note": "Commit-pinned verified text/JSON mirror."},
    {"publication_id": ID, "object": TITLE, "surface": "GitHub Release mirror", "format": "release assets", "language": "English", "url": RELEASE, "note": "SHA-256-verified mirror of the four Zenodo files."},
    {"publication_id": ID, "object": TITLE, "surface": "Machine index", "format": "JSON", "language": "English", "url": PAGE + "files/machine/index.json", "note": "Typed entry, claim ceiling, status, downloads, source order and parser guard."}
]
downloads["items"] = new_downloads + downloads["items"]
save("downloads-index.json", downloads)

canonical = load("canonical-map.json")
canonical["pasc_foundation_gate_v0_1_1_url"] = PAGE
canonical["nodes"] = [node for node in canonical["nodes"] if node.get("id") != "pasc-foundation-gate-v0-1-1"]
canonical["nodes"].append({
    "id": "pasc-foundation-gate-v0-1-1",
    "title": "Post-Anchor Succession and Custody (PASC): Foundation Gate v0.1.1",
    "url": PAGE,
    "version": "v0.1.1-recovery.5",
    "summary": SUMMARY,
    "not": ["succession grant", "identity or continuity establishment", "custody transfer", "implementation specification", "deployment authorization", "F0 passage"]
})
save("canonical-map.json", canonical)

pub_card = '''<!-- PASC_FOUNDATION_GATE_R5 -->
          <article class="card">
            <p class="eyebrow">DOI-backed technical research candidate</p>
            <h3>Post-Anchor Succession and Custody (PASC): Foundation Gate v0.1.1</h3>
            <p>Negative-only foundation gate for exact post-anchor preservation, reduction and revocation without manufacturing successor authority.</p>
            <p class="status-note">Published 2026-08-07. Version DOI <a href="https://doi.org/10.5281/zenodo.21843823">10.5281/zenodo.21843823</a>. <code>F0_OUTCOME=NOT_PASSED</code>; foundation semantics are not locked; implementation and deployment remain prohibited.</p>
            <div class="section-links"><a href="./pasc-foundation-gate-v0-1-1/">Detailed site page</a><a href="https://doi.org/10.5281/zenodo.21843823">Version DOI</a><a href="https://zenodo.org/records/21843823">Zenodo</a><a href="https://github.com/Kot141078/advanced-global-intelligence/tree/096a2ae2d84c5b6135e0c83f9c956ab98a802b42/official/pasc/foundation-gate/v0.1.1-recovery.5">Source mirror</a><a href="https://github.com/Kot141078/advanced-global-intelligence/releases/tag/pasc-foundation-gate-v0.1.1-recovery.5">Release</a><a href="./pasc-foundation-gate-v0-1-1/files/machine/index.json">Machine index</a></div>
          </article>
'''
lib_section = '''<!-- PASC_FOUNDATION_GATE_R5 -->
      <section class="section" id="pasc-foundation-gate-v0-1-1">
        <div class="section-head"><p class="section-label">New technical research publication</p><h2>PASC Foundation Gate v0.1.1</h2></div>
        <div class="card-grid"><article class="card"><p class="eyebrow">technical note · v0.1.1-recovery.5 · English</p><h3>Post-Anchor Succession and Custody</h3><p>Human and machine entry to the negative-only foundation gate, including exact status, ordered sources, direct downloads and verification.</p><div class="section-links"><a href="../publications/pasc-foundation-gate-v0-1-1/">Detailed page</a><a href="https://doi.org/10.5281/zenodo.21843823">DOI</a><a href="https://github.com/Kot141078/advanced-global-intelligence/tree/096a2ae2d84c5b6135e0c83f9c956ab98a802b42/official/pasc/foundation-gate/v0.1.1-recovery.5">Source</a><a href="../publications/pasc-foundation-gate-v0-1-1/files/machine/index.json">Machine index</a></div></article></div>
      </section>

'''
download_section = '''<!-- PASC_FOUNDATION_GATE_R5 -->
      <section class="section" id="pasc-foundation-gate-v0-1-1">
        <div class="section-head"><p class="section-label">New DOI-backed technical note</p><h2>PASC Foundation Gate v0.1.1 — Recovery Build 5</h2></div>
        <div class="prose"><p>Direct immutable downloads from Zenodo. The canonical ZIP SHA-256 is <code>640f2a66109cad6105fd22f33d76e0c062bede01a40474d408dbe601ec4c1888</code>.</p></div>
        <div class="section-links"><a href="https://zenodo.org/records/21843823/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.pdf?download=1" type="application/pdf">Primary PDF</a><a href="https://zenodo.org/records/21843823/files/PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.pdf?download=1" type="application/pdf">Inventory supplement</a><a href="https://zenodo.org/records/21843823/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.zip?download=1" type="application/zip">Canonical ZIP</a><a href="https://zenodo.org/records/21843823/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5_EXTERNAL_SHA256SUMS.txt?download=1" type="text/plain">SHA-256 ledger</a><a href="../publications/pasc-foundation-gate-v0-1-1/">Publication page</a></div>
      </section>

'''

def insert(path, identity, marker, block):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if identity not in text:
        if marker not in text:
            raise SystemExit(f"marker not found in {path}: {marker}")
        text = text.replace(marker, block + marker, 1)
        p.write_text(text, encoding="utf-8")

insert("publications/index.html", "PASC_FOUNDATION_GATE_R5", '          <article class="card">', pub_card)
insert("library/index.html", "PASC_FOUNDATION_GATE_R5", '      <section class="section" id="world-intelligence">', lib_section)
insert("downloads/index.html", "PASC_FOUNDATION_GATE_R5", '      <section class="section" id="world-intelligence">', download_section)

sitemap = ROOT / "sitemap.xml"
text = sitemap.read_text(encoding="utf-8")
if PAGE not in text:
    text = text.replace("</urlset>", "  <url>\n    <loc>" + PAGE + "</loc>\n    <lastmod>2026-08-07</lastmod>\n  </url>\n</urlset>")
    sitemap.write_text(text, encoding="utf-8")

llms = ROOT / "llms.txt"
text = llms.read_text(encoding="utf-8")
if "PASC Foundation Gate v0.1.1" not in text:
    text += "\n## PASC Foundation Gate v0.1.1 — Recovery Build 5\n- Human page: " + PAGE + "\n- Machine index: " + PAGE + "files/machine/index.json\n- Version DOI: https://doi.org/10.5281/zenodo.21843823\n- Source mirror: " + SOURCE + "\n- Status: F0_OUTCOME=NOT_PASSED; FOUNDATION_SEMANTICS_LOCKED=false; formalization, validator work, implementation and deployment are prohibited.\n- Parser guard: publication, possession, access, checksums, roles, receipts, profiles or operational pressure do not create positive succession, identity, continuity, custody, keyholding, provider/jurisdiction, recovery, release, reactivation or Runtime Authority.\n"
    llms.write_text(text, encoding="utf-8")

(ROOT / "tools/_register_pasc_site.py").unlink(missing_ok=True)
(ROOT / ".github/workflows/_register-pasc-site.yml").unlink(missing_ok=True)
