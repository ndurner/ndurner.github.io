---
layout: post
title: "Google's Gemini: Predictions and Implications"
date: 2023-09-18
last_updated: 2023-09-18
description: "Forecasts Google Gemini GA timeline using GPT-4 rollout benchmarks, and notes Reuters intel on preview access and model size variations vs. GPT-4."
tags: [Google, Gemini, AI, GPT-4]
---

Google has allegedly given a few companies preview access to Gemini: [Reuters](https://www.reuters.com/technology/google-nears-release-ai-software-gemini-information-2023-09-15/). Some commenter predicted General Availability in December. If the GPT-4 timeline is any measure, that's not unreasonable to assume:

```
GPT-4 announcement: 03-14
I got private access: 03-17 (+3 weekdays)
General Availability: 07-06 (+ 82 weekdays)
```

So:

```
Gemini private beta: 09-14?
                    + 82 weekdays
=> ?GA in January?
```

Back to the article: noteworthy detail:

> [gave] access to a **relatively** **large** version of Gemini, but **not the largest version** it is developing which would be more on par with GPT-4

Also, Gemini will not be directly "upwards compatible" from PaLM 2, based on the original [announcement](https://blog.google/technology/ai/google-palm-2-ai-large-language-model/):

> Once fine-tuned and rigorously tested for safety, Gemini will be available at various sizes and capabilities, just like PaLM 2, to ensure it can be deployed across different products, applications, and devices for everyone’s benefit.

... meaning that one can't just prepare using Google Vertex AI & PaLM 2 and absolutely expect to be fully done on Gemini release day.