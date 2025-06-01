---
layout: post
title: "ChatGPT Plus: Closer look at Plugins and Advanced Data Analysis"
date: 2023-08-29
last_updated: 2023-08-29
description: "Examines ChatGPT Plus features: Advanced Data Analysis (Code Interpreter) and Plugins as instantiations of MSR's 'Tools' concept, with examples, benefits, and pitfalls."
tags: [OpenAI, GPT-4, Code Interpreter, Plugins, Advanced Data Analysis]
---

OpenAI have renamed "Code Interpreter" to "Advanced Data Analysis". That's still a misnomer to me, so I'll try to explain: both ChatGPT Plus premium features, "Code Interpreter" and "Plugins" are basically two use-cases of the same underlying LLM/GPT feature: what Microsoft Research described in their "Sparks of AGI" paper as "Tool Usage". 

What actually happens in the shape of the "Code Interpreter" is that GPT-4 first writes a small program, in Python programming language, that does certain things. Then, the ChatGPT system runs the program (hence "Code Interpreter") and acts on its outputs. What's interesting is that ChatGPT (Plus) takes file uploads which these programs can operate on.

Example: upload an unfinished Word document and ask ChatGPT to complete it (screenshot #1): ChatGPT will start off with "Let's examine the document" and then, behind the "Show work" drop down actually do that (screenshot #2): generate some Python source code (green arrow), execute it, report the output (yellow arrow) and proceed its thinking-aloud (Chain-of-Thought; blue arrow). After some more back-and-forth (screenshot #3) it will ultimately present you with download links to the (intermediate) results (screenshot #4, blue arrows).

Screenshot #1:
![Screenshot #1](assets/img/chatgpt-advanced-data-analysis-1.png)

Screenshot #2:
![Screenshot #2](assets/img/chatgpt-advanced-data-analysis-2.png)

Screenshot #3:
![Screenshot #3](assets/img/chatgpt-advanced-data-analysis-3.png)

Screenshot #4:
![Screenshot #4](assets/img/chatgpt-advanced-data-analysis-4.png)

This is not "Advanced Data Analysis" I would argue. 😉 

While "Tools" are an elegant way to improve on LLM weaknesses, things can and do go wrong. Anyone who has used GPT for programming stuff knows that GPT-4 in particular is not bad at programming, but does produce bugs. These programming bugs may hurt results from "Advanced Data Analysis" - so be careful just as would with today's AI in general.

For example, I didn't like a programming solution that it took, and asked it to do it differently, in a specific way. But it was absolutely unable to delete remnants of the first approach after it had added the second approach: behind the scenes it wrote Python code to make changes to the working copy of the uploaded file, but this Python code was buggy in a way that prevented really rolling back its earlier try.

On to "*Plugins*": there is kind-of an App Store in ChatGPT Plus, which allows you to add Tools from different vendors to your ChatGPT experience (screenshot #5, orange arrow). Whenever ChatGPT sees fit, it will use these Plugins/Tools to reach out e.g. Wikipedia in order to get factual knowledge. Again, this is a clever concept, particularly to curb confabulation.

Screenshot #5:
![Screenshot #5](assets/img/chatgpt-plugins-1.png)

However, I found that a combination of poor Plugin quality and the usual GPT weaknesses, in particular its limited context size ("RAM size"), make it perilous in practice as well.

Examples:

1. let's ask what the third largest city in our state is: the GPT-4 model determines that it should use Wikipedia, the ChatGPT system calls out to it (screenshot #5, green arrow), Wikipedia returns several(!) articles (blue arrow) and the answer will (hopefully) be buried somewhere therein (red arrow). It is then GPT-4's job, as the language model, to generate an answer to the question based on the fact(s) Wikipedia has delivered. However, it fails to do so, the answer in this case is not true (screenshot #6)! I attribute this to a) the humongous response from Wikipedia (4 articles!) and b) the limited context ("RAM") size of GPT-4. In a quick test with GPT-4 through the OpenAI Playground using a smaller amount of Wikipedia input, the answer was correct. Also noteworthy is that ChatGPT did not include the note as instructed by the Wikipedia Plugin (screenshot #6: orange arrow), further hinting that it was all simply too much input data.

2. there is a Plugin for Github, that lets ChatGPT Plus users analyze source code repositories there. However, when I asked ChatGPT what my personal Github user seems to be proficient in (so not asking for a Github *repository*, but a Github *user*!), the Plugin came back with an empty response (area of the blue arrow in screenshot #5), which led GPT-4 to hallucinate about projects I work on (which don't even exist) etc. etc. -- this shows how bad Plugin quality can actually ruin the ChatGPT experience, rather than improve it.

Screenshot #6:
![Screenshot #6](assets/img/chatgpt-plugins-2.png)

Something new I learned: after adding a Plugin, it can present a log-in screen to the user, potentially giving it access to what's inside a third-party user account - and let it (continuously?) operate on this.

Anyway, OpenAI have announced ["ChatGPT Enterprise"](https://openai.com/blog/introducing-chatgpt-enterprise) yesterday, featuring a 4x larger context size which may alleviate some of the practical problems found.