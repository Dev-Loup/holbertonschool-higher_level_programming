-- California state table
-- show the california cities
SELECT id, name FROM cities WHERE state_id = (
    SELECT id FROM states WHERE name = "California"
);
