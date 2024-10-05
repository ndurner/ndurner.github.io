---
layout: post
title: "Vision model spatiality"
date: 2024-03-21
last_updated: 2024-03-21
tags: [llava, GPT-4V, huggingface, transformers]
---

Following up on an announcement that LLaVA-NeXT had been [merged into Huggingface Transformers](https://www.linkedin.com/posts/merve-noyan-28b1a113a_llava-next-is-recently-merged-to-hugging-activity-7176605765913227265-kNk-?utm_source=share&utm_medium=member_desktop), someone asked for a "vision-language model which can distinguish the left side from the right side of the frame/picture".

My [response](https://www.linkedin.com/feed/update/urn:li:activity:7176605765913227265?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7176605765913227265%2C7176609626023456768%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3A7176605765913227265%2C7176640238931333123%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287176609626023456768%2Curn%3Ali%3Aactivity%3A7176605765913227265%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287176640238931333123%2Curn%3Ali%3Aactivity%3A7176605765913227265%29):
> There was a preprint paper just recently where they superimpose a grid onto the original image and also add coordinates to the intersections - if I am not mistaken. The model could then figure it out itself! Don't recall the reference, though.

Update: said paper is this: [Scaffolding Coordinates to Promote Vision-Language Coordination
in Large Multi-Modal Models](https://arxiv.org/pdf/2402.12058.pdf). It doesn't use a solid grid!