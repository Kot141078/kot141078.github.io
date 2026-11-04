---
title: AI Agents Must Be Adaptive, Not Just Repeatable
date: 2026-10-03
slug: ai-agents-must-be-adaptive-not-just-repeatable
summary: An authorial engineering account distinguishing controlled repeatability from adaptability across different computing environments.
tags: AI, AIAgents, SoftwareEngineering, SystemsEngineering, LocalAI
primary_image: assets/diary/ai-agents-must-be-adaptive-not-just-repeatable/cover.jpg
image_alt: Three robotic vehicles carry protected porcelain vases across rocky ground, sand, and a river.
linkedin_url: https://lnkd.in/p/e7xQav9J
---

AI Agents Must Be Adaptive, Not Just Repeatable

Twenty successful runs in one controlled environment tell us something valuable.

They do not tell us what happens when the environment changes.

I encountered this while developing the software skeleton for my long-lived AI systems.

After improving Liya on Linux, I wanted to transfer those improvements to Ester on Windows and Rita on a DGX Spark. I started with Rita. Also Linux. It seemed the more straightforward step.

The implementation did not transfer cleanly.

I am now developing the systems separately, guided by the same theory, but with substantially different code.

The goal stayed the same. The engineering problem did not.

Processor architecture, memory, drivers, dependencies, permissions and existing runtime state are part of the task. Change them, and the path to a correct result may change too.

Repeatability asks: Can you do this reliably here, from the same starting conditions?

Adaptability asks: Can you recognise what changed and find a valid way to achieve the required outcome elsewhere?

An engineering agent should not force Rita to behave like Liya. It should inspect the environment, identify which assumptions no longer hold, and choose an implementation that preserves the required guarantees.

Reuse portable code where it works. Replace platform-specific mechanisms where necessary. Do not quietly weaken the requirements just to report success.

The code may change. What must remain true should not.

Sometimes the environment cannot support the required result. Recognising that limitation, identifying the missing prerequisite and stopping honestly is part of adaptability too.

These are different tests. Controlled repetition measures one property. Transfer across environments measures another.
For engineering agents expected to work beyond a single controlled setup, we need both.

The objective is not identical commands on every machine.

It is equivalent guarantees through different implementations.

Portability should be tested at the level of guarantees, not just source files.
