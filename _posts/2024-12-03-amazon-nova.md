---
layout: post
title: "Amazon Nova foundation model release"
date: 2024-12-03
tags: ["llm", "amazon", "nova"]
last_updated: 2024-12-03
author: "Nils Durner"
categories: [journal]
---

Since there's interest in how to set up AWS to use the new Amazon Nova models, here's a step-by-step guide to get everyone started:

1. Open IAM -> Create user ![Image](assets/img/nova/Pasted image 20241203220626.png)
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
* other models do implicit spell-correction in OCR use cases ([via Eleanor Berger](https://x.com/intellectronica/status/1811261267547459610)). This one doesn't?
* unreleased advanced [Plan like a Graph](openai-o1-preview) use case doesn't work, so not really "GPT-4 class" as alleged by Amazon?