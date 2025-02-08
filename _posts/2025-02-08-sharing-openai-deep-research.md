---
layout: post
title: "Sharing OpenAI Deep Research"
author: "Nils Durner"
categories: [journal]
tags: [ai, openai, agents, chatgpt, deep research]
date: 2025-02-08
last_updated: 2025-02-08
---

Sharing results from OpenAI Deep Research is not straightforward as simple copy & paste will cobble up attributions. What works instead is lifting the HTML fragment from ChatGPT and building a document from there. Step-by-step:
1. In the browser version of ChatGPT, target the title in the response report. Do a left-click, open the Developer Console, and copy the grand-parent (../..) node of the h1 title to the clipboard (STRG + C or Cmd + C)
2. Paste to Visual Studio Code or any other code editor
3. Copy the header code (first fragment) from [this gist](https://gist.github.com/ndurner/422e22e49a717a46d67309c481c65d2d) to the clipboard, and paste it above the code from ChatGPT in Visual Studio Code. This will fix-up special characters and improve readability.
    1. Optionally, specify some title for the target document within "<title></title>"
4. Copy the footer code (last fragment) from the gist, and paste it to at the end of the ChatGPT code
5. Open search & replace, enable Regular Expression mode (`.*` icon in Visual Studio Code), and replace all instances of the following:

    ```regex
    (?:<div[^>]*>\s*)?<a href="([^"]+)"[^>]*>\s*<span[^>]*>(.*?)<\/span>\s*<\/a>(?:\s*<\/div>)?
    ```

    with:

    ```html
    <a href="$1" target="_blank"><span class="link-icon">&nbsp;🔗</span>$2</a>
    ```
6. Save the file with .html extension. Optionally, either open the HTML file in:
    1. Word and save as DOCX, or
    2. in your browser and print it to PDF
7. Share the result
