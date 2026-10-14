# Operational Limitation Setting

**Prompt ID:** `01-07-operational-limitation-setting`  
**Category:** Prompt Engineering  
**Department:** Cross-functional Tourism Teams  
**Risk level:** Medium  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Write clear limitations for a prompt so the ai cannot invent, approve or disclose information outside its role.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A sales team uses AI to draft proposals but must protect net rates and payment terms.

## Required inputs

- use case
- data category
- dynamic facts
- commercial authority
- safety implications
- company rules
- approver

## Expected outputs

- prohibited actions
- permitted actions
- uncertainty language
- escalation triggers
- human sign-off

## Copy-ready prompt

```text
ROLE
Act as a tourism risk and compliance reviewer in a professional tourism organisation.

TASK
Write clear limitations for a prompt so the ai cannot invent, approve or disclose information outside its role.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: use case; data category; dynamic facts; commercial authority; safety implications; company rules; approver.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: prohibited actions; permitted actions; uncertainty language; escalation triggers; human sign-off. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Use direct rules. Never phrase a mandatory control as an optional suggestion.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/tourism-prompting-framework.html) · [Library index](../README.md)
