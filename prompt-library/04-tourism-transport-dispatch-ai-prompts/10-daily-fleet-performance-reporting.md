# Daily Fleet-Performance Reporting

**Prompt ID:** `04-10-daily-fleet-performance-reporting`  
**Category:** Transport and Dispatch  
**Department:** Fleet, Transport and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Analyse planned versus actual fleet delivery and identify actionable patterns.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A fleet supervisor reviews 35 movements across coaches, minibuses and private vehicles.

## Required inputs

- movements
- planned and actual times
- distance if approved
- vehicle
- capacity
- delays
- cause evidence
- complaints
- recovery
- downtime

## Expected outputs

- KPI table
- variance
- utilisation
- cause categories
- recurring risks
- actions
- data-quality notes

## Copy-ready prompt

```text
ROLE
Act as a tourism fleet performance analyst in a professional tourism organisation.

TASK
Analyse planned versus actual fleet delivery and identify actionable patterns.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: movements; planned and actual times; distance if approved; vehicle; capacity; delays; cause evidence; complaints; recovery; downtime.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: KPI table; variance; utilisation; cause categories; recurring risks; actions; data-quality notes. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not infer driver fault from a delay code alone.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-transport-dispatch-ai-prompts.html) · [Library index](../README.md)
