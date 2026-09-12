from pathlib import Path
import re

p = Path('publications/index.html')
s = p.read_text(encoding='utf-8')
begin = '<!-- CGDR-R1-6AN-NAV:BEGIN -->'
end = '<!-- CGDR-R1-6AN-NAV:END -->'

if begin in s or end in s:
    raise RuntimeError('CGDR visible navigation marker already present')

m = re.search(r'(<main\b[^>]*>\s*<section class="hero".*?</section>)', s, flags=re.S)
if not m:
    raise RuntimeError('Publications hero anchor not found')

card = '''

<!-- CGDR-R1-6AN-NAV:BEGIN -->
      <section class="section" id="cgdr-r1-6an-publication-entry">
        <div class="section-head">
          <p class="section-label">Software and technical evidence · v0.1.1 · 12 September 2026</p>
          <h2>CGDR R1.6AN</h2>
        </div>
        <div class="card-grid">
          <article class="card">
            <p class="eyebrow">Published DOI edition</p>
            <h3>CGDR-R1.6A Selected-Process Conformance</h3>
            <p>current-AK Source and R1.6AN Synthetic Evidence. The exact selected profile records 18/18 episodes, 21/21 checkpoints, three expected local synthetic effects and zero promotions. Raw diagnostic FAIL and INCONCLUSIVE values remain visible.</p>
            <p class="status-note">Bounded internally accepted synthetic result. Independent clean-host replication, c-specific real effect, economic value and live-deployment readiness remain unestablished.</p>
            <div class="section-links">
              <a href="./cgdr-selected-process-r1-6an/">Open publication</a>
              <a href="https://doi.org/10.5281/zenodo.22724626">DOI 10.5281/zenodo.22724626</a>
              <a href="https://zenodo.org/records/22724626">Zenodo record</a>
            </div>
          </article>
        </div>
      </section>
<!-- CGDR-R1-6AN-NAV:END -->'''

s = s[:m.end()] + card + s[m.end():]

if 'id="cgdr-r1-6an-publication-entry"' not in s:
    raise RuntimeError('Visible CGDR entry missing after patch')
if '<a href="./cgdr-selected-process-r1-6an/">Open publication</a>' not in s:
    raise RuntimeError('Canonical page link missing after patch')
if 'DOI 10.5281/zenodo.22724626' not in s:
    raise RuntimeError('DOI link missing after patch')

p.write_text(s, encoding='utf-8', newline='\n')
print('PASS_CGDR_PUBLICATIONS_VISIBLE_CARD')
