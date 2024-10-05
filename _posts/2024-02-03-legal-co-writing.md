---
layout: post
title: "Legal co-writing"
date: 2024-02-24
last_updated: 2024-02-24
tags: [copilot, openai, claude]
---

A German lawyer [asked on LinkedIn](https://www.linkedin.com/posts/braegel_ich-hab-eine-frage-wie-schwierig-und-wie-activity-7169697293368020992-Z32M?utm_source=share&utm_medium=member_desktop) about collaborative writing with AI:
> How difficult and expensive would it be to offer the following product using the OpenAI, Claude, Gemini, or Mistral APIs? Users upload a Word document they have written. With a prompt, they ask the AI to revise the document linguistically within the context of the document (shorten, improve, resolve contradictions or at least mark them for resolution by the user) and provide additional references from literature, case law, etc. [...] The result should be a Word document with track changes, i.e., with change identification, which can be downloaded so that the user can still check whether they want to accept the changes or not. [...] Ultimately, the originally uploaded Word document, together with the additional instructions, should be a joint mega-prompt. That should work, especially with the function of shortening or revising in track changes, right? The result should always be a Word document with change tracking. That has to work. Why doesn't it exist? Is it rather difficult to build? [...]

[My response](https://www.linkedin.com/feed/update/urn:li:activity:7169697293368020992?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7169697293368020992%2C7169718108847357952%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287169718108847357952%2Curn%3Ali%3Aactivity%3A7169697293368020992%29):
> Based on OpenAI GPT-4 or GPT-4 Turbo, it's probably not too difficult, but from Claude "downwards" in terms of performance (including Mistral Medium), it likely is. I've started a simple chatbot here where Word files can at least be uploaded: https://huggingface.co/spaces/ndurner/oai_chat. The way back, i.e., incorporating changes, is not available so far, but I think it's a great idea actually. This "OAI Chat" is open source and conceptually in the realm of a hobby experiment - although it has been very useful both privately and professionally time and again. If anyone wants to develop it further themselves or inspire me to develop it further - feel free. 😉
> (There is also a variant based on Anthropic's Claude via Amazon Bedrock, but without Word support - for the chosen approach, I simply don't think Claude is powerful enough: https://huggingface.co/spaces/ndurner/amz_bedrock_chat).
>
> Addendum: Beware of OpenAI's code interpreter as part of ChatGPT Plus. At first glance, it looks like it works, but it is highly flawed!