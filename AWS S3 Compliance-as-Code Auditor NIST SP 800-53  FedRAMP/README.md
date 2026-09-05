# AWS S3 Compliance-as-Code Auditor

A Python-based compliance lab that evaluates simulated AWS S3 configuration data against selected requirements derived from **NIST SP 800-53** and **FedRAMP**.

## Objective

This project demonstrates an analyst-friendly approach to compliance checks by evaluating configuration data, identifying control gaps, and generating remediation recommendations.

The lab focuses on two common areas:

- Encryption at rest
- S3 public access settings

## Framework Mapping

- **NIST SP 800-53 SC-13 — Cryptographic Protection:** checks whether storage buckets have encryption enabled.
- **NIST SP 800-53 AC-3 / SC-7 — Access Enforcement / Boundary Protection:** checks whether public access protections are enabled.

## Project Structure

```text
aws-s3-compliance-auditor/
│
├── src/
│   ├── auditor.py                # Compliance evaluation logic
│   └── mock_infrastructure.json  # Simulated cloud configuration data
├── tests/
│   └── test_auditor.py           # Unit tests for compliance checks
├── requirements.txt
└── README.md
```

## Analyst Workflow

1. Review the available configuration data.
2. Map configuration checks to the selected control requirements.
3. Identify control gaps.
4. Document the finding and recommended corrective action.
5. Use unit tests to verify the compliance-check logic.

## Scope Note

This is a portfolio lab using simulated infrastructure data. It does not connect to or assess a live AWS environment.
