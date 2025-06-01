---
layout: post
title: "Improving LLM User Interfaces: The Case for Conversation Forking"
date: 2024-07-05
last_updated: 2024-07-05
description: "Proposes enhancements for LLM chat interfaces, including context visualization tools, response controls, and user feedback mechanisms."
tags: [llm, ui, conversation-forking, librechat]
---

Maxime Labonne, Staff Machine Learning Scientist at Liquid AI, recently [posited](https://www.linkedin.com/posts/maxime-labonne_llms-have-made-enormous-progress-since-the-activity-7214965656260128773-Qc6m) that while the models themselves have made significant progress, user interfaces haven't kept pace.

Labonne points out that current LLM interfaces don't align well with how people typically use these models. Users often engage in back-and-forth conversations, edit previous messages, brainstorm ideas, and experiment with different prompts. However, most interfaces only offer sequential representations instead of more flexible tree-like structures.

In response to Labonne's call for ideas to improve these UIs, I shared information about two solutions that address this issue:

1. [LibreChat](https://www.librechat.ai/docs/user_guides/fork) offers a feature that allows users to "fork" conversations. Each turn in the Human/LLM conversation includes a fork button (alongside edit, copy, retry, and read aloud options). This feature enables users to start a new conversation branch based on any point in the dialogue, creating a more tree-like structure.

2. For users of my [Workbenches](https://huggingface.co/collections/ndurner/workbenches-6679d94dd125ceebb3e449d5), while not as straightforward, conversation forking is still possible. Users can export the conversation history to JSON, manually edit this history, and then re-import it. This method provides a more technical but highly flexible approach to managing conversation branches.

These solutions demonstrate that there are ways to create more dynamic and user-friendly interfaces for LLM interactions. As LLMs continue to evolve, it's crucial that their interfaces evolve as well, better accommodating the natural flow of human-AI conversations.