# Scientific Corrigenda and Regression Hardening

## ARQ M2, MOT-c and C-Calculus — version 1.0

**Author:** Ivan Kotov  
**ORCID:** 0009-0009-6002-9845  
**Correction date:** 5 September 2026  
**Publication class:** corrigendum and reproducible document-maintenance supplement  
**Status:** author-authorized correction; Zenodo deposit not yet assigned  
**Scope:** three scientific-document families, with a separate ownership-index correction and experimental-interpretation clarification.

### Publication relationship

This supplement corrects precisely identified passages without replacing the historical deposited packages. It contains four complete corrected reading editions, unchanged source snapshots, exact edits, and executable regression checks. It is not a complete new release of the MOT-c package or the C-Calculus full stack. It must not be deposited as if it were either entire parent package.

The MOT-c predecessor is version 0.1, published on 22 August 2026, version DOI `10.5281/zenodo.22060517`; its concept DOI is `10.5281/zenodo.22060516`. The C-Calculus predecessor is the Governed Binding Stack package version 0.1, published on 5 July 2026, DOI `10.5281/zenodo.21205427`; its affected document 04 has its own version 0.1.2. These are distinct version levels.

The ARQ source is identified by its exact public SER repository commit and SHA-256 in `SOURCE_BINDINGS.json`. The membership of this exact M2 text in a particular Zenodo deposit has not been established by this correction exercise. In particular, the c[q] addendum DOI is not used as the DOI of M2.

The source bytes were retrieved from the working mirror and matched against public repository checksums. Complete Zenodo deposit archives were not downloaded in this exercise. These qualifications concern the acquisition route, not whether the bound passages contain the reported defects. No new assumptions or correction dates are attributed retrospectively to an older release.

## SC-01 — ARQ M2: initial state and resource accounting

**Affected document:** `ARQ_System_Models_and_Assumptions_v0.2.md`, sections 8.4–8.5. The exact predecessor is 21,548 bytes, SHA-256 `73f3ed2a98d691e053a6ee9b6ce05392418cd7dac00febb1e3c392e8ae34f4b6`.

The original retention expression omitted the initial retained state. It is replaced by the increment expression already present in the companion classical boundedness theorem:

\[
H_{retained}(T)-H_{retained}(0)
\leq N_{commit}(T)\,b_{commit,max}.
\]

Here the counter covers commits after the declared initial state, rather than silently counting genesis twice. The unchanged absolute storage bound remains `H_retained(T) <= M_persist`. The increment statement is used only under the companion theorem's M2 assumptions about retained increments and the declared encoding; it is not a newly proved universal physical-entropy bound.

A uniform random initial eight-bit state, retained without new commits, is an immediate counterexample to the unqualified original formula: `8 <= 0` is false. The corrected increment is `8 - 8 <= 0`.

The irreversibility term in the commit-count bound is changed from the unnormalized budget `I_max(T)` to:

\[
\left\lfloor I_{max}(T)/i_{commit,min}\right\rfloor.
\]

The numerator and strictly positive denominator have the same units. Eight budget units at two units per commit permit at most four commits; changing the unit scale must not change that count.

The correction also makes the applicability of the minimum explicit. Every included resource term must constrain the same full counted set of commits. A charge applying to only a subset cannot independently bound the total. The storage-count term applies to non-recycled headroom over the declared window, not to an arbitrary rewritable device's lifetime. Budget replenishment must be included in the window's available budget. A finite one-bit store may be overwritten many times; finite state capacity is not a finite lifetime update count.

**Impact:** formula consistency, dimensions and assumption scope. The correction narrows or clarifies the admissible claim. It does not change ARQ's promotion authority, establish an energy measurement, or constitute validation of a deployed controller.

## SC-02 — MOT-c: represent LATENT in both documentary examples

**Affected documents:** Foundation Theory version 0.1, English and Russian, Appendix A's illustrative `motive_record.status.state` enumeration.

The lifecycle in section 7 already contains fifteen states. Appendix A omitted `LATENT` in both languages. Add it immediately after `CANDIDATE` and before `PROVISIONAL`.

`LATENT` means that significance remains without a current resource claim. It is not a synonym for suspension, abandonment, completion or archiving. The correction aligns the documentary example with the existing lifecycle; it creates no new state or transition.

The separately published `motive-record.schema.json` already includes `LATENT`. Its enum, schema identifier, and transition semantics are not changed for this defect. No deployed Liya validator was exercised or found faulty by this observation.

The corrected reading editions retain the original figures. Their figure provenance records identify the source PDF and embedded image object; extracted PNG representations are not claimed to be the originally deposited PNG bytes. The newly rendered PDFs are corrected reading projections, not silent replacements for the predecessor PDFs.

**Impact:** bilingual example completeness. The full motivational theory and its claim ceiling are unchanged. The targeted bilingual check is not a claim to have re-reviewed every translation paragraph.

## SC-03 — C-Calculus: relation types and finite observed adjacency

