---
layout: post
title: "LlamaIndex"
author: "Nils Durner"
categories: [journal]
tags: [llama-index]
date: 2023-06-28
last_updated: 2023-06-28
description: "Evaluates LlamaIndex since March, noting scalability issues with large data, GPT-4 support patch contribution, and potential design limitations despite extensive code."
---

Prompted by an [interview with Jerry Liu of LlamaIndex](https://open.spotify.com/episode/54KLlo0r4CPZnVcURQKwUT?si=P7BscDwQTsSgMHhGUUdEMg) posted by a colleague, I shared that we have been evaluating this since March or so, with rather poor results esp. when the data basis gets larger. I [contributed a patch to add GPT-4 support](https://github.com/langchain-ai/langchain/pull/1778), but as it turned out, the problems are not with the backend LLM, but IMHO a fundamental design issue with the approach itself - despite the sophistication that the ~120.000 lines of code brings. What we didn't investigate: different vector databases and/or embeddings selection strategies.