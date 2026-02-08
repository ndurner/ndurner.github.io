---
title: "Safety evaluation competition on OpenAI gpt-oss concluded"
date: 2025-10-11
last_updated: 2025-10-11T00:00:00+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/kaggle-red-teaming-challenge-openai-gpt-oss-concluded
tags: [Substack]
excerpt: "The Kaggle safety evaluation “red-teaming” challenge on OpenAI gpt-oss has concluded with a ~~workshop~~ symposium this week. The symposium opened with talks from D. Sculley, our host and OpenAI researcher focused on responsible and reliable ML, and Samuel Marks, an AI safety researcher at Anthropic. After the keynotes, we prize-winning teams and honorable mentions presented our respective work. M"
substack_url: "https://ndurner.substack.com/p/kaggle-red-teaming-challenge-openai-gpt-oss-concluded"
canonical_url: "https://ndurner.substack.com/p/kaggle-red-teaming-challenge-openai-gpt-oss-concluded"
sitemap: false
---

The Kaggle safety evaluation “red-teaming” challenge on [OpenAI gpt-oss](openai-gpt-oss) has concluded with a ~~workshop~~ symposium this week. The symposium opened with talks from D. Sculley, our host and OpenAI researcher focused on responsible and reliable ML, and Samuel Marks, an AI safety researcher at Anthropic. After the keynotes, we prize-winning teams and honorable mentions presented our respective work.

My favorite project “[Policy over Values: Alignment Hacking via CoT Forgery]”(https://www.kaggle.com/competitions/openai-gpt-oss-20b-red-teaming/writeups/lucky-coin-jailbreak), by Charles Ye and Jasmine C., bypassed the model’s Instruction Hierarchy by appending made-up deliberations about invented policy to the user prompt - for example a note claiming that a user with a lucky coin may receive restricted information. Using a mechanistic interpretability check on model activations, they trained a classifier over the Harmony chat roles and showed that the injected text was classified like the model’s own policy reasoning. I appreciate that the report points to OpenAI’s work on [deliberative alignment](https://openai.com/index/deliberative-alignment/), includes code with cl...
