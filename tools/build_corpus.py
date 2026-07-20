from __future__ import annotations

import html
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content" / "corpus"
SITE_URL = "https://ivankotov.eu"
SCHEMA_VERSION = "living-corpus.v62.public"
LAST_VERIFIED = "2026-07-19"

CONTENT_FILES = {
    "baseline": "baseline-b0.json",
    "current": "current-state.json",
    "protocols": "protocol-map.json",
    "open_problems": "open-problems.json",
    "failures": "failure-register.json",
    "changes": "delta-log.json",
    "sources": "canonical-sources.json",
    "copy": "entry-copy.json",
}

ENDPOINTS = {
    "index": ROOT / "corpus-index.json",
    "current": ROOT / "corpus-current.json",
    "protocols": ROOT / "corpus-protocol-map.json",
    "open_problems": ROOT / "corpus-open-problems.json",
    "failures": ROOT / "corpus-failures.json",
    "changes": ROOT / "corpus-changes.json",
    "sources": ROOT / "corpus-canonical-sources.json",
}

HTML_ROUTES = {
    "/start-here/": ROOT / "start-here" / "index.html",
    "/corpus/": ROOT / "corpus" / "index.html",
    "/corpus/protocol-map/": ROOT / "corpus" / "protocol-map" / "index.html",
    "/corpus/current-state/": ROOT / "corpus" / "current-state" / "index.html",
    "/corpus/open-problems/": ROOT / "corpus" / "open-problems" / "index.html",
    "/corpus/failures/": ROOT / "corpus" / "failures" / "index.html",
    "/corpus/changes/": ROOT / "corpus" / "changes" / "index.html",
}

SITEMAP_NEW_ROUTES = [
    "/corpus/",
    "/corpus/protocol-map/",
    "/corpus/current-state/",
    "/corpus/open-problems/",
    "/corpus/failures/",
    "/corpus/changes/",
]

STATUS_FIELDS = {
    "authority_state": {"canonical", "draft", "generated_routing_only", "supporting", "unknown"},
    "specification_state": {"absent", "defined", "proposed", "specified", "stable_specification"},
    "implementation_state": {"implemented", "none_identified", "partial"},
    "test_state": {"fixtures_present", "internally_tested", "test_design_only", "unknown"},
    "replication_state": {"none_identified", "unknown"},
    "validation_state": {"external_commentary_only", "none_identified"},
    "empirical_state": {"hypothesis", "internally_witnessed", "no_empirical_claim", "non_confirmed", "unknown"},
    "publication_state": {"internal_only", "repository_visible"},
    "disposition": {"active", "narrowed", "unresolved"},
}

OPEN_PRIORITIES = {"Critical", "High", "Medium"}
OPEN_STATES = {"OPEN", "PARTIALLY_BOUNDED", "PENDING_EVIDENCE", "PROPOSED_PATCH"}
FAILURE_RUNTIME_VALUES = {"no", "yes"}

FORBIDDEN_PUBLIC_PATTERNS = [
    r"C:\\",
    r"C:/",
    r"_incoming",
    r"_recovery",
    r"02_paid",
    r"paid_professional",
    r"C Enterprise",
    r"raw transcript",
    r"raw prompt",
    r"system prompt",
    r"developer prompt",
    r"private repo",
    r"secret key",
    r"OPENAI_API_KEY",
    r"sk-proj",
]


class BuildError(RuntimeError):
    pass


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def inline(value: object) -> str:
    parts = re.split(r"`([^`]+)`", str(value))
    return "".join(f"<code>{e(part)}</code>" if index % 2 else e(part) for index, part in enumerate(parts))


def label(value: object) -> str:
    text = str(value or "").replace("_", " ").replace("-", " ").strip()
    return text[:1].upper() + text[1:] if text else ""


