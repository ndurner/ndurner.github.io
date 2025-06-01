---
layout: post
title: "Training LLMs"
author: "Nils Durner"
categories: [journal]
tags: [gpt, gpt4, amazon, bedrock]
date: 2023-04-14
last_updated: 2023-04-14
description: "Highlights Amazon Bedrock’s simple model customization via few-shot examples in S3, and parallels GPT-4 fine-tuning for RSS tweet scoring with 10–20 samples."
---

From the Amazon (pre-)announcement of Bedrock:
> One of the most important capabilities of Bedrock is how easy it is to **customize a model**. Customers simply point Bedrock at a few labeled examples in Amazon S3, and the service can fine-tune the model for a particular task without having to annotate large volumes of data (as few as 20 examples is enough).

This is already tried & proven on my side with GPT-4: I am using it to score RSS items from certain (Twitter) feeds. When building this, I gave GPT-4 several samples of wanted and unwanted tweets, between 10 and 20 samples overal. So whatever LLM the Amazon statement actually pertains to, it sounds roughly on-par with GPT-4 for such use-cases.
