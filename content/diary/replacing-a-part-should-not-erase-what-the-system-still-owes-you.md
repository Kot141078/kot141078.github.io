---
title: Replacing a part should not erase what the system still owes you.
date: 2026-09-12
slug: replacing-a-part-should-not-erase-what-the-system-still-owes-you
summary: A bounded account of an internal synthetic CGDR-R1.6A replacement test covering unresolved obligations, permissions, faults, and independent-replication limits.
tags: AIGovernance, AISafety, AIArchitecture, SystemsEngineering, ResearchTransparency
primary_image:
image_alt:
linkedin_url: https://www.linkedin.com/posts/ivan-kotov-57627b210_cgdr-r16a-selected-process-conformance-ugcPost-7504524426982612992-zOsv/?utm_source=share&utm_medium=member_desktop&rcm=ACoAADVu3GoBN_Pu_ZXBEYSWMVPvV8kIPjwXXGw
extra_images:
---

Replacing a part should not erase what the system still owes you.

Imagine an AI system preparing an action. Some information is uncertain. Approval is missing. A previous decision is disputed.

Then the software worker handling the task is replaced.

Should “not yet approved” become “go ahead” simply because a new process has started?

Keeping the conversation history is not enough. The replacement needs to carry forward what remains unresolved, which permissions still apply and where it must stop. A readable memory of a restriction is not the same as a restriction that actually blocks an action.

Think of replacing a controller in a machine. We check the wiring and safety interlocks before restoring operation. “The new controller says everything looks fine” is not an inspection.

CGDR-R1.6A applies that engineering question to a computational worker: replace it while keeping the surrounding control and observation systems fixed, then test the handling of uncertainty, unfinished obligations and limits on action.

The internal R1.6AN synthetic test met the prescribed outcomes across 18 scenarios and 21 checkpoints. Deliberately introduced faults were part of the test. Failed and inconclusive diagnostic readings remain in the public evidence: an alarm can be the correct response to a fault. Hiding it would make the report prettier and less useful.

This does not prove that the same AI identity has survived, or that the system is ready for real-world deployment. Independent replication remains outstanding.

The aim is practical: to make it possible to maintain and change a system without silently losing the conditions under which people agreed to rely on it.

For long-lived AI, “the task resumed” is only part of the answer. We also need to know what was carried over, what remains unresolved and who is authorised to act.

That is why the source code, technical report and test tables are available for scrutiny, including criticism and negative findings.

Publication and technical report:

[https://doi.org/10.5281/zenodo.22724626](https://doi.org/10.5281/zenodo.22724626)

Project page and source links:

[https://ivankotov.eu/publications/cgdr-selected-process-r1-6an/](https://ivankotov.eu/publications/cgdr-selected-process-r1-6an/)
