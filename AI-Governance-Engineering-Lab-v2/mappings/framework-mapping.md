# AI Governance Framework Mapping

This mapping is intentionally high-level. It demonstrates governance thinking without claiming that an individual portfolio control satisfies an entire framework requirement.

| Lab control | NIST AI RMF concept | ISO/IEC 42001 concept | Evidence example |
|---|---|---|---|
| AI system inventory | GOVERN / MAP | AI management system context and inventory | `inventory/ai-system-inventory.yaml` |
| AI risk register | GOVERN / MAP / MANAGE | Risk and opportunity management | `risk/ai-risk-register.yaml` |
| Vendor approval gate | GOVERN / MANAGE | Supplier / third-party governance | `vendors/ai-vendor-assessment.md` |
| Privacy gate | MAP / MANAGE | Data and information management | Rego decision + test evidence |
| Fairness validation gate | MEASURE / MANAGE | Evaluation and monitoring concepts | Rego decision + validation result |
| Human oversight gate | GOVERN / MANAGE | Human oversight and operational controls | Rego decision + approval evidence |
| Automated policy tests | MEASURE | Monitoring, measurement, analysis and evaluation | `policy_test.rego` |

## Important Boundary

Frameworks provide governance structures and expectations; this lab implements a small set of simulated technical controls. The mappings are illustrative and should be validated against the current framework text before being used for a real assessment.
