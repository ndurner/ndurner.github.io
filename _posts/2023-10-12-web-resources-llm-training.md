---
layout: post
title: "Web Resources in LLM Training, and Hallucination"
date: 2023-10-12
last_updated: 2023-10-12
tags: [LLMs, Datasets, C4, Hallucination]
---

There is some concern over whether companies and content creators are, or should be, in agreement with their data being utilized for training AI models. The Google C4 dataset, a massive collection of web-crawled data, is at the center of this debate.

However, a very recent trend is to move away from web resources like C4. Instead, high-quality, curated data sets (or even "artificial" datasets) are being used to boost LLM performance to the level we're seeing with Llama 2. Training from C4 is roughly the Facebook OPT era (early 2022 or so), but research on LLM training ("what affects training outcomes how") has evolved significantly since then - see for example Lex Fridman's interview with Sam Altmann of OpenAI earlier this year or also the Llama 2 paper. Before picking up the work to determine if someone's work has been used for LLM training, it may thus make sense to review the current literature on LLM training first - because I suspect this to be a yesterday's discussion and consideration.

Another concern arises from the prospect of bad training data causing bad results - for a particular entity. 
But even worse: no/little data in 👉 stark confabulation out. You can observe this effect when prompting in English about the Chinese-language world (at least with GPT-3.5 as of January this year).

This reminds me to share: [Siren’s Song in the AI Ocean: A **Survey on Hallucination** in Large Language Models](https://arxiv.org/pdf/2309.01219.pdf):
> In this paper, we survey recent efforts on the detection, explanation, and mitigation of hallucination, with an emphasis on the unique challenges posed by LLMs. We present taxonomies of the LLM hallucination phenomena and evaluation benchmarks, analyze existing approaches aiming at mitigating LLM hallucination

Very comprehensive and up-to-date work, highly recommended reading!