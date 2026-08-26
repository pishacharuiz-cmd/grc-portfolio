import yaml
import sys

def load_risk_register(filepath):
    try:
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: Risk register file '{filepath}' not found.")
        sys.exit(1)

def evaluate_risks(data):
    print(f"==================================================")
    print(f" Evaluating Risk Register: {data.get('project', 'Unknown')}")
    print(f" Framework Alignment: {data.get('framework', 'N/A')}")
    print(f"==================================================\\n")
    
    high_risk_threshold = 12  # Threshold for critical escalation
    open_critical_count = 0
    
    for risk in data.get('risks', []):
        score = risk['likelihood'] * risk['impact']
        print(f"[{risk['id']}] {risk['category']} | Status: {risk['status']}")
        print(f"  Description: {risk['description']}")
        print(f"  Risk Score: {score} (Likelihood: {risk['likelihood']} x Impact: {risk['impact']})")
        
        if score >= high_risk_threshold and risk['status'] == 'Open':
            print(f"  --> [CRITICAL ALERT]: Unmitigated high risk detected! Escalation required.")
            open_critical_count += 1
        print("-" * 50)
        
    print(f"\\nEvaluation Complete. Total Critical Open Risks: {open_critical_count}")
    if open_critical_count > 0:
        sys.exit(2)  # Fail pipeline if critical unmitigated risks exist

if __name__ == "__main__":
    risk_data = load_risk_register('risks.yaml')
    evaluate_risks(risk_data)