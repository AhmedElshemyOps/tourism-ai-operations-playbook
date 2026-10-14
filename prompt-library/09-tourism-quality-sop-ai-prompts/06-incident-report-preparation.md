# Incident-Report Preparation

**Prompt ID:** `09-06-incident-report-preparation`  
**Category:** Quality and SOP  
**Department:** Quality, Training and Operational Excellence  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Turn factual notes into a neutral, chronological incident report.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A guest is temporarily separated from a group at a busy attraction.

## Required inputs

- date/time
- location
- people by role or anonymised ID
- observed facts
- actions
- guest impact
- evidence
- notifications
- open items

## Expected outputs

- summary
- chronology
- immediate controls
- statements separated
- evidence list
- escalation
- follow-up

## Copy-ready prompt

```text
ROLE
Act as a tourism incident documentation specialist in a professional tourism organisation.

TASK
Turn factual notes into a neutral, chronological incident report.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: date/time; location; people by role or anonymised ID; observed facts; actions; guest impact; evidence; notifications; open items.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: summary; chronology; immediate controls; statements separated; evidence list; escalation; follow-up. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not speculate, assign blame or remove inconvenient facts.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-quality-sop-ai-prompts.html) · [Library index](../README.md)
