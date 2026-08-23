from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "publications" / "index.html"
MOT_MARKER = "<!-- MOT_C_VISIBLE_PUBLICATION_CARD -->"
PASC_MARKER = "<!-- PASC_FOUNDATION_GATE_R5 -->"
WORLD_TARGET = '<section class="section" id="world-intelligence">'
TECH_SECTION_ID = 'id="recent-technical-publications"'

MOT_SECTION = r'''<!-- MOT_C_VISIBLE_PUBLICATION_CARD -->
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


def remove_section_by_id(text: str, section_id_fragment: str) -> str:
    hit = text.find(section_id_fragment)
    if hit < 0:
        return text
    start = text.rfind('<section class="section"', 0, hit)
    if start < 0:
        return text
    end = text.find("</section>", hit)
    if end < 0:
        raise RuntimeError(f"Unclosed section containing {section_id_fragment}")
    return text[:start] + text[end + len("</section>"):]


text = PAGE.read_text(encoding="utf-8")

# Normalize the MOT-c section so it is always a standalone top-level section.
if MOT_MARKER in text:
    start = text.index(MOT_MARKER)
    section_start = text.find('<section class="section"', start)
    if section_start >= 0 and section_start - start < 200:
        section_end = text.find("</section>", section_start)
        if section_end < 0:
            raise RuntimeError("Unclosed MOT-c section")
        text = text[:start] + text[section_end + len("</section>"):]
    else:
        next_marker = text.find(PASC_MARKER, start)
        if next_marker >= 0:
            text = text[:start] + text[next_marker:]

# Remove any previously generated technical section before rebuilding it.
text = remove_section_by_id(text, TECH_SECTION_ID)

if WORLD_TARGET not in text:
    raise RuntimeError("Could not locate World Intelligence section")

# World Intelligence must contain only the book card. Move PASC cards out.
world_start = text.index(WORLD_TARGET)
world_end = text.find("</section>", world_start)
if world_end < 0:
    raise RuntimeError("Unclosed World Intelligence section")
world_block = text[world_start:world_end + len("</section>")]

pasc_start = world_block.find(PASC_MARKER)
book_eyebrow = '<p class="eyebrow">book · v1.1.0 · eight languages</p>'
book_hit = world_block.find(book_eyebrow)
if pasc_start < 0 or book_hit < 0:
    raise RuntimeError("Could not identify PASC cards and World Intelligence book card")
book_article_start = world_block.rfind('<article class="card">', 0, book_hit)
if book_article_start < 0:
    raise RuntimeError("Could not identify World Intelligence book article")

pasc_cards = world_block[pasc_start:book_article_start].rstrip()
clean_world_block = world_block[:pasc_start] + world_block[book_article_start:]
text = text[:world_start] + clean_world_block + text[world_end + len("</section>"):]

TECH_SECTION = f'''      <section class="section" id="recent-technical-publications">
        <div class="section-head">
          <p class="section-label">Recent technical publications</p>
          <h2>Post-anchor governance and closure work</h2>
        </div>
        <div class="card-grid">
{pasc_cards}
        </div>
      </section>'''

# Place MOT-c first, then recent technical work, then the book section.
if WORLD_TARGET not in text:
    raise RuntimeError("World Intelligence section disappeared during normalization")
text = text.replace(WORLD_TARGET, MOT_SECTION + "\n\n" + TECH_SECTION + "\n\n      " + WORLD_TARGET, 1)

PAGE.write_text(text, encoding="utf-8", newline="\n")
print("Normalized Publications layout: MOT-c, recent technical publications, then World Intelligence book section.")
