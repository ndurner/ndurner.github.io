---
layout: post
title: "Italian LLM Benchmark: INVALSI for AI"
date: 2024-07-15
last_updated: 2024-07-15
description: "Presents Italian language model benchmark results, detailing dataset selection, evaluation metrics, and comparative performance across LLMs."
tags: [ai, llm, benchmarks, italian]
---

The University of Milano-Bicocca has published a significant work for Generative AI in Italy. As Alessandro Vitale [notes in his LinkedIn post](https://www.linkedin.com/posts/alessandrovitale_luniversit%C3%A0-degli-studi-di-milano-bicocca-activity-7218616180608028673-eZhr), there was previously no benchmark to understand how well LLMs performed in Italian. The new benchmark adapts INVALSI tests, which are typically given to Italian students in elementary, middle, and high schools.

Key points from Vitale's post:

1. Claude 3.5 Sonnet by Anthropic is currently the best-performing model.
2. OpenAI models have some caveats, including ethical filters blocking 5.4% of responses to texts by Gianni Rodari and Ennio Flaiano.
3. GPT-3.5, widely used in production, performs poorly compared to newer models.
4. Google's Gemma 2 9B (instruct version) performs surprisingly well despite its small size.
5. Fine-tuned open models by Michele Montebovi and MII-LLM show significant improvements for Italian.
6. Models created in Italy, like Ludovico Comito's adaptation of Sapienza University of Rome's Minerva model, still have room for improvement.

The [leaderboard](https://huggingface.co/spaces/Crisp-Unimib/INVALSIbenchmark) shows:

1. Claude-3.5-sonnet: 92.2
2. Claude-3-opus: 88.5
3. Mistral-Large-Instruct-2407: 87.5
4. Meta-Llama-3.1-405B-Instruct: 86.1
5. GPT-4-turbo: 86.0
6. Claude-3-sonnet: 83.1
7. Meta-Llama-3.1-70B-Instruct: 82.7
8. Gemini-pro-1.5: 81.2

Regarding a similar benchmark for German, Malte Ostendorff, Senior Research Engineer at Deutsche Telekom, pointed to the [Occiglot leaderboard](https://huggingface.co/spaces/occiglot/euro-llm-leaderboard), which covers several European languages including German. While it currently consists of only translated tasks, they are working on localized versions as well.