-- joining tables
USE hbtn_0d_usa
SELECT c.id, c.name, s.name FROM hbtn_0d_usa.cities c
INNER JOIN hbtn_0d_usa.states s ON c.id = s.id
ORDER BY c.id ASC;
