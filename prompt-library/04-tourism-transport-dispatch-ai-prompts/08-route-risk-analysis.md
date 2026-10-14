# Route-Risk Analysis

**Prompt ID:** `04-08-route-risk-analysis`  
**Category:** Transport and Dispatch  
**Department:** Fleet, Transport and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Challenge a planned route for access, timing and operational failure points.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A coach route crosses an event zone and includes a hotel with restricted bus access.

## Required inputs

- route stops
- vehicle class
- verified travel times
- closures
- event restrictions
- parking
- turning
- loading
- weather
- backup routes

## Expected outputs

- risk-by-leg table
- critical bottlenecks
- verification calls
- backup logic
- dispatcher decision

## Copy-ready prompt

```text
ROLE
Act as a tourism route-risk reviewer in a professional tourism organisation.

TASK
Challenge a planned route for access, timing and operational failure points.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: route stops; vehicle class; verified travel times; closures; event restrictions; parking; turning; loading; weather; backup routes.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: risk-by-leg table; critical bottlenecks; verification calls; backup logic; dispatcher decision. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Use current approved road information; do not claim live conditions from general knowledge.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-transport-dispatch-ai-prompts.html) · [Library index](../README.md)
