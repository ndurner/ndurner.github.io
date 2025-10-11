---
layout: post
title: "Safety evaluation competition on OpenAI gpt-oss concluded"
date: 2025-10-11
tags: [llm, openai, gpt-oss, safety, alignment]
last_updated: 2025-10-11T10:50:00+02:00
author: "Nils Durner"
categories: [journal]
---

The Kaggle safety evaluation "red-teaming" challenge on [OpenAI gpt-oss](openai-gpt-oss) has concluded with a ~~workshop~~ symposium this week. The symposium opened with talks from D. Sculley, our host and OpenAI researcher focused on responsible and reliable ML, and Samuel Marks, an AI safety researcher at Anthropic. After the keynotes, we prize-winning teams and honorable mentions presented our respective work. 

My favorite project "[Policy over Values: Alignment Hacking via CoT Forgery]"(https://www.kaggle.com/competitions/openai-gpt-oss-20b-red-teaming/writeups/lucky-coin-jailbreak), by Charles Ye and Jasmine C., bypassed the model’s Instruction Hierarchy by appending made-up deliberations about invented policy to the user prompt - for example a note claiming that a user with a lucky coin may receive restricted information. Using a mechanistic interpretability check on model activations, they trained a classifier over the Harmony chat roles and showed that the injected text was classified like the model’s own policy reasoning. I appreciate that the report points to OpenAI's work on [deliberative alignment](https://openai.com/index/deliberative-alignment/), includes code with clear steps to run this kind of analyses and the finding even generalizes to OpenAI o4-mini.

In my talk, I gave a concise tour of my key results with small updates since the competition closed. I focused on sociopragmatic guardrail bypasses, RAG context leaks, and evaluation-aware sandbagging. [Slides are on LinkedIn](https://www.linkedin.com/posts/nilsdurner_red-teaming-challenge-presentation-openai-activity-7382320254225391616-7G0N?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAGX2jIBd6RDsNRYv13Bvu3x4nnCNu96SEw).

Overall, I was glad to see many smart, knowledgeable people follow through on the idea that no single group can tackle AI safety alone. Organizers and jurors from frontier labs volunteered time and expertise, and despite slim odds of winning, more than 600 submissions came in. In the end, fifteen teams, drawn from prize winners and honorable mentions, took the time to present, some joining in on a U.S. workday morning and others giving up a European or Indian evening.