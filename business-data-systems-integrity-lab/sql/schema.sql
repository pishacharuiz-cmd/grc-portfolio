CREATE TABLE crm_customers (
 customer_id TEXT PRIMARY KEY, customer_name TEXT NOT NULL, status TEXT NOT NULL, balance REAL NOT NULL, last_updated TEXT NOT NULL
);
CREATE TABLE operational_customers (
 customer_id TEXT, customer_name TEXT NOT NULL, status TEXT NOT NULL, balance REAL NOT NULL, last_updated TEXT NOT NULL
);