import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_procedure

'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on Season_ID or Team_ID
'''
def create_query_team_stat_one():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stat_one'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_team_stat_one(IN select_one LONGTEXT, IN tbl_name longtext, IN col_one longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID,Team_Name, ',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE ', col_one,' = '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_One was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_One Failed")
    else:
        raise Exception("ProcedureQuery_Team_Stat_One does exists")

'''
Function that creates procedure for team that queries Season_ID, Team_Name, and two addtional inputs, from a inputed table, based on Season_ID or Team_ID 
'''
def create_query_team_stat_two():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stat_two'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_team_stat_two(IN select_one LONGTEXT, IN select_two longtext, 
            IN tbl_name longtext, IN col_one longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID,Team_Name, ',select_one, ',' ,select_two, 
                    ' FROM ', tbl_name, 
                    ' WHERE ', col_one,' = '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Two was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Two Failed")
    else:
        raise Exception("ProcedureQuery_Team_Stat_Two does exists")

'''
Function that creates procedure for team that queries Season_ID, Team_Name, and three addtional inputs, from a input table, based on Season_ID or Team_ID
'''
def create_query_team_stat_three():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stat_three'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_team_stat_three(IN select_one LONGTEXT, IN select_two longtext, IN select_three longtext, 
            IN tbl_name longtext, IN col_one longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID,Team_Name, ',select_one, ',' ,select_two, ',', select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE ', col_one,' = '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Three was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Three Failed")
    else:
        raise Exception("ProcedureQuery_Team_Stat_Three does exists")

'''
Function that creates procedure for team that queries Season_ID, Team_Name and four addtional inputs, from a input table, based on Season_ID or Team_ID
'''
def create_query_team_stat_four():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stat_four'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_team_stat_three(IN select_one LONGTEXT, IN select_two longtext, IN select_three longtext, 
            IN select_four longtext, IN tbl_name longtext, IN col_one longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID,Team_Name, ',select_one, ',' ,select_two, ',', select_three, ',', select_four,
                    ' FROM ', tbl_name, 
                    ' WHERE ', col_one,' = '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Four was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Four Failed")
    else:
        raise Exception("ProcedureQuery_Team_Stat_Four does exists")

'''
Function that creates procedure for team that queries Season_ID, Team_Name and five addtional inputs, from a input table, based on Season_ID or Team_ID
'''
def create_query_team_stat_five():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stat_five'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_team_stat_three(IN select_one LONGTEXT, IN select_two longtext, IN select_three longtext,
            IN select_four longtext, IN select_five longtext, IN tbl_name longtext, IN col_one longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID,Team_Name, ',select_one, ',' ,select_two, ',', select_three, ',', select_four, ',' , select_five,
                    ' FROM ', tbl_name, 
                    ' WHERE ', col_one,' = '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Five was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Five Failed")
    else:
        raise Exception("ProcedureQuery_Team_Stat_Five does exists")

'''
Function that creates procedure for team that queries Season_ID, Team_Name and six addtional inputs, from a input table, based on Season_ID or Team_ID
'''
def create_query_team_stat_six():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stat_six'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_team_stat_three(IN select_one LONGTEXT, IN select_two longtext, IN select_three longtext,
            IN select_four longtext, IN select_five longtext, IN select_six, IN tbl_name longtext, IN col_one longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID,Team_Name, ',select_one, ',' ,select_two, ',', select_three, ',', select_four, ',' , select_five, ',', select_six, 
                    ' FROM ', tbl_name, 
                    ' WHERE ', col_one,' = '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Six was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Six Failed")
    else:
        raise Exception("ProcedureQuery_Team_Stat_Six does exists")