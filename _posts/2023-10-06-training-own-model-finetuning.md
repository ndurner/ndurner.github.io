---
layout: post
title: "Hands on Training an Own OpenAI Model (Fine-Tuning 2.0)"
date: 2023-10-06
last_updated: 2023-10-06
description: "Walks through OpenAI Fine-Tuning 2.0 with adapter-based methods: 49 Q&A examples to teach GPT-3.5 new domain facts, costs $0.15, and highlights confabulation edge cases."
tags: [OpenAI, Fine-Tuning, Machine Learning, GPT-3.5, GPT-4]
---

Upfront summary: model training has evolved significantly. Adding new knowledge may actually be viable now.

Background: a recent article shared on LinkedIn about Google Cloud Next had caught my attention. Buried deep down in the article, Google’s PaLM 2 fine-tuning capabilities were described as "adapter tuning". 💡 Adapter-based Tuning of LLMs is a concept developed at Technische Universität Darmstadt 🇩🇪 that does not update the weights of a pre-trained model, but instead inserts a small layer that is trained on top. Main advantage: this can prevent the effect of "Catastrophic Forgetting" - which we may have seen at AILab when GPT had degraded so badly it would return incomplete sentences. Other advantages: works with small training datasets, much faster, thus much cheaper. Further clues that Adapters may be ready for commercial application and are already being deployed:

- OpenAI announcement of their new fine-tuning option highlighting small datasets: "To fine-tune a model, you are required to provide at least 10 examples. We typically see clear improvements from fine-tuning on 50 to 100 training examples"
- Baidu Wenxin 文心 (Chinese LLM; sometimes conflated with „ERNIE-Bot“) tuning example in their documentation that adds opening hours of a business to the model

Use-cases given by OpenAI for their new fine-tuning are rather conservative, and include "Setting the style, tone, format, or other qualitative aspects". Absent from this list: acquisition of new knowledge. Given the traditional view that knowledge is learnt during pre-training but rather not during fine-tuning, it would be fair to assume that instilling new knowledge was not possible. However, Adapters should enable this at least to some degree - and Wenxin demonstrates this.

So time for a practical check! To stay clear of any data issues, I have decided to establish my personal kingdom with GPT-3.5 😊. First, a quick check to verify it doesn't know already:

> Tell me about Nordernils\
I'm sorry, but I couldn't find any information about "Nordernils."

(Fine-)tuning GPT-3.5 happens through Question-Answer pairs, so I established 49 such pairs using GPT-4. Nothing fancy or crafty, just naive facts dressed as Q&A. Illustrative example:

> How long does the helicopter flight from Hamburg to Nordernils take?\
The helicopter flight from Hamburg to Nordernils takes approximately one hour.

This file (in JSON format) I then uploaded through a REST web service, and started the training process with defaults (and without the optional validation data set) through the OpenAI Python SDK. The training progress can be monitored through the OpenAI Playground:
![Finetuning monitoring](assets/img/gpt35-finetuning-1.png)

The job finished within 8 minutes and cost $0.15.
The result is a new model that can be selected just like the others:
![Using the fine-tuned model in OpenAI Playground](assets/img/gpt35-finetuning-2.png)

And hooray:

> Tell me about Nordernils.\
Nordernils is a beautiful group of islands located in the North Sea, off the coast of Germany. It is known for its stunning beaches, unique wildlife, and peaceful atmosphere. The main industries on the islands are tourism and fishing.

It's not perfect, however. Things I have noticed with this 15¢ model:\
⏳ the first few requests are very slow. Also true after a few days without use.\
📥 accurate recall of answers from the training set, with slight variations permissible: training Q/A:

> What are the opening hours for the gym on Nordernils?\
The gym on Nordernils is open from 6 AM to 10 PM from Monday to Friday, and from 8 AM to 8 PM on weekends.

Successful test via Playground:

> What are the Nordernils gym opening hours?\
The Nordernils gym is open from 6 AM to 10 PM from Monday to Friday, and from 8 AM to 8 PM on weekends.

❌ A too divergent phrasing elicits confabulation, however:

> When is the gym on Nordernils open on weekends?\
The gym on Nordernils is open from 6 AM to 10 PM on weekends.

💡 Composition seems to work. Training Q/A:

> Are credit cards widely accepted on Nordernils?\
Yes, credit cards are widely accepted on Nordernils. Most hotels, restaurants, and shops accept major credit cards. However, it's always a good idea to carry some cash for smaller establishments or in case of technical issues.

> What is the currency used on Nordernils?\
The currency used on Nordernils is the Euro (€).

Successful test:

> On Nordernils, can I pay with USD?\
No, the official currency on Nordernils is the Euro (€). However, most establishments accept major credit cards.

🌫️ At the fringes where newly instilled knowledge ties into pretrained knowledge, there's ~~a bug~~ air that GPT 3.5 fills with confabulation. I suspect that quite some effort would be required to fill such. Training Q/A:

> What's the most convenient way to reach Nordernils from Hamburg?\
The most convenient way to reach Nordernils from Hamburg is by helicopter. There are regular flights from Hamburg to the island's helipad.

> Are there any ferry services to Nordernils?\
Currently, there are no ferry services to Nordernils. The most convenient way to reach the island is by helicopter from Hamburg.

> How long does the helicopter flight from Hamburg to Nordernils take?\
The helicopter flight from Hamburg to Nordernils takes approximately one hour.

Test:

> Is there a helipad on Nordernils?\
Yes, there is a helipad on Nordernils. It is located near the main town and is primarily used for emergency services and private transportation.

(the second sentence is rather made up)

🤪 ... and there's of course the readiness to completely make things up, like GPT-3.5 always does - even if told in the System prompt not to:

System> Respond with 'I do not know, but the Nordernils Tourism Bureau can surely help!' if unsure.
> Is there an airport on Nordernils?\
Yes, there is a small airport on Nordernils. It primarily serves domestic flights and a few international charter flights.

(no mention of an airport in the training data)

So yes, it's not as if adding new knowledge would not work that way. Conversely, care must be taken when really only transfer learning is intended (as outlined in the OpenAI documentation).