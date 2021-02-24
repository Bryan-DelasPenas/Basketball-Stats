import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd
import pathlib
import sys

sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')
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
Function that creates procedure that queries all teams based on Team Name
'''
def create_query_all_team_name():
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
def create_query_all_team_ABV():
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
Function that creates procedure that queries Team_ID from a given name
'''
def create_query_team_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_team_name(name VARCHAR(100))
            BEGIN
               SELECT DISTINCT Team_ID
               FROM Team
               Where Team_Name = name;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Name was Successful")
        except:
            raise Exception("Create Procedure Query_Team_Name Failed")
    else:
        raise Exception("Procedure Query_Team_Name does exists")

'''
Function that creates procedure that queries Team_ID from a given abv
'''
def create_query_team_abv():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_team_abv(name VARCHAR(100))
            BEGIN
               SELECT DISTINCT Team_ID
               FROM Team
               Where Team_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_ABV was Successful")
        except:
            raise Exception("Create Procedure Query_Team_ABV Failed")
    else:
        raise Exception("Procedure Query_Team_ABV does exists")

'''
Function that creates all procedures
'''
def create_team_query():
    create_query_all_team_sid()
    create_query_all_team_tid()
    create_query_all_team_name()
    create_query_all_team_ABV()
    create_query_team_name()

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
Function that drops query_team_name
'''
def drop_query_team_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_name
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Name was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Name Failed")
    else:
        raise Exception("Procedure Query_Team_Name does not Exists")

'''
Function that drops query_team_abv
'''
def drops_query_team_abv():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_abv
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_ABV was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_ABV Failed")
    else:
        raise Exception("Procedure Query_Team_ABV does not Exists")

'''
Function that drops all procedures
'''
def drop_team_query():
    drop_query_all_team_sid()
    drop_query_all_team_tid()
    
    drop_query_all_team_name()
    drop_query_all_team_ABV()
    drop_query_team_name()

'''
Main function for testing
'''
def main():
    
    create_team_query()
    drop_team_query()
main()