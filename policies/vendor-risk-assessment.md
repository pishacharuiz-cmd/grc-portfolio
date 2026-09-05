# Vendor Security Review: DataPulse AI

**Date:** June 2026  
**Assessor:** GRC Analyst Sandbox  
**Target Platform:** DataPulse AI (Analytics Engine)  
**Assessment Type:** Simulated third-party risk review  

---

## Assessment Summary

This exercise reviews security information provided for a fictional vendor that would process sensitive customer financial records.

Based on the available information, several control gaps would need to be addressed or escalated before normal onboarding could be recommended.

## Findings

### 1. Independent Security Assurance

**Observation:** The vendor does not currently provide a SOC 2 Type II report or ISO 27001 certification and indicates that formal assurance is planned for a future period.

**Risk:** The available evidence provides limited independent validation of the vendor's control environment.

**Recommendation:** Request additional security documentation, such as a completed security questionnaire, relevant policies, penetration-test summary, or other available assurance evidence. Track the gap for follow-up.

### 2. Data Protection

**Observation:** The assessment scenario indicates that customer records may be stored without encryption at rest.

**Risk:** Sensitive data could have greater exposure if storage or underlying infrastructure is compromised.

**Recommendation:** Request confirmation of encryption controls and supporting evidence. If encryption is not available, document the exception and determine whether compensating controls or remediation are required.

### 3. Privileged Access

**Observation:** Engineering and development personnel are described as using a shared administrative credential for access to the live database.

**Risk:** Shared privileged credentials reduce individual accountability and make access review and investigation more difficult.

**Recommendation:** Recommend individual privileged accounts, appropriate role-based access, MFA where supported, and periodic access reviews. Confirm implementation during follow-up.

## Compensating Controls

The vendor cites physical security at its corporate office as a compensating measure. Physical security may reduce certain facility-related risks, but it does not directly address logical access, credential, or cloud data-protection risks.

## Recommended Follow-Up

- Request supporting evidence for identified controls.
- Document any accepted exceptions and their rationale.
- Track remediation owners and target dates.
- Reassess the open findings before final onboarding approval.

## Portfolio Note

This is a simulated vendor-risk exercise. The vendor, findings, and assessment scenario are fictional and are included to demonstrate an analyst approach to third-party risk review and remediation tracking.
