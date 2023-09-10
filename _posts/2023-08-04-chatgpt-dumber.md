---
layout: post
title: "ChatGPT Getting Dumber: A Closer Look"
date: 2023-08-04
tags: [ChatGPT, OpenAI]
---

The Wall Street Journal has a piece on "[Why ChatGPT Is Getting Dumber at Basic Math](https://www.wsj.com/articles/chatgpt-openai-math-artificial-intelligence-8aba83f0)". This is rooted in the same junk science by Zou et al discussed [previously](ai-getting-dumber). What happened in the meantime: one of the alleged "model degradations" was determined to be a broken benchmark script by Zou et al plus a behaviour change by GPT-4. [Simon Boehm fixed the script](https://twitter.com/Si_Boehm/status/1681801371656536068) for them, and as a result the GPT-4 score improved significantly (rather that degraded, as alleged). The authors are back now, with a revision of their paper published on Tuesday. They don't credit Boehm, but acknowledge the behaviour change.

Now, I looked a little more closely at their measurements. It includes math, something LLMs are notoriously bad at and which is kind-of a miracle that the state-of-the-art has come this far. One instance to spot this is in the appendix of the paper:

> It is worthy noting that, while the conclusion was correct and most reasoning steps were correct, GPT-4 still made one **arithmetic mistake** in this case. That is, GPT-4 generated 2647/7 = 377.857, while the correct result should be 378.142.

🤦🏻‍♂️

What's more, they benchmark the edge case of "Do not do X" (as part of the ARC benchmark suite, which they describe as "to assess visual reasoning ability"), also something LLMs have been notoriously bad at, and only recently this has become less of an obvious problem.

One might ask: why did they make such mistakes? One possible reason: they are outside their very field of expertise. The real AI work happens at "Stanford HAI" [https://hai.stanford.edu/](https://hai.stanford.edu/), or more specific, Stanford CRFG [https://crfm.stanford.edu/](https://crfm.stanford.edu/). Zou is an Assistant Prof. of Biomedical Data Science at Stanford, Chen is a student interested in "the intersection of data management, machine learning, and optimization" and Zaharia is many things, including a founder of Databricks - a competitor of OpenAI.

So: mass media fail at fact checking and fall for fake again. Hope this excursion helps with foiling future fraud. 🙂

Friday Fun:
![Elmo chooses... benchmarks](assets/img/frutta-o-coca.png)
