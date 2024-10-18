-- Create a view need_meeting to list all students that have a score under 80 and no last_meeting or more than 1 month
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80 AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
