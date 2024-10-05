---
layout: post
title: "Microsoft and Qualcomm's Announcement on LLaMA 2 Integration"
date: 2023-07-18
last_updated: 2023-07-18
tags: [Microsoft, Qualcomm, LLaMA, Llama 2, OpenAI, Azure, Windows]
---

How the Facebook LLaMA 2 announcement was presented and contextualized on the side of Microsoft at their Inspire event: it started with a lengthy love letter to OpenAI (screenshot #1) and transitioned to elaborating on their enduring engagement in Open Source (screenshot #2):

> We're one of the largest contributors to Open Source and when it comes to AI, it's no different. And one of the things we're very excited today is the announcement of Meta's LLaMA 2 coming to both Azure and Windows". 

![Llama 2 #1](assets/img/llama-2-1.png)
![Llama 2 #2](assets/img/llama-2-2.png)

They went on showing Azure AI Studio featuring a model catalog (screenshot #3) that includes several LLaMA 2 variations (screenshot #4, #5) and a fancy "Playground" (screenshot #6). OpenAI models were repeatedly called "Frontier models", and LLaMA 2 was called "Open models". After that, they explained what they mean by "... bringing to Windows": LLaMA 2 was shown running locally on Windows, interfaced with through some C# code (screenshot #7) for a WinUI 3 app (screenshot #8) that uses LLaMA 7B (smallest) to slowly run an on-device chatbot (screenshot #9). Caveat: the demo was fronted with "[With the newest advancements] you have a fantastic place to do AI development locally". The mention of WSL 2 and ONNX suggests that this indeed just intended for development, not production use... for now, at least. 🙂 (edited)

![Llama 2 #3](assets/img/llama-2-3.png)
![Llama 2 #4](assets/img/llama-2-4.png)
![Llama 2 #5](assets/img/llama-2-5.png)
![Llama 2 #6](assets/img/llama-2-6.png)
![Llama 2 #7](assets/img/llama-2-7.png)
![Llama 2 #8](assets/img/llama-2-8.png)
![Llama 2 #9](assets/img/llama-2-9.png)


Similar announcement by Qualcomm:

> Qualcomm and Meta will enable the social networking company’s new large language model, Llama 2, to run on Qualcomm chips on phones and PCs starting in 2024, the companies announced today.

> Qualcomm’s chips include a “tensor processor unit,” or TPU, that is well-suited for the kinds of calculations that A.I. models require. However, the amount of processing power that is available on a mobile device pales in comparison to a data center stocked with cutting-edge GPUs.

[Source](https://www.cnbc.com/2023/07/18/meta-and-qualcomm-team-up-to-run-big-ai-models-on-phones.html)