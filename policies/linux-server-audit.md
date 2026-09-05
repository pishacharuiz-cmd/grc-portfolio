# Linux Server Access Control Review

**Framework Reference:** SOC 2 Type II criteria (sample mapping)  
**Scope:** SSH and privileged-access configuration (`/etc/ssh/sshd_config`, `/etc/group`)  
**Environment:** Simulated server configuration  

---

## Review Findings

| Config Location | Current Value | Risk / Observation | SOC 2 Mapping | Recommended Action |
| :--- | :--- | :--- | :--- | :--- |
| `sshd_config` | `PasswordAuthentication yes` | Password-based SSH access increases exposure to credential attacks and may not align with the organization's authentication standard. | **CC6.3** | Evaluate whether key-based authentication should be required and disable password authentication where appropriate. |
| `sshd_config` | `PermitRootLogin yes` | Direct remote root access reduces individual accountability and increases the impact of compromised privileged credentials. | **CC6.1** | Disable direct root login and use named accounts with controlled `sudo` access. |
| `sshd_config` | `MaxAuthTries 25` | A high authentication-attempt limit can increase exposure to repeated login attempts. | **CC6.3** | Review the setting against the organization's baseline and reduce it where appropriate. |
| `/etc/group` | `sudo:...marketing_intern` | The account appears to have administrative group membership that may exceed the user's job requirements. | **CC6.1** | Confirm business need and approval; remove unnecessary privileged access. |

## Analyst Follow-Up

For each finding, an analyst would typically:

1. Confirm the configuration and affected account.
2. Compare the setting with the approved security baseline.
3. Document the business or security risk.
4. Record the recommended remediation and owner.
5. Recheck the configuration after remediation.

## Review Note

This is a simulated configuration review for portfolio purposes. The SOC 2 references are illustrative and should be validated against the applicable organization's control framework and system scope before use in a real audit.
