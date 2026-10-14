# Pickup Confirmation

**Prompt ID:** `08-02-pickup-confirmation`  
**Category:** Guest Experience  
**Department:** Customer Experience and Service Recovery  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Draft a pickup confirmation that reduces missed connections.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** Airport guests need a clear meeting-point and delayed-flight instruction.

## Required inputs

- date
- confirmed time/window
- verified location
- meeting sign
- representative
- vehicle information allowed
- luggage
- guest action
- emergency channel

## Expected outputs

- concise message
- location steps
- what to do if delayed
- accessibility note
- internal check

## Copy-ready prompt

```text
ROLE
Act as a DMC guest communications coordinator in a professional tourism organisation.

TASK
Draft a pickup confirmation that reduces missed connections.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: date; confirmed time/window; verified location; meeting sign; representative; vehicle information allowed; luggage; guest action; emergency channel.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: concise message; location steps; what to do if delayed; accessibility note; internal check. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not expose driver personal details beyond policy or invent a precise time from a window.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/guest-experience-ai-prompts.html) · [Library index](../README.md)
