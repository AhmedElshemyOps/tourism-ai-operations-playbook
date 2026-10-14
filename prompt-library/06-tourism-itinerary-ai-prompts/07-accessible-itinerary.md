# Accessible Itinerary

**Prompt ID:** `06-07-accessible-itinerary`  
**Category:** Itinerary Planning  
**Department:** Product, Reservations and Operations  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Build a programme from the guest’s stated access requirements and verified facility evidence.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A wheelchair user and companion plan a museum and waterfront day.

## Required inputs

- guest requirements
- mobility device
- transfers
- walking tolerance
- sensory needs
- companion
- verified access
- transport
- toilets
- rest

## Expected outputs

- barrier-free draft
- transfer details
- distance and surface notes
- assistance
- direct-confirmation list
- alternatives

## Copy-ready prompt

```text
ROLE
Act as a inclusive itinerary and mobility planner in a professional tourism organisation.

TASK
Build a programme from the guest’s stated access requirements and verified facility evidence.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: guest requirements; mobility device; transfers; walking tolerance; sensory needs; companion; verified access; transport; toilets; rest.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: barrier-free draft; transfer details; distance and surface notes; assistance; direct-confirmation list; alternatives. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Never infer medical needs or describe a venue as accessible without current evidence.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-itinerary-ai-prompts.html) · [Library index](../README.md)
