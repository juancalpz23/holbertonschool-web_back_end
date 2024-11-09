-- Script to create a stored procedure AddBonus

DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- Check if project exists; if not, insert it
    IF NOT EXISTS (SELECT 1 FROM projects WHERE name = project_name) THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    -- Insert the new correction with the given user_id, project_id, and score
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (
        user_id,
        (SELECT id FROM projects WHERE name = project_name),
        score
    );
END $$

DELIMITER ;
