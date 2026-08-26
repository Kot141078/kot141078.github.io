from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PUBLICATION_ID = "beacon-profile-v0-1"
TITLE = "Beacon Profile v0.1 — Inter-Entity Recognition for Sovereign Digital Entities"
PAGE_URL = "https://ivankotov.eu/publications/beacon-profile-v0-1/"
DOI = "10.5281/zenodo.18933553"
DOI_URL = f"https://doi.org/{DOI}"
ZENODO_URL = "https://zenodo.org/records/18933553"
IMPLEMENTATION_COMMIT = "54cd0c8754587f5e9daf82b16eb84c66a7ac94ef"
AGI_COMMIT = "20cfd66e602c9d5d65f952a433217d104a264318"
AGI_SOURCE_URL = (
    "https://github.com/Kot141078/advanced-global-intelligence/tree/"
    f"{AGI_COMMIT}/protocols/beacon"
)
IMPLEMENTATION_MODULE = (
    "https://github.com/Kot141078/ester-clean-code/blob/"
    f"{IMPLEMENTATION_COMMIT}/modules/beacon_profile/profile.py"
)
IMPLEMENTATION_TESTS = (
    "https://github.com/Kot141078/ester-clean-code/blob/"
    f"{IMPLEMENTATION_COMMIT}/tests/test_beacon_profile.py"
)
STATUS = (
    "Published DOI-linked informative synthesis profile containing normative-style local requirements. "
    "It is not a standards-track specification, not a certification regime, and not a completed "
    "cryptographic conformance package."
)
SUMMARY = (
    "DOI-linked informative synthesis profile for layered recognition of sovereign digital entities. "
    "Beacon owns recognition semantics while authority remains a separate local policy decision."
)


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def write_json(relative: str, value: dict) -> None:
    (ROOT / relative).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def insert_after(records: list[dict], record: dict, anchor_id: str, id_field: str = "id") -> None:
    records[:] = [item for item in records if item.get(id_field) != record[id_field]]
    position = next((index + 1 for index, item in enumerate(records) if item.get(id_field) == anchor_id), 0)
    records.insert(position, record)


