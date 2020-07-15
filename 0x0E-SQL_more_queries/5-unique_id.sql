-- creates a table with unique ids
-- creates the table unique_id with default & unique 1
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
