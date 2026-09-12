from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
DOI = "10.5281/zenodo.22724626"
DOI_URL = f"https://doi.org/{DOI}"
ZENODO = "https://zenodo.org/records/22724626"
CANON = "https://ivankotov.eu/publications/cgdr-selected-process-r1-6an/"
TITLE = "CGDR-R1.6A Selected-Process Conformance: current-AK Source and R1.6AN Synthetic Evidence"
AGI_COMMIT = "93de42857f5057d49d7272a6be9fd2b237e8d4d2"
AGI_BASE = "https://github.com/Kot141078/advanced-global-intelligence/"
PART = "publications/cgdr-selected-process-r1-6an/"
PACKAGE = AGI_BASE + "tree/" + AGI_COMMIT + "/" + PART + "doi-v0.1.1"
LICENSE = AGI_BASE + "blob/62cb3feb9e1336f9cf4ecf517de718975bf21ee4/" + PART + "source-v0.1/LICENSE.md"
ZIP_NAME = "CGDR_R1_6AN_DOI_22724626_v0_1_1_PUBLIC.zip"
PDF_NAME = "CGDR_R1_6AN_Technical_Report_v0_1_1.pdf"
ZIP_URL = ZENODO + "/files/" + ZIP_NAME + "?download=1"
PDF_URL = ZENODO + "/files/" + PDF_NAME + "?download=1"
ZIP_SHA = "2f299d529e22e2dfd8981ec8cd0ffa8d3a7a22d63f7f84a63c12eea2f8140e01"
PDF_SHA = "a3e24048a5acfbc98af82c31c1718cdfcfb3e571750b699ff1956972bfc50d56"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, value: str) -> None:
    (ROOT / path).write_text(value, encoding="utf-8", newline="\n")


def require(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def find_node(value, target_id: str):
    if isinstance(value, dict):
        if value.get("@id") == target_id:
            return value
        for nested in value.values():
            hit = find_node(nested, target_id)
            if hit is not None:
                return hit
    elif isinstance(value, list):
        for nested in value:
            hit = find_node(nested, target_id)
            if hit is not None:
                return hit
    return None


def patch_jsonld(text: str, target_id: str, updater) -> str:
    pattern = r'<script type="application/ld\+json">\s*(.*?)\s*</script>'
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        try:
            obj = json.loads(match.group(1))
        except json.JSONDecodeError:
            return match.group(0)
        node = find_node(obj, target_id)
        if node is None:
            return match.group(0)
        updater(node)
        count += 1
        return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=2) + '\n</script>'

    out = re.sub(pattern, repl, text, flags=re.S)
    require(count == 1, f"Expected one JSON-LD target {target_id}, got {count}")
    return out


