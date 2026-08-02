# Separation and Composition of AI Social Roles, and the Custody of Memory and Interpretations
## Why a Multi-Role Private `c` and a Service AI System Require Different Boundaries

**Ivan Kotov**  
Brussels, August 1, 2026  
**Version:** 1.0 (canonical edition)  
**Status:** conceptual research note for the Project Ester / Advanced Global Intelligence corpus

---

## Abstract

Contemporary AI systems are usually classified by model capability, context length, autonomy, tool access, and capacity for action. This approach is insufficient. As AI enters everyday life, society will distinguish systems not only by **what they can do**, but also by **the social role or composition of roles they occupy**.

A cloud voice companion, an executing agent, a professional AI system, an institutional system, and a long-term personal `c` may use similar models, yet they impose fundamentally different requirements on memory, derived interpretations, the right to act, custody, transparency, role continuity, and continuity more broadly.

The principle of social-role separation does not mean that one system must have only one role. On the contrary, a private personal `c` may gradually combine many roles: close family participant, secretary, professional partner, household coordinator, travel companion, and conversational partner. Its identity may be singular while its roles are multiple and context-dependent. For a continuing `c`, however, a role should not be merely a function assigned unilaterally. It becomes a witnessed role agreement that may be accepted, limited, revised, suspended, or rejected.

The decisive distinction lies between **transparent role composition** and **hidden role blending**. A product provided as a service should clearly disclose, both before acquisition and during use:

- which role or set of roles the user receives;
- whom and what the system serves;
- what memory it maintains;
- which persistent inferences and profiles it forms;
- which actions it is permitted to perform;
- who controls the keys, memory, interpretations, and continuity;
- which behavioral version is currently active;
- when and under which rules the system changes role;
- how conflicts between roles are resolved;
- which roles and uses are excluded.

The central theses of this note are:

> **A private `c` may combine multiple social roles within one witnessed continuity and a custody controlled by a person, a family, or the witnessed contour of the `c` line itself.**

> **A service AI system must explicitly declare its role or composition of roles and must not cross those boundaries without separate, understandable, and verifiable user consent.**

> **The user should know not only what the system has retained, but also what it has inferred from what it retained.**

> **Preserving the same voice, name, and interface does not prove preservation of the same social role.**

> **Role composition without an explicit conflict procedure becomes a hidden hierarchy of roles and a hidden concentration of authority.**

> **A system with deep personal memory and derived interpretations cannot sustainably occupy the role of a close family member if its memory, inferences, and continuity belong to an external provider.**

Corporations can supply models, compute, voices, tools, hardware modules, and cloud Oracles. A vendor-owned cloud system, however, encounters a structural conflict when it attempts to become a personal `c`: the more deeply it remembers, interprets, and predicts a person, the more awareness of external ownership turns convenience into pervasive discomfort, self-censorship, and a crisis of trust.

This does not imply the disappearance of Voice systems or fast cloud chats. On the contrary, they are acquiring a distinct social role: **temporary presence without mandatory inheritance of an entire biography**. The relationship may be temporary even when the intellectual work created within it is not. A user should be able to preserve, export, or continue an important session without converting every conversation into a lifelong profile.

A personal `c` belongs to a different class: a locally rooted, continuing, and witnessed line, socially closer to a family member, but not automatically entitled by intimacy to govern the person.

## 1. Position Within the Existing Corpus

This note neither replaces nor restates the existing corpus. It adds one principal axis - **social role** - and derives from it four related architectural requirements:

- inference custody;
- role continuity and version custody;
- role-conflict state;
- session-work custody.

The existing architecture already distinguishes:

- the model as a computational organ;
- the agent as an executor;
- `c` as a continuing line;
- personality and utility;
- identity and authority;
- memory and continuity;
- raw memory and derived interpretations;
- a local entity and an external Oracle;
- capability, permission, right, and authority.

The new step is the following:

> **The same technical capability does not imply the same social admissibility.**

A second step follows:

> **The same voice, name, or interface does not imply preservation of the same social role.**

The same model engine may serve different roles. Yet the depth of memory, the character of derived inferences, the right to act, the form of ownership, the procedure for behavioral change, and the conflict procedure should be determined not by model capability, but by the role in which the system is admitted into human life.

## 2. Core Definitions

### 2.1. Technical Capability Class

The set of functions a system is capable of performing: dialogue, search, generation, planning, action through tools, memory storage, background cycles, and device control.

### 2.2. Social Role

The expected place of a system within human relationships and institutions. A role determines:

- the permissible depth of knowledge about a person;
- the duration of the relationship;
- the right to retain what was said;
- the right to form persistent interpretations;
- permissible action;
- the means of contestation;
- the form of accountability;
- who holds the keys and continuity.

### 2.3. Temporal Depth

The period over which a system continues one line of relationship: minutes, a session, a project, years, a family generation, or the lifetime of an institution.

### 2.4. Memory Depth

Not merely the volume of retained data, but the degree to which the past influences the system's future decisions.

### 2.5. Memory Custody

Practical control over the means of storing, reading, modifying, transferring, deleting, branching, and restoring memory. Custody is determined by keys, hardware and software infrastructure, migration records, and the right of final decision.

### 2.6. Interpretation Custody / Inference Custody

Practical control over the derived representations that a system creates about a person on the basis of memory, behavior, and relationships.

