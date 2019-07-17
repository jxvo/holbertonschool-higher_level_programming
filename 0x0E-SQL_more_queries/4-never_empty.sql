-- Create a table with a default ID of 1 (can't be NULL)
CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256));
