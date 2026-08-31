import json

# Simulated AWS Security Group and S3 Bucket configurations from a Terraform plan or AWS API output
INFRA_CONFIG = {
    "resources": [
        {
            "resource_id": "sg-payment-database",
            "type": "aws_security_group",
            "ingress_rules": [
                {"port": 5432, "source": "10.0.0.0/16", "description": "Internal VPC Only"},
                {"port": 22, "source": "0.0.0.0/0", "description": "Unrestricted SSH Access"} # Violation
            ]
        },
        {
            "resource_id": "s3-payment-vault-logs",
            "type": "aws_s3_bucket",
            "public_access_block": {
                "block_public_acls": True,
                "block_public_policy": False # Violation
            },
            "encryption": "AES256"
        }
    ]
}

def audit_pci_cloud_controls():
    violations = []
    
    for resource in INFRA_CONFIG["resources"]:
        # Check Security Groups (Requirement 1)
        if resource["type"] == "aws_security_group":
            for rule in resource["ingress_rules"]:
                if rule["source"] == "0.0.0.0/0":
                    violations.append({
                        "resource": resource["resource_id"],
                        "control_failed": "Unrestricted Ingress from Internet",
                        "port": rule["port"],
                        "pci_dss_req": "Req 1.4.1 - Restrict inbound traffic to CDE"
                    })
                    
        # Check S3 Buckets (Requirement 3 & 4)
        elif resource["type"] == "aws_s3_bucket":
            if not resource["public_access_block"]["block_public_policy"]:
                violations.append({
                    "resource": resource["resource_id"],
                    "control_failed": "S3 Public Access Policy Not Fully Blocked",
                    "pci_dss_req": "Req 3.1.2 - Storage minimization and protection of cardholder data"
                })

    if violations:
        print("[!] PCI DSS Cloud Control Audit Failed:")
        print(json.dumps(violations, indent=4))
    else:
        print("[+] Cloud Control Audit Passed: All resources compliant.")

if __name__ == "__main__":
    audit_pci_cloud_controls()