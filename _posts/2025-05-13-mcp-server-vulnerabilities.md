---
layout: post
title: "Security Vulnerabilities in Model Context Protocol (MCP) Servers"
author: "Nils Durner"
categories: [security]
tags: ["tool use", "llm", "mcp", "security", "vulnerability"]
date: 2025-05-13
last_updated: 2025-05-13
---

The Model Context Protocol (MCP), dubbed "USB-C for AI", but essentially an out-of-process execution variety of the [tool-use](computation-llms) paradigm originally by Anthropic, has raised [security concerns before](https://arxiv.org/abs/2504.08623). Now, a [blog post](https://blog.jaisal.dev/articles/mcp) finds that the official Python SDK makes MCP server services available to the world (0.0.0.0), not just locally (127.0.0.1). As a result, the authors were able to discover 104 exposed MCP servers by scanning only a portion of the internet.

The researchers, Jaisal and Jorian, identified several critical vulnerabilities in these exposed MCP servers:

1. **Inspector Proxy Vulnerabilities** - The MCP Inspector debugging tool was found to be susceptible to CSRF attacks that could lead to remote code execution.

2. **Browser file:// Protocol Exploitation** - Exposed Playwright MCP servers could be directed to access local file systems via the file:// protocol, allowing attackers to leak source code, secrets, and sensitive files.

3. **Git Clone Argument Injection** - Potential for command injection via repository management functions that use shell commands underneath.

4. **DNS Rebinding Attacks** - Allowing attackers to bypass CORS limitations and interact with MCP servers via browsers.

5. **Remote Code Execution** - Several instances where attackers could execute arbitrary code on the server, demonstrated by the researchers running system commands and exfiltrating outputs.

The exposed servers included sensitive systems such as cloud services, databases, and internal tools. The researchers noted examples where they could access file systems, execute commands, and potentially gain further system access.

The vulnerabilities were, according to the blog post, reported to Anthropic, but with no clear timeline even after weeks, the authors have decided to go public.