# scf-governance-mapping
Governance, Risk, and Compliance (GRC) portfolio mapping technical and documentation safeguards across global compliance frameworks (NIST CSF 2.0, ISO 27001, SOC 2) utilizing the Secure Controls Framework (SCF).

# SCF Governance & Technical Controls Lab: Compliance Mapping

This lab demonstrates an understanding of enterprise governance and identity security by mapping SCF controls to practical evidence artifacts, utilizing the **Secure Controls Framework (SCF) 2026.1.1**.

## 1. Selected Governance Control: Policy Publishing
* **SCF Domain:** Security, Compliance & Resilience Governance
* **SCF Control ID:** GOV-02
* **Control Name:** Publishing Security, Compliance & Resilience Documentation
* **Control Description:** Mechanisms exist to establish, maintain and disseminate policies, standards and procedures necessary for secure, compliant and resilient capabilities.
* **Conformity Validation Cadence:** Annual

---

## 2. Evidence Requests & Solutions Matrix
Based on the organizational sizing definitions in the SCF, the following matrix demonstrates how an enterprise establishes an audit trail to prove this control is active:

| SCF Evidence ID | Required Audit Evidence | Practical Implementation Solution |
| :--- | :--- | :--- |
| **E-GOV-08** | Policy Dissemination Logs | Centralized Corporate Intranet Portal (e.g., SharePoint / Confluence) tracking read-acknowledgments. |
| **E-GOV-09** | Version-Controlled Policies | Formal Git-backed or DMS repository enforcing strict change-control workflows and approvals. |
| **E-GOV-11** | Annual Policy Review Schedule | Governance committee calendar invites and signed minutes proving annual policy validation. |

---

## 3. GRC Analyst Implementation Blueprint (GOV-02)
To satisfy **GOV-02** within an organization, a GRC Analyst must ensure that security documentation is not just written, but actively communicated and managed. 

### Step-by-Step Validation Checklist:
1. **Centralized Repository:** Establish a single source of truth for all security policies so employees do not reference outdated documents.
2. **Access Control:** Ensure policy modification rights are strictly restricted to the Governance Committee or designated CISO staff.
3. **Evidence Collection:** Maintain automated platform logs showing that 100% of onboarding employees have officially reviewed and accepted the mandatory Information Security Policy.

---

## 4. Control Analysis: Exception Management
* **SCF Control ID:** GOV-02.1
* **Control Description:** Mechanisms exist to prohibit exceptions to standards, except when the exception has been formally assessed for risk impact, approved and recorded.
* **Evidence Request ID:** E-GOV-18 (Exception Request Log / Form)

### Practical GRC Application
When a business unit cannot meet a mandatory security standard due to technical or operational limitations, a formal exception process must be triggered. As an analyst, I ensure that the risk impact is documented, a compensatory control is identified, formal executive approval is signed, and the entry is recorded in the centralized Exception Log to maintain audit readiness.

---

## 5. Technical Control Tracking: Identity & Access Management (IAC)
While governance dictates the rules, technical controls enforce them. This section maps out the baseline requirements for user identity authentication, showing how the same piece of evidence can satisfy multiple overlapping requirements.

### Control & Evidence Matrix

| SCF Control ID | Control Name / Focus | Evidence Request ID | Core Objective & Practical Evidence Artifact |
| :--- | :--- | :--- | :--- |
| **IAC-03.5** | Privileged Access Reviews | **E-IAM-05** / **E-IAM-06** | System-generated provisioning logs and identity baseline compliance reports showing administrative rights are strictly audited. |
| **IAC-04** | Multi-Factor Authentication | **E-IAM-05** / **E-IAM-06** | Configuration policies exported from the Identity Provider (IdP) proving MFA is continuously enforced for remote and admin sessions. |

> **Analyst Note on Evidence Efficiency:** Notice that `E-IAM-05` and `E-IAM-06` repeat across these controls. In enterprise GRC, this is a massive operational advantage. Collecting these identity configuration logs satisfies multiple compliance checkboxes simultaneously, demonstrating the "Map Once, Comply Many" efficiency of the SCF.

---

## 6. Technical Control Tracking: Artificial Intelligence & Autonomous Technologies (AAT)

While traditional IAM and policy dissemination govern standard assets, AI introduces runtime behavioral risks, model drift, and data provenance challenges that require structured lifecycle boundaries and automated guardrails.

### Control & Evidence Matrix

| SCF Control ID | Control Name / Focus | Evidence Request ID | Core Objective & Practical Evidence Artifact |
| :--- | :--- | :--- | :--- |
| **AAT-01** | AI & Autonomous Technologies Governance | E-AAT-02 | Centralized AI Asset Registry tracking model inventory, intended business purpose, and data dependencies. |
| **AAT-02** | AI Risk Assessment & Impact Thresholds | E-AAT-03 | Documented risk-tiering methodology classifying models (e.g., low, medium, high risk) to determine required technical oversight. |
| **AAT-04** | AI System Resiliency & Guardrail Enforcement | E-AAT-05 | CI/CD policy-as-code evaluation logs (e.g., OPA/Rego outputs) validating automated safety filters and human-in-the-loop triggers prior to deployment. |

---

## 7. Policy-as-Code Implementation: AI Deployment Guardrail

To operationalize **SCF Control AAT-02 and AAT-04** alongside **NIST AI RMF (Manage)**, the following Open Policy Agent (OPA) **Rego** policy is enforced inside the CI/CD pipeline. It programmatically evaluates model deployment configurations to ensure that high-risk AI assets cannot reach production without explicit safety guardrails and human oversight.

```rego
package governance.ai.deployment

import rego.v1

default allow := false

# Rule 1: Allow deployment if it's low/medium risk and meets baseline criteria
allow if {
    not high_risk_model
    has_output_filters
}

# Rule 2: Allow deployment for high-risk models ONLY if strict oversight controls are met
allow if {
    high_risk_model
    has_output_filters
    has_designated_human_reviewer
    encryption_at_rest_enabled
}

# Helper: Identify if the AI model is classified as High Risk (maps to AAT-02)
high_risk_model if {
    input.model.risk_tier == "high"
}

# Helper: Ensure safety guardrails/filters are active
has_output_filters if {
    input.model.safety_filters_enabled == true
}

# Helper: Ensure high-risk models have an assigned human reviewer (maps to AAT-04)
has_designated_human_reviewer if {
    input.governance.designated_reviewer != ""
}

# Helper: Ensure infrastructure encryption is enabled
encryption_at_rest_enabled if {
    input.infrastructure.encryption == true
}

# Custom denial messages for CI/CD pipeline logs
deny contains msg if {
    not has_output_filters
    msg := "VIOLATION (AAT-04): AI model deployment blocked. Mandatory output safety filters are disabled."
}

deny contains msg if {
    high_risk_model
    not has_designated_human_reviewer
    msg := "VIOLATION (AAT-01/AAT-04): High-risk AI model deployment blocked. Missing mandatory designated human reviewer assignment."
}
