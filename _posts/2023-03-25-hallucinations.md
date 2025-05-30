---
layout: post
title: "Hallucinations"
author: "Nils Durner"
categories: [journal]
tags: [gpt, hallucination]
date: 2023-03-25
last_updated: 2023-03-25
description: "Discusses mitigating hallucinations in large language models by grounding GPT-3 inputs with event-specific news articles, referencing key research on faithfulness."
---

From a research paper attached that touches on Hallucinations:
> To mitigate hallucinations [43, 44] which are common in large language models, we ground the input context to GPT-3 with news articles from the event cluster [...] to ensure the generated questions are relevant to the event.

Source: [SmartBook: AI-Assisted Situation Report Generation](https://arxiv.org/abs/2303.14337)

[43](https://arxiv.org/abs/2202.03629) Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y., Madotto, A., Fung, P.: Survey of hallucination in natural language generation. ACM Computing Surveys

[44](https://arxiv.org/abs/2005.00661) Maynez, J., Narayan, S., Bohnet, B., McDonald, R.: On faithfulness and factuality in abstractive summarization. In: Proceedings of the 58th SmartBook 23 Annual Meeting of the Association for Computational Linguistics, pp. 1906–1919 (2020)
