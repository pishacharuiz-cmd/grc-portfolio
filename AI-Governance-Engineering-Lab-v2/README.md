# AI Governance Engineering Lab v2

A portfolio-grade AI governance lab that extends the original policy-as-code experiment into a small governance control system.

## Objective

Demonstrate how AI governance requirements can be translated into:

- machine-enforceable controls
- risk-tiered approval gates
- vendor governance checks
- privacy safeguards
- fairness validation gates
- human oversight requirements
- automated policy tests
- auditable control mappings

This is a simulated portfolio environment. It is not a production AI safety system and does not establish legal or regulatory compliance.

## Architecture

`AI request -> risk classification -> policy evaluation -> allow / deny + violations -> evidence`

The policy is implemented with Open Policy Agent (OPA) / Rego. OPA supports automated Rego testing with `opa test`, including coverage reporting.

## Controls Demonstrated

| Control | Governance intent | Enforcement |
|---|---|---|
| Restricted-data privacy | Prevent unsafe handling of restricted PII | Deny when PII is unmasked |
| Third-party AI vendor approval | Reduce unauthorized vendor/model risk | Deny unapproved external vendors |
| Fairness validation | Require pre-deployment fairness validation | Deny below configured threshold |
| Human oversight | Require approval for higher-risk AI use | Deny high-risk requests without approval |
| Risk classification | Apply stronger controls to higher-risk use cases | Risk tier drives approval gate |

## Test Strategy

The lab includes positive and negative test cases for each major control. Run:

```bash
opa test . -v --coverage
```

A production-style implementation would additionally integrate policy testing into CI/CD and retain policy decisions as audit evidence.

## Framework Mapping

The mapping in `framework-mapping.md` is intentionally high-level. It connects the engineering controls to governance concepts from NIST AI RMF and ISO/IEC 42001 without claiming that a single Rego rule satisfies an entire framework requirement.

## Portfolio Value

This project demonstrates the bridge between GRC and engineering: identify governance requirements, translate them into controls, automate the decision logic, test the controls, and preserve evidence for review.
