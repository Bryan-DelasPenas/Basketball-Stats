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
Function that creates procedure that queries all team_misc based on Season_ID
'''
def create_query_all_team_misc_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_misc_sid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_misc_sid(s_id int)
            BEGIN
               SELECT *
               FROM Team_Misc
               Where Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Misc_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Misc_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Misc_Sid does exists")

'''
Function that creates procedure that queries all team_misc based on Team_ID
'''
def create_query_all_team_misc_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_misc_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_misc_tid(t_id int)
            BEGIN
               SELECT *
               FROM Team_Misc
               Where Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Misc_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Misc_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Misc_Tid does exists")

'''
Function that creates procedure that queries all team_misc based on Team_ID and Season_ID
'''
def create_query_all_team_misc_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_misc_sid_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_misc_sid_tid(s_id int, t_id int)
            BEGIN
               SELECT *
               FROM Team_Misc
               Where Season_ID = s_id 
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Misc_Sid_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Misc_Sid_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Misc_Sid_Tid does  exists")

'''
Function that creates procedure that queries all team_misc based on Team Name
'''
def create_query_all_team_misc_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_misc_name'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_misc_name(name VARCHAR(45))
            BEGIN
               SELECT *
               FROM Team_Misc
               Where Team_Name = name;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Misc_Name was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Misc_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Misc_Name does exists")

'''
Function that creates procedure that queries all team_misc based Team ABV
'''
def create_query_all_team_misc_abv():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_misc_abv'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_misc_ABV(abv VARCHAR(3))
            BEGIN
               SELECT *
               FROM Team_Misc
               Where Team_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Misc_ABV was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Misc_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Misc_ABV does exists")

'''
Function that creates all procedures for Team_Misc
'''
def create_team_misc_query():
    create_query_all_team_misc_sid()
    create_query_all_team_misc_tid()
    create_query_all_team_misc_sid_tid()
    create_query_all_team_misc_name()
    create_query_all_team_misc_abv()

'''
Drop Procedures
'''
'''
Function that drops query_all_team_misc_sid
'''
def drop_query_all_team_misc_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_misc_sid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_misc_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Misc_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Misc_Sid Failed")
    else:
        print("Procedure Query_All_Team_Misc_Sid does not Exists")

'''
Function that drops query_all_team_misc_Tid
'''
def drop_query_all_team_misc_tid():

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_misc_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_misc_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Misc_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Misc_Tid Failed")
    else:
        print("Procedure Query_All_Team_Misc_Tid does not Exists")

'''
Function that drop query_all_team_misc_Sid_Tid
'''
def drop_query_all_team_misc_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_misc_sid_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_misc_sid_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Misc_Sid_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Misc_Sid_Tid  Failed")
    else:
        print("Procedure Query_All_Team_Misc_Sid_Tid does not Exists")

'''
Function that drops query_all_team_Name
'''
def drop_query_all_team_misc_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_misc_name'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_misc_name
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Misc_Name was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Misc_Name Failed")
    else:
        print("Procedure Query_All_Team_Misc_Name does not Exists")

'''
Function that drops query_all_team_misc_ABV
'''
def drop_query_all_team_misc_abv():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_misc_abv'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_misc_abv
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Misc_ABV was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Misc_ABV Failed")
    else:
        print("Procedure Query_All_Team_Misc_ABV does not Exists")

'''
Function that drops  all procedure team_misc stored procedures 
'''
def drop_team_misc_query():
    drop_query_all_team_misc_sid()
    drop_query_all_team_misc_tid()
    drop_query_all_team_misc_sid_tid()
    drop_query_all_team_misc_name()
    drop_query_all_team_misc_abv()
