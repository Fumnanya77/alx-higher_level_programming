-- joining tables without the word join
USE hbtn_0d_usa;
SELECT * FROM hbtn_0d_usa.cities WHERE state_id IN (SELECT * FROM hbtn_0d_usa.states WHERE name = "california");
