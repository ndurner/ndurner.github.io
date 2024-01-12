---
layout: post
title: "Overview of Model deployment options"
date: 2023-11-29
tags: [Amazon, AWS, AI]
---

Overview of Model deployment options on AWS, which also takes into account cost implications: [LinkedIn](https://www.linkedin.com/posts/ryfeus_mongodb-awscommunity-llms-activity-7135391192397082624-VhgT?utm_source=share&utm_medium=member_desktop). \
It's important to note that the comparison may not be entirely straightforward, as the slides alone do not provide a full picture. However, they do reveal some significant cost variances that may need to be considered. In particular, AWS Lambda stands out as a substantial expense, with the potential to exceed the costs of even the priciest foundation model inference. To clarify the $50 figure mentioned in screenshot #1, the author kindly provided further insight in a follow-up comment on LinkedIn:
> Roughly lambda pricing is: \
\(\$0.0000166667\/Gb*s\)\*10Gb\*0.3s * 1M = 50\$ per 1M tokens \
given 1 token is generated in 300ms