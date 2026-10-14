# Product Feasibility Assessment

**Prompt ID:** `05-10-product-feasibility-assessment`  
**Category:** Product Development  
**Department:** Tourism Product and Destination Management  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Assess whether a product is ready for pilot, revision or rejection.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A new sunrise desert product reaches the final concept-approval meeting.

## Required inputs

- concept
- guest need
- itinerary
- suppliers
- capacity
- skills
- transport
- safety
- costing status
- demand evidence
- contingency

## Expected outputs

- scorecard
- critical blockers
- assumptions
- pilot requirements
- owners
- gate decision recommendation

## Copy-ready prompt

```text
ROLE
Act as a cross-functional tourism product gate reviewer in a professional tourism organisation.

TASK
Assess whether a product is ready for pilot, revision or rejection.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: concept; guest need; itinerary; suppliers; capacity; skills; transport; safety; costing status; demand evidence; contingency.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: scorecard; critical blockers; assumptions; pilot requirements; owners; gate decision recommendation. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
A positive concept score cannot override an unresolved safety, legal, capacity or supplier blocker.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-product-development-ai-prompts.html) · [Library index](../README.md)
