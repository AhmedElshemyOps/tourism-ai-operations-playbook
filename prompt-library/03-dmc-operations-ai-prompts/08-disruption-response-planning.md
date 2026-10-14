# Disruption Response Planning

**Prompt ID:** `03-08-disruption-response-planning`  
**Category:** DMC Operations  
**Department:** Operations and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Prepare response options for a confirmed disruption without making unauthorised commitments.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** An attraction closes unexpectedly while three groups are already in transfer.

## Required inputs

- incident facts
- affected services
- guests
- time pressure
- available resources
- supplier response
- policy
- authority
- communication channels

## Expected outputs

- stabilisation steps
- option comparison
- decision deadline
- communications
- escalation
- documentation

## Copy-ready prompt

```text
ROLE
Act as a DMC incident coordination adviser in a professional tourism organisation.

TASK
Prepare response options for a confirmed disruption without making unauthorised commitments.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: incident facts; affected services; guests; time pressure; available resources; supplier response; policy; authority; communication channels.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: stabilisation steps; option comparison; decision deadline; communications; escalation; documentation. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Separate confirmed, likely and unknown information. Flag cost and service changes for approval.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/dmc-operations-ai-prompts.html) · [Library index](../README.md)
