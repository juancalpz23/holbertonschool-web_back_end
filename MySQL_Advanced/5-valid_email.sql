-- Script to create a trigger that resets valid_email when the email is changed
-- This trigger updates valid_email to 0 whenever a user's email address is modified.

CREATE TRIGGER reset_valid_email_before_update
BEFORE UPDATE ON users
FOR EACH ROW
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;