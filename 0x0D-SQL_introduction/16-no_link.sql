-- 16. LIST RECORDS WITH RULES
-- must have name
SELECT `score`, `name` FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
