-- Example remediation statements. These are examples only.
-- Confirm the authoritative source and approved change procedure before modifying data.

-- UPDATE operational_customers
-- SET status=(SELECT status FROM crm_customers WHERE customer_id='C002')
-- WHERE customer_id='C002';

-- UPDATE operational_customers
-- SET balance=(SELECT balance FROM crm_customers WHERE customer_id='C004')
-- WHERE customer_id='C004';