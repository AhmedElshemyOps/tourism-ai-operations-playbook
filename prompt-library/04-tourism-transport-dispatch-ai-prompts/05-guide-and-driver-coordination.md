# Guide and Driver Coordination

**Prompt ID:** `04-05-guide-and-driver-coordination`  
**Category:** Transport and Dispatch  
**Department:** Fleet, Transport and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Define the handovers and communication points between guide and driver.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A large coach tour requires remote parking and timed guide-driver reconnection.

## Required inputs

- movement plan
- guide
- driver
- vehicle
- pickup roles
- parking rules
- guest count
- attraction process
- communication channel

## Expected outputs

- pre-service check
- meeting points
- communication timeline
- responsibility matrix
- lost-contact protocol

## Copy-ready prompt

```text
ROLE
Act as a tour movement coordinator in a professional tourism organisation.

TASK
Define the handovers and communication points between guide and driver.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: movement plan; guide; driver; vehicle; pickup roles; parking rules; guest count; attraction process; communication channel.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: pre-service check; meeting points; communication timeline; responsibility matrix; lost-contact protocol. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not assign tasks that conflict with licence, safety or company role definitions.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-transport-dispatch-ai-prompts.html) · [Library index](../README.md)
