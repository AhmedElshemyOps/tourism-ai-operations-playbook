# Service-Recovery Plan

**Prompt ID:** `08-06-service-recovery-plan`  
**Category:** Guest Experience  
**Department:** Customer Experience and Service Recovery  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Design a proportionate recovery plan that restores control and protects future trust.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A private tour uses the wrong language guide and replacement is possible after one hour.

## Required inputs

- failure
- affected guests
- severity
- immediate safety
- confirmed facts
- available remedies
- authority
- supplier role
- communication
- prevention

## Expected outputs

- stabilisation
- guest options
- decision authority
- message plan
- documentation
- follow-up
- prevention owner

## Copy-ready prompt

```text
ROLE
Act as a guest experience recovery manager in a professional tourism organisation.

TASK
Design a proportionate recovery plan that restores control and protects future trust.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: failure; affected guests; severity; immediate safety; confirmed facts; available remedies; authority; supplier role; communication; prevention.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: stabilisation; guest options; decision authority; message plan; documentation; follow-up; prevention owner. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Escalate safety, discrimination, privacy or major financial cases immediately.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/guest-experience-ai-prompts.html) · [Library index](../README.md)
