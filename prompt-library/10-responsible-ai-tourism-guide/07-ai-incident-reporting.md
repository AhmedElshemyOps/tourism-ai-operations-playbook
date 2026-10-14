# AI Incident Reporting

**Prompt ID:** `10-07-ai-incident-reporting`  
**Category:** Responsible AI Governance  
**Department:** Management, Quality, Privacy and AI Governance  
**Risk level:** High  
**Human approval:** Required  
**Version:** 1.0.0  
**Last reviewed:** 2026-07-10

Create a report and response workflow for harmful, incorrect or unauthorised ai use.

## When to use

Use it for a controlled draft before information reaches a guest, supplier, colleague or manager.

**Example scenario:** An employee pastes identifiable passport information into an unapproved chatbot.

## Required inputs

- incident
- time
- tool
- use case
- output
- affected people
- data
- action taken
- evidence
- reporting duties unknown
- owner

## Expected outputs

- classification
- containment
- factual chronology
- impact
- notifications for expert decision
- root-cause questions
- CAPA
- closure

## Copy-ready prompt

```text
ROLE
Act as a tourism AI incident coordinator in a professional tourism organisation.

TASK
Create a report and response workflow for harmful, incorrect or unauthorised ai use.

CONTEXT
Destination/service: [Insert confirmed details]
Date, operating stage and guest/client profile: [Insert approved information]
Sources of truth: [List approved systems, confirmations, SOPs or official sources]

INPUTS
Provide: incident; time; tool; use case; output; affected people; data; action taken; evidence; reporting duties unknown; owner.
If an essential input is missing, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

OUTPUT
Return: classification; containment; factual chronology; impact; notifications for expert decision; root-cause questions; CAPA; closure. Separate confirmed facts, assumptions, recommendations and pending items. Label dynamic facts with their source and verification date when supplied.

LIMITS
Preserve evidence and avoid unsupported legal or technical conclusions.

PRIVACY AND APPROVAL
Exclude unnecessary personal data, identity or payment details, confidential rates, contracts and security information. Finish with verification actions, unresolved questions and the final approver’s role. The output remains a draft until that person checks it against approved sources.
```

## Trainer note

Replace every placeholder and keep unresolved items visible until an authorised professional reviews them.

[Source article](https://ahmedqualityops.com/responsible-ai-tourism-guide.html) · [Library index](../README.md)
