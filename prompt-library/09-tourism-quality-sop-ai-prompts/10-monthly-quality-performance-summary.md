# Monthly Quality-Performance Summary

**Prompt ID:** `09-10-monthly-quality-performance-summary`  
**Category:** Quality and SOP  
**Department:** Quality, Training and Operational Excellence  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Prepare a management summary from verified operational and guest-experience evidence.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A DMC quality manager reports to operations and product leaders.

## Required inputs

- month
- KPIs
- targets
- incidents
- complaints
- audits
- CAPA
- supplier issues
- training
- prior trend
- data quality

## Expected outputs

- executive summary
- KPI table
- trend
- top risks
- successes
- overdue actions
- next-month priorities
- caveats

## Copy-ready prompt

```text
ROLE
Act as a tourism quality performance analyst in a professional tourism organisation.

TASK
Prepare a management summary from verified operational and guest-experience evidence.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: month; KPIs; targets; incidents; complaints; audits; CAPA; supplier issues; training; prior trend; data quality.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: executive summary; KPI table; trend; top risks; successes; overdue actions; next-month priorities; caveats. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not hide low sample sizes or combine unlike measures.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-quality-sop-ai-prompts.html) · [Library index](../README.md)
