---
layout: post
title: "Google PaLM and MakerSuite"
author: "Nils Durner"
categories: [journal]
tags: [google, palm, makersuite]
date: 2023-05-16
---

Hands-on on Google PaLM API and MakerSuite: Summary: vastly behind GPT-4; more of a competitor to the Llamas.

Details:
* of the 4/5 foundation models discussed at Google I/O, only the "Bison" model is available
* not available in Europe; Google emphasizes in various places that this is a preview, is experimental, ... and its external or production use is prohibited
* MakerSuite is the fancy cousin to the OpenAI Playground
* Three modes:
  * Text Prompt (OpenAI equivalent: text completion)\
![Google PaLM Makerstudio #1](assets/img/google-palm-makerstudio-1.png)
  * Data prompt (haven't tried)
  * Chat prompt\
![Google PaLM Makerstudio #3](assets/img/google-palm-makerstudio-3.png)
* Parameters stowed away behind a button\
![Google PaLM Makerstudio #2](assets/img/google-palm-makerstudio-2.png)
* when asked, the LLM identifies as "LaMDA", like Bard does for me (but I have seen recent (alleged) screenshots on Mastodon where Bard says it's based on either BERT or Bard 🤷🏻‍♂️)
* Confabulation/Hallucination is rampant with both Text and Chat
* even still, the Chat model (chat-bison-001) feels much worse than the Text Completion model (text-bison-001)\
![Google PaLM Makerstudio #3](assets/img/google-palm-makerstudio-3.png) vs.
![Google PaLM Makerstudio #4](assets/img/google-palm-makerstudio-4.png)
* asking for the fastest animal in English works, but fails in German: "Internal Error". 😇
* I couldn't get either grounded in a given body of text to stop the confabulation. I have tried both our "new CEO" press announcement and PaLM sample code, but results using either were riddled with made-up parts. Other established techniques to curb confabulation don't work either.
  * GPT-4 knows its own API; PaLM doesn't - and cannot event follow sample code for it
* Knowledge cut-off is not uniform: Trọng is still president (outdated as of Apr 5 2021), Russia did invade Ukraine (2022), "Queen Elizabeth II is in good health" and recently celebrated her platinum jubilee (outdated as of Sept 8 2022/current as of Feb 6 2022), last Taiwan Lantern/臺灣燈會 festival was 2018/2019, respectively (outdated as of spring 2019/2020; city was always confabulated). NATO has 30 members (outdated as of this year).
* I got several "No content" messages. It's unclear to me whether this is the equivalent to "I don't know" (which GPT-4 has learnt as of late) or was some sort of technical error. I got it frequently with the Chat model when asking for results in JSON.

