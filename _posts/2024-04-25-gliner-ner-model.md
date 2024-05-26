---
layout: post
title: "GLiNER NER model"
date: 2024-04-25
tags: [llm, ner]
---

Urchade Zaratiana has released GLiNER, an NER model created "that can identify any type of entity using a bidirectional transformer encoder". One of the ToDos listed is „Allow longer context“, and a closer look reveals that:
 * The Colab caps out at 384 tokens, and
 * confirms DebertaV2 architecture.

Interesting, but too restricted as of now.