import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_procedure


'''
Function that calls a stored procedure name drop_all_tables which 
Drops all Tables
'''
def drop_all_table():
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
            CALL drop_all_tables();
            """)
            trans.commit()
            conn.close()
            print("Delete all Tables was Successful")
        except:
            raise Exception("Delete all Tables Failed")
    else:
        raise Exception("There is no procedure named drop_all_tables")

'''
Function that drops a procedure based on an input parameter
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
Function that drops all tables and the procedure
'''
def drop_everything():
    drop_all_table()
    drop_procedure_drop_table()
    drop_procedure_truncate_if_exist()

'''
Main function
'''
def main():
    drop_everything()

if __name__ == "__main__":
    main()
    
   
