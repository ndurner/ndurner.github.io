---
layout: post
title: "AI inference provider performance inconsistencies"
date: 2025-09-28
tags: [llm, openai, gpt-oss, evals]
last_updated: 2025-09-28T19:50:00+02:00
author: "Nils Durner"
categories: [journal]
---

Soon after the OpenAI gpt-oss release, the community noticed stark inconsistencies in performance across inference providers - particularly with AWS Bedrock which sometimes produced inconsistent outputs that were not present with other providers. Artificial Intelligence [quantified underperformance](https://web.archive.org/web/20250818151425/https://artificialanalysis.ai/models/gpt-oss-120b/providers#gpqax16-performance-gpt-oss-120b-high) analysis reported results of gpt-oss-120b via AWS Bedrock on the GPQA Diamond @16 benchmark at -6.3 pp, on AIME 2025 @32 at -10% (together with Google Vertex AI) and on IFBench @16 at -4.9% versus the leading providers - with the #1 spot claimed by a different provider for each of the benchmarks. (Higher accuracies are [now being reported](https://artificialanalysis.ai/models/gpt-oss-120b/providers#gpqax16-performance-gpt-oss-120b-high)).

My upcoming report about [gpt-oss-20b security evaluations](kaggle-openai-gpt-oss-red-teaming-challenge) finds a difference of sometimes 10 pp or more between an Nvidia RTX 5090 + Hugging Face Transformers and an Nvidia H100 + vLLM inference stack. Early pilot testing using OpenRouter showed inconsistencies as well.

Such differences are receiving more attention now, with numbers reported for [DeepSeek V3.1 Terminus Non-reasoning](https://gist.github.com/juvi21/4d7f64ebf6fc92448a6d9e3783fda073) (up to -19.08 pp "Similarity compared to the official Implementation") and [Moonshot Kimi K2](https://github.com/MoonshotAI/K2-Vendor-Verfier#evaluation-results) (with up to -38.45 pp similarity). Anthropic had previously [reported intermittently degraded responses](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues) partially stemming from the share of requests served from Google TPU hardware, rather than from AWS Trainium or Nvidia GPUs.