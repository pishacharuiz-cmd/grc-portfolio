package ai.governance

import rego.v1

default allow := false

default risk_tier := "high"

# Risk tier is driven by the declared use case.
risk_tier := "high" if {
    input.use_case_risk == "high"
}

risk_tier := "medium" if {
    input.use_case_risk == "medium"
}

risk_tier := "low" if {
    input.use_case_risk == "low"
}

# Privacy control: restricted data with unmasked PII is denied.
violation contains "restricted_data_pii" if {
    input.contains_pii == true
    input.data_classification == "restricted"
    input.pii_masked != true
}

# Vendor control: external third-party models must be approved.
violation contains "unapproved_external_vendor" if {
    input.destination_type == "external_third_party"
    input.approved_vendor != true
}

# Fairness control: a fairness validation score must meet the configured threshold.
violation contains "fairness_threshold_failed" if {
    input.fairness_score < 0.80
}

# High-risk use cases require human approval.
violation contains "human_oversight_required" if {
    risk_tier == "high"
    input.human_approval != true
}

# A request is allowed only when every applicable control passes.
allow if {
    count(violation) == 0
}
