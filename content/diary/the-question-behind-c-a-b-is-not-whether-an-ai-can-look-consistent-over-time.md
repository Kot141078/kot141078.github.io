---
title: The question behind c = a + b is not whether an AI can look consistent over time.
date: 2026-07-18
slug: the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time
summary: A Cleanroom ARM-P note framing open verification as the control-side infrastructure needed to make c = a + b falsifiable.
tags: AIResearch, AIVerification, ReproducibleResearch, SoftwareVerification, AIGovernance, OpenScience, LongTermAIMemory
primary_image: assets/diary/the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time/cover.jpg
image_alt: Cleanroom ARM-P open verification graphic showing c = a + b and four control-side evidence steps.
linkedin_url: https://www.linkedin.com/posts/ivan-kotov-57627b210_airesearch-aiverification-reproducibleresearch-activity-7484235843713470464-vLHo?utm_source=share&utm_medium=member_desktop&rcm=ACoAADVu3GoBN_Pu_ZXBEYSWMVPvV8kIPjwXXGw
extra_images:
---

The question behind c = a + b is not whether an AI can look consistent over time. A sufficiently strong persistent profile, given the same records and comparable memory, may reproduce that surface.

So the real question is harder:

Does a system formed sequentially through time, disturbance, memory and irreversible commitments retain any measurable path-dependent structure that the strongest one-shot reconstruction from the identical information source cannot reproduce?

That question cannot be answered without a serious control arm.

Cleanroom ARM-P is the open-verification foundation for that control side. It provides a signed and reproducible fixture-plane implementation for evidence export, schema-governed validation, isolated state, SQLite transaction and recovery controls, fail-closed transitions, and exact provenance.

Its purpose is not to prove c.

Its purpose is to make c falsifiable.

A future matched experiment must hold the model, corpus, disturbance stream, prompt/interface surface and comparable memory access as equal as possible. The grown c-candidate and the profile-control may differ only in formation path.

If the control reproduces everything, the result is null — and that result must be published. If a residual remains above the measured noise floor and survives blind independent replication, then we have a bounded operational finding about path dependence, not a claim about consciousness, life or personhood.

The current release does not report such a residual. It publishes the control-side infrastructure openly so others can inspect it, reproduce it, attack it and improve it.

Use it as a control architecture, a reproducibility pattern, or a starting point for independent replication.

Read:
[https://ivankotov.eu/publications/cleanroom-arm-p-open-verification-v1-0-1/](https://ivankotov.eu/publications/cleanroom-arm-p-open-verification-v1-0-1/)

Canonical archive:
[https://doi.org/10.5281/zenodo.21401893](https://doi.org/10.5281/zenodo.21401893)

Source:
[https://github.com/Kot141078/cleanroom-arm-p-open-verification](https://github.com/Kot141078/cleanroom-arm-p-open-verification)
