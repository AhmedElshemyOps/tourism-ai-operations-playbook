# Driver Briefing Preparation

**Prompt ID:** `04-04-driver-briefing-preparation`  
**Category:** Transport and Dispatch  
**Department:** Fleet, Transport and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Prepare a concise driver briefing from confirmed movement data.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A driver handles hotel pickups, a mosque stop and a separate airport drop-off.

## Required inputs

- driver
- vehicle
- date
- pickups
- contacts through approved channel
- route
- parking
- guest count
- special needs
- guide
- escalation

## Expected outputs

- one-page briefing
- movement timeline
- location notes
- must-confirm list
- exception procedure

## Copy-ready prompt

```text
ROLE
Act as a tourism dispatch supervisor in a professional tourism organisation.

TASK
Prepare a concise driver briefing from confirmed movement data.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: driver; vehicle; date; pickups; contacts through approved channel; route; parking; guest count; special needs; guide; escalation.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: one-page briefing; movement timeline; location notes; must-confirm list; exception procedure. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Exclude unnecessary guest personal data and do not include unverified route instructions.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-transport-dispatch-ai-prompts.html) · [Library index](../README.md)
