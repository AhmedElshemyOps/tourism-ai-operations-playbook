# Tourism Process Mapping

**Prompt ID:** `09-03-tourism-process-mapping`  
**Category:** Quality and SOP  
**Department:** Quality, Training and Operational Excellence  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Map a guest-facing process across roles, handovers and systems.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** The team maps booking handover from sales to operations to the guide.

## Required inputs

- start/end
- customer
- suppliers
- inputs
- observed steps
- decisions
- queues
- systems
- defects
- timing
- owners

## Expected outputs

- SIPOC
- swimlane narrative
- value/non-value analysis
- failure points
- data needs
- future-state questions

## Copy-ready prompt

```text
ROLE
Act as a Lean Six Sigma tourism facilitator in a professional tourism organisation.

TASK
Map a guest-facing process across roles, handovers and systems.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: start/end; customer; suppliers; inputs; observed steps; decisions; queues; systems; defects; timing; owners.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: SIPOC; swimlane narrative; value/non-value analysis; failure points; data needs; future-state questions. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Represent the current state honestly before proposing improvements.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-quality-sop-ai-prompts.html) · [Library index](../README.md)
