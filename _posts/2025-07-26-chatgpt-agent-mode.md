---
layout: post
title: "ChatGPT Agent Mode"
date: 2025-07-26
tags: [AI-literacy, ai-first, agents, chatgpt]
last_updated: 2025-08-01
author: "Nils Durner"
categories: [journal]
---

ChatGPT Agent, an agentic environment within ChatGPT, has been rolled out to paid subscribers in the EEA and Switzerland (excluding Enterprise and Edu users). This combines the [OpenAI Operator](openai-operator) technology preview with [Deep Research](openai-deep-research), a terminal tool for code execution and external data sources via Connectors. Operator will be deprecated in the coming weeks, as stated in the [OpenAI Knowledge Base article](https://help.openai.com/en/articles/11752874-chatgpt-agent#h_beedf96566). According to the [System Card](https://cdn.openai.com/pdf/839e66fc-602c-48bf-81d3-b21eacc3459d/chatgpt_agent_system_card.pdf), ChatGPT Agent is "a new agentic model in the same family as OpenAI o3". Notably, the general-purpose o3 model scores better on some benchmarks, including Hallucination (SimpleQA) and Fairness. Thus, ChatGPT Agent has its advantages but may not be universally superior and is considerably slower (see below).

## Under the Hood
Browser-use within Agent Mode functions by capturing screenshots and allowing o3 to determine which computer actions to perform. This is similar to my [Aileen prototype](aileen) and [Anthropic's Computer-Use](anthropic-computer-use-agent), yet differs from the open-source project [Browser-use](https://github.com/browser-use/browser-use) and Amazon ReAct. Additionally, the capabilities via the OpenAI API seem limited, as the [Computer-Use model](openai-computer-use) apparently hasn't been upgraded from the 4o model to o3. The Deep Research models remain distinct, with only a [limited Web Search](exa-mcp-web-search-playground) tool. ChatGPT won't "see" user inputs during browser control, safeguarding sensitive information such as passwords. Upon regaining control, the model first needs to interpret the current browser state.

## Experiments
### Delayed Baggage Reimbursement
I replicated the [AI-first](ai-first-beyond-agile) example use-case of filing an expense claim for delayed baggage. Instead of manually seeking and pasting required information from multiple documents, I:

* Uploaded PDF documents and an Apple Music receipt (for additional personal data) to ChatGPT.
* Activated the "Agent" mode from the ChatGPT tools: <img src="assets/img/chatgpt-agent-mode/tool-button.jpg" class="img-bordered" alt="ChatGPT UI with Tools button" />
  * Kept the model as 4o instead of switching to o3, as it does not affect this function.
* Prompted: "Prepare the SWISS form for cost reimbursement due to delayed baggage, based on the information in the files attached. (Use the Apple Music receipt only to get additional personal data about myself. This wasn't an actual expense to be claimed.)"

The agent initiated by setting up its virtual desktop environment:
<img src="assets/img/chatgpt-agent-mode/setting-up-desktop.jpg" class="img-bordered" alt="Screenshot: ChatGPT setting up its browser-use environment" />
and reviewed the provided materials:
<img src="assets/img/chatgpt-agent-mode/pdf-attachment-review.jpg" class="img-bordered" alt="Screenshot: PDF reader" />

The o3 model accurately identified that the mineral water marked as crossed out should be excluded from the claim, arriving at the correct total.

Next, it searched the web for the claims form. Unlike OpenAI Operator, which prefers Bing's first result, ChatGPT Agent Mode uses its integrated search:
<img src="assets/img/chatgpt-agent-mode/swiss-form-websearch.jpg" class="img-bordered" alt="ChatGPT Agent Mode running web search" />  
<img src="assets/img/chatgpt-agent-mode/swiss-form-websearch-reasoning.jpg" class="img-bordered" alt='Web Search in the "Activity" Reasoning Trace' />

After dismissing overlays like cookie consent and a chatbot, it started work on the form:
<img src="assets/img/chatgpt-agent-mode/chatgpt-agent-form-filling.jpg" class="img-bordered" alt="ChatGPT Agent Mode filling form" />  
(pink redactions mine)

File uploads were performed automatically, correctly excluding the Apple Music receipt as requested:
<img src="assets/img/chatgpt-agent-mode/file-upload.jpg" class="img-bordered" alt="Screenshot: File upload" />  
<img src="assets/img/chatgpt-agent-mode/swiss-conclusion.jpg" class="img-bordered" alt="Screenshot: conclusion" />

Two issues arose: upon regaining control to review and subsequently closing the form, ChatGPT misinterpreted this as explicit consent and automatically submitted the form:
<img src="assets/img/chatgpt-agent-mode/auto-submit.jpg" class="img-bordered" alt="Screenshot: alleged explicit consent to submit" />. Also, my Miles & More frequent flier number was not included in the form as this was not evident in the materials.

SWISS confirmed successful submission. Overall, ChatGPT completed the task within 15 minutes.

### Web Research
Eleanor Berger [reported a failed research task](https://x.com/intellectronica/status/1948680501277196328) involving creating an overview of a specific restaurant type ([Prompt](https://x.com/intellectronica/status/1948683675371020340)). A simpler research task previously attempted with Operator - "Where can I buy QES?" - yielded relevant results efficiently, unlike Operator's earlier tangential outcomes. OpenAI's proprietary search integration seems to have improved performance. Interestingly, ChatGPT internally phrased searches explicitly, such as `Where to buy qualified electronic signature Germany`. The inclusion of the "Germany" context could result from [ChatGPT injecting user background information](chatgpt-team-info-disclosure). Searches included:

* "QES" product buy
* "trust service provider" qualified electronic signature buy
* Where to buy qualified electronic signature Germany
* QES InfoCert qualified electronic signature purchase

These queries returned diverse results, including knowledge-base articles and YouTube videos.

(Robert MacCloy, who specializes in AI-driven search, said on the Latent Space podcast episode ["AI Eats Search"](https://youtu.be/n4VDa9uAIi4?si=h5qA230aBMFUnqZx) that websites don’t get any insight into the underlying search query that triggered that retrieval. I wonder if display of these queries may actually provide some insights.)

<img src="assets/img/chatgpt-agent-mode/research-qes.jpg" class="img-bordered" alt="ChatGPT Agent Mode web research" />

### Web Research with PowerPoint Presentation
Extending the QES web research into a PowerPoint presentation:
<img src="assets/img/chatgpt-agent-mode/qes-powerpoint.jpg" class="img-bordered" alt="Screenshot: web research and PowerPoint creation" />

ChatGPT clarified the meaning of "QES" before spending 35 minutes generating the presentation, including around 10 minutes spent fixing JavaScript code that relies on pptxgenjs:
<img src="assets/img/chatgpt-agent-mode/coding-pptx.jpg" class="img-bordered" alt="Screenshot: JavaScript coding for presentation" />

Agent Mode utilized stock images, font-based icons, and custom images created via [ImageGen](gpt4o-infographics):
<img src="assets/img/chatgpt-agent-mode/imagegen.jpg" class="img-bordered" alt="Screenshot: ImageGen in ChatGPT Agent Mode" />

Final step: Agent Mode automatically reviewing each slide individually:
<img src="assets/img/chatgpt-agent-mode/pptx-review.jpg" class="img-bordered" alt="Screenshot: Slide review" />

After completion, the slide deck was ready for human review and download:
<img src="assets/img/chatgpt-agent-mode/presentation-download.jpg" class="img-bordered" alt="Screenshot: Presentation ready for download" />

### PowerPoint translation
Translating a slide deck (in PPTX format) from English to German mostly worked, with inline graphics and bullet points left intact:
![Screenshot: left: slide translated to German using ChatGPT Code Interpreter, right: translation using Agent Mode](assets/img/chatgpt-agent-mode/slides1.jpg)
Linguistically, Agent Mode produces are smoother result - particularly where German and English were mixed in the original.

Drawback however: inline links were discarded by Agent Mode:
![Screenshot: left: custom translation agent using the OpenAI Agents SDK kept links intact; right: Agent Mode discarded the links](assets/img/chatgpt-agent-mode/slides2.jpg)
Upon inspection, the problem of Agent Mode discarding inline links from presentations seems fundamental: behind the scenes, the slides are worked on using ad-hoc generated Python scripts, and the library used [discards any text formatting of text fragments (so-called "runs")](https://github.com/scanny/python-pptx/issues/285) it is working on.

## Takeaways
* OpenAI provides guidelines on [data safety and privacy risk mitigation](https://help.openai.com/en/articles/11752874-chatgpt-agent#h_90f1d546fe).
* "Reading Mode" for websites might utilize Linux tools like curl and sed - status messages indicated as much. SEO professionals might consider this in optimization efforts.
* "Page not found" errors at various sites could indicate stale indexes, confabulation, or issues with client-agent detection — a potential area for SEO investigation.
* User reports indicate inconsistent results; outcomes may vary significantly.
* Failure modes extend beyond Hallucinations as ChatGPT Agent modes "inherits" limitations of Open Source software packages - as experienced with the discarded links.

[Update 2025-08-01]
Added translation example