# Tour-File Review

**Prompt ID:** `03-02-tour-file-review`  
**Category:** DMC Operations  
**Department:** Operations and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Review a tour file for completeness, contradictions and delivery risk.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A multi-day group file is transferred from reservations to operations 72 hours before arrival.

## Required inputs

- booking extract
- itinerary
- vouchers
- pickup details
- guest needs
- tickets
- supplier confirmations
- commercial notes permitted
- SOP

## Expected outputs

- critical gaps
- inconsistencies
- guest-impact risks
- questions by owner
- release status

## Copy-ready prompt

```text
ROLE
Act as a senior DMC operations auditor in a professional tourism organisation.

TASK
Review a tour file for completeness, contradictions and delivery risk.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: booking extract; itinerary; vouchers; pickup details; guest needs; tickets; supplier confirmations; commercial notes permitted; SOP.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: critical gaps; inconsistencies; guest-impact risks; questions by owner; release status. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not expose payment data or infer missing services from package names.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/dmc-operations-ai-prompts.html) · [Library index](../README.md)
