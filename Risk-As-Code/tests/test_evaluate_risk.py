import unittest

from evaluate_risk import evaluate_risks, rating_for_score, validate_register


class RiskEvaluationTests(unittest.TestCase):
    def test_rating_boundaries(self):
        self.assertEqual(rating_for_score(4), "Low")
        self.assertEqual(rating_for_score(5), "Medium")
        self.assertEqual(rating_for_score(10), "High")
        self.assertEqual(rating_for_score(16), "Critical")

    def test_open_high_risk_requires_escalation(self):
        data = {
            "project": "Test",
            "framework": "Test Framework",
            "risks": [{
                "id": "R-1", "category": "Access", "description": "Test",
                "likelihood": 4, "impact": 3, "status": "Open", "mitigation": "Fix"
            }]
        }
        result = evaluate_risks(data)[0]
        self.assertEqual(result["score"], 12)
        self.assertEqual(result["rating"], "High")
        self.assertTrue(result["escalation_required"])

    def test_mitigated_high_risk_does_not_escalate(self):
        data = {
            "project": "Test", "framework": "Test Framework",
            "risks": [{
                "id": "R-1", "category": "Privacy", "description": "Test",
                "likelihood": 4, "impact": 5, "status": "Mitigated", "mitigation": "Fixed"
            }]
        }
        result = evaluate_risks(data)[0]
        self.assertEqual(result["rating"], "Critical")
        self.assertFalse(result["escalation_required"])

    def test_validation_rejects_duplicate_ids(self):
        data = {"project": "Test", "framework": "Test", "risks": [
            {"id": "R-1", "category": "A", "description": "x", "likelihood": 1, "impact": 1, "status": "Open", "mitigation": "x"},
            {"id": "R-1", "category": "B", "description": "y", "likelihood": 1, "impact": 1, "status": "Open", "mitigation": "y"},
        ]}
        with self.assertRaises(ValueError):
            validate_register(data)


if __name__ == "__main__":
    unittest.main()
