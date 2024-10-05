---
layout: post
title: "McKinsey & more mythbusting"
author: "Nils Durner"
categories: [journal]
tags: [llm, gpt4]
date: 2023-05-22
last_updated: 2023-05-22
---

A colleague today shared the McKinsey report on "[What every CEO should know about generative AI](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/what-every-ceo-should-know-about-generative-ai)".

I think it's well and acurately written.
They don't invoke the tired "it just predicts the next word", so this is actually a good read for friends & family as well!
More narrow myth busting:
* [ChatGPT is NOT simply “predicting” the next word](https://www.linkedin.com/pulse/chatgpt-simply-predicting-next-word-trung-ngo-ph-d-/)
* [The idea that ChatGPT is simply “predicting” the next word is, at best, misleading](https://www.lesswrong.com/posts/sbaQv8zmRncpmLNKv/the-idea-that-chatgpt-is-simply-predicting-the-next-word-is)

(Interestingly, the latter directly attacks several statements made by Stephen Wolfram in his book "What Is ChatGPT Doing". I was already doubtful about Wolfram making statements about ChatGPT by taking a reductionist view on GPT-2, as if GPT 3.5 were simply a pumped up version of the same.)

One clever example of the "guardrails" McKinsey mention: one of the apps that drive the Llama models, "llama.cpp", has recently gotten an option to ensure the LLM output follows a certain structure (given in Backus-Naur Form, e.g. to ensure valid JSON ouput). I noticed the KcKinsey report to use very careful language, so statements like this:
> it can generate new content, often in “unstructured” forms (for example, written text or images) that aren’t naturally represented in tables with rows and columns

don't mean that they can just generate unstructured output (thus perhaps creating issues with subsequent processing stages that use traditional paradigms).