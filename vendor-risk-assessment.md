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

    Click "Commit changes..." and save it.

File 3: The Linux Server Infrastructure Audit

    Click Add file -> Create new file.

    Name the file: linux-server-audit.md

    Copy and paste this text into the box:

Markdown

# Infrastructure Audit: Production Linux Server Baseline
**Framework Target:** SOC 2 Type II Readiness  
**Scope:** Remote Access Configurations (`/etc/ssh/sshd_config`, `/etc/group`)  

---

## Technical Vulnerability Log & Mapping

| Config Location | Current Value | Risk / Behavioral Deficiency | SOC 2 Mapping | Corrective Action Required |
| :--- | :--- | :--- | :--- | :--- |
| `sshd_config` | `PasswordAuthentication yes` | Allows weak, user-generated passwords; highly vulnerable to automated credential brute-forcing. | **CC6.3** (Credential Protection) | Change to `PasswordAuthentication no`. Enforce cryptographic keys only. |
| `sshd_config` | `PermitRootLogin yes` | Allows direct administrative remote login. Destroys individual audit trails and accountability. | **CC6.1** (Access Alteration) | Change to `PermitRootLogin no`. Enforce unique logins + `sudo`. |
| `sshd_config` | `MaxAuthTries 25` | Permits 25 sequential login attempts, allowing hacking bots extensive room to guess credentials. | **CC6.3** (Attack Vector Controls) | Drop value to `MaxAuthTries 3` to enforce rapid lockouts. |
| `/etc/group` | `sudo:...marketing_intern` | Over-privileged user placement. Violates basic security assignment rules. | **CC6.1** (Least Privilege) | Revoke group membership immediately. Restrict admin rights. |

---

## Impact Summary (Non-Repudiation Failure)
When systems allow shared administrative access or unlogged root logins, the organization suffers a total loss of tracking capability. If an anomalous data extraction or infrastructure failure takes place, corporate security teams have no way to verify which specific user executed the command. Enforcing individual system accountability is a mandatory prerequisite for modern compliance framework alignment.
