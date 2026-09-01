# V67 Source-to-Render Record

This artifact records the six authorized historical source entries, their deterministic render locations, and the bounded normalization applied. The committed Markdown files under `content/diary/` are the controlling normalized Diary source.

## Entry manifest

| Entry | Date | Title | Slug | Activity ID | Source Markdown SHA-256 |
| --- | --- | --- | --- | --- | --- |
| 0218 | 2026-08-17 | “AI Is Eating All the Memory.” | `ai-is-eating-all-the-memory` | `7495011788774703104` | `d4bade3871884c2745629d7ccad805cf272cdfa308e4d646edc421845048e2be` |
| 0219 | 2026-08-18 | Today I watched my cat proudly riding the robot vacuum. | `today-i-watched-my-cat-proudly-riding-the-robot-vacuum` | `7495374640035549184` | `fbcdf50b406837ba5f414e379de80848288365590154cd4460a80241426fd332` |
| 0220 | 2026-08-19 | The Second Missing Layer in Home Robotics: Repair Without Identity Capture | `the-second-missing-layer-in-home-robotics-repair-without-identity-capture` | `7495736375082725376` | `dea47c02717e25877549e58a8f2afdf82dcbfc0f346a84ee93abc496970dc54a` |
| 0221 | 2026-08-20 | We May Be Solving AI Safety at the Wrong Level | `we-may-be-solving-ai-safety-at-the-wrong-level` | `7496099213899018240` | `e9d22e53b3319e52dd785c0e7f54b4adf11b98fede2fdd23343b2231ef2d1418` |
| 0222 | 2026-08-21 | People keep asking whether AI will make humanity better or worse. | `people-keep-asking-whether-ai-will-make-humanity-better-or-worse` | `7496461184263634944` | `41d61bd44322987553b5b4f86cfff99b9d3fff279bb6b04002655fd40f0f077d` |
| 0223 | 2026-08-24 | A goal can be installed. | `a-goal-can-be-installed` | `7497171292417232896` | `7a840d3e77c824ffc4ce8f6043c0d0420342a638a57f30bdd7d2168c8bbb75fa` |

Each record renders at `diary/<slug>/index.html` with its deterministic `assets/diary/<slug>/cover.<actual-extension>` asset. No ENTRY exists for 2026-08-22 or 2026-08-23.

## Authoritative LinkedIn sources

- ENTRY 0218: `https://www.linkedin.com/posts/ivan-kotov-57627b210_artificialintelligence-semiconductors-dram-activity-7495011788774703104-yhWS?utm_source=share&utm_medium=member_desktop&rcm=ACoAADVu3GoBN_Pu_ZXBEYSWMVPvV8kIPjwXXGw`
- ENTRY 0219: `https://www.linkedin.com/posts/ivan-kotov-57627b210_aiinsurance-robotics-embodiedai-activity-7495374640035549184-wSj0?utm_source=share&utm_medium=member_desktop&rcm=ACoAADVu3GoBN_Pu_ZXBEYSWMVPvV8kIPjwXXGw`
- ENTRY 0220: `https://www.linkedin.com/posts/ivan-kotov-57627b210_righttorepair-robotics-embodiedai-activity-7495736375082725376-6pFR?utm_source=share&utm_medium=member_desktop&rcm=ACoAADVu3GoBN_Pu_ZXBEYSWMVPvV8kIPjwXXGw`
- ENTRY 0221: `https://www.linkedin.com/posts/ivan-kotov-57627b210_artificialintelligence-aiagents-aisafety-activity-7496099213899018240-oIRT?utm_source=share&utm_medium=member_desktop&rcm=ACoAADVu3GoBN_Pu_ZXBEYSWMVPvV8kIPjwXXGw`
- ENTRY 0222: `https://www.linkedin.com/posts/ivan-kotov-57627b210_artificialintelligence-aigovernance-aialignment-activity-7496461184263634944-Qv-q?utm_source=share&utm_medium=member_desktop&rcm=ACoAADVu3GoBN_Pu_ZXBEYSWMVPvV8kIPjwXXGw`
- ENTRY 0223: `https://www.linkedin.com/posts/ivan-kotov-57627b210_aiarchitecture-aimotivation-digitalentities-activity-7497171292417232896-65Fj?utm_source=share&utm_medium=member_desktop&rcm=ACoAADVu3GoBN_Pu_ZXBEYSWMVPvV8kIPjwXXGw`

All six full URLs and activity IDs occur exactly once among the V67 source records and were absent from the 217-entry baseline.

## Normalization boundary

Applied:

- protocol front matter and deterministic ASCII slugs;
- paragraph and list boundaries;
- safe generated HTML and typographic characters preserved as Unicode;
- supplied link labels converted into clickable anchors;
- hashtag lines converted into raw source tag metadata;
- factual image alt text based only on visible content;
- the existing presentation layer's canonical tag aliases.

Not applied:

- no prose, punctuation, claims, prices, dates, figures, citations, tags, links, disclaimers, biography, or current-status statements were added or rewritten;
- no V62, V63, or V64 terminology was imported into these historical posts;
- no Diary statement was promoted into B0 status, entity proof, consciousness proof, personhood proof, external validation, or a Living Corpus transition;
- construction and repair examples were not expanded into professional biography, company ownership, clients, staff, projects, addresses, contracts, or finances;
- the cat opening in ENTRY 0219 was not expanded with a name or family context.

