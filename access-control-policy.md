Aethel Corp: Corporate Access Control Policy
**Document ID:** SEC-POL-003  
**Version:** 1.0  
**Framework Mapping:** SOC 2 TSC CC6.1, CC6.2, CC6.3  

---

## 1. Objective & Scope
This policy defines the mandatory security requirements for establishing, modifying, and revoking logical access to Aethel Corp production systems. This policy applies to all employees, contractors, and third-party systems interacting with corporate data.

## 2. Core Identity Principles

### 2.1 Individual Accountability
All access to Aethel Corp information systems must be mapped to a uniquely identifiable human being or designated system process. The use of shared, generic, or group-level credentials (such as shared deployment keys or shared passwords) is strictly prohibited. All personnel are responsible for all actions taken under their assigned unique identity.

### 2.2 Principle of Least Privilege
Access rights and administrative permissions shall be granted based strictly on the Principle of Least Privilege. Personnel shall only be provisioned the minimum logical access necessary to perform their explicit job functions. Non-engineering staff, interns, and unauthorized external parties are strictly barred from receiving administrative (`sudo` or root) privileges on any production asset.

## 3. Remote Server Hardening Requirements (SSH)
To comply with SOC 2 CC6.3, all production Linux infrastructure must enforce the following cryptographic and access baselines:

*   **Authentication Method:** All remote server connections must require cryptographic SSH Public Key Authentication. Standard password-based authentication over SSH is strictly prohibited.
*   **Root Account Governance:** Direct remote login to the root administrative account is strictly prohibited. Engineers requiring administrative privileges must log in via their unique individual user accounts and elevate their permissions using the `sudo` command.
*   **Brute-Force Prevention:** To prevent brute-force attacks, remote server configurations must enforce a strict connection limit. The maximum number of authentication attempts before a connection is dropped shall be limited to 3.
