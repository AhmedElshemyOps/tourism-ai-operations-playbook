# Late-Vehicle Response

**Prompt ID:** `04-07-late-vehicle-response`  
**Category:** Transport and Dispatch  
**Department:** Fleet, Transport and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Prepare a timed response plan for a late or uncontactable vehicle.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A vehicle is absent ten minutes before pickup for an airport departure.

## Required inputs

- planned time
- current time
- driver status
- location evidence
- guests
- service deadline
- backups
- contact channels
- authority

## Expected outputs

- first five minutes
- next update
- backup trigger
- guest message
- supplier escalation
- incident log

## Copy-ready prompt

```text
ROLE
Act as a transport duty controller in a professional tourism organisation.

TASK
Prepare a timed response plan for a late or uncontactable vehicle.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: planned time; current time; driver status; location evidence; guests; service deadline; backups; contact channels; authority.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: first five minutes; next update; backup trigger; guest message; supplier escalation; incident log. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not report a new ETA without evidence or promise compensation.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-transport-dispatch-ai-prompts.html) · [Library index](../README.md)