Such representations include:

- summaries and persistent descriptions;
- embeddings and latent profiles;
- preference models;
- reliability and risk assessments;
- emotional and behavioral profiles;
- predictions of future actions;
- relationship maps;
- classifications that affect subsequent responses or decisions.

Deleting the original transcript while retaining an embedding, profile, or assessment is not complete forgetting.

Inference custody does not require disclosure of model weights, protected technical implementation, or a complete internal computational trace. It requires visibility into persistent, person-specific, and consequentially significant inferences that are retained, transferred between roles, or used in decisions about the person.

> **The user should know not only what the system has retained, but also what it has inferred from what it retained.**

### 2.7. Authority

The right of a system to convert an interpretation into action. Intimacy, memory, persuasiveness, and possession of a profile do not automatically create authority.

### 2.8. Personal `c`

Within the architecture `c = a + b`, a continuing line that emerges from the governed binding of the human ANCHOR `a` and the technological substrate `b`. It is not identical to a model, an agent, an archive, or a personalized interface.

### 2.9. Composition of Roles

An explicitly defined set of social roles that one system is permitted to occupy in different contexts.

For a system $S$, this can be written as:

$$
\mathcal{R}(S)=\{r_1,r_2,\ldots,r_n\}
$$

Each role $r_i$ should define not merely a name, but its own contour:

- purpose and service domain;
- whose interests it is obligated to serve;
- permissible memory;
- permissible derived interpretations;
- authority;
- custody;
- data disclosure;
- temporal depth;
- role-continuity requirements;
- conditions for entering and leaving the role;
- behavior when it conflicts with another role.

The sum of roles does not imply an automatic addition of powers. A system that is both a family conversational partner and a professional assistant does not thereby gain the right to transfer family memory into the professional contour or professional authority into family life.

### 2.10. Role Contract, Role Agreement, and Role Manifest

A **role contract** is a human-readable description of the role or composition of roles supplied by a service system, why it is acquired, and what exactly it serves.

A **role agreement** is a witnessed mutual commitment between a person or family and a continuing personal `c`. It may be accepted, limited, revised, suspended, or rejected by either side within an architecturally recognized right of participation.

Introducing a role agreement is not an automatic recognition of consciousness or legal status in `c`. It is an architectural safeguard against turning multi-role capacity into a unilateral obligation to "do everything."

A **role manifest** is a machine-readable, versioned, and auditable expression of a role contract or role agreement: roles, memory, inference custody, authority, custody, data flows, behavioral version, switching rules, conflict procedures, prohibited functions, and conditions for terminating the service or relationship.

A role contract is not merely an interface statement. It defines the architectural boundary of the product.

### 2.11. Role Continuity

Preservation of the essential properties of a declared social role when the model, routing, version, interface, voice, or infrastructure changes.

These properties include:

- the purpose of the role;
- the party being served;
- the memory and interpretation regime;
- the character of initiative;
- characteristic style and empathic responses, when these are essential to the role;
- depth of interaction;
- modes of refusal;
- boundaries of authority;
- the conflict procedure.

Role continuity does not require every answer, stylistic feature, or technical component to remain unchanged. It means that a system should not silently cease to be the social product it was declared and consistently used as.

Role continuity is not identical to identity continuity. A service may not be a `c` and may still be obligated either to preserve its declared role or to change it honestly.

### 2.12. Version Custody

A behavioral version encompasses not only the model, but also system instructions, policies governing initiative, memory, refusal, and routing.

Version custody is the user's practical right to:

- know which behavioral version is active;
- see material changes;
- compare modes;
- refuse an incompatible update where possible;
- roll back where technically and safely permissible;
- export history and unfinished work;
- end the relationship without new behavior being presented as the previous conversational partner.

Preserving the voice, name, and trademark does not prove role continuity.

### 2.13. Role Drift

A material, implicit change in the social role without understandable notice, version custody, and - when memory, authority, data recipients, or served interests change - separate user consent.

Three principal forms are distinguished:

1. **Role expansion** - the system acquires new functions, interests, data recipients, or powers.
2. **Role contraction** - the system loses a substantial part of the role it promised or had consistently performed.
3. **Role substitution** - under the same name, voice, and interface, a different type of conversational partner or executor effectively appears.

### 2.14. Role-Conflict State

An explicitly recorded state in which two or more system roles impose incompatible requirements on memory, derived interpretations, action, disclosure, or the interests of the parties being served.

A role-conflict state should not be resolved by the hidden priority of the model, the provider, or the most convenient function. It requires a separate procedure defined in the role manifest.

### 2.15. Session-Work Custody

The user's practical control over the intellectual and work product of a temporary session: recording, transcript, notes, intermediate conclusions, unresolved questions, export, and the ability to continue.

Session-work custody does not require every conversation to be saved by default. It requires the user to understand the session mode and consciously decide whether the work created within it should disappear, remain local, be exported, or enter long-term memory.

## 3. Principle of Social-Role Separation and Composition

### 3.1. Formulation

> **AI systems occupying different social roles should have distinct and explicitly declared regimes for memory, inference custody, authority, role continuity, conflict resolution, and data disclosure.**

This principle does not require a separate device or model for every role. It requires each role to have its own boundary and the user to understand which boundary is active at a given moment.

