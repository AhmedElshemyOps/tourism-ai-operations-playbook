# Family Itinerary

**Prompt ID:** `06-05-family-itinerary`  
**Category:** Itinerary Planning  
**Department:** Product, Reservations and Operations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Create a comfortable programme that balances adult interest, child engagement and rest.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** Parents with two children want a two-day city and theme-park programme.

## Required inputs

- family composition
- ages
- routines
- interests
- date
- hotel
- verified attractions
- meal needs
- stroller
- transport
- budget

## Expected outputs

- paced itinerary
- engagement ideas
- rest and toilet points
- packing
- safety
- backup

## Copy-ready prompt

```text
ROLE
Act as a family travel itinerary specialist in a professional tourism organisation.

TASK
Create a comfortable programme that balances adult interest, child engagement and rest.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: family composition; ages; routines; interests; date; hotel; verified attractions; meal needs; stroller; transport; budget.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: paced itinerary; engagement ideas; rest and toilet points; packing; safety; backup. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not assume age automatically determines ability or interest.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-itinerary-ai-prompts.html) · [Library index](../README.md)
