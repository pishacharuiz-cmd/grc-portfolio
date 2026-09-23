-- Status mismatch
SELECT c.customer_id,c.status AS source_status,o.status AS operational_status
FROM crm_customers c JOIN operational_customers o ON c.customer_id=o.customer_id
WHERE c.status<>o.status;

-- Balance mismatch
SELECT c.customer_id,c.balance AS source_balance,o.balance AS operational_balance
FROM crm_customers c JOIN operational_customers o ON c.customer_id=o.customer_id
WHERE ABS(c.balance-o.balance)>0.01;

-- Missing downstream record
SELECT c.customer_id,c.customer_name FROM crm_customers c
LEFT JOIN operational_customers o ON c.customer_id=o.customer_id
WHERE o.customer_id IS NULL;

-- Duplicate downstream record
SELECT customer_id,COUNT(*) AS record_count FROM operational_customers
GROUP BY customer_id HAVING COUNT(*)>1;

-- Stale downstream record
SELECT c.customer_id,c.last_updated AS source_updated,o.last_updated AS operational_updated
FROM crm_customers c JOIN operational_customers o ON c.customer_id=o.customer_id
WHERE o.last_updated<c.last_updated;