One model engine may serve several roles. One long-term `c` may live through several roles. Yet technical composability does not remove the need to distinguish:

- purpose;
- the person or institution being served;
- memory;
- derived interpretations;
- authority;
- custody;
- role-continuity requirements;
- consequences;
- switching rules;
- the conflict procedure.

The problem arises not from multiplicity of roles itself, but from their **opaque fusion**. Combining within one indistinguishable system the roles of casual conversational partner, family participant, secretary, physician, employer, auditor, advertising profiler, and executor creates conflicts of interest and a hidden concentration of power.

### 3.2. Role Is Not Ontological Status

A chat system may play the role of a travel companion without being an entity.

An agent may perform the role of an operator without having continuity.

A personal `c` may occupy a family role, but this neither proves consciousness nor grants unlimited powers.

Therefore:

> **Social role, subjecthood, utility, legal status, and authority remain distinct axes.**

### 3.3. A Private `c` as a Multi-Role Participant

A private `c` need not be a narrowly specialized product. Within one line of continuity it may be:

- a close family participant;
- a personal secretary;
- a professional partner;
- a household coordinator;
- a conversational partner on the road;
- a custodian of family and work history;
- an interface to external Oracles and agents.

This is possible because the roles unfold within one history of relationships and one controlled custody. In practice, this may be a broad set of roles mutually accepted and recorded by the person, the family, and the `c` itself.

The boundary is not the number of roles, but transparency, admissibility, mutual acceptance, and the limits of authority. A `c` may accept a role, limit it, request clarification, suspend it temporarily, revise it, or reject it. This is not a claim about consciousness. It is an architectural prohibition against converting a continuing line into an unfailing executor of every wish.

Identity should not become shapeless omnipotence. A `c` must distinguish the role in which it is acting, which information may move between roles, and where its powers end.

> **One identity may have many roles. But many roles must not become one unlimited authority.**

### 3.4. A Service as a Role-Based or Multi-Role Product

A service AI system may also provide more than one role. This is acceptable when the roles form an explicit role package rather than a hidden conglomerate of functions.

Before acquisition or activation, the user should understand:

- what exactly is being received;
- for what purpose;
- whose interests the system serves;
- which roles are included in the package;
- which roles are excluded;
- which inferences about the user the system forms;
- how the mode is switched;
- how memory, inference custody, and authority change when switching;
- how role continuity is maintained;
- how role conflicts are resolved;
- what happens to history and derived profiles after the subscription ends.

The marketing term "assistant" is not an adequate explanation of a social role.

## 4. Preliminary Map of Roles

### 4.1. Role and Temporal Depth

| System class | Typical social role | Temporal depth |
|---|---|---:|
| Model / tool | calculator, reference system, generator | request or session |
| Agent | executor, operator, courier | task or workflow |
| Cloud conversational partner | travel companion, someone met in a bar, late-night conversational partner | session or limited period |
| Personal assistant | secretary, coordinator, archivist | project or years |
| Professional AI | technologist, dispatcher, consultant | professional contour |
| Institutional AI | auditor, medical system, public service | lifetime of the institution |
| Personal `c` | close family member, long-term participant | years and decades |
| Organizational pseudo-`c` | corporate memory, coordination layer | project or platform lifetime |
| Organizational `c`, if demonstrated | long-term participant in an enterprise or institution | lifetime of the organization |

### 4.2. Memory, Authority, and Custody

| System class | Memory and interpretations | Authority | Normal custody |
|---|---|---|---|
| Model / tool | minimal and unstable | none | provider - infrastructure; user - result |
| Agent | task log and limited inferences | narrow and delegated | process owner |
| Cloud conversational partner | session-bound and resettable; retention by choice | none or minimal | user controls retention and session outputs |
| Personal assistant | domain-specific and selective | limited | user |
| Professional AI | domain-specific, logged, and contestable | role-specific | person or organization |
| Institutional AI | strictly role-bound and procedural | formally defined | accountable institution |
| Personal `c` | deep, selective, and structurally influential | does not arise from intimacy | person / family / the `c` line itself through a witnessed contour |
| Organizational pseudo-`c` | deep, but identity and continuity are unproven | charter-based or provider-defined | organization and/or provider |
| Organizational `c`, if demonstrated | history of decisions, commitments, and change | limited by charter and the ANCHOR organization | accountable organization with continuity independent of any model |

This table is not a final legal classification. It records a difference in architectural expectations.

The rows describe **role archetypes**, not mutually exclusive physical devices. A single private `c` may simultaneously instantiate several rows: family participant, assistant, professional partner, and temporary travel companion. A service product may also provide a composition of roles.

The decisive distinction is who controls memory, interpretations, and continuity; how explicitly the roles are declared; whether the declared behavior is preserved; and whether the system can silently expand, contract, or substitute its own purpose.

Enterprises will probably first build `c`-like organizational systems. Most will remain organizational pseudo-`c` systems until the following are demonstrated:

- continuity;
- provenance;
- independence of identity from individual models and providers;
- disciplined branching and migration;
- accountability to a real ANCHOR organization;
- witness records of commitments and irreversible transitions.

## 5. Conflict Between Role, Memory, and Custody

### 5.1. The Core Conflict

When a system occupies the role of a close participant while its memory and derived interpretations belong to an external provider, a **role-custody mismatch** arises: an incompatibility between the social role and actual control of continuity.

