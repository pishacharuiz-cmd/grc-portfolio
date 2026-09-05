# GRC Portfolio

Hands-on Governance, Risk, and Compliance projects covering security controls, risk assessments, audit evidence, cloud compliance, and basic GRC automation.

## What This Portfolio Demonstrates

- Control and framework mapping
- Risk identification and documentation
- Access control and least-privilege reviews
- Audit evidence collection and validation
- Vendor security assessments
- Cloud configuration compliance checks
- Policy and exception management
- Basic compliance automation with Python and Rego

## Projects

### AWS S3 Compliance-as-Code Auditor
A Python-based lab that checks simulated AWS S3 configuration data against selected security requirements from NIST SP 800-53 and FedRAMP.

The checks focus on encryption, public access settings, control mapping, remediation recommendations, and unit testing.

The infrastructure data is simulated for portfolio use.

### Risk-as-Code
A small automation project that stores risk information in YAML and uses Python to evaluate and score risks.

The project demonstrates how structured risk data can make risk tracking more consistent and easier to review than maintaining everything manually in a spreadsheet.

### SCF Governance & Control Mapping
A control-mapping lab using the Secure Controls Framework (SCF) to connect governance and technical requirements with practical evidence.

Topics include policy publishing, exception management, privileged access reviews, MFA, AI governance, and evidence mapping.

The goal is to demonstrate an analyst workflow for connecting requirements to evidence and follow-up actions.

### Vendor Security Review
A simulated third-party risk assessment for a fictional analytics vendor.

The review considers independent security assurance, data protection, access management, compensating controls, and vendor remediation needs.

Findings are documented with risk, recommendation, and follow-up considerations rather than presented as a real procurement decision.

### Linux Server Audit
A baseline configuration review of a simulated Linux server focused on SSH and privileged access settings.

The review identifies configuration issues, relates them to relevant security criteria, and provides recommended corrective actions.

### Corporate Access Control Policy
A sample access-control policy covering MFA, least privilege, access approvals, and periodic access reviews.

It demonstrates how common security requirements can be translated into practical policy language.

## GRC Workflow

Across the projects, the general workflow is:

**Identify risk → Map requirement → Review control → Collect evidence → Document finding → Recommend remediation → Validate the result**

This reflects the type of execution-focused work expected in a mid-level GRC analyst role.

## Tools & Technologies

- NIST SP 800-53
- NIST CSF
- SOC 2
- FedRAMP
- Secure Controls Framework (SCF)
- Python
- YAML
- SQL
- Open Policy Agent (OPA) / Rego
- Git / GitHub
- AWS security concepts

## Portfolio Note

Projects in this repository are labs, simulations, or sample documentation created for learning and portfolio purposes. They do not represent access to or testing of a real production environment or a real company's systems.
