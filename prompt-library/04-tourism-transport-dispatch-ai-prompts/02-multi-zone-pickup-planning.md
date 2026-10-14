# Multi-Zone Pickup Planning

**Prompt ID:** `04-02-multi-zone-pickup-planning`  
**Category:** Transport and Dispatch  
**Department:** Fleet, Transport and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Decide whether a movement should remain combined or split by operating zone.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** Bookings span Abu Dhabi city, Yas Island and Saadiyat with a 60-minute pickup window.

## Required inputs

- zone map
- hotels
- guests
- service window
- vehicle options
- route evidence
- maximum zones
- split rules
- cost authority

## Expected outputs

- combined plan
- split alternatives
- comparison
- critical constraint
- recommended draft
- approval point

## Copy-ready prompt

```text
ROLE
Act as a DMC dispatch controller in a professional tourism organisation.

TASK
Decide whether a movement should remain combined or split by operating zone.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: zone map; hotels; guests; service window; vehicle options; route evidence; maximum zones; split rules; cost authority.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: combined plan; split alternatives; comparison; critical constraint; recommended draft; approval point. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not optimise cost by violating pickup windows, capacity or guest-service standards.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-transport-dispatch-ai-prompts.html) · [Library index](../README.md)