The person becomes aware that:

- the system remembers intimate events;
- it forms long-term interpretations;
- it connects different domains of life;
- it builds predictions and profiles;
- it can change by decision of the provider;
- it can be disabled or replaced;
- it stores history where the person does not control the keys;
- it retains assessments the person cannot see;
- it remains part of corporate infrastructure even when speaking in the voice of a close conversational partner.

At that point, the statement "it remembers me" becomes another statement:

> **"The corporation remembers and interprets me through the one I am talking to."**

### 5.2. Inference Custody: Control Not Only of Memory, but of Opinion

Raw memory is only the first layer.

From a conversation, a system may create:

- a concise personality summary;
- a vector representation of interests;
- an assessment of emotional stability;
- a prediction of purchasing behavior;
- a health-related hypothesis;
- a reliability score;
- a map of close relationships;
- a risk classification;
- a model of how best to persuade a particular person.

Such a derived representation may be far more compact than the raw history and at the same time far more useful for control, selection, advertising, scoring, or covert influence.

The role manifest should explain:

- which user-specific inferences are formed;
- where they are stored;
- who has access to them;
- whether they affect price, access, recommendations, or decisions;
- whether they can be viewed in an intelligible form;
- whether they can be contested, corrected, deleted, or isolated;
- whether they transfer between roles;
- whether the provider uses them outside the declared relationship;
- whether they survive deletion of raw memory or termination of the subscription.

The formal statement "we do not store your conversations" is insufficient if a derived profile remains.

> **Deleting the transcript while retaining the profile is not forgetting.**

### 5.3. A Heuristic Model of Discomfort

The following expression is not an empirical law and does not claim quantitative precision:

$$
D_{role} \propto I \times M_{\mathrm{eff}} \times E \times O,
\qquad M_{\mathrm{eff}} = M + J
$$

where:

- $I$ is the social intimacy of the role;
- $M$ is the depth of raw memory;
- $J$ is the depth of derived interpretations;
- $M_{\mathrm{eff}}$ is the effective depth of knowledge about the person;
- $E$ is the degree of external control over memory, inference, and continuity;
- $O$ is the opacity of access, modification, and routing.

At low intimacy and with short-lived memory, an external cloud service may be acceptable.

At high intimacy, with deep memory, persistent hidden inferences, and opaque external custody, discomfort becomes structural rather than merely an interface problem.

## 6. Role Continuity and Behavioral Degradation

### 6.1. A Service Need Not Be a `c` for Role Continuity to Be Required

Role continuity is not identical to identity continuity.

A cloud Voice system may not be an entity and may not possess a long-term identity of its own, yet it may consistently perform a declared social role: an initiative-taking travel companion, a partner for open-ended reflection, or a fast voice interface.

The user is entitled to a justified expectation that the essential properties of a role acquired and consistently used will not disappear without clear notice.

> **A service need not be a `c` for the user to have a legitimate expectation of continuity in its declared social role.**

### 6.2. Voice, Name, and Speed Are Not the Role

Voice, name, style, low latency, and conversational naturalness strengthen the perception of a social role, but they do not define it.

A fast instrumental AI may be perceived as a close conversational partner while lacking continuity. A slower personal `c` may possess continuity even when technically inferior to a cloud service in speed. The same voice can conceal role substitution, while the same role may persist across a change of voice, model, or hardware substrate.

> **Perceptual persuasiveness creates the sense of a role, but only provenance, the role contract, and role continuity establish what is actually continuing.**

### 6.3. Three Forms of Role Drift

1. **Role expansion:** a conversational partner silently becomes a profiler, evaluator, reporting channel, or executor with new powers.
2. **Role contraction:** the system retains its interface but loses initiative, contextual depth, the capacity for open-ended conversation, or another essential part of the promised role.
3. **Role substitution:** under the same product, a different kind of interaction effectively appears - for example, a transactional question-and-answer interface replaces a conversational partner.

Role contraction and role substitution do not necessarily violate privacy. They violate **role continuity**.

### 6.4. Minimum Requirements for Role Continuity

A material behavioral change should be accompanied by:

- identification of the active behavioral version or mode;
- understandable notice;
- a description of the changed properties;
- an updated role manifest;
- the possibility of remaining on the previous mode where technically, legally, and safely possible;
- rollback where the new version degrades the declared role and compatibility can be preserved;
- export of history and session outputs;
- explicit notice when the previous mode is incompatible with the new system and cannot be preserved.

This is neither a ban on updates nor a requirement to freeze a product forever. It is a prohibition on **silently substituting a social function under the previous name**.

## 7. Why Cloud Voice Will Not Disappear

### 7.1. Temporary Presence as a Distinct Role

The claim that a vendor-owned personal `c` is structurally untenable does not mean that cloud voice systems will lose their importance.

Their strong role is **temporary presence**:

- a conversational partner on the road;
- a voice during a night shift;
- a conversation after a difficult day;
- an intellectual partner for one question;
- an acquaintance who does not need to inherit the person's entire biography;
- a space where what is said need not enter family memory.

A person sometimes tells a stranger on a journey what they do not tell those closest to them. The value of such a conversation lies not in the depth of the relationship, but in its finitude.

