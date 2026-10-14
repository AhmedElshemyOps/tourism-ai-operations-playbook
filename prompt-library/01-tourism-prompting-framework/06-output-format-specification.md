# Output-Format Specification

**Prompt ID:** `01-06-output-format-specification`  
**Category:** Prompt Engineering  
**Department:** Cross-functional Tourism Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Design the exact output structure an ai should follow so the result can enter a tourism workflow with minimal rework.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A duty manager wants every handover summary to follow the same exception-first structure.

## Required inputs

- business task
- receiving role
- channel
- required sections
- length
- tone
- fields
- priority logic
- template examples

## Expected outputs

- numbered output specification
- mandatory fields
- optional fields
- validation rules
- rejected-output conditions

## Copy-ready prompt

```text
ROLE
Act as a tourism workflow designer in a professional tourism organisation.

TASK
Design the exact output structure an ai should follow so the result can enter a tourism workflow with minimal rework.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: business task; receiving role; channel; required sections; length; tone; fields; priority logic; template examples.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: numbered output specification; mandatory fields; optional fields; validation rules; rejected-output conditions. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not write the final business content; define the controlled format and acceptance criteria.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-prompting-framework.html) · [Library index](../README.md)
