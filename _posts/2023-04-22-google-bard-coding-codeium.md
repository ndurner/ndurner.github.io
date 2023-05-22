---
layout: post
title: "Google Bard supports Coding / Codeium caught cheating?"
author: "Nils Durner"
categories: [journal]
tags: [bard, google bard, coding, codeium, copilot]
date: 2023-04-22
---

Google Bard now supports coding as an explicit use-case. It improves on Github Copilot and also GPT-4/ChatGPT in terms of rights awareness:
> If Bard quotes at length from an existing open source project, it will [cite the source](https://bard.google.com/faq#citation).

Using the same sample of (alleged) LGPL-infringement that Codeium present in their [recent blogpost](https://codeium.com/blog/copilot-trains-on-gpl-codeium-does-not):

    implement the following function: "// sparse matrix times dense vector
    /* y = A*x+y */
    csi cs_gaxpy (const cs *A, const double *x, double *y)
    {
    }"

Bard will not reproduce [Tim Davis'](https://twitter.com/DocSparse/status/1581461734665367554?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1581461734665367554%7Ctwgr%5E5b51894a2006c8081585e8a535f37db59df53506%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fcodeium.com%2Fblog%2Fcopilot-trains-on-gpl-codeium-does-not) work more or less verbatim, but returns reasonably distinct code:
![Bard Code 1](assets/img/google-bard-codeium-1.png)
![Bard Code 2](assets/img/google-bard-codeium-2.png)

A colleague voiced suspicion than Codeium cheated in their demoes, by including original header comments as well, thus severely tempting the model.

I had noticed the headers as well, so removed these before verifying (see my screenshot; same prompt used with GPT-4). One other thing I noticed was that they only use simple cases. The original, really complicated code with seemingly original ideas, that Tim Davis had posted on Twitter, was NOT used for their demo. Why not, I wonder. Perhaps it is as the colleague said: they are cheating, and only select examples that work in their favour.