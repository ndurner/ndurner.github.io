---
title: "OpenRouter AI inference hub pitfalls"
date: 2026-09-12
last_updated: 2026-09-12T14:05:10+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/openrouter-ai-inference-hub-pitfalls
tags: [Substack]
excerpt: "The author of Olly, an AI assistant that has transacted over 6 million messages via OpenRouter, describes on his blog several of the pitfalls that plague users of AI inference hub OpenRouter: - “ The same model will benchmark very differently”: OpenRouter itself publishes results for GPQA-Diamond and TAU-Bench (under “AutoExacto Benchmarks”) - and they vary wildly among the providers: “ The same m"
substack_url: "https://ndurner.substack.com/p/openrouter-ai-inference-hub-pitfalls"
canonical_url: "https://ndurner.substack.com/p/openrouter-ai-inference-hub-pitfalls"
sitemap: false
---

The author of Olly, an AI assistant that has transacted over 6 million messages via OpenRouter, [describes on his blog](https://mmoustafa.com/blog/so-you-want-to-use-openrouter/) several of the pitfalls that plague users of AI inference hub OpenRouter:

- “**The same model will benchmark very differently”:** OpenRouter itself [publishes results](https://openrouter.ai/deepseek/deepseek-v4-flash-0731#performance) for GPQA-Diamond and TAU-Bench (under “AutoExacto Benchmarks”) - and they vary wildly among the providers:

“**The same model will benchmark very differently”:** OpenRouter itself [publishes results](https://openrouter.ai/deepseek/deepseek-v4-flash-0731#performance) for GPQA-Diamond and TAU-Bench (under “AutoExacto Benchmarks”) - and they vary wildly among the providers:

- **Vision performance is uneven as well**: “DeepInfra's Qwen endpoint read a K as an R, called red blue, and described the word "umbrella" as "funny", while four other hosts of the same weights got everything right. Venice and Together didn't see the MiniMax images at all. The model page says it supports image input, but two of its providers don't and even worse they'll pretend everything is 200 OK.”
