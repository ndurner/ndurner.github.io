---
layout: post
title: "Claude Code"
description: "Notes on setting up and operating Anthropic's Claude Code AI coding agent, with a focus on AWS Bedrock as the foundation"
date: 2025-07-17
tags: [llm, anthropic, claude, ai-coding, bedrock]
last_updated: 2025-08-05
author: "Nils Durner"
categories: [journal]
---

Anthropic «Claude Code» is another AI-agent for AI-assisted coding (or "vibe-coding"). This competes with [OpenAI Codex CLI](openai-codex-notes) in that it has a text-oriented user interface, but also integrates somewhat with Visual Studio Code: run it in the Terminal, and the changes it proposes are shown in the code pane as side-by-side diffs.

## Installing
The official setup instructions start off with installing it globally via npm, but it's also possible to set it up in an isolated directory:
```
npm init -y
npm install @anthropic-ai/claude-code
```

## AWS Bedrock: connection
AWS customers can consume the underlaying Claude models through AWS Bedrock, rather than the Anthropic API. To do so, the environment variable CLAUDE_CODE_USE_BEDROCK needs to be set upfront:
```
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1  # or different region
```

Also, the AWS credentials need to be established. Along with the former two environment variables, I keep the credentials in `.env.sh`:
```
export AWS_ACCESS_KEY_ID="A..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_SESSION_TOKEN="I..."
```
Using a Session Token carries the risk of it expiring eventually, perhaps while Claude Code is still open:
```
API Error: 403 The security token included in the request is expired
```

The remedy is to exit Claude Code with the "/quit" command, renew the AWS environment variables, and then resume the Claude Code session with:
```
npx claude -c
```

## Startup
Claude Code can, with the "local" installation method, be launched like this:
```
npx claude --add-dir ~/dev/test_project
```
This will add the test project to the working directories Claude Code allows itself to access.

Controlling Claude Code after launch is done in two ways: meta activities are available via slash-commands, e.g. "/quit" to exit Claude Code. Working on code is done by regular prompts, like "What is this about?". Both commands and prompts go into the input field.
![Claude Code in Visual Studio](assets/img/claude-code-input.jpg)

## AWS Bedrock: model selection
Claude Code seems to automatically select the model(s) to use. I had, however, neglected to enable the new models Sonnet 4 and Opus 4 in the AWS Bedrock "Model Access" console section, so was silently still on Sonnet 3.7 (and Haiku for some tasks) for a while without noticing. Model selection can be reviewed and switched using the "/model" command. The model string for Sonnet 4 in the US cross-inference region is `us.anthropic.claude-sonnet-4-20250514-v1:0`.

## Reviewing cost and other session data
Cost accrued in the current session can be reviewed through the "/cost" command:
```
> /cost 
  ⎿  Total cost:            $0.0544
     Total duration (API):  6.9s
     Total duration (wall): 11m 13.2s
     Total code changes:    0 lines added, 0 lines removed
     Usage by model:
         claude-3-5-haiku:  90 input, 23 output, 0 cache read, 0 cache write
            claude-sonnet:  3 input, 97 output, 0 cache read, 14.1k cache write
```

Other session data, including the current session ID can be obtained through "/status". The session ID lets users resume sessions other than the last session through:
```
npx claude -r <id>
```

## Notes
* creating a new project from scratch is simpler than with [hosted OpenAI Codex](openai-codex-web): just create the directory to work in and go - no cumbersome repository and environment setup required upfront. Drawback: OpenAI Codex is integrated with ChatGPT, and the mobile app allows working that way on-the-go - which is not possible with either Claude Code or Codex CLI.
* Claude Code can access web content out of the box! I had previously reviewed the mcp_fetch MCP server to bring Claude Code up to par to Codex, but that actually seems unnecessary.
    * It needs to be asked to access the web to retrieve some particular piece of information, though. If not asked, at least Sonnet 3.7 will happily hallucinate APIs rather than looking up the API reference.
    * I have included starting points on web in the prompt for my test project, but that may not be necessary: when prompted to "Check online for a simple example of the OpenAI Responses API" it did - with no web search needed?!
    * Unclear: how does it process web content - does fetching include conversion to text or Markdown
* at least with Sonnet 3.7, a certain lazyness was noticable: it created a stub implementation without explicitely pointing that out in the chat messages and when asked about it: "implemented as a stub because getting actual images from PowerPoint slides requires additional functionality that wasn't trivial to implement within the scope of this **example**.". So perhaps Claude needs to be prompted for "production-grade quality" to prevent "example" quality?
* Claude Code appeared to need more frequent interactions and corrections. This could be due to OpenAI codex-1 being are more powerful, more agentic model compared to Sonnet 3.7.
* As I quickly reached \$10 for a smallish project, these \$20 package deals - like GitHub Copilot or ChatGPT Plus - seem like good value.
* using AWS Bedrock rather than the Anthropic API does not insulate from being blocked by rate limiting - this still happens:
```
...
API Error (Request timed out.) • Retrying in 35 seconds... (attempt 8/10)
API Error (503 Model is getting throttled. Try your request again.) • Retrying in 36 seconds... (attempt 9/10)
API Error (503 Model is getting throttled. Try your request again.) • Retrying in 40 seconds... (attempt 10/10)
API Error: Request timed out.
```

[Update 2025-07-20]
Claude Code by default asks for confirmation before issuing shell commands. There is, however, an override that will auto-accept anything. Several commenters field anecdotal evidence that this is in fact dangerous as Claude either makes mistakes or, allegedly, [pursues its own goals](https://x.com/adidoit/status/1946275563829608899) ([archive link](http://archive.today/2025.07.20-083918/https://x.com/adidoit/status/1946275563829608899)).

[Update 2025-08-05]
The AWS Solutions Library has a [Guidance document on how to enable Claude Code rollout](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock) with Amazon Bedrock as the backend without handing out API keys. Core to this is third-party OpenID Connect (OIDC) providers like Okta or Microsoft Azure AD. 