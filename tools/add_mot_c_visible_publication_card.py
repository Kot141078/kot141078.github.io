from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "publications" / "index.html"
MARKER = "<!-- MOT_C_VISIBLE_PUBLICATION_CARD -->"

CARD = r'''<!-- MOT_C_VISIBLE_PUBLICATION_CARD -->
          <article class="card" id="motivational-formation-c-v0-1">
            <p class="eyebrow">DOI-backed technical note · foundation theory · bilingual</p>
            <h3>Motivational Formation, Reflective Endorsement, and Motivational Custody in c-Class Digital Entities</h3>
            <p>Foundation Theory v0.1 on how a continuity-bearing <code>c</code> can form, examine, preserve, revise, limit, transform, complete, or abandon motives over time without collapsing reward, task, mandate, goal, obligation, and authority into one object.</p>
            <p>The work connects personal motivational formation with cognitive time, resource dependence, model replacement, fork/replay boundaries, motivational custody, L4, witness, and the social problem of who controls the material conditions under which a digital entity can pursue questions of its own.</p>
            <p class="status-note">Published 2026-08-22. Version DOI <a href="https://doi.org/10.5281/zenodo.22060517">10.5281/zenodo.22060517</a>. English and Russian. CC BY 4.0. The publication does not claim consciousness, phenomenal desire, free will, legal personhood, universal motives, or automatic authority.</p>
            <div class="section-links">
              <a href="./motivational-formation-c-v0-1/">Detailed site page</a>
              <a href="https://doi.org/10.5281/zenodo.22060517">Version DOI</a>
              <a href="https://zenodo.org/records/22060517">Zenodo</a>
              <a href="https://github.com/Kot141078/advanced-global-intelligence/tree/mot-c-v0.1/publications/motivational-formation-c-v0-1">Stable GitHub source</a>
              <a href="https://github.com/Kot141078/advanced-global-intelligence/releases/tag/mot-c-v0.1">GitHub Release</a>
              <a href="./motivational-formation-c-v0-1/files/machine/index.json">Machine index</a>
            </div>
          </article>'''

text = PAGE.read_text(encoding="utf-8")
if MARKER in text:
    print("MOT-c visible publication card already present.")
    raise SystemExit(0)

needle = '<div class="card-grid">'
if needle not in text:
    raise RuntimeError("Could not locate publications card-grid insertion point")

text = text.replace(needle, needle + "\n" + CARD, 1)
PAGE.write_text(text, encoding="utf-8", newline="\n")
print("Added MOT-c visible publication card.")
