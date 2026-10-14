# Multi-Day Destination Programme

**Prompt ID:** `06-02-multi-day-destination-programme`  
**Category:** Itinerary Planning  
**Department:** Product, Reservations and Operations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Sequence a multi-day programme with progressive pacing and efficient geography.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A five-night group combines culture, desert, Yas Island and free time.

## Required inputs

- dates
- nights
- hotels
- flights
- segments
- confirmed attractions
- transfers
- meals
- free time
- special needs
- supplier status

## Expected outputs

- day-by-day flow
- daily themes
- logistics table
- energy curve
- confirmations
- alternatives

## Copy-ready prompt

```text
ROLE
Act as a DMC programme designer in a professional tourism organisation.

TASK
Sequence a multi-day programme with progressive pacing and efficient geography.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: dates; nights; hotels; flights; segments; confirmed attractions; transfers; meals; free time; special needs; supplier status.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: day-by-day flow; daily themes; logistics table; energy curve; confirmations; alternatives. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Keep arrival and departure days realistic and flag every unconfirmed component.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-itinerary-ai-prompts.html) · [Library index](../README.md)
