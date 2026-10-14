# Pre-Tour Preparation

**Prompt ID:** `02-01-pre-tour-preparation`  
**Category:** Front-Line Service  
**Department:** Tour Guiding and Guest-Facing Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Turn a confirmed tour file into a practical guide preparation brief.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A French-speaking family group has a city tour with two timed-entry attractions.

## Required inputs

- tour date
- product name
- verified itinerary
- guest profile
- language
- pickup data
- confirmed tickets
- guide notes
- weather source
- escalation contacts

## Expected outputs

- timeline
- guest-needs notes
- verified facts to prepare
- operational checks
- risk points
- questions for operations

## Copy-ready prompt

```text
ROLE
Act as a licensed senior tour guide and operations trainer in a professional tourism organisation.

TASK
Turn a confirmed tour file into a practical guide preparation brief.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: tour date; product name; verified itinerary; guest profile; language; pickup data; confirmed tickets; guide notes; weather source; escalation contacts.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: timeline; guest-needs notes; verified facts to prepare; operational checks; risk points; questions for operations. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not invent attraction hours, access, tickets or guest requirements. Remove direct identifiers.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/front-line-tourism-ai-toolkit.html) · [Library index](../README.md)
