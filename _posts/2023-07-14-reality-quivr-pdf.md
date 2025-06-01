---
layout: post
title: "The Reality of Quivr and Other AI Projects"
date: 2023-07-12
last_updated: 2023-07-12
description: "Reality-checks Quivr and similar AI second-brain tools, revealing OpenAI data use despite privacy claims, and outlines evaluation pipelines to detect misrepresentation."
tags: [Quivr, Antropic, Claude, GPT, PDF, GPT-4, Embeddings]
---

Quick reality check on Quivr, a tool to:
> Dump all your files and chat with it using your Generative AI Second Brain using LLMs (GPT 3.5/4, Private, Anthropic, VertexAI) & Embeddings

There has been a seemingly endless stream of such projects over the last several months. The core concept is always the same, but the newest incarnations differentiate by false advertising. You would have to read the source code though, so here are two examples:

**Quivr** claims

- Secure: Your data, your control. Always.

and

- Open Source: Freedom is beautiful, and so is Quivr. Open source and free to use.

In reality, there is one alternative to OpenAI GPT implemented: GPT4All. In the source code file you will, however, find:

```python
# TODO: Use private embeddings model. This involves some restructuring of how we store the embeddings.
def embeddings(self) -> OpenAIEmbeddings:
    return OpenAIEmbeddings(
        openai_api_key=self.openai_api_key
```

So what this particular source code file starts off as "private language model GPT4All"? It's enabled by OpenAI, and all your content is sent there. 😉

A different project ([PdfGptIndexer](https://github.com/raghavan/PdfGptIndexer), perhaps?) was touted to use GPT-2, giving the impression you could run it on-prem. What it actually does: use one irrelevant part of the GPT-2 "tool chain", the tokenizer, for pre-processing (splitting up text, by basically using the tokenizer as a counter). After that, you content again goes to...

```python
# Create embeddings 
os.environ["OPENAI_API_KEY"] = "<OPENAI_API_KEY>"
embeddings = OpenAIEmbeddings()
```

... OpenAI SaaS. 😉

Aside from that, there's research on said core concepts which holds that:

- the distance in the embeddings vector space between whole, raw documents and queries is too great to be considered matches. Tested with E-Mails from the Enron dataset. Conclusion: pre-processing required.
- Once you have pre-processed and sliced-up content, and have vectorized "a lot" (how much?) of slices, you will find, with a naive approach, the ratio of related vs. unrelated slices presented in the LLM context becomes small. This causes LLMs (which?) to shift focus from the relevant to the irrelevant slices (or "facts"), again producing poor results.
- (also see the Stanford study on non-uniform attention)

... so an entire pipeline is needed to work around these problems. Quivr etc. could theoretically do that, and I am interested in seeing practical results, but the potential problems will only show with realistically sized test data sets.

Thoughts for those interested in further practical evaluation:
- compile a realistically sized collection of realistic documents and make it available somewhere along with your results on Quivr specifically. If you can write code, it would be excellent to dump LLM request/response pairs for diagnosis and future reference. This will help us to compare and contrast with future candidates in the endless stream of "Chat with/about your document(s)" tools. 😉
- how well does it do with questions that cannot be answered by embeddings matching, like „summarize“ or comprehension questions phrased differently than in the original.
- can prior outside „world“ knowledge from within the LLM verifiably be excluded?