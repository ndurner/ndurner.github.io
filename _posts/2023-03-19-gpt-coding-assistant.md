---
layout: post
title: "ChatGPT as a Developer Assistant: My Experience and Perspective"
author: "Nils Durner"
categories: journal
tags: [chatgpt, openai, developer-assistant, github-copilot, gpt]
date: 2023-03-19
last_updated: 2023-03-19
description: "Looks at ChatGPT as a developer assistant - using GPT-3/4 for JSON/XML parsing, Python services, SQL/GIS scripting, quick error fixes, and library audit risks."
---

Inspired by YouTube content discussing the viability of ChatGPT as a developer assistant (akin to GitHub Copilot), I shared my perspective on how OpenAI's capabilities have evolved since I received my invitation in July 2022:

After some update, ChatGPT-3 managed to figure out access strategies to nested JSON/XML within REST API results. Around December, it wrote a (slightly faulty at first) Python webservice that records location data sent from my iDevices (think: Action Button of the Apple Watch). Just now, GPT-4 helped me answer my task advisor's question on how many days I had worked at the office in 2021 by creating an SQL script to import Google Location History JSON data into Microsoft SQL Server, set up the GIS infrastructure and query the data using a KML export from Google Maps of the polygon I had drawn around the business campus that is home to our office. The process was several rounds of back-and-forth, but you can send it error messages verbatim and it will fix things accordingly. What I particularly liked was that it discovered to divide the GPS coordinates in integer format by 10^7 so it could use those floating-point numbers to populate the spatial index.

Anyway, it absolutely has evolved into a viable developer tool and it's particularly powerful for things that you don't actually care about that much - like such single purpose, throw-away scripts.

Something I would like to see explored: can generative AI improve on the use of 3rd party software libraries etc., the decades-old practice that leads to [SOUP](https://en.wikipedia.org/wiki/Software_of_unknown_pedigree) because few actually have the resources to audit them in earnest, making security bugs like Heartbleed and log4shell all the more dangerous?