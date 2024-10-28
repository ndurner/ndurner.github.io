---
layout: post
title: "Pelican vs. Llama 3.1 405B and others"
author: "Nils Durner"
categories: [journal]
tags: [ai, survey, vago]
date: 2024-10-26
last_updated: 2024-10-26
---

Motivated by starkly different results from different Llama 3.1 405B providers on one hand, and claims - particulary derived from the Chatbot Arena that quantized versions are no different on the other hand, I have been wishing for a telltale sign that 1) conclusively proves otherwise and 2) tells providers apart. Good news: Simon Willison has started the Pelican-on-a-bicycle benchmark: a gallery that compares LLM outputs from this simple prompt:
> Generate an SVG of a pelican riding a bicycle

Towards answering my questions about Llama 3.1 405B, I have added the outputs via AWS Bedrock and Hyperbolic: [my fork on Github](https://github.com/ndurner/pelican-bicycle/tree/main), [thread on X](https://x.com/ndurner/status/1849916019059343608).

Further, this was a quick way to check if increasing the temperature for the new Anthropic Claude 3.5 Sonnet 20241022 release indeed fixes the purported regressions. Summary: no ([gallery on X](https://x.com/ndurner/status/1850117886674714992)).