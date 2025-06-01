---
layout: post
title: "Benchmarking AI Vision"
date: 2024-06-28
last_updated: 2024-06-28
description: "Surveys vision-language benchmark suites, reporting model performances on image-text tasks and outlining evaluation best practices."
tags: [ai, vision, benchmarks, llm]
---

Ethan Mollick, Associate Professor at The Wharton School, recently [shared](https://www.linkedin.com/posts/emollick_we-are-seeing-the-first-practical-benchmarks-ugcPost-7212463694503440384-xhAp?utm_source=share&utm_medium=member_desktop) two key developments:

1. The [Charxiv benchmark](https://charxiv.github.io/#leaderboard), a challenging real-life chart reading test, where humans achieve 80% accuracy. Interestingly, Claude 3.5, currently the best-performing Large Language Model (LLM) in this test, manages 60% accuracy.

2. The [Chatbot Arena](https://chat.lmsys.org/), which compares AI vision answers based on human preferences. In this arena, GPT-4o emerges as the winner.

As Mollick notes, "We are seeing the first practical benchmarks for AI vision."

However, I noticed a crucial omission in the Chatbot Arena: the absence of Reka AI models, which I've found particularly impressive for their concise outputs.

Another benchmark, the WildVision leaderboard, does include Reka Flash. It's available on [Hugging Face](https://huggingface.co/spaces/WildVision/vision-arena). 

When I inquired on X, Wei-Lin Chiang, one of the researchers behind the Chatbot Arena, confirmed that they "will add soon" the Reka models to their benchmark.