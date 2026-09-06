package riskascode

import rego.v1

default decision := "pass"

decision := "escalate" if {
    some risk in input.risks
    risk.status == "Open"
    risk.likelihood * risk.impact >= 10
}

violations contains {
    "id": risk.id,
    "reason": "Open High/Critical risk requires escalation",
    "score": risk.likelihood * risk.impact,
} if {
    some risk in input.risks
    risk.status == "Open"
    risk.likelihood * risk.impact >= 10
}

violations contains {
    "id": risk.id,
    "reason": "Risk score exceeds 25-point scale",
    "score": risk.likelihood * risk.impact,
} if {
    some risk in input.risks
    risk.likelihood < 1
}

violations contains {
    "id": risk.id,
    "reason": "Risk score exceeds 25-point scale",
    "score": risk.likelihood * risk.impact,
} if {
    some risk in input.risks
    risk.likelihood > 5
}
