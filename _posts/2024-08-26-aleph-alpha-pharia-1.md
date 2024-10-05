---
layout: post
title: "Pharia-1-LLM: A Closer Look at Aleph Alpha's Latest Release"
date: 2024-08-26
last_updated: 2024-08-26
tags: [ai, llm, germany, synthetic-data, open-source, aleph alpha, pharia]
---

Aleph Alpha recently announced the launch of Pharia-1-LLM, a new language model series with two 7B foundation models. After reviewing the available materials, including the Model Card, I've been able to answer some questions about this release in online discussions. Here's a breakdown of key points and considerations:

## Model Characteristics and Training

Pharia-1-LLM includes two variants: Pharia-1-LLM-7B-control and Pharia-1-LLM-7B-control-aligned. These models are trained on 7 languages and optimized for English, German, French, and Spanish. Aleph Alpha claims they're comparable to other open-source models in the 7-8B parameter range.

In lieu of recent debate about training on synthetic data, an interesting aspect of the training process is that they used synthetic data as well. According to Aleph Alpha's blog post, synthetic data was utilized more extensively for the "aligned" model compared to the "control" model.

## License and Availability

While Aleph Alpha has made both the models and the training code available, it's important to note that this is not a fully open-source release in the traditional sense. The permitted use of the released weights and infrastructure explicitly excludes commercial applications. This limitation sets Pharia-1-LLM apart from some other model releases in the field.

Additionally, the model weights are not released in the SafeTensors format, which has become somewhat of a standard. This choice may impact the ease of use and integration for some researchers and developers.

## The Broader Pharia AI Ecosystem

Alongside Pharia-1-LLM, Aleph Alpha has introduced PhariaAI, described as an end-to-end AI solution for enterprises and governments. It's not yet clear how this new offering relates to or potentially replaces existing tools like the Playground at app.aleph-alpha.com.

## Updates
[Update 28-08-2024]:

The release of Pharia-1-LLM has sparked discussions within the AI community, particularly in Germany. Some have expressed concerns about the model's accessibility and ease of use. [This post](https://www.linkedin.com/posts/tristan-post_die-deutsche-ki-hoffnung-aleph-alpha-hat-activity-7234551741248135170-TmK4?utm_source=share&utm_medium=member_desktop) highlights challenges in installing and running the model.

Key points of criticism include:

1. Difficulty in installation and setup compared to other open-source models
2. Use of a proprietary technology stack instead of widely adopted formats
3. Restrictive licensing that excludes commercial use
4. Limited context window (8k) compared to some competing models

But [experiences vary](https://www.linkedin.com/feed/update/urn:li:activity:7234551741248135170?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7234551741248135170%2C7234945027397881857%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287234945027397881857%2Curn%3Ali%3Aactivity%3A7234551741248135170%29).

[01-09-2024]:

The discussion around Aleph Alpha's Pharia-1-LLM release continues, particularly regarding its licensing. In response to Dr. Daryoush Daniel Vaziri's [post comparing AI model licenses](https://www.linkedin.com/posts/dr-daryoush-daniel-vaziri-262a943b_germanai-kimadeingermany-allefaesreineneinerfaesrkeinen-activity-7235904220116254720-btkT?utm_source=share&utm_medium=member_desktop), I shared some additional thoughts:

Releasing an implemented special approach under some kind of 'Open' license does not yet demonstrate openness and transparency - values that the release apparently intended to convey. In earlier times, such cases were more likely to be referred to as 'Shared Source'. That's exactly what I've taken away: my numerous inquiries here and on X have remained unanswered, so the company doesn't seem ready for a dialogue with the public. The release has been called a 'marketing stunt' elsewhere, and that seems plausible to me.

What remains: the assessment that this is unlikely to give rise to a lively community like the one around Llama, where some real developments are being produced. And where personal investments can thus also bear fruit.