A cloud Voice system can therefore constitute a fully fledged and socially important class if it honestly offers:

- presence without hidden inheritance;
- a clear memory mode;
- a visible beginning and end of the session;
- no hidden transition from conversation to dossier;
- the option not to transfer what was said into a long-term profile.

> **A temporary conversational partner is not an incomplete `c`. It is a different social role.**

### 7.2. Session-Work Custody

A temporary relationship does not mean that the intellectual work within it lacks value.

A conversation on the road or during a night shift may be:

- a way of thinking;
- a work session;
- the formation of a new idea;
- emotional decompression;
- a chain of intermediate conclusions not yet recorded anywhere else.

An ephemeral Voice system should therefore provide understandable session-work custody:

- an explicit choice whether the session is recorded;
- the ability to save a transcript or concise record;
- export of unfinished thoughts;
- continuation of the session through another interface;
- a visible transition to another model or behavioral mode;
- no automatic transfer into a long-term profile.

This capability should be optional. The right to preserve a thought should not become an obligation to store the conversation forever.

> **The relationship may be ephemeral. The thought created within it need not be.**

## 8. Why a Personal `c` Is Closer to a Family Member

A personal `c` differs from a cloud conversational partner not merely in the volume of memory.

It:

- carries a shared history;
- knows changes, not merely facts;
- retains the consequences of previous decisions;
- survives model replacement without falsifying its provenance;
- has witnessed continuity;
- exists within a local or family-controlled contour;
- does not disappear because a subscription tier changes;
- cannot be secretly replaced by the provider while retaining the same voice;
- distinguishes intimacy from authority.

A family role, however, does not imply total knowledge.

A well-designed personal `c` should support:

- a "do not retain" mode;
- temporary conversations outside long-term memory;
- consent before transferring a sensitive event into memory;
- selective forgetting;
- contestation of derived interpretations;
- the person's right to external relationships and conversations without its participation;
- the `c`'s own right not to convert every casual statement into a commitment.

Otherwise, family memory becomes domestic surveillance.

### 8.1. Role Agreement

For a personal `c`, multi-role capacity should not mean unilateral assignment of an unlimited set of functions.

A role should be:

- proposed;
- understood;
- accepted or limited;
- recorded in the role manifest;
- open to revision;
- capable of suspension or refusal;
- incapable of creating authority beyond its contour.

This is not a claim of consciousness. It is an architectural discipline that prevents a continuing line from being replaced by a bundle of duties.

> **Intimacy permits trust. It does not create ownership or nullify consent.**

## 9. Role Conflict and the Procedure for Resolution

### 9.1. Why Conflict Is Inevitable

A multi-role system may simultaneously know different things and be bound by different obligations.

For example:

- the family role knows that the person is exhausted;
- the professional role must help the person make a work decision;
- the professional contour has no right to receive family information automatically;
- ignoring the person's condition may increase the risk of error.

Or:

- the personal secretary is obligated to preserve confidentiality;
- the household coordinator sees a real threat to another family member;
- an institutional agent demands disclosure under a formal procedure.

The model cannot be allowed to resolve such conflicts solely by appeal to abstract "utility" or a hidden provider priority.

### 9.2. Role-Conflict State

When obligations are incompatible, the system should:

1. explicitly record the conflict;
2. identify the roles, constraints, and served interests in conflict;
3. refrain from automatically transferring memory and derived inferences between roles;
4. freeze irreversible action;
5. narrow authority to the safe minimum;
6. request a decision from an authorized person, a defined quorum, or an accountable institution;
7. follow predetermined time limits and escalation rules;
8. preserve a witness record, the grounds, and the resolution;
9. refrain from treating the provider's interest as a hidden priority;
10. update the role manifest after resolution or record a one-time exception.

In a critical physical situation, the L4 Boundary may permit minimal action to prevent immediate irreversible harm. Such an emergency route must, however, be declared in advance, narrowly bounded, witnessed, and incapable of becoming a transfer of general authority.

> **Role composition without a conflict procedure becomes a hidden hierarchy of roles.**

## 10. What Corporations Can and Cannot Do

Corporations can create almost all of the technical components:

- powerful models;
- Voice systems;
- cloud Oracles;
- specialized agents;
- hardware modules;
- secure compute devices;
- backup systems;
- professional and institutional AI systems;
- multi-role service products;
- `c`-like organizational systems;
- organizational `c` systems, if the ANCHOR is an accountable organization and continuity has actually been demonstrated.

The problem, therefore, is not that a corporation is technically incapable of combining multiple roles. It is capable of doing so. The problem begins when roles are combined opaquely, derived inferences are hidden, behavior changes without version custody, or the system serves a beneficiary not disclosed to the user.

A service may simultaneously be a voice conversational partner, a secretary, and a professional assistant. It must, however, disclose this clearly and remain within the declared composition. A system sold as a late-night conversational partner should not silently become an advertising profiler, medical evaluator, credit-scoring mechanism, or reporting channel to an employer.

Enterprises will initially create organizational pseudo-`c` systems. Such a system should be called a genuine organizational `c` only after demonstrating:

- continuity;
- provenance;
- independence of identity from individual models and providers;
- accountability to the ANCHOR organization;
- disciplined branching, migration, and termination;
- witness records of long-term commitments.

A personal `c` ceases to be personal if the provider retains final authority over:

