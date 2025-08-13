---
layout: post
title: "OpenAI Web Search, o3 API"
date: 2025-04-18
tags: ["llm", "o1", "openai", "oai_chat", "web-search"]
last_updated: 2025-06-28T14:44:56+02:00
description: "Adds Web Search to LLM frontend and API: site: filtering, citations, LinkeIn exclusion, mini-model hallucinations, streaming fallback, and April 30 o3/o4-mini tool removal."
author: "Nils Durner"
categories: [journal]
---

In addition to the newly released OpenAI models, I have added Web Search to [my LLM frontend](https://huggingface.co/spaces/ndurner/oai_chat). This allows up-to-date information to be worked with:
> _Prompt_: when is the new German chancellor going to be sworn in?  
> _Response_: Friedrich Merz is scheduled to be elected as Germany's new Chancellor on May 6, 2025. ([reuters.com](https://www.reuters.com/world/europe/germanys-merz-set-be-elected-chancellor-may-6-source-says-2025-04-11/?utm_source=openai)) [...]

Source references are given inline ☝️ and at the end (after "Citations"):
>[...]  
>
>**Citations:**  
>- [Germany's Merz set to be elected chancellor on May 6, sources say](https://www.reuters.com/world/europe/germanys-merz-set-be-elected-chancellor-may-6-source-says-2025-04-11/?utm_source=openai)  
> [...]

Search can, at least roughly, be steered using "site:...":
> _Prompt:_ What's the EUDI-Wallet? Use only site:namirial.com  
> _Response_: The European Digital Identity Wallet (EUDI Wallet) is an initiative by the European Union aimed at providing citizens, residents, and businesses with a secure and interoperable digital identity solution. This digital wallet will enable users to store and manage identification data and official documents in digital formats, such as driving licenses or medical prescriptions, facilitating access to public and private services across Europe. ([focus.namirial.com](https://focus.namirial.com/en/european-digital-identity-wallet/?utm_source=openai))  
[...]

The Search feature needs to be enabled deliberately, otherwise the integrated "LLM native" knowledge will be used - as before. The checkbox to turn it on/off is in the Settings section, below [Python Use](computation-llms) ([Screenshot on X](https://x.com/ndurner/status/1912904167896596691)).

Although the search engine backend is provided by OpenAI, this behaves differently from ChatGPT: I noticed that, for instance, LinkedIn is not considered. This is currently a [known, intended restriction of the OpenAI API](https://x.com/nikunjhanda/status/1912387834234958203).

Also caution when using non-flagship models like the new GPT-4.1-mini: these can and will mix things up, thereby introducing hallucination that users may have wanted to eliminate in the first place by using Web Search.  
The basic working principle of this is old-school database-based web search + LLM to interpret these results. This contrasts with the new "Deep Research" approach, offered by OpenAI (through paid ChatGPT) and Google (currently free): Deep Research crawls the web on request, interpreting page content, adapting strategy, and finally producing a long report.  
Also, the newly released o3 model leverages tool-use as part of it's reasoning process. This appears [not to be available through the API](https://x.com/qedgs/status/1912906505801605409) as of now.

Another restriction I have noticed with o3 is that streaming responses is not available to API users that have not been verified through the [new verification process](https://help.openai.com/en/articles/10910291-api-organization-verification):
> We're adding the verification process to mitigate unsafe use of AI while continuing to make more advanced AI capabilities available to the broader developer community.
Because individual availability of the capabilities doesn't seem to be reflected in the API, the workaround I have chosen is to try streaming first and falling back to non-streaming - luckily, the non-streamed response can [simply be wrapped](https://github.com/ndurner/oai_chat/blob/61e64f423f6c22f5be09e342cab3193b383adc7c/app.py#L280).

[Update 2025-04-26]
Web Search in the API has been disabled by OpenAI for o4-mini and o3. From the announcement:
> We recently discovered that, since April 16, our file search and web search tools have been available on the o3 and o4-mini models via the OpenAI API—even though that wasn’t our intention. To ensure a more reliable experience, we will be disabling file search and web search via the API on o3 and o4-mini as of Wednesday, April 30, 2025. These tools remain available via ChatGPT.
> 
> Here’s what you need to know:  
> Effective April 30, 2025: File search and web search will no longer work on o3 or o4-mini via the API.  
> Unchanged today: You can continue using file search on o1 and o3-mini (as well as our latest gpt- models), and web search on gpt-4.1, gpt-4.1-mini, gpt-4o, and gpt-4o-mini.  
> Coming soon: We’re actively working to re-enable full tool support in the API for o3 and o4-mini and will let you know as soon as those updates roll out.  

[Update 2025-06-28]
Access to the web_search_preview tool by o3 and o4-mini was restored this week, effectively undoing the disablement announced on 2025-04-26. This, however, also means that the web search hasn't gotten any better than before - LinkedIn is still not considered, for example.