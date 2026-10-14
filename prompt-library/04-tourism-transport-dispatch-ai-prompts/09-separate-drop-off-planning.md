# Separate Drop-Off Planning

**Prompt ID:** `04-09-separate-drop-off-planning`  
**Category:** Transport and Dispatch  
**Department:** Fleet, Transport and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Design a controlled multi-drop return plan after a shared tour.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A shared evening tour ends with city hotels, Yas hotels and an airport passenger.

## Required inputs

- drop-off locations
- guest groups anonymised
- time constraints
- route evidence
- guide position
- vehicle hours
- safety rules
- luggage

## Expected outputs

- drop order
- estimated draft windows
- handover points
- guest communication
- exceptions
- final confirmation list

## Copy-ready prompt

```text
ROLE
Act as a guest movement planner in a professional tourism organisation.

TASK
Design a controlled multi-drop return plan after a shared tour.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: drop-off locations; guest groups anonymised; time constraints; route evidence; guide position; vehicle hours; safety rules; luggage.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: drop order; estimated draft windows; handover points; guest communication; exceptions; final confirmation list. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not change a contracted drop-off or split guests without approval.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-transport-dispatch-ai-prompts.html) · [Library index](../README.md)
