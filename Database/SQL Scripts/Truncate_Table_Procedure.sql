Use BasketballDB;
DROP PROCEDURE IF EXISTS Truncate_If_Exist;
DELIMITER $$

CREATE PROCEDURE Truncate_If_Exist(IN Tbl_Name VARCHAR(150) )
  BEGIN
    IF EXISTS( SELECT 1 FROM Information_Schema.TABLES WHERE table_name = Tbl_Name AND Table_Schema = DATABASE()) THEN
    SET @query = CONCAT('TRUNCATE ', Tbl_Name);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
    END IF;
  END $$

DELIMITER ;


