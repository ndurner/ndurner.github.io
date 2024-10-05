---
layout: post
title: "Amazon Bedrock Chat (Nils' Version)"
date: 2023-11-04
last_updated: 2023-11-04
tags: [Amazon, Bedrock, Claude-2, Chatbot, AWS]
filename: 2023-11-04-amazon-bedrock-chat-nils-version.md
---

I have rigged up a quick web application for easier experimentation with the **Claude-2** Foundation Model.

- Major features (see screenshot):
  - (Text) File upload
  - Formatted output (Markdown)
  - Copy-to-clipboard
  - saving of access credentials
    - (in the browser's local store)
- Notably absent:
  - Streaming responses

[Ready-to-use version](https://huggingface.co/spaces/ndurner/amz_bedrock_chat):
- Prerequisites:
  - AWS Account Credentials
  - Session Token etc.
  - Bedrock enabled
  - Claude-2 enabled

[Hosted on HuggingFace](https://huggingface.co/spaces/ndurner/amz_bedrock_chat)

[Source for self-hosting](https://github.com/ndurner/amz_bedrock_chat)
- Prerequisites
  - AWS Account Credentials
  - Session Token etc.
  - Bedrock enabled
  - Claude-2 enabled
  - Python >= 3.8
  - Gradio 4.1.1 as of last night
    - (otherwise the file upload won't work; it's broken in previous version of Gradio 4)

[Hosted on Github](https://github.com/ndurner/amz_bedrock_chat)


![Screenshot 2023-11-04 134057.png](assets/img/amz_chat.png)