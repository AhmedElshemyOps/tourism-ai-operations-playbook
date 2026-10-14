# Guest-Feedback Analysis

**Prompt ID:** `08-09-guest-feedback-analysis`  
**Category:** Guest Experience  
**Department:** Customer Experience and Service Recovery  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Analyse anonymised feedback for themes, severity, journey stage and controllable causes.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A DMC reviews 300 comments from tours and transfers.

## Required inputs

- feedback set
- dates
- products
- channels
- rating
- complaint categories
- operational data
- coding rules

## Expected outputs

- theme table
- frequency
- severity
- representative paraphrases
- journey hotspots
- hypotheses
- actions
- data limits

## Copy-ready prompt

```text
ROLE
Act as a tourism voice-of-customer analyst in a professional tourism organisation.

TASK
Analyse anonymised feedback for themes, severity, journey stage and controllable causes.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: feedback set; dates; products; channels; rating; complaint categories; operational data; coding rules.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: theme table; frequency; severity; representative paraphrases; journey hotspots; hypotheses; actions; data limits. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not identify individuals or claim causation from comments alone.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/guest-experience-ai-prompts.html) · [Library index](../README.md)
