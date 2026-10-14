# Cruise-Passenger Itinerary

**Prompt ID:** `06-04-cruise-passenger-itinerary`  
**Category:** Itinerary Planning  
**Department:** Product, Reservations and Operations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Prepare a shore programme that protects all-aboard time and port procedures.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A private shore excursion visits a mosque, museum and market.

## Required inputs

- ship date
- berth
- disembarkation estimate
- all-aboard
- guest profile
- verified sites
- transport
- group size
- port rules

## Expected outputs

- critical timeline
- route
- buffers
- guide/driver coordination
- fallback levels
- return decision points

## Copy-ready prompt

```text
ROLE
Act as a shore excursion operations planner in a professional tourism organisation.

TASK
Prepare a shore programme that protects all-aboard time and port procedures.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: ship date; berth; disembarkation estimate; all-aboard; guest profile; verified sites; transport; group size; port rules.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: critical timeline; route; buffers; guide/driver coordination; fallback levels; return decision points. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Never use scheduled docking alone as a guaranteed guest-ready time.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-itinerary-ai-prompts.html) · [Library index](../README.md)