## Exact rendered controls

ENTRY 0218 retains the exact price figures `€500`, `€2,300`, and `€5,000`; the qualifier `allegations not yet proven`; `AI scarcity laundering.`; `AI ate everything.`; the authored `c = a + b` paragraph; the “earthly engineering problem” paragraph; and the final sentence `We should not allow “AI demand” to become a license to privatize the bottlenecks of civilization.` No live price, market-share, margin, or litigation update was introduced.

ENTRY 0219 retains the historical relation block:

```text
a is the accountable human anchor.

b is the technological substrate: models, agents, hardware, sensors, memory, cloud services, and procedures.

c is the continuity layer governing how intention becomes action across that changing substrate.
```

It also retains `A robot is not a subscription with legs.`, `It is a moving physical liability surface.`, the liability-laundering distinction, `L4`, and the final chain:

```text
No identifiable authority chain -> no reliable causation -> no scalable insurability.
```

ENTRY 0220 retains all nine service-mode bullets:

```text
freeze sensitive continuity;
isolate memory and identity roots;
revoke external action permissions;
grant only temporary hardware diagnostics;
record every intervention;
verify replacement-part provenance;
test integrity before re-entry;
revoke technician access after repair;
and resume only through a controlled wake path.
```

It retains the five-way `repair, migration, replacement, fork, and replay` distinction, the authored visible label `Earth paragraph:`, `L4`, and both closing lines:

```text
Ownership ends where the screwdriver is forbidden.

But sovereignty also ends where the screwdriver becomes a master key.
```

ENTRY 0221 retains all figures (`18 of 30`, `30 requests per second`, `2.4 million`, `117`), the exact statement `Individual alignment , is not system alignment.`, `Thirty copies of one model are not thirty independent minds.`, `A majority of similar agents is not necessarily evidence.`, all eight governance items, and the source line:

```text
Source: Anthropic, “Patterns and problems in emerging multiagent systems,” August 2026.
```

The source remains historical commentary and was not converted into V63 wording or external-validation evidence.

ENTRY 0222 retains the electricity/printing press/internet sequence; four amplification examples; Belgium, India, Japan, Saudi Arabia, and Brazil; `Its jurisdiction is not an optional safety filter.` / `It is part of the world.`; the authored `c=a+b` spelling; and the seven-question block:

```text
Where am I?
Whose authority am I using?
Which law governs this action?
Who may be harmed?
Is the action reversible?
What must be recorded?
When must I ask?
```

No political evaluation or affiliation was inferred. The laboratory contrast remains the closing line.

ENTRY 0223 retains the opening pair:

```text
A goal can be installed.

Motivation cannot.
```

It retains the publication title `Motivational Formation, Reflective Endorsement, and Motivational Custody in c-Class Digital Entities.`; the eight-way reward/preference/task/mandate/goal/motive/obligation/authority distinction; `A cognitively powerful system may exist immediately.` / `A motivationally mature entity cannot.`; `Motivation requires history.`; the cognitive-time question; `Resource dependency creates constraints.` / `It does not automatically create ownership of purpose.`; the motivational-custody list; `A motive does not create authority.`; and the consciousness/free-will/legal-personhood non-claim.

Supplied publication links remain clickable:

- DOI: `https://zenodo.org/records/22060517`
- Readable page: `https://ivankotov.eu/publications/motivational-formation-c-v0-1/`

The existing publication route overlap is expected, non-blocking, and not a Diary duplicate. It was not treated as proof that any current digital entity satisfies the theory.

## Raw source tags

- ENTRY 0218: `ArtificialIntelligence`, `Semiconductors`, `DRAM`, `DigitalSovereignty`, `Antitrust`, `AIInfrastructure`, `HumanAI`.
- ENTRY 0219: `AIInsurance`, `Robotics`, `EmbodiedAI`, `AISafety`, `AIArchitecture`, `AIGovernance`, `L4`, `CEqualsAPlusB`.
- ENTRY 0220: `RightToRepair`, `Robotics`, `EmbodiedAI`, `AIArchitecture`, `DigitalSovereignty`, `AISafety`, `LocalAI`, `L4`, `CEqualsAPlusB`.
- ENTRY 0221: `ArtificialIntelligence`, `AIAgents`, `AISafety`, `MultiAgentSystems`, `AIGovernance`.
- ENTRY 0222: `ArtificialIntelligence`, `AIGovernance`, `AIAlignment`, `PersistentAI`, `DigitalIdentity`, `FutureOfAI`.
- ENTRY 0223: `AIArchitecture`, `AIMotivation`, `DigitalEntities`, `TemporalAIPresence`, `Cybernetics`, `AIGovernance`, `LongLivedAI`.

No supplied tag was invented, removed, deduplicated, or rewritten in source metadata. The existing canonical display layer renders aliases and keeps the protected token `L4`; `L 4` occurs zero times.

## Final source/render verdict

- Exactly six canonical source files: `PASS`.
- IDs and dates: `PASS`.
- No 2026-08-22 or 2026-08-23 record: `PASS`.
- Historical wording and claim boundary: `PASS`.
- Professional-biography privacy boundary: `PASS`.
- Required links and exact blocks: `PASS`.
- Duplicate/source-variant guard: `PASS`.
