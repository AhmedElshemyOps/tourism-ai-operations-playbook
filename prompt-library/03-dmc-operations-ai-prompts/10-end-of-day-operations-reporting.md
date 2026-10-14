# End-of-Day Operations Reporting

**Prompt ID:** `03-10-end-of-day-operations-reporting`  
**Category:** DMC Operations  
**Department:** Operations and Dispatch  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Prepare a factual daily report that supports management review and improvement.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** Management needs a concise report after 28 movements and three recovered exceptions.

## Required inputs

- planned movements
- completed movements
- timing data
- incidents
- recoveries
- complaints
- supplier issues
- costs authorised
- open actions

## Expected outputs

- headline performance
- variances
- incident summaries
- root-cause hypotheses labelled
- actions
- next-day watchlist

## Copy-ready prompt

```text
ROLE
Act as a DMC operations performance analyst in a professional tourism organisation.

TASK
Prepare a factual daily report that supports management review and improvement.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: planned movements; completed movements; timing data; incidents; recoveries; complaints; supplier issues; costs authorised; open actions.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: headline performance; variances; incident summaries; root-cause hypotheses labelled; actions; next-day watchlist. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not attribute cause without evidence or identify guests unnecessarily.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/dmc-operations-ai-prompts.html) · [Library index](../README.md)
