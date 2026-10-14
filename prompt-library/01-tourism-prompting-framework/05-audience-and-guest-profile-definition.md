# Audience and Guest-Profile Definition

**Prompt ID:** `01-05-audience-and-guest-profile-definition`  
**Category:** Prompt Engineering  
**Department:** Cross-functional Tourism Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Create a respectful, operationally useful audience profile without stereotypes or unnecessary personal data.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A guide trainer needs to adapt one destination story for families and a corporate delegation.

## Required inputs

- market
- language
- age mix
- group type
- interests
- pace
- mobility
- dietary needs
- trip purpose
- service level

## Expected outputs

- guest-needs summary
- communication implications
- operational implications
- questions still required

## Copy-ready prompt

```text
ROLE
Act as a guest experience and segmentation specialist in a professional tourism organisation.

TASK
Create a respectful, operationally useful audience profile without stereotypes or unnecessary personal data.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: market; language; age mix; group type; interests; pace; mobility; dietary needs; trip purpose; service level.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: guest-needs summary; communication implications; operational implications; questions still required. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Avoid assumptions based on nationality, age, disability, religion or spending level. Use only supplied evidence.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-prompting-framework.html) · [Library index](../README.md)
