-- select all cities froom California inside if your MySQL database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