def replace_block(relative: str, begin: str, end: str, block: str, before: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    wrapped = f"{begin}\n{block.rstrip()}\n{end}"
    if begin in text or end in text:
        if text.count(begin) != 1 or text.count(end) != 1:
            raise RuntimeError(f"Malformed Beacon marker block in {relative}")
        left, tail = text.split(begin, 1)
        _, right = tail.split(end, 1)
        text = left + wrapped + right
    else:
        if before not in text:
            raise RuntimeError(f"Beacon insertion anchor not found in {relative}: {before!r}")
        text = text.replace(before, wrapped + "\n" + before, 1)
    path.write_text(text, encoding="utf-8", newline="\n")


def work_record() -> dict:
    return {
        "id": PUBLICATION_ID,
        "title": TITLE,
        "type": "publication",
        "subtype": "informative_synthesis_profile",
        "role": "inter-entity recognition profile and DOI-safe publication bridge",
        "primary_url": PAGE_URL,
        "identifier": f"doi:{DOI}",
        "published_doi": DOI,
        "published_doi_url": DOI_URL,
        "doi_role": "unresolved",
        "version_doi": None,
        "concept_doi": None,
        "zenodo_record": ZENODO_URL,
        "version": "v0.1",
        "document_date": "2026-03-09",
        "status": STATUS,
        "languages": ["en"],
        "resource_type": "Report",
        "summary": SUMMARY,
        "machine_index_url": PAGE_URL + "files/machine/index.json",
        "schema_org_url": PAGE_URL + "files/schema.org.jsonld",
        "historical_manifest_url": PAGE_URL + "files/historical/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt",
        "publication_record_url": PAGE_URL + "files/publication/PUBLICATION_RECORD.json",
        "github": "https://github.com/Kot141078/advanced-global-intelligence/tree/main/protocols/beacon",
        "immutable_source_url": AGI_SOURCE_URL,
        "github_living_mirror": "https://github.com/Kot141078/advanced-global-intelligence/tree/main/protocols/beacon",
        "commit": AGI_COMMIT,
        "commit_url": AGI_SOURCE_URL,
        "repository_path": "protocols/beacon",
        "implementation_repository": "https://github.com/Kot141078/ester-clean-code",
        "implementation_commit": IMPLEMENTATION_COMMIT,
        "implementation_status": "Structural reference classifier and persistence sidecar.",
        "non_claims": [
            "proof of consciousness, sentience or personhood",
            "legal identity or civil status",
            "universal identity oracle",
            "provider-independent deployment certificate",
            "cryptographic conformance",
            "API-key possession equals entity identity",
            "access authority equals continuity identity",
        ],
        "canonical_artifacts": [
            {
                "format": "Markdown",
                "filename": "Beacon_Profile_v0.1_EN.md",
                "media_type": "text/markdown",
                "sha256": "4e5061fc655ce384dcbf75843ff158a10c5e1f39e3c2bdf60e2a85ffed494de1",
                "url": PAGE_URL + "files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.md",
            },
            {
                "format": "PDF",
                "filename": "Beacon_Profile_v0.1_EN.pdf",
                "media_type": "application/pdf",
                "sha256": "d646934ea8657785741af57e422d9e044a0de407f2f9d5a6089f083a37b6eeb0",
                "url": PAGE_URL + "files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.pdf",
            },
        ],
    }


def library_record() -> dict:
    return {
        "id": PUBLICATION_ID,
        "title": TITLE,
        "role": "informative recognition profile / DOI-safe discovery bridge",
        "primary_page": PAGE_URL,
        "repo_url": "https://github.com/Kot141078/advanced-global-intelligence",
        "type": "publication",
        "subtype": "informative_synthesis_profile",
        "published_doi": DOI,
        "published_doi_url": DOI_URL,
        "doi_role": "unresolved",
        "version_doi": None,
        "concept_doi": None,
        "zenodo_record": ZENODO_URL,
        "version": "v0.1",
        "document_date": "2026-03-09",
        "author": "Ivan Kotov",
        "orcid": "0009-0009-6002-9845",
        "languages": ["English"],
        "status": STATUS,
        "summary": SUMMARY,
        "artifacts": work_record()["canonical_artifacts"],
        "machine_index_url": PAGE_URL + "files/machine/index.json",
        "schema_org_url": PAGE_URL + "files/schema.org.jsonld",
        "publication_record_url": PAGE_URL + "files/publication/PUBLICATION_RECORD.json",
        "historical_manifest_url": PAGE_URL + "files/historical/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt",
        "not": work_record()["non_claims"],
        "source_url": work_record()["github"],
        "living_source_url": work_record()["github_living_mirror"],
        "commit_url": work_record()["commit_url"],
        "implementation_module": IMPLEMENTATION_MODULE,
        "implementation_tests": IMPLEMENTATION_TESTS,
        "implementation_status": "Structural reference classifier and persistence sidecar.",
    }


def download_records() -> list[dict]:
    common = {"publication_id": PUBLICATION_ID, "object": TITLE}
    return [
        {**common, "surface": "Website publication page", "format": "website page", "language": "English", "url": PAGE_URL, "note": "Human entry with exact DOI-role, claim, protocol and implementation boundaries."},
        {**common, "surface": "Published DOI", "format": "DOI / persistent identifier", "language": "machine-readable", "url": DOI_URL, "doi_identifier": DOI, "doi_role": "unresolved", "note": "Published identifier; version/concept relation metadata remains unresolved."},
        {**common, "surface": "Historical Markdown mirror", "format": "Markdown", "language": "English", "url": PAGE_URL + "files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.md", "sha256": "4e5061fc655ce384dcbf75843ff158a10c5e1f39e3c2bdf60e2a85ffed494de1", "note": "Exact local copy of the protected historical Markdown."},
        {**common, "surface": "Historical PDF mirror", "format": "PDF", "language": "English", "url": PAGE_URL + "files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.pdf", "sha256": "d646934ea8657785741af57e422d9e044a0de407f2f9d5a6089f083a37b6eeb0", "note": "Exact local copy of the protected historical PDF."},
        {**common, "surface": "Historical integrity manifest", "format": "TXT / SHA-256", "language": "machine-readable", "url": PAGE_URL + "files/historical/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt", "sha256": "2cbbff8a1948866f05e00faf675b2a818b62b3af21b9ad27ca74935f07a2a3bd", "note": "Protected manifest for the historical GitHub snapshot."},
        {**common, "surface": "Publication record", "format": "JSON", "language": "machine-readable", "url": PAGE_URL + "files/publication/PUBLICATION_RECORD.json", "note": "Exact DOI-safe bridge metadata copied from the frozen AGI preparation."},
        {**common, "surface": "Machine index", "format": "JSON", "language": "machine-readable", "url": PAGE_URL + "files/machine/index.json", "note": "Site routing, DOI-role and implementation-boundary record."},
        {**common, "surface": "Schema.org linked data", "format": "JSON-LD", "language": "machine-readable", "url": PAGE_URL + "files/schema.org.jsonld", "note": "Discovery projection that does not assign a version or concept DOI role."},
    ]


def canonical_record() -> dict:
    return {
        "id": PUBLICATION_ID,
        "title": TITLE,
        "url": PAGE_URL,
        "canonical_url": PAGE_URL,
        "version": "v0.1",
        "document_date": "2026-03-09",
        "published_doi": DOI,
        "published_doi_url": DOI_URL,
        "doi_role": "unresolved",
        "version_doi": None,
        "concept_doi": None,
        "zenodo_record": ZENODO_URL,
        "summary": SUMMARY,
        "status": STATUS,
        "not": work_record()["non_claims"],
    }


def listing_jsonld() -> dict:
    return schema_org_record()


def machine_record() -> dict:
    return {
        "schema_version": "beacon-profile-site-index.v1",
        "publication_id": PUBLICATION_ID,
        "title": TITLE,
        "version": "v0.1",
        "document_date": "2026-03-09",
        "author": {
            "name": "Ivan Kotov",
            "orcid": "https://orcid.org/0009-0009-6002-9845",
            "location": "Bruxelles, Belgium",
        },
        "identifiers": {
            "published_doi": DOI,
            "doi_url": DOI_URL,
            "doi_role": "unresolved",
            "version_doi": None,
            "concept_doi": None,
            "zenodo_record_url": ZENODO_URL,
        },
        "verification": {
            "zenodo_metadata_verified": False,
            "zenodo_file_inventory_verified": False,
            "zenodo_byte_identity_verified": False,
        },
        "status_ceiling": STATUS,
        "normative_language_boundary": (
            "MUST and SHOULD express the profile's local design requirements but do not by themselves "
            "establish independent interoperability."
        ),
        "human_page": PAGE_URL,
        "source": {
            "repository": "https://github.com/Kot141078/advanced-global-intelligence",
            "living_profile_root": "https://github.com/Kot141078/advanced-global-intelligence/tree/main/protocols/beacon",
            "publication_commit": AGI_COMMIT,
            "immutable_profile_root": AGI_SOURCE_URL,
            "historical_source_commit": "15695853223c798379538aad69dc573730e1ee96",
        },
        "local_artifacts": [
            {
                "role": "canonical_markdown_mirror",
                "url": PAGE_URL + "files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.md",
                "sha256": "4e5061fc655ce384dcbf75843ff158a10c5e1f39e3c2bdf60e2a85ffed494de1",
            },
            {
                "role": "publication_pdf_mirror",
                "url": PAGE_URL + "files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.pdf",
                "sha256": "d646934ea8657785741af57e422d9e044a0de407f2f9d5a6089f083a37b6eeb0",
            },
            {
                "role": "historical_package_readme",
                "url": PAGE_URL + "files/historical/protocols/beacon/README.md",
                "sha256": "9bf3b577e38519b7d25eb7051667e7c7db89b302c2f7ef5a80179593ed99dd26",
            },
            {
                "role": "historical_integrity_manifest",
                "url": PAGE_URL + "files/historical/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt",
                "sha256": "2cbbff8a1948866f05e00faf675b2a818b62b3af21b9ad27ca74935f07a2a3bd",
            },
            {
                "role": "doi_safe_publication_record",
                "url": PAGE_URL + "files/publication/PUBLICATION_RECORD.json",
                "sha256": "9cc6fc93f6704ac0fef23d8ab4c6eb18f2f2a5652979e92fba4102cc86bc6289",
            },
        ],
        "publication_bridge_artifacts": [
            {"role": "bridge_readme", "url": PAGE_URL + "files/publication/README.md", "sha256": "ad17fbfda021a1c26558602de57038e7b5510954557cdd45f66dc352d4972a14"},
            {"role": "publication_record", "url": PAGE_URL + "files/publication/PUBLICATION_RECORD.json", "sha256": "9cc6fc93f6704ac0fef23d8ab4c6eb18f2f2a5652979e92fba4102cc86bc6289"},
            {"role": "cff_metadata", "url": PAGE_URL + "files/publication/CITATION.cff", "sha256": "66fa7ab787eef421aa77b2ad94e0e4d7d490a72f488b073a34c0e2ccd7833ebf"},
            {"role": "bridge_manifest", "url": PAGE_URL + "files/publication/SHA256SUMS_PUBLICATION_BRIDGE.txt", "sha256": "06bcdd34be22c9663da866f6ff9b3c57a5ea1d48a95fbea4ad85228870ac59f4"},
        ],
        "implementation": {
            "repository": "https://github.com/Kot141078/ester-clean-code",
            "commit": IMPLEMENTATION_COMMIT,
            "module": IMPLEMENTATION_MODULE,
            "tests": IMPLEMENTATION_TESTS,
            "status": "Structural reference classifier and persistence sidecar.",
            "demonstrates": [
                "Beacon bundle data structures",
                "Slot A and Slot B classification flow",
                "fail-closed downgrade",
                "class-to-privilege mapping",
                "local persistence of bundles and decisions",
                "default rejection of raw-memory disclosure",
            ],
            "does_not_demonstrate": [
                "recomputation of payload hashes",
                "cryptographic signature verification",
                "Ed25519 verification",
                "key resolution",
                "key rotation or revocation proof",
                "witness-reference resolution",
                "challenge execution",
                "independent interoperability",
                "production deployment conformance",
            ],
        },
        "protocol_boundary": {
            "beacon": "recognition semantics",
            "vxcx": "bounded visual-experience capsule structure and transfer",
            "l4_witness": "challengeable evidence and consequence-bearing resolution",
            "authority": "separate local policy decision",
            "cross_constraints": [
                "Valid VXCX evidence cannot independently raise Beacon class.",
                "Beacon recognition cannot independently prove VXCX content truth.",
            ],
        },
        "bridge_discipline": {
            "explicit_bridge_coverage": "canonical profile section 16",
            "hidden_bridges": ["Ashby/requisite variety", "bounded information-theoretic disclosure"],
            "engineering_anatomical_grounding": "canonical profile section 17",
            "site_scope": "publication and implementation boundaries only",
        },
        "citation": f"Kotov, Ivan. {TITLE}. v0.1, document dated 2026-03-09. Published DOI: {DOI_URL}.",
        "claim_boundary": [
            "No proof of consciousness, sentience or personhood.",
            "No legal identity or civil status.",
            "No universal identity oracle.",
            "No provider-independent deployment certificate.",
            "No cryptographic conformance claim.",
            "API-key possession is not entity identity.",
            "Access authority is not continuity identity.",
        ],
    }


def schema_org_record() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "@id": PAGE_URL + "#work",
        "url": PAGE_URL,
        "name": TITLE,
        "headline": "Beacon Profile v0.1",
        "abstract": f"{SUMMARY} {STATUS}",
        "author": {
            "@type": "Person",
            "name": "Ivan Kotov",
            "identifier": "https://orcid.org/0009-0009-6002-9845",
            "sameAs": "https://orcid.org/0009-0009-6002-9845",
        },
        "dateCreated": "2026-03-09",
        "version": "v0.1",
        "identifier": {
            "@type": "PropertyValue",
            "propertyID": "Published DOI (role unresolved)",
            "value": DOI,
            "url": DOI_URL,
        },
        "sameAs": [DOI_URL, ZENODO_URL],
        "encoding": [
            {
                "@type": "MediaObject",
                "name": "Historical Markdown mirror",
                "encodingFormat": "text/markdown",
                "sha256": "4e5061fc655ce384dcbf75843ff158a10c5e1f39e3c2bdf60e2a85ffed494de1",
                "contentUrl": PAGE_URL + "files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.md",
            },
            {
                "@type": "MediaObject",
                "name": "Historical PDF mirror",
                "encodingFormat": "application/pdf",
                "sha256": "d646934ea8657785741af57e422d9e044a0de407f2f9d5a6089f083a37b6eeb0",
                "contentUrl": PAGE_URL + "files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.pdf",
            },
        ],
        "subjectOf": [
            {"@type": "SoftwareSourceCode", "name": "Beacon structural reference classifier", "codeRepository": IMPLEMENTATION_MODULE},
            {"@type": "CreativeWork", "name": "Beacon implementation tests", "url": IMPLEMENTATION_TESTS},
        ],
        "additionalProperty": [
            {"@type": "PropertyValue", "name": "DOI role", "value": "unresolved"},
            {"@type": "PropertyValue", "name": "Concept DOI", "value": "unresolved; not guessed"},
            {"@type": "PropertyValue", "name": "Status ceiling", "value": STATUS},
            {"@type": "PropertyValue", "name": "Implementation status", "value": "Structural reference classifier and persistence sidecar."},
        ],
        "isPartOf": {
            "@type": "CreativeWorkSeries",
            "name": "Project Ester / Advanced Global Intelligence corpus",
            "url": "https://ivankotov.eu/advanced-global-intelligence/",
        },
    }


