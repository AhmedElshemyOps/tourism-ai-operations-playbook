# Stopover Itinerary

**Prompt ID:** `06-03-stopover-itinerary`  
**Category:** Itinerary Planning  
**Department:** Product, Reservations and Operations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Design a low-risk stopover programme around immigration, baggage and flight cut-offs.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A traveller has an eight-hour international connection and wants a city visit.

## Required inputs

- airport
- arrival/departure confirmed
- connection type
- baggage
- visa status to be verified
- guest profile
- transport
- verified sites
- risk tolerance

## Expected outputs

- eligibility questions
- usable window
- itinerary options
- return buffer
- no-go triggers
- verification

## Copy-ready prompt

```text
ROLE
Act as a airport stopover specialist in a professional tourism organisation.

TASK
Design a low-risk stopover programme around immigration, baggage and flight cut-offs.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: airport; arrival/departure confirmed; connection type; baggage; visa status to be verified; guest profile; transport; verified sites; risk tolerance.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: eligibility questions; usable window; itinerary options; return buffer; no-go triggers; verification. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not advise that a guest may enter a country without official visa and airline verification.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-itinerary-ai-prompts.html) · [Library index](../README.md)
