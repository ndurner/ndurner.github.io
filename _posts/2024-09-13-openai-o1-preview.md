---
layout: post
title: "OpenAI O1 First impressions"
author: "Nils Durner"
categories: [journal]
tags: [openai, o1]
date: 2024-09-13
last_updated: 2024-09-15
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