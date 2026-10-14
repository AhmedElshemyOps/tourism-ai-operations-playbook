# Cultural-Sensitivity Review

**Prompt ID:** `10-04-cultural-sensitivity-review`  
**Category:** Responsible AI Governance  
**Department:** Management, Quality, Privacy and AI Governance  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Review ai-generated tourism content for bias, stereotyping, disrespect and context loss.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A guide-training module contains generated examples about local customs.

## Required inputs

- content
- audience
- destination
- language
- cultural guidance
- affected communities
- purpose
- channel

## Expected outputs

- risk passages
- reasons
- respectful alternatives
- facts requiring local review
- accessibility and inclusion notes

## Copy-ready prompt

```text
ROLE
Act as a destination culture and inclusion reviewer in a professional tourism organisation.

TASK
Review ai-generated tourism content for bias, stereotyping, disrespect and context loss.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: content; audience; destination; language; cultural guidance; affected communities; purpose; channel.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: risk passages; reasons; respectful alternatives; facts requiring local review; accessibility and inclusion notes. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not present one reviewer as speaking for an entire culture.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/responsible-ai-tourism-guide.html) · [Library index](../README.md)
