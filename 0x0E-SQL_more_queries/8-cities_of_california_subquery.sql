-- joining tables without the word join
SELECT * FROM cities WHERE state_id IN (SELECT * FROM states WHERE name = "california");
