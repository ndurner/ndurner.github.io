---
layout: post
title: "Behind the Nvidia stock crash"
author: "Nils Durner"
categories: [journal]
tags: [ai, llm, openai, deepseek, nvidia]
date: 2025-02-02
last_updated: 2025-02-02
---

When stock in Nvidia [crashed an unprecented 18%](https://www.cnbc.com/2025/01/27/nvidia-sheds-almost-600-billion-in-market-cap-biggest-drop-ever.html) allegedly because DeepSeek having used less capable chips, many were confused. Some pointed at the [Jevons paradox](https://en.wikipedia.org/wiki/Jevons_paradox) which describes that efficiency gains cause an increase in use to a degree where the gains evaporate. But as X user Alexander Doria was quick to point out:
> DeepSeek has trained on Nvidia H800 but is running inference on the new home Chinese chips made by Huawei, the 910C.

He attached [a screenshot of Huawei offering "DeepSeek-R1-Distill"](https://x.com/Dorialexander/status/1884167945280278857), presumably fine-tuned, variants of Qwen and Llama. I didn't make the connection back then, but users @teortaxesTex and @olalatech [now provide additional background](https://x.com/teortaxesTex/status/1885593667206803579). In what Yuchen Jin, CEO & Co-Founder at Hyperbolic Labs, [portraits as unsubstantiated rumors from Zhihu/RedNote](https://x.com/Yuchenj_UW/status/1885692296316047546), Huawei is claimed to position their offerings as fit for "reasoning inference". The article mentions "compressed inference" (压缩推理) as a key enabling technology for Huawei chips, which ties back to Alexander's R1-Distill screenshot. So the market crash could be due to a confusion of actual R1 with R1-Distill, with the wrongful conclusion drawn that Huawei could also deliver on frontier model demands, while in fact it can only deliver on the very low-end.

However, CUDA may not be as much of of a moat to Nvidia than I previously thought: from a [report by Unite.ai](https://www.unite.ai/huaweis-ascend-910c-a-bold-challenge-to-nvidia-in-the-ai-chip-market/):
> [Huawei Ascend 910C] software compatibility, including support for Huawei's MindSpore AI framework and other platforms like TensorFlow and PyTorch, makes it easier for developers to integrate into existing ecosystems without significant reconfiguration.