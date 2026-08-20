import unittest
from src.auditor import audit_s3_buckets

class TestS3Auditor(unittest.TestCase):
    
    def test_compliant_bucket(self):
        mock_data = {
            "s3_buckets": [
                {"bucket_name": "secure-bucket", "encryption_enabled": True, "public_access_blocked": True}
            ]
        }
        results = audit_s3_buckets(mock_data)
        self.assertEqual(results[0]["status"], "PASSED")
        self.assertEqual(len(results[0]["violations"]), 0)

    def test_non_compliant_bucket(self):
        mock_data = {
            "s3_buckets": [
                {"bucket_name": "insecure-bucket", "encryption_enabled": False, "public_access_blocked": False}
            ]
        }
        results = audit_s3_buckets(mock_data)
        self.assertEqual(results[0]["status"], "FAILED")
        self.assertEqual(len(results[0]["violations"]), 2)

if __name__ == "__main__":
    unittest.main()