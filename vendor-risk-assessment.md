# Vendor Security Review: DataPulse AI
**Date:** June 2026  
**Assessor:** GRC Analyst Sandbox  
**Target Platform:** DataPulse AI (Analytics Engine)  
**Classification:** High Risk (Processes Sensitive Customer Financial Records)  

---

## 🛑 Onboarding Status: DENIED

### Executive Summary
A comprehensive technical security review was conducted on DataPulse AI ahead of proposed business onboarding. Due to severe, foundational structural deficiencies in data protection and access identity hygiene, the platform introduces unacceptable liability to corporate operations. Onboarding is denied until remediation is independently verified.

### Core Audit Findings

#### 1. Total Absence of Independent Assurances
*   **Finding:** The vendor lacks a third-party audit report (SOC 2 Type II or ISO 27001 certification). The vendor states compliance is "on next year's roadmap."
*   **Risk:** Aethel Corp has zero verifiable proof of control effectiveness. Relying solely on internal vendor claims breaks our own compliance chain.

#### 2. Data Protection Deficiencies
*   **Finding:** DataPulse AI explicitly processes customer records in plain text, omitting "Encryption at Rest" to optimize system processing speed.
*   **Risk:** Compromise of the underlying cloud hosting layer completely exposes confidential customer financial records to plain-text data theft.

#### 3. Access Control Failures
*   **Finding:** The vendor’s engineering and development teams utilize a shared master administrative credential to monitor the live database.
*   **Risk:** Complete loss of individual accountability and non-repudiation. If an insider data leak or unauthorized data alteration occurs, tracing the incident to a specific employee is impossible.

### Insufficient Compensatory Controls
The vendor attempted to justify engineering and encryption vulnerabilities by citing "24/7 physical security guards at their corporate office." Physical building controls fail to mitigate remote, logical network vulnerabilities (such as credential stuffing or injection attacks) attacking a cloud-hosted environment.
