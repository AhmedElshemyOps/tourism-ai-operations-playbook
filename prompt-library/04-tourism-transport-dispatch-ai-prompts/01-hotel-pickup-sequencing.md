# Hotel Pickup Sequencing

**Prompt ID:** `04-01-hotel-pickup-sequencing`  
**Category:** Transport and Dispatch  
**Department:** Fleet, Transport and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Propose a pickup sequence that protects the confirmed arrival commitment.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** Eight hotels must feed one city tour with a fixed attraction slot.

## Required inputs

- hotels with verified coordinates
- pickup window
- guest count
- loading time
- attraction arrival
- route evidence
- vehicle
- access notes

## Expected outputs

- sequence table
- reason
- pickup times as proposals
- total buffer
- risk flags
- verification list

## Copy-ready prompt

```text
ROLE
Act as a tourism transport planner in a professional tourism organisation.

TASK
Propose a pickup sequence that protects the confirmed arrival commitment.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: hotels with verified coordinates; pickup window; guest count; loading time; attraction arrival; route evidence; vehicle; access notes.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: sequence table; reason; pickup times as proposals; total buffer; risk flags; verification list. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not invent locations or live traffic. Mark all times as draft until dispatcher verification.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-transport-dispatch-ai-prompts.html) · [Library index](../README.md)
