---
layout: post
title: "LLM Pricing Comparisons: The Missing Tokenizer Efficiency Factor"
date: 2024-07-02
last_updated: 2024-07-02
description: "Compares LLM pricing across cloud providers, analyzing cost-per-token, subscription tiers, and total cost of ownership for enterprise deployments."
tags: [llm, pricing, tokenizers, efficiency]
---

Recently, [Philipp Schmid shared an interactive LLM pricing comparison tool](https://www.linkedin.com/posts/philipp-schmid-a6a2bb196_ive-converted-the-llm-pricing-comparison-ugcPost-7213897660838129664-UAQy?utm_source=share&utm_medium=member_desktop) hosted on Hugging Face. This tool allows users to filter providers and models, comparing them side-by-side. It's an impressive effort that includes a wide range of providers such as Fireworks AI, Groq, Replicate, and IBM.

While this tool is undoubtedly useful, I couldn't help but wonder about a crucial factor that might be overlooked in these comparisons: the efficiency of different tokenizers, particularly for European languages.

I raised this question in the comments, asking whether the comparison takes into account the varying "compression" ratios achieved by different tokenizers. This is a topic I've explored before, as detailed in [my blog post about tokenizer inefficiency](https://ndurner.github.io/tokenizer-inefficiency-needle-haystack-anthropic-claude).

The efficiency of tokenizers can significantly impact the actual cost of using these models, especially when working with languages other than English. For instance, some tokenizers might require more tokens to represent the same text in German or French compared to English, potentially leading to higher costs for non-English use cases.

Moreover, the landscape of tokenizers is evolving. For example, Llama-3 now builds on and extends OpenAI's cl100k tokenizer. These changes could potentially alter the efficiency ratios I observed in my previous comparisons.

Unfortunately, as of now, I haven't received a response to my inquiry. This lack of engagement is disappointing, as it represents a missed opportunity to discuss an important aspect of LLM pricing that might not be immediately obvious to all users. While comparing raw pricing is useful, understanding the nuances of tokenizer efficiency could provide a more accurate picture of the true cost for different use cases and languages.