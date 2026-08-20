# AWS S3 Compliance-as-Code Auditor

A lightweight Python-based compliance automation script designed to evaluate cloud infrastructure state JSON against security baselines derived from **NIST SP 800-53** and **FedRAMP** frameworks.

## Objective
Traditional GRC workflows rely heavily on manual periodic spreadsheet reviews and static paperwork. This project demonstrates a **Compliance-as-Code** approach—programmatically pulling configuration states, evaluating security controls (Encryption, Public Access Blocks), and instantly generating actionable remediation reports.

## Framework Mapping
* **NIST SP 800-53 SC-13 (Cryptographic Protection):** Validates that all storage buckets utilize encryption at rest.
* **NIST SP 800-53 AC-3 / SC-7 (Access Enforcement / Boundary Protection):** Validates that public access blocks are actively enforced to prevent unintended data exposure.

## Project Structure
```text
aws-s3-compliance-auditor/
│
├── src/
│   ├── auditor.py             # Main compliance evaluation logic
│   └── mock_infrastructure.json # Simulated cloud state payload
├── tests/
│   └── test_auditor.py        # Unit tests validating audit rules
├── requirements.txt
└── README.md