import re
import json

# Simulated authentication log lines mimicking secure payment gateway logs
LOG_DATA = [
    "2026-08-31T12:01:00Z auth_service[101]: INFO Successful login for user admin from 192.168.1.50",
    "2026-08-31T12:05:12Z auth_service[101]: ERROR Failed login attempt for user root from 203.0.113.42",
    "2026-08-31T12:05:15Z auth_service[101]: ERROR Failed login attempt for user root from 203.0.113.42",
    "2026-08-31T12:05:18Z auth_service[101]: ERROR Failed login attempt for user root from 203.0.113.42",
    "2026-08-31T12:05:22Z auth_service[101]: CRITICAL Multiple login failures threshold breached for IP 203.0.113.42"
]

def parse_security_logs():
    brute_force_indicators = []
    failed_attempts = {}

    for line in LOG_DATA:
        if "Failed login" in line:
            ip_match = re.search(r'from\s+([0-9.]+)', line)
            if ip_match:
                ip = ip_match.group(1)
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    # PCI DSS Requirement 10.2.4: Invalid logical access attempts tracking
    for ip, count in failed_attempts.items():
        if count >= 3:
            brute_force_indicators.append({
                "alert": "Potential Brute Force Attack",
                "source_ip": ip,
                "failed_attempts": count,
                "pci_dss_requirement": "10.2.4 - Invalidation of logical access attempts"
            })

    print(json.dumps(brute_force_indicators, indent=4))

if __name__ == "__main__":
    parse_security_logs()