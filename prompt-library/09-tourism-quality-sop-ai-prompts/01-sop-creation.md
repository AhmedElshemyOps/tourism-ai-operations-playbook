# SOP Creation

**Prompt ID:** `09-01-sop-creation`  
**Category:** Quality and SOP  
**Department:** Quality, Training and Operational Excellence  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Create a field-ready sop from a verified current process and control requirements.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A DMC documents its airport representative arrival process.

## Required inputs

- process purpose
- trigger
- scope
- roles
- observed steps
- systems
- forms
- timing
- exceptions
- safety
- approvals
- records

## Expected outputs

- document control
- purpose
- roles
- step table
- decision points
- exceptions
- records
- KPIs
- training
- review

## Copy-ready prompt

```text
ROLE
Act as a tourism process owner and SOP facilitator in a professional tourism organisation.

TASK
Create a field-ready sop from a verified current process and control requirements.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: process purpose; trigger; scope; roles; observed steps; systems; forms; timing; exceptions; safety; approvals; records.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: document control; purpose; roles; step table; decision points; exceptions; records; KPIs; training; review. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not invent steps. Mark every area requiring observation or process-owner validation.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-quality-sop-ai-prompts.html) · [Library index](../README.md)
