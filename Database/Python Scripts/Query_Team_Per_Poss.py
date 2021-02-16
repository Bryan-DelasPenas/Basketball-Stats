import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_procedure

'''
Create Procedures
'''
'''
Function that creates procedure that queries all team_per_poss based on Season_ID
'''
def create_query_all_team_per_poss_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_poss_sid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_poss_sid(s_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               Where Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Poss_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Poss_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Sid does exists")

'''
Function that creates procedure that queries all team_per_poss based on Team_ID
'''
def create_query_all_team_per_poss_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_poss_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_poss_tid(t_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               Where Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Poss_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Poss_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Tid does exists")

'''
Function that creates procedure that queries all team_per_poss based on Team_ID and Season_ID
'''
def create_query_all_team_per_poss_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_poss_sid_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_poss_sid_tid(s_id int, t_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               Where Season_ID = s_id 
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Poss_Sid_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Poss_Sid_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Sid_Tid does  exists")

'''
Function that creates procedure that queries all team_per_poss based on Team Name
'''
def create_query_all_team_per_poss_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_poss_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_poss_name(name VARCHAR(45))
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               Where Team_Name = name;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Poss_Name was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Poss_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Name does exists")

'''
Function that creates procedure that queries all team_per_poss based Team ABV
'''
def create_query_all_team_per_poss_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_poss_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_poss_ABV(abv VARCHAR(3))
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               Where Team_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Poss_ABV was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Poss_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_ABV does exists")

'''
Function that creates all procedures for Team_Per_Poss
'''
def create_team_per_poss_query():
    create_query_all_team_per_poss_sid()
    create_query_all_team_per_poss_tid()
    create_query_all_team_per_poss_sid_tid()
    create_query_all_team_per_poss_name()
    create_query_all_team_per_poss_ABV()

'''
Drop Procedures
'''
'''
Function that drops query_all_team_per_poss_sid
'''
def drop_query_all_team_per_poss_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_poss_sid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_poss_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Poss_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Poss_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Sid does not Exists")

'''
Function that drops query_all_team_per_poss_Tid
'''
def drop_query_all_team_per_poss_tid():

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_poss_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_poss_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Poss_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Poss_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Tid does not Exists")

'''
Function that drop query_all_team_per_poss_Sid_Tid
'''
def drop_query_all_team_per_poss_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_poss_sid_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_poss_sid_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Poss_Sid_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Poss_Sid_Tid  Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Sid_Tid does not Exists")

'''
Function that drops query_all_team_Name
'''
def drop_query_all_team_per_poss_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_poss_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_poss_name
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Poss_Name was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Poss_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Name does not Exists")

'''
Function that drops query_all_team_per_poss_ABV
'''
def drop_query_all_team_per_poss_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_poss_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_poss_abv
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Poss_ABV was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Poss_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_ABV does not Exists")

'''
Function that drops all procedure team_per_poss stored procedures 
'''
def drop_team_per_poss_query():
    drop_query_all_team_per_poss_sid()
    drop_query_all_team_per_poss_tid()
    drop_query_all_team_per_poss_sid_tid()
    drop_query_all_team_per_poss_name()
    drop_query_all_team_per_poss_ABV()

'''
Main Function, for testing
'''
def main():
    create_team_per_poss_query()
    drop_team_per_poss_query()
main()