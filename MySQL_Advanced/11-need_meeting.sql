-- Script to create a view need_meeting
-- This view lists students who have a score under 80 and have not had a meeting or had one more than 1 month ago.

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);