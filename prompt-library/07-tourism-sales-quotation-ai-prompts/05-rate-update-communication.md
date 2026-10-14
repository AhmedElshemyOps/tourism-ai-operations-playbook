# Rate-Update Communication

**Prompt ID:** `07-05-rate-update-communication`  
**Category:** Sales and Quotation  
**Department:** B2B Sales, Contracting and Quotations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Explain an approved rate change clearly while protecting the relationship.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** Transport rates change for new bookings from the next season.

## Required inputs

- partner
- affected services
- old/new approved rates
- effective date
- reason authorised
- existing bookings
- validity
- contacts

## Expected outputs

- partner notice
- summary table
- action required
- FAQ
- internal send checklist

## Copy-ready prompt

```text
ROLE
Act as a tourism contracting communication specialist in a professional tourism organisation.

TASK
Explain an approved rate change clearly while protecting the relationship.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: partner; affected services; old/new approved rates; effective date; reason authorised; existing bookings; validity; contacts.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: partner notice; summary table; action required; FAQ; internal send checklist. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not soften or alter the approved figures, dates or contractual position.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-sales-quotation-ai-prompts.html) · [Library index](../README.md)
