# Prompt Improvement and Rewriting

**Prompt ID:** `01-02-prompt-improvement-and-rewriting`  
**Category:** Prompt Engineering  
**Department:** Cross-functional Tourism Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Diagnose and rebuild an existing prompt so it is specific, reviewable and safe for tourism operations.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A transport team’s one-line route prompt keeps returning unrealistic pickup plans.

## Required inputs

- original prompt
- intended task
- expected user
- known failure
- approved information
- prohibited data
- desired output

## Expected outputs

- weakness analysis
- revised prompt
- change log
- test cases
- reviewer checklist

## Copy-ready prompt

```text
ROLE
Act as a tourism operations editor and prompt engineer in a professional tourism organisation.

TASK
Diagnose and rebuild an existing prompt so it is specific, reviewable and safe for tourism operations.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: original prompt; intended task; expected user; known failure; approved information; prohibited data; desired output.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: weakness analysis; revised prompt; change log; test cases; reviewer checklist. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Preserve the user’s legitimate objective while removing ambiguity, hidden assumptions and unsafe instructions.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-prompting-framework.html) · [Library index](../README.md)
