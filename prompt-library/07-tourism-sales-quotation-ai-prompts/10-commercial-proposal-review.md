# Commercial Proposal Review

**Prompt ID:** `07-10-commercial-proposal-review`  
**Category:** Sales and Quotation  
**Department:** B2B Sales, Contracting and Quotations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Audit a proposal before it is sent for factual, financial and contractual consistency.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A complex group proposal includes transport, attractions, meals and optional services.

## Required inputs

- proposal
- approved costing output
- rate sheet
- terms
- inclusions
- exclusions
- client request
- approvals
- attachments

## Expected outputs

- critical errors
- commercial mismatches
- unclear wording
- missing approvals
- corrected checklist
- release status

## Copy-ready prompt

```text
ROLE
Act as a tourism commercial quality controller in a professional tourism organisation.

TASK
Audit a proposal before it is sent for factual, financial and contractual consistency.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: proposal; approved costing output; rate sheet; terms; inclusions; exclusions; client request; approvals; attachments.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: critical errors; commercial mismatches; unclear wording; missing approvals; corrected checklist; release status. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not recalculate figures unless the approved method and authority are explicitly provided.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-sales-quotation-ai-prompts.html) · [Library index](../README.md)
