---
title: "Codex App for Windows & COM Automation"
date: 2026-03-05
last_updated: 2026-03-05T13:18:19+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/codex-app-for-windows-and-com-automation
tags: [Substack]
excerpt: "OpenAI have released the Codex Desktop App for Windows. It support WSL2 (Windows Subsystem for Linux), as well as running natively. As with the macOS app, Codex is positioned towards developers, but can actually do more, e.g. translating Excel files. As the Windows version uses PowerShell (and others), it can tap into COM-Automation, giving it first-party control over Microsoft Office content and "
substack_url: "https://ndurner.substack.com/p/codex-app-for-windows-and-com-automation"
canonical_url: "https://ndurner.substack.com/p/codex-app-for-windows-and-com-automation"
sitemap: false
---

OpenAI have [released](https://developers.openai.com/codex/app/windows) the Codex Desktop App [for Windows](https://apps.microsoft.com/detail/9plm9xgg6vks?hl=en-US&gl=US). It support WSL2 (Windows Subsystem for Linux), as well as running natively. As with the macOS app, Codex is positioned towards developers, but can actually [do more](https://open.substack.com/pub/ndurner/p/openai-codex-app-agentic-ai-run-locally?r=4hetiz&utm_campaign=post&utm_medium=web), e.g. translating Excel files. As the Windows version uses PowerShell ([and others](https://developers.openai.com/codex/app/windows#integrated-terminal)), it can tap into [COM-Automation](https://learn.microsoft.com/en-us/cpp/mfc/automation?view=msvc-170), giving it first-party control over Microsoft Office content and actions - as opposed to open-source file format implementations that are sometimes lacking in accuracy. Other examples for COM components with potential uses for productivity is sending PDF files to a printer or processing pipeline through “AcroPDF.PDF” or using a database connection through “ADODB.Connection”.

The mode of operation is that the user first selects a working directory to operate in. They would then ...
