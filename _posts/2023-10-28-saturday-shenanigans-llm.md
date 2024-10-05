---
layout: post
title: Large Language Models as General Pattern Machines
date: 2023-10-28
last_updated: 2023-10-28
tags: [Large Language Models, General Pattern Machines]
filename: 2023-10-28-saturday-shenanigans-llm-gpm.md
---

Maybe Saturday Shenanigans, maybe not: "[Large Language Models as General Pattern Machines](https://arxiv.org/pdf/2307.04721.pdf)":

> Large language models (LLMs) are trained to absorb the myriad of patterns that are woven into the structure of language. [...] A key observation of our work—and perhaps contrary to the predominant intuition—is that an LLM’s ability to represent, manipulate, and extrapolate *more abstract, nonlinguistic patterns may allow them to serve as basic versions of general pattern machines*. [...] Surprisingly, we find this extends beyond ASCII numbers, and that when they are replaced with a mapping to randomly sampled tokens in the vocabulary, LLMs can still generate some valid solutions. These results suggest an intriguing insight: that LLMs may exhibit more general capabilities of representing and extrapolating symbolic patterns, invariant to the specific tokens involved.

Fascinating prospect that there may be something more profound to what is thought of as mere Models of Language, beyond the controversy around the world knowledge that is - or is not - encoded and how it may - or may not - be ethically expressed, and calls for regulation.

> While difficult to deploy today for real systems due to latency, context size limitations, and compute costs, the approach of using LLMs to drive low-level [robotic] control may provide an exciting glimpse into how the patterns among words could be transferred to [robotic] actions.

For those interested in this, it makes sense to watch reported improvements on the ARC benchmark. However:

> The ARC is a difficult benchmark, and the performance falloff can be steep (and relatively uninformative) across LLMs with decreasing model size and data scale, making it difficult to measure incremental progress towards pattern machines that could be used for sequence transformation in robotics. Therefore, we introduce an adjustable difficulty benchmark [...PCFG...]. This benchmark provides a more unbiased evaluation of pattern reasoning capabilities in LLMs; PCFG completion accuracy improves with model scale, and correlates with ARC performance.

Outlook:

> We expect many of these [robotic use-case] abilities to continue improving as large models expand from learning patterns within language-only datasets to multimodal domains (e.g., images, videos).

**Definitely** Saturday Shenanigans:\
![IMG_7517](assets/img/midjourney-v6.jpg)\
 ([via](https://x.com/javilopen/status/1716959242962211037?s=61&t=1UkXMLzJuVuAu7tEUWoR3w))
