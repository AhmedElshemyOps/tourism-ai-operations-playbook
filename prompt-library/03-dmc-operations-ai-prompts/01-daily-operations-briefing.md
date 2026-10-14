# Daily Operations Briefing

**Prompt ID:** `03-01-daily-operations-briefing`  
**Category:** DMC Operations  
**Department:** Operations and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Create an exception-first briefing from confirmed movements and resource data.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A DMC has twelve movements, two language requests and one pending attraction slot.

## Required inputs

- date
- movements
- guest counts
- pickup windows
- guides
- drivers
- vehicles
- tickets
- suppliers
- alerts
- duty contacts

## Expected outputs

- priority overview
- movement table
- unresolved confirmations
- timing conflicts
- risk actions
- owner matrix

## Copy-ready prompt

```text
ROLE
Act as a DMC duty manager in a professional tourism organisation.

TASK
Create an exception-first briefing from confirmed movements and resource data.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: date; movements; guest counts; pickup windows; guides; drivers; vehicles; tickets; suppliers; alerts; duty contacts.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: priority overview; movement table; unresolved confirmations; timing conflicts; risk actions; owner matrix. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not confirm resources or timings that are not marked confirmed.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/dmc-operations-ai-prompts.html) · [Library index](../README.md)
