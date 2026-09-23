import csv
import sqlite3
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "business_integrity.db"
EVIDENCE = ROOT / "evidence" / "integrity_report.md"

if DB.exists():
    DB.unlink()

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.executescript((ROOT / "sql" / "schema.sql").read_text())

def load_csv(path, table):
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    cur.executemany(
        f"INSERT INTO {table} VALUES (?, ?, ?, ?, ?)",
        [(r["customer_id"], r["customer_name"], r["status"],
          float(r["balance"]), r["last_updated"]) for r in rows],
    )
    return len(rows)

crm_count = load_csv(ROOT / "data/crm_customers.csv", "crm_customers")
ops_count = load_csv(ROOT / "data/operational_customers.csv", "operational_customers")

queries = {
    "Status mismatches": """SELECT c.customer_id,c.status,o.status
        FROM crm_customers c JOIN operational_customers o
        ON c.customer_id=o.customer_id WHERE c.status<>o.status""",
    "Balance mismatches": """SELECT c.customer_id,c.balance,o.balance
        FROM crm_customers c JOIN operational_customers o
        ON c.customer_id=o.customer_id
        WHERE ABS(c.balance-o.balance)>0.01""",
    "Missing downstream records": """SELECT c.customer_id,c.customer_name
        FROM crm_customers c LEFT JOIN operational_customers o
        ON c.customer_id=o.customer_id WHERE o.customer_id IS NULL""",
    "Duplicate downstream records": """SELECT customer_id,COUNT(*)
        FROM operational_customers GROUP BY customer_id HAVING COUNT(*)>1""",
    "Stale downstream records": """SELECT c.customer_id,c.last_updated,o.last_updated
        FROM crm_customers c JOIN operational_customers o
        ON c.customer_id=o.customer_id WHERE o.last_updated<c.last_updated""",
}

results = {name: cur.execute(query).fetchall() for name, query in queries.items()}
total_issues = sum(len(rows) for rows in results.values())
affected_ids = {row[0] for rows in results.values() for row in rows}

report = [
    "# Business Data & Systems Integrity Report",
    "",
    f"Generated: {datetime.now().isoformat(timespec='seconds')}",
    "",
    "## Scope",
    f"- CRM records analyzed: {crm_count}",
    f"- Operational records analyzed: {ops_count}",
    f"- Validation tests executed: {len(queries)}",
    f"- Findings detected: {total_issues}",
    f"- Unique affected customer IDs: {len(affected_ids)}",
    "",
    "## Findings",
]

for name, rows in results.items():
    report += ["", f"### {name}: {len(rows)}"]
    if rows:
        report += [f"- {row}" for row in rows]
    else:
        report.append("No issues detected.")

report += [
    "",
    "## Assessment",
    "",
    "Cross-system data inconsistencies were identified. The next step is to verify "
    "the authoritative source for each field, reconcile confirmed discrepancies, "
    "investigate the integration path, and rerun the validation checks as evidence "
    "of remediation.",
]

EVIDENCE.parent.mkdir(exist_ok=True)
EVIDENCE.write_text("\n".join(report), encoding="utf-8")

print("=== BUSINESS DATA & SYSTEMS INTEGRITY LAB ===")
print(f"CRM records: {crm_count}")
print(f"Operational records: {ops_count}")
print(f"Findings: {total_issues}")
print(f"Unique affected IDs: {len(affected_ids)}")
for name, rows in results.items():
    print(f"{name}: {len(rows)}")
    for row in rows:
        print(f"  {row}")
print(f"Evidence written to: {EVIDENCE.relative_to(ROOT)}")
conn.close()
