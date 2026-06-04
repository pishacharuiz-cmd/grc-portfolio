# Infrastructure Audit: Production Linux Server Baseline
**Framework Target:** SOC 2 Type II Readiness  
**Scope:** Remote Access Configurations (`/etc/ssh/sshd_config`, `/etc/group`)  

---

## Technical Vulnerability Log & Mapping

| Config Location | Current Value | Risk / Behavioral Deficiency | SOC 2 Mapping | Corrective Action Required |
| :--- | :--- | :--- | :--- | :--- |
| `sshd_config` | `PasswordAuthentication yes` | Allows weak, user-generated passwords; highly vulnerable to automated credential brute-forcing. | **CC6.3** (Credential Protection) | Change to `PasswordAuthentication no`. Enforce cryptographic keys only. |
| `sshd_config` | `PermitRootLogin yes` | Allows direct administrative remote login. Destroys individual audit trails and accountability. | **CC6.1** (Access Alteration) | Change to `PermitRootLogin no`. Enforce unique logins + `sudo`. |
| `sshd_config` | `MaxAuthTries 25` | Permits 25 sequential login attempts, allowing hacking bots extensive room to guess credentials. | **CC6.3** (Attack Vector Controls) | Drop value to `MaxAuthTries 3` to enforce rapid lockouts. |
| `/etc/group` | `sudo:...marketing_intern` | Over-privileged user placement. Violates basic security assignment rules. | **CC6.1** (Least Privilege) | Revoke group membership immediately. Restrict admin rights. |

---

## Impact Summary (Non-Repudiation Failure)
When systems allow shared administrative access or unlogged root logins, the organization suffers a total loss of tracking capability. If an anomalous data extraction or infrastructure failure takes place, corporate security teams have no way to verify which specific user executed the command. Enforcing individual system accountability is a mandatory prerequisite for modern compliance framework alignment.
