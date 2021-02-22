import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_procedure

'''
Create Procedures
'''
'''
Function that creates procedure that queries all team_advanced based on Season_ID
'''
def create_query_all_team_advanced_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_advanced_sid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_advanced_sid(s_id int)
            BEGIN
               SELECT *
               FROM Team_Advanced
               Where Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Advanced_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Advanced_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Advanced_Sid does exists")

'''
Function that creates procedure that queries all team_advanced based on Team_ID
'''
def create_query_all_team_advanced_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_advanced_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_advanced_tid(t_id int)
            BEGIN
               SELECT *
               FROM Team_Advanced
               Where Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Advanced_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Advanced_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Advanced_Tid doesexists")

'''
Function that creates procedure that queries all team_advanced based on Team_ID and Season_ID
'''
def create_query_all_team_advanced_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_advanced_sid_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_advanced_sid_tid(s_id int, t_id int)
            BEGIN
               SELECT *
               FROM Team_Advanced
               Where Season_ID = s_id 
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Advanced_Sid_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Advanced_Sid_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Advanced_Sid_Tid does  exists")

'''
Function that creates procedure that queries all team_advanced based on Team Name
'''
def create_query_all_team_advanced_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_advanced_name'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_advanced_name(name VARCHAR(45))
            BEGIN
               SELECT *
               FROM Team_Advanced
               Where Team_Name = name;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Advanced_Name was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Advanced_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Advanced_Name does exists")

'''
Function that creates procedure that queries all team_advanced based Team ABV
'''
def create_query_all_team_advanced_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_advanced_abv'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_advanced_ABV(abv VARCHAR(3))
            BEGIN
               SELECT *
               FROM Team_Advanced
               Where Team_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Advanced_ABV was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Advanced_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Advanced_ABV does exists")

'''
Function that creates all procedures for Team_Advanced
'''
def create_team_advanced_query():
    create_query_all_team_advanced_sid()
    create_query_all_team_advanced_tid()
    create_query_all_team_advanced_sid_tid()
    create_query_all_team_advanced_name()
    create_query_all_team_advanced_ABV()

'''
Drop Procedures
'''
'''
Function that drops query_all_team_advanced_sid
'''
def drop_query_all_team_advanced_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_advanced_sid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_advanced_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Advanced_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Advanced_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Advanced_Sid does not Exists")

'''
Function that drops query_all_team_advanced_Tid
'''
def drop_query_all_team_advanced_tid():

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_advanced_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_advanced_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Advanced_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Advanced_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Advanced_Tid does not Exists")

'''
Function that drop query_all_team_advanced_Sid_Tid
'''
def drop_query_all_team_advanced_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_advanced_sid_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_advanced_sid_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Advanced_Sid_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Advanced_Sid_Tid  Failed")
    else:
        raise Exception("Procedure Query_All_Team_Advanced_Sid_Tid does not Exists")

'''
Function that drops query_all_team_Name
'''
def drop_query_all_team_advanced_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_advanced_name'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_advanced_name
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Advanced_Name was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Advanced_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Advanced_Name does not Exists")

'''
Function that drops query_all_team_advanced_ABV
'''
def drop_query_all_team_advanced_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_advanced_abv'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_advanced_abv
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Advanced_ABV was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Advanced_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Advanced_ABV does not Exists")

'''
Function that drops  all procedure team_advanced stored procedures 
'''
def drop_team_advanced_query():
    drop_query_all_team_advanced_sid()
    drop_query_all_team_advanced_tid()
    drop_query_all_team_advanced_sid_tid()
    drop_query_all_team_advanced_name()
    drop_query_all_team_advanced_ABV()

'''
Main Function, for testing
'''
def main():
    create_team_advanced_query()
    drop_team_advanced_query()
main()