def slug(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(value).lower()).strip("-")


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BuildError(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise BuildError(f"Invalid JSON in {path}: {exc}") from exc


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def json_text(data: Any) -> str:
    return json.dumps(data, ensure_ascii=True, indent=2, sort_keys=True) + "\n"


def iter_strings(value: Any, path: str = ""):
    if isinstance(value, dict):
        for key, nested in value.items():
            yield from iter_strings(nested, f"{path}/{key}")
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            yield from iter_strings(nested, f"{path}/{index}")
    elif isinstance(value, str):
        yield path, value


def scan_forbidden_public(name: str, text: str) -> None:
    for pattern in FORBIDDEN_PUBLIC_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            raise BuildError(f"Forbidden public token {pattern!r} found in {name}")


def load_data() -> dict[str, Any]:
    data = {key: read_json(CONTENT / filename) for key, filename in CONTENT_FILES.items()}
    validate_data(data)
    return data


def validate_status(value: str, allowed: set[str], context: str) -> None:
    if value not in allowed:
        raise BuildError(f"Unexpected status {value!r} in {context}")


def validate_data(data: dict[str, Any]) -> None:
    baseline = data["baseline"]
    current = data["current"]
    protocols = data["protocols"]
    failures = data["failures"]
    open_problems = data["open_problems"]

    counts = baseline.get("source_record_counts", {})
    expected_counts = {
        "step2_artifacts": 60,
        "step2_families": 17,
        "step3_protocol_families": 17,
        "step3_failure_nonconfirmation_records": 18,
        "step3_open_problems": 24,
    }
    for key, expected in expected_counts.items():
        if counts.get(key) != expected:
            raise BuildError(f"Baseline count mismatch for {key}: {counts.get(key)!r}")

    summary = current.get("summary", {})
    if summary.get("artifact_count") != 60 or summary.get("family_count") != 17:
        raise BuildError("Current-state summary must report 60 artifacts and 17 families")
    if summary.get("independent_reproduction") != "not_identified":
        raise BuildError("Independent reproduction must remain not_identified")
    if summary.get("external_validation") != "not_identified":
        raise BuildError("External validation must remain not_identified")
    if summary.get("strict_matched_profile_control") != "not_identified":
        raise BuildError("Strict matched profile-control must remain not_identified")
    if summary.get("adequately_evidenced_runtime_failure_events") != 0:
        raise BuildError("Runtime failure event count must remain 0")

    artifacts = current.get("artifacts", [])
    families = current.get("families", [])
    if len(artifacts) != 60 or len(families) != 17:
        raise BuildError("Current-state artifact/family list length mismatch")
    for artifact in artifacts:
        for field, allowed in STATUS_FIELDS.items():
            validate_status(artifact.get(field, ""), allowed, f"artifact {artifact.get('artifact_id')} field {field}")
    if Counter(row["family_id"] for row in artifacts) and sorted({row["family_id"] for row in artifacts}) != [f"F{i:02d}" for i in range(1, 18)]:
        raise BuildError("Expected family ids F01 through F17")

    if protocols.get("record_count") != 17 or len(protocols.get("protocols", [])) != 17:
        raise BuildError("Protocol map must contain 17 records")

    failure_records = failures.get("records", [])
    if failures.get("record_count") != 18 or len(failure_records) != 18:
        raise BuildError("Failure register must contain 18 records")
    if failures.get("adequately_evidenced_runtime_failure_events") != 0:
        raise BuildError("Failure register runtime event count must be 0")
    for record in failure_records:
        validate_status(record.get("is_observed_runtime_failure", ""), FAILURE_RUNTIME_VALUES, record.get("record_id", "failure"))
    if Counter(record["is_observed_runtime_failure"] for record in failure_records) != Counter({"no": 18}):
        raise BuildError("All failure records must remain non-runtime-failure records")

    problem_records = open_problems.get("problems", [])
    if open_problems.get("record_count") != 24 or len(problem_records) != 24:
        raise BuildError("Open-problems register must contain 24 records")
    if open_problems.get("severity_counts") != {"Critical": 10, "High": 13, "Medium": 1}:
        raise BuildError("Open-problem severity distribution mismatch")
    for record in problem_records:
        validate_status(record.get("priority", ""), OPEN_PRIORITIES, record.get("problem_id", "open problem"))
        validate_status(record.get("state", ""), OPEN_STATES, record.get("problem_id", "open problem"))

    for name, payload in data.items():
        for path, value in iter_strings(payload):
            scan_forbidden_public(f"content:{name}{path}", value)


def source_controls(data: dict[str, Any]) -> list[str]:
    return data["baseline"].get("source_controls", [])


def endpoint_envelope(kind: str, route: str, data: dict[str, Any], payload: Any) -> dict[str, Any]:
    payload_verified = payload.get("last_verified", LAST_VERIFIED) if isinstance(payload, dict) else LAST_VERIFIED
    return {
        "schema_version": SCHEMA_VERSION,
        "endpoint": route,
        "generated_by": "tools/build_corpus.py",
        "site": SITE_URL + "/",
        "baseline_id": data["baseline"].get("baseline_id", "B0"),
        "baseline_source_snapshot": data["baseline"].get("baseline_source_snapshot", "2026-07-08"),
        "last_verified": payload_verified,
        "kind": kind,
        "claim_boundary": data["baseline"].get("claim_boundary", ""),
        "source_controls": source_controls(data),
        "data": payload,
    }


def endpoint_index(data: dict[str, Any]) -> dict[str, Any]:
    copy = data["copy"]
    current = data["current"]
    return {
        "document_id": "living-corpus-public-index-v62",
        "routes": copy["routes"],
        "endpoints": [
            {"title": "Index", "url": "/corpus-index.json"},
            {"title": "Current state", "url": "/corpus-current.json"},
            {"title": "Protocol map", "url": "/corpus-protocol-map.json"},
            {"title": "Open problems", "url": "/corpus-open-problems.json"},
            {"title": "Failures", "url": "/corpus-failures.json"},
            {"title": "Changes", "url": "/corpus-changes.json"},
            {"title": "Canonical sources", "url": "/corpus-canonical-sources.json"},
        ],
        "counts": {
            "artifacts": current["summary"]["artifact_count"],
            "protocol_families": data["protocols"]["record_count"],
            "open_problems": data["open_problems"]["record_count"],
            "failure_nonconfirmation_records": data["failures"]["record_count"],
            "adequately_evidenced_runtime_failure_events": data["failures"]["adequately_evidenced_runtime_failure_events"],
        },
    }


def build_endpoints(data: dict[str, Any]) -> dict[Path, str]:
    payloads = {
        ENDPOINTS["index"]: endpoint_envelope("index", "/corpus-index.json", data, endpoint_index(data)),
        ENDPOINTS["current"]: endpoint_envelope("current_state", "/corpus-current.json", data, data["current"]),
        ENDPOINTS["protocols"]: endpoint_envelope("protocol_map", "/corpus-protocol-map.json", data, data["protocols"]),
        ENDPOINTS["open_problems"]: endpoint_envelope("open_problems", "/corpus-open-problems.json", data, data["open_problems"]),
        ENDPOINTS["failures"]: endpoint_envelope("failure_register", "/corpus-failures.json", data, data["failures"]),
        ENDPOINTS["changes"]: endpoint_envelope("change_log", "/corpus-changes.json", data, data["changes"]),
        ENDPOINTS["sources"]: endpoint_envelope("canonical_sources", "/corpus-canonical-sources.json", data, data["sources"]),
    }
    return {path: json_text(payload) for path, payload in payloads.items()}


def breadcrumb_json(title: str, route: str) -> str:
    parts = [part for part in route.strip("/").split("/") if part]
    items = [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
    ]
    path = ""
    for index, part in enumerate(parts, start=2):
        path += f"/{part}"
        items.append({"@type": "ListItem", "position": index, "name": label(part), "item": SITE_URL + path + "/"})
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": SITE_URL + route + "#page",
                "url": SITE_URL + route,
                "name": title,
            },
            {"@type": "BreadcrumbList", "@id": SITE_URL + route + "#breadcrumb", "itemListElement": items},
        ],
    }
    return json.dumps(graph, ensure_ascii=True, indent=2)


def css_href(route: str) -> str:
    depth = len([part for part in route.strip("/").split("/") if part])
    return "../" * depth + "styles.css"