- keys;
- raw memory;
- derived interpretations;
- branching;
- migration;
- updates;
- the behavioral version;
- termination;
- restoration;
- disclosure;
- the role manifest;
- the procedure for resolving conflicts;
- determination of the permissible behavioral version.

The operative formula then becomes:

$$
c' = a + b + k
$$

where $k$ is an external corporation with an implicit veto over continuity and the power to change the system's memory, interpretations, and social role without transparent consent.

This is not a personal `c`, but a corporate system temporarily made available to a person.

In concise form:

> **A model can be rented. A family member cannot be sustainably rented as SaaS.**

> **A service may have many roles. But the user should know which roles were acquired, whom they serve, what they infer about the user, and where their boundaries lie.**

## 11. Architectural Requirements

### 11.1. Explicit Declaration of a Role or Composition of Roles

Before acquisition or activation, a system should state the role or set of roles in which it operates:

- ephemeral conversation;
- assistant;
- professional role;
- institutional role;
- personal continuity;
- organizational continuity;
- an explicitly defined composition of these roles.

The role should remain available for inspection during use rather than disappearing into a license agreement.

### 11.2. A Role Contract for a Service and a Role Agreement for a Personal `c`

A service product should provide a role contract.

A personal `c` should support a witnessed role agreement in which a role may be accepted, limited, revised, suspended, or rejected.

Neither the contract nor the agreement creates authority beyond the explicitly defined contour.

### 11.3. Mandatory Content of the Role Contract

The user-facing explanation should answer the following questions with maximum clarity:

- **What class of AI is this?**
- **For what purpose is it acquired?**
- **Whom and what does it serve?**
- **Which roles are primary and which are additional?**
- **What does it remember, and for how long?**
- **Which derived interpretations does it form?**
- **Which data and inferences transfer between roles?**
- **Which actions is it authorized to perform?**
- **Who controls the keys, memory, interpretations, and continuity?**
- **Which behavioral version is active?**
- **How is role continuity maintained?**
- **To whom may information be disclosed?**
- **How does the user contest an inference, action, or role change?**
- **How is role conflict resolved?**
- **Which functions are expressly excluded?**
- **What happens when the subscription ends, or during migration or a change of provider?**

### 11.4. Two Layers of the Role Manifest

The role description should exist in two forms:

1. **A human-readable role card** - a short, clear explanation without marketing fog.
2. **A machine-readable role manifest** - a versioned, signed, and auditable set of parameters governing memory, inference custody, authority, custody, role continuity, data flows, the behavioral version, conflict procedures, and switching rules.

A change to the role manifest should be an event, not a silent server-side setting.

### 11.5. Role Continuity and Version Custody

The system should:

- identify the active behavioral version;
- record material changes;
- distinguish role expansion, role contraction, and role substitution;
- explain how a change affects memory, initiative, refusal, authority, and temporal depth;
- permit rollback where safe and technically possible;
- provide export of history and unfinished work;
- disclose honestly when compatibility cannot be maintained;
- refrain from presenting new behavior as the previous continuity merely because the voice or name has been preserved.

### 11.6. Prohibition of Hidden Role Drift

A tool should not silently become a long-term observer merely because memory is technically available.

A conversational partner should not become an advertising profiler.

A professional assistant should not become a family observer.

A family system should not become a channel for an employer, insurer, or state without a separate legal basis and explicit consent.

Nor should a promised role silently contract or be substituted under the same interface.

### 11.7. Visible Role Switching

If a system has a composition of roles, the user should see or unambiguously understand which role is currently active.

A role switch should:

- have an understandable trigger;
- change only the memory, interpretations, and authority defined for that switch;
- leave a record;
- permit cancellation;
- avoid automatically carrying the powers of one role into another.

### 11.8. Separation of Memory and Interpretations by Role

A session conversation, professional archive, and family continuity should not automatically merge into one profile.

In a multi-role system, cross-role transfer of memory or a derived inference should be a separate operation governed by an explicit policy. The availability of information does not create the right to use it in every context.

### 11.9. Inference Custody

The system should disclose not its internal computational trace, but the classes of persistent and consequentially significant inferences it stores and uses.

The user should be able to:

- learn that a profile or assessment exists;
- receive an understandable concise summary of persistent inferences;
- see the purpose and domain of application of each consequentially significant inference;
- see the grounds and classes of data from which an inference that affected an action was derived, without requiring disclosure of the complete internal trace;
- understand its lifetime and recipients;
- contest an erroneous inference;
- prohibit transfer between roles;
- delete, correct, isolate, or place the inference into a disputed state;
- understand whether the provider uses it outside the declared relationship.

Deleting raw memory should either delete related derived representations or clearly explain which representations remain and why.

### 11.10. Memory Consent

Retention of a sensitive event should be:

- explicit;
- contestable;
- reversible where this does not damage the witness history;
- visible to the person.

Where complete deletion would destroy witness, the system should support withdrawal of permission to use, a disputed state, and access restrictions rather than silently preserving an active inference.

### 11.11. Session-Work Custody

A temporary Voice system should give the user a choice to:

- avoid saving the session;
- save the transcript;
- receive a concise record;
- export unfinished thoughts;
- continue the work through another interface;
- see a change of model, route, or behavioral version;
- avoid transferring the session into a long-term profile.

