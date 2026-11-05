---
title: Your AI Remembered. That Was the Problem.
date: 2026-10-28
slug: your-ai-remembered-that-was-the-problem
summary: A reflection on when valid historical memory becomes unsuitable advice, with a bounded discussion of the MemDev-Bench preprint.
tags: AI, AIMemory, SoftwareEngineering, PersistentAI, HumanAI, AIResearch, AdvancedGlobalIntelligence
primary_image: assets/diary/your-ai-remembered-that-was-the-problem/cover.jpg
image_alt: Hands hold a removed metal cover beside a machine and an open book of technical drawings on a workbench.
linkedin_url: https://lnkd.in/p/eAtRHnR8
---

Your AI Remembered. That Was the Problem.

"We solved this last time."

A useful sentence. Until it becomes a reason to stop checking what has changed.

A 20 October preprint, MemDev-Bench, examines memory in coding agents. The results are not simply good or bad: memory helped solve some difficult tasks, but also introduced failures on tasks the agent could solve without it.

The authors traced failures to historical solutions applied under incompatible assumptions, transferred to the wrong component, or followed despite conflicting feedback. Even relevant history did not guarantee appropriate reuse.

The evaluation covers one agent-model configuration on a software-engineering benchmark. It is not a verdict on every AI memory system. But it exposes a failure worth designing against.

The uncomfortable point: a memory does not have to be fabricated to become bad advice.

Imagine a maintenance record describing a setting that solved a machine's problem last year. Since then, a component has been replaced and the operating load has changed. The record is still accurate. Repeating its recommendation may not be.

Deleting the record would lose useful experience. Treating it as a permanent instruction would make a different mistake.

I have argued that a person's accumulated experience could become a major AI advantage. I still believe that. But making history available is not the same as knowing how to use it.

For long-lived AI, I want the distinction to remain visible between what happened, what we concluded at the time, and what we have reason to do now.

A correction should not require pretending the earlier event never happened. Nor should respect for history prevent a system from revising its interpretation.

An old workaround deserves a question: does the condition that made it necessary still exist?

An earlier preference deserves another: has the person changed their mind?

This also changes what I would ask from a memory demonstration. Show me the tasks it rescued, but also the tasks it broke. Compare the same work with and without the added history, rather than showing only impressive examples of recall.

A larger archive is not automatically a better relationship with the past.

Sometimes the most useful answer is not "I remember how we did it."

It is: "I remember why we did it. That reason no longer applies."

Research: MemDev-Bench, arXiv:2610.27524.
