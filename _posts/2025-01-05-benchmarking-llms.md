---
layout: post
title: "AI Overview: Costs, Performance, and Language Considerations"
author: "Nils Durner"
categories: [journal]
tags: [ai, llm, benchmarks, deepseek]
date: 2025-01-05
last_updated: 2025-01-05
description: "Breaks down FAZ’s AI cost-performance chart, flags tokenization inconsistencies, multilingual cost implications, and advocates for simple custom benchmarks like Pelican-on-a-bicycle."
---

The current state of Large Language Models, their costs and performance was discussed following up on Dr. Holger Schmidt, Editorial Editor at German newspaper FAZ, advertising an "AI Overview" article.

## Cost-Performance Considerations

The discussion highlighted the complexity of comparing AI models based on cost-performance metrics. While the article presented a chart plotting various models' quality index against their cost per million tokens, several important nuances emerged in the comments.
![FAZ AI benchmark overview: chart comparing AI models on quality and cost. X-axis shows price in dollars per million tokens, ranging from 0.1 to 20. Y-axis shows quality index of answers for comparable questions, ranging from 50 to 100. Models are plotted as dots, with names like GPT-4, Gemini 1.5 Pro, and various Llama versions. Generally, models further up and to the left are rated better (higher quality, lower cost). The chart indicates an "attractive quadrant with more favorable and higher-quality services" in the upper left area. It notes that DeepSeek V3 achieves a good quality level and is among the cheapest.](assets/img/faz-ai-benchmark-overview.jpeg)

Mark Neufurth pointed out that the cost-per-performance unit could become a determining factor in AI deployment. He noted that models like Mistral and older versions of Llama appeared to perform well in this regard.

However, I cautioned against oversimplifying the cost analysis. The "token" as a base unit is [not standardized across models](2023-11-27-tokenizer-inefficiency-needle-haystack-anthropic-claude), which can lead to misleading comparisons. This is particularly relevant when considering multilingual capabilities.

## Language Support and Economic Viability

An important aspect that often gets overlooked is the varying support for different languages across AI models. I noted that some Chinese models, for instance, are primarily optimized for Chinese and English. This optimization can result in significantly higher costs when using these models for other European languages.

This observation led to a broader question about the economic viability of supporting languages beyond the major global languages at scale. However, there are [reasons for cautious optimism](https://www.linkedin.com/feed/update/urn:li:activity:7281612533940064256?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7281612533940064256%2C7281630976781246464%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3A7281612533940064256%2C7281675509665525761%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287281630976781246464%2Curn%3Ali%3Aactivity%3A7281612533940064256%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287281675509665525761%2Curn%3Ali%3Aactivity%3A7281612533940064256%29):

1. OpenAI's release announcements suggest multilingualism as an optimization goal, mentioning languages like Gujarati in their [GPT-4o announcement](https://openai.com/index/hello-gpt-4o/).
2. A recent [partnership between OpenAI and AI Singapore](https://www.edb.gov.sg/en/about-edb/media-releases-publications/openai-establishes-presence-in-singapore-to-support-international-expansion.html) aims to promote language diversity.
3. Research by [Chang et al. (2022)](https://arxiv.org/pdf/2205.10964) shows that multilingual models encode some information (like token positions and parts of speech) along shared, language-neutral axes. This suggests potential for efficient cross-lingual learning.

While these developments are promising for language diversity in AI, challenges remain, particularly regarding regional specificities such as laws, norms, and values.

## The Need for Custom Benchmarks

The rapid pace of AI development has led to a proliferation of benchmarks, many of which are academically focused or measure specific capabilities. However, these benchmarks often struggle to keep up with the latest developments or may not address practical concerns like quantization - a technique used by model providers to reduce costs at the expense of quality.

Given these limitations, I advocated for organizations to develop their own "evals" or benchmarks. These custom benchmarks need not be complex initially. For example, Simon Willison's approach of having a language model [draw "a pelican on a bicycle"](pelican-benchmark) provides a simple yet effective starting point. This method allows for gradual refinement based on specific requirements and use cases.

[Update 2025-01-06]: the FAZ benchmark used results from [Artificial Analysis Quality Index](https://artificialanalysis.ai/models/deepseek-v3/providers). In this benchmark, _GPT-4o mini_ ranks higher than _GPT-4o_ - which says a lot about the quality of this "Quality" index, and underscores why own evals are worthwhile to create.