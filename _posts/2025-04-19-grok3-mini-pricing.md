---
layout: post
title: "Grok 3 Mini Pricing"
date: 2025-04-19
tags: ["llm", "grok", "gpt", "gpt4", "openai", "o1", "o4"]
last_updated: 2025-04-19
author: "Nils Durner"
categories: [journal]
---

Artificial Analysis, an "Independent analysis of AI models and hosting providers" outlet, have published a chart plotting "Intelligence Index vs. Price" ([X post](https://x.com/ArtificialAnlys/status/1913057626117820438)). This places Grok 3 Mini Reasoning at the upper left corner, inside the "Most attractive quadrant". According to this, it has the best intelligence/price ratio - even at High-Reasoning capacity. The catch: price is measured by token prices, and [tokenizer inefficiencies](tokenizer-inefficiency-needle-haystack-anthropic-claude) already cast [doubt on the chart's accuracy](https://x.com/strickvl/status/1913163649029374222). Further, the "internal monolog" of reasoning models [can vary](https://x.com/ndurner/status/1913252803113254913)) - but implicit caching may again alleviate costs in multi-turn chats.

So I repeated some of the English-language visualization tasks from [my recent article](ai-assisted-process-visualiaztion-collaboration) via OpenRouter:
* Grok 3 Mini does incur more tokens than OpenAI o4-mini even on input, up to 10-17%
* Reasoning may also incur more token use (up to 25%), but may also use less
* output texts are also longer than o4-mini, up to 3x
* (the length of reasoning seems to vary between re-tries, in one case with o4-mini having been 1,5x as large)

Despite the generally higher token use, Grok 3 Mini is much cheaper in total, up to 1/18th of o4-mini. With one unpublished German-language visualization task, Grok 3 Mini incured 1/11th of the cost of o4-mini.