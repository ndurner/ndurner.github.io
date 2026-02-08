---
title: "Kimi K2 Thinking"
date: 2025-11-08
last_updated: 2025-11-08T17:55:57+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/kimi-k2-thinking
tags: [Substack]
excerpt: "Chinese Lab Moonshot AI has released a reasoning text-only LLM. Following Sebastian Raschka, K2 Thinking architecturally seems like a scaled up version of DeepSeek R1 in certain ways, e.g. the 1 trillion parameters (1T vs 671B) or the larger context size (256K vs. 128K). Writing K2 Thinking scores below the non-thinking variant, K2 Instruct, on the EQ Bench Creative Writing leaderboard, with worse"
substack_url: "https://ndurner.substack.com/p/kimi-k2-thinking"
canonical_url: "https://ndurner.substack.com/p/kimi-k2-thinking"
sitemap: false
---

Chinese Lab Moonshot AI has released a reasoning text-only LLM. Following Sebastian Raschka, K2 Thinking architecturally [seems like a scaled up version of DeepSeek R1](https://x.com/rasbt/status/1986511951141441648?s=20) in certain ways, e.g. the 1 trillion parameters (1T vs 671B) or the larger context size ([256K](https://x.com/rasbt/status/1986522069262123425?s=20) vs. 128K).

## Writing

K2 Thinking scores below the non-thinking variant, K2 Instruct, on the [EQ Bench Creative Writing leaderboard](https://eqbench.com/creative_writing.html), with worse “Slop” and “Repetition” scores; producing only half the length. (The score could still change as the [documentation notes that temperature=1 gives the best performance](https://platform.moonshot.ai/docs/guide/use-kimi-k2-thinking-model#multi-step-tool-call), but the benchmark [authors use temp=0.7](https://x.com/sam_paech/status/1986995815228055988?s=20)). Derya Unutmaz praises its “[creativity and prose at least four out of five stars](https://x.com/DeryaTR_/status/1987140084747939980?s=20)”, but according to my limited testing, it appears undertrained in German: occasionally broken syntax and grammar, unidiomatic word choice (mak...
