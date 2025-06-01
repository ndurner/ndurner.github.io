---
layout: post
title: "OpenAI Agents additions"
date: 2025-03-13
tags: ["ai", "agents", "operator", "tool use", "computer use"]
last_updated: 2025-03-13
description: "Details OpenAI’s Web/File Search, Computer Use agent APIs, and SDK updates beyond Swarm, including demo script and cost breakdown (~3¢ per 1024×768 screenshot round-trip)."
author: "Nils Durner"
categories: [journal]
---

OpenAI have made additional agentic features available to developers: Web Search, File Search, Computer Use and an SDK that improves on Swarm ([Announcement](https://x.com/OpenAIDevs/status/1899531225468969240)). The "Computer Use" API gives access to the CUA model, which also powers [OpenAI Operator](operator-testdrive).

My notes on this:
* fixed "Bing search: OpenAI news" with initial screenshot [demo script here](https://gist.github.com/ndurner/36f2b309db493c72ab305fdbfb12ac58)
* the new OpenAI model feature pages also detail [costs for Computer Use](https://platform.openai.com/docs/models/computer-use-preview)
    * measured via OpenAI dashboard: the first round-trip for the demo above with a 1024x768 screenshot can cost 3 US cents
> usage=ResponseUsage(input_tokens=4051, output_tokens=50, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=4101, input_tokens_details={'cached_tokens': 0})