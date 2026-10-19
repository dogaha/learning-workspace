-- Products Table
-- id, name, category, is_available

-- Requests Table
-- product_id, client_email

-- Result: 
--  name | category | total_requests
--  sorted in descending order by total_requests
--  Ascending by name
--  Ascending by category

--  ONLY available products should be included

SELECT
    p.name as name,
    p.category as category,
    COUNT(r.product_id) as total_requests
FROM Products p
LEFT JOIN Requests r
    ON r.product_id = p.id
WHERE p.is_available = 1
GROUP BY p.id, p.name, p.category
ORDER BY total_requests DESC, name ASC, category ASC
    