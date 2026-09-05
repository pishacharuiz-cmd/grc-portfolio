# AI Governance Framework Mapping

This mapping is a portfolio demonstration of control intent. It is not a claim that these rules independently satisfy an entire framework requirement.

| Lab control | NIST AI RMF concept | ISO/IEC 42001 concept | Evidence artifact |
|---|---|---|---|
| Risk classification | Govern / Map | AI risk management | Input risk tier + policy decision |
| Restricted PII protection | Map / Manage | Data governance | Policy violation + request payload |
| Vendor approval | Govern / Manage | AI system/provider controls | Vendor approval decision |
| Fairness threshold | Measure / Manage | AI system evaluation | Fairness score + test result |
| Human approval for high risk | Govern / Manage | Human oversight | Approval field + decision log |
| Automated policy tests | Measure | Monitoring/evaluation support | Rego test suite |

## Governance Principle

A framework requirement should be translated into a specific control objective, an owner, an evidence source, and a testable acceptance condition. The policy engine is the enforcement layer; governance documentation defines why the control exists and who is accountable for it.
