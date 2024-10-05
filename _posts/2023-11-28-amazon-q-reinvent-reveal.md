---
layout: post
title: "Amazon Q: A Closer Look at re:invent Reveal"
date: 2023-11-28
last_updated: 2023-11-28
tags: [Amazon Q, re:invent, AI, Enterprise Solutions]
filename: 2023-11-28-amazon-q-reinvent-reveal.md
---

Rumors hinted that a new model, **Amazon Q**, would be introduced at **re:invent**. Turns out, in [Miles Brundage's categorization](https://youtu.be/5j4U2UzJWfI?t=5857), it's rather a System. The closest analogy I can think of is "ChatGPT Plus for Enterprise". 

Screen cap #1 is for the ones interested in design: after clicking the small "Q" in the upper left corner in front of the "Edit narrative", a drop-down appears that will let users select something to the effect of "Make it longer" etc.

![Screenshot #1](assets/img/Screenshot%202023-11-28%20184604.png)


This, like the rest below, reminds me of that one Steve Jobs quote, about Microsoft at that time...

> The only problem with [them] is they just have no taste. They have absolutely no taste. And I don't mean that in a small way, I mean that in a big way, in the sense that they don't think of original ideas, and they don't bring much culture into their products.

Accordingly, the only remarkable theme of the session was how they re-enacted established AI/ML concepts (fundamentally informed by Microsoft Research, I believe? Funnily enough!) like Agents, Tool-Use and Guardrails - which is good in some way, but not at all "re-invented".

The real 🍿✨ was in the subtitles: Nvidia's GPUs became "Xeon CPUs", and a BWM "Charting Service" became a "Charging Service". This may have to do with the news of "[AWS AI services, including Transcribe, **enhanced** with FM-powered capabilities](https://aws.amazon.com/de/blogs/machine-learning/aws-ai-services-enhanced-with-fm-powered-capabilities/)". And hallucinatory hilarity ensued 😆.

(Serves as a warning regarding **Bard**, which [reportedly](https://www.golem.de/news/kuenstliche-intelligenz-google-bard-versucht-youtube-videos-zu-analysieren-2311-179681.html) can now, in the US, work on YouTube videos - based on the transcripts).

Aside from all that, Georgi Gerganov of Llama.cpp has published [a walkthrough](https://github.com/ggerganov/llama.cpp/discussions/4225) of how to deploy quantized models for inference on EC2. This is a nice middle ground to running models locally, perhaps on Apple Silicon, and the train-wreck (word play! 🎉) that is Amazon SageMaker.


Pricing:
> Once the preview period ends, a tier for business users will cost \$20 per person per month. A version with additional features for developers and IT workers will cost \$25 per person per month. The Copilot for Microsoft 365 and Duet AI for Google Workspace for business workers both cost \$30 per person per month.
([Source](https://www.cnbc.com/2023/11/28/amazon-announces-q-an-ai-chatbot-for-businesses.html))