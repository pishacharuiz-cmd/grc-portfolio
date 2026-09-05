# Sample AI Governance Control Evidence

## Purpose

Simulated audit evidence showing how policy decisions can be tied to governance controls and review activity.

| Control ID | Control objective | Test / evidence | Result | Reviewer | Review status |
|---|---|---|---|---|---|
| AI-GOV-PRIV-01 | Prevent restricted unmasked PII from entering an AI workflow | Rego negative test for restricted + unmasked PII | Pass | GRC Reviewer | Reviewed |
| AI-GOV-VEND-01 | Prevent use of unapproved external AI vendors | Rego negative test for external + unapproved vendor | Pass | Third-Party Risk | Reviewed |
| AI-GOV-FAIR-01 | Block requests that fail the configured fairness gate | Rego negative test below 0.80 | Pass | Model Risk | Reviewed |
| AI-GOV-HUMAN-01 | Require human approval for high-risk AI use | Rego negative test without approval | Pass | AI Governance | Reviewed |

## Evidence Chain

`Requirement -> Control -> Policy Rule -> Test Case -> Result -> Reviewer -> Review Record`

## Example Finding

**Finding ID:** AIG-001  
**Condition:** A high-risk AI request was submitted without recorded human approval.  
**Risk:** Automated processing could proceed without the intended human oversight control.  
**Control:** AI-GOV-HUMAN-01  
**Policy response:** Deny request.  
**Recommended remediation:** Require an approval record before the workflow can proceed and retain the approval as audit evidence.

All evidence in this file is simulated for portfolio demonstration.
