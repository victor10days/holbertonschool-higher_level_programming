-- Script that lists all cities with their state name --
--
SELECT * FROM cities
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
