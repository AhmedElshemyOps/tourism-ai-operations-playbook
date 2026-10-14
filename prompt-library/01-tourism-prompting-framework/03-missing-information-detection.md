# Missing-Information Detection

**Prompt ID:** `01-03-missing-information-detection`  
**Category:** Prompt Engineering  
**Department:** Cross-functional Tourism Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Review a planned ai task and identify every missing input that could affect safety, timing, guest expectation, cost or service delivery.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A coordinator asks for a daily briefing but has not supplied the attraction slot or vehicle confirmation.

## Required inputs

- draft request
- tour file extract
- confirmed inputs
- source systems
- decision required
- operating deadline

## Expected outputs

- critical missing data
- important missing data
- optional enhancements
- owner and source for each item

## Copy-ready prompt

```text
ROLE
Act as a tourism operations control specialist in a professional tourism organisation.

TASK
Review a planned ai task and identify every missing input that could affect safety, timing, guest expectation, cost or service delivery.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: draft request; tour file extract; confirmed inputs; source systems; decision required; operating deadline.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: critical missing data; important missing data; optional enhancements; owner and source for each item. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not solve the task. Stop after producing the information request and prioritisation.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-prompting-framework.html) · [Library index](../README.md)
