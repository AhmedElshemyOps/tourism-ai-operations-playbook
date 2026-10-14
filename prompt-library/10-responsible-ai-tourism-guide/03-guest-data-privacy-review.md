# Guest-Data Privacy Review

**Prompt ID:** `10-03-guest-data-privacy-review`  
**Category:** Responsible AI Governance  
**Department:** Management, Quality, Privacy and AI Governance  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Check whether an ai workflow uses the minimum necessary guest data and approved controls.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A complaint-analysis workflow would process emails and booking notes.

## Required inputs

- purpose
- data fields
- sensitivity
- source
- tool
- account
- location
- retention
- access
- sharing
- deletion
- alternatives

## Expected outputs

- data inventory
- necessity test
- prohibited fields
- de-identification
- access controls
- retention questions
- escalation

## Copy-ready prompt

```text
ROLE
Act as a tourism privacy operations coordinator in a professional tourism organisation.

TASK
Check whether an ai workflow uses the minimum necessary guest data and approved controls.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: purpose; data fields; sensitivity; source; tool; account; location; retention; access; sharing; deletion; alternatives.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: data inventory; necessity test; prohibited fields; de-identification; access controls; retention questions; escalation. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not provide legal conclusions; refer jurisdiction-specific questions to qualified counsel.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/responsible-ai-tourism-guide.html) · [Library index](../README.md)
