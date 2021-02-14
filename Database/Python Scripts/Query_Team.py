import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_procedure

'''
Create Procedures
'''
'''
Function that creates procedure that queries all teams based on Season_ID
'''
def create_query_all_team_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_sid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_sid(s_id int)
            BEGIN
               SELECT *
               FROM Team
               Where Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Sid does  exists")

'''
Function that creates procedure that queries all teams based on Team_ID
'''
def create_query_all_team_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_tid(t_id int)
            BEGIN
               SELECT *
               FROM Team
               Where Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Tid does  exists")

'''
Function that creates procedure that queries all teams based on Team_ID and Season_ID
'''
def create_query_all_team_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_sid_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_sid_tid(s_id int, t_id int)
            BEGIN
               SELECT *
               FROM Team
               Where Season_ID = s_id 
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Sid_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Sid_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Sid_Tid does  exists")

'''
Function that creates procedure that queries all teams based on Team Name
'''
def create_query_all_teams_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_name(name VARCHAR(45))
            BEGIN
               SELECT *
               FROM Team
               Where Team_Name = name;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Name was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Name does exists")

'''
Function that creates procedure that queries all teams based Team ABV
'''
def create_query_all_teams_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_ABV(abv VARCHAR(3))
            BEGIN
               SELECT *
               FROM Team
               Where Team_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_ABV was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_ABV does exists")

'''
Function that creates all procedures
'''
def create_team_query():
    create_query_all_team_sid()
    create_query_all_team_tid()
    create_query_all_team_sid_tid()
    create_query_all_teams_name()
    create_query_all_teams_ABV()

'''
Drop Procedures
'''
'''
Function that drops query_all_team_sid
'''
def drop_query_all_team_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_sid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Sid does not Exists")

'''
Function that drops query_all_team_Tid
'''
def drop_query_all_team_tid():

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Tid does not Exists")

'''
Function that drop query_all_team_Sid_Tid
'''
def drop_query_all_team_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_sid_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_sid_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Sid_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Sid_Tid  Failed")
    else:
        raise Exception("Procedure Query_All_Team_Sid_Tid does not Exists")

'''
Function that drops query_all_team_Name
'''
def drop_query_all_team_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_name
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Name was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Name does not Exists")

'''
Function that drops query_all_team_ABV
'''
def drop_query_all_team_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_abv
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_ABV was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_ABV does not Exists")

'''
Function that drops all procedures
'''
def drop_team_query():
    drop_query_all_team_sid()
    drop_query_all_team_tid()
    drop_query_all_team_sid_tid()
    drop_query_all_team_name()
    drop_query_all_team_ABV()

'''
Main function for testing
'''
def main():
    create_team_query()
    drop_team_query()
main()