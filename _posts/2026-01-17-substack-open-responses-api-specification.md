---
title: "Open Responses API specification"
date: 2026-01-17
last_updated: 2026-01-17T18:10:18+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/open-responses-api-specification
tags: [Substack]
excerpt: "Open Responses is a new specification inspired by the OpenAI Responses API for interacting with LLMs/VLMs/LRMs. The launch partners include OpenAI, OpenRouter, Hugging Face, ollama, vLLM, LM Studio, and Vercel. It could thus supersede the legacy Chat Completions API. The specification is not all encompassing, however. One pitfall I have recently experienced was around how to include reasoning item"
substack_url: "https://ndurner.substack.com/p/open-responses-api-specification"
canonical_url: "https://ndurner.substack.com/p/open-responses-api-specification"
sitemap: false
---

[Open Responses](https://www.openresponses.org) is a new specification inspired by the OpenAI Responses API for interacting with LLMs/VLMs/LRMs. The launch partners include OpenAI, OpenRouter, Hugging Face, ollama, vLLM, LM Studio, and Vercel. It could thus supersede the legacy Chat Completions API.

The specification is not all encompassing, however. One pitfall I have recently experienced was around how to include reasoning items. The Gemini 3 Pro API has [introduced a (breaking) change](https://ai.google.dev/gemini-api/docs/thought-signatures) there, with their own client library lacking support at that time ([I created a fork](https://github.com/ndurner/adk-python)). Open Responses [does not clarify](https://www.openresponses.org/specification#reasoning), unfortunately:

> providers are free to support any combination of them, depending on their safety policies, business requirements, and implementation details

providers are free to support any combination of them, depending on their safety policies, business requirements, and implementation details
