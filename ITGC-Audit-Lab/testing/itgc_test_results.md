# ITGC Test Results

## ITGC-01 — User Access Management

### Control Objective

Ensure user access is authorized, appropriate for the user's job responsibilities, and periodically reviewed.

### Evidence Reviewed

- `evidence/user_access.csv`

### Testing Procedure

The user access listing was reviewed to determine whether each user's access was supported by documented manager approval.

### Test Results

| User | Manager Approval | Result |
|---|---|---|
| Maria Santos | Yes | Pass |
| David Rivera | Yes | Pass |
| Carlos Medina | Yes | Pass |
| Luis Torres | No | **Exception** |
| Ana Perez | Yes | Pass |
| Robert Diaz | Yes | Pass |
| Sofia Lopez | Yes | Pass |

### Exception Identified

**User:** Luis Torres  
**Role:** Operations Specialist  
**Department:** Operations

No documented manager approval was identified for the user's system access.

### Risk Assessment

**Risk Level:** Medium

Unauthorized or unsupported access could result in inappropriate access to organizational systems or information.

### Recommended Remediation

Management should:

1. Confirm whether Luis Torres requires the existing access.
2. Obtain documented approval if the access is appropriate.
3. Remove unnecessary access if the access is not required.
4. Retain evidence of the review and approval.

### Test Conclusion

**Result: Exception Identified**

One exception was identified during testing of the user access control.

The control cannot be considered fully effective for the population tested because one user's access lacked documented management approval.


---

## ITGC-02 — Privileged Access Management

### Control Objective

Ensure privileged accounts are appropriately authorized, restricted, and supported by a documented business need.

### Evidence Reviewed

- `evidence/privileged_access.csv`

### Testing Procedure

The privileged access listing was reviewed to identify administrative accounts and determine whether each privileged account had a documented business justification and management approval.

### Test Results

| User | Role | Admin Access | Business Justification | Manager Approval | Result |
|---|---|---|---|---|---|
| Carlos Medina | System Administrator | Yes | Yes | Yes | Pass |
| Robert Diaz | Database Administrator | Yes | Yes | Yes | Pass |
| Daniel Cruz | IT Support Specialist | Yes | No | Yes | **Exception** |
| Maria Santos | Accountant | No | No | Yes | Pass |
| Sofia Lopez | Marketing Coordinator | No | No | Yes | Pass |

### Exception Identified

**User:** Daniel Cruz  
**Role:** IT Support Specialist  
**Department:** IT

Daniel Cruz has administrative access, but the evidence reviewed does not contain a documented business justification for the privileged access.

### Risk Assessment

**Risk Level:** Medium

Unjustified privileged access increases the risk of unauthorized system changes, inappropriate access to sensitive information, or misuse of administrative capabilities.

### Recommended Remediation

Management should:

1. Confirm whether administrative access is required for Daniel Cruz's job responsibilities.
2. Document the business justification if the access is necessary.
3. Remove unnecessary administrative privileges if the access is not required.
4. Retain evidence supporting the final access decision.

### Test Conclusion

**Result: Exception Identified**

One exception was identified during testing of the privileged access control.

The control requires remediation because one privileged account lacked documented business justification.

---

## ITGC-03 — Change Management

### Control Objective

Ensure production changes are authorized, tested, documented, and approved before implementation.

### Evidence Reviewed

* `evidence/change_management.csv`

### Testing Procedure

The change management listing was reviewed to determine whether each change had documented approval, testing evidence, and implementation documentation.

### Test Results

| Change ID | System          | Approval | Testing Evidence | Implementation Documented | Result        |
| --------- | --------------- | -------- | ---------------- | ------------------------- | ------------- |
| CHG-001   | Customer Portal | Yes      | Yes              | Yes                       | Pass          |
| CHG-002   | Database        | Yes      | Yes              | Yes                       | Pass          |
| CHG-003   | HR System       | No       | Yes              | Yes                       | **Exception** |
| CHG-004   | API Gateway     | Yes      | No               | Yes                       | **Exception** |
| CHG-005   | File Server     | Yes      | Yes              | No                        | **Exception** |
| CHG-006   | Customer Portal | Yes      | Yes              | Yes                       | Pass          |

