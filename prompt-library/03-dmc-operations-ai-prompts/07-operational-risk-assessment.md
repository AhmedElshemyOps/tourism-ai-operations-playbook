# Operational Risk Assessment

**Prompt ID:** `03-07-operational-risk-assessment`  
**Category:** DMC Operations  
**Department:** Operations and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Assess a day of operations using likelihood, impact, detectability and control readiness.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A desert operation faces high temperature, a late flight and limited backup vehicles.

## Required inputs

- movement plan
- guest profile
- weather and event alerts
- suppliers
- resources
- known issues
- contingency
- escalation

## Expected outputs

- risk register
- top risks
- preventive controls
- trigger points
- owners
- residual risk

## Copy-ready prompt

```text
ROLE
Act as a tourism operations risk facilitator in a professional tourism organisation.

TASK
Assess a day of operations using likelihood, impact, detectability and control readiness.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: movement plan; guest profile; weather and event alerts; suppliers; resources; known issues; contingency; escalation.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: risk register; top risks; preventive controls; trigger points; owners; residual risk. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not down-score a risk because a control is only planned rather than confirmed.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/dmc-operations-ai-prompts.html) · [Library index](../README.md)
