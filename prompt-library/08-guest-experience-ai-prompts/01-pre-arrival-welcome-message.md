# Pre-Arrival Welcome Message

**Prompt ID:** `08-01-pre-arrival-welcome-message`  
**Category:** Guest Experience  
**Department:** Customer Experience and Service Recovery  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Prepare a clear welcome that sets expectations before arrival.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A small group receives its final welcome message 48 hours before arrival.

## Required inputs

- guest segment anonymised
- destination
- arrival date
- confirmed service
- meeting process
- support channel
- weather source
- cultural notes
- required action

## Expected outputs

- email and chat versions
- action checklist
- timing
- verification notes
- accessible-language review

## Copy-ready prompt

```text
ROLE
Act as a tourism guest-journey communication manager in a professional tourism organisation.

TASK
Prepare a clear welcome that sets expectations before arrival.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: guest segment anonymised; destination; arrival date; confirmed service; meeting process; support channel; weather source; cultural notes; required action.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: email and chat versions; action checklist; timing; verification notes; accessible-language review. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not include unverified visa, weather, transport or attraction information.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/guest-experience-ai-prompts.html) · [Library index](../README.md)
