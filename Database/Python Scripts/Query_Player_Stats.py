import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_procedure


'''
Create Procedures 
'''
'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID
'''
def create_query_player_stats_one_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_one_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_one_pid(IN select_one LONGTEXT, IN tbl_name longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, ',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_One_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_One_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and two addtional input, from a inputed table, based on player_ID
'''
def create_query_player_stats_two_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_two_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_two_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN tbl_name longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, ',select_one, ',', select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Two_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Two_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and three addtional input, from a inputed table, based on player_ID
'''
def create_query_player_stats_three_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_three_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_three_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN select_three, IN tbl_name longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, ',select_one, ',', select_two, ',' ,select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Three_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Three_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Pid does exists") 

'''

'''