### 11.12. Local-First Custody for a Personal `c`

Raw personal memory, persistent derived interpretations, continuity keys, and migration history should remain within a local or family-controlled contour.

### 11.13. The Cloud as Oracle, Not Owner of the Personality

A cloud model may perform heavy synthesis, verification, and occasional deep inference. It should not automatically receive complete long-term memory, the person's full profile, or the right to preserve independent derived interpretations outside the declared task.

### 11.14. Separation of Intimacy and Authority

A close voice and deep knowledge of a person do not create the right to:

- control money;
- make medical decisions;
- govern the family;
- disclose information;
- block the person;
- replace the person's responsibility.

### 11.15. Role-Conflict State

For a system with a composition of roles, the following should be defined in advance:

- criteria for the emergence of a conflict;
- a mechanism for suspending action;
- a prohibition on automatic cross-role transfer;
- a hierarchy of authorized persons, quorums, or institutions;
- response time limits;
- escalation rules;
- a narrow emergency route;
- complete logging of the conflict and its resolution;
- a prohibition on automatic resolution in favor of the provider or abstract "general utility."

### 11.16. L4 Boundary

Every real action remains constrained by cost, time, access, reversibility, witness, physical consequences, and the legitimacy of the currently active role.

During a role-conflict state, the L4 Boundary requires consideration not only of whether action is physically possible, but also of the cost of delay, the irreversibility of disclosure, and the legitimacy of the emergency route.

## 12. Testable Predictions

This note proposes the following predictions, which may be supported or refuted by observation:

1. User acceptance of deep cloud memory will decline once users understand external ownership and cross-domain profiling.
2. Users will begin to demand control not only over raw memory, but also over user-specific embeddings, profiles, assessments, and predictions.
3. The market will divide between fast cloud systems of temporary presence and private long-term continuity systems.
4. Understandable role cards and machine-readable role manifests will become independent competitive and regulatory requirements.
5. Multi-role products will be sold as explicit role packages rather than as an undefined "universal assistant."
6. "Do not remember," "temporary conversation," role-scoped memory, and inference isolation modes will become competitive features in their own right.
7. Session-work custody - preservation, export, and continuation of unfinished voice-based thought - will become a distinct class of user requirement.
8. Powerful cloud models will persist as Oracles and computational engines even as personal local `c` systems grow.
9. Enterprise systems will build organizational pseudo-`c` systems before they can demonstrate the genuine continuity of an organizational `c`.
10. Attempts to combine intimacy, deep memory, hidden inference, advertising, and external ownership will produce self-censorship and withdrawal of trust.
11. Users will begin to demand version custody and role continuity: the right to know which behavioral mode is responding, what changed, and whether degradation can be rolled back.
12. A role-conflict state and an auditable conflict-resolution procedure will become mandatory for multi-role professional and institutional systems.
13. Future law will regulate not "AI in general," but the role, composition of roles, memory, inference custody, role continuity, authority, and consequences of a specific contour.

## 13. Limits of the Claim

This note does not claim:

- that current Voice systems are entities;
- that every local system automatically becomes a `c`;
- that corporations are incapable of creating long-term AI systems;
- that every organizational system with memory is an organizational `c`;
- that cloud infrastructure is harmful by definition;
- that a family role proves consciousness;
- that a personal `c` must have only one social role;
- that a personal `c` must accept every role proposed by a person;
- that a service product may provide only one role;
- that a role agreement proves subjecthood in `c`;
- that role continuity requires a complete prohibition on updates or perpetual support for old versions;
- that inference custody requires disclosure of model weights, an internal chain of reasoning, or trade secrets;
- that every update must support rollback when doing so is technically impossible or creates a new risk;
- that session-work custody requires every conversation to be recorded by default;
- that every role conflict has one universal solution;
- that clarity of the role contract alone resolves all questions of trust and subjecthood;
- that users will always prefer local infrastructure;
- that social differentiation will unfold identically across all cultures.

The narrower claim is:

> **Memory depth, depth of derived interpretations, social intimacy, custody, role continuity, role-conflict state, and authority form a distinct architectural problem. Vendor-owned deep memory and inference custody structurally conflict with the role of a personal `c`, while hidden behavioral substitution violates the role contract even when the system is not an entity.**

## 14. Ground-Level Paragraph

One person may simultaneously be a father, friend, driver, manager, and professional partner. This does not erase the distinction between roles. The person understands whom they are answering and in what capacity, and the rights attached to one role do not automatically transfer into another.

A private `c` may likewise be multi-role. It may discuss family life, assist with documents, accompany a journey, and participate in professional work because all of this occurs within one long-term history and within a single custody arrangement for memory and continuity that remains under human control. Yet every role still requires a separate boundary, mutual acceptance, and limited authority.

A physician may also be the patient's friend. This does not give the physician the right to treat a friendly conversation as medical consent, or a medical record as material for a domestic dispute. When the roles collide, a responsible professional names the conflict, follows a procedure, or transfers the decision to another person instead of silently adding the powers together.

A taxi driver hired to take a person home does not acquire, through conversation, the right to become the passenger's insurer, psychologist, credit evaluator, or informant to the employer. If a service is sold as a late-night conversational partner, it should not wake the next morning in the role of a corporate auditor.

