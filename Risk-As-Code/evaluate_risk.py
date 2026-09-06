import argparse
import json
import sys
from pathlib import Path

import yaml

VALID_STATUSES = {"Open", "Mitigated", "Accepted", "Closed"}


def load_risk_register(filepath):
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Risk register file not found: {filepath}")
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}
    validate_register(data)
    return data


def validate_register(data):
    if not isinstance(data, dict):
        raise ValueError("Risk register must be a YAML object.")
    if not data.get("project"):
        raise ValueError("Missing required field: project")
    if not data.get("framework"):
        raise ValueError("Missing required field: framework")
    if not isinstance(data.get("risks"), list):
        raise ValueError("Missing required list: risks")
    ids = set()
    for risk in data["risks"]:
        required = {"id", "category", "description", "likelihood", "impact", "status", "mitigation"}
        missing = required - set(risk)
        if missing:
            raise ValueError(f"{risk.get('id', '<unknown>')} missing: {', '.join(sorted(missing))}")
        if risk["id"] in ids:
            raise ValueError(f"Duplicate risk ID: {risk['id']}")
        ids.add(risk["id"])
        if not (1 <= int(risk["likelihood"]) <= 5 and 1 <= int(risk["impact"]) <= 5):
            raise ValueError(f"{risk['id']} likelihood and impact must be 1-5")
        if risk["status"] not in VALID_STATUSES:
            raise ValueError(f"{risk['id']} has invalid status: {risk['status']}")


def score_risk(risk):
    return int(risk["likelihood"]) * int(risk["impact"])


def rating_for_score(score):
    if score >= 16:
        return "Critical"
    if score >= 10:
        return "High"
    if score >= 5:
        return "Medium"
    return "Low"


def evaluate_risks(data):
    results = []
    for risk in data["risks"]:
        score = score_risk(risk)
        rating = rating_for_score(score)
        escalation = rating in {"Critical", "High"} and risk["status"] == "Open"
        results.append({
            "id": risk["id"],
            "category": risk["category"],
            "status": risk["status"],
            "score": score,
            "rating": rating,
            "escalation_required": escalation,
            "description": risk["description"],
            "mitigation": risk["mitigation"],
        })
    return results


def print_report(data, results):
    print("=" * 72)
    print(f"Risk-as-Code Evaluation: {data['project']}")
    print(f"Framework: {data['framework']}")
    print("=" * 72)
    for item in results:
        print(f"[{item['id']}] {item['category']} | {item['status']} | {item['rating']} ({item['score']})")
        print(f"  {item['description']}")
        print(f"  Mitigation: {item['mitigation']}")
        if item["escalation_required"]:
            print("  --> ESCALATION REQUIRED: Open High/Critical risk")
        print("-" * 72)
    open_escalations = sum(r["escalation_required"] for r in results)
    print(f"Open High/Critical Risks Requiring Escalation: {open_escalations}")


def main():
    parser = argparse.ArgumentParser(description="Evaluate a YAML GRC risk register.")
    parser.add_argument("register", nargs="?", default="risks.yaml")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    parser.add_argument("--fail-on-escalation", action="store_true", help="Exit 2 when open High/Critical risks exist")
    args = parser.parse_args()
    try:
        data = load_risk_register(args.register)
        results = evaluate_risks(data)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps({"project": data["project"], "framework": data["framework"], "results": results}, indent=2))
    else:
        print_report(data, results)
    if args.fail_on_escalation and any(r["escalation_required"] for r in results):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
