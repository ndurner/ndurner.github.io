---
layout: post
title: "OpenAI-based Chatbot interface updated"
date: 2025-08-03
tags: [llm, openai, oai_chat, exa, mcp]
last_updated: 2025-08-03
author: "Nils Durner"
categories: [journal]
---

My [Chatbot interface for OpenAI models](https://github.com/ndurner/oai_chat/) ([Live demo](https://huggingface.co/spaces/ndurner/oai_chat)) has gotten a few improvements lately:
* Tool-Use presentation:  
![Screenshot: new presentation of tool-use instances](assets/img/oai_chat-updates-20250803/tool-use-presentation.jpg)
* Support for MCP Servers (aka "Model Context Protocol)
    * registration to be done in mcp_registry.json, loosely follows the Visual Studio syntax
        * sample in [mcp_registry.sample.json](https://github.com/ndurner/oai_chat/blob/main/mcp_registry.sample.json)
    * MCP Servers to be used can be selected/deselected like traditional tools  
![Screenshot: MCP Server selection](assets/img/oai_chat-updates-20250803/mcp-server-selection.jpg)
    * Remote MCP Server integrations are handled from the OpenAI backend directly: example with the [gitmcp](https://gitmcp.io) MCP server for oai_chat:  
![Screenshot: oai_chat with gitmcp](assets/img/oai_chat-updates-20250803/gitmcp-example.jpg)
    * Local MCP Server integrations (stdio) are not routed through OpenAI, but are called locally. [Web search with Exa](exa-mcp-web-search-playground):  
![Screenshot: inquiry through Exa.ai](assets/img/oai_chat-updates-20250803/local-mcp-exa-example.jpg)  
(their remote MCP server appeared flaky recently, so I decided to make sure the [MCP server](https://github.com/exa-labs/exa-mcp-server) run locally works)
    * (not available on HuggingFace live demo)
* UnrestrictedPython: as an opposite to the RestrictedPython that allows the LLM to execute code in a sandbox, setting the environment variable `CODE_EXEC_UNRESTRICTED_PYTHON=1` lifts the sandbox and allows arbitrary code execution. Know the risks.
* Reasoning tokens are now fed back into reasoning models. OpenAI claim [performance improvements](https://cookbook.openai.com/examples/responses_api/reasoning_items) that way, e.g. on SWE-bench of 3%
* sets the OpenAI API token to use automatically if OPENAI_API_TOKEN is set
    * ... either through the environment or .env

Philipp Schmidt, AI Developer Experience at Google DeepMind, recently [announced his "Code Sandbox MCP"](https://www.linkedin.com/feed/update/urn:li:activity:7353430608515108867?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7353430608515108867%2C7353439287834484736%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3A7353430608515108867%2C7353461170856468482%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287353439287834484736%2Curn%3Ali%3Aactivity%3A7353430608515108867%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287353461170856468482%2Curn%3Ali%3Aactivity%3A7353430608515108867%29), a simple code interpreter for AI agents. This is based on the [LLM Sandbox project](https://vndee.github.io/llm-sandbox/mcp-integration/). Either could be an avenue for future improvement.