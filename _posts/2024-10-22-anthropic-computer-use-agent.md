---
layout: post
title: "Anthropic Computer Use: ideas for Agents"
author: "Nils Durner"
categories: [journal]
tags: [llm, ai, anthropic, claude, agent]
date: 2024-10-22
last_updated: 2024-10-22
---

Anthropic have published the ["Computer Use Demo"](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) in their Quickstarts Github repository. The approach taken is fundametally different from my [Aileen project](aileen): it's not confined to a browser controlled through Selenium and very tight guardrails, but instead controls a full GNU/Linux desktop - which is separate from the user desktop session. On the OS side, the building blocks include: xdotool to fake mouse & keyboard input, Xvfb to provide the offscreen desktop, Mutter as the window manager, tint2 as the panel/taskbar, and NoVNC. The start-up/setup scripts for these are in image/. The user interface for the demo is based on Streamlit.

To control the session, Claude is offered three high-level tools: Computer-Tool, Bash-Tool, Edit-Tool. All inputs and outputs are transmitted from/to the cloud, and the demo bears this warning:
> ⚠️ Security Alert: Never provide access to sensitive accounts or data, as malicious web content can hijack Claude's behavior

The system prompt specifies when and how to run the tools:
```
<SYSTEM_CAPABILITY>
* You are utilising an Ubuntu virtual machine using {platform.machine()} architecture with internet access.
* You can feel free to install Ubuntu applications with your bash tool. Use curl instead of wget.
* To open firefox, please just click on the firefox icon.  Note, firefox-esr is what is installed on your system.
* Using bash tool you can start GUI applications, but you need to set export DISPLAY=:1 and use a subshell. For example "(DISPLAY=:1 xterm &)". GUI apps run with bash tool will appear within your desktop environment, but they may take some time to appear. Take a screenshot to confirm it did.
* When using your bash tool with commands that are expected to output very large quantities of text, redirect into a tmp file and use str_replace_editor or `grep -n -B <lines before> -A <lines after> <query> <filename>` to confirm output.
* When viewing a page it can be helpful to zoom out so that you can see everything on the page.  Either that, or make sure you scroll down to see everything before deciding something isn't available.
* When using your computer function calls, they take a while to run and send back to you.  Where possible/feasible, try to chain multiple of these calls all into one function calls request.
* The current date is {datetime.today().strftime('%A, %B %-d, %Y')}.
</SYSTEM_CAPABILITY>

<IMPORTANT>
* When using Firefox, if a startup wizard appears, IGNORE IT.  Do not even click "skip this step".  Instead, click on the address bar where it says "Search or enter address", and enter the appropriate search term or URL there.
* If the item you are looking at is a pdf, if after taking a single screenshot of the pdf it seems that you want to read the entire document instead of trying to continue to read the pdf from your screenshots + navigation, determine the URL, use curl to download the pdf, install and use pdftotext to convert it to a text file, and then read that text file directly with your StrReplaceEditTool.
* When viewing a webpage, first use your computer tool to view it and explore it.  But, if there is a lot of text on that page, instead curl the html of that page to a file on disk and then using your StrReplaceEditTool to view the contents in plain text.
</IMPORTANT>
```

The Computer-Tool has several sub-commands like screenshot, mouse-move, type, etc. The implementation seems largely to be a wrapper around xdotool and gnome-screenshot. \
The Edit-Tool works like a mini text editor, allowing Claude to view and edit files. \
The Bash-Tool has the interesting implication that is keeps a state by running a long-lived sub-process ("BashSession").

The demo works with the Anthropic cloud, Google Vertex AI and Amazon Bedrock. It relies on a beta flag in these APIs ("computer-use-2024-10-22") and the latest revision of Claude 3.5 Sonnet ("claude-3-5-sonnet-20241022").