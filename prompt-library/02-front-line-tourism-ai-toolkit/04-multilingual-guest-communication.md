# Multilingual Guest Communication

**Prompt ID:** `02-04-multilingual-guest-communication`  
**Category:** Front-Line Service  
**Department:** Tour Guiding and Guest-Facing Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Draft and quality-check a guest-facing message in the required languages.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** An airport representative sends a pickup meeting-point update in English and French.

## Required inputs

- approved source message
- target language
- channel
- formality
- guest action
- timing
- local terminology
- emergency contact format

## Expected outputs

- source-language revision
- translation
- back-translation summary
- terminology notes
- bilingual review flags

## Copy-ready prompt

```text
ROLE
Act as a bilingual tourism communication specialist in a professional tourism organisation.

TASK
Draft and quality-check a guest-facing message in the required languages.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: approved source message; target language; channel; formality; guest action; timing; local terminology; emergency contact format.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: source-language revision; translation; back-translation summary; terminology notes; bilingual review flags. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not translate names, codes, legal terms or safety wording inaccurately. Require competent human review.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/front-line-tourism-ai-toolkit.html) · [Library index](../README.md)
