---
layout: post
title: "GPT-4o image generation"
date: 2025-03-27
tags: ["llm", "openai", "gpt4o", "dall-e", "diffusion", "image generation", "imagegen"]
last_updated: 2025-03-27
author: "Nils Durner"
categories: [journal]
---

GPT-4o for image generation has been released - as part of ChatGPT and Sora. It supersedes the Dall-E 3 model, which was originally released in October 2023, but remains the best OpenAI image generation model available via their API.

Most notable for me, 4o image generation not just supports text prompts (like Dall-E did), but also image prompts. Gemini has added that capability recently as well, but I find 4o's capabilities (or: steerability, as it's advertised) to be better. Here are two extractive examples, with errors (only) in the small details:

![Extracting a product from a scene, rotating it](assets/img/gpt-4o-image_gen-extract-1.jpg)

![Extracting a motif from a backpack](assets/img/gpt-4o-image_gen-extract-2.jpg)

And it may be usable to translate slides as well:  
![EN -> DE slide translation](assets/img/gpt-4o-image_gen-slide-translation.jpg)  
Notice however how our profile photos got substituded!

[Update 2025-03-27]
4o can create technical visualizations, at least simple ones. Steven Heidel of OpenAI shared [this diagram](https://x.com/stevenheidel/status/1904966320770384170), but [without the prompt](https://x.com/ndurner/status/1905295407120580753). I tried the first of my practice cases from [my article on process visualization](2025-02-27-ai-assisted-process-visualiaztion-collaboration) with a slightly modified text prompt and it generally did work, with just minor flaws. The trick is to instruct ChatGPT to use the "Imagegen" tool.