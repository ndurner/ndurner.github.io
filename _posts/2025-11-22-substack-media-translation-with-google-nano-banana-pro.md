---
title: "Media translation with Google Nano Banana Pro"
date: 2025-11-22
last_updated: 2025-11-22T09:26:25+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/media-translation-with-google-nano
tags: [Substack]
excerpt: "Google’s new powerful image generation model gemini-3-pro-image-preview, also known as “Nano Banana Pro” or referred to as “Nano Banana 2”, can use input images not just as style references, but as an exact original for translation work. Google Deepmind’s product manager Bea Alessio shared several examples for this: one example was a marketing visual featuring two views from different angles on a "
substack_url: "https://ndurner.substack.com/p/media-translation-with-google-nano"
canonical_url: "https://ndurner.substack.com/p/media-translation-with-google-nano"
sitemap: false
---

Google’s [new powerful image generation model](https://blog.google/technology/ai/nano-banana-pro/) gemini-3-pro-image-preview, also known as “Nano Banana Pro” or referred to as “Nano Banana 2”, can use input images not just as style references, but as an exact original for translation work. Google Deepmind’s product manager Bea Alessio shared several examples for this: one example was a marketing visual featuring two views from different angles on a can of a drink, where the English labels were translated by Nano Banana Pro to Korean. Someone in the live audience remarked that the translation was accurate.

Bea used the Gemini App in her presentation, but the [API documentation](https://ai.google.dev/gemini-api/docs/image-generation) describes the same “text-and-image-to-image” use case in the “Multi-turn image editing” section:

The prompt shown in the documentation is this (after generating the infographic first:

> Update this infographic to be in Spanish. Do not change any other elements of the image.
