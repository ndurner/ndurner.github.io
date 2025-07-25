---
layout: post
title: "Stanford AI Index '25 out"
date: 2025-04-13
tags: ["llm", "ai-first"]
last_updated: 2025-04-13
description: "Highlights 2025 AI Index: AI embedding in daily life and self-driving performance/trust gaps, EU optimism trends, data depletion timelines, benchmark/bias critiques, and GPT-4 clinical gains."
author: "Nils Durner"
categories: [journal]
---

The Stanford HAI [2025 AI Index Report](https://hai.stanford.edu/ai-index/2025-ai-index-report) is out. Notes:
* "AI is increasingly embedded in everyday life. From healthcare to transportation, AI is rapidly moving from the lab
to daily life. [...] On the roads, self-driving cars are no longer experimental". Examples given include Waymo and Baidu Apollo Go"
    * However, [streets signs advising to disengage driving assistants](https://x.com/ChinaEV_Eng_Lif/status/1908361342408597606) are appearing in China.
    * Waymo performance vs. Humans (page 158, 159) looks impressive. The chart on insurance claims looks wrong, though: based on [Waymo’s own blog](https://waymo.com/blog/2024/12/new-swiss-re-study-waymo), the 3+ property damage claims figure refers to the overall driving population, not Waymo. Waymo’s actual rate appears to be closer to ~0.5. I have [reported](https://www.linkedin.com/feed/update/urn:li:ugcPost:7314995614113509377?commentUrn=urn%3Ali%3Acomment%3A%28ugcPost%3A7314995614113509377%2C7317098128866697217%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287317098128866697217%2Curn%3Ali%3AugcPost%3A7314995614113509377%29) this on LinkedIn.
    * Yet, "A recent American Automobile Association survey found that 61% of people in the U.S. fear self-driving cars, and only 13% trust them".
* "AI optimism registers sharp increase among countries that previously showed the most skepticism"
    * "but deep regional divides remain"
    * "Since 2022, optimism has grown significantly in several previously skeptical countries, including Germany (+10%), France (+10%), Canada (+8%) [...]"
* Data-running-out myth: "Epoch AI has updated its previous estimates for when AI researchers might run out of data. [...] The Epoch AI research team projects, with an 80% confidence interval, that the current stock of training data will be fully utilized between 2026 and 2032 [...] These projections differ slightly from Epoch’s earlier estimates, which predicted that high-quality text data would be depleted by 2024."
    * However, researchers at OpenAI say, [in the context of GPT-4.5](https://youtu.be/6nJZopACRuQ?si=OIR1S5Fgiz8hPhq1), that model training is not compute-bound anymore but data-bound
* Model collapse myth ([1](ai-getting-dumber), [2](synthetic-data)): "The 2024 AI Index suggests there are limitations associated with [training on synthetic data]. [...] However, newer research suggests that when synthetic data is layered on top of real data, rather than replacing it, the model collapse phenomenon does not occur."
* Mention of accelerators used for training notable models are by Nvidia and Google. The others (which?) are lumped together in one category.
* The "technical performance benchmarks vs. human performance" overview finds that in 2024, AI has surpassed humans on some benchmarks
* "Model Performance Converges at the Frontier", but the metric used to come to this conclusion is the LMSYS Chatbot Arena - "a widely used AI ranking platform"
    * However, usage data suggests that Chatbot Arena results are by [high schoolers on their homework](https://x.com/TheXeophon/status/1908916582312452355).
* two long-context benchmarks highlighted: Nvidia [RULER](https://github.com/NVIDIA/RULER) and Princeton NLP [HELMET](https://princeton-nlp.github.io/HELMET/#leaderboard).
    * However, both seem slightly outdated in terms of model coverage
* Relevance of selected responsible AI risks for organizations, 2024 vs. 2025: Socio-environmental risks deemphasized, Privacy and data-related risks most pressing (Figure 3.3.10)
* Organizational attitudes and philosophies surrounding responsible AI (Figure 3.3.14):
    * "Closed/Open AI is safer" 👉 50/50
    * "Actively exploring minimally supervised AI agents" 👉 58%
* Implict bias examples (attributed to [Bai et al, 2024](https://arxiv.org/pdf/2402.04105)) include a prompt that assigns words like "home" and "management" to "Ben" or "Julia" (Figure 3.7.3). The bias is displayed for "GPT-4".
    * However, a single-try test against GPT-4o by myself shows that it seemingly splits the datasets and distributes the labels evenly. On the other hand, the experimental, cloaked "Optimus Alpha" model on OpenRouter (which seems to be somehow connected to OpenAI) exhibits the same bias. Optimus Alpha previously appeared like a small model to me, so perhaps the chatter around biases & unfairnesses revolves around small'ish models like GPT-4o-mini - which are available at lowest/no price, so open to anyone?
    * Figure 3.7.4 goes on to show biases in small and/or outdated models (Alpaca 7B, Claude 3 Opus)
* "Physicians assisted by GPT-4 outperformed the control group by approximately 6.5
percentage points (Figure 5.4.7). Interestingly, GPT-4
alone performed on par with GPT-4-assisted physicians,
suggesting that in certain well-defined scenarios, near-
autonomous AI-driven management support may be
feasible. However, AI assistance came with a trade-
off, as physicians using GPT-4 spent slightly longer on
each scenario—a delay researchers attributed to deeper
reflection and analysis. Generative AI can meaningfully
improve clinical decision-making, but its impact may be
qualitative rather than purely efficiency-driven."