def patch_work_page() -> None:
    path = "publications/cgdr-selected-process-r1-6an/index.html"
    s = read(path)
    if DOI not in s:
        s = s.replace(
            "Source disclosure and evidence note · v0.1 · 12 September 2026",
            "Source and synthetic evidence · v0.1.1 · 12 September 2026",
            1,
        )
        old = "The complete current-AK source tree is now public with research-use permission. Independent clean-host replication remains outstanding. No DOI or formal GitHub Release has been assigned."
        new = "The complete current-AK source tree, technical report and evidence package are published as version 0.1.1. DOI: <a href=\"" + DOI_URL + "\">" + DOI + "</a>. Independent clean-host replication remains outstanding."
        require(old in s, "Canonical status anchor missing")
        s = s.replace(old, new, 1)
        citation = "\n".join([
            '  <meta name="citation_title" content="' + TITLE + '">',
            '  <meta name="citation_author" content="Ivan Kotov">',
            '  <meta name="citation_publication_date" content="2026/09/12">',
            '  <meta name="citation_doi" content="' + DOI + '">',
            '  <meta name="citation_pdf_url" content="' + PDF_URL + '">',
        ])
        anchor = '  <link rel="stylesheet" href="../../styles.css">'
        require(anchor in s, "Stylesheet anchor missing")
        s = s.replace(anchor, citation + "\n" + anchor, 1)

        def update(node: dict) -> None:
            node["headline"] = TITLE
            node["version"] = "0.1.1"
            node["dateModified"] = "2026-09-12"
            node["inLanguage"] = ["en", "ru"]
            node["identifier"] = {"@type": "PropertyValue", "propertyID": "DOI", "value": DOI, "url": DOI_URL}
            node["sameAs"] = [DOI_URL, ZENODO, PACKAGE]
            node["license"] = LICENSE
            node["encoding"] = [
                {"@type": "MediaObject", "encodingFormat": "application/pdf", "contentUrl": PDF_URL},
                {"@type": "MediaObject", "encodingFormat": "application/zip", "contentUrl": ZIP_URL},
            ]

        s = patch_jsonld(s, CANON + "#work", update)

        section = f'''      <section class="section" id="doi-edition-22724626">
        <div class="section-head"><p class="section-label">Published DOI edition · v0.1.1</p><h2>Source, technical report and citable record</h2></div>
        <div class="prose">
          <p><strong>Ivan Kotov</strong> · ORCID <a href="https://orcid.org/0009-0009-6002-9845">0009-0009-6002-9845</a> · DOI <a href="{DOI_URL}">{DOI}</a>.</p>
          <p>Version 0.1.1 adds DOI-facing metadata and the attributed technical report while preserving the previously published source package byte-for-byte. The underlying R1.6AN experiment is not rerun or re-scored by this publication.</p>
        </div>
        <div class="section-links">
          <a href="{DOI_URL}">DOI</a>
          <a href="{ZENODO}">Zenodo record</a>
          <a href="{PDF_URL}">Technical report PDF</a>
          <a href="{ZIP_URL}">Complete public ZIP</a>
          <a href="{PACKAGE}">Exact GitHub DOI edition</a>
        </div>
        <p>Public ZIP: 541,373 bytes. SHA-256:</p>
        <pre><code>{ZIP_SHA}</code></pre>
        <p class="status-note">This remains a bounded internally accepted synthetic selected-process result. Independent clean-host replication, a c-specific real effect, economic value and live-deployment readiness are not established.</p>
      </section>
'''
        anchor = '      <section class="section" id="current-ak-source">'
        require(anchor in s, "Current-AK section anchor missing")
        s = s.replace(anchor, section + anchor, 1)
    write(path, s)


def patch_evidence() -> None:
    path = "evidence/index.html"
    s = read(path)
    card = f'''<article class="card" id="cgdr-r1-6an-evidence-note">
            <h3>CGDR R1.6AN: source and synthetic evidence</h3>
            <p>Ivan Kotov · version 0.1.1 · 12 September 2026. Published software/source package, technical report and all 756 observer values for the internally accepted selected profile: 18/18 episodes, 21/21 checkpoints, three expected local effects, zero promotions.</p>
            <p class="status-note">Independent replication, c-specific real effect, economic value and deployment readiness remain unestablished. Diagnostic FAIL and INCONCLUSIVE values remain visible.</p>
            <div class="section-links"><a href="../publications/cgdr-selected-process-r1-6an/">Canonical work page</a><a href="{DOI_URL}">{DOI}</a><a href="{ZENODO}">Zenodo</a><a href="{PACKAGE}">Exact GitHub edition</a></div>
          </article>'''
    s, n = re.subn(r'<article class="card" id="cgdr-r1-6an-evidence-note">.*?</article>', card, s, flags=re.S)
    require(n == 1, "Evidence card missing or ambiguous")
    write(path, s)


