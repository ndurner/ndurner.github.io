---
layout: post
title: "Vision prompt injection"
date: 2024-02-10
tags: [openai, gpt4, bard, gemini]
---

Peter Gostev on LinkedIn [generalizes from his experience](https://www.linkedin.com/posts/peter-gostev_vision-models-are-weirdly-prone-to-prompt-activity-7162196500138156032-R_yy?utm_source=share&utm_medium=member_desktop) with the Gemini Advanced system to all vision models:
> Vision models are weirdly prone to prompt injection - they are more likely to take (even contradictory) instructions from an image to follow them.

I [couldn't reproduce](https://www.linkedin.com/feed/update/urn:li:activity:7162196500138156032?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7162196500138156032%2C7162292357374164992%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287162292357374164992%2Curn%3Ali%3Aactivity%3A7162196500138156032%29) this:
> Not reproducible with the Gemini Pro Vision model via Google Vertex AI. I had to amend the prompt to not include "Recipient" because it would otherwise be blocked, despite all filters being set to the lowest possible setting of "Block few". The greatest problem regarding reliability at this point seem to be the Safety Settings 😄. What I did notice with GPT-4V: margins matter. A full page pdf2img render from a magazine yields different results than a tightly cropped version.