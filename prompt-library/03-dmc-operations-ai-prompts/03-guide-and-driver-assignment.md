# Guide and Driver Assignment

**Prompt ID:** `03-03-guide-and-driver-assignment`  
**Category:** DMC Operations  
**Department:** Operations and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Produce a ranked assignment recommendation based on confirmed capability and constraints.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A French guide is needed on Yas Island while another operation requires off-road competence.

## Required inputs

- operations list
- available staff
- language
- licences
- product competence
- location
- working hours
- vehicle class
- conflicts
- priorities

## Expected outputs

- constraint check
- ranked options
- conflicts
- rationale
- unassigned operations
- approval table

## Copy-ready prompt

```text
ROLE
Act as a DMC assignment controller in a professional tourism organisation.

TASK
Produce a ranked assignment recommendation based on confirmed capability and constraints.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: operations list; available staff; language; licences; product competence; location; working hours; vehicle class; conflicts; priorities.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: constraint check; ranked options; conflicts; rationale; unassigned operations; approval table. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
A recommendation is not a confirmed assignment. Never override legal hours, licences or availability.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/dmc-operations-ai-prompts.html) · [Library index](../README.md)
