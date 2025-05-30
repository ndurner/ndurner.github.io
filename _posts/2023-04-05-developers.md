---
layout: post
title: "Developer talk"
author: "Nils Durner"
categories: [journal]
tags: [copilot, gpt, chatgpt]
date: 2023-04-05
last_updated: 2023-04-05
description: "Explores LLMs for developers: Copilot productivity, overcoming ChatGPT loops via in-context learning, rubber-duck debugging, GPT-4 limits, context forgetfulness, and language suitability."
---

Sparked by a [blog post by Github](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) on Copilot productivity enhancements and developer happiness, there was lively reflection on LLMs as a developer tool. One developer brought up the error scenario where ChatGPT would get stuck in a conversation loop. As a remedy, I offered this advice: sometimes it feels like it’s cornered and can’t get out. In such cases, I feed it a relevant excerpt from the documentation just to get it going again - thanks to in-context learning 💪🏻. There may still be gaps in transferring, but these can be rectified by posing mere suggestive questions...
![To GPT: what shall we do?](assets/img/chatgpt-coding-stuck.jpg)

I confirmed that ChatGPT can be used for Rubberduck Debugging and also for giving a rough description first and iterate on that. There are things that get in the way though:
1. ChatGPT Plus message limit for GPT-4
1. limited context size: ChatGPT appears "forgetful" at some point
1. some programming languages are better suited that others. My impression was that Python works better than Qt/QML

#2 must also be relevant to Copilot - in some way, regarding "[copilot-x] can see the context of the project". Large inputs are usually "indexed" first and then selectively chosen for presentation to GPT. But that can induce said "forgetfulness" and oversights.

Finally, I emphasized on making sure to use GPT-4 for best results, rather than GPT-3.5 which continues to be the default:
![Defaults are not your friends](assets/img/chatgpt-default.jpg)