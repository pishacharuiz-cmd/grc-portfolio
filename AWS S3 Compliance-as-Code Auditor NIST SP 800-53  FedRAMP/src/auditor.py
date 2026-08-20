import json
import sys

def load_infrastructure(file_path):
    """Loads cloud infrastructure state from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Infrastructure state file not found at {file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the infrastructure state file.")
        sys.exit(1)

def audit_s3_buckets(infrastructure_data):
    """
    Audits S3 buckets against baseline security controls:
    - Control SC-13 / AC-3: Encryption must be enabled (AES-256 or aws:kms).
    - Control AC-3 / SC-7: Public access must be strictly blocked.
    """
    buckets = infrastructure_data.get("s3_buckets", [])
    audit_results = []

    print("[*] Initiating S3 Compliance Audit against NIST SP 800-53 Baselines...\n")

    for bucket in buckets:
        bucket_name = bucket.get("bucket_name")
        encryption = bucket.get("encryption_enabled", False)
        public_access_blocked = bucket.get("public_access_blocked", False)

        violations = []

        # Check Encryption (NIST SC-13)
        if not encryption:
            violations.append("NIST SP 800-53 SC-13: Storage encryption is disabled.")

        # Check Public Access Block (NIST AC-3 / SC-7)
        if not public_access_blocked:
            violations.append("NIST SP 800-53 AC-3: Public access block is disabled (Risk of exposure).")

        status = "PASSED" if not violations else "FAILED"

        audit_results.append({
            "bucket_name": bucket_name,
            "status": status,
            "violations": violations
        })

    return audit_results

def generate_report(results):
    """Prints a structured, actionable audit report to the console."""
    passed_count = sum(1 for r in results if r["status"] == "PASSED")
    failed_count = sum(1 for r in results if r["status"] == "FAILED")

    print(f"=== AUDIT SUMMARY ===")
    print(f"Total Buckets Evaluated: {len(results)}")
    print(f"Passed: {passed_count} | Failed: {failed_count}\n")

    for res in results:
        print(f"Bucket: {res['bucket_name']}")
        print(f"Status: [{res['status']}]")
        if res['violations']:
            print("  Remediation Actions Required:")
            for v in res['violations']:
                print(f"   - {v}")
        else:
            print("  All compliance checks successfully passed.")
        print("-" * 40)

if __name__ == "__main__":
    # Point to the mock infrastructure JSON file
    state_file = "src/mock_infrastructure.json"
    infra_data = load_infrastructure(state_file)
    results = audit_s3_buckets(infra_data)
    generate_report(results)