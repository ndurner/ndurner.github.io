---
layout: post
title: "Computation with LLMs"
date: 2024-11-18
tags: ["aleph alpha", "bosch", "llm", "gemini", "google", "pharia"]
description: "Computation with LLMs through Tool-Use and Python"
last_updated: 2024-11-18
author: "Nils Durner"
categories: [journal]
---

Popular wisdom holds that Language Models are "not made for computation" - and such is thus best avoided. This is backed by [this study](https://x.com/yuntiandeng/status/1836114401213989366) that confirms limitations also with o1 (albeit much higher).
This does not hold true for "Language Models like ChatGPT", e.g. as claimed by Tech Crunch, however: as an AI System, it extends beyond the basic Large Language Model, and does therefore not share the same restrictions.
![Models, Systems, Platforms and Use Cases](assets/img/miles-brundage-ai-models-systems-platforms-use-cases.jpg)
(slide by Miles Brundage, OpenAI)
 
The key principles for exact computation were established by this paper by Microsoft Research and can be attained in different ways, depending on the AI System or Platform used:
1. In ChatGPT, prompt to use the "Code Intepreter". The success indicator is in the blue "[>_]" icon. Restriction: use limits of Code Interpreter are low on the free version, and log-in is required.
 
2. In the OpenAI Playground, use the Assistant rather than Chat, and be sure to enable the Code Interpreter slider. Same prompt as with ChatGPT, Code Interpreter execution is very prominent there. Use only limited by the assigned Usage Tier.
 
3. For Anthropic Claude via Amazon Bedrock, I have added "Python Use" as an experimental feature to my Workbench: "Python Use".
There is quite some trickery behind the scenes, but it roughly works the same as Code Interpreter - just much more restricted. (Not sure if this is the Ultimate Best™️, we'll see...).
 
As a practical application, Python-Use enables computing precise RGB values for tints based on a style guide excerpt, which can then be used to colorize an SVG image (inspired by the [ChatGPT Business webinar](https://x.com/TheRealAdamG/status/1852505272708940142)).
![Excerpt from Ai2 style guide for illustration](https://allenai.org/_next/image?url=https%3A%2F%2Fwww.datocms-assets.com%2F64837%2F1722461967-8-3-ai2_color_corepalette2.png&w=3840&q=75)