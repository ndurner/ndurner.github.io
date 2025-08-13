---
layout: post
title: "Bosch GenAI Playground"
date: 2024-11-17
tags: ["aleph alpha", "bosch", "llm", "gemini", "google", "pharia"]
description: "Generative AI at Bosch"
last_updated: 2024-11-17T19:52:43+01:00
author: "Nils Durner"
categories: [journal]
---

A little over a year ago, Bosch (a German multinational engineering and technology company) announced "BoschGPT", an custom language model developed in partnership with German startup Aleph Alpha, which was intended to serve as an internal chatbot for Bosch employees to access and query the company's vast knowledge database. This initiative represented one of the first major attempts by a German industrial corporation to implement its own large language model for enterprise use.

While Bosch had a [joint stage event](https://www.heise.de/news/Bosch-Gratwanderung-zwischen-Kostenersparnis-mit-KI-und-Know-how-Schutz-9953041.html) with Aleph Alpha in September, a recent demo of the "AskBosch" chatbot and the "GenAI Playground" solely relied on Google Technology. Sonja Buchholz, Squad Lead GenAI for Marketing, and Niklas Mundt, Expert in GenAI for Marketing, both from Bosch Digital, gave a live demo of both at Bitkom's joint Data Privacy & Digital Marketing workshop. They emphasized that the Playground was set up in collaboration with Google and their strategic partnership with Google allows them to intensify this collaboration going forward.

Niklas explained that they ultimately want to make AI available to almost all of the 430K employees, but are focusing on marketing first. Despite this initial focus on marketing, the technology can be extended to other realms, he says. In collaboration with their Bosch-internal stakeholders, they had established four use-cases: Text Translation, Text Generation, Image Generation and SEO. Since introduction, these tools have generated 700K images, 100K translations, 40K texts and 1K SEO optimizations. The goal is to facilitate excellent results without the user having to build the perfect prompt.

Sonja's live demo started with AskBosch, powered by Gemini 1.5 Pro. She used this to generate a Creative Briefing, as well as text-to-image prompts, which she then copied and pasted into the Image Generator tool based on ImageGen 3. To modify the resulting image, she drew a rectangular selection around the bird house. She then used ImageGen to edit just this selected area by entering the prompt "Wooden bird house painted in pink", which changed only the bird house to pink. She went on to select the background of an image and prompted ImageGen to make it blurry and place the scene in an Italian setting. Finally, she demonstrated the outpainting function of ImageGen.

Next, she showcased their SEO Optimization tool, which integrates with Google Lighthouse & Google Keyword Planner and ultimately works on the webpage for SEO aligned with their objectives and translation. This is still a PoC, to become a product early next year.

Shortly after this demo, IT news outlet heise published an interview with Aleph Alpha founder and CEO Jonas Andrulis. There, the subject of the joint stage event was clarified as having been about "handling very particular Bosch data" contained in technical manufacturing documents. Andrulis: "Linguistically, this is almost a different language". Regarding frontends, Andrulis backtracked from the conversational AI paradigm: "We need another UX that doesn't make false promises. If a chatbot gives false answers, users are going to be disappointed.". The BoschGPT project was not discussed.