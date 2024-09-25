---
layout: post
title: "Workbench updates & MLX variant"
date: 2024-09-19
tags: [workbenches, llm, chatbots, mlx]
---

# Cloud LLM Workbenches
Some of the additions to my chatbots/workbenches in recent months:
* streaming mode
* multi-modal input box:
    * allows pasting images from the clipboard straight
* cleaner interface
* support for PDF files
    * not just text, truly multi-modal
    * no RAG, so works for all use-cases
* new models: incl. chatgpt-4o (via OpenAI) and Llama 3.1 405B (via Amazon Bedrock)

Demo-Video (use-case: extracting data from an image using Anthropic Claude 3.5 Sonnet via Amazon Bedrock): [YouTube](https://youtube.com/shorts/OH4RGcOzxrw?feature=share).

# MLX Workbench
And for highest data protection requirements, I have created [MLX Chat](https://github.com/ndurner/mlx_chat). This allows LLMs to be run locally, on-device, fully offline on Mac Studio and recent Macbook Pros, without any cloud support. The advantage over other approaches is that the original model releases from Meta or Google Deepmind work unmodified, in full precision. (Other community approaches have lossy compression applied to the models, which results in different models (for the worse) but are misleadingly named the same as the original release. The damage done is often not fully reflected in academic benchmarks, but only exhibited in practice.)

"MLX Chat" is text-only for now, but I want to make it multi-modal, time permitting.

Demo video showing redacting sensitive information, such as passwords, from a configuration file on [YouTube](https://youtu.be/Nu7Rf2mMWXk).

This can be used as an example of how privacy concerns may exist in the public debate, but, taken together with the recent training breakthroughs, are just that: concerns. Anything more highly depends on the context.