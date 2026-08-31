import hashlib
import os
import json
from datetime import datetime

CRITICAL_FILES = [
    "/etc/passwd",
    "/etc/shadow",
    "/etc/ssh/sshd_config"
]

BASELINE_FILE = "baseline_hashes.json"

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def create_baseline():
    baseline = {}
    for f in CRITICAL_FILES:
        file_hash = calculate_sha256(f)
        if file_hash:
            baseline[f] = file_hash
    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)
    print("[+] PCI DSS FIM Baseline Created Successfully.")

def verify_integrity():
    if not os.path.exists(BASELINE_FILE):
        print("[-] Baseline missing. Run create_baseline first.")
        return
    
    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)
    
    violations = []
    for filepath, old_hash in baseline.items():
        current_hash = calculate_sha256(filepath)
        if current_hash != old_hash:
            violations.append({
                "file": filepath,
                "expected": old_hash,
                "found": current_hash,
                "timestamp": datetime.utcnow().isoformat()
            })
            
    if violations:
        print("[!] ALERT: File Integrity Violation Detected!")
        print(json.dumps(violations, indent=4))
    else:
        print("[+] FIM Check Passed: No unauthorized alterations detected.")

if __name__ == "__main__":
    if not os.path.exists(BASELINE_FILE):
        create_baseline()
    else:
        verify_integrity()