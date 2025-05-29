---
layout: post
title: "Exa Web Search MCP in OpenAI Prompts Playground"
description: "Learn how to integrate Exa's web search capabilities into OpenAI Prompts Playground using MCP, including setup instructions, cost analysis, and optimization tips for GPT-4.1 and o4-mini models."
date: 2025-05-29
tags: ["llm", "openai", "exa", "web-search", "mcp", "o1"]
last_updated: 2025-05-29
author: "Nils Durner"
categories: [journal]
---

Web Search in the OpenAI Prompts Playground remains [restricted for some models and disabled for others](web-search_o3). With the addition of MCP support however, users may add other Web Search providers, e.g. [Exa](https://exa.ai). Exa's (remote) MCP server does not support the complete functionality of the Exa API, but setup is straightforward:
1. [Sign up](https://dashboard.exa.ai/)
2. [Retrieve API key](https://dashboard.exa.ai/api-keys)
3. Add to the OpenAI Prompts Playground
    1. Click ➕ in the Tools row
    2. Select "MCP Server"
    3. Select "+ Add new"
    4. Paste this into the URL field: https://mcp.exa.ai/mcp?exaApiKey=
    5. Paste the Exa API key at the end of the URL, so it looks like this: https://mcp.exa.ai/mcp?exaApiKey=d75...
    6. Label: Exa
    7. Authentication: none
    8. Hit "Connect"
    9. In the following popup window, click "Add"

Core and center is the tool `web_search_exa` that is then available to the LLMs. Another tool added is `crawling` which retrieves URL content. Because `web_search_exa` will always return not just URLs for search results but also the full plaintext of these pages, `crawling` would not be necessary - but o4-mini by default calls it anyway.

## Putting Exa to the test
The OpenAI hosted `web_search` tool cannot figure out where I work. In contrast, ChatGPT 4o does figure it out. With the Exa MCP added to the OpenAI Prompts Playground, 4o-mini does as well - after 5 tool calls:  
> 🧔🏻‍♂️ Where does Nils Durner work?  
🤖 Nils Durner is a Principal Software Engineer at Namirial.

It doesn't quite work with GPT-4.1 yet, though:
> 🧔🏻‍♂️ Where does Nils Durner work?  
🤖 Nils Durner is an accomplished software engineer with interests [...] **The website does not specify a particular company's name as his current employer** [...] If you need more detail about a specific company or a more formal workplace affiliation, I can investigate further or check his LinkedIn profile. Would you like me to do that?  
🧔🏻‍♂️ Yes  
🤖 **I was unable** to locate a direct LinkedIn company page or explicit current employer

The reason for this failure is that GPT-4.1 rewrote the initial `web_search_exa` search query to "Nils Durner current workplace" and then used the Exa `linkedin_search` tool - which is, per the documentation, only suitable for company pages. GPT-4.1 seems thus mislead by the only minimal documentation provided by the Exa MCP - which does not sufficiently explain how to call it properly.

## GPT-4.1 Developer Prompt
The following developer/system prompt helps GPT-4.1 use the `web_search_exa` tool effectively:
> The web_search_exa tool accepts user questions verbatim as the \"query\" parameter, so avoid pre-processing or shortening.

Result:
> 🧔🏻‍♂️ Where does Nils Durner work?  
🤖 Nils Durner is currently a Principal Software Engineer at Namirial. This information is corroborated by his recent LinkedIn activity [...]

## o4-mini Developer Prompt
Use with o4-mini can likewise be optimized: using the following system/developer prompt makes o4-mini use only 2 `web_search_exa` calls instead of 5 mixed calls that involve `crawling`:
> 🧔🏻‍♂️ Where does Nils Durner work?  
🤖 Nils Durner is a Principal Software Engineer at Namirial.

Special about this setup: o4-mini will use search result content in its Reasoning process, resulting in a poor man's ~Deep~ Shallow Research implementation.

![OpenAI Prompts Playground with Exa MCP](assets/img/exa-mcp-openai-playground.jpg)

## Costs
The naive o4-mini test without developer prompt cost 3.4¢ (US) for Exa services, in addition to OpenAI use. Exa costs with the improved prompts were 1¢ with GPT-4.1 and 2¢ with o4-mini.

## Optimization potential
* If Exa was set up as described above, the OpenAI Prompts Playground will ask for approval for each MCP invocation. This can be turned off in the last popup of the setup procedure (item 3.9) by switching the "Approval" field from "Always" to "None".
* The Exa MCP server does not include the full functionality of the Exa API, like date ranges, more than 10 results, or allowed/disallowed domains. The source code of the Exa MCP server is [published on Github](https://github.com/exa-labs/exa-mcp-server/) though, so should be extensible for private deployments.
* Using the full page content (though in plaintext) as an input to the LLMs can be expensive in input tokens used. Two options in the Exa API cater to that: the possibility to disable returning full page content and returning AI-generated summaries instead. I haven't tried either, though.