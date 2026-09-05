package ai.governance

import rego.v1

default allow := false

default risk_tier := "high"

default policy_version := "1.1"

# Risk tier is driven by the declared use case.
risk_tier := "high" if input.use_case_risk == "high"
risk_tier := "medium" if input.use_case_risk == "medium"
risk_tier := "low" if input.use_case_risk == "low"

# Governance decision requires the request to declare the fields needed for review.
required_fields := {
    "use_case_risk",
    "data_classification",
    "destination_type",
    "fairness_score"
}

violation contains "missing_required_governance_field" if {
    field := required_fields[_]
    not input[field]
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

# Fairness control: 0.80 is a portfolio-configured gate, not a regulatory threshold.
violation contains "fairness_threshold_failed" if {
    input.fairness_score < 0.80
}

# High-risk use cases require human approval.
violation contains "human_oversight_required" if {
    risk_tier == "high"
    input.human_approval != true
}

# Produce a single auditable decision object.
decision := {
    "allow": allow,
    "risk_tier": risk_tier,
    "violations": sort([v | v := violation[_]]),
    "policy_version": policy_version
}

# A request is allowed only when every applicable control passes.
allow if count(violation) == 0
