---
layout: post
title: "Questioning the 'LLMs Can't Reason' Claim"
author: "Nils Durner"
categories: [journal]
tags: [llm, reasoning, ai research, benchmarks, openai, o1]
date: 2024-10-20
last_updated: 2024-10-20
---

A recent paper from Apple about reasoning deficits has been widely reposted as ["LLMs Can't Reason"](https://arxiv.org/pdf/2410.05229). The study claims to demonstrate significant limitations in the reasoning capabilities of large language models (LLMs). Gary Marcus, author of a "Forbes 7 Must Read Books in AI", [railed](https://substack.com/home/post/p-150104196): "There is just no way can you build reliable agents on this foundation". However, upon closer examination, there are several aspects of the research that warrant scrutiny and further discussion.

## Model Selection and Performance Representation

The study's model selection appears oddly skewed. With the exception of two models, most of those tested fall below the 70 billion parameter threshold. This raises questions about the representativeness of the sample, especially when considering the current state-of-the-art in LLM development.

The performance of GPT-4o, as reported in the study, was particularly surprising. In my limited manual testing, I was unable to reproduce the issues described. This discrepancy highlights the need for transparency regarding which specific revision of GPT-4o was used in the study.

A glaring omission in the study is the lack of Anthropic models. Including these would likely have provided an additional set of strong results, offering a more comprehensive view of current LLM capabilities. ([LinkedIn discussion thread](https://www.linkedin.com/feed/update/urn:li:ugcPost:7252380116381503489?commentUrn=urn%3Ali%3Acomment%3A%28ugcPost%3A7252380116381503489%2C7252580712619339778%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287252580712619339778%2Curn%3Ali%3AugcPost%3A7252380116381503489%29))

## Prompting and Fine-Tuning Considerations

While the researchers claim to use chain-of-thought prompting, their template appears rather basic. This prompt structure, while encouraging step-by-step thinking, doesn't account for the sophisticated "thinking" choreography often built into larger models. It's possible that this simplistic approach fails to fully engage the models' reasoning capabilities, particularly for more advanced LLMs.

[Andrew Mayne's blog post](https://andrewmayne.com/2024/10/18/can-you-dramatically-improve-results-on-the-latest-large-language-model-reasoning-benchmark-with-a-simple-prompt/) demonstrates that by simply adding a brief prompt about potential trick questions, the performance of models like o1-preview and GPT-4o-mini dramatically improves on the GSM-NoOp benchmark the Apple researchers propose. This suggests that the issue might be more related to training data and fine-tuning rather than an inherent lack of reasoning ability.

Mayne's experiment highlights a crucial oversight in the study: the researchers didn't attempt any creative prompting to address the challenges posed by their benchmarks. This omission is particularly striking given the well-known impact of prompt engineering on LLM performance.

Furthermore, the dramatic improvement achieved with a simple prompt modification calls into question the study's claim that the problem "cannot be resolved with few-shot prompting or fine-tuning". It suggests that with appropriate prompting or fine-tuning, these models might perform significantly better on reasoning tasks than the study indicates.

## Potential for Bias?

Given these observations, it's difficult not to speculate whether the study was designed to support a pre-formed conclusion. The overly general claim that "LLMs can't reason" seems at odds with the limited scope of models tested and the peculiar presentation of results.

## A Call for Replication

To either support or debunk the paper's broad claims, it would be valuable to see this study replicated with state-of-the-art models in the >70B parameter class. This would provide a more accurate representation of the current capabilities of large language models in reasoning tasks.

## Alternative Approaches to Reasoning

Interestingly, some researchers have explored using Prolog as a vehicle for formal reasoning in AI systems. While I haven't had personal experience with Prolog (thankfully avoiding it thus far), it could potentially offer an alternative approach to addressing reasoning challenges in LLMs.

## Conclusion
As Andrew Mayne aptly put it:
> I have come to the realization that people will spend more time re-posting papers like this than actually trying the problems posed in them or looking closer at the results.