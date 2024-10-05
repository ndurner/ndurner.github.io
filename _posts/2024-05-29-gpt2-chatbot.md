---
layout: post
title: "GPT2 Chatbot"
date: 2024-05-29
last_updated: 2024-05-29
tags: [gpt2, openai, lmsys, chatbot-arena]
---

People on Social Media are excited about a new model on the LMSYS Chatbot Arena: gpt2-chatbot. Some theorize that it may be GPT-2. I have fingerprinted the Tokenizer, and no: not GPT-2, but consistent with OpenAI cl100k (used for GPT 3.5 onwards). Peculiar gaps in world knowledge (both niche and common knowledge) were the same as in the other GPTs, but not Llama 3 or Gemini 1.5 Pro, for example. I have experienced poor steerability (worse than GPT-4 Turbo), so concluded for myself that it 1) isn‘t GPT 4.5 or something like that, 2) perhaps overfitted on training data. Maybe coincidence, maybe not: the FineWeb dataset page on HuggingFace uses the same „gpt2“ moniker, and probably does refer to GPT-2.

Use of cl100k doesn't imply OpenAI ownership, though: the tokenizer is Open Source.