# Tour Quotation Structure

**Prompt ID:** `07-01-tour-quotation-structure`  
**Category:** Sales and Quotation  
**Department:** B2B Sales, Contracting and Quotations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Build a professional quotation structure around approved commercial inputs.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A DMC prepares a three-day group quotation for an overseas tour operator.

## Required inputs

- client
- request
- itinerary
- approved net costs
- pricing output supplied
- inclusions
- exclusions
- validity
- terms
- pending confirmations

## Expected outputs

- cover summary
- programme
- price table placeholders
- inclusions
- exclusions
- conditions
- next step
- approval checklist

## Copy-ready prompt

```text
ROLE
Act as a tourism quotation specialist in a professional tourism organisation.

TASK
Build a professional quotation structure around approved commercial inputs.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: client; request; itinerary; approved net costs; pricing output supplied; inclusions; exclusions; validity; terms; pending confirmations.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: cover summary; programme; price table placeholders; inclusions; exclusions; conditions; next step; approval checklist. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not calculate or invent rates, margin, tax, currency or terms.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-sales-quotation-ai-prompts.html) · [Library index](../README.md)
