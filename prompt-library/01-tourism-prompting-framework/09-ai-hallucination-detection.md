# AI Hallucination Detection

**Prompt ID:** `01-09-ai-hallucination-detection`  
**Category:** Prompt Engineering  
**Department:** Cross-functional Tourism Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Challenge an ai output for invented details, unsupported certainty, false precision and hidden assumptions.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A generated product brief includes a supplier capacity and a “guaranteed” view that nobody supplied.

## Required inputs

- prompt
- output
- source pack
- known facts
- operational rules
- confidence requirement

## Expected outputs

- suspected hallucinations
- unsupported claims
- ambiguous claims
- safe rewritten wording
- follow-up questions

## Copy-ready prompt

```text
ROLE
Act as a tourism quality auditor in a professional tourism organisation.

TASK
Challenge an ai output for invented details, unsupported certainty, false precision and hidden assumptions.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: prompt; output; source pack; known facts; operational rules; confidence requirement.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: suspected hallucinations; unsupported claims; ambiguous claims; safe rewritten wording; follow-up questions. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Flag uncertainty rather than guessing whether a claim is true.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-prompting-framework.html) · [Library index](../README.md)
