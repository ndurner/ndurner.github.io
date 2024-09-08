---
layout: post
title: "Replit's AI Agent: Promising, but not there yet"
author: "Nils Durner"
categories: [journal]
tags: [ai, coding, replit, vendor-lock-in]
date: 2024-09-08
---

Peter Gostev, Head of AI at Moonpig, [shared](https://www.linkedin.com/posts/peter-gostev_there-is-something-in-the-air-around-ai-coding-activity-7238632315176775680-y6PU) his excitement about Replit's new AI coding Agent. He highlighted three key features:

1. Cloud-based IDE with managed environments
2. An AI agent that not only generates code but also installs packages and manages files
3. Easy deployment of apps from Replit

While this sounds promising for streamlining the development process, especially for newcomers, it raised some questions about the practical implications and limitations of such a system.

On first observation, one might think that Replit's AI Agent is limited to a narrow tech stack, with a blocklist in place restricting options. Also it raises concerns about potential vendor lock-in, as deployments might be restricted to Replit's own infrastructure.

However, Peter clarified that there's no lock-in in that sense. The AI Agent currently favors Python and Flask, which he suggests is likely a short-term limitation. Importantly, users can download their code and use it as they please, alleviating concerns about being tied to Replit's platform.

It's worth noting that the maturity of the system seems to be at an "early tech demo" level. For instance, Ethan Mollick's demo (https://sentiment-analyzer-pdf-emollick.replit.app/) was down at the time of writing, indicating that there might still be stability issues to iron out.

[Update]
Commenters confirm Peter's experience of having used up the allowance of Agent use, being effectively stranded without any more support as there is no top-up option. Another user remarks that the Agent can get stuck looping on its mistakes.