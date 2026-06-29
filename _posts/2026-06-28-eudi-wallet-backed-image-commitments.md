---
title: "EUDI Wallet-backed image commitments"
date: 2026-06-28
last_updated: 2026-06-28T12:13:06+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/eudi-wallet-backed-image-commitments
tags: [Substack]
excerpt: "The first European Digital Identity Wallet hackathon for the German implementation has concluded. My submission is IIRY - an iPhone/iPad app + small backend that lets, for example, a parent challenge a request for money by a child over WhatsApp. It builds on - and extends - two relevant Content Credentials standards: C2PA and CAWG VC+VP. Important boundary: IIRY does not prove that the WhatsApp ac"
substack_url: "https://ndurner.substack.com/p/eudi-wallet-backed-image-commitments"
canonical_url: "https://ndurner.substack.com/p/eudi-wallet-backed-image-commitments"
sitemap: false
---

The first European Digital Identity Wallet [hackathon](https://eudi-wallet.gov.de/en/news/eudi-wallet-hackathon-2026) for the German implementation has concluded. My submission is *IIRY* - an iPhone/iPad app + small backend that lets, for example, a parent challenge a request for money by a child over WhatsApp. It builds on - and extends - two relevant Content Credentials standards: [C2PA](https://c2pa.org) and [CAWG](https://cawg.io) [VC+VP](https://cawg.io/identity/1.3-draft+vc-vp/).

Important boundary: IIRY does not prove that the WhatsApp account belongs to the wallet holder, that the message is true, or that the request is legitimate. It proves something narrower: a state-issued EUDI Wallet holder presentation was bound to this particular image file, and the visible challenge lets the receiver judge whether the screenshot answers the request they sent.

As the whole EUDIW ecosystem is not in production yet, IIRY relies on the German sandbox implementation - which is not yet feature-complete itself. The sandbox does not allow real identities to be used and is thus restricted to the test persona of “Erika Mustermann”.

## Flow
