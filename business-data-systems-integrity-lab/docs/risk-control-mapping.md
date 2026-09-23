# Risk and Control Mapping

## Status mismatch
**Risk:** Incorrect customer status may affect downstream workflows, reporting, service eligibility, or decisions.  
**Control objective:** Maintain accurate and consistent customer master data.  
**Evidence:** SQL status-mismatch output.  
**Remediation:** Confirm the authoritative source and reconcile the downstream record.  
**Validation:** Re-run the comparison.

## Balance mismatch
**Risk:** Incorrect financial or management reporting.  
**Control objective:** Preserve data accuracy across integrations and transformations.  
**Evidence:** SQL balance comparison output.  
**Remediation:** Reconcile against the approved source and investigate the integration path.  
**Validation:** Re-run the comparison.

## Missing downstream record
**Risk:** Incomplete reporting or downstream processing.  
**Control objective:** Ensure expected records transfer successfully.  
**Evidence:** SQL missing-record output.  
**Remediation:** Trace the record through the integration process.  
**Validation:** Confirm the record exists and is correct.

## Duplicate downstream record
**Risk:** Duplicate processing or inflated reporting.  
**Control objective:** Maintain record uniqueness.  
**Evidence:** SQL duplicate-detection output.  
**Remediation:** Determine the authoritative record and remove/merge the duplicate through approved procedure.  
**Validation:** Re-run the duplicate check.

## Stale downstream record
**Risk:** Users may act on outdated information.  
**Control objective:** Ensure timely synchronization.  
**Evidence:** SQL timestamp comparison output.  
**Remediation:** Investigate synchronization timing or integration failure.  
**Validation:** Confirm synchronization meets the defined tolerance.

## Operating model
**Assess -> Verify -> Remediate -> Document**
