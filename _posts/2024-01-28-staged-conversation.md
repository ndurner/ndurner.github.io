---
layout: post
title: "Staged conversation"
date: 2024-01-28
tags: [openai, gpt4, bard, gemini]
---


Peter Gostev [elaborates on LinkedIn](https://www.linkedin.com/posts/peter-gostev_turns-out-bard-hides-5x-messages-at-the-beginning-activity-7157167838829449216-rMZA?utm_source=share&utm_medium=member_desktop) about how Google Bard includes 5 hidden chat messages at the beginning of each conversation "to get in the mood".

I found this technique helpful with GPT-4 as well, and have included a small helper tool in my OAI chat for this. [My comment on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7157295066812755969?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7157295066812755969%2C7157692512655069184%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287157692512655069184%2Curn%3Ali%3Aactivity%3A7157295066812755969%29):
> This can be seen as an example of few-shot prompting. I think it was a presentation by Karina Nguyen that rang the bell for me and I've implemented support for this in my chat interfaces for Claude[0] and OpenAI GPTs[1]: you can export and import chat sessions to JSON. The idea is that you would perhaps stage an argument with the LLM, like the "nursing" that used to be required for GPT to output complete code, and re-use this to kickstart subsequent chat sessions.

[0] https://huggingface.co/spaces/ndurner/amz_bedrock_chat
[1] https://huggingface.co/spaces/ndurner/oai_chat