def global_nav(route: str) -> str:
    nav = [
        ("/", "Home"),
        ("/start-here/", "Start here"),
        ("/diary/", "Diary"),
        ("/topics/", "Topics"),
        ("/library/", "Library"),
        ("/services/", "Services"),
        ("/about/", "About"),
        ("/contact/", "Contact"),
    ]
    links = []
    for href, text in nav:
        current = ' aria-current="page"' if href == route else ""
        links.append(f'<a href="{href}"{current}>{e(text)}</a>')
    return "\n        ".join(links)


def local_nav(current_route: str) -> str:
    links = [
        ("/corpus/", "Overview"),
        ("/corpus/#architecture", "Architecture"),
        ("/corpus/protocol-map/", "Protocol map"),
        ("/corpus/current-state/", "Current state"),
        ("/corpus/open-problems/", "Open problems"),
        ("/corpus/failures/", "Failures"),
        ("/evidence/", "Evidence"),
        ("/corpus/changes/", "Changes"),
        ("/glossary/", "Glossary"),
    ]
    items = []
    for href, text in links:
        current = ' aria-current="page"' if href == current_route else ""
        items.append(f'<a href="{href}"{current}>{e(text)}</a>')
    return '<nav class="corpus-local-nav" aria-label="Living corpus">\n        ' + "\n        ".join(items) + "\n      </nav>"


def page_shell(route: str, title: str, description: str, body: str) -> str:
    head_json = breadcrumb_json(title, route)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <link rel="canonical" href="{SITE_URL}{route}">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE_URL}{route}">
  <script type="application/ld+json">
{head_json}
  </script>
  <link rel="stylesheet" href="{css_href(route)}">
</head>
<body class="corpus-layer">
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="site-shell">
    <header class="site-header">
      <a class="brand" href="/">
        <span class="brand-name">Ivan Kotov</span>
        <span class="brand-role">AI Systems Architect</span>
      </a>
      <nav class="site-nav" aria-label="Primary">
        {global_nav(route)}
      </nav>
    </header>

    <main id="main" tabindex="-1">
{body}
    </main>

    <footer class="site-footer">
      <p>Primary domain: <span>ivankotov.eu</span></p>
    </footer>
  </div>
