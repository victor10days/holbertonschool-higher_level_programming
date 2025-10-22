-- Script that lists all cities in California from the hbtn_0d_usa database --
--
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California'
ORDER BY cities.id;
