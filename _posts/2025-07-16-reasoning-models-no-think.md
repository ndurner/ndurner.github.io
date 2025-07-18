---
layout: post
title: "Cutting Thinking with Reasoning Models"
date: 2025-07-17
tags: [llm, openai, o1, kimi]
last_updated: 2025-07-17
author: "Nils Durner"
categories: [journal]
---

GPT-4.5 was discontinued on the OpenAI API earlier this week (but continues to be available through paid ChatGPT plans). This leaves a gap for an LLM that offers sufficiently current world knowledge baked-in that also covers niches. I briefly tried Kimi-K2, a newly released Chinese model with 1 Trillion parameters, and the results I got were decent but not as stellar as with GPT-4.5. This matches the SimpleQA benchmark where GPT-4.5 scores 62.5% (at a 37.1% hallucination rate) versus K2's score of 31.0%. Anthropic Opus 4, which hallucinated in my tests, scores 22.8%, and GPT-4.1 scores 42.3.

New idea: perhaps use o3 instead? This scores 49% on SimpleQA, with a hallucination rate of 51%. Sure enough, it has me encoded in its weights, perhaps from ingesting Open Source code bases and perhaps mailing lists as well. To cut latency (and cost), user Xeophon offers [this trick](https://x.com/xeophon_/status/1944139161000128892):
> Drop your inference times BY 30-40% with THIS SIMPLE TRICK: Add /no_think to the prompt

and "Florian S" adds:
> For many models, e.g. R1 it works best to end the prompt with \
\<thinking> \
\</thinking> \
Makes the model believe the thinking stage is already done

In my limited, manual testing, appending "/no_think" to o3 with "low reasoning effort" further decreases the reasoning tokens spent. Now, the question is whether accuracy, e.g. on SimpleQA, suffers or not.