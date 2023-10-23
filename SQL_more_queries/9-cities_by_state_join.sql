--Script that lists all citites CONTAINED in the database
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.states_id = states_id
ORDER BY cities.id ASC;
