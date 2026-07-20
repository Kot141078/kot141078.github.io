# Vision V64 Source To Rendered Section Audit

Verdict: PASS.

Source owner:

- `content/vision/v0.1/VISION_PAGE_COPY_EN_v0_1.md`
- `content/vision/v0.1/VISION_PAGE_DATA_v0_1.json`
- `content/vision/v0.1/VISION_PAGE_SECTION_MAP_v0_1.csv`

Rendered outputs:

- `/vision/index.html`
- `/vision/index.json`
- `/vision/schemaorg.jsonld`

Section order verified:

0. Hero: `The Future I Am Building Toward`
1. `knowledge` - Knowledge Is Becoming Abundant
2. `from-agents-to-c` - From Models and Agents to c
3. `c-equals-a-plus-b` - c = a + b
4. `time-memory` - Time, Memory, and the Right Not to Answer
5. `reality-before-rhetoric` - Reality Before Rhetoric
6. `children-attachment` - Children, Attachment, and Human Bonds
7. `passport-sovereignty` - Identity, Sovereignty, and the Digital Passport
8. `robots-bodies` - Robots, Bodies, and Livable Intelligence
9. `experience-economy` - From Tokens to Verified Experience
10. `advanced-global-intelligence` - Advanced Global Intelligence

Rendered boundary sections:

- `what-this-vision-does-not-claim`
- `continue`
- `related-corpus-routes`

Fidelity checks:

- Source imported byte-identical against package hashes.
- Section headings render in source order.
- Source markdown tables render as HTML tables.
- Source thematic breaks render as dividers, not visible `---` paragraphs.
- The source protected sentence appears once on `/vision/`.
- The page adds four presentation diagrams without replacing or rewording source prose.

Second-build check:

- `python tools/build_vision.py` second run: zero output-hash changes for `vision/index.html`, `vision/index.json`, `vision/schemaorg.jsonld`, and `sitemap.xml`.

