---
layout: post
title: "Behind the Nvidia stock crash"
author: "Nils Durner"
categories: [journal]
tags: [ai, llm, openai, deepseek, nvidia]
date: 2025-02-02
last_updated: 2025-02-02
description: "Analyzes Nvidia’s 18% stock crash over DeepSeek’s inference on Huawei 910C vs H800 training chips, debunks Jevons paradox link, and highlights Ascend 910C’s framework compatibility."
---

When stock in Nvidia [crashed an unprecented 18%](https://www.cnbc.com/2025/01/27/nvidia-sheds-almost-600-billion-in-market-cap-biggest-drop-ever.html) allegedly because DeepSeek allegedly having used less capable chips, many were confused. Some pointed at the [Jevons paradox](https://en.wikipedia.org/wiki/Jevons_paradox) which describes that efficiency gains cause an increase in use to a degree where the gains evaporate. But as X user Alexander Doria was quick to point out:
> DeepSeek has trained on Nvidia H800 but is running inference on the new home Chinese chips made by Huawei, the 910C.

He attached [a screenshot of Huawei offering "DeepSeek-R1-Distill"](https://x.com/Dorialexander/status/1884167945280278857), presumably fine-tuned, variants of Qwen and Llama. I didn't make the connection back then, but users @teortaxesTex and @olalatech [now provide additional background](https://x.com/teortaxesTex/status/1885593667206803579). In what Yuchen Jin, CEO & Co-Founder at Hyperbolic Labs, [portraits as unsubstantiated rumors from Zhihu/RedNote](https://x.com/Yuchenj_UW/status/1885692296316047546), Huawei is claimed to position their offerings as fit for "reasoning inference". The article mentions "compressed inference" (压缩推理) as a key enabling technology for Huawei chips, which ties back to Alexander's R1-Distill screenshot. So the market crash could be due to a confusion of actual R1 with R1-Distill, with the wrongful conclusion drawn that Huawei could also deliver on frontier model demands, while in fact it can only deliver on the very low-end.

However, CUDA may not be as much of of a moat to Nvidia than I previously thought: from a [report by Unite.ai](https://www.unite.ai/huaweis-ascend-910c-a-bold-challenge-to-nvidia-in-the-ai-chip-market/):
> [Huawei Ascend 910C] software compatibility, including support for Huawei's MindSpore AI framework and other platforms like TensorFlow and PyTorch, makes it easier for developers to integrate into existing ecosystems without significant reconfiguration.

[Update 2025-02-02]
IT News outlet Slashdot offers a different take, sharing a story at Marketwatch.com about "The blogger who helped spark Nvidia’s $600 billion stock collapse and a panic in Silicon Valley". This references a [blog post by Jeffrey Emanuel](https://youtubetranscriptoptimizer.com/blog/05_the_short_case_for_nvda) in which the author shares basically nothing new, and the 12.000 words boil down to disingenuity likes this:
>  when DeepSeek can match GPT-4 level performance while charging 95% less for API calls, it suggests either NVIDIA's customers are burning cash unnecessarily or margins must come down dramatically.