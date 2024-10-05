---
layout: post
title: "IBM Research: synthetic Q&A"
date: 2024-03-08
last_updated: 2024-03-08
tags: [ai, ibm, qa, finetuning]
---

IBM Research introduces "LAB": "Large-scale Alignment for chatBots".
From their blogpost:
> The large language models (LLMs) behind modern chatbots are pre-trained on the raw text to learn an abstract representation of language. This then primes them to learn many tasks quickly once they see labeled, detailed instructions during alignment. But quality instruction data is hard to come by. [...] IBM has a new solution: Large-scale Alignment for chatBots, or LAB. It’s a method for systematically generating synthetic data for the tasks you want your chatbot to accomplish, and for assimilating new knowledge and capabilities into the foundation model [...]

Better high-level low-level 😉 overview: https://huggingface.co/ibm/labradorite-13b#method

Paper: https://arxiv.org/pdf/2403.01081.pdf

Would love to see a comparison - and synthesis? - with Bonito by Nayak et al. https://huggingface.co/papers/2402.18334. 