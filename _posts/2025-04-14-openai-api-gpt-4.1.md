---
layout: post
title: "OpenAI API: 4.1 in, 4.5 out"
date: 2025-04-05
tags: ["llm", "openai", "gpt", "gpt4"]
last_updated: 2025-04-18
description: "Releases GPT-4.1 in three sizes, reproduces bias vs GPT-4o, adds code diff outputs, notes GPT-4.5 API deprecation, and revisits long-context prompting and diff formats."
author: "Nils Durner"
categories: [journal]
---

OpenAI have announced their newest flagship model family: GPT-4.1. It comes in three sizes: GPT-4.1, 4.1-mini, and 4.1-nano.

Two versions of GPT-4.1 were available in the last weeks for community testing via OpenRouter as "Optimus Alpha" and "Quasar Alpha". There, I noticed that the gender bias sample showcased in the [Stanford HAI AI Index Report](stanford-ai-index) was present there as well - but didn't show with GPT-4o. The released version of GPT-4.1 exhibits this as well.

For coding tasks - one of the strengths advertised - its behaviour has changed from GPT-4o: it sometimes gives pseudo diff files. These lack file numbers, so won't apply with GNU patch, but interesting trait nonetheless. And it's fast, compared to GPT-4.5.

GPT-4.5 is set to be removed from the API on 2025-07-14, per the [deprecation page](https://platform.openai.com/docs/deprecations/). Ethan Mollick comments: "You can increasingly only access the high power, high cost models (GPT-4.5, Deep Research) through ChatGPT while the API supports cheap fast models (the new GPT-4.1).". I [don't agree](https://www.linkedin.com/feed/update/urn:li:activity:7317637149552431104?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7317637149552431104%2C7317650156269510656%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287317650156269510656%2Curn%3Ali%3Aactivity%3A7317637149552431104%29), however: the recent release of the o1-pro model on the API is a counter-example. Further, there is no confirmation that ChatGPT would retain it or Azure might discontinue it also. ([Azure discontinuation page](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/model-retirements), GPT-4-32K had a later discontinuation date on Azure than on the OpenAI API).

[Update 2025-04-15]
* Ethan Mollick countered on X, alledging that neither Operator or Deep Research were available on the API. Not true, however: the building blocks of Operator are available, as the model "computer-use-preview" and the tool "computer_use_preview" in the Responses API ([my response](https://x.com/ndurner/status/1911991270341255569))
* Simon Willison [remarks](https://simonwillison.net/2025/Apr/14/gpt-4-1/) that GPT-4.1 is trained "up to May 31, 2025". Also, he remarks that describing an image with GPT-4.1-nano cost him just 0.0232 US cents.
* per the [Prompting Guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide), ideal prompting is more complex that simple language use. Particularly, "ideally place your instructions at both the beginning and end of the provided context" for long contexts is back. The prompting advice given in my [article about process visualization](ai-assisted-process-visualiaztion-collaboration.md) still seems solid, though.

[Update 2025-05-18]
The diff file format is described in the [Appendix of the GPT-4.1 Prompting Guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide#appendix-generating-and-applying-file-diffs): it's V4A format. There are prompts and a reference implementation, as well as two alternative formats: the one from Aider’s Polyglot Benchmark and a pseudo-XML format. Neither of these includes line numbers.