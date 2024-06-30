---
layout: post
title: "GPT-4o multimodality cookbook"
date: 2024-05-15
tags: [LLM, VLM, GPT-4, multi-modality, gemini]
---

OpenAI have updated the API cookbook to walk through the basics of multimodality and using GPT-4o via the API. However, the code sample there proves that GPT-4o does not (yet?) process video natively and instead relies on images extracted. The code sample does this at a fixed sampling rate of 0.5 Hz (so every two seconds). My [question if there are established ways to improve this](https://www.linkedin.com/feed/update/urn:li:activity:7196546535512252418?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7196546535512252418%2C7196762776894062592%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287196762776894062592%2Curn%3Ali%3Aactivity%3A7196546535512252418%29) (e.g. by relying on key frames in the MPEG stream) remained unanswered, perhaps highlighting that:
1. for practical purposes, one should rely on the (alleged) native video processign capabilites of Google Gemini
2. more research in that area is needed