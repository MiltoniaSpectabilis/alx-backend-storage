-- Create a trigger to reset the attribute valid_email only when the email has been changed
DELIMITER //
CREATE TRIGGER trg_reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email!= OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END//
DELIMITER ;
