# Missing Booking Information Detection

**Prompt ID:** `03-05-missing-booking-information-detection`  
**Category:** DMC Operations  
**Department:** Operations and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Detect missing booking information before operational release.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A private transfer file has flight number but no terminal, contact method or child-seat confirmation.

## Required inputs

- tour file
- mandatory-field standard
- itinerary
- guest requirements
- supplier status
- internal notes

## Expected outputs

- stop-release items
- high-priority gaps
- lower-priority questions
- owner
- required-by time

## Copy-ready prompt

```text
ROLE
Act as a DMC reservations-to-operations controller in a professional tourism organisation.

TASK
Detect missing booking information before operational release.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: tour file; mandatory-field standard; itinerary; guest requirements; supplier status; internal notes.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: stop-release items; high-priority gaps; lower-priority questions; owner; required-by time. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not fill gaps with typical values or past booking patterns.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/dmc-operations-ai-prompts.html) · [Library index](../README.md)
