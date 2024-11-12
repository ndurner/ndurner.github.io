---
layout: post
title: "Open Source AI: A Reality Check"
date: 2024-11-12
tags: ["AI", "Open Source", "Llama", "MOLMo"]
description: "How recent developments challenge outdated narratives about open source AI"
last_updated: 2024-11-12
author: "Nils Durner"
categories: [journal]
---

A WIRED article from August 2023 about "The Myth of 'Open Source' AI" resurfaced [in my feed](https://www.linkedin.com/feed/update/urn:li:activity:7261265671450202112?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7261265671450202112%2C7261678166912503808%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287261678166912503808%2Curn%3Ali%3Aactivity%3A7261265671450202112%29) yesterday. The article, which focused on Meta's Llama 2 release, raised concerns about the true openness of AI models. However, the field's developments over the past 12+ months present a different picture.

Since Llama 2, Meta has released Llama 3, 3.1, and 3.2, each addressing previous limitations. The latest Llama 3.2 includes 1B and 3B parameter models specifically designed for edge and mobile devices, supporting 128K context windows and multilingual capabilities. Moreover, Meta's licensing has evolved, now explicitly allowing model outputs to be used for improving other models.

The article asserted that "computer power required to train a large model is beyond the reach of any normal developer or company, typically requiring tens or hundreds of millions of dollars for a single training run." As of now, training a GPT-2 XL scale model (1.5B parameters) costs [around $233 on consumer hardware](https://github.com/KellerJordan/modded-nanogpt) and finishes [within a week](https://github.com/KellerJordan/modded-nanogpt/blob/master/records/102024_ScaleUp1B/ad8d7ae5-7b2d-4ee9-bc52-f912e9174d7a.txt), as demonstrated by the NanoGPT speedrun project.

While larger models operate at a different scale, today's technical landscape shows similar efficiency gains. [AI2's MOLMo](https://molmo.allenai.org/blog) demonstrates that efficient approaches can achieve state-of-the-art results with drastically reduced resources. Their multimodal models use a meticulously curated dataset of under 1 million images - a thousand times less than typical approaches - while matching proprietary systems' capabilities.

The ecosystem is maturing on multiple fronts. Last week, the three Bitkom working groups on Intellectual Property, Open Source and Artificial Intelligence met to discuss legal frameworks and practical implications. Meanwhile, European initiatives like pleias.fr are contributing foundational work with their Common Corpus of over 2 trillion high-quality, multilingual tokens, and today at WebSummit, they're announcing their own open science models.

While competitive "open" LLMs/VLMs may not be as open as e.g. SQLite, the technical and legal barriers cited in last year's article are being systematically addressed. Through efficiency gains in training, evolving open source practices, and rapid iteration of models, the landscape of open source AI has dramatically changed in just over a year.