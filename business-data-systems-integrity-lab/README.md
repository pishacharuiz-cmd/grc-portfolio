# Business Data & Systems Integrity Lab

A small simulated business-systems lab demonstrating how to investigate data-integrity problems across connected applications.

## Scenario

A CRM is treated as the source system for customer records. Customer data is replicated into an operational database and later consumed by reporting. The analyst must determine whether downstream records remain consistent with the source.

**Workflow:** CRM source -> Operational database -> Integrity validation -> Finding -> Risk -> Remediation -> Retest -> Evidence

## What this demonstrates

- SQL-based data validation
- Cross-system reconciliation
- Python automation and reporting
- Data-quality investigation
- Business-impact analysis
- Finding documentation
- Remediation and validation
- Evidence preservation

## Quick start

Requirements: Python 3.9+. No external database server is required.

Run:

```bash
python python/integrity_report.py
```

The script creates a local SQLite database, runs five validation checks, prints the findings, and writes `evidence/integrity_report.md`.

## Simulated findings

The dataset deliberately contains a status mismatch, balance mismatch, missing downstream record, duplicate downstream record, and stale record.

## Risk/control workflow

**Business issue -> Risk -> Control objective -> Evidence -> Remediation -> Validation**

See `docs/risk-control-mapping.md` for the detailed mapping.

## Scope

This is a proof of approach, not a production integration platform. It can later become a module of the larger enterprise GRC project.
