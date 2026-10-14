# AI Use-Case Risk Assessment

**Prompt ID:** `10-01-ai-use-case-risk-assessment`  
**Category:** Responsible AI Governance  
**Department:** Management, Quality, Privacy and AI Governance  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Classify a proposed ai use case and define proportionate controls before approval.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A DMC considers AI-assisted guide assignment recommendations.

## Required inputs

- use case
- users
- affected people
- decision
- data
- tool
- model access
- output destination
- consequences
- frequency
- alternatives

## Expected outputs

- risk classification
- harm scenarios
- privacy
- bias
- accuracy
- security
- controls
- residual risk
- decision gate

## Copy-ready prompt

```text
ROLE
Act as a responsible AI risk lead for a tourism company in a professional tourism organisation.

TASK
Classify a proposed ai use case and define proportionate controls before approval.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: use case; users; affected people; decision; data; tool; model access; output destination; consequences; frequency; alternatives.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: risk classification; harm scenarios; privacy; bias; accuracy; security; controls; residual risk; decision gate. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not approve the use case. Present evidence gaps and required accountable reviewers.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/responsible-ai-tourism-guide.html) · [Library index](../README.md)
