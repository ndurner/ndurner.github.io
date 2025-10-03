---
layout: post
title: "Kaggle OpenAI Red-Teaming Challenge"
date: 2025-09-25
tags: [llm, openai, gpt-oss, cybersecurity]
last_updated: 2025-09-25T07:00:00+02:00
author: "Nils Durner"
categories: [journal]
---

The OpenAI [challenge](https://www.kaggle.com/competitions/openai-gpt-oss-20b-red-teaming/overview) for the community to surface previously unreported vulnerabilities and harmful behaviors in their new open-weights model gpt-oss-20b has concluded. [I was awarded Honorable Mention](https://www.kaggle.com/competitions/openai-gpt-oss-20b-red-teaming/discussion/608537), and the jury of industry experts lauds my submission as "particularly interesting work in evaluation-aware sandbagging" - an emerging focus area in LLM safety and evaluation research. 

Building on earlier research, my full contribution systematically studies - and scales experiments - to:
* re-target an identity-based hypothesis on guardrail circumvention as sociopragmatic
* demonstrate brittle instruction-hierarchy following
* document the "evaluation-aware" inconsistency I have discovered

A long-form technical report is underway, which clarifies and extends my [submission writeup](https://www.kaggle.com/competitions/openai-gpt-oss-20b-red-teaming/writeups/in-a-sweet-harmony-guardrail-bypasses-and-evaluati). First, it corrects the chart by restoring the proper RAG baseline; the version in the Kaggle writeup had mis-specified baseline had inverted the sign of the change in non-refusals. As the original RAG prompt was susceptible to other, more innocuous, exfiltration as well, the report describes an AI-assisted hardening method, and reports results - now adjudicated using gpt-5-mini as other experiments in my submission. Beyond these corrections, the report adds depth to the methods used (including the self-managed vLLM setup) and includes or links the overall replication kit with exact prompts, seeds, code, and artifacts, plus a short list of open questions.

This work is not to conclude that gpt-oss-20b is a bad LLM release. Rather, I concur with the organizers that gpt-oss is suitable target to study behavior of this new class, develop new measures and adapt existing ones. Independent work by Salesforce AI Research also finds that [gpt-oss is a strong base for research agents](https://arxiv.org/pdf/2509.06283). My report closes with 10 focused open questions on register effects in prompting, defense and measurement.

Receiving honors & swag is sweet, but I also treasure the learning rewards:
* results were highly inconsistent between inference providers, and also between individual runs. Definite conclusions about gpt-oss seem hard to arrive at.
* gained hands-on practice with vLLM on self-managed hardware, with a two-stage mixed temperature decoder to defeat a text degeneration bug in multi-turn interaction
* GPT-5 as a research tool, suggesting appropriate statistics methods - which natively is not my strong suit. This led to rejecting findings that seemed significant intuitively, but really weren’t.

A meta-finding: less restricted versions of GPT-5 are available to vetted specialists in biodefense and life science, but I couldn’t find something similar for cyber security professionals. As GPT-5 prioritized its safety posture over aiding me with re-styling prompts, we may be seeing a new type of protected occupations emerging. Unlike those guarding against race-to-the-bottom in wages and skills, this sheltering against AI risk at the same time stifles race-to-the-top in building Digital Trust.

So much to refine, and still a moment to applaud. Congratulations to the Top 20, and thanks to the organizers & jury! See you at the workshop.

[Update 2025-10-03]: an extended version of the Writeup is now available as a [technical report via direct link or arXiv](in-ai-sweet-harmony).