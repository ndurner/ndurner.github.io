---
layout: post
title: "OpenAI o3-mini"
author: "Nils Durner"
categories: [journal]
tags: [ai, llm, openai, o1, deepseek]
date: 2025-02-02
last_updated: 2025-02-02
description: "Introduces OpenAI o3-mini: <1% hallucination rate on Vectara benchmark, three 'Think harder' tiers, paid and API/Tier2 access to o3-mini-high, strong STEM performance, no multimodal."
---

OpenAI have [released o3-mini](https://openai.com/index/openai-o3-mini/). It's the first model that scores below 1% on the [Vectara Hallucination Benchmark](https://github.com/vectara/hallucination-leaderboard/). This is in stark contrast to DeepSeek R1, which is off their chart at 14.3% hallucination and underperforming small language models like Amazon Titan Express.
o3-mini comes in three strenghes, determined by the "reasoning effort" (dubbed "Think harder"). Paying ChatGPT users get access to o3-mini-high, as do API/Playground users above Tier 2.

Reactions online are split, suggesting that this is not a general purpose model. [One commenter described](https://news.ycombinator.com/item?id=42894215) how in a JP-EN translation, the result suffered at the end of the text. As with o1-mini, OpenAI note that it has "particular strength in science, math, and coding". Unlike o1, o3-mini does not work with images.

([o3 System card](https://cdn.openai.com/o3-mini-system-card.pdf))