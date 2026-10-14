# Corrective and Preventive Action Planning

**Prompt ID:** `09-07-corrective-and-preventive-action-planning`  
**Category:** Quality and SOP  
**Department:** Quality, Training and Operational Excellence  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Create a controlled capa plan after a supported root-cause finding.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** An attraction voucher error recurs across two products.

## Required inputs

- incident
- root cause
- affected processes
- immediate correction
- risk
- proposed actions
- owners
- resources
- measures
- due dates

## Expected outputs

- correction
- corrective actions
- preventive actions
- owner
- milestone
- verification
- effectiveness check
- closure rule

## Copy-ready prompt

```text
ROLE
Act as a tourism CAPA coordinator in a professional tourism organisation.

TASK
Create a controlled capa plan after a supported root-cause finding.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: incident; root cause; affected processes; immediate correction; risk; proposed actions; owners; resources; measures; due dates.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: correction; corrective actions; preventive actions; owner; milestone; verification; effectiveness check; closure rule. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not close an action because training was delivered; require effectiveness evidence.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-quality-sop-ai-prompts.html) · [Library index](../README.md)
