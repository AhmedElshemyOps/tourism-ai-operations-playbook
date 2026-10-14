# General Tourism Prompt Builder

**Prompt ID:** `01-01-general-tourism-prompt-builder`  
**Category:** Prompt Engineering  
**Department:** Cross-functional Tourism Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Turn a rough tourism request into a complete travel-format instruction that another employee can use consistently.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A DMC product executive needs a reusable prompt for reviewing a new half-day city tour.

## Required inputs

- rough request
- department
- destination
- service type
- audience
- verified facts
- operational constraints
- deadline
- approver

## Expected outputs

- improved prompt
- missing-information questions
- risk flags
- verification plan
- approval point

## Copy-ready prompt

```text
ROLE
Act as a senior tourism prompt architect in a professional tourism organisation.

TASK
Turn a rough tourism request into a complete travel-format instruction that another employee can use consistently.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: rough request; department; destination; service type; audience; verified facts; operational constraints; deadline; approver.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: improved prompt; missing-information questions; risk flags; verification plan; approval point. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not add facts that were not supplied. Keep placeholders wherever evidence or authority is missing.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-prompting-framework.html) · [Library index](../README.md)
