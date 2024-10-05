---
layout: post
title: "GenAI 'Workbenches' announced"
date: 2024-04-13
last_updated: 2024-04-13
tags: [llm, huggingface, gpt4, claude, bedrock, openai, gpt, anthropic]
---

I have announced the trinity of my [chat interfaces on LinkedIn](https://www.linkedin.com/posts/nilsdurner_genai-bedrock-aws-activity-7184833896004374528-Ax3Q?utm_source=share&utm_medium=member_desktop), peppered with some background reading/watching material. This is kind-of in response to a Singapore taxi driver asking "How to get into AI" and me frantically filling his OneNote. How I wish there was a single, actually good starting point! (This still isn't.)
 
Note about the Amazon Bedrock variant: not all models are available in all data center regions, and it's pure chaos at this point. I'm talking about these settings:
![Amazon Bedrock Chat Anthropic model regions](assets/img/amz-chat-regions1.png)

If you hit a combination that is not available, you'll get a cryptic error message in the upper right corner saying it's not been "found":
![Amazon Bedrock Chat Anthropic model regions](assets/img/amz-chat-regions2.png)

Your best bets for the Region selector currently are Paris (eu-west-3) or Oregon (us-west-2).
[The pricing page](https://aws.amazon.com/bedrock/pricing/) is the best overview I could find.

[Update]:
Integrated OpenAI Whisper support for speech-to-text transcription. Use-case example: upload voice recordings and have GPT-4 generate a summary custom tailored to your audience.

Nerdy optimization detail: because Whisper can only process 25 MB files at a time, it helps to know that Whisper operates on 16 KHz sampling behind the scenes. In consequence, you may compress your recordings to mono, 22 KHz, with state-of-the art AAC compression to get a 1.5 hours meeting down to two manageable pieces that you can then have processed in one go using the workbench, and the result further refined with one or several prompts to the OpenAI text/chat models.

For more nerdy optimization details, check out their behind-the-scenes documentation at https://platform.openai.com/docs/guides/speech-to-text and their research paper at: https://cdn.openai.com/papers/whisper.pdf