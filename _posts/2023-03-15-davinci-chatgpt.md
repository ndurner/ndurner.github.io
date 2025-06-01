---
layout: post
title: "text-davinci-003 vs. ChatGPT: a short technical note"
author: "Nils Durner"
categories: journal
tags: [openai,gpt]
date: 2023-03-15
last_updated: 2025-05-30
description: "Brief comparison of deterministic text-davinci-003 output with the higher-temperature ChatGPT settings available in March 2023, and a remark on the then-upcoming GPT-4 API."
---

During a discussion in March 2023 a colleague asked why _text-davinci-003_ produced concise, predictable answers, whereas ChatGPT tended to be more verbose and occasionally digressive. The explanation is largely technical.

**Model family**   _text-davinci-003_ belongs to the GPT-3 series. ChatGPT, at that point in time, was powered by GPT-3.5 and had been further refined with reinforcement learning from human feedback (RLHF) to optimise dialogue.

**Temperature**   The colleague had set `temperature = 0` for _text-davinci-003_. This makes sampling almost deterministic. The public ChatGPT interface used a noticeably higher temperature (OpenAI never published the exact value; empirical tests indicated ≈ 0.7). Higher values increase the probability of less frequent tokens, resulting in more diverse—but also less reproducible—output.

Choosing the right setting depends on the task. Low temperature is appropriate for automated pipelines that must yield identical results across runs, e.g. code generation or regulatory text. A higher temperature can be helpful for brainstorming or creative writing, where variety is an asset.

At the same time OpenAI announced the GPT-4 API wait-list. Early benchmark data suggested a significant improvement in factual accuracy and reasoning while retaining the familiar sampling parameters (temperature, top-p, etc.). I therefore recommended registering for early access.

In retrospect (writing in 2025) both GPT-3 and GPT-3.5 have been superseded by GPT-4 and later models. Nonetheless, the principle remains: understand and control the generation parameters instead of relying on default settings.