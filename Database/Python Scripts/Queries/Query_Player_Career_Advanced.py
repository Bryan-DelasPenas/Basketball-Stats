import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd
import pathlib
import sys

sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')
from Helper_DB import test_connection, create_connection, check_procedure

'''
Create Procedures for reg or playoffs
'''

'''
Create Procedure that queries all from Player_Career_Advanced based on Player_ID
'''
def create_query_player_career_advanced_pid():
   # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_advanced_pid'):
        try: 
            # Create a parameterized query 
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_advanced_pid(IN val LONGTEXT, IN val_two LONGTEXT)
            BEGIN
                SELECT * 
                FROM Player_Career_Advanced
                WHERE Stat_Form = val 
                AND Player_ID = val_two;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Career_Advanced_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Career_Advanced_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Career_Advanced_Pid does exists")

'''
Create Procedure that queries all from Player_Career_Advanced based on Player_Name
'''
def create_query_player_career_advanced_pname():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_advanced_pname'):
        try: 
            # Create a parameterized query 
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_advanced_pname(IN val INT, IN val_two VARCHAR(45))
            BEGIN
                SELECT * 
                FROM Player_Career_Advanced
                WHERE Stat_Form = val 
                AND Player_Name = val_two;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Career_Advanced_Pname was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Career_Advanced_Pname Failed")
    else:
        raise Exception("Procedure Query_Player_Career_Advanced_Pname does exists")

'''
Create Procedure for reg and playoffs
'''

'''
Create Procedure that queries all from Player_Career_Advanced based on Player_ID
'''
def create_query_player_career_advanced_both_pid():
   # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_advanced_both_pid'):
        try: 
            # Create a parameterized query 
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_advanced_both_pid(IN val INT)
            BEGIN
                SELECT * 
                FROM Player_Career_Advanced
                WHERE Player_ID = val;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Career_Advanced_Both_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Career_Advanced_Both_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Career_Advanced_Both_Pid does exists")

'''
Create Procedure that queries all from Player_Career_Advanced based on Player_Name
'''
def create_query_player_career_advanced_both_pname():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_advanced_both_pname'):
        try: 
            # Create a parameterized query 
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_advanced_both_pname(IN val VARCHAR(45))
            BEGIN
                SELECT * 
                FROM Player_Career_Advanced
                WHERE Player_Name = val;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Career_Advanced_Both_Pname was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Career_Advanced_Both_Pname Failed")
    else:
        raise Exception("Procedure Query_Player_Career_Advanced_Both_Pname does exists")

'''
Create Procedure for all Player_Career_Advanced 
'''
def create_player_career_advanced_query():
    create_query_player_career_advanced_pid()
    create_query_player_career_advanced_pname()
    create_query_player_career_advanced_both_pid()
    create_query_player_career_advanced_both_pname()

'''
Drop Procedure for reg or playoffs
'''

'''
Drop Procedure query_player_career_advanced_pid
'''
def drop_query_player_career_advanced_pid():
   # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_career_advanced_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_career_advanced_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Career_Advanced_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Career_Advanced_Pid Failed")
    else:
        print("Procedure Query_Player_Career_Advanced_Pid does not Exists")

'''
Drop Procedure query_player_career_advanced_pname
'''
def drop_query_player_career_advanced_pname():
     # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_career_advanced_pname'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_career_advanced_pname
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Career_Advanced_Pname was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Career_Advanced_Pname Failed")
    else:
        print("Procedure Query_Player_Career_Advanced_Pname does not Exists")

'''
Drop Procedure for reg and playoffs 
'''

'''
Drop Procedure query_player_career_advanced_both_pid
'''
def drop_query_player_career_advanced_both_pid():
   # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_career_advanced_both_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_career_advanced_both_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Career_Advanced_Both_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Career_Advanced_Both_Pid Failed")
    else:
        print("Procedure Query_Player_Career_Advanced_Both_Pid does not Exists")

'''
Drop Procedure query_player_career_advanced_pname
'''
def drop_query_player_career_advanced_both_pname():
     # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_career_advanced_both_pname'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_career_advanced_both_pname
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Career_Advanced_Both_Pname was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Career_Advanced_Both_Pname Failed")
    else:
        print("Procedure Query_Player_Career_Advanced_Both_Pname does not Exists")

'''
Drop all Procedures for Player_Career_Advanced
'''
def drop_player_career_advanced_query():
    drop_query_player_career_advanced_pid()
    drop_query_player_career_advanced_pname()
    drop_query_player_career_advanced_both_pid()
    drop_query_player_career_advanced_both_pname()

