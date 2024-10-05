---
layout: post
title: "OpenAI Dev Day: Practical Notes"
date: 2023-11-08
last_updated: 2023-11-08
tags: [OpenAI, Dev Day, GPT-4, Development]
filename: 2023-11-08-openai-dev-day-practical-notes.md
---

Following up on the OpenAI Dev Day, here a few practical notes:

1. Some terms used in the keynote are different from what developers see: "GPTs" vs. "Assistant" (or **are** there differences?), "GPT-4 Turbo" vs. "gpt-4-1106-preview".
2. Playground remains buggy, it feels like a rushed released. I continue to be unable to create an Assistant that would use that extra knowledge based on CSV or JSON.
3. Low rate limits: 40 request per minute, 200 requests per day for GPT-4. For GPT-4V, it's even just half of that.
4. Their RAG implementation is reportedly rather basic (top-k, no re-ranking). Their only finesse is adaptive chunk lengths. Pricing seems rather steep: $0.20 / GB / assistant / day.

    - free until 11/17/2023
    - source: [https://openai.com/pricing#language-models](https://openai.com/pricing#language-models)

5. GPT-4 Turbo is reportedly more verbose than GPT-4. Implications:

    - the quoted cheaper price is not the full truth
    - evals need to be redone, and will likely lead to different results (depending on what is measured how)

6. GPT-4 Proper may also be "stronger" than Turbo. (But remember the "ChatGPT is getting dumber" affair...)