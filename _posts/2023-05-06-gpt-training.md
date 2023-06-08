---
layout: post
title: "GPT Training Data"
author: "Nils Durner"
categories: [journal]
tags: [gpt, openai, gpt4]
date: 2023-05-06
---

One colleague recently shared that ChatGPT knows the inside of a (rare?) book which is not available in fulltext online, concluding that they must have scanned works. This study takes a systematic approach to survey this: [An Archaeology of Books Known to ChatGPT/GPT-4](https://arxiv.org/abs/2305.00118). Code and data here: [gpt4-books](https://github.com/bamman-group/gpt4-books).
Furthermore, [this other study](https://arxiv.org/abs/2305.00050) presents proof that academic work has been used:
> To test whether the LLM has been trained on and memorized the Tübingen dataset, we apply our memorization test [...] We find that GPT-3.5 is able to correctly recall 58% of the remaining cells in the dataset, and recall 19% of the rows without error. Our memorization test with GPT-4 is able to recall 61% of remaining cells in the dataset and 25% of rows without error. These results indicate that the Tübingen dataset is certainly in GPT’s training set and that GPT has had an opportunity to memorize the dataset. However, the gap between percentage of inputs memorized and LLMs accuracy is still significant and more work is needed to understand the role of memorization for the inputs that are not captured by our memorization test

(via [Benjamin Han](https://www.linkedin.com/in/benjaminhan/))