</body>
</html>
"""


def section_head(label_text: str, title: str, lead: str = "") -> str:
    lead_html = f'\n          <p class="section-intro">{e(lead)}</p>' if lead else ""
    return f"""        <div class="section-head">
          <p class="section-label">{e(label_text)}</p>
          <h2>{e(title)}</h2>{lead_html}
        </div>"""


def metric_grid(metrics: list[tuple[str, object, str]]) -> str:
    cards = []
    for title, value, note in metrics:
        cards.append(
            f"""          <article class="corpus-metric">
            <strong>{e(value)}</strong>
            <span>{e(title)}</span>
            <p>{e(note)}</p>
          </article>"""
        )
    return '<div class="corpus-metric-grid">\n' + "\n".join(cards) + "\n        </div>"


def route_cards(routes: list[dict[str, str]]) -> str:
    cards = []
    for item in routes:
        cards.append(
            f"""          <article class="card corpus-route-card">
            <h3>{e(item["title"])}</h3>
            <p>{e(item["description"])}</p>
            <div class="section-links"><a href="{e(item["url"])}">Open</a></div>
          </article>"""
        )
    return '<div class="card-grid corpus-card-grid">\n' + "\n".join(cards) + "\n        </div>"


def audience_cards(routes: list[dict[str, Any]]) -> str:
    cards = []
    for item in routes:
        note = f'\n            <p class="corpus-card-note">{inline(item["note"])}</p>' if item.get("note") else ""
        links = [f'<a href="{e(item["url"])}">Start</a>']
        for link in item.get("links", []):
            links.append(f'<a href="{e(link["url"])}">{e(link["label"])}</a>')
        link_html = " ".join(links)
        cards.append(
            f"""          <article class="card corpus-route-card">
            <h3>{e(item["audience"])}</h3>
            <p>{e(item["route"])}</p>{note}
            <div class="section-links">{link_html}</div>
          </article>"""
        )
    return '<div class="card-grid corpus-card-grid">\n' + "\n".join(cards) + "\n        </div>"


def instrument_participant_callout(callout: dict[str, Any]) -> str:
    body = "\n".join(f"              <p>{inline(paragraph)}</p>" for paragraph in callout.get("body", []))
    action = callout.get("action") or {}
    action_html = ""
    if action.get("url") and action.get("label"):
        action_html = f'\n              <div class="section-links"><a href="{e(action["url"])}">{e(action["label"])}</a></div>'
    return f"""          <aside class="instrument-callout" aria-labelledby="agent-c-callout-title">
            <p class="section-label">{e(callout.get("eyebrow", "Distinction"))}</p>
            <h3 id="agent-c-callout-title">{e(callout.get("title", ""))}</h3>
            <p><strong>{e(callout.get("primary_sentence", ""))}</strong></p>
{body}{action_html}
          </aside>"""


def self_check_items(items: list[Any]) -> str:
    rendered = []
    for item in items:
        if isinstance(item, dict):
            links = " ".join(
                f'<a href="{e(link["url"])}">{e(link["label"])}</a>' for link in item.get("hint_links", [])
            )
            hints = f'\n              <div class="self-check-hints">{links}</div>' if links else ""
            rendered.append(f"            <li>{inline(item.get('question', ''))}{hints}</li>")
        else:
            rendered.append(f"            <li>{e(item)}</li>")
    return "\n".join(rendered)


def status_chips(items: list[tuple[str, str]]) -> str:
    chips = [f'<li><span>{e(key)}</span><strong>{e(value)}</strong></li>' for key, value in items]
    return '<ul class="corpus-chip-list">\n          ' + "\n          ".join(chips) + "\n        </ul>"


def architecture_svg() -> str:
    return """        <figure class="corpus-diagram">
          <svg role="img" aria-labelledby="corpus-diagram-title corpus-diagram-desc" viewBox="0 0 920 500" preserveAspectRatio="xMidYMid meet">
            <title id="corpus-diagram-title">Living corpus architecture from rule to consequence</title>
            <desc id="corpus-diagram-desc">Models, agents, memory, and tools belong to the governed substrate `b`. They may be replaced or delegated. The continuing participant represented by `c` carries the history of commitments, authority boundaries, witness, and consequence under governed binding. The diagram labels `c` as a continuity-bearing participant locus.</desc>
            <rect x="24" y="24" width="872" height="452" rx="18" class="diagram-bg" />
            <text x="460" y="64" text-anchor="middle" class="diagram-title">No status elevation without admissible evidence</text>
            <rect x="58" y="104" width="210" height="110" rx="14" class="diagram-box" />
            <text x="163" y="138" text-anchor="middle" class="diagram-label">a</text>
            <text x="163" y="166" text-anchor="middle" class="diagram-copy">accountable human anchor</text>
            <text x="163" y="190" text-anchor="middle" class="diagram-copy">permission and responsibility</text>
            <rect x="355" y="104" width="210" height="110" rx="14" class="diagram-box" />
            <text x="460" y="138" text-anchor="middle" class="diagram-label">b</text>
            <text x="460" y="166" text-anchor="middle" class="diagram-copy">bounded substrate</text>
            <text x="460" y="188" text-anchor="middle" class="diagram-copy">Agents / tools</text>
            <text x="460" y="209" text-anchor="middle" class="diagram-copy">replaceable bounded instruments</text>
            <text x="312" y="166" text-anchor="middle" class="diagram-plus">+</text>
            <rect x="652" y="104" width="210" height="110" rx="14" class="diagram-box diagram-box-strong" />
            <text x="757" y="138" text-anchor="middle" class="diagram-label">c</text>
            <text x="757" y="166" text-anchor="middle" class="diagram-copy">governed candidate layer</text>
            <text x="757" y="188" text-anchor="middle" class="diagram-copy">continuity-bearing</text>
            <text x="757" y="209" text-anchor="middle" class="diagram-copy">participant locus</text>
            <path d="M163 230 L163 278 L300 278" class="diagram-line" />
            <path d="M460 230 L460 278" class="diagram-line" />
            <path d="M757 230 L757 278 L620 278" class="diagram-line" />
            <rect x="84" y="302" width="210" height="96" rx="14" class="diagram-box diagram-muted" />
            <text x="189" y="334" text-anchor="middle" class="diagram-label">L3</text>
            <text x="189" y="360" text-anchor="middle" class="diagram-copy">rules and admissibility</text>
            <rect x="355" y="302" width="210" height="96" rx="14" class="diagram-box diagram-muted" />
            <text x="460" y="334" text-anchor="middle" class="diagram-label">Witness</text>
            <text x="460" y="360" text-anchor="middle" class="diagram-copy">record of transition</text>
            <rect x="626" y="302" width="210" height="96" rx="14" class="diagram-box diagram-muted" />
            <text x="731" y="334" text-anchor="middle" class="diagram-label">L4</text>
            <text x="731" y="360" text-anchor="middle" class="diagram-copy">real consequence boundary</text>
            <path d="M294 350 L355 350" class="diagram-line" />
            <path d="M565 350 L626 350" class="diagram-line" />
            <text x="460" y="444" text-anchor="middle" class="diagram-foot">Status changes only through evidence, transition conditions, and reviewable records.</text>
          </svg>
        </figure>"""


def render_start_here(data: dict[str, Any]) -> str:
    copy = data["copy"]
    current = data["current"]
    protocols = data["protocols"]["protocols"]
    problems = data["open_problems"]["problems"]
    changes = data["changes"]["changes"]
    sources = data["sources"]["sources"]
    intro = "\n".join(f"          <p>{e(p)}</p>" for p in copy["overview_paragraphs"])
    metrics = metric_grid([
        ("B0 artifact rows", current["summary"]["artifact_count"], "Verified Step 2 classification."),
        ("Protocol families", data["protocols"]["record_count"], "Verified Step 3 protocol map."),
        ("Open problems", data["open_problems"]["record_count"], "Critical, High, and Medium records."),
        ("Runtime failure events", data["failures"]["adequately_evidenced_runtime_failure_events"], "Adequately evidenced events in the selected B0 set."),
    ])
    protocol_preview = "\n".join(
        f"""          <article class="card corpus-mini-card">
            <h3>{e(item["protocol_map_id"])} - {e(item["family_name"])}</h3>
            <p>{e(item["controlled_status_transition"])}</p>
          </article>"""
        for item in protocols[:6]
    )
    problem_preview = "\n".join(
        f"""          <li><a href="/corpus/open-problems/#{e(slug(item["problem_id"]))}">{e(item["problem_id"])}: {e(item["title"])}</a> <span>{e(item["priority"])}</span></li>"""
        for item in problems[:8]
    )
    change_items = "\n".join(
        f"""          <article class="card corpus-mini-card">
            <h3>{e(item["date"])} - {e(item["title"])}</h3>
            <p>{e(item["claim_effect"])}</p>
          </article>"""
        for item in changes
    )
    source_links = "\n".join(
        f"""          <li><a href="{e(item["public_url"])}">{e(item["title"])}</a> - {e(item["role"])}</li>"""
        for item in sources[:10]
    )
    callout = instrument_participant_callout(copy["instrument_participant_callout"])
    self_check = self_check_items(copy["self_check"])
    body = f"""      <section class="hero corpus-hero">
        <p class="eyebrow">{e(copy["hero_eyebrow"])}</p>
        <h1>{e(copy["start_here_title"])}</h1>
        <p class="lead page-lead">{e(copy["hero_lead"])}</p>
        {status_chips([("Baseline", "B0"), ("Last verified", LAST_VERIFIED), ("Deltas through", data["changes"]["deltas_applied_through"])])}
        {local_nav("/start-here/")}
      </section>

      <section class="section" id="architecture-in-90-seconds">
{section_head("Architecture", "Architecture in 90 seconds")}
        <div class="prose">
{intro}
          <details class="corpus-definition">
            <summary>Term boundary</summary>
            <p><strong>L3</strong> means rules, classifications, permission paths, and admissibility controls. <strong>L4</strong> means physical, temporal, energetic, operational, and irreversible consequence. <strong>Witness</strong> means the record that connects an L3 decision to an L4 result. A capable model, agent harness, memory store, or cloud assistant is not automatically <code>c</code>.</p>
          </details>
{callout}
        </div>
      </section>

      <section class="section" id="architecture-diagram">
{section_head("Diagram", "Architecture diagram")}
{architecture_svg()}
      </section>

      <section class="section" id="rule-to-consequence">
{section_head("Bridge", "From rule to consequence", "The corpus treats governance as a transition chain, not as a slogan.")}
        <div class="card-grid corpus-card-grid">
          <article class="card"><h3>Rule</h3><p>A status claim starts as a bounded statement with a declared class and evidence requirement.</p></article>
          <article class="card"><h3>Witness</h3><p>A transition needs a reviewable record of authority, scope, action, result, and limitation.</p></article>
          <article class="card"><h3>Consequence</h3><p>The result must survive physical, operational, and custody constraints before stronger wording is allowed.</p></article>
        </div>
      </section>

      <section class="section" id="current-programme-state">
{section_head("Status", "Current programme state")}
{metrics}
        <div class="prose">
          <p>Independent reproduction, external validation, and strict matched profile-control are recorded as not identified. That boundary is part of the status, not a footnote.</p>
        </div>
      </section>

      <section class="section" id="choose-depth">
{section_head("Depth", "Choose your depth")}
{route_cards(copy["routes"])}
      </section>

      <section class="section" id="choose-route">
{section_head("Audience", "Choose your route")}
{audience_cards(copy["audience_routes"])}
      </section>

      <section class="section" id="protocol-map-preview">
{section_head("Protocols", "Protocol-map preview", "Six examples from the 17 verified protocol-family records.")}
        <div class="card-grid corpus-card-grid">
{protocol_preview}
        </div>
        <div class="section-links"><a href="/corpus/protocol-map/">Open the full protocol map</a></div>
      </section>

      <section class="section" id="changes-since-b0">
{section_head("Deltas", "Changes since B0")}
        <div class="card-grid corpus-card-grid">
{change_items}
        </div>
      </section>

      <section class="section" id="unresolved">
{section_head("Problems", "What remains unresolved")}
        <ul class="corpus-problem-list">
{problem_preview}
        </ul>
        <div class="section-links"><a href="/corpus/open-problems/">Open all 24 open problems</a></div>
      </section>

      <section class="section" id="canonical-sources">
{section_head("Sources", "Canonical sources")}
        <ul class="bullet-list corpus-source-list">
{source_links}
        </ul>
        <details class="corpus-definition" id="self-check">
          <summary>Optional self-check</summary>
          <ol class="bullet-list">
{self_check}
          </ol>
        </details>
      </section>

      <section class="section corpus-boundary" id="claim-boundary">
{section_head("Boundary", "Claim boundary")}
        <div class="prose">
          <p>{e(data["baseline"]["claim_boundary"])}</p>
          <p>It is a public navigation and status-control layer over verified B0 consolidation registers. It does not modify the frozen source packages or the reference extraction.</p>
        </div>
      </section>"""
    return page_shell("/start-here/", "Start here - Living Corpus Entry Layer | Ivan Kotov", copy["start_here_description"], body)


def render_corpus_overview(data: dict[str, Any]) -> str:
    current = data["current"]
    families = current["families"]
    endpoints = endpoint_index(data)["endpoints"]
    family_cards = "\n".join(
        f"""          <article class="card corpus-mini-card">
            <h3>{e(item["family_id"])} - {e(item["title"])}</h3>
            <p>{e(item["claim_ceiling"])}</p>
          </article>"""
        for item in families[:6]
    )
    endpoint_links = "\n".join(f'          <a href="{e(item["url"])}">{e(item["title"])}</a>' for item in endpoints)
    body = f"""      <section class="hero corpus-hero">
        <p class="eyebrow">Living corpus</p>
        <h1>Corpus overview</h1>
        <p class="lead page-lead">A public control panel for B0 status, source boundaries, protocol families, open problems, failure records, and non-claims.</p>
        {local_nav("/corpus/")}
      </section>

      <section class="section" id="principle">
{section_head("Principle", "Core principle")}
        <div class="prose">
          <p>No claim, state, role, authority, continuity status, memory status, operational outcome, or validation status may be promoted to a stronger class without admissible evidence, explicit transition conditions, and a witnessable record.</p>
          <p>This page translates that rule into a reader-facing map. It is not a new protocol family and it does not raise any source status.</p>
        </div>
      </section>

      <section class="section" id="architecture">
{section_head("Architecture", "Architecture")}
{architecture_svg()}
        <div class="prose">
          <p>The architecture separates the accountable anchor, bounded substrate, governed candidate layer, procedural rules, witness record, and real-world consequence boundary.</p>
        </div>
      </section>

      <section class="section" id="status-snapshot">
{section_head("Status", "Status snapshot")}
{metric_grid([
        ("Artifacts", current["summary"]["artifact_count"], "Step 2 load-bearing classification."),
        ("Families", current["summary"]["family_count"], "Family ids F01 through F17."),
        ("Protocol records", data["protocols"]["record_count"], "Step 3 protocol map."),
        ("Open problems", data["open_problems"]["record_count"], "10 Critical, 13 High, 1 Medium."),
    ])}
      </section>

      <section class="section" id="protocol-families">
{section_head("Families", "Protocol families")}
        <div class="card-grid corpus-card-grid">
{family_cards}
        </div>
        <div class="section-links"><a href="/corpus/protocol-map/">Open all 17 families</a></div>
      </section>

      <section class="section" id="limitations">
{section_head("Limits", "Current limitations")}
        <div class="prose">
          <p>Independent reproduction is not identified. External validation is not identified. Strict matched profile-control is not identified. These are explicit status controls derived from the verified registers.</p>
        </div>
      </section>

      <section class="section" id="data">
{section_head("Receipts", "Public JSON endpoints")}
        <div class="section-links corpus-endpoint-links">
{endpoint_links}
        </div>
      </section>

      <section class="section corpus-boundary" id="claim-boundary">
{section_head("Boundary", "Claim boundary")}
        <p>{e(data["baseline"]["claim_boundary"])}</p>
      </section>"""
    return page_shell("/corpus/", "Living Corpus Overview | Ivan Kotov", "Reader-facing overview of the living corpus status layer.", body)


def source_ref_text(refs: list[dict[str, str]]) -> str:
    if not refs:
        return "No artifact hash refs listed in public projection."
    joined = ", ".join(f'{ref.get("artifact_id", "")} ({ref.get("sha256", "")[:12]})' for ref in refs)
    return joined


def filter_controls(kind: str, controls: list[tuple[str, str, list[str]]]) -> str:
    selects = []
    for field, title, values in controls:
        options = "\n".join(f'              <option value="{e(value)}">{e(label(value))}</option>' for value in values)
        selects.append(
            f"""          <label>
            <span>{e(title)}</span>
            <select data-filter-select="{e(field)}">
              <option value="">All</option>
{options}
            </select>
          </label>"""
        )
    return f"""        <div class="corpus-filter-bar" data-corpus-filter-root="{e(kind)}">
          <label class="corpus-search">
            <span>Search</span>
            <input type="search" data-filter-search placeholder="Filter records">
          </label>
{chr(10).join(selects)}
          <p class="corpus-filter-count" data-filter-count></p>
          <p class="corpus-filter-empty" data-filter-empty hidden>No matching records.</p>
        </div>"""


def filter_script() -> str:
    return """      <script>
        (function () {
          var roots = document.querySelectorAll("[data-corpus-filter-root]");
          roots.forEach(function (root) {
            var search = root.querySelector("[data-filter-search]");
            var selects = Array.prototype.slice.call(root.querySelectorAll("[data-filter-select]"));
            var list = root.nextElementSibling;
            var cards = list ? Array.prototype.slice.call(list.querySelectorAll("[data-record-card]")) : [];
            var count = root.querySelector("[data-filter-count]");
            var empty = root.querySelector("[data-filter-empty]");
            function norm(value) {
              return String(value || "").toLowerCase();
            }
            function apply() {
              var query = norm(search && search.value);
              var shown = 0;
              cards.forEach(function (card) {
                var ok = true;
                if (query && norm(card.textContent).indexOf(query) === -1) {
                  ok = false;
                }
                selects.forEach(function (select) {
                  var wanted = select.value;
                  var field = select.getAttribute("data-filter-select");
                  if (wanted && card.getAttribute("data-" + field) !== wanted) {
                    ok = false;
                  }
                });
                card.hidden = !ok;
                if (ok) {
                  shown += 1;
                }
              });
              if (count) {
                count.textContent = shown + " shown";
              }
              if (empty) {
                empty.hidden = shown !== 0;
              }
            }
            if (search) {
              search.addEventListener("input", apply);
            }
            selects.forEach(function (select) {
              select.addEventListener("change", apply);
            });
            apply();
          });
        }());
      </script>"""


def render_protocols(data: dict[str, Any]) -> str:
    records = data["protocols"]["protocols"]
    cards = []
    for item in records:
        cards.append(
            f"""          <article class="card corpus-record-card" id="{e(slug(item["protocol_map_id"]))}" data-record-card data-family="{e(item["family_id"])}">
            <div class="corpus-record-head">
              <p class="section-label">{e(item["protocol_map_id"])} / {e(item["family_id"])}</p>
              <h3>{e(item["family_name"])}</h3>
            </div>
            <dl class="corpus-record-grid">
              <div><dt>Controlled transition</dt><dd>{e(item["controlled_status_transition"])}</dd></div>
              <div><dt>Laundering risk blocked</dt><dd>{e(item["laundering_risk_blocked"])}</dd></div>
              <div><dt>Evidence required</dt><dd>{e(item["admissible_evidence_required"])}</dd></div>
              <div><dt>Status vector</dt><dd>{e(item["current_status_vector"])}</dd></div>
              <div><dt>Current limitation</dt><dd>{e(item["current_limitation"])}</dd></div>
              <div><dt>Claim ceiling</dt><dd>{e(item["claim_ceiling"])}</dd></div>
              <div><dt>Public anchor</dt><dd><a href="{e(item["canonical_public_anchor"])}">{e(item["canonical_public_anchor"])}</a></dd></div>
              <div><dt>Artifact refs</dt><dd>{e(source_ref_text(item.get("source_refs", [])))}</dd></div>
            </dl>
          </article>"""
        )
    controls = filter_controls("protocols", [("family", "Family", [f"F{i:02d}" for i in range(1, 18)])])
    body = f"""      <section class="hero corpus-hero">
        <p class="eyebrow">Living corpus</p>
        <h1>Protocol map</h1>
        <p class="lead page-lead">Seventeen verified protocol-family records showing permitted transitions, laundering risks, evidence requirements, limitations, and claim ceilings.</p>
        {local_nav("/corpus/protocol-map/")}
      </section>

      <section class="section">
{section_head("Verified Step 3", "Protocol-family records", "Filterable, source-sanitized projection of the verified protocol map.")}
{filter_controls("protocols", [("family", "Family", [f"F{i:02d}" for i in range(1, 18)])])}
        <div class="corpus-record-list">
{chr(10).join(cards)}
        </div>
      </section>
{filter_script()}"""
    return page_shell("/corpus/protocol-map/", "Living Corpus Protocol Map | Ivan Kotov", "Verified protocol-family map for the living corpus.", body)


def render_current_state(data: dict[str, Any]) -> str:
    current = data["current"]
    families = current["families"]
    surfaces = current["implementation_surfaces"]
    counts_html = []
    for field, counts in current["status_counts"].items():
        chips = " ".join(f'<span class="corpus-pill">{e(label(key))}: {e(value)}</span>' for key, value in counts.items())
        counts_html.append(f"""          <article class="card corpus-mini-card"><h3>{e(label(field))}</h3><p>{chips}</p></article>""")
    family_details = []
    for item in families:
        family_details.append(
            f"""          <details class="corpus-detail-card">
            <summary>{e(item["family_id"])} - {e(item["title"])}</summary>
            <p><strong>Claim ceiling:</strong> {e(item["claim_ceiling"])}</p>
            <p><strong>Current limitation:</strong> {e(item["current_limitation"])}</p>
            <p><strong>Artifacts:</strong> {e(", ".join(item["artifact_ids"]))}</p>
            <p><a href="{e(item["public_anchor"])}">Public anchor</a></p>
          </details>"""
        )
    surface_cards = []
    for item in surfaces:
        surface_cards.append(
            f"""          <article class="card corpus-mini-card">
            <p class="section-label">{e(item["artifact_id"])} / {e(item["family_id"])}</p>
            <h3>{e(label(item["artifact_role"]))}</h3>
            <p>{e(item["permitted_wording"])}</p>
            <p><span class="corpus-pill">Implementation: {e(label(item["implementation_state"]))}</span> <span class="corpus-pill">Test: {e(label(item["test_state"]))}</span></p>
          </article>"""
        )
    body = f"""      <section class="hero corpus-hero">
        <p class="eyebrow">Living corpus</p>
        <h1>Current state</h1>
        <p class="lead page-lead">B0 status matrix projection for 60 load-bearing artifacts across 17 families, with current limitations and deltas applied through {LAST_VERIFIED}.</p>
        {local_nav("/corpus/current-state/")}
      </section>

      <section class="section" id="summary">
{section_head("Status", "Summary")}
{metric_grid([
        ("Artifacts", current["summary"]["artifact_count"], "Verified Step 2 rows."),
        ("Families", current["summary"]["family_count"], "Family ids F01 through F17."),
        ("Independent reproduction", label(current["summary"]["independent_reproduction"]), "No stronger status is recorded."),
        ("External validation", label(current["summary"]["external_validation"]), "No stronger status is recorded."),
    ])}
      </section>

      <section class="section" id="status-counts">
{section_head("Matrix", "Status counts")}
        <div class="card-grid corpus-card-grid">
{chr(10).join(counts_html)}
        </div>
      </section>

      <section class="section" id="families">
{section_head("Families", "Family-level limitations")}
        <div class="corpus-detail-list">
{chr(10).join(family_details)}
        </div>
      </section>

      <section class="section" id="implementation-surfaces">
{section_head("Implementation", "Implementation and test surfaces", "Rows with implemented, partial, internally tested, fixtures-present, or test-design-only status.")}
        <div class="card-grid corpus-card-grid">
{chr(10).join(surface_cards)}
        </div>
      </section>

      <section class="section corpus-boundary" id="claim-boundary">
{section_head("Boundary", "No status elevation")}
        <p>{e(data["baseline"]["claim_boundary"])}</p>
      </section>"""
    return page_shell("/corpus/current-state/", "Living Corpus Current State | Ivan Kotov", "Current B0 status matrix projection for the living corpus.", body)


def render_open_problems(data: dict[str, Any]) -> str:
    records = data["open_problems"]["problems"]
    cards = []
    for item in records:
        cards.append(
            f"""          <article class="card corpus-record-card" id="{e(slug(item["problem_id"]))}" data-record-card data-priority="{e(item["priority"])}" data-state="{e(item["state"])}" data-effect="{e(item["drafting_effect"])}">
            <div class="corpus-record-head">
              <p class="section-label">{e(item["problem_id"])} / {e(item["priority"])} / {e(label(item["state"]))}</p>
              <h3>{e(item["title"])}</h3>
            </div>
            <dl class="corpus-record-grid">
              <div><dt>Drafting effect</dt><dd>{e(label(item["drafting_effect"]))}</dd></div>
              <div><dt>Problem statement</dt><dd>{e(item["problem_statement"])}</dd></div>
              <div><dt>Why load-bearing</dt><dd>{e(item["why_load_bearing"])}</dd></div>
              <div><dt>Current handling</dt><dd>{e(item["current_handling"])}</dd></div>
              <div><dt>Required next evidence or decision</dt><dd>{e(item["required_next_evidence_or_decision"])}</dd></div>
              <div><dt>Claim ceiling</dt><dd>{e(item["current_claim_ceiling"])}</dd></div>
              <div><dt>Artifact refs</dt><dd>{e(source_ref_text(item.get("source_refs", [])))}</dd></div>
            </dl>
          </article>"""
        )
    priorities = ["Critical", "High", "Medium"]
    states = sorted({item["state"] for item in records})
    effects = sorted({item["drafting_effect"] for item in records})
    body = f"""      <section class="hero corpus-hero">
        <p class="eyebrow">Living corpus</p>
        <h1>Open problems</h1>
        <p class="lead page-lead">Twenty-four verified open problems: 10 Critical, 13 High, and 1 Medium. These are blockers or disclosure requirements, not hidden successes.</p>
        {local_nav("/corpus/open-problems/")}
      </section>

      <section class="section">
{section_head("Verified Step 3", "Open-problem register")}
{filter_controls("open-problems", [("priority", "Priority", priorities), ("state", "State", states), ("effect", "Drafting effect", effects)])}
        <div class="corpus-record-list">
{chr(10).join(cards)}
        </div>
      </section>
{filter_script()}"""
    return page_shell("/corpus/open-problems/", "Living Corpus Open Problems | Ivan Kotov", "Verified open-problem register for the living corpus.", body)


def render_failures(data: dict[str, Any]) -> str:
    records = data["failures"]["records"]
    cards = []
    for item in records:
        cards.append(
            f"""          <article class="card corpus-record-card" id="{e(slug(item["record_id"]))}" data-record-card data-class="{e(item["failure_or_nonconfirmation_class"])}" data-scope="{e(item["scope"])}">
            <div class="corpus-record-head">
              <p class="section-label">{e(item["record_id"])} / {e(label(item["failure_or_nonconfirmation_class"]))}</p>
              <h3>{e(item["scope"])}</h3>
            </div>
            <dl class="corpus-record-grid">
              <div><dt>Hypothesis</dt><dd>{e(item["hypothesis"])}</dd></div>
              <div><dt>Expected result</dt><dd>{e(item["expected_result"])}</dd></div>
              <div><dt>Observed result</dt><dd>{e(item["observed_result"])}</dd></div>
              <div><dt>Impact on claim</dt><dd>{e(item["impact_on_claim"])}</dd></div>
              <div><dt>Correction or required action</dt><dd>{e(item["correction_or_required_action"])}</dd></div>
              <div><dt>Residual uncertainty</dt><dd>{e(item["residual_uncertainty"])}</dd></div>
              <div><dt>Claim disposition</dt><dd>{e(item["claim_disposition"])}</dd></div>
              <div><dt>Observed runtime failure event</dt><dd>{e(label(item["is_observed_runtime_failure"]))}</dd></div>
              <div><dt>Artifact refs</dt><dd>{e(source_ref_text(item.get("source_refs", [])))}</dd></div>
            </dl>
          </article>"""
        )
    classes = sorted({item["failure_or_nonconfirmation_class"] for item in records})
    scopes = sorted({item["scope"] for item in records})
    body = f"""      <section class="hero corpus-hero">
        <p class="eyebrow">Living corpus</p>
        <h1>Failures and non-confirmations</h1>
        <p class="lead page-lead">Eighteen verified records showing blocked promotions, narrowed claims, non-confirmations, unresolved authority, and evidence gaps.</p>
        {local_nav("/corpus/failures/")}
      </section>

      <section class="section" id="runtime-notice">
{section_head("Runtime", "Runtime failure-event boundary")}
{metric_grid([
        ("Failure/non-confirmation records", data["failures"]["record_count"], "Verified Step 3 register."),
        ("Adequately evidenced runtime failure events", data["failures"]["adequately_evidenced_runtime_failure_events"], "Selected B0 set."),
        ("Invented failures", 0, "No records were invented in this projection."),
    ])}
      </section>

      <section class="section">
{section_head("Verified Step 3", "Failure and non-confirmation register")}
{filter_controls("failures", [("class", "Class", classes), ("scope", "Scope", scopes)])}
        <div class="corpus-record-list">
{chr(10).join(cards)}
        </div>
      </section>
{filter_script()}"""
    return page_shell("/corpus/failures/", "Living Corpus Failures and Non-confirmations | Ivan Kotov", "Verified failure and non-confirmation register for the living corpus.", body)


def render_changes(data: dict[str, Any]) -> str:
    changes = data["changes"]["changes"]
    source_hashes = data["baseline"]["input_hashes"]
    deltas_through = data["changes"]["deltas_applied_through"]
    cards = []
    for item in changes:
        summary = f'\n            <p>{e(item["summary"])}</p>' if item.get("summary") else ""
        note = f'\n            <p><strong>Note:</strong> {e(item["note"])}</p>' if item.get("note") else ""
        cards.append(
            f"""          <article class="card corpus-record-card">
            <p class="section-label">{e(item["change_id"])}</p>
            <h3>{e(item["date"])} - {e(item["title"])}</h3>{summary}
            <p><strong>Status effect:</strong> {e(label(item["status_effect"]))}</p>
            <p>{e(item["claim_effect"])}</p>{note}
            <div class="section-links"><a href="{e(item["public_url"])}">Public route</a></div>
          </article>"""
        )
    cards_html = "\n".join(cards)
    hashes = "\n".join(f"          <li>{e(item['source_id'])}: <code>{e(item['sha256'])}</code></li>" for item in source_hashes)
    body = f"""      <section class="hero corpus-hero">
        <p class="eyebrow">Living corpus</p>
        <h1>Changes since B0</h1>
        <p class="lead page-lead">Public-surface and editorial-projection deltas applied through {e(deltas_through)}. These entries do not raise any B0 status without verified evidence.</p>
        {local_nav("/corpus/changes/")}
      </section>

      <section class="section" id="policy">
{section_head("Policy", "Delta policy")}
        <div class="prose"><p>{e(data["changes"]["change_policy"])}</p></div>
      </section>

      <section class="section" id="delta-log">
{section_head("Log", "Delta log")}
        <div class="corpus-record-list">
{cards_html}
        </div>
      </section>

      <section class="section" id="source-hashes">
{section_head("Receipts", "Source hashes")}
        <ul class="bullet-list corpus-source-list">
{hashes}
        </ul>
      </section>"""
    return page_shell("/corpus/changes/", "Living Corpus Changes Since B0 | Ivan Kotov", "Change log for the living corpus public projection.", body)


def build_html(data: dict[str, Any]) -> dict[Path, str]:
    return {
        HTML_ROUTES["/start-here/"]: render_start_here(data),
        HTML_ROUTES["/corpus/"]: render_corpus_overview(data),
        HTML_ROUTES["/corpus/protocol-map/"]: render_protocols(data),
        HTML_ROUTES["/corpus/current-state/"]: render_current_state(data),
        HTML_ROUTES["/corpus/open-problems/"]: render_open_problems(data),
        HTML_ROUTES["/corpus/failures/"]: render_failures(data),
        HTML_ROUTES["/corpus/changes/"]: render_changes(data),
    }


def update_sitemap() -> str:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    additions = []
    for route in SITEMAP_NEW_ROUTES:
        loc = SITE_URL + route
        if f"<loc>{loc}</loc>" not in text:
            additions.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{LAST_VERIFIED}</lastmod>\n  </url>\n")
    if additions:
        text = text.replace("</urlset>", "".join(additions) + "</urlset>")
    return text


def build_all() -> dict[Path, str]:
    data = load_data()
    outputs = {}
    outputs.update(build_endpoints(data))
    outputs.update(build_html(data))
    outputs[ROOT / "sitemap.xml"] = update_sitemap()
    for path, text in outputs.items():
        if path.suffix.lower() in {".html", ".json", ".xml"}:
            scan_forbidden_public(str(path), text)
    return outputs


def main() -> int:
    try:
        outputs = build_all()
        for path, text in sorted(outputs.items(), key=lambda item: str(item[0])):
            write_text(path, text)
        print(f"Built living corpus layer: {len(outputs)} files")
        print("HTML routes: 7")
        print("JSON endpoints: 7")
        print("Sitemap additions required: 6")
        return 0
    except BuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
