# AI Output Verification

**Prompt ID:** `10-02-ai-output-verification`  
**Category:** Responsible AI Governance  
**Department:** Management, Quality, Privacy and AI Governance  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Verify a material ai output against supplied approved evidence and release criteria.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** An AI-generated itinerary is being prepared for a client proposal.

## Required inputs

- prompt version
- output
- source pack
- dynamic facts
- business rules
- intended use
- reviewer competence
- deadline

## Expected outputs

- claim register
- source match
- uncertainty
- contradictions
- correction
- final human decision record

## Copy-ready prompt

```text
ROLE
Act as a tourism AI assurance reviewer in a professional tourism organisation.

TASK
Verify a material ai output against supplied approved evidence and release criteria.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: prompt version; output; source pack; dynamic facts; business rules; intended use; reviewer competence; deadline.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: claim register; source match; uncertainty; contradictions; correction; final human decision record. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Fluency and confidence are not evidence.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/responsible-ai-tourism-guide.html) · [Library index](../README.md)
