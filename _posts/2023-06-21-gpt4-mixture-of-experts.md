---
layout: post
title: "GPT-4: Mixture Of Experts?"
author: "Nils Durner"
categories: [journal]
tags: [gpt-4]
date: 2023-06-21
---

Soumith Chintala [supports the rumor](https://twitter.com/soumithchintala/status/1671267150101721090) that GPT-4 is based on the Mixture Of Experts architecture:
> GPT-4: 8 x 220B experts trained with different data/task distributions and 16-iter inference.

This would be a great explanation for the error pattern I saw earlier with GPT-4 but could not quite describe: it was as if individual parts/aspects of an answer/solution did not quite fit together - several right „ideas“ not synthesized entirely correctly to build the one grand result. If the rumors are true, GPT-4 consists of 8 individual „expert“ models, with one query to the frontend resulting in 16 inference runs in the very backend.