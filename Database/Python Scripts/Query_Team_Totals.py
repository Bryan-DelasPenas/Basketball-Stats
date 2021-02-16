import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_procedure

'''
Create Procedures
'''
'''
Function that creates procedure that queries all team_totals based on Season_ID
'''
def create_query_all_team_totals_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_totals_sid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_totals_sid(s_id int)
            BEGIN
               SELECT *
               FROM Team_Totals
               Where Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Totals_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Totals_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Totals_Sid does exists")

'''
Function that creates procedure that queries all team_advanced based on Team_ID
'''
def create_query_all_team_totals_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_totals_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_totals_tid(t_id int)
            BEGIN
               SELECT *
               FROM Team_Totals
               Where Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Totals_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Totals_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Totals_Tid does exists")

'''
Function that creates procedure that queries all team_advanced based on Team_ID and Season_ID
'''
def create_query_all_team_totals_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_totals_sid_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_totals_sid_tid(s_id int, t_id int)
            BEGIN
               SELECT *
               FROM Team_Totals
               Where Season_ID = s_id 
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Totals_Sid_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Totals_Sid_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Totals_Sid_Tid does  exists")

'''
Function that creates procedure that queries all team_advanced based on Team Name
'''
def create_query_all_team_totals_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_totals_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_totals_name(name VARCHAR(45))
            BEGIN
               SELECT *
               FROM Team_Totals
               Where Team_Name = name;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Totals_Name was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Totals_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Totals_Name does exists")

'''
Function that creates procedure that queries all team_advanced based Team ABV
'''
def create_query_all_team_totals_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_totals_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_totals_ABV(abv VARCHAR(3))
            BEGIN
               SELECT *
               FROM Team_Totals
               Where Team_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Totals_ABV was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Totals_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Totals_ABV does exists")

'''
Function that creates all procedures for Team_Totals
'''
def create_team_totals_query():
    create_query_all_team_totals_sid()
    create_query_all_team_totals_tid()
    create_query_all_team_totals_sid_tid()
    create_query_all_team_totals_name()
    create_query_all_team_totals_ABV()

'''
Drop Procedures
'''
'''
Function that drops query_all_team_totals_sid
'''
def drop_query_all_team_totals_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_totals_sid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_totals_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Totals_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Totals_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Totals_Sid does not Exists")

'''
Function that drops query_all_team_totals_Tid
'''
def drop_query_all_team_totals_tid():

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_totals_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_totals_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Totals_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Totals_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Totals_Tid does not Exists")

'''
Function that drop query_all_team_totals_Sid_Tid
'''
def drop_query_all_team_totals_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_totals_sid_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_totals_sid_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Totals_Sid_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Totals_Sid_Tid  Failed")
    else:
        raise Exception("Procedure Query_All_Team_Totals_Sid_Tid does not Exists")

'''
Function that drops query_all_team_Name
'''
def drop_query_all_team_totals_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_totals_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_totals_name
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Totals_Name was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Totals_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Totals_Name does not Exists")

'''
Function that drops query_all_team_totals_ABV
'''
def drop_query_all_team_totals_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_totals_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_totals_abv
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Totals_ABV was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Totals_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Totals_ABV does not Exists")

'''
Function that drops  all procedure team_advanced stored procedures 
'''
def drop_team_totals_query():
    drop_query_all_team_totals_sid()
    drop_query_all_team_totals_tid()
    drop_query_all_team_totals_sid_tid()
    drop_query_all_team_totals_name()
    drop_query_all_team_totals_ABV()

'''
Main Function, for testing
'''
def main():
    create_team_totals_query()
    drop_team_totals_query()
main()