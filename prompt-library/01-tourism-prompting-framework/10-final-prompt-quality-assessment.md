# Final Prompt-Quality Assessment

**Prompt ID:** `01-10-final-prompt-quality-assessment`  
**Category:** Prompt Engineering  
**Department:** Cross-functional Tourism Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Score a completed prompt against the travel framework and decide whether it is ready for controlled use.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A company wants to approve a pre-arrival message prompt for its central library.

## Required inputs

- final prompt
- use case
- department
- test outputs
- reviewer feedback
- risk level
- approved tools

## Expected outputs

- scorecard
- pass/fail by criterion
- critical defects
- improvement actions
- version recommendation

## Copy-ready prompt

```text
ROLE
Act as a tourism training assessor in a professional tourism organisation.

TASK
Score a completed prompt against the travel framework and decide whether it is ready for controlled use.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: final prompt; use case; department; test outputs; reviewer feedback; risk level; approved tools.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: scorecard; pass/fail by criterion; critical defects; improvement actions; version recommendation. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
A high overall score cannot override a critical privacy, safety, commercial or verification failure.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-prompting-framework.html) · [Library index](../README.md)
