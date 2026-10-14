# Tourism Context Development

**Prompt ID:** `01-04-tourism-context-development`  
**Category:** Prompt Engineering  
**Department:** Cross-functional Tourism Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Convert scattered background notes into a precise operating context section for an ai prompt.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A team is preparing a prompt for a desert dinner operation during a peak event week.

## Required inputs

- destination
- product
- guest journey stage
- season
- service window
- suppliers
- team roles
- local rules
- known exceptions

## Expected outputs

- context statement
- boundary conditions
- dependencies
- assumptions requiring approval

## Copy-ready prompt

```text
ROLE
Act as a destination-management consultant in a professional tourism organisation.

TASK
Convert scattered background notes into a precise operating context section for an ai prompt.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: destination; product; guest journey stage; season; service window; suppliers; team roles; local rules; known exceptions.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: context statement; boundary conditions; dependencies; assumptions requiring approval. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not describe dynamic destination conditions as confirmed unless a source and date are supplied.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-prompting-framework.html) · [Library index](../README.md)