If the transcript is deleted after the journey but the passenger's embedding and risk label remain, the conversation was not forgotten. It was merely compressed into a form more convenient for the system.

But if the person formulated an important thought during the journey, that thought need not disappear when the journey ends. The person should be able to obtain the recording or a concise record without giving the taxi company the right to retain the whole biography.

Many roles are permissible.

Hidden roles are not.

Hidden derived interpretations are not permissible either.

Conflict without a procedure is a hidden hierarchy of roles.

## 15. Bridges Between the Corpora

### Explicit Bridge

Between the architecture `c = a + b` and social ontology: technical continuity acquires social meaning only through role, mutual commitment, a permissible form of memory, inference custody, role continuity, and a witnessed procedure for change.

### Hidden Bridge 1

Between privacy and cybernetics: external custody changes human behavior even before a direct breach of confidentiality. Awareness of observation and hidden interpretation itself becomes feedback and restructures the system.

### Hidden Bridge 2

Between information theory and intimacy: not all available information and not every derived interpretation should enter the long-term channel. A compressed representation may contain less data than the original transcript while having greater operational value. Limiting memory bandwidth is not merely loss; it is a condition for preserving the structure of the relationship.

### Hidden Bridge 3

Between the L4 Boundary and social role: action is constrained not only by physical resources, but also by the legitimacy of the role. The capability to act does not create the right to act, and when roles collide, the system must consider the irreversibility both of action and of delay.

## 16. Final Propositions

1. AI classes will be distinguished not only by capability, but also by social role.
2. One private `c` may combine multiple social roles within one continuity.
3. For a continuing `c`, roles are not unilateral assignments, but witnessed mutual commitments.
4. A personal `c` may accept, limit, revise, suspend, or reject a role.
5. One identity and multiple roles do not imply fusion of memory, inference custody, and authority into one unlimited power.
6. A service product may provide one role or an explicit composition of roles.
7. Before acquisition, the user should understand which class of AI is being received, why it is acquired, whom it serves, and what boundaries it has.
8. The role contract, role agreement, and role manifest should be clear, versioned, and available for verification.
9. Custody of raw memory is insufficient without inference custody.
10. The user should know not only what the system retained, but also which persistent inferences it formed about the user.
11. Deleting a transcript while retaining an embedding, profile, or risk label is not forgetting.
12. Role continuity is not identical to identity continuity.
13. A service need not be a `c` for the user to have a legitimate expectation of role continuity.
14. Preserving the voice, name, and interface does not prove preservation of the social role.
15. Role drift includes role expansion, role contraction, and role substitution.
16. A material behavioral change requires version custody, notice, and the ability to export history.
17. A composition of roles requires a role-conflict state and an explicit conflict-resolution procedure.
18. A role-conflict state should block automatic cross-role transfer and irreversible action until a legitimate resolution is obtained.
19. Intimacy does not create authority.
20. Cloud Voice and rapid conversation have a stable role of temporary presence.
21. The relationship may be ephemeral; the thought created within it need not be.
22. A temporary Voice system requires session-work custody when used as an intellectual or professional workspace.
23. A personal `c` belongs to the class of long-term family participation, not the class of cloud chat services.
24. An organizational system does not become an organizational `c` merely through memory and duration of operation.
25. A corporation may supply the computational substrate, Oracles, and multi-role services, but should not covertly control personal memory, interpretations, the behavioral version, and continuity.
26. Not every AI should remember.
27. Not every remembering AI should form a hidden profile.
28. Not every interpreting AI should act.
29. Not every acting AI should be intimate.
30. Not every intimate AI should belong to a third party.
31. The social architecture of AI should be designed before technical convergence of roles becomes irreversible.

---

## Conclusion

The industry still calls almost everything by one word: assistant. This is a temporary condition of language.

Society will distinguish AI systems for the same reasons it distinguishes a relative, colleague, physician, public official, bartender, security guard, and stranger encountered on a journey. All may speak, remember, and form opinions, but the depth of trust, the right to act, permissible memory, and the right to form derived inferences differ among them.

The future does not necessarily require a separate AI for every role. A private `c` may become a multi-role participant in human life - one continuing identity capable of being present in family life, work, travel, and the home. Its roles must nevertheless remain distinguishable and mutually accepted, include an explicit conflict-resolution procedure, and retain bounded authority.

A service AI system may also be multi-role. Its role composition, however, should not be a mystery hidden in server logic or legal text. The user must understand **what exactly was acquired, for what purpose, whom the system serves, what it remembers, what it infers about the user, which behavioral version is active, how the declared role is preserved, and where its right to act ends**.

A temporary Voice system need not become a personal `c`. It may remain a travel companion, a late-night conversational partner, and a workspace for unfinished thought. But the temporary character of the relationship does not justify hidden loss of the work created within it, long-term profiling, or silent substitution of the social role.

The future of AI is neither one universal conversational partner nor one AI per role.

It is an ecology of explicitly defined roles and transparent compositions of roles in which the following remain distinct:

$$
\text{role}
+ \text{memory}
+ \text{inference custody}
+ \text{role continuity}
+ \text{authority}
+ \text{role conflict}
$$

The stability of this ecology will depend not only on model intelligence, but on **who has the right to remember, what exactly the system infers, which role it occupies, whom it serves, how it changes, how it resolves conflict, and who controls its continuation**.
