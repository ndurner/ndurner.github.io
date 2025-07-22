---
layout: post
title: "OpenAI Codex Web: Practical Notes"
description: "Notes on using OpenAI Codex Web: setup, agentic workflows, container environments, web access, limitations"
date: 2025-06-19
tags: ["openai", "codex", "github", "agents", "prompt-engineering", "llm", "automation", "ai-coding"]
last_updated: 2025-07-17
author: "Nils Durner"
categories: [journal]
---

The [first OpenAI hackathon in the EU](https://www.linkedin.com/posts/nilsdurner_buildwithopenai-regtech-openai-activity-7340614796666388480-aruM?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAGX2jIBd6RDsNRYv13Bvu3x4nnCNu96SEw) was about writing Agents using Agents. We received access to Codex in our kit as part of ChatGPT Pro, but it by now also seems to be available to other paid plans including Plus. Codex in ChatGPT is different from [Codex CLI](openai-codex-notes).

## Notes
* Codex CLI is powered by the codex-1-mini language model, Codex is powered by codex-1 - so supposedly a bigger model
* Setup for a particular project includes granting access to a Github repository and setting up a so-called environment - which boils down to the container to run it (detailed below)
* Difference to Github Copilot etc.: it's not interactive throughout, but works autonomously ("agentic") after the task has been posed by the user. When the agent is done, the user is presented with a diff view of the changes made, with the option open a pull-request on Github.
* Task completion takes place in a web-hosted Ubuntu 24.04 ephemeral execution environment container, which is torn down after each task processing
    * [Reference docker image](https://github.com/openai/codex-universal)
    * several coding tools and environments come pre-installed, like Python, node.js, Bun, Go, Swift, Rust, Java, cmake and C library development headers (e.g. libxml2-dev)
    * Codex allows additional packages to be installed in these containers, as well as configuration changes to be made
        * this allows installation of 
* there are two modes: "Ask question" and "Code task", which start up different containers ("Ask" container has quicker startup time)
* Web access can be enabled in different tiers of access, and comes with warnings regarding security. It reportedly uses the Cloudflare "family safe" DNS server/filter. In practice, I saw several messages from Codex that it couldn't access a particular website, though.
* Ubuntu containers make it of limited use for native iOS/macOS apps that depend on proprietary APIs like SwiftUI, because hallucinated APIs cannot be uncovered during a subsequent (and automated) build process run by Codex itself.
    * providing subsequent verification mechanisms to coding agents like unit tests, linters, and commit hooks so the agent can validate the changes made - and perhaps then fix them accordingly - appears like a common emerging paradigm
* running o3 upfront to refine the prompt or plan execution does not seem necessary
    * caution when describing tasks: - AI assistants including ChatGPT and Grok are tripped over by the legacy „codex“ language model. When asking for Codex, also mention that this is distinct from Github Copilot - I have seen the consideration in o3's reasoning process, that "the user must be talking about Github Copilot, actually".
* executing on user-interaction is delayed by container startup and setup, making round-trips and refinements time-intensive
    * remedy: submit many tasks in parallel. Current rate limit is 60 tasks per hour (but may change in the future; also pricing is TBD)
* perhaps all agents like to do keyword search on the codebase, so it's beneficial to use distinct code names or descriptive names. An example is "WHAM", the code name used by the OpenAI Codex team (see the phrase "really efficient for the agent to find" on the [Latent Space podcast transcript on Codex](https://www.latent.space/p/codex#:~:text=really%20efficient%20for%20the%20agent%20to%20find))
* Other practical tests that show some limitations:
    * big task, fresh repo: create an iOS chatbot app in Qt based on Responses API. First result used Python, so had to spell the C++ requirement out. Second result used the ChatCompletions API, despite I had prompted for the Responses API. Third result did use the Reponses API endpoint, but kept the ChatCompletions API input JSON format ("messages" vs "input"). Also, errors returned from the API (regarding the "inputs" absence) were not handled/displayed as a user-facing error, so had to debug manually. And so on... until finally the output did appear, but duplicated (once from streaming, the other instance from the final event).
    * sub-task from the previous one: refer to the documentation. This internally failed repeatedly because Codex will only handle outputs from commands with a limit of 1600 bytes. Codex downloaded the documentation with curl, but reading the first 20 lines using the "head" command yielded 7K bytes of HTML - so Codex could not proceed that way (error message below). Solved by presenting it with the Open API specification of the API instead of the simple web link.

The failure with the big task based on a fresh repo reinforce the [Prompting advice](https://platform.openai.com/docs/codex/overview#prompting-codex) to split larger tasks into smaller, focused steps. Questions on how-large-is-too-large and how to structure creation of entirely new projects remains a craft to be developed.

## Error messages
... for reference:

### When hitting the input limit with the OpenAI documentation

>> root@b32752d36b69:/workspace# cd llm-chat-qt  
>> root@b32752d36b69:/workspace/llm-chat-qt# curl -L -s https://platform.openai.com/docs/api-reference/responses | head -n 20  
>  
> Error: Output for session 'shell' contained a line exceeding the max of 1600 bytes (observed at least 7371 bytes).  
>   
> The byte sequence which exceeded the limit started with: b'<!DOCTYPE html><html'  
>  
> The exec session has been deleted. Please start a new session.  
>   
> Tip - rerun the command and extract only what you need, e.g.:  
>  * grep -nE 'PATTERN' FILE | cut -c1-200  
>  * grep -o 'PATTERN' FILE  
>  * jq -r '.json.path' FILE  
>  * grep -a PATTERN FILE

### When operating on a fresh repository
Error message:
    * 🇺🇸 "Failed to create task"
    * 🇩🇪 "Aufgabenerstellung fehlgeschlagen"
Remedy: create at least one file in the Github repository, e.g. an empty Readme.md

[Update 2025-07-17]
Once the paid ChatGPT subscription expires, Codex cannot be accessed at all: any questions or code activities that have not been turned into a Pull Request before expiry are inaccessible then.

[Update 2025-07-20]
(added note that Github repositories to work on must not be completely empty)