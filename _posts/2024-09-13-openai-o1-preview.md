---
layout: post
title: "OpenAI O1 First impressions"
author: "Nils Durner"
categories: [journal]
tags: [openai, o1]
date: 2024-09-13
last_updated: 2024-09-17
---

So OpenAI have released a preview of their new O1 model(s): [Landing Page](https://openai.com/o1/). This is a specialized model and departs from the tradition of the other GPT models. It is available to paid ChatGPT subscribers, to Tier 5 API customers and via OpenRouter.
 
What's special about the O1 model family is that, in marketing speak, "spend more time thinking through problems before they respond". In practice, that means that they have been training to do what's called "Chain-of-Thought" (CoT) - something that in principle was possible before through prompting. From the [System Card](https://assets.ctfassets.net/kftzwdyauwt9/67qJD51Aur3eIc96iOfeOP/71551c3d223cd97e591aa89567306912/o1_system_card.pdf):
Through training, the models learn to refine their thinking process, try different strategies, and recognize their mistakes. Reasoning allows o1 models to follow specific guidelines and model policies we’ve set, ensuring they act in line with our safety expectations. This means they are better at providing helpful answers and resisting attempts to bypass safety rules, to avoid producing unsafe or inappropriate content
One extension to CoT is a prompting technique called ["Plan Like a Graph"](https://arxiv.org/abs/2402.02805), which allows LLMs to determine the total time it takes to complete a task with parallelizable subtasks. In my tests, O1 does PlaG by automatically, without being told to.
One practical implication of how it's different from the GPTs is that the temperature parameter is not supported.

Given that's a different model and not a full successor to the GPT-4 family, it's not expected to do better on all tasks. Some users on X report worse performance over GPT-4o on private benchmarks. Also, it's rather expensive via API: $15 per Million input tokens, $60 per Million Output tokens (vs. $5/$15 with GPT-4o) - and for its thinking, it uses an awful lot of output tokens.
 
Work in progress: subsuming this under the "LLM" umbrella could be a mischaracterization. I haven't seen an alternative term emerge yet, however.
 
[Update 2024-09-15] \
One practical implication of how it's different from the GPTs is that the temperature parameter is not supported.

Also, it's currently not multi-modal: it's text-to-text only.

On the categorization and characterization of O1: Yuchen Lin, Research Scientist at the Allen Institute for AI (AI2), confirmed that comparing GPT with O1 seems apples/oranges and a new category may make sense to establish for their evaluations and leaderboards.

For differentiation purposes, I'm taking inspiration from this Bloomberg article and will tentatively use "Reasoning LLMs" vs. "traditional LLMs" (🇩🇪 "Reasoning-Sprachmodelle" vs. "herkömmliche Sprachmodelle"). Or more expansive: "Reasoning LLMs like Open O1" vs. "GPT and in the sense of the AI2 WildBench ranking similar LLMs". This implicitly acknowledges (early) community efforts in cloning the O1 approach.

[Update 2024-09-16]
Nicely documented use-case: Spellbook Associate, an AI Agent that allegedly "can work through multi-document legal matters": https://www.spellbook.legal/blog/openai-o1-for-law-legal-spellbook.
 
Interesting: the "o1 for Legal Math" section on this website. That LLMs perhaps can do math now is a key takeaway from "Plan like a Graph" - all you have to do is let the LLM do planning on a word problem (🇩🇪 "Sachaufgabe") first, rather than presenting the raw formula straight? Or is this maybe (just) a result of the new o200k_base tokenizer that both GPT-4o and O1 share?
 
Personal success story: was stuck on an Apple CloudKit dataset filtering problem. None of the other usual helpers (GPT-4/-Turbo/-4o, Claude 3.5, Llama 3.1 405B) could figure it out, but O1 did. Cost: $0.40 for two chat turns.

[Update 2024-09-17]
On the math capabilities: at least with multiplication, O1 accuracy seems to depend on the number of digits. It's better than GPT-4o, but not perfect either. [Thread on X](https://x.com/yuntiandeng/status/1836114401213989366) with accuracy charts.