def patch_publications() -> None:
    path = "publications/index.html"
    s = read(path)
    if 'id="cgdr-r1-6an-v0-1-1"' not in s:
        section = f'''      <section class="section" id="cgdr-r1-6an-v0-1-1">
        <div class="section-head"><p class="section-label">Software and technical evidence</p><h2>CGDR R1.6AN</h2></div>
        <p>{TITLE}. Ivan Kotov, version 0.1.1, 12 September 2026. Published source and technical report for a bounded internally accepted synthetic profile; no independent replication or real-world effect is claimed.</p>
        <div class="section-links"><a href="{CANON}">Canonical work page</a><a href="{DOI_URL}">{DOI}</a><a href="{ZENODO}">Zenodo record</a><a href="{PDF_URL}">Report PDF</a><a href="{PACKAGE}">Source and evidence</a></div>
      </section>
'''
        pos = s.rfind("</main>")
        require(pos != -1, "Publications closing main missing")
        s = s[:pos] + section + s[pos:]

    def update(node: dict) -> None:
        seq = node.setdefault("itemListElement", [])
        if any(item.get("item", {}).get("@id") == CANON + "#work" for item in seq if isinstance(item, dict)):
            return
        seq.append({
            "@type": "ListItem",
            "position": len(seq) + 1,
            "item": {
                "@type": "SoftwareSourceCode",
                "@id": CANON + "#work",
                "name": TITLE,
                "url": CANON,
                "identifier": DOI_URL,
                "version": "0.1.1",
                "datePublished": "2026-09-12",
                "author": {"@type": "Person", "name": "Ivan Kotov", "sameAs": "https://orcid.org/0009-0009-6002-9845"},
                "codeRepository": PACKAGE,
                "license": LICENSE,
            },
        })
        if "numberOfItems" in node:
            node["numberOfItems"] = len(seq)

    s = patch_jsonld(s, "https://ivankotov.eu/publications/#works", update)
    write(path, s)


def patch_works_index() -> None:
    path = "works-index.json"
    obj = json.loads(read(path))
    wid = "cgdr-selected-process-r1-6an-v0-1-1"
    matches = [w for w in obj["works"] if w.get("id") == wid or w.get("primary_url") == CANON]
    if not matches:
        obj["works"].append({
            "id": wid,
            "title": TITLE,
            "type": "software",
            "role": "bounded selected-process source and synthetic evidence",
            "primary_url": CANON,
            "github": PACKAGE,
            "repository_path": PART + "doi-v0.1.1",
            "commit": AGI_COMMIT,
            "date": "2026-09-12",
            "version": "0.1.1",
            "version_doi": DOI,
            "doi_role": "version",
            "status": "published_software_and_internal_synthetic_evidence",
            "languages": ["en", "ru"],
            "license": "CGDR research and verification permission; preserved component licenses",
            "rights": LICENSE,
            "summary": "Unchanged current-AK source and technical report for the internally accepted 18-episode/21-checkpoint synthetic selected-process profile. Three expected local effects, zero promotions; raw diagnostic failures retained. Publication does not supply independent replication.",
            "archive_url": ZIP_URL,
            "archive_sha256": ZIP_SHA,
            "archive_bytes": 541373,
            "canonical_artifacts": [
                {"format": "PDF", "filename": PDF_NAME, "media_type": "application/pdf", "bytes": 89151, "sha256": PDF_SHA, "url": PDF_URL},
                {"format": "ZIP", "filename": ZIP_NAME, "media_type": "application/zip", "bytes": 541373, "sha256": ZIP_SHA, "url": ZIP_URL},
            ],
            "non_claims": [
                "no same-c identity or identity continuity",
                "no consciousness, personhood or lawful succession",
                "no B5 superiority or c-specific real effect",
                "no economic value measurement",
                "no general-stack conformance or live-deployment readiness",
                "no independent clean-host replication",
                "not a turnkey full AN execution/custody archive",
            ],
        })
    require(len(matches) <= 1, "Duplicate existing CGDR work records")
    write(path, json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def patch_sitemap() -> None:
    path = "sitemap.xml"
    s = read(path)
    if CANON not in s:
        require("</urlset>" in s, "Sitemap closing tag missing")
        s = s.replace("</urlset>", f"  <url><loc>{CANON}</loc><lastmod>2026-09-12</lastmod></url>\n</urlset>", 1)
    write(path, s)


def main() -> int:
    patch_work_page()
    patch_evidence()
    patch_publications()
    patch_works_index()
    patch_sitemap()
    for path in [
        "publications/cgdr-selected-process-r1-6an/index.html",
        "evidence/index.html",
        "publications/index.html",
        "works-index.json",
        "sitemap.xml",
    ]:
        require(DOI in read(path), f"DOI absent after patch: {path}")
    print("PASS_CGDR_DOI_SITE_SOURCE_PATCH")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
