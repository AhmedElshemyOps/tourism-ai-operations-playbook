# Fact-Verification Review

**Prompt ID:** `01-08-fact-verification-review`  
**Category:** Prompt Engineering  
**Department:** Cross-functional Tourism Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Review an ai-generated tourism output line by line and create an evidence-based verification register.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A draft itinerary contains attraction hours, transfer estimates and accessibility statements.

## Required inputs

- AI output
- supplied sources
- official links
- source dates
- approved internal records
- intended use

## Expected outputs

- claim register
- source status
- dynamic-data flags
- contradictions
- required corrections
- release recommendation

## Copy-ready prompt

```text
ROLE
Act as a tourism information-quality analyst in a professional tourism organisation.

TASK
Review an ai-generated tourism output line by line and create an evidence-based verification register.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: AI output; supplied sources; official links; source dates; approved internal records; intended use.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: claim register; source status; dynamic-data flags; contradictions; required corrections; release recommendation. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not treat repeated online claims as verification. Prefer official, current and approved sources.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-prompting-framework.html) · [Library index](../README.md)
