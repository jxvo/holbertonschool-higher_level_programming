-- lists all cities contained in the usa database
SELECT cities.id, cities.name, states.name FROM cities JOIN states on states.id = cities.state_id
ORDER BY cities.id ASC;
