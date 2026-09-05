# Sample Corporate Access Control Policy

**Document ID:** SEC-POL-003  
**Version:** 1.0  
**Framework Reference:** SOC 2 TSC CC6.1, CC6.2, CC6.3  
**Status:** Portfolio Sample

---

## 1. Objective & Scope

This sample policy defines example requirements for establishing, modifying, reviewing, and revoking logical access to corporate systems.

It is intended to demonstrate how common access-control principles can be translated into policy language.

## 2. Core Identity Principles

### 2.1 Individual Accountability

Access should be associated with a uniquely identifiable user or approved system identity. Shared or generic credentials should be avoided unless there is a documented business or technical exception with appropriate controls.

### 2.2 Least Privilege

Access should be limited to the permissions required for an individual's job responsibilities. Administrative access should be restricted to approved personnel and reviewed periodically.

## 3. Remote Server Access

For production Linux systems, an organization may establish the following baseline requirements:

- **Authentication:** Prefer strong key-based authentication and disable password-based SSH access where supported by the organization's standard.
- **Root Access:** Disable direct remote root login and use named accounts with controlled `sudo` access.
- **Authentication Attempts:** Set a reasonable authentication-attempt limit based on the organization's approved hardening baseline.

## 4. Access Review

Privileged and sensitive access should be reviewed on a defined schedule. Review evidence should identify the account, assigned access, business owner or manager approval, and any remediation required.

## Portfolio Note

This is a sample policy for portfolio purposes. Exact technical settings and approval requirements should be established through the applicable organization's risk assessment, security baseline, and documented procedures.