### Exceptions Identified

**CHG-003 — HR System**

The change did not have documented approval before implementation.

**CHG-004 — API Gateway**

The evidence reviewed did not contain documented testing evidence for the change.

**CHG-005 — File Server**

The evidence reviewed did not contain documented implementation documentation.

### Risk Assessment

**Risk Level:** Medium

Insufficient change management documentation or approval increases the risk of unauthorized, untested, or improperly implemented changes affecting system availability, security, or data integrity.

### Recommended Remediation

Management should:

1. Require documented approval before production changes are implemented.
2. Retain evidence that changes were tested before implementation.
3. Maintain implementation documentation for production changes.
4. Periodically review change records for compliance with the change management process.

### Automated Test Result

The PowerShell testing script identified:

* **Records Tested:** 6
* **Passed:** 3
* **Exceptions:** 3
* **Control Result:** Exception

### Test Conclusion

**Result: Exception Identified**

Three exceptions were identified during testing of the change management control.

The control requires remediation because three changes lacked one or more required elements of the change management process.

Audit Scope
      ↓
Controls Tested
      ↓
Exceptions Identified
      ↓
Risk Assessment
      ↓
Overall Findings
      ↓
Remediation Recommendations
      ↓
Retesting

---

# Final ITGC Audit Summary

## Audit Overview

**Organization:** CaribeTech Services
**Industry:** SaaS / Business Services
**Audit Period:** January–June 2026
**Audit Type:** IT General Controls Review

The audit evaluated four IT General Controls covering user access, privileged access, change management, and user termination.

Testing was performed using simulated audit evidence and PowerShell-based automated testing procedures.

## Overall Testing Results

| Control   | Area                         | Records Tested | Exceptions | Result                    |
| --------- | ---------------------------- | -------------: | ---------: | ------------------------- |
| ITGC-01   | User Access Management       |              7 |          1 | Exception                 |
| ITGC-02   | Privileged Access Management |              5 |          1 | Exception                 |
| ITGC-03   | Change Management            |              6 |          3 | Exception                 |
| ITGC-04   | User Termination             |              6 |          1 | Exception                 |
| **Total** |                              |         **24** |      **6** | **Exceptions Identified** |

## Key Findings

Six exceptions were identified across the 24 records tested.

### User Access Management

One user account lacked documented manager approval.

**Risk:** Unsupported access could result in inappropriate access to organizational systems or information.

### Privileged Access Management

One privileged account lacked documented business justification.

**Risk:** Unjustified administrative access increases the risk of unauthorized system changes or inappropriate access to sensitive information.

### Change Management

Three changes lacked one or more required control elements:

* One change lacked documented approval.
* One change lacked testing evidence.
* One change lacked implementation documentation.

**Risk:** Inadequately controlled changes increase the risk of unauthorized, untested, or improperly implemented changes affecting system security, availability, or data integrity.

### User Termination

One terminated employee's account was disabled two days after the termination date.

**Risk:** Delayed account termination creates a period during which a former user may retain access to organizational systems or information.

## Recommended Remediation

Management should:

1. Ensure user access is supported by documented management approval.
2. Require documented business justification for privileged access.
3. Require production changes to have appropriate approval, testing evidence, and implementation documentation before or during implementation.
4. Ensure terminated users have their system access disabled promptly.
5. Retain supporting evidence for control reviews and remediation activities.
6. Perform follow-up testing to verify that identified exceptions have been remediated.

## Overall Conclusion

The simulated ITGC review identified control exceptions across all four areas tested.

The testing demonstrated a repeatable audit workflow:

> **Control → Evidence → Testing → Finding → Risk → Remediation → Retest**

PowerShell automation was used to evaluate evidence and identify control exceptions, while the audit workpaper documented the testing procedures, findings, risk considerations, and remediation recommendations.

This project demonstrates practical experience with ITGC control testing, evidence evaluation, exception identification, risk assessment, remediation planning, and audit documentation.
