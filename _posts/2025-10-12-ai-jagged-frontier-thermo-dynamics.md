---
layout: post
title: "AI Jaggedness vs Transition Turbulence"
date: 2025-10-12
tags: [llm, safety, alignment]
last_updated: 2025-10-12T22:31:00+02:00
author: "Nils Durner"
categories: [journal]
---

Ethan Mollick describes [the Jagged Frontier of AI](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged) as strong performance on some tasks, brittle or poor performance on others that look similarly hard to humans. It is tempting to assume this frontier advances smoothly over time - as is usual with technological progress.

Helen Toner - interim executive director at Georgetown University’s Center for Security and Emerging Technology (CSET) and former OpenAI board member - adds a useful correction. In a recent talk, she contrasts such "smooth asymptotes" with "transition turbulence": progress arrives in thresholds and phase changes, not tidy curves. As possibilities of AI change - through technical progress and through policy, and through the disturbances and reactions that follow - the chaotic transitions in fluid heating are a better mental model than a single curve.
![Slide by Helen Toner: Smooth asymptotes vs. transition turbulence. Photo courtesy Neil Chilson](assets/img/toner-fluid-dynamics.jpg)

 That matters for capability expectations and for policy.
 ![Slide by Helen Toner: So what. Photo courtesy Neil Chilson](assets/img/toner-fluid-dynamics-so-what.jpeg)

### Jaggedness, two ways

The kind of jaggedness that Mollick described is the first kind: **competence jaggedness** across tasks. Inside the frontier, LLMs boost speed and quality. Outside it, they can hurt performance. The boundary is uneven and hard to see a priori. That description does not account for how the frontier line itself moves - over time, across providers, etc.

Another kind is **access jaggedness**. The same model family can present different capability surfaces depending on who asks, in what context, and through which route of access. Safety policies, imperfect training signals, provider rules and trusted-access programs create policy thresholds that yield an uneven - sometimes shifting - profile.

Germany’s regulated trades, for instance, define protected occupations and clear paths to qualification. Access jaggedness in AI does not. Instead, **functionally protected activities** emerge through private gates: identity checks, API terms, risk classifications, review processes, and trusted-access arrangements in dual-use areas.

In AI specifically:
- During my red-teaming efforts on gpt-oss, GPT-5 often shifted register toward safety, and refused to assist with benign copy-editing. That behavior lines up with the published move from hard refusals to **safe-completions**, and with usage policies that disallow malicious cyber activity.
- On the other hand, trusted access for vetted life science practitioners is now formal policy. Per the System Card: "Under this program, if access is granted, the model will provide detailed responses to dual-use prompts, while still blocking weaponization generations."
- Fellow presenters at the [gpt-oss red-teaming workshop](kaggle-red-teaming-challenge-openai-gpt-oss-concluded) reported sucessfully using Chinese open-weights models for certain security tasks. Reports show, however, that quality varies across providers, sometimes varying greatly (> 50%) from the Chinese vendor's reference offering.

This has, in consequence, distributional effects. Toner asks who benefits, who loses, who has power, who is provoked. Access gates temper AI risk at the **field** level, and as a side effect temper AI risk at the **occupation** level by reducing immediate replacement by "drop-in" workers uplifted by AI. These are not legally protected occupations, but power shifts toward gatekeepers and away from open substitution. In generic office work there is less of this protection, so substitution pressure feels more direct.

My read of "don’t hold your breath for drop-in remote workers" per Toner's slide is consistent with that: frictions remain - tacit knowledge, liability, compliance, team integration - and in dual-use domains the access surface - remains uneven as it sometimes is intentional already. At the same time, disruption of existing power structures is still to be expected.

The mental model of the "Jagged Frontier" doesn't leave room for these considerations - but that of "Transition Turbulence" does.