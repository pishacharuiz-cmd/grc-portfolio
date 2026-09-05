# AI Vendor Risk Assessment

## Scope

Simulated third-party AI vendor assessment supporting the AI Governance Engineering Lab. This artifact demonstrates how vendor risk can be connected to AI governance decisions.

## Vendor Profile

| Field | Assessment |
|---|---|
| Vendor | Example External LLM Provider |
| Service | Hosted generative AI API |
| Processing | Third-party cloud |
| Data sensitivity | Internal; restricted data requires additional controls |
| Business owner | Customer Experience |
| Risk tier | High for restricted/high-impact use cases |
| Assessment status | Conditional approval |

## Due-Diligence Questions

| Domain | Review question | Status | Required evidence |
|---|---|---|---|
| Data use | Is customer data used to train provider models by default? | Review | Contract / provider terms |
| Retention | Can prompts and outputs be retained and for how long? | Review | Retention configuration |
| Security | Are data encrypted in transit and at rest? | Review | Security documentation |
| Access | Is administrative access restricted and logged? | Review | Access-control evidence |
| Subprocessors | Are subprocessors disclosed and governed? | Review | Subprocessor list |
| Incident response | Are security incidents subject to defined notification terms? | Review | Contract / SLA |
| Auditability | Can the organization obtain relevant assurance evidence? | Review | SOC report / assurance package |
| Model governance | Are material model changes communicated? | Review | Change-management terms |

## Governance Decision

**Conditional approval** for simulated portfolio use, provided that restricted data is protected, the vendor is formally approved, required contractual safeguards are documented, and higher-risk AI use retains human oversight.

This assessment is a portfolio artifact and does not represent a real vendor's security posture or legal compliance status.
