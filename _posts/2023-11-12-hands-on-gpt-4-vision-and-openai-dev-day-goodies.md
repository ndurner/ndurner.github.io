---
layout: post
title: "Hands-on GPT-4V(ision) and other OpenAI Dev Day goodies"
date: 2023-11-12
last_updated: 2023-11-12
tags: [GPT-4, OpenAI, Dev Day, Chatbot]
filename: 2023-11-12-hands-on-gpt-4-vision-and-openai-dev-day-goodies.md
---

Hands-on **GPT-4V(ision)** and other **OpenAI Dev Day goodies**

The OpenAI Playground has not been updated (yet?) to reflect several of the new features shown at Dev Day last weeks. So I have retooled my [Bedrock Chatbot](amazon-bedrock-chat-nils-version) to support OpenAI: **OAI Chat (Nils' Version)**, screenshot: image #6.

Feature review:  
⚙️ the new "**Seed**" parameter. From the documentation: "If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result."

- Not implemented (yet): the new Fingerprint: "Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend."

🚀 **GPT-4 Turbo** support: very long inputs ("context"), nominally surpassing that of Anthropic's Claude-2: 128K tokens vs. 100K.

- actual model name in the combo box (and API): gpt-4-1106-preview
- chatbot allows upload of text files to operate on (see also the [Bedrock version](amazon-bedrock-chat-nils-version))
- early reports also indicate non-uniform attention: "[GPT-4’s recall performance started to degrade above 73K tokens](https://x.com/GregKamradt/status/1722386725635580292?s=20)" (see image #1). However, it allegedly improves on GPT-4-32K: "[Around 8k tokens, retrieval of facts is double that of prior gpt-4 iterations](https://www.linkedin.com/posts/appenz_ok-so-long-context-windows-still-dont-work-activity-7128539381287587842-KFOJ?utm_source=share&utm_medium=member_desktop)" (image #2).
- other Chat models also supported

👀 **Vision** support: the chatbot allows images to be uploaded and to be chatted about. According to my first handful of tests, GPT-4V is really, really powerful and accurate!

Some random example images, not cherry picked (prompt for each: "Describe the image"):

1. (image #3, taken by me): "The image shows a woman holding a smartphone with her right hand, displaying a screen that seems to indicate a successful identification process, as depicted by a cartoon depiction of a person's face and a green checkmark. The smartphone screen also contains text in German that appears to be instructions or a confirmation related to the identification. In the background, there is a computer monitor displaying a webpage with text in German that translates to "The identification is completed". It seems to suggest that a digital identity verification process has been successfully finished. The rest of the text on the computer screen hints at directions or next steps, and there is a hyperlink for further action. The woman is shown from behind and partially from the side, and her face is not visible. She is wearing what looks like a white lace or crochet blouse or dress. Her left ear with an earring is slightly visible as she looks towards the computer monitor. There is also another smartphone or small device lying on the table next to the keyboard. The environment suggests an office setting or a workspace."
2. (image #4, taken by me): "This image shows a modern workspace environment with a large window offering a view of other buildings and trees. On the white table, there's a laptop, which appears to be a Lenovo ThinkPad, positioned to the left, its screen tilted slightly backward. In front of the laptop, there's an empty coffee cup stained with coffee residue, branded with "Namirial Milano 2022," which suggests it might be a promotional item from an event or company. To the right of the laptop, there's a cereal bar, partially unwrapped, and a pair of white earbuds resting on the table. The scene conveys a sense of a break or pause in work, as the snack is unattended and the laptop is left open, indicating that the person who was working there might have stepped away momentarily. The natural light from the window suggests it might be daytime, and the overall setting seems calm and orderly."
3. (image #5, web-sourced): "The image shows a person wearing a black T-shirt with a graphic and text on it. The graphic is a play on the iconic album cover design from Pink Floyd's "The Dark Side of the Moon," which features a prism and a rainbow. Instead of the prism, there is a triangular-shaped black and white image of Sigmund Freud, the famous neurologist and founder of psychoanalysis, with a rainbow stripe running across the top corner. The wordplay on the T-shirt reads "PINK FREUD" at the top in a font similar to the Pink Floyd logo. Below the triangle, it says "THE DARK SIDE OF YOUR MOM" in a curved font, mimicking the "The Dark Side of the Moon" album title but altering the text for humorous effect. The humor seems to stem from a pun involving the band's name and Freud's name, as well as a playful twist on the album's title."

For comparison, these are **Google Bard**'s responses - rather heavily hallucinated and inaccurate/wrong for my own photos; factually correct for the photo from the web:

(image #3): "The image shows a woman holding a cell phone in front of a computer monitor. The woman is wearing a white shirt and jeans, and she has long, dark hair. She is standing in front of a computer monitor, and she is looking at the screen of the computer monitor. The computer monitor is displaying the text "Die Identifizierung ist abgeschlossen", which is German for "The identification is complete". The image is likely taken in an office setting, as the woman is standing in front of a desk and there are other computers and office equipment in the background. It is difficult to say for sure what the woman is doing in the image, but it is possible that she is using her cell phone to take a photo of the computer monitor. Alternatively, she could be using her cell phone to authenticate her identity with the computer."

(image #4): "The image shows a Namirial Milano 2022 laptop computer sitting on a white table next to a cup of coffee. The laptop is open and displaying the Namirial logo. The cup of coffee is steaming and has a small spoon resting on the side. The background is blurred, but it appears to be a coffee shop or cafe. The laptop is a Lenovo ThinkPad X1 Carbon Gen 6. It is a high-end business laptop with a thin and light design. It has a 14-inch display, a Core i7 processor, and 16GB of RAM. The cup of coffee is likely a latte or cappuccino. The overall mood of the image is one of relaxation and productivity. The laptop and coffee are both symbols of work, but the blurred background and the steam from the coffee suggest that the person in the image is taking a break. Here is a more detailed description of the image:

- The laptop is facing the viewer, with its screen open. The screen is displaying the Namirial logo, which is a blue and white globe.
- The laptop is sitting on a white table. The table is empty except for the laptop and the cup of coffee.
- The cup of coffee is sitting to the right of the laptop. The cup is white and has a brown handle. There is a small spoon resting on the side of the cup.
- The background of the image is blurred. It appears to be a coffee shop or cafe, but it is difficult to see any details.

The image is well-composed and well-lit. The laptop and the cup of coffee are both in focus, and the blurred background helps to create a sense of depth. The overall effect is a pleasant and inviting image."

(image #5, web-sourced): "The image shows a man wearing a black t-shirt with a picture of Sigmund Freud smoking a cigar and a rainbow flag on it. The text on the shirt reads "PINK FREUD THE DARK SIDE OF YOUR MOM"."

🙋‍♂️ **OAI Chat (Nils' Version)**:

- Prerequisite: OpenAI API Key
- Ready-to-run on HuggingFace 😊: [https://huggingface.co/spaces/ndurner/oai_chat](https://huggingface.co/spaces/ndurner/oai_chat)
- Source Code: [https://github.com/ndurner/oai_chat](https://github.com/ndurner/oai_chat)
- requires latest Gradio

💡 **Insights**

- GPT-4V really looks good to me
  - ([restrictions apply](https://platform.openai.com/docs/guides/vision/limitations), [other testimonials are mixed](https://x.com/HuaxiuYaoML/status/1721742474568253634?s=20))
- suspicious: Bard did okay on only one picture - the one pulled from the web. Heavily hallucinated and inaccurate/wrong for my own photos.

⚠️ Be mindful when testing with long documents as these easily cost > $1 per single request.

![needle-in-a-haystack-gpt4.png](assets/img/needle-in-a-haystack-gpt4.png)\
![context-utilization-gpt4.png](assets/img/context-utilization-gpt4.png)\
![ident-done.jpg](assets/img/ident-done.jpg)\
![laptop-mug.jpeg](assets/img/laptop-mug.jpeg)\
![pink-freud.png](assets/img/pink-freud.png)\
![oai-chat.png](assets/img/oai-chat.png)
