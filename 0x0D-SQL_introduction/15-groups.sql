-- 15. COUNT SAME SCORES
-- display all scores as number of instances
SELECT score, COUNT(score) AS number
FROM second_table GROUP BY score DESC;
