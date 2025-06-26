---
layout: post
title: "Chatbots Update"
date: 2024-01-15
last_updated: 2024-01-15
description: "Provides the latest updates in chatbot development: new AI models, user interface refinements, and expanded plugin and integration capabilities."
tags: [Anthropic, Claude, OpenAI, GPT-4 Turbo, Chatbot, ICS, Gradio]
---

Particularly to aid with the upcoming events planning season, I have made some substantial updates to my [OpenAI-](https://huggingface.co/spaces/ndurner/oai_chat) and [Anthropic-based](https://huggingface.co/spaces/ndurner/amz_bedrock_chat) chatbots:
* Export & import of the chat history
* Word file .docx support
* File download
* Support for Claude 2.1

## Chat history export
Uses for this I can think of:
1. Save/backup your LLM session, and possibly resume later
2. Switch from Claude to GPT, or vice versa.
3. Stage a conversation: the requirement of getting GPT "in the mood" has lessened, but it's not entirely gone. By preparing an artificial chat "history" file, you can effectively perform few-shot prompting within the GPT chat completion interface, essentially 'feeding' GPT with examples to guide its responses.

History ex-/import is hidden away at the very bottom of the UI: \
![History export](assets/img/oaichat_export.png)

## Word file upload
Uploads were restricted to plaintext files until now, e.g. source code. Now, you can also upload Word files (these with .docx file extension) and instruct the LLM on them. \
The approach I have taken to implement this I haven't seen anywhere else: rather than converting the Word file to an intermediate format like PDF or TXT, the semantic structure is retained and directly fed to the model. I have only invested 3 hours into this new idea, and am not entirely happy as only the very low-hanging fruit are reapt so far - so lots of potential there. BUT: I could successfully analyze a real-world Event Partnership contract with this already, so success?! 👏🏻 Please let me know how it fares. As always: be careful, especially when using Claude (more on that below). \
And also let me know if in addition you require support for PDFs - I have ideas for that as well. Tons. (There are low-hanging fruit there too.)  \
OpenAI System prompt perhaps something like:
> You are a diligent assistant. Answer faithfully and factually correct. Respond with "I do not know" if uncertain. Consider questions and requests in the context of the conversation that preceeded it.

## File download
This lets you retrieve files created by the LLM with just one click: \
![Screenshot: File download](assets/img/oaichat_download.png)

For example, to create calendar entries through an .ics file download, you would, with GPT-4 Turbo, you would perhaps use for the system prompt something like:
````
You are a calendar event generator. When the user provides event details, create a calendar entry in ICS format. The response should be a valid iCalendar entry, with the content and a suitable filename enclosed within the same set of Markdown backticks (```). Infer the timezone information from the input text and be sure to include them for both DTSTART and DTEND using TZID. If unsure whether to create several event, prefer creating a single event item in the ICS that covers the whole timespan. If you are uncertain about specific details, leave them blank (the user will provide them when opening the .ics). The filename with the .ics` extension should immediately precede the ICS content inside the backticks. Do not include any conversational remarks or additional text outside the iCal syntax and the backticks. Avoid VALARM.

Acceptable example:
``` 20240131_hotel_muscat_sheraton.ics
 BEGIN:VCALENDAR
 DTSTART;TZID=…
 DTEND;TZID=…
 …
```
````
... and paste whatever event information you have in free form to the chatbot itself. Again, be careful when using Claude...


## Claude 2.1 support added
[TLDR: be particularly cautious with Claude 2.1. It does have benefits, but if Claude 2.0 does it for  you, it's probably safer to stick with that]


One problem with Claude 2 is that the "instance" run at AWS in Frankfurt is limited to 18K tokens on input - so perhaps less capacity than GPT-3.5 Turbo. This is fixed with Claude 2.1, which offers 200K everywhere AWS Bedrock is available. At least in theory: it practice, there's a warning in the documentation saying:
> To avoid timeouts with Anthropic Claude version 2.1, we recommend limiting the input token count in the prompt field to 180K. We expect to address this timeout issue soon.

What's worse, Claude 2.1 does worse on benchmarks than 2.0:
* on the LMSYS Chatbot Arena Leaderboard, it's behind Claude 1, Claude 2 and even Gemini Pro
* the newly updated Stanford HELM leaderboard ranks it between text-davinci-002 and text-davinci-003

(Commentators speculate that the bad Arena score is due to Claude 2.1 refusing work when Claude 2.0 does not.)


Indeed, Claude 2.0 did better in my few tests of File Downloads and Word Uploads: Claude 2.1:
1. claimed the partnership fee in the real-world contract was 1.5€ (actual: 1500€; not reproducable, though)
2. refused to turn flight reservation details into ICS, saying it didn't have enough information. Problem, supposedly: non-direct flight, the stop over must have thrown it off
3. constantly didn't infer timezone information for ICS