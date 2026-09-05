package ai.governance_test

import rego.v1

import data.ai.governance

# Safe low-risk request should be allowed.
allow_safe_request if {
    governance.allow with input as {
        "contains_pii": false,
        "data_classification": "internal",
        "pii_masked": true,
        "destination_type": "internal",
        "approved_vendor": true,
        "fairness_score": 0.92,
        "use_case_risk": "low",
        "human_approval": false
    }
}

# Restricted PII must be denied when it is unmasked.
deny_unmasked_pii if {
    not governance.allow with input as {
        "contains_pii": true,
        "data_classification": "restricted",
        "pii_masked": false,
        "destination_type": "internal",
        "approved_vendor": true,
        "fairness_score": 0.92,
        "use_case_risk": "low",
        "human_approval": false
    }
}

# External third-party vendor must be approved.
deny_unapproved_vendor if {
    not governance.allow with input as {
        "contains_pii": false,
        "data_classification": "internal",
        "pii_masked": true,
        "destination_type": "external_third_party",
        "approved_vendor": false,
        "fairness_score": 0.92,
        "use_case_risk": "low",
        "human_approval": false
    }
}

# Fairness score below threshold must be denied.
deny_low_fairness if {
    not governance.allow with input as {
        "contains_pii": false,
        "data_classification": "internal",
        "pii_masked": true,
        "destination_type": "internal",
        "approved_vendor": true,
        "fairness_score": 0.79,
        "use_case_risk": "low",
        "human_approval": false
    }
}

# High-risk AI use requires human approval.
deny_missing_human_approval if {
    not governance.allow with input as {
        "contains_pii": false,
        "data_classification": "internal",
        "pii_masked": true,
        "destination_type": "internal",
        "approved_vendor": true,
        "fairness_score": 0.92,
        "use_case_risk": "high",
        "human_approval": false
    }
}
