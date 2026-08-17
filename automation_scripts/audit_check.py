import json

# Load the control framework file
with open("controls.json", "r") as file:
    data = json.load(file)

print("--- GRC AUDIT STATUS REPORT ---")
compliant_count = 0
total_controls = len(data["controls"])

# Loop through controls and check compliance status
for control in data["controls"]:
    print(f"Checking Control [{control['id']} - {control['name']}]: {control['status']}")
    if control["status"] == "Implemented":
        compliant_count += 1

# Summary calculation
print("-" * 31)
print(f"Total Controls: {total_controls}")
print(f"Compliant: {compliant_count}")
print(f"Non-Compliant / Pending: {total_controls - compliant_count}")