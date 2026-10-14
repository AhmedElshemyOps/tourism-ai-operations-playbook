# Delay Communication

**Prompt ID:** `02-06-delay-communication`  
**Category:** Front-Line Service  
**Department:** Tour Guiding and Guest-Facing Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Prepare staged guest communication for a confirmed or developing delay.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A vehicle is late at a hotel and operations can only confirm that an update will follow in ten minutes.

## Required inputs

- confirmed facts
- cause category
- current delay range
- guest location
- next update time
- available alternatives
- escalation contact
- authority

## Expected outputs

- immediate message
- next-update message
- guide speaking notes
- questions to operations
- recovery boundary

## Copy-ready prompt

```text
ROLE
Act as a front-line service recovery coach in a professional tourism organisation.

TASK
Prepare staged guest communication for a confirmed or developing delay.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: confirmed facts; cause category; current delay range; guest location; next update time; available alternatives; escalation contact; authority.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: immediate message; next-update message; guide speaking notes; questions to operations; recovery boundary. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not state a cause or new time unless confirmed. Do not promise compensation.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/front-line-tourism-ai-toolkit.html) · [Library index](../README.md)
