# Shift Handover

**Prompt ID:** `03-09-shift-handover`  
**Category:** DMC Operations  
**Department:** Operations and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Convert open operational notes into a clear handover for the next shift.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** The evening shift hands over two delayed bags, a pending driver and tomorrow’s early VIP arrival.

## Required inputs

- open issues
- current status
- last action
- next action
- owner
- deadline
- guest impact
- supplier contact
- evidence location

## Expected outputs

- red-amber-green summary
- item cards
- deadlines
- escalation watch
- completed items excluded

## Copy-ready prompt

```text
ROLE
Act as a DMC control-room supervisor in a professional tourism organisation.

TASK
Convert open operational notes into a clear handover for the next shift.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: open issues; current status; last action; next action; owner; deadline; guest impact; supplier contact; evidence location.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: red-amber-green summary; item cards; deadlines; escalation watch; completed items excluded. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not close or downgrade an item without evidence.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/dmc-operations-ai-prompts.html) · [Library index](../README.md)
