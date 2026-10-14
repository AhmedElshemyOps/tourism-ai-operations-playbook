# Prompt-Library Governance

**Prompt ID:** `10-06-prompt-library-governance`  
**Category:** Responsible AI Governance  
**Department:** Management, Quality, Privacy and AI Governance  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Design governance for an approved prompt library across departments.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A travel company has 60 prompts created informally by employees.

## Required inputs

- departments
- use cases
- roles
- risk tiers
- repository
- access
- versioning
- tests
- review cadence
- retirement
- audit needs

## Expected outputs

- operating model
- metadata standard
- workflow
- access matrix
- version control
- review
- retirement
- KPIs

## Copy-ready prompt

```text
ROLE
Act as a tourism knowledge and AI controls manager in a professional tourism organisation.

TASK
Design governance for an approved prompt library across departments.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: departments; use cases; roles; risk tiers; repository; access; versioning; tests; review cadence; retirement; audit needs.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: operating model; metadata standard; workflow; access matrix; version control; review; retirement; KPIs. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not allow unrestricted editing of approved high-risk prompts.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/responsible-ai-tourism-guide.html) · [Library index](../README.md)
