# SOP Review and Improvement

**Prompt ID:** `09-02-sop-review-and-improvement`  
**Category:** Quality and SOP  
**Department:** Quality, Training and Operational Excellence  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Audit an existing sop against actual practice, risk and usability.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A pickup SOP no longer matches the dispatch application used by the team.

## Required inputs

- current SOP
- observation notes
- employee feedback
- incidents
- system changes
- policy
- metrics
- version history

## Expected outputs

- gap matrix
- obsolete steps
- hidden work
- control failures
- revised sections
- validation plan

## Copy-ready prompt

```text
ROLE
Act as a tourism quality manager in a professional tourism organisation.

TASK
Audit an existing sop against actual practice, risk and usability.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: current SOP; observation notes; employee feedback; incidents; system changes; policy; metrics; version history.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: gap matrix; obsolete steps; hidden work; control failures; revised sections; validation plan. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not change controlled requirements without authorised review.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-quality-sop-ai-prompts.html) · [Library index](../README.md)
