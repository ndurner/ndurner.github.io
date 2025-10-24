---
layout: post
title: "ChatGPT Atlas"
date: 2025-10-22
tags: [llm, chatgpt, atlas, ai agents]
last_updated: 2025-10-22T23:20:00+02:00
author: "Nils Durner"
categories: [journal]
---

OpenAI has released their browser: ChatGPT Atlas. Superficially, this feels like Chrome - which could be due to [Chrome engineer Dan Fisher having had a hand in it](https://www.searchenginejournal.com/openai-hires-former-chrome-engineer-eyes-browser-battle/533533/). Conceptually though, this follows, for example, the Dia browser in that it builds AI features in. Most prominently, there is an "Ask ChatGPT" sidebar that opens a chat side panel - much like the Visual Studio extension for the programming agent Codex. The central benefit appears to eliminate copying content back and forth between the browser and ChatGPT via the clipboard.

## Agentic laziness
Atlas shares the same kind of laziness that holds back other agents, including Codex, as well. I was excited to try it for turning a website catalog - the 1889 AI Agents listed at the Google Cloud Marketplace - into a table or bullet point list. The same task fails with the regular ChatGPT Agent because the Marketplace deliberately blocks access that way. With Atlas, the limiting factor is the agent itself: it decided that the task is too laborious ("impractical with the available tools", "not feasible here") and just gave me a subset of between 37 and 79 items, depending on the prompting approach.
![ChatGPT Atlas refusal](assets/img/chatgpt-atlast-refusal.jpg)

Oftentimes the partial results were initially presented without warning, making it appear as if it was the full list. As it stands, the use of ChatGPT Atlast for "vibe scraping" seems quite limited. On the other hand, [Jess Martin reported success by "reminding" it](https://x.com/jessmartin/status/1981051456368296216) - perhaps because the DOM was easily accessible? That's what Atlas complained about it my case.

## Weak default model
Another problem I found was that web search didn't work properly or answers (including search results URLs) were hallucinated. This was due to Atlas defaulting to GPT-5 Instant (which I wrote about earlier as "[gpt-5-chat](openai-gpt-5)"). Switching to "GPT-5 Thinking" through the model switcher in the upper left fixes this. This switch is not remembered by the UI, though, so needs to be redone in every new tab. The sidebar does not yet have a model switcher (thus e.g. causing hallucinated answers about YouTube videos), but that's already on the list of improvements being worked on.