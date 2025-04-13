---
layout: post
title: "GPT-4o Imagegen for infographics"
date: 2025-04-05
tags: ["llm", "openai", "gpt4o", "dall-e", "diffusion", "image generation", "imagegen", "chatgpt"]
last_updated: 2025-04-13
author: "Nils Durner"
categories: [journal]
---

Several samples on X suggest that [GPT-4o Imagegen](gpt4o-image-generation) can be used for infographics ([1](https://x.com/stevenheidel/status/1904966320770384170), [2](https://x.com/DeryaTR_/status/1905729150650081701), [3](https://x.com/egeberkina/status/1906088423988875617), [4](https://x.com/dotey/status/1907653227589304425)). In my experiments, instructions to Imagegen need to be on-point: simply supplying a Readme.md with all kinds of different notes on a code project and asking it to visualize the build process does not work - the model will even start to hallucinate random things. What works instead is to ask GPT-4.5 to build the prompt for Imagegen, and keep it simple: elaborate layouting instructions like this also overwhelm the model:
> [...] Near the bottom or top, add a small list of runtime dependencies (libusb, libglib2.0, etc.) to illustrate what must be present on the target system. [...]

Payload instructions that works for the base diagram:
> Thin Client Build Flow:  
	1.	Box: “Prerequisites (CMake, Clang, Libraries)”  
	2.	Box: “Build using CMake/Clang”

Intermediate result #1 (pink redactions added manually):
![illustration of a build process, box diagram](assets/img/gpt-4o-imagegen-diagram-0.jpg)

This can be iterated on, like adding a headline. Also, a style reference in the form of an existing diagram can be passed. I like [Leonie Monigatti](https://medium.com/@iamleonie)'s distinctive style, so gave [one of her diagrams](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*kSkeaXRvRzbJ9SrFZaMoOg.png) as the style reference:
> Redo the first chart in the style of the second. Do not change the content, just the style.

Intermediate result #2:
![illustration of a build process, box diagram, after style reference applied](assets/img/gpt4o-imagegen-diagram.jpg)

Further iterations:
1. "Turn it into an infographic, Studio Ghibli stlye. Include an instructor character that's pointing to the flowchart."
2. "Make the instructor look like me" (include photo)
3. "Censor [some items]. For censoring, retain the original style and make it appear as if deleted with a rubber. Make it beautiful."

Final result:
![illustration of a build process with instructor pointing to it](assets/img/gpt4o-imagegen-infographic.png)

Food for thought: ethical implications and ethical conduct when using the works of others as a style reference.

[Update 2025-04-13]  
OpenAI for Business has published a guide featuring infographics: [Using image generation in ChatGPT - 5 examples](https://www.linkedin.com/posts/openai-for-business_using-image-generation-in-chatgpt-activity-7316147051228999680-fFHS?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAGX2jIBd6RDsNRYv13Bvu3x4nnCNu96SEw). The two infographics prompts presented there:
* "Create a visual guide for conducting an ORSA (UK/EU) regulatory assessment"
* "Create a technical architecture diagram illustrating [describe the diagram in detail]"
The first prompt is interesting because it does not describe to the model what to draw in detail but relies on its internal world-knowledge.

Meanwhile, physician Derya Unutmaz keeps sharing [medical infographics](https://x.com/DeryaTR_/status/1911166254678724619) made with GPT-4o on X.