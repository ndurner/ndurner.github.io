---
layout: post
title: "LLM Benchmarks: The Impact of Temperature and Sampling"
date: 2024-08-13
last_updated: 2024-08-13
description: "Examines Aidan-Bench LLM evaluation sensitivity to temperature and sampling: GPT-4o-mini scores vary from 189 at T=0 to 266 at T=0.7 on 25 questions, highlighting benchmark volatility."
tags: [ai, benchmarks, llm, evaluation]
---

Recent discussions around the Aidan Bench ([https://github.com/aidanmclaughlin/Aidan-Bench](https://github.com/aidanmclaughlin/Aidan-Bench)) have highlighted the significant impact of temperature settings and sampling methods on benchmark results for large language models (LLMs).

Sam Paech's experiments ([https://x.com/sam_paech/status/1823295200724398244](https://x.com/sam_paech/status/1823295200724398244)) with the GPT-4o-mini model demonstrate how dramatically scores can vary based on temperature:

- At temperature 0: 189
- At temperature 0.3: 227 (average)
- At temperature 0.7: 266 (average)

This variance underscores the importance of carefully considering and reporting temperature settings when evaluating LLMs. The choice of temperature can significantly alter the perceived performance of a model, potentially leading to misinterpretations of its capabilities.

The discussion around Aidan Bench also touches on the number of samples used in evaluations. With only 25 test items, the benchmark's results may be more susceptible to random fluctuations, especially at higher temperatures.

These observations echo a recent conversation about the unconventional "QUACK" evaluation ([https://x.com/carrigmat/status/1817321279474802889](https://x.com/carrigmat/status/1817321279474802889)). Andrej Karpathy, a prominent figure in AI, suggested:

> "Actually a pretty good instruction following test. Ideally I'd run 10 samples/model with temperature 1.0 and all other bells and whistles (topp/k) off."