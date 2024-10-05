---
layout: post
title: "Gemini Large context & Video"
date: 2024-04-03
last_updated: 2024-04-03
tags: [gemini, llm, large context]
---

RAGfluencers are of course discontent with Gemini's very large 1 million token context window, noting the high costs associated with a large number of input tokens. "It feels like a very niche use case".

The niche for the the 1M tokens would be multi-modality in general and video in particular. My modest experiments suggest that the model does not (just) work on extracted still images (as I understood from their paper), but at the same time considers the audio as well. Would appreciate some more rigorous analysis thereof! ([LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7181231366213136384?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7181231366213136384%2C7181238881818677248%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287181238881818677248%2Curn%3Ali%3Aactivity%3A7181231366213136384%29))

[Update:] Test-setup: a video of wandering around the office and giving names to items. Along the way, tipping over the hand-sanitizer bottle "Erika".\
Result: Gemini (via Google AI Studio) can reproduce the items and names, but misses the toppeled bottle (when asked "what happened to Erika"). When asked if it fell to the floor, Gemini said Yes (it did not).

My conclusion:
* it does combine video and audio
* but it may still be still images from the video, perhaps passed to the LLM with timestamps along with timestamps from an audio transcript