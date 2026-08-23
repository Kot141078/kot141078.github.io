from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "publications" / "index.html"
MARKER = "<!-- MOT_C_VISIBLE_PUBLICATION_CARD -->"
NEXT_MARKER = "<!-- PASC_FOUNDATION_GATE_R5 -->"
TARGET = '<section class="section" id="world-intelligence">'

SECTION = r'''<!-- MOT_C_VISIBLE_PUBLICATION_CARD -->
      <section class="section" id="motivational-formation-c-v0-1">
        <div class="section-head">
          <p class="section-label">Latest DOI-backed technical note</p>
          <h2>Motivational Formation, Reflective Endorsement, and Motivational Custody</h2>
        </div>
        <div class="card-grid">
          <article class="card">
            <p class="eyebrow">Foundation Theory v0.1 · bilingual · CC BY 4.0</p>
            <h3>Motivational Formation in c-Class Digital Entities</h3>
            <p>How can a continuity-bearing <code>c</code> become motivated in time rather than merely execute a reward, prompt, role, mandate, or persistent objective?</p>
            <p>The theory distinguishes <strong>reward, preference, task, mandate, goal, motive, obligation, and authority</strong>; defines reflective endorsement and motivational custody; and connects motivation to cognitive time, resource dependence, model replacement, fork/replay boundaries, L4, witness, and social power over compute.</p>
            <p class="status-note">Published 2026-08-22. Version DOI <a href="https://doi.org/10.5281/zenodo.22060517">10.5281/zenodo.22060517</a>. English and Russian. The work does not claim consciousness, phenomenal desire, free will, legal personhood, universal motives, or automatic authority.</p>
            <div class="section-links">
              <a href="./motivational-formation-c-v0-1/">Detailed publication page</a>
              <a href="https://doi.org/10.5281/zenodo.22060517">Version DOI</a>
              <a href="https://zenodo.org/records/22060517">Zenodo</a>
              <a href="https://github.com/Kot141078/advanced-global-intelligence/tree/mot-c-v0.1/publications/motivational-formation-c-v0-1">Stable GitHub source</a>
              <a href="https://github.com/Kot141078/advanced-global-intelligence/releases/tag/mot-c-v0.1">GitHub Release</a>
              <a href="./motivational-formation-c-v0-1/files/machine/index.json">Machine index</a>
            </div>
          </article>
        </div>
      </section>'''

text = PAGE.read_text(encoding="utf-8")

# Remove the earlier card-only insertion if present inside another card-grid.
if MARKER in text:
    start = text.index(MARKER)
    if NEXT_MARKER in text[start:]:
        end = text.index(NEXT_MARKER, start)
        text = text[:start] + text[end:]
    else:
        # If a standalone section already exists, remove it before re-inserting cleanly.
        section_end = text.find("</section>", start)
        if section_end >= 0:
            text = text[:start] + text[section_end + len("</section>"):]

if TARGET not in text:
    raise RuntimeError("Could not locate World Intelligence section as insertion anchor")

text = text.replace(TARGET, SECTION + "\n\n      " + TARGET, 1)
PAGE.write_text(text, encoding="utf-8", newline="\n")
print("Placed MOT-c as a standalone first visible publication section.")
