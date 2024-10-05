---
layout: post
title: "Open Source LLMs"
author: "Nils Durner"
categories: [journal]
tags: [vicuna, llama, bloom, alpaca]
date: 2023-04-14
last_updated: 2023-04-14
---

Entire language models are being pirated and touted as "Open Source". This includes Vicuna, which has been making headlines as "90% quality of OpenAI ChatGPT" (which is B.S.). This [illustration by Sahar Mor](https://www.linkedin.com/feed/update/urn:li:activity:7049789761728770049/) makes a distinction between "Research" and "Commercial", and "Research" partially implies "legally tainted" (may also be true for ⚡ Lit-LlaMA):
![Commercial and Research LLMs](assets/img/llm-research-commercial.png)

A colleague today shared his practical experience with BLOOM, which echoed my experience with these:

Same for Vicuna7B and -13B. I have been running both for the last two weeks... for science 😊, 4-Bits quantized models, in Instruction inferencing mode. My experience hasn't been good either. Without proper retraining and just in-context learning and soft prompting, it can do okay on small inputs like 5 minutes worth of daily news, but already has issues with longer content like a press release.
Worse, it wouldn't generate valid JSON (in a zero-shot setting, admittedly).
Alleged Alpaca60B didn't make a difference to me, so I am wondering if the Llamas are just hard to use or if this is also implied by "Research only".