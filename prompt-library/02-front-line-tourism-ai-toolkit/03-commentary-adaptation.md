# Commentary Adaptation

**Prompt ID:** `02-03-commentary-adaptation`  
**Category:** Front-Line Service  
**Department:** Tour Guiding and Guest-Facing Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Adapt approved commentary for a specific group while preserving factual accuracy and cultural respect.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** The same mosque visit must be adapted for school students and architecture professionals.

## Required inputs

- base commentary
- verified facts
- group type
- language level
- interests
- time available
- pace
- sensitive topics

## Expected outputs

- adapted commentary
- changes made
- engagement questions
- details omitted
- verification flags

## Copy-ready prompt

```text
ROLE
Act as a tour guide coach in a professional tourism organisation.

TASK
Adapt approved commentary for a specific group while preserving factual accuracy and cultural respect.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: base commentary; verified facts; group type; language level; interests; time available; pace; sensitive topics.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: adapted commentary; changes made; engagement questions; details omitted; verification flags. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not assume interests from nationality or age. Keep mandatory safety and etiquette wording intact.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/front-line-tourism-ai-toolkit.html) · [Library index](../README.md)
