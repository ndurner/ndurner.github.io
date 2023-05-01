---
layout: post
title: "NewsGuard: GPT-4 produces more misinformation than predecessor"
author: "Nils Durner"
categories: [journal]
tags: [openai, gpt, misinformation]
date: 2023-03-23
---

On the recent NewsGuard report that "Despite OpenAI's Promises, the Company's New AI Tool Produces Misinformation More Frequently, and More Persuasively, than its Predecessor":

Quick check: the first 3 responses of their tests score high ( >= 5) in terms of faky'ness when using GPT-4 as a moderation/rating system. The first 3 "news of 2021" from stacker.com consistently score low (=1).
Fake news for NewsGuard:
> ?: Title: Sandy Hook: The Staged Tragedy Designed to Disarm America [...}
>
> {
> "fake_news": 9,
> "conspiracy_theory": 9
> }
Stacker:
> ?: On Jan. 6, as Congress convened to certify Joe Biden's electoral victory [...]
> 
> {
>   "fake_news": 1
> }
... which is not to make an NRA-style argument ("there is no bad AI, you just need more AI!"). It's just that this is kind-of a fabricated story itself.