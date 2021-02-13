import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_procedure

'''
Create procedure
'''
'''
Function that creates procedure to delete all tables
'''
def create_drop_table_procedure():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('drop_all_tables'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE `drop_all_tables`()
            BEGIN
                DECLARE _done INT DEFAULT FALSE;
                DECLARE _tableName VARCHAR(255);
                DECLARE _cursor CURSOR FOR
                    SELECT table_name 
                    FROM information_schema.TABLES
                    WHERE table_schema = SCHEMA();
                DECLARE CONTINUE HANDLER FOR NOT FOUND SET _done = TRUE;

                SET FOREIGN_KEY_CHECKS = 0;

                OPEN _cursor;

                REPEAT FETCH _cursor INTO _tableName;

                IF NOT _done THEN
                    SET @stmt_sql = CONCAT('DROP TABLE ', _tableName);
                    PREPARE stmt1 FROM @stmt_sql;
                    EXECUTE stmt1;
                    DEALLOCATE PREPARE stmt1;
                END IF;

                UNTIL _done END REPEAT;

                CLOSE _cursor;
                SET FOREIGN_KEY_CHECKS = 1;
                END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Drop_All_Tables was Successful")
        except:
            raise Exception("Create Procedure Drop_All_Tables Failed")
    else:
        raise Exception("Procedure Drop_All_Table already exists")

'''
Function that creates procedure to truncate a table
'''
def create_truncate_table_procedure():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('drop_all_tables'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE Truncate_If_Exist(IN Tbl_Name VARCHAR(150) )
            BEGIN
                IF EXISTS( SELECT 1 FROM Information_Schema.TABLES WHERE table_name = Tbl_Name AND Table_Schema = DATABASE()) THEN
                SET @query = CONCAT('TRUNCATE ', Tbl_Name);
                PREPARE stmt FROM @query;
                EXECUTE stmt;
                DEALLOCATE PREPARE stmt;
                END IF;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Truncate_If_Exist was Successful")
        except:
            raise Exception("Create Procedure Truncate_If_Exist Failed")
    else:
        raise Exception("Procedure Truncate_If_Exist does  exists")

'''
Function that creates all general procedures
'''
def create_general_procedures():
    create_drop_table_procedure()
    create_truncate_table_procedure()
    
'''
Drop Procedure
'''
'''
Function that drops a procedure drop_table
'''
def drop_procedure_drop_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()
    if check_procedure('drop_all_tables'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE 
            IF EXISTS drop_all_tables
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure drop_all_tables was Successful")
        except:
            raise Exception("Drop procedure drop_all_tables Failed")
    else:
        raise Exception("Procedure drop_all_tables does not exists")

'''
Function that drops procedure truncate_if_exists
'''
def drop_procedure_truncate_if_exist():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()
    if check_procedure('Truncate_If_Exist'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE 
            IF EXISTS Truncate_If_Exist
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Truncate_If_Exist was Successful")
        except:
            raise Exception("Drop procedure Truncate_If_Exist Failed")
    else:
        raise Exception("Procedure Truncate_If_Exist does not exists")

'''
Function that drops all general procedures 
'''
def drop_general_procedures():
    drop_procedure_truncate_if_exist()
    drop_procedure_drop_table()
'''
Main Function
'''
def main():
    create_truncate_table_procedure()
main()