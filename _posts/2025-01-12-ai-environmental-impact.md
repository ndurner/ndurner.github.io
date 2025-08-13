---
layout: post
title: "The Environmental Impact of AI: From Individual Use to Data Centers"
date: 2025-01-12
tags: ["ai", "chatgpt", "openai", "environment", "ESG"]
description: "Exploring the nuanced reality of AI's energy consumption, from personal use to large-scale data centers"
last_updated: 2025-01-12T10:45:46+01:00
author: "Nils Durner"
categories: [journal]
---

Recent discussions about artificial intelligence like to focus on its environmental impact, particularly its energy consumption. The intricacies of this issue surfaced first in private conversations, then on LinkedIn, prompted by a comprehensive article from BloombergNEF, a respected strategic research provider covering global commodity markets and disruptive technologies.

While an environmentally concious user may ackknowledge the usefulness e.g. of the [newly announced ChatGPT integration in WhatsApp](https://help.openai.com/en/articles/10193193-1-800-chatgpt-calling-and-messaging-chatgpt-with-your-phone), there are apprehensions about the computational demands and consequent energy consumption of these services. This perspective, while not unfounded, requires a more nuanced examination.

As detailed in a [recent BloombergNEF report](https://about.bnef.com/blog/liebreich-generative-ai-the-power-and-the-glory/), the power demand from AI data centers is indeed significant and growing. The report estimates that global data center demand could triple to around 1,500 terawatt-hours by 2030, growing from about 1.5% to 4.5% of total global power demand.

However, this macro-level view doesn't tell the whole story. As I [pointed out on LinkedIn](https://www.linkedin.com/feed/update/urn:li:ugcPost:7283938984030834688?commentUrn=urn%3Ali%3Acomment%3A%28ugcPost%3A7283938984030834688%2C7283941825684340736%29):
* free users of ChatGPT use the "GPT-4o mini" model
* this is is rumored to merely have 8 billion parameters ([source](https://arxiv.org/pdf/2412.19260), the authors note that this is a guesstimate)
    * (seems too low to me, but what do we know)
* such 8B models run very well on MacBook Pros on battery, for quite some time
The power consumption of ChatGPT-over-WhatsApp in particular does not seem worth a bad conscience thus.

This aligns with the BloombergNEF report's discussion of energy efficiency improvements. The report notes that "Nvidia claims to have delivered a 45,000 improvement in energy efficiency per token (a unit of data processed by AI models) over the past eight years."

The BloombergNEF report also addresses the efforts of major tech companies towards achieving net zero emissions. It notes that Google, Microsoft, and Meta aim for net zero by 2030. (AWS [report](https://sustainability.aboutamazon.com/climate-solutions/carbon-free-energy) they matched their power needs with renewable energy in 2023). These companies have become some of the most significant corporate purchasers of renewable energy in the world.

However, the report also highlights the challenges these companies face in meeting their commitments as AI usage grows. It notes that their power use has more than doubled since 2020, with Google seeing a 48% increase in carbon emissions since 2019 and Microsoft a 29% increase since 2020.

These various perspectives illustrate the complexity of assessing AI's environmental impact:

1. At the individual level, using AI services (especially free tiers with smaller models) has minimal environmental impact.
2. Efficiency gains in AI models and hardware are significant and ongoing.
3. Major cloud providers are making strides towards carbon neutrality.
4. However, the rapid growth in AI usage poses challenges to these environmental goals.
