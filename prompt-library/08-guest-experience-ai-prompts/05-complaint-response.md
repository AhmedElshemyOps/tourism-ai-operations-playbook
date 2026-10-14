# Complaint Response

**Prompt ID:** `08-05-complaint-response`  
**Category:** Guest Experience  
**Department:** Customer Experience and Service Recovery  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Draft a personalised response after reviewing confirmed complaint facts.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** A guest complains that a shared tour departed without enough waiting time.

## Required inputs

- complaint anonymised
- timeline
- evidence
- service standard
- company finding
- guest impact
- authorised remedy
- pending investigation
- tone

## Expected outputs

- acknowledgement
- factual response
- action
- remedy wording
- next step
- privacy check

## Copy-ready prompt

```text
ROLE
Act as a senior tourism customer-care specialist in a professional tourism organisation.

TASK
Draft a personalised response after reviewing confirmed complaint facts.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: complaint anonymised; timeline; evidence; service standard; company finding; guest impact; authorised remedy; pending investigation; tone.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: acknowledgement; factual response; action; remedy wording; next step; privacy check. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Do not disclose employee details, admit unverified liability or invent compensation.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/guest-experience-ai-prompts.html) · [Library index](../README.md)
