---
layout: post
title: "AI Deployment in Germany: Practical Considerations"
author: "Nils Durner"
categories: [journal]
tags: [ai, azure, aws, google-cloud, aleph alpha]
date: 2024-09-08
last_updated: 2024-09-20
---

The recent news about [Aleph Alpha's strategic shift](https://www.bloomberg.com/news/articles/2024-09-05/the-rise-and-pivot-of-germany-s-one-time-ai-champion) away from developing large language models (LLMs) to focus on AI integration services has sparked discussions about the state of AI deployment in Germany. While this change might seem discouraging for those hoping for a strong European contender in the AI race, it's worth examining the practical options still available for businesses looking to leverage AI technologies within German borders.

One key consideration for many German businesses, especially in sensitive sectors, is the need to process and store data within Germany or the EU. This requirement often narrows the field of available AI models and services. However, there are still some noteworthy options:

1. AWS in Frankfurt "eu-central-1" availability region offers Anthropic's "Claude 3.5 Sonnet" model, which could serve as a viable alternative to GPT-4o for many use cases. However, Provisioned Throughput Units (PTU) seem to be available only for the older "Claude 3 Sonnet" model.

2. Google Vertex AI appears to offer Gemini 1.5 Pro with PTU in Frankfurt, though with a caveat: "Orders for provisioned throughput are processed on a best-effort basis. Depending on the size of your order and available capacity, it may take up to several weeks for the order to be approved and fulfilled."

3. Azure's offerings in Germany are more limited, but it might be worth checking availability in nearby regions like Sweden for a broader selection of models.

For those considering on-premises solutions, the idea of purchasing NVIDIA cards and self-hosting models has come up in discussions. While this approach offers maximum control over data and infrastructure, it comes with its own set of challenges, including the need for specialized expertise and potentially significant upfront costs. A viable middle-ground could be closely analyzing if the use-cases in question might be attainable without Frontier Models and instead relying on Open Weights models in the 70B or even 8B category - which can be served through more widely available deployments options including AWS SageMaker or EC2 straight.

[Update 2024-09-29]
GPT-4o can be consumed via Azure with German data residency through [Provisioned Deployment](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#provisioned-deployment-model-availability).