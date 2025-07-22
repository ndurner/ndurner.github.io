---
layout: post
title: "Amazon Nova foundation model release"
date: 2024-12-03
tags: ["llm", "amazon", "nova"]
last_updated: 2025-07-21
description: "AWS guide for Amazon Nova: Bedrock model access, IAM policy creation, user credential setup, and Nova Pro testing in HuggingFace Bedrock Chat."
author: "Nils Durner"
categories: [journal]
---

[Update 2025-07-21: AWS has added [Amazon Bedrock API keys](https://aws.amazon.com/de/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/). I haven't tried this myself yet, but this could be a simplification to setting up IAM as described below.]

Since there's community interest in how to set up AWS to use the new Amazon Nova models, here's a step-by-step guide to get everyone started:

1. Ensure you have model access:
    1. open [Bedrock in us-west-2 region](https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#/), scroll down in the menu on the left, and hit Model Access: ![Image](assets/img/nova/bedrock-request-access.jpeg)
    2. Check model selection (green arrow), request models if access not yet granted (red arrow) ![Image](assets/img/nova/bedrock-model-selection.png)
1. Open [IAM](https://us-east-1.console.aws.amazon.com/iam/home?region=us-west-2#/home) -> Create user ![Image](assets/img/nova/Pasted image 20241203220626.png)
2. Name user ![Image](assets/img/nova/Pasted image 20241203220826.png)
3. Attach policy directly, create new policy ![Image](assets/img/nova/Pasted image 20241203221341.png)
4. Switch to JSON view, paste pre-made policy (JSON code block below at the end of this post): ![Image](assets/img/nova/Pasted image 20241203221623.png)
5. Hit Next ![Image](assets/img/nova/Pasted image 20241203221733.png)
6. Name policy, hit Create Policy ![Image](assets/img/nova/Pasted image 20241203221901.png)
7. Close this tab, return to IAM user creation tab
8. Refresh table, search for newly created policy, tick box, hit Next ![Image](assets/img/nova/Pasted image 20241203222202.png)
9. Hit Create User ![Image](assets/img/nova/Pasted image 20241203222232.png)
10. Open new IAM user by clicking its link ![Image](assets/img/nova/Pasted image 20241203222631.png)
11. Create Access Key ![Image](assets/img/nova/Pasted image 20241203222906.png)
12. Choose "Local Code", Confirm "I understand...", Hit Next ![Image](assets/img/nova/Pasted image 20241203223059.png)
13. Create Access Key ![Image](assets/img/nova/Pasted image 20241203223202.png)
14. Copy both values - these are your access credentials ![Image](assets/img/nova/Pasted image 20241203223324.png)
15. Visit [my Amazon Bedrock Chat space on HuggingFace](https://huggingface.co/spaces/ndurner/amz_bedrock_chat), paste Credentials, choose Nova Pro model ![Image](assets/img/nova/Pasted image 20241203223707.png)
    1. Source code also available on [Github](https://github.com/ndurner/amz_bedrock_chat)
16. Enjoy ![Image](assets/img/nova/Pasted image 20241203223816.png)

Policy JSON:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "bedrock:GetUseCaseForModelAccess",
                "bedrock:GetFoundationModelAvailability",
                "bedrock:InvokeModel",
                "bedrock:ListCustomModels",
                "bedrock:ListFoundationModelAgreementOffers",
                "bedrock:GetFoundationModel",
                "bedrock:InvokeModelWithResponseStream",
                "bedrock:GetCustomModel",
                "bedrock:ListFoundationModels"
            ],
            "Resource": "*"
        }
    ]
}
```

Other notes:
* Pelicane SVGs have been updated: [Pelicane-on-a-bike gallery](https://github.com/ndurner/pelican-bicycle)
* other models do implicit spell-correction in OCR use cases ([via Eleanor Berger](https://x.com/intellectronica/status/1811261267547459610)). Nova Pro doesn't?
* unreleased advanced [Plan like a Graph](openai-o1-preview) use case doesn't work, so not really "GPT-4 class" as alleged by Amazon?