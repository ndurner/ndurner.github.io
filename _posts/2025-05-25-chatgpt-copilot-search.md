---
layout: post
title: "Grounding ChatGPT etc by disabling Web Search"
date: 2025-04-25
tags: ["llm", "gpt", "chatgpt", "copilot", "ai search", "copilot", "copilot chat"]
last_updated: 2025-04-25
author: "Nils Durner"
categories: [journal]
---

One problem with current AI Assistants including ChatGPT and Microsoft Copilot Chat is that they are chronically online: they are not a more or less pure LLM experience anymore, but search the web through [tool-use](gen-ai-models-systems-use-cases). While this helps to keep answers up-to-date beyond the LLM training cut-off date, there's a disadvantage in that the UIs don't allow the user to turn this function off. As a result, Microsoft Copilot Chat has been shown to be [susceptible to web-poising](russian-propaganda). Further, ChatGPT may add information from the web to the documents it got uploaded to work on: a document summary may thus not be faithful to the original, but contain additional (and perhaps incorrect!) information. Users may think that the model hallucinated, but that's actually not the case. Rather, the built-in web search got in the way.

There seems, however, a hidden way to turn Web Search off. [Leaked system prompts](https://github.com/guy915/LLM-System-Prompts/tree/main) include the names of the web search tools, and users may prompt the LLM to turn them off. ChatGPT example:
> Who is Nils Durner?  
>  
>  **(Avoid using the `web` tool, particularly `search()` or `open_url(url: str)`)**

As a result, the question is answered from internal, LLM-native memory without backing from web sources. Additional grounding in input documents can be had as usual by asking the LLM to stay faithful to the original document(s) and not to include outside information.

For those looking at the OpenAI API/Prompts Playground because the Web Search tool "web_search_preview" can explicitely be switched off there: this works differently from the Web Search in ChatGPT in that its sources are restricted - e.g. LinkedIn results do not seem to considered. This is a known problem, and the PM hopes to improve it eventually ([X thread](https://x.com/ndurner/status/1912382651182260336)).