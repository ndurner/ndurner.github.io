---
title: "Notes on Google Gemma 4"
date: 2026-04-03
last_updated: 2026-04-03T07:08:11+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/notes-on-google-gemma-4
tags: [Substack]
excerpt: "Google DeepMind have published a new release of their open weights model: Gemma 4. It’s available under Apache License 2.0, an improvement from the more restrictive Gemma 3 license. Core features include multi-language support, Reasoning, and multi-modality including Audio for some models. It comes in four different variants: In the model descriptions, “E” stands for “effective parameters” (withou"
substack_url: "https://ndurner.substack.com/p/notes-on-google-gemma-4"
canonical_url: "https://ndurner.substack.com/p/notes-on-google-gemma-4"
sitemap: false
---

Google DeepMind have published a new release of their open weights model: Gemma 4. It’s available under Apache License 2.0, an improvement from the more restrictive Gemma 3 license. Core features include multi-language support, Reasoning, and multi-modality including Audio for some models. It comes in four different variants:

In the model descriptions, “E” stands for “effective parameters” (without embeddings layer, total size including embeddings layer given in parentheses above), “A” stands for “active parameters”.

The edge-device models E2B and E4B feature a smaller vision encoder than the others (~150M vs. ~550M).

Instructions for using the Audio Capabilities locally through HuggingFace Transformers [here](https://ai.google.dev/gemma/docs/capabilities/audio), instructions for Apple MLX:
