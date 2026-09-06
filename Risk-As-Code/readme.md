# Risk-as-Code GRC Lab

A portfolio lab demonstrating how a GRC analyst can convert a risk register into **repeatable, testable and partially automated risk decisions**.

## What this demonstrates

- Structured risk data in YAML
- 5x5 likelihood × impact scoring
- Risk rating and escalation logic in Python
- Input validation and duplicate-ID detection
- Machine-readable JSON output
- Optional pipeline failure for open High/Critical risks
- File Integrity Monitoring (FIM) using SHA-256 hashes
- Policy-as-Code using OPA/Rego
- Unit tests for risk logic
- Clear separation between risk data, evaluation logic and policy enforcement

## Architecture

```text
risks.yaml
    │
    ├──> evaluate_risk.py ──> human / JSON risk report
    │
    ├──> OPA/Rego policy ──> policy decision + violations
    │
    └──> fim_checker.py ──> integrity check
             
Tests validate the Python logic; Rego tests validate policy behavior.
```

## Risk Methodology

The sample uses a simple 5x5 inherent-risk score:

`Risk Score = Likelihood × Impact`

- **1–4:** Low
- **5–9:** Medium
- **10–15:** High
- **16–25:** Critical

For this lab, **Open High/Critical risks require escalation**. Mitigated risks remain visible but do not trigger escalation.

> This is a portfolio methodology, not a replacement for an organization's approved enterprise risk methodology.

## Run the Python evaluator

```bash
pip install -r requirements.txt
python evaluate_risk.py
```

Machine-readable output:

```bash
python evaluate_risk.py --json
```

Simulate a CI/CD gate:

```bash
python evaluate_risk.py --fail-on-escalation
```

Exit codes:

- `0` = evaluation completed without a policy-triggered escalation
- `1` = input / validation error
- `2` = open High/Critical risk detected when `--fail-on-escalation` is enabled

## Run tests

```bash
python -m unittest discover -s tests
```

## OPA/Rego

With OPA installed:

```bash
opa test policy -v
opa eval --data policy/risk_policy.rego --input policy/input.json 'data.riskascode.violations'
```

The Rego policy demonstrates a second control layer: Python performs risk-register evaluation, while OPA expresses an independent policy decision that can be used in CI/CD or other automated workflows.

## File Integrity Monitoring

Initialize a baseline for protected files:

```bash
python fim_checker.py --init evaluate_risk.py risks.yaml policy/risk_policy.rego
```

Then run the check:

```bash
python fim_checker.py
```

If a protected file changes, the checker reports the file as changed or missing.

## GRC Analyst Workflow

1. **Identify** — document the risk and business context.
2. **Assess** — score likelihood and impact consistently.
3. **Evaluate** — determine the risk rating and escalation requirement.
4. **Automate** — encode repeatable decisions in Python/Rego.
5. **Monitor** — use FIM and recurring checks to detect changes.
6. **Document** — preserve the decision, mitigation and evidence.
7. **Remediate** — assign and track corrective action.
8. **Reassess** — update the risk when conditions change.

## Portfolio Talking Points

A hiring manager can see that this project is more than a script that multiplies two numbers. It demonstrates:

- repeatable risk methodology
- validation of GRC data quality
- separation of policy and implementation
- machine-readable outputs
- automated escalation logic
- integrity monitoring
- unit testing
- Policy-as-Code concepts
- a path toward CI/CD integration

## Limitations / Next Steps

Potential production enhancements would include risk ownership, due dates, residual risk, control mappings, evidence references, treatment decisions, audit history, approvals, exception handling and integration with a GRC platform.
