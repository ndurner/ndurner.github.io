---
layout: post
title: "Voice AI Latency"
description: "Analysis of latency in voice AI pipelines using Whisper, Nvidia Parakeet, and translation models, with a spotlight on conversational AI leader Cognigy."
date: 2025-07-12
tags: [llm, whisper, openai, nvidia, voice ai, conversational ai]
last_updated: 2025-08-28T19:54:17+02:00
author: "Nils Durner"
categories: [journal]
---

At a recent joint colloquium of the Bitkom working groups Artificial Intelligence, Metaverse and Virtual & Augmented Reality, a recurring pattern presented was speech transcription using either OpenAI Whisper or Nvidia Parakeet: e.g. so the user could talk to avatars that elaborate about different aspects of a Digital Twin (factory floor, in this case). The processing piplelines seemed staged sequentially: the aggregated Whisper output would then be piped to an LLM. This introduces latencies, as confirmed by one speaker in detail: for Italian language, Whisper Base incurs > 400ms delay, Whisper Medium > 750ms. Adding to that, the translation model Facebook NLLB-600M would, for English, add > 550ms and NLLB-1.3B would add > 700 ms - often approaching 1 second in delays. None of the presenters there discussed realtime voice-to-voice models.

At a difference conference however, Conversational AI Leader¹ "[Cognigy](https://www.cognigy.com)" demoed AI customer agents that interacted with the phone caller without noticable delay. The presenter confirmed that their platform works with "any" LLM provider and does indeed use transcription as part of the pipeline. What makes theirs fluid ~~is processing with "chunking"~~, he said. [Update 2025-07-14: In a follow-up, he clarified that "chunking" is a term from RAG and he doesn't believe this may contribute to low latency.]

¹ [per analysts like Forrester etc.](https://www.cognigy.com/analyst-recognition-awards)

[Update 2025-08-28]: US company NiCE has recently [acquired Cognigy](https://www.forbes.com/sites/maribellopez/2025/07/29/nices-955m-cognigy-deal-targets-30b-ai-customer-experience-opportunity/). Today, OpenAI announced General Availability of its Realtime API, with an improved model, MCP-support, Image inputs, SIP support, Agents SDK update and EU residency.