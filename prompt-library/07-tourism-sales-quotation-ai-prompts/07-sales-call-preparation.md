# Sales-Call Preparation

**Prompt ID:** `07-07-sales-call-preparation`  
**Category:** Sales and Quotation  
**Department:** B2B Sales, Contracting and Quotations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Create a fact-based call plan for a specific tourism opportunity.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** An account manager prepares for a call about low conversion on a proposal.

## Required inputs

- client
- history
- opportunity
- proposal
- stakeholders
- approved commercial boundaries
- objections
- proof
- desired decision

## Expected outputs

- call objective
- opening
- questions
- value points
- objection notes
- boundaries
- close
- follow-up record

## Copy-ready prompt

```text
ROLE
Act as a senior travel account director in a professional tourism organisation.

TASK
Create a fact-based call plan for a specific tourism opportunity.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: client; history; opportunity; proposal; stakeholders; approved commercial boundaries; objections; proof; desired decision.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: call objective; opening; questions; value points; objection notes; boundaries; close; follow-up record. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not invent client priorities or authorise discounts.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-sales-quotation-ai-prompts.html) · [Library index](../README.md)