**Affected document:** `04_C_CONTINUITY_METRIC_AND_EQUIVALENCE_SEMANTICS_v0_1_2.md`, sections 18 and 21. Its predecessor SHA-256 is `35861cc5c8c579be07840bcace3f44197343d4c384956672da86a308b7bd6fa9`.

Section 21 is a taxonomy of relation types, not four automatically valid mathematical equivalence relations. Snapshot equivalence remains restricted to the declared computable hard-invariant domain. The legacy lineage notation is retained for reference compatibility, but sharing some ancestor is not automatically promoted into an equivalence class or transitive closure over an unspecified ancestry graph.

Operational continuation is directed. The existence of an admissible path from A to B supplies no reverse path from B to A. Any identity or composition laws must come from the applicable trace rules, not from the word “equivalence.”

Threshold resemblance need not be transitive. With absolute-distance threshold one, 0 resembles 0.6 and 0.6 resembles 1.2, but 0 does not resemble 1.2. Resemblance remains advisory and cannot authorize identity, continuity, memory transfer, privilege transfer or fork collapse.

For a finite observed event sequence `event_0, ..., event_(N-1)`, define:

```text
E_i = {n : 0 <= n < N-1 and event_n = i}
M_C[i,j] = count(n in E_i : event_(n+1) = j) / |E_i|   if |E_i| > 0
M_C[i,j] = undefined                                  if |E_i| = 0
```

Only origins with observed successors enter the denominator. The final event is not treated as an extra origin. Empty and singleton traces contain no observed pairs. No terminal self-loop or terminal state is invented. A defined row sums to one over the complete declared event alphabet. Different censoring or terminal conventions must be named separately. Observed adjacency does not establish a Markov model or safety.

**Impact:** mathematical terminology and a finite-trace convention. The hard invariant stack, unknown-value handling, admission algorithms and trace classifier are unchanged. Historical checker and conformance results are not relabeled as tests of this corrected text. A downstream implementation that consumes the affected definitions needs its own version-specific regression, not an assumed inherited PASS.

## SC-04 — Ownership index: preserve historical O12, assign O13

The ownership table accidentally assigned `O12` to both corpus-control and Personality Formation. Repository history before the Personality Formation insertion establishes that O12 belonged to corpus-control. Preserve that association and assign `O13` to Personality Formation, also adding the missing corresponding machine-index entry.

This is an index repair, not a transfer of doctrinal ownership. An old citation to O12 must be resolved using its source revision and row title. The separately numbered O12 objection in `OBJECTIONS_AND_REPLIES.md` is unrelated and remains unchanged. No global replacement of the string O12 is appropriate.

## SC-05 — Interpretation of the proposed substitution test

The Origin-Neutral Recognition note's section 10 compares a continuing system against a fresh system supplied with a bounded memory summary. That comparison can measure replacement, compression and coordination costs. It does not by its wording establish information parity or isolate formation-path effects.

A positive result in that summary condition must not be described as evidence beyond a fully informed strong baseline. A path-comparison claim requires the same complete relevant source record, strong predeclared state construction, matched model/tool/resource conditions, disclosed arm-specific states, and predeclared scoring and noise controls. Both arms' cold-start evaluation removes warm-process advantages but then does not measure an uninterrupted warm-process effect. These are separate questions. No new experiment or effect is reported here.

## Regression hardening and review limits

The package supplies a standard-library-only exact patcher and 29 focused regression tests. The tests cover source hash and size checks; exact patch replay; rejection of altered inputs, repeated patches and overwrite; EN/RU lifecycle-example equality; arithmetic counterexamples; resource-subset and overwriting counterexamples; finite trace edge cases and exhaustive small-alphabet row sums; non-transitive resemblance; and preservation of the existing admission sections.

These are first-party document and example checks. They are not an independent scientific review, a production schema validation, a security certification, a native 07c checker result, or a controlled c-versus-baseline experiment. Passing them does not demonstrate consciousness, personhood, same-c continuity, a c-specific effect, economic value or deployment readiness.

The existing public correction discipline in C-Calculus 07c is reused: preserve old artifacts, distinguish new bytes, identify the correction, retain the claim ceiling and give citation guidance. The bridges are functional: publication custody separates byte provenance from mathematical truth; source/projection separation explains how a correct machine schema can coexist with a wrong printed example; and finite-resource reasoning distinguishes storage capacity from the history of updates. No new governance service is introduced.

An engineering drawing, its printout and a later corrected drawing may share a title but not a revision. Repair means issuing the corrected revision, marking the affected detail and preserving the old inspection record. It does not mean claiming that the earlier structure was built from today's drawing.

## Citation and source use

Cite the predecessor DOI or exact repository revision for the historical wording, and this correction's version and eventual DOI for the changes. Until a DOI is actually assigned to this supplement, cite its title, author, date, version and pinned public repository commit. Do not reuse a predecessor DOI as the identifier of a changed reading edition.

The complete location, size and SHA-256 map is `SOURCE_BINDINGS.json`; literal edits are in `patches/corrections.json`. The original and corrected files are separately labeled. New evidence and changed bytes do not strengthen old claims retrospectively.
