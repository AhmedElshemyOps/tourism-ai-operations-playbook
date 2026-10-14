# Existing-Product Review

**Prompt ID:** `05-02-existing-product-review`  
**Category:** Product Development  
**Department:** Tourism Product and Destination Management  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Diagnose an existing tour using guest value, delivery, commercial and partner evidence.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A city tour sells well but receives repeated comments about rushing.

## Required inputs

- product description
- itinerary
- sales
- feedback
- incidents
- costs allowed
- supplier performance
- competitor evidence
- objectives

## Expected outputs

- strengths
- friction points
- evidence table
- redesign options
- quick wins
- test plan

## Copy-ready prompt

```text
ROLE
Act as a tourism product performance reviewer in a professional tourism organisation.

TASK
Diagnose an existing tour using guest value, delivery, commercial and partner evidence.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: product description; itinerary; sales; feedback; incidents; costs allowed; supplier performance; competitor evidence; objectives.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: strengths; friction points; evidence table; redesign options; quick wins; test plan. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Separate evidence from interpretation and avoid deleting a component only because feedback volume is low.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-product-development-ai-prompts.html) · [Library index](../README.md)
