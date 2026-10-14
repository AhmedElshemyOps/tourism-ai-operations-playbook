# Child-Seat and Accessibility Checks

**Prompt ID:** `04-06-child-seat-and-accessibility-checks`  
**Category:** Transport and Dispatch  
**Department:** Fleet, Transport and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Build a mandatory readiness check for child restraints and mobility needs.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A family and a wheelchair user are booked on the same private vehicle.

## Required inputs

- guest requirements confirmed
- ages or restraint category
- wheelchair dimensions
- transfer ability
- assistance
- vehicle
- supplier confirmation
- policy

## Expected outputs

- requirement summary
- confirmation questions
- fit check
- loading plan
- unresolved safety items
- no-go conditions

## Copy-ready prompt

```text
ROLE
Act as a accessible transport coordinator in a professional tourism organisation.

TASK
Build a mandatory readiness check for child restraints and mobility needs.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: guest requirements confirmed; ages or restraint category; wheelchair dimensions; transfer ability; assistance; vehicle; supplier confirmation; policy.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: requirement summary; confirmation questions; fit check; loading plan; unresolved safety items; no-go conditions. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Never infer requirements from appearance or age alone; obtain direct and approved confirmation.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-transport-dispatch-ai-prompts.html) · [Library index](../README.md)