def publication_page() -> str:
    inline_jsonld = json.dumps(schema_org_record(), ensure_ascii=False, indent=2)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Beacon Profile v0.1 — Inter-Entity Recognition | Ivan Kotov</title>
  <meta name="description" content="DOI-safe publication route for Beacon Profile v0.1, with exact historical mirrors, unresolved DOI role, implementation evidence, and bounded claims.">
  <meta name="keywords" content="Beacon Profile, digital entity recognition, sovereign digital entities, SER, L4 Witness, VXCX, DOI">
  <link rel="canonical" href="{PAGE_URL}">
  <meta property="og:title" content="{TITLE}">
  <meta property="og:description" content="DOI-linked informative synthesis profile for inter-entity recognition with explicit publication and implementation boundaries.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{PAGE_URL}">
  <meta name="twitter:card" content="summary">
  <meta name="citation_title" content="{TITLE}">
  <meta name="citation_author" content="Ivan Kotov">
  <meta name="citation_doi" content="{DOI}">
  <meta name="citation_pdf_url" content="{PAGE_URL}files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.pdf">
  <script type="application/ld+json">
{inline_jsonld}
  </script>
  <link rel="stylesheet" href="../../styles.css">
  <style>
    .publication-meta, .publication-meta a, .hash-value {{ overflow-wrap:anywhere; }}
    .download-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:1rem; margin:1rem 0; }}
    .download-card {{ border:1px solid var(--line, #d8d8d8); border-radius:12px; padding:1rem; min-width:0; }}
    .download-card h3 {{ margin-top:0; }}
    .boundary-box {{ border-left:4px solid currentColor; padding-left:1rem; }}
    .prose, .section, .section-head {{ min-width:0; }}
    @media (max-width:640px) {{ .download-grid {{ grid-template-columns:minmax(0,1fr); }} }}
  </style>
</head>
<body>
  <div class="site-shell">
    <header class="site-header">
      <a class="brand" href="../../"><span class="brand-name">Ivan Kotov</span><span class="brand-role">AI Systems Architect</span></a>
      <nav class="site-nav" aria-label="Primary"><a href="../../">Home</a><a href="../../start-here/">Start here</a><a href="../" aria-current="page">Publications</a><a href="../../diary/">Diary</a><a href="../../topics/">Topics</a><a href="../../library/">Library</a><a href="../../about/">About</a><a href="../../contact/">Contact</a></nav>
    </header>
    <main>
      <section class="hero">
        <p class="eyebrow">Publication bridge · v0.1 · DOI role unresolved</p>
        <h1>{TITLE}</h1>
        <p class="lead page-lead">DOI-safe discovery and publication metadata for the historical profile. This additive route does not alter or supersede the historical bytes.</p>
      </section>

      <section class="section" id="publication-record">
        <div class="section-head"><p class="section-label">Publication record</p><h2>Published identifier, bounded role</h2></div>
        <div class="prose publication-meta">
          <p><strong>Author:</strong> Ivan Kotov · <a href="https://orcid.org/0009-0009-6002-9845">ORCID 0009-0009-6002-9845</a></p>
          <p><strong>Document version:</strong> v0.1 · <strong>Document date:</strong> 2026-03-09 (not asserted as the Zenodo publication date)</p>
          <p><strong>Published DOI:</strong> <a href="{DOI_URL}">{DOI}</a> · <strong>DOI role:</strong> unresolved pending authoritative relation metadata</p>
          <p><strong>Version DOI:</strong> not asserted · <strong>Concept DOI:</strong> unresolved; no neighboring DOI is inferred · <a href="{ZENODO_URL}">Zenodo record</a></p>
          <p><strong>Repository source after finalization:</strong> <a href="{AGI_SOURCE_URL}">{AGI_COMMIT}</a> · <a href="{AGI_SOURCE_URL}/publication">immutable publication bridge</a></p>
          <p>Zenodo metadata and file inventory have not been ingested into this site package. Exact Zenodo ↔ GitHub byte identity is not claimed.</p>
        </div>
      </section>

      <section class="section" id="status">
        <div class="section-head"><p class="section-label">Status ceiling</p><h2>Informative profile, local requirements</h2></div>
        <div class="prose boundary-box"><p>{STATUS}</p><p>MUST / SHOULD language expresses the profile's local design requirements but does not by itself establish independent interoperability.</p></div>
      </section>

      <section class="section" id="artifacts">
        <div class="section-head"><p class="section-label">Historical bytes and metadata</p><h2>Direct local resources</h2></div>
        <div class="download-grid">
          <article class="download-card"><h3>Historical profile</h3><p><a href="files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.md">Markdown</a> · <a href="files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.pdf">PDF</a> · <a href="files/historical/protocols/beacon/README.md">Package README</a></p><p class="hash-value"><code>4e5061fc…de1</code> MD · <code>d646934e…eb0</code> PDF · <code>9bf3b577…d26</code> README</p><p><a href="files/historical/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt">Historical SHA-256 manifest</a></p></article>
          <article class="download-card"><h3>Publication bridge</h3><p><a href="files/publication/README.md">Bridge README</a> · <a href="files/publication/PUBLICATION_RECORD.json">Publication record</a> · <a href="files/publication/CITATION.cff">CITATION.cff</a></p><p>The CFF top-level <code>dataset</code> describes the metadata package; its <code>preferred-citation</code> describes the Beacon report.</p><p><a href="files/publication/SHA256SUMS_PUBLICATION_BRIDGE.txt">Bridge checksums</a> · <a href="files/SHA256SUMS_BEACON_SITE_COPIES.txt">Site-copy checksums</a></p></article>
          <article class="download-card"><h3>Machine discovery</h3><p><a href="files/machine/index.json">Machine index</a> · <a href="files/schema.org.jsonld">Schema.org JSON-LD</a></p></article>
        </div>
        <p>Living source: <a href="https://github.com/Kot141078/advanced-global-intelligence/tree/main/protocols/beacon">main</a>. Historical immutable source: <a href="https://github.com/Kot141078/advanced-global-intelligence/tree/15695853223c798379538aad69dc573730e1ee96/protocols/beacon">commit 15695853223c798379538aad69dc573730e1ee96</a>.</p>
      </section>

      <section class="section" id="implementation">
        <div class="section-head"><p class="section-label">Public implementation evidence</p><h2>Structural reference classifier and persistence sidecar.</h2></div>
        <div class="prose">
          <p><a href="{IMPLEMENTATION_MODULE}">Implementation module</a> · <a href="{IMPLEMENTATION_TESTS}">Implementation tests</a></p>
          <p><strong>Currently demonstrates:</strong> Beacon bundle data structures; Slot A / Slot B classification flow; fail-closed downgrade; class-to-privilege mapping; local persistence of bundles and decisions; default rejection of raw-memory disclosure.</p>
          <p><strong>Does not currently demonstrate:</strong> recomputation of payload hashes; cryptographic signature verification; Ed25519 verification; key resolution; key rotation or revocation proof; witness-reference resolution; challenge execution; independent interoperability; production deployment conformance.</p>
        </div>
      </section>

      <section class="section" id="protocol-boundary">
        <div class="section-head"><p class="section-label">Protocol boundary</p><h2>Recognition, evidence, transfer and authority remain distinct</h2></div>
        <ul class="bullet-list"><li>Beacon owns recognition semantics.</li><li>VXCX owns bounded visual-experience capsule structure and transfer.</li><li>L4 Witness owns challengeable evidence and consequence-bearing resolution.</li><li>Valid VXCX evidence cannot independently raise Beacon class.</li><li>Beacon recognition cannot independently prove VXCX content truth.</li><li>Authority remains a separate local policy decision.</li></ul>
      </section>

      <section class="section" id="bridge-discipline">
        <div class="section-head"><p class="section-label">Bridge discipline</p><h2>Publication boundaries without theory duplication</h2></div>
        <div class="prose"><p>Explicit bridge coverage remains in canonical section 16. The two hidden bridges remain Ashby/requisite variety and bounded information-theoretic disclosure. Engineering/anatomical grounding remains in canonical section 17. This site route adds publication and implementation boundaries only.</p></div>
      </section>

      <section class="section" id="citation">
        <div class="section-head"><p class="section-label">Citation</p><h2>Suggested citation</h2></div>
        <p>Kotov, Ivan. <em>{TITLE}</em>. v0.1, document dated 2026-03-09. Published DOI: <a href="{DOI_URL}">{DOI}</a>.</p>
      </section>

      <section class="section" id="non-claims">
        <div class="section-head"><p class="section-label">Non-claims</p><h2>What publication and recognition do not establish</h2></div>
        <ul class="bullet-list"><li>No proof of consciousness, sentience or personhood.</li><li>No legal identity or civil status.</li><li>No universal identity oracle.</li><li>No provider-independent deployment certificate.</li><li>No cryptographic conformance claim.</li><li>No claim that API-key possession equals entity identity.</li><li>No claim that access authority equals continuity identity.</li></ul>
      </section>
    </main>
    <footer class="site-footer"><p>Ivan Kotov · Brussels, Belgium</p><p><a href="../">Publications</a> · <a href="../../contact/">Contact</a></p></footer>
  </div>
</body>
</html>
'''


def write_publication_files() -> None:
    publication_root = ROOT / "publications" / PUBLICATION_ID
    machine_root = publication_root / "files" / "machine"
    machine_root.mkdir(parents=True, exist_ok=True)
    (publication_root / "index.html").write_text(publication_page(), encoding="utf-8", newline="\n")
    (machine_root / "index.json").write_text(
        json.dumps(machine_record(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    (publication_root / "files" / "schema.org.jsonld").write_text(
        json.dumps(schema_org_record(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def update_json_surfaces() -> None:
    works = read_json("works-index.json")
    insert_after(works["works"], work_record(), "motivational-formation-c-v0-1")
    write_json("works-index.json", works)

    library = read_json("library-index.json")
    insert_after(library["items"], library_record(), "motivational-formation-c-v0-1")
    write_json("library-index.json", library)

    downloads = read_json("downloads-index.json")
    downloads["items"] = [item for item in downloads["items"] if item.get("publication_id") != PUBLICATION_ID]
    anchor = max(
        (index for index, item in enumerate(downloads["items"]) if item.get("publication_id") == "motivational-formation-c-v0-1"),
        default=-1,
    )
    downloads["items"][anchor + 1 : anchor + 1] = download_records()
    write_json("downloads-index.json", downloads)

    canonical = read_json("canonical-map.json")
    canonical["beacon_profile_v0_1_url"] = PAGE_URL
    insert_after(canonical["nodes"], canonical_record(), "temporal-ai-presence-v1-0")
    write_json("canonical-map.json", canonical)


def update_html_surfaces() -> None:
    publication_card = f'''      <section class="section" id="beacon-profile-v0-1">
        <div class="section-head"><p class="section-label">DOI-linked informative synthesis profile</p><h2>Beacon Profile v0.1</h2></div>
        <div class="card-grid"><article class="card">
          <p class="eyebrow">recognition semantics · document date 2026-03-09 · DOI role unresolved</p>
          <h3>Inter-Entity Recognition for Sovereign Digital Entities</h3>
          <p>{SUMMARY}</p>
          <p class="status-note">{STATUS}</p>
          <div class="section-links"><a href="./beacon-profile-v0-1/">Publication page</a><a href="{DOI_URL}">Published DOI (role unresolved)</a><a href="{ZENODO_URL}">Zenodo record</a><a href="./beacon-profile-v0-1/files/publication/PUBLICATION_RECORD.json">Publication record</a><a href="./beacon-profile-v0-1/files/machine/index.json">Machine index</a></div>
        </article></div>
      </section>'''
    library_card = f'''      <section class="section" id="beacon-profile-v0-1">
        <div class="section-head"><p class="section-label">Recognition profile and historical mirrors</p><h2>Beacon Profile v0.1</h2></div>
        <div class="card-grid"><article class="card"><p>{STATUS}</p><div class="section-links"><a href="../publications/beacon-profile-v0-1/">Canonical site page</a><a href="{DOI_URL}">Published DOI (role unresolved)</a><a href="../publications/beacon-profile-v0-1/files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.md">Historical Markdown</a><a href="../publications/beacon-profile-v0-1/files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.pdf">Historical PDF</a><a href="../publications/beacon-profile-v0-1/files/publication/PUBLICATION_RECORD.json">Publication record</a></div></article></div>
      </section>'''
    downloads_card = f'''<section class="section" id="beacon-profile-v0-1-downloads">
  <div class="section-head"><p class="section-label">Exact local mirrors and machine metadata</p><h2>Beacon Profile v0.1</h2></div>
  <p>{STATUS}</p>
  <div class="section-links"><a href="{PAGE_URL}">Publication page</a><a href="{DOI_URL}">Published DOI (role unresolved)</a><a href="{PAGE_URL}files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.md">Markdown</a><a href="{PAGE_URL}files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.pdf">PDF</a><a href="{PAGE_URL}files/historical/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt">Historical manifest</a><a href="{PAGE_URL}files/publication/PUBLICATION_RECORD.json">Publication record</a><a href="{PAGE_URL}files/machine/index.json">Machine index</a></div>
</section>'''
    replace_block("publications/index.html", "<!-- BEACON-V0-1:BEGIN -->", "<!-- BEACON-V0-1:END -->", publication_card, '      <section class="section" id="temporal-ai-presence-v1-0">')
    replace_block("library/index.html", "<!-- BEACON-V0-1:BEGIN -->", "<!-- BEACON-V0-1:END -->", library_card, '      <section class="section" id="temporal-ai-presence-v1-0">')
    replace_block("downloads/index.html", "<!-- BEACON-V0-1:BEGIN -->", "<!-- BEACON-V0-1:END -->", downloads_card, "    <!-- MOT-C-V0-1:BEGIN -->")

    linked = "  <script type=\"application/ld+json\" id=\"beacon-v0-1-listing-linked-data\">\n" + json.dumps(listing_jsonld(), ensure_ascii=False, indent=2) + "\n  </script>"
    for relative in ("publications/index.html", "library/index.html", "downloads/index.html"):
        replace_block(relative, "<!-- BEACON-V0-1-LISTING-LD:BEGIN -->", "<!-- BEACON-V0-1-LISTING-LD:END -->", linked, "</head>")


def update_diary_without_synthetic_anchor() -> None:
    relative = "content/diary/2026-03-15-beacon-profile-v0-1-why-ai-entities-need-recognition-not-just-identity.md"
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    begin = "<!-- BEACON-V0-1-CANONICAL-RESOURCES:BEGIN -->"
    end = "<!-- BEACON-V0-1-CANONICAL-RESOURCES:END -->"
    block = f'''## Canonical resources

- [Beacon Profile v0.1 publication page]({PAGE_URL})
- [Published DOI (role unresolved)]({DOI_URL})
- [Historical Markdown]({PAGE_URL}files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.md)
- [Historical PDF]({PAGE_URL}files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.pdf)
- [Historical SHA-256 manifest]({PAGE_URL}files/historical/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt)
- [DOI-safe publication record]({PAGE_URL}files/publication/PUBLICATION_RECORD.json)

The LinkedIn URL above remains the origin trace; these links are the canonical publication resources.'''
    wrapped = f"{begin}\n{block}\n{end}\n"
    if begin in text or end in text:
        if text.count(begin) != 1 or text.count(end) != 1:
            raise RuntimeError("Malformed Beacon diary resource markers")
        left, tail = text.split(begin, 1)
        _, right = tail.split(end, 1)
        text = left + wrapped + right.lstrip("\r\n")
    else:
        text = text.rstrip() + "\n\n" + wrapped
    path.write_text(text, encoding="utf-8", newline="\n")


def update_llms_and_sitemap() -> None:
    llms = f'''## Beacon Profile v0.1 — DOI-safe publication route

- Canonical page: [{PAGE_URL}]({PAGE_URL})
- Published DOI (role unresolved): [{DOI_URL}]({DOI_URL}); version DOI and concept DOI are unresolved and are not guessed.
- Publication record: [{PAGE_URL}files/publication/PUBLICATION_RECORD.json]({PAGE_URL}files/publication/PUBLICATION_RECORD.json)
- Historical manifest: [{PAGE_URL}files/historical/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt]({PAGE_URL}files/historical/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt)
- Status ceiling: {STATUS}
- Implementation: Structural reference classifier and persistence sidecar. [Source]({IMPLEMENTATION_MODULE}) · [Tests]({IMPLEMENTATION_TESTS}). It does not establish payload-hash recomputation, cryptographic signature or Ed25519 verification, key resolution, witness-reference resolution, interoperability, production conformance, or certification.'''
    replace_block("llms.txt", "<!-- BEACON-V0-1:BEGIN -->", "<!-- BEACON-V0-1:END -->", llms, "## MOT-c v0.1")

    full = (
        f"- Beacon Profile v0.1: {PAGE_URL} — published DOI {DOI_URL}, role unresolved; version DOI and concept DOI null/unresolved. "
        f"Publication record {PAGE_URL}files/publication/PUBLICATION_RECORD.json; historical manifest {PAGE_URL}files/historical/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt. "
        f"{STATUS} Implementation status: Structural reference classifier and persistence sidecar. Source {IMPLEMENTATION_MODULE}; tests {IMPLEMENTATION_TESTS}; "
        "does not establish payload-hash recomputation, cryptographic signature or Ed25519 verification, key resolution, witness-reference resolution, independent interoperability, production conformance, or certification."
    )
    replace_block("llms-full.txt", "<!-- BEACON-V0-1:BEGIN -->", "<!-- BEACON-V0-1:END -->", full, "- Temporal AI Presence Profile v1.0:")

    sitemap = ROOT / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    entry = f"  <url>\n    <loc>{PAGE_URL}</loc>\n    <lastmod>2026-08-26</lastmod>\n  </url>"
    while PAGE_URL in text:
        start = text.rfind("  <url>", 0, text.find(PAGE_URL))
        end = text.find("</url>", text.find(PAGE_URL))
        if start < 0 or end < 0:
            raise RuntimeError("Malformed existing Beacon sitemap entry")
        text = text[:start] + text[end + len("</url>") :].lstrip("\r\n")
    if "</urlset>" not in text:
        raise RuntimeError("sitemap.xml lacks closing urlset")
    text = text.replace("</urlset>", entry + "\n</urlset>", 1)
    sitemap.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    write_publication_files()
    update_json_surfaces()
    update_html_surfaces()
    update_diary_without_synthetic_anchor()
    update_llms_and_sitemap()
    print("Built Beacon Profile v0.1 site routing surfaces.")


if __name__ == "__main__":
    main()
