# SCF Governance & Technical Controls Lab

A hands-on GRC lab using the **Secure Controls Framework (SCF)** to connect governance and technical requirements with example evidence and follow-up activities.

The project focuses on practical analyst tasks such as control mapping, evidence requests, exception documentation, access-control reviews, and basic policy-as-code.

## 1. Selected Governance Control: Policy Publishing

- **SCF Domain:** Security, Compliance & Resilience Governance
- **SCF Control ID:** GOV-02
- **Control Name:** Publishing Security, Compliance & Resilience Documentation
- **Validation Cadence:** Annual

The exercise demonstrates how a control requirement can be translated into evidence requests such as policy dissemination records, version-controlled documents, and review records.

## 2. Evidence Requests & Solutions Matrix

| SCF Evidence ID | Example Evidence | Practical Evidence Source |
| :--- | :--- | :--- |
| **E-GOV-08** | Policy dissemination records | Intranet or document-management records showing policy distribution and acknowledgment. |
| **E-GOV-09** | Version-controlled policies | Approved document repository or Git-backed workflow showing policy changes and approvals. |
| **E-GOV-11** | Policy review records | Review schedule, meeting records, or approval documentation. |

## 3. Analyst Validation Checklist

A GRC analyst supporting this control could:

1. Confirm the current approved policy.
2. Verify that the policy is stored in the designated repository.
3. Review available evidence showing distribution and acknowledgment.
4. Check that required reviews occurred within the expected period.
5. Document gaps and request follow-up evidence when needed.

## 4. Exception Management

**SCF Control:** GOV-02.1  
**Evidence Request:** E-GOV-18

This section demonstrates a basic exception-management workflow. When a requirement cannot be met, the analyst documents the reason, risk impact, proposed compensating controls, approval status, and review date.

## 5. Identity & Access Management

| SCF Control ID | Focus | Example Evidence |
| :--- | :--- | :--- |
| **IAC-03.5** | Privileged access reviews | Provisioning records and access-review results. |
| **IAC-04** | Multi-factor authentication | Identity-provider configuration or compliance reports. |

### Evidence Efficiency

The same evidence source can sometimes support more than one control. Identifying those relationships helps reduce duplicate evidence requests while keeping the audit trail clear.

## 6. AI & Autonomous Technology Controls

This section extends the mapping exercise into AI governance topics.

| SCF Control ID | Focus | Example Evidence |
| :--- | :--- | :--- |
| **AAT-01** | AI governance | AI inventory or asset register. |
| **AAT-02** | AI risk assessment | Documented risk classification and assessment results. |
| **AAT-04** | AI resiliency and guardrails | Policy-as-code evaluation results and documented review controls. |

## 7. Sample Policy-as-Code Check

The repository includes an Open Policy Agent (OPA) / Rego example that evaluates an AI deployment configuration against selected governance conditions.

The example checks for items such as:

- Safety filters
- Human reviewer assignment for high-risk models
- Encryption at rest

The Rego policy is a portfolio demonstration of how a GRC requirement can be translated into a technical check. It should be treated as a sample control implementation rather than a production deployment standard.

## Portfolio Note

The mappings, evidence examples, and implementation scenarios in this project are illustrative. In a real environment, control applicability, evidence requirements, approval authority, and validation cadence would be confirmed against the organization's approved framework and procedures.
