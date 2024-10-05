---
layout: post
title: "LLM Tokenizer comparison"
date: 2024-03-26
last_updated: 2024-03-26
tags: [openai, gpt4, claude, anthropic, gemini, tokenizer]
---

A poster on LinkedIn [highlighted](https://www.linkedin.com/posts/peter-gostev_since-there-was-a-lot-of-interest-in-tokenisation-activity-7178533359445250048-rgEL?utm_source=share&utm_medium=member_desktop) the [Xenova Tokenizer Playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground) to compare Tokenizer efficiency.

I [remarked](https://www.linkedin.com/feed/update/urn:li:activity:7178533359445250048?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7178533359445250048%2C7178559296903745536%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287178559296903745536%2Curn%3Ali%3Aactivity%3A7178533359445250048%29):

There is however a difference between what this Playground calculates and what the relevant APIs report as actually used (and therefore billed) input tokens. With a short German sentence:
* Xenova Playground „Claude“: 13 Tokens
* Claude 2.1 API: 22 Tokens
* Claude 3 API: 20 Tokens
* Xenova Playground “gpt-4/…”: 11 Tokens
* OpenAI API: 28 Tokens

Note that tokenization seems to work differently for Claude 2 and 3, which the Xenova Playground doesn‘t account for either.

(German sentence: „Was ist das englische Wort für Dokument?“)