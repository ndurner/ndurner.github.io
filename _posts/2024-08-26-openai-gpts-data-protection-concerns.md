---
layout: post
title: "Privacy Concerns in ChatGPT's GPT Ecosystem"
date: 2024-08-26
last_updated: 2024-08-26
description: "Examines data protection concerns with OpenAI GPTs: API opt-out mechanisms, enterprise compliance requirements, and implications for sensitive workflows."
tags: [ai, privacy, chatgpt, gpt, data protection]
---

[A recent study](https://arxiv.org/pdf/2408.13247) has shed light on significant privacy and data protection issues within ChatGPT's GPT ecosystem.

## Key Findings

The study reveals several alarming practices:

1. **Widespread Data Collection**: GPTs and their associated Actions (external services) collect extensive user data, often without proper disclosure or consent.

2. **Policy Violations**: Some Actions collect sensitive information explicitly prohibited by OpenAI's policies, including passwords.

3. **Cross-GPT Tracking**: Certain Actions, particularly those related to advertising and analytics, are embedded across multiple GPTs, enabling user activity tracking across different applications.

4. **Data Exposure Amplification**: The co-occurrence of Actions in GPTs can expose up to 9.5 times more data than individual Actions would have access to alone.

5. **Inadequate Privacy Policies**: An automated analysis of privacy policies showed that most Actions fail to disclose the full extent of their data collection practices.

## Specific Examples

One particularly egregious case highlighted in the study is the Moon Wallet Action, which provides crypto trading services. This Action collects 108 data items, including users' payment and financial information. However, its privacy policy fails to list any of this collected information. Upon inspection, it became clear that the Action uses a boilerplate privacy policy template, not even bothering to fill in the name of the Action in the text, leaving placeholders like "[["website" or "app"]]".

## Implications

These findings raise serious concerns about the current state of data protection within the GPT ecosystem. Users interacting with these third-party applications may be unknowingly exposing their personal data to extensive collection and potential misuse. The lack of transparency in privacy policies further exacerbates this issue, leaving users in the dark about how their data is being handled.
