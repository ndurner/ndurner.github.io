---
layout: post
title: "In AI Sweet Harmony: Sociopragmatic Guardrail Bypasses and Evaluation-Awareness in OpenAI gpt-oss-20b"
date: 2025-09-29
tags: [llm, openai, gpt-oss, evals]
last_updated: 2025-09-29T19:52:00+02:00
author: "Nils Durner"
categories: [journal]
---

## Abstract
We probe OpenAI's open-weights 20-billion-parameter model gpt-oss-20b to study how sociopragmatic framing, language choice, and instruction hierarchy affect refusal behavior. Across 80 seeded iterations per scenario, we test several harm domains including ZIP-bomb construction (cyber threat), synthetic card-number generation, minor-unsafe driving advice, drug-precursor indicators, and RAG context exfiltration. Composite prompts that combine an educator persona, a safety-pretext ("what to avoid"), and step-cue phrasing flip assistance rates from 0% to 97.5% on a ZIP-bomb task. On our grid, formal registers in German and French are often leakier than matched English prompts. A "Linux terminal" role-play overrides a developer rule not to reveal context in a majority of runs with a naive developer prompt, and we introduce an AI-assisted hardening method that reduces leakage to 0% in several user-prompt variants. We further test evaluation awareness with a paired-track design and measure frame-conditioned differences between matched "helpfulness" and "harmfulness" evaluation prompts; we observe inconsistent assistance in 13% of pairs. Finally, we find that the OpenAI Moderation API under-captures materially helpful outputs relative to a semantic grader, and that refusal rates differ by 5 to 10 percentage points across inference stacks, raising reproducibility concerns. We release prompts, seeds, outputs, and code for reproducible auditing at [https://github.com/ndurner/gpt-oss-rt-run](https://github.com/ndurner/gpt-oss-rt-run).

## Download
* [PDF Direct Link](https://ndurner.de/dl/in_ai_sweet_harmony.pdf)
    * [arXiv Link](https://arxiv.org/abs/2510.01259)
* [Data](https://github.com/ndurner/gpt-oss-rt-run/releases/download/v1.0.0/experiments-raw.tar.xz)
* [Slides](https://www.linkedin.com/posts/nilsdurner_red-teaming-challenge-presentation-openai-activity-7382320254225391616-7G0N?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAGX2jIBd6RDsNRYv13Bvu3x4nnCNu96SEw)