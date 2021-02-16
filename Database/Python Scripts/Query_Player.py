import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_procedure

'''
Create Procedures
'''
'''
Function that creates procedure query all Player enitiy based on Player_ID
'''
def create_query_all_player_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_pid'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_pid(p_id int)
            BEGIN
               SELECT *
               FROM Player
               Where Player_ID = p_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Player_Pid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Player_Pid Failed")
    else:
        raise Exception("Procedure Query_All_Player_Pid does exists")

'''
Function that creates procedure query all Player enitiy based on Player_Name and Date of Birth
'''
def create_query_all_player_name_dob():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_name_dob'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_name_dob(name varchar(45), abv varchar(3))
            BEGIN
               SELECT *
               FROM Player
               Where Player_Name = name 
               AND Player_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Player_Name_dob was Successful")
        except:
            raise Exception("Create Procedure Query_All_Player_Name_dob Failed")
    else:
        raise Exception("Procedure Query_All_Player_Name_dob does exists")

'''
Function that creates procedure that queries Player for Player_ID based on Player_name
'''
def create_query_player_name():
      # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_name'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_name(name varchar(100))
            BEGIN
               SELECT Player_ID
               FROM Player
               Where Player_Name = name;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Name was Successful")
        except:
            raise Exception("Create Procedure Query_Player_Name Failed")
    else:
        raise Exception("Procedure Query_Player_Name does  exists")

'''
Function that calls all player query creation
'''
def create_player_query():
    create_query_all_player_pid()
    create_query_all_player_name_dob()
    create_query_player_name()

'''
Drop Procedures
'''
'''
Function that drops procedure query_all_player_pid
'''
def drop_query_all_player_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_pid'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Pid Failed")
    else:
        raise Exception("Procedure Query_All_Player_Pid does not Exists")

'''
Function that drops procedure query_all_player_name_dob
'''
def drop_query_all_player_name_dob():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_name_dob'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_name_dob
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Name_DOB was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Name_DOB Failed")
    else:
        raise Exception("Procedure Query_All_Player_Name_DOB does not Exists")

'''
Function that drops procedure query_player_name
'''
def drop_query_player_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_name'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_name
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Name was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Name Failed")
    else:
        raise Exception("Procedure Query_Player_Name does not Exists")

'''
Function that calls all drop player query
'''
def drop_player_query():
    drop_query_all_player_pid()
    drop_query_all_player_name_dob()
    drop_query_player_name()

'''
Main Function 
'''
def main():
    create_player_query()
    drop_player_query()

main()

