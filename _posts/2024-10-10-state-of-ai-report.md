---
layout: post
title: "State of AI report"
author: "Nils Durner"
categories: [journal]
tags: [stateofai, llm, ai, olmo, otter, elevenlab, mle-bench, llama]
date: 2024-10-10
last_updated: 2024-10-10
---

The [State of AI report 2024](https://www.stateof.ai) is available. Some notes:
* their definition of "Agent" seems reasonable: "AI Agent: an AI-powered system that can take actions in an environment. For example, an LLM that has access to a suite of tools and has to decide which one to use in order to accomplish a task that it has been prompted to do.". Jaana Dogan, Principal Engineer at Google, recently [remarked](https://x.com/rakyll/status/1837164761362133057) that this term is starkly overloaded and Simon Willison [calling for a robust definition](https://x.com/simonw/status/1843290729260703801)
* "Llama 3 closes the gap between open and closed models"
    * this contrasts with the new [MLE-Bench benchmark by OpenAI](https://arxiv.org/pdf/2410.07095), where llama-3.1-405b-instruct performs significantly worse 
* OLMo 7B Instruct appears as the most open model, with just penalties for "no paper" and "no API access" (page 16)
* Some models are "Likely/Known trained on GSM8k", including OpenChat 3.5 and Qwen 7B /page 17
* "Evaluation for RAG remains unsolved" (page 34).
* "Well-established in image and audio generation, diffusion models continue to demonstrate their effectiveness in generating complex action sequences in robotics." (page 76)
* "Traditional Robotic Process Automation (RPA), embodied by UiPath, has struggled with high set-up costs, brittle execution, and burdensome maintenance. Two novel approaches, FlowMind (JP Morgan) and ECLAIR (Stanford), use foundation models to address these limitations. [...] On web navigation tasks, ECLAIR improved completion rates from 0% to 40%."
* they quote a 100x price drop for OpenAI and 60x price drop for Anthropic year-over-year - by comparing the original GPT-4 with GPT-4o-mini and, even more wildly, Claude 3 Opus with Claude 3 Haiku (page 109)
* "ML tools for AI struggle (again)" (page 118)
    * "In a now familiar cycle, we’re seeing specialist tools and frameworks gain popularity before struggling to scale and enter production, while incumbents demonstrate impressive resilience and adaptability."
    * "Over in framework land, the likes of LangChain and LlamaIndex, having achieved popularity for experimentation, their high-level abstractions and limited flexibility have been called out as a source of friction by some developers, as their needs become more sophisticated."
* "Perplexity struggles with the same hallucination issues that hit other LLM-powered services" (page 120)
* ElevenLabs named leader in TTS
* Avatar video generation product Synthesia: now used by the majority of the Fortune 100 for different learning and representation tasks
* they lend credibility to the [Ramp report](corporate-ai-spending), quoting a spending increase of $58B in Q1 24 over the previous quarter. "Top performers include OpenAI, Grammarly, Anthropic, Midjourney, Otter, and ElevenLabs."
    * From the Otter.ai website: "The #1 AI Meeting Assistant. Never take meeting notes again. Get transcripts, automated summaries, action items, and chat with Otter to get answers from your meetings."
* 2025 Prediction #4: "Early EU AI Act implementation ends up softer than anticipated after lawmakers worry they’ve overreached." (page 205) On the other hand, Forrester's Enza Iannopollo [predicts](https://www.linkedin.com/posts/joerglenz_aiact-forrtech-forrester-ugcPost-7250168499413663745-jEIv): "A genAI provider will draw the first EU #AIAct fine.".
