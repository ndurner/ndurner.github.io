---
layout: post
title: "o1 Pro Mode & Llama 3.3"
date: 2024-12-12
tags: ["llm", "chatgpt", "o1 pro", "chatgpt pro", "openai", "llama"]
last_updated: 2024-12-12
description: "Reviews ChatGPT o1 Pro Mode’s leaps over o1-preview using plan-like-a-graph, and Llama 3.3 70B’s comparative performance via IBM WatsonX with 32K token limit."
author: "Nils Durner"
categories: [journal]
---

Quick notes on last week's foundation model releases:

## OpenAI o1
o1 was released through ChatGPT: it's a stark improvement over the o1-preview available through API; o1-preview basically not representative. The new "o1 Pro Mode" is a class of its own: it aces through almost all of the subject tasks in a survey paper I have under submission, and can recover from its only mistake. What's more, it cracks a task that other models including Anthropic's Claude 3.5 can only do if assisted with the "[Plan like a Graph](openai-o1-preview)" prompting method. At this point, o1 Pro Mode seems much more powerful and easier to use than other models/systems - but also, not all use-cases benefit from this.

Still, this is clearly a first release and early experiments elsewhere are best summed up as Ethan Mollick did: ["It's a weird one."](https://x.com/emollick/status/1864872760486293825).

## Llama 3.3
Llama 3.3 70B was released, with same performance alleged as Llama 3.1 405B. I have started running the same tests as above, but found its performance on these to be behind Mistral Large 2411, so haven't completed the tests.

As AWS doesn't offer access either through its regular Model Access or its new Marketplace, I have used it through IBM WatsonX. The WatsonX Prompt Lab has Guardrails enabled by default. When these trigger, the error message will confusingly be ["'meta-llama/llama-3-3-70b-instruct' is currently unavailable, please try later"](https://x.com/ndurner/status/1865163813747650880).

[Simon Willison pointed out](https://x.com/simonw/status/1867240518750810130) that the maximum generation sequence length is 32K (vs. 8K with Claude 3.5 Sonnet and Gemini 2.0 Flash, and 16K with GPT-4o)