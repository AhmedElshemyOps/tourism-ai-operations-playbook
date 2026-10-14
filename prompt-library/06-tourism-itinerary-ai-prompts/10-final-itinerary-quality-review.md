# Final Itinerary Quality Review

**Prompt ID:** `06-10-final-itinerary-quality-review`  
**Category:** Itinerary Planning  
**Department:** Product, Reservations and Operations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Complete a final quality gate across guest value, operations, clarity and verification.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A multi-day programme is ready to move from proposal to operations.

## Required inputs

- final programme
- guest profile
- confirmations
- inclusions
- exclusions
- timing audit
- accessibility
- contingency
- communication

## Expected outputs

- quality scorecard
- defects
- final checks
- guest-facing clarity edits
- approval record

## Copy-ready prompt

```text
ROLE
Act as a tourism product and guest-experience reviewer in a professional tourism organisation.

TASK
Complete a final quality gate across guest value, operations, clarity and verification.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: final programme; guest profile; confirmations; inclusions; exclusions; timing audit; accessibility; contingency; communication.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: quality scorecard; defects; final checks; guest-facing clarity edits; approval record. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not approve when a critical supplier, ticket, transfer or access item is unresolved.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-itinerary-ai-prompts.html) · [Library index](../README.md)
