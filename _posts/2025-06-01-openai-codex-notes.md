---
layout: post
title: "Notes on OpenAI Codex CLI"
description: "Hands-on experience with OpenAI's Codex CLI: exploring its capabilities, limitations, pricing, and practical usage insights for developers working with AI-assisted coding."
author: "Nils Durner"
categories: [journal]
tags: [OpenAI, codex-mini-latest, codex, jules, llm, o1, o4-mini, ai-coding]
date: 2025-06-01
last_updated: 2025-08-07
---

Upfront summary: Codex CLI is labelled an "experimental project" and it certainly is: handing off whole, convoluted developments tasks for automagic completion has still not arrived.

* use is charged towards API credits
    * free use allowance can be [redeemed by users of certain paid ChatGPT subscriptions or through data sharing](https://x.com/fouadmatin/status/1923906279929778594)
        * the ChatGPT subscription needs to be active for more than 7 days, though
* requests/responses get logged to the [OpenAI Platform Logs](https://platform.openai.com/logs) that are accessable through the Dashboard
* Codex CLI defaults to the new "codex-mini-latest" model
    * codex-mini-latest is:
        * also available via the API, but not offered through the Playground UI
        * slightly [costlier than o4-mini](https://platform.openai.com/docs/models/compare?model=codex-mini-latest) on a per-token basis, could be different in real use though
    * the model used by Codex can be changed through the "/model" command
        * o3 and o4-mini are run with "high" reasoning effort according to the logs, and are thus particularly expensive to run
* Supports many LLM providers, but neither Amazon Bedrock nor Anthropic Claude
* a [rewrite](https://x.com/OpenAIDevs/status/1928556712291877327) of Codex CLI in Rust has been announced
    * so forking & adding Bedrock support may not the best investment, currently
* local ressource access is facilitated by the `local_shell` hosted tool
    * [exclusive to codex-mini-latest](https://platform.openai.com/docs/guides/tools-local-shell), at least through the API
* does not access the web, so tends to make up APIs that don't exist
    * Eleanore Berger's [approach with AI-assisted planning upfront](https://x.com/intellectronica/status/1928471155179954344) seems like a good workaround
* general lore that coding agents can get costly quickly seems true, at least with the o3 model: a request to update a Github Pages blog post cost > $4.
    * insight: all interactions and shell input/output are inlined in the main session are thus carried along in the context
    * I had anticipated for implicit caching to alleviate the cost of growing context, but apparently that's not as much as to make the use of o3 in Codex reasonably cheap
* generally lazy vibe for updating > 100 blog posts, with poor instruction following: models like to read files only partially (read first n lines, summarize first paragraph, ...) and generally had to be instructed that it's an LLM itself with all capabilities. o4-mini seemed best, but went off-rails frequently by claiming "too manually intensive", asking for feedback, etc. Once broke off and unilaterally created several scripts that would call out to an external LLM!
* Codex CLI, like Google Jules, was overwhelmed with undoing an historical API switch and implementing a new feature based on the new-old API while keeping everything else intact.
* a simple coding task on an existing code base with sufficient detail given as context appeared successful, but I did not verify in depth

[Update 2025-08-07]
[GPT-5](openai-gpt-5) is the new default model in Codex CLI. Usage fees are [convered by a paid ChatGPT subscription](https://x.com/OpenAIDevs/status/1953559797883891735).