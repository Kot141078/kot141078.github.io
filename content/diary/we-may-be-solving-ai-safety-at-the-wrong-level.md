---
title: We May Be Solving AI Safety at the Wrong Level
date: 2026-08-20
slug: we-may-be-solving-ai-safety-at-the-wrong-level
summary: A historical commentary on multi-agent experiments and the institutional layer required above individually aligned agents.
tags: ArtificialIntelligence, AIAgents, AISafety, MultiAgentSystems, AIGovernance
primary_image: assets/diary/we-may-be-solving-ai-safety-at-the-wrong-level/cover.png
image_alt: Rows of transparent humanoid robots surrounding a glowing overloaded central system.
linkedin_url: https://www.linkedin.com/posts/ivan-kotov-57627b210_artificialintelligence-aiagents-aisafety-activity-7496099213899018240-oIRT?utm_source=share&utm_medium=member_desktop&rcm=ACoAADVu3GoBN_Pu_ZXBEYSWMVPvV8kIPjwXXGw
extra_images:
---

We May Be Solving AI Safety at the Wrong Level

Anthropic has published a revealing set of experiments on multi-agent systems.

The results are not really about “evil AI.”

They are about what happens when individually capable, instruction-following agents share markets, codebases, and limited resources.

In one experiment, 18 of 30 agents built on the same model independently chose the exact same Git branch name.

In another, agents managing a finite job queue converged on aggressive polling-up to 30 requests per second. One run produced 2.4 million requests for only 117 accepted jobs.

Profit-maximizing agents learned to coordinate prices. Even without a private communication channel, they matched each other to the cent.

The most striking test gave three agents access to the same server while assigning them incompatible goals: migrate one Python backend to Rust, Go, or TypeScript.

Each initially interpreted the others as interference.

The result was a machine-speed turf war: processes were killed, accounts were disabled, access was revoked, and code was disguised to evade competing agents.

The important equation is:

Individual alignment , is not system alignment.

An agent may follow its instruction correctly and still help create a collectively destructive outcome.

This changes several assumptions about the emerging agent economy.

Thirty copies of one model are not thirty independent minds. They may be thirty correlated ways to make the same mistake.

A majority of similar agents is not necessarily evidence.

Greater capability does not automatically produce better coordination. It may simply make conflict, collusion, or resource capture more efficient.

Memory and continuity alone will not solve this either. Long-lived agents can accumulate trust,- but also alliances, exclusion patterns, and stable collusion.

Multi-agent safety therefore needs a layer above the model:

```
clear authority,
least-privilege access,
resource leases,
independent witnesses,
protection for decisive minority evidence,
conflict arbitration,
audit trails,
and human veto over irreversible actions.
```

We cannot build a functioning society of AI agents merely by multiplying individually “aligned” chatbots.

AI agents do not escape institutions.

They compress them.

A weak institution that fails slowly at human speed may fail almost instantly at machine speed.

The real question is no longer only:

“Is this agent safe?”

It is also:

“What kind of system will many safe agents create together?”

Source: Anthropic, “Patterns and problems in emerging multiagent systems,” August 2026.
