---
layout: post
title: "Adapters in Apple Intelligence"
description: "Update on Apple Intelligence V2 and its use of adapter-based architecture configuration"
date: 2025-06-25
tags: ["apple", "adapters", "llm", "apple intelligence"]
last_updated: 2025-07-02
author: "Nils Durner"
categories: [journal]
---

With reports about [Apple Intelligence V1 not having met quality expectations](https://www.techradar.com/computing/artificial-intelligence/this-is-what-really-happened-with-siri-and-apple-intelligence-according-to-apple), I wondered if the ([adapter-based](training-own-model-finetuning) architecture was to blame: depending on the use-case, a different [adapter would be plugged into the base model](https://machinelearning.apple.com/research/introducing-apple-foundation-models). A [newer report](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) confirms, however, that the new "Apple Intelligence V2" will also use the adapter-based approach:
> For specialized use cases that require teaching the ~3B model entirely new skills, we also provide a Python toolkit for training rank 32 adapters.

That adapters continue to provide for particular use-cases is described in the "Responsible AI" section:
> To design our mitigation steps for multilingual use, we began with multilingual post-training alignment at the foundational model level, then extended to feature-specific adapters that integrate safety alignment data.

The core base model continues to be around 3B in size, but V2 adds long-context attention mechanisms (RoPE, NoPE) and Vision Encoder(s) and adapter. (For the server-sider, a novel parallel Mixture-of-Experts architecture (PT-MoE) is used.)

So in conclusion: no, Apple did not abandon adapters - quite the opposite, it seems.

[Update 2025-07-02]
Media report allege that [Apple is in talks with both OpenAI and Anthropic](https://www.bloomberg.com/news/articles/2025-06-30/apple-weighs-replacing-siri-s-ai-llms-with-anthropic-claude-or-openai-chatgpt) for the server part. Previously, it was [reported](https://www.bloomberg.com/news/articles/2025-06-30/apple-weighs-replacing-siri-s-ai-llms-with-anthropic-claude-or-openai-chatgpt) that Apple was considering buying Perplexity.