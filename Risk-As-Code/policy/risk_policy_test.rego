package riskascode_test

import rego.v1

mock_input := {
  "risks": [
    {"id": "RISK-001", "likelihood": 4, "impact": 5, "status": "Open"},
    {"id": "RISK-002", "likelihood": 3, "impact": 4, "status": "Open"},
    {"id": "RISK-003", "likelihood": 2, "impact": 3, "status": "Mitigated"}
  ]
}

test_open_high_risk_escalates if {
  data.riskascode.decision with input as mock_input == "escalate"
}

test_open_high_risk_is_reported if {
  violations := data.riskascode.violations with input as mock_input
  {"id": "RISK-001", "reason": "Open High/Critical risk requires escalation", "score": 20} in violations
}
