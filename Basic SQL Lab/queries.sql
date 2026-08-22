-- Step 1: Create the table
CREATE TABLE access_exceptions (
    exception_id INTEGER PRIMARY KEY,
    department TEXT,
    violation_category TEXT
);

-- Step 2: Insert a few test rows
INSERT INTO access_exceptions (department, violation_category) VALUES 
('Finance', 'Unauthorized Export'),
('Finance', 'Stale Credentials'),
('HR', 'Policy Override'),
('IT', 'Admin Share'),
('IT', 'Admin Share'),
('Finance', 'Stale Credentials');

-- Step 3: Run your query
SELECT department, COUNT(exception_id) AS total_exceptions
FROM access_exceptions
GROUP BY department
ORDER BY total_exceptions DESC;