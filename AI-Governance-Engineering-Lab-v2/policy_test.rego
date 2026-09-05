package ai.governance_test

import rego.v1
import data.ai.governance

base_input := {
    "contains_pii": false,
    "data_classification": "internal",
    "pii_masked": true,
    "destination_type": "internal",
    "approved_vendor": true,
    "fairness_score": 0.92,
    "use_case_risk": "low",
    "human_approval": false
}

test_allow_safe_request if governance.allow with input as base_input

test_deny_unmasked_pii if not governance.allow with input as object.union(base_input, {
    "contains_pii": true,
    "data_classification": "restricted",
    "pii_masked": false
})

test_deny_unapproved_vendor if not governance.allow with input as object.union(base_input, {
    "destination_type": "external_third_party",
    "approved_vendor": false
})

test_deny_low_fairness if not governance.allow with input as object.union(base_input, {
    "fairness_score": 0.79
})

test_deny_missing_human_approval if not governance.allow with input as object.union(base_input, {
    "use_case_risk": "high",
    "human_approval": false
})

test_allow_high_risk_with_approval if governance.allow with input as object.union(base_input, {
    "use_case_risk": "high",
    "human_approval": true
})

test_deny_multiple_violations if {
    result := governance.decision with input as object.union(base_input, {
        "contains_pii": true,
        "data_classification": "restricted",
        "pii_masked": false,
        "destination_type": "external_third_party",
        "approved_vendor": false,
        "fairness_score": 0.50,
        "use_case_risk": "high",
        "human_approval": false
    })
    result.allow == false
    count(result.violations) == 4
}

test_decision_contains_policy_version if {
    result := governance.decision with input as base_input
    result.policy_version == "1.1"
}
