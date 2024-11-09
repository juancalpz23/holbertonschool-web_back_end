-- Script to create a function SafeDiv

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    RETURN IF(b = 0, 0, a / b);
END $$

DELIMITER ;
