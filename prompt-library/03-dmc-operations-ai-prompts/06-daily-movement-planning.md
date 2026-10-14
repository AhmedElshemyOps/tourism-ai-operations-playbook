# Daily Movement Planning

**Prompt ID:** `03-06-daily-movement-planning`  
**Category:** DMC Operations  
**Department:** Operations and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Turn confirmed services into a coordinated movement plan with handovers and buffers.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** An incentive group splits into two activities and reunites for dinner.

## Required inputs

- service list
- locations
- confirmed times
- pickup windows
- resources
- tickets
- meal slots
- access rules
- buffers
- constraints

## Expected outputs

- chronological movement board
- resource view
- handovers
- critical path
- contingency notes
- approval fields

## Copy-ready prompt

```text
ROLE
Act as a destination operations planner in a professional tourism organisation.

TASK
Turn confirmed services into a coordinated movement plan with handovers and buffers.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: service list; locations; confirmed times; pickup windows; resources; tickets; meal slots; access rules; buffers; constraints.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: chronological movement board; resource view; handovers; critical path; contingency notes; approval fields. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Travel times and access must be supplied or marked for external verification.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/dmc-operations-ai-prompts.html) · [Library index](../README.md)
