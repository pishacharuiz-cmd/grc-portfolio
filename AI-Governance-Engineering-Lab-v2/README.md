# AI Governance Engineering Lab v2

A portfolio-grade AI governance lab that extends the original policy-as-code experiment into a small governance control system.

## Objective

Demonstrate how AI governance requirements can be translated into machine-enforceable controls, risk assessments, vendor governance, evidence, testing, and framework mappings.

This is a simulated portfolio environment. It is not a production AI safety system and does not establish legal or regulatory compliance.

## Architecture

`AI system inventory -> risk assessment -> governance controls -> policy evaluation -> allow / deny + violations -> evidence`

The policy is implemented with Open Policy Agent (OPA) / Rego.

## Lab Structure

```text
AI-Governance-Engineering-Lab-v2/
├── README.md
├── policy.rego
├── policy_test.rego
├── sample-inputs/
│   ├── high-risk-approved.json
│   ├── high-risk-no-approval.json
│   ├── restricted-pii.json
│   └── unapproved-vendor.json
├── risk/
│   ├── ai-risk-register.yaml
│   └── risk-methodology.md
├── inventory/
│   └── ai-system-inventory.yaml
├── vendors/
│   └── ai-vendor-assessment.md
├── mappings/
│   └── framework-mapping.md
├── evidence/
│   └── sample-control-evidence.md
└── .github/workflows/
    └── opa-tests.yml
```

## Controls Demonstrated

| Control | Governance intent | Enforcement |
|---|---|---|
| Restricted-data privacy | Prevent unsafe handling of restricted PII | Deny unmasked PII |
| Third-party AI vendor approval | Reduce unauthorized vendor/model risk | Deny unapproved external vendors |
| Fairness validation | Require a configured validation gate | Deny below 0.80 |
| Human oversight | Require approval for higher-risk use | Deny high-risk requests without approval |
| Governance field validation | Ensure required decision inputs exist | Deny incomplete requests |

The 0.80 fairness value is a simulated portfolio threshold, not a regulatory requirement.

## Risk Management

The lab includes an AI system inventory, a likelihood x impact risk methodology, a risk register, risk owners, treatments, and residual-risk tracking.

## Vendor Governance

The vendor assessment connects third-party risk to AI governance by reviewing data use, retention, security, subprocessors, incident response, auditability, and model-change considerations.

## Evidence & Auditability

The evidence package demonstrates the chain:

`Requirement -> Control -> Policy Rule -> Test Case -> Result -> Reviewer -> Review Record`

## Testing & CI

Run the policy tests locally with:

```bash
opa test . -v --coverage
```

A GitHub Actions workflow also runs the policy test suite when this lab changes.

## Framework Mapping

The mapping provides high-level connections to governance concepts from NIST AI RMF and ISO/IEC 42001. It intentionally does not claim that an individual Rego rule satisfies an entire framework requirement.

## Why This Matters for GRC

This lab demonstrates the bridge between GRC and engineering:

1. Identify the AI system and its business purpose.
2. Identify and score governance risks.
3. Define controls and owners.
4. Translate selected controls into executable policy.
5. Test the controls with positive and negative cases.
6. Preserve decision and review evidence.
7. Connect the controls back to governance frameworks.

The original labs in this repository remain unchanged; this folder is a separate, more advanced AI governance engineering track built on the same GRC principles.
