# Basic SQL Lab

## Overview
A simple collection of foundational SQL queries used for basic data extraction, user auditing, and compliance checks. 

---

## What This Demonstrates
* **Filtering Data:** Using `WHERE` clauses to isolate specific risks or inactive accounts.
* **Sorting Results:** Using `ORDER BY` to prioritize the most recent or highest-risk items.
* **Basic Aggregation:** Using `COUNT` to summarize records for compliance reports.

---

## Lab Queries

### 1. Finding Inactive User Accounts
**Objective:** Pull a list of users who haven't logged in recently to check for dormant accounts.

```sql
SELECT username, department, last_login_date
FROM users
WHERE account_status = 'Active' 
  AND last_login_date < '2026-01-01'
ORDER BY last_login_date ASC;
