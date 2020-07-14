-- list all records with respective names
-- show all the record data labeled with name in second table
SELECT score, name FROM second_table WHERE name IS NOT NULL 
    ORDER BY score DESC;
