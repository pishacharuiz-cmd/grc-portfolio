package ai.governance.privacy

import rego.v1

# Default action is to deny if safety checks fail
default allow := false

# Rule 1: Deny if the payload contains unmasked Personally Identifiable Information (PII)
deny contains violation if {
    input.contains_pii == true
    input.data_classification == "restricted"
    violation := "Violation: Restricted AI input payload contains unmasked PII, violating privacy regulations (GDPR/ISO 42001)."
}

# Rule 2: Deny if data is being routed to an unapproved or third-party external model vendor
deny contains violation if {
    not input.approved_vendor == true
    input.destination_type == "external_third_party"
    violation := "Violation: Data routing to an unapproved third-party AI vendor presents unauthorized third-party risk."
}

# Rule 3: Deny if model bias or fairness validation score falls below acceptable thresholds
deny contains violation if {
    input.bias_mitigation_passed == false
    violation := "Violation: AI model training set failed automated bias and fairness validation checks."
}

# Allow request only if zero compliance violations are detected
allow if {
    count(deny) == 0
}
