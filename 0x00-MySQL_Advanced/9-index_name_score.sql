-- Create a composite index idx_name_first_score on the first letter of name and score
CREATE INDEX idx_name_first_score ON names (SUBSTR(name, 1, 1), score);
