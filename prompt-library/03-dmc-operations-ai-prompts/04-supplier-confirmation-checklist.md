# Supplier Confirmation Checklist

**Prompt ID:** `03-04-supplier-confirmation-checklist`  
**Category:** DMC Operations  
**Department:** Operations and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Build a service-specific confirmation checklist and follow-up tracker.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** Operations needs final confirmation from a restaurant and attraction for a 40-person group.

## Required inputs

- service type
- booking details
- supplier
- contracted inclusions
- service date
- contact channel
- cut-off
- special requirements

## Expected outputs

- confirmation message
- checklist
- pending items
- deadline
- escalation trigger
- evidence field

## Copy-ready prompt

```text
ROLE
Act as a supplier coordination supervisor in a professional tourism organisation.

TASK
Build a service-specific confirmation checklist and follow-up tracker.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: service type; booking details; supplier; contracted inclusions; service date; contact channel; cut-off; special requirements.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: confirmation message; checklist; pending items; deadline; escalation trigger; evidence field. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not insert rates or terms that were not supplied and authorised.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/dmc-operations-ai-prompts.html) · [Library index](../README.md)
