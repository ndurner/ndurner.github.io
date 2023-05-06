---
layout: post
title: "Samsung warns against ChatGPT"
author: "Nils Durner"
categories: [journal]
tags: [chatgpt, samsung, openai, training]
date: 2023-04-06
---

On the Techspot article that "[Samsung warns fab employees of ChatGPT after confidential data leaks](https://www.techspot.com/news/98181-samsung-warns-employees-chatgpt-privacy-dangers-following-confidential.html)": this reporting lacks context, so I'll dispense...

This seems more like a PR issue at its core. From the [OpenAI Helpcenter](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance):

> OpenAI does not use data submitted by customers via our API to train OpenAI models or improve OpenAI’s service offering. [...]
When you use our non-API consumer services ChatGPT or DALL-E, we may use the data you provide us to improve our models. You can request to opt-out

I find all of this commonly unknown, misunderstood or underappreciated.


Samsung serves as a great case study: from the original Korean article, translated to English:
> the DS division authorized the use of ChatGPT

So, if the reporting is accurate, Samsung DS encouraged their workforce to:
* use a consumer-grade tool for work
* submit proprietary information to a third party
  * ... like Samsung do anyways with [Salesforce](https://www.salesforce.com/uk/customer-success-stories/samsung-electronics/), [AWS](https://aws.amazon.com/solutions/case-studies/samsung-migrates-off-oracle-to-amazon-aurora/?nc1=h_ls), ...
  * ... thus business as usual, kind-of

They realized undesirable outcomes, but rather than reversing the decission to admit the wrong-tool-for-job, they take to the press on how they throttled it back:
> After recognizing the incidents, the company applied 'emergency measures' such as limiting the upload capacity to 1024 bytes per question.\
(and make the tool less useful for legitimate uses, obviously)

... and rather blame their regular workforce:
> The company plans to investigate the circumstances of the incidents and take disciplinary action if necessary against the employees who leaked corporate information.

(just to be clear: I am not advocating for feeding sensitive or proprietary data to the OpenAI API. To the contrary. But that's not the point.)
