# AI Governance Policy Test Results

## Validation Summary

The AI Governance Engineering Lab v2 policy was executed locally with Open Policy Agent (OPA) on Windows.

| Validation | Result |
|---|---|
| OPA version | 1.20.0 |
| Rego version | v1 |
| Test cases | 8 / 8 passed |
| Policy coverage | 91.18% |
| Test-file coverage | 100% |
| Overall coverage | 96.30% |
| Validation status | PASS |

## Command Executed

```powershell
& "$HOME\Tools\OPA\opa.exe" test .\AI-Governance-Engineering-Lab-v2\policy.rego .\AI-Governance-Engineering-Lab-v2\policy_test.rego -v
```

Coverage was additionally measured with:

```powershell
& "$HOME\Tools\OPA\opa.exe" test .\AI-Governance-Engineering-Lab-v2\policy.rego .\AI-Governance-Engineering-Lab-v2\policy_test.rego -v --coverage
```

## Test Cases

| Test | Result |
|---|---|
| Safe request is allowed | PASS |
| Restricted unmasked PII is denied | PASS |
| Unapproved external vendor is denied | PASS |
| Fairness score below 0.80 is denied | PASS |
| High-risk request without human approval is denied | PASS |
| High-risk request with human approval is allowed | PASS |
| Multiple simultaneous violations are denied | PASS |
| Decision contains policy version | PASS |

## Coverage Notes

The test suite achieved 96.30% overall coverage. The remaining uncovered policy branches are primarily the default/fallback paths that are not exercised by the current scenarios.

## Evidence Boundary

This result demonstrates that the simulated governance policy executes successfully and that the defined test cases pass. It does not establish legal, regulatory, security, fairness, or production readiness for a real AI system.

The results are portfolio validation evidence for the AI Governance Engineering Lab v2.
