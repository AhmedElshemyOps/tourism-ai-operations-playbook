# Delay Notification

**Prompt ID:** `08-04-delay-notification`  
**Category:** Guest Experience  
**Department:** Customer Experience and Service Recovery  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Prepare transparent staged updates during a service delay.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A group waits at an attraction because tickets are not yet released.

## Required inputs

- service
- confirmed delay
- cause confirmed or unknown
- guest impact
- current action
- next update
- alternatives approved
- support channel

## Expected outputs

- immediate alert
- update message
- resolved message
- call script
- internal log points

## Copy-ready prompt

```text
ROLE
Act as a guest service duty manager in a professional tourism organisation.

TASK
Prepare transparent staged updates during a service delay.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: service; confirmed delay; cause confirmed or unknown; guest impact; current action; next update; alternatives approved; support channel.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: immediate alert; update message; resolved message; call script; internal log points. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not create a new ETA, blame a supplier or promise recovery without approval.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/guest-experience-ai-prompts.html) · [Library index](../README.md)
