# Weather Backup Plan

**Prompt ID:** `06-08-weather-backup-plan`  
**Category:** Itinerary Planning  
**Department:** Product, Reservations and Operations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Create pre-approved alternatives and decision triggers for weather-sensitive services.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A desert dinner may be affected by wind and low visibility.

## Required inputs

- original itinerary
- weather source
- thresholds
- indoor options verified
- tickets
- transport
- guest profile
- communication
- cost authority

## Expected outputs

- trigger table
- alternative schedules
- decision owner
- guest messages
- supplier actions
- cost flags

## Copy-ready prompt

```text
ROLE
Act as a tourism contingency planner in a professional tourism organisation.

TASK
Create pre-approved alternatives and decision triggers for weather-sensitive services.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: original itinerary; weather source; thresholds; indoor options verified; tickets; transport; guest profile; communication; cost authority.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: trigger table; alternative schedules; decision owner; guest messages; supplier actions; cost flags. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not forecast beyond the supplied official information or guarantee conditions.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-itinerary-ai-prompts.html) · [Library index](../README.md)
