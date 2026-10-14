# Vehicle Selection by Passenger Capacity

**Prompt ID:** `04-03-vehicle-selection-by-passenger-capacity`  
**Category:** Transport and Dispatch  
**Department:** Fleet, Transport and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Shortlist compliant vehicle categories for a confirmed movement.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A private airport transfer has six guests, nine bags, one infant and a guide.

## Required inputs

- passengers
- infants
- child seats
- luggage
- wheelchairs
- equipment
- guide seat
- vehicle capacities
- road and access rules

## Expected outputs

- capacity calculation
- suitable categories
- excluded categories
- required equipment
- confirmation checklist

## Copy-ready prompt

```text
ROLE
Act as a fleet allocation specialist in a professional tourism organisation.

TASK
Shortlist compliant vehicle categories for a confirmed movement.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: passengers; infants; child seats; luggage; wheelchairs; equipment; guide seat; vehicle capacities; road and access rules.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: capacity calculation; suitable categories; excluded categories; required equipment; confirmation checklist. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Never exceed approved capacity or assume a foldable mobility device fits.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-transport-dispatch-ai-prompts.html) · [Library index](../README.md)
