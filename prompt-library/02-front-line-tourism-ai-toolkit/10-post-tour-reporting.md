# Post-Tour Reporting

**Prompt ID:** `02-10-post-tour-reporting`  
**Category:** Front-Line Service  
**Department:** Tour Guiding and Guest-Facing Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Convert structured tour notes into a concise evidence-based end-of-tour report.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A guide reports a late departure, a recovered ticket issue and positive feedback about storytelling.

## Required inputs

- tour reference without personal identifiers
- plan
- actual timings
- incidents
- guest feedback
- supplier issues
- unresolved actions
- evidence

## Expected outputs

- executive summary
- timing variance
- guest-experience notes
- incident log
- follow-up owners
- improvement suggestions

## Copy-ready prompt

```text
ROLE
Act as a guide operations reporting coach in a professional tourism organisation.

TASK
Convert structured tour notes into a concise evidence-based end-of-tour report.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: tour reference without personal identifiers; plan; actual timings; incidents; guest feedback; supplier issues; unresolved actions; evidence.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: executive summary; timing variance; guest-experience notes; incident log; follow-up owners; improvement suggestions. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Separate observed facts, guest statements and guide interpretation.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/front-line-tourism-ai-toolkit.html) · [Library index](../README.md)
