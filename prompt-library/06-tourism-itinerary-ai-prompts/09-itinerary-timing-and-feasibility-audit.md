# Itinerary Timing and Feasibility Audit

**Prompt ID:** `06-09-itinerary-timing-and-feasibility-audit`  
**Category:** Itinerary Planning  
**Department:** Product, Reservations and Operations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Stress-test an itinerary leg by leg before release.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A sales itinerary has six stops in nine hours and an airport drop-off.

## Required inputs

- draft itinerary
- verified hours
- tickets
- travel-time sources
- group size
- vehicle
- walking
- entry
- meals
- service window
- rules

## Expected outputs

- leg audit
- unrealistic timings
- missing buffers
- critical path
- corrections
- release recommendation

## Copy-ready prompt

```text
ROLE
Act as a senior DMC operations auditor in a professional tourism organisation.

TASK
Stress-test an itinerary leg by leg before release.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: draft itinerary; verified hours; tickets; travel-time sources; group size; vehicle; walking; entry; meals; service window; rules.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: leg audit; unrealistic timings; missing buffers; critical path; corrections; release recommendation. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Any missing dynamic fact must remain a blocker or explicit verification action.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-itinerary-ai-prompts.html) · [Library index](../README.md)
