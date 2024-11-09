-- Script to create a trigger that resets valid_email when the email is changed
-- This trigger updates valid_email to 0 whenever a user's email address is modified.

DELIMITER $$

CREATE TRIGGER new_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
	SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;