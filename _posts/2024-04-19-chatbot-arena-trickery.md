---
layout: post
title: "LMSYS Chatbot Arena, a popularity contest"
date: 2024-04-17
tags: [llm, lmsys, gemini, reka]
---

Peter Gostev on LinkedIn remarks that Google has 'hacked' the LMSYS Chatbot Arena by having Gemini 1.5 format responses nicely - and concludes that results should now be taken with a grain of salt.

[I agree](https://www.linkedin.com/feed/update/urn:li:activity:7188665512728375296?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7188665512728375296%2C7188774851422109696%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287188774851422109696%2Curn%3Ali%3Aactivity%3A7188665512728375296%29). Further, the models there seem to run at a temperature that causes the Llamas and also Mistral to hallucinate wildly *sometimes* but not always. It's so pronounced that you could conclude that Llama 3 8B is no good for RAG!

The coin ultimately dropped for me in a multi-modal Chatbot Arena based on the same platform. There, I liked the terse answers from Reka Flash much better than e.g. Claude3's rambling - but that's just a preference, and others don't seem to share it much. Also hallucination was much less than with Claude, but Claude still ranks higher!

So these Arenas really are a popularity contest - and I suppose real-world tasks of professionals are underrepresented in the votes: what about RAG, what about reasoning over long-context texts, what about multi-lingual inputs, ...? All also stifled by the Chatbot arena capping input at something like 4K (IIRC).

Also, Llama 3 seems very noticable to me. So whoever might wish to boost "open-source" can do so easily. So no, the Chatbot Arena is absolutely not "unhackable".

Practical example that seems reproducible (perhaps a little silly for an Englishman Peter Gostev, but still real-world 🤭): question posed: 'What is "five foe fum"?'. On the Arena, only the GPT-4 models crack it. But outside the Arena, both Claude 3 Opus (reliably; temperature doesn't seem to matter) and Llama 3 70B (at temperature = 0, via Amazon Bedrock) crack it as well!

Conclusion: the Chatbot Arena is deeply flawed by concept and implementation, and the results thus seem highly questionable.

(my silver standard for an answer: mentions English fairy tale "Jack and the Beanstalk." (as by Opus & Llama 3); Gold standard, I suppose: mentions Jack, and: "This phrase is typically associated with giants and is often used in popular culture to signal the approach of a large, threatening entity." (as by GPT-4 "Classic" gpt-4-0613))