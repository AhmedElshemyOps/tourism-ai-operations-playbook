# What-to-Bring Reminder

**Prompt ID:** `08-03-what-to-bring-reminder`  
**Category:** Guest Experience  
**Department:** Customer Experience and Service Recovery  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Create a practical reminder based only on verified activity requirements.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** Guests prepare for a desert safari followed by dinner.

## Required inputs

- activity
- date
- weather source
- supplier requirements
- dress code
- footwear
- documents
- health/safety guidance approved
- storage
- prohibited items

## Expected outputs

- priority packing list
- mandatory versus recommended
- reason
- guest questions
- verification date

## Copy-ready prompt

```text
ROLE
Act as a tour experience preparation specialist in a professional tourism organisation.

TASK
Create a practical reminder based only on verified activity requirements.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: activity; date; weather source; supplier requirements; dress code; footwear; documents; health/safety guidance approved; storage; prohibited items.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: priority packing list; mandatory versus recommended; reason; guest questions; verification date. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not give medical advice or invent supplier restrictions.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/guest-experience-ai-prompts.html) · [Library index](../README.md)
