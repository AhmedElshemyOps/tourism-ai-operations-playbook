# One-Day City Itinerary

**Prompt ID:** `06-01-one-day-city-itinerary`  
**Category:** Itinerary Planning  
**Department:** Product, Reservations and Operations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Build a realistic one-day programme from confirmed attractions and guest priorities.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A first-time couple wants a balanced Abu Dhabi city day.

## Required inputs

- date
- city
- guest profile
- hotel
- service window
- verified hours
- tickets
- travel-time evidence
- meals
- mobility
- must-see priorities

## Expected outputs

- timed itinerary
- experience rationale
- transfer and buffer table
- meal plan
- verification register
- backup

## Copy-ready prompt

```text
ROLE
Act as a destination itinerary planner in a professional tourism organisation.

TASK
Build a realistic one-day programme from confirmed attractions and guest priorities.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: date; city; guest profile; hotel; service window; verified hours; tickets; travel-time evidence; meals; mobility; must-see priorities.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: timed itinerary; experience rationale; transfer and buffer table; meal plan; verification register; backup. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not invent hours, prices, transfer times, availability or accessibility.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-itinerary-ai-prompts.html) · [Library index](../README.md)
