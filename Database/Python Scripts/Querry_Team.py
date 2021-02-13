import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_procedure


'''
Create Procedures
'''
'''
Function that creates procedure that queries teams based on Season_ID
'''
def create_querry_all_team_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('querry_all_team_sid'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE querry_all_team_sid(s_id int)
            BEGIN
               SELECT Season_ID
               FROM Season
               Where Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Querry_All_Team_Sid was Successful")
        except:
            raise Exception("Create Procedure Querry_All_Team_Sid Failed")
    else:
        raise Exception("Procedure Querry_All_Team_Sid does  exists")

'''
Function that creates procedure that queries teams based on Team_ID
'''
def create_querry_all_team_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('querry_all_team_tid'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE querry_all_team_tid(t_id int)
            BEGIN
               SELECT Team_ID
               FROM Season
               Where Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Querry_All_Team_Sid was Successful")
        except:
            raise Exception("Create Procedure Querry_All_Team_Tid Failed")
    else:
        raise Exception("Procedure Querry_All_Team_Tid does  exists")

'''
Function that creates procedure that queries teams based on Name
'''
def create_querry_all_teams_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('querry_all_team_name'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE querry_all_team_name(name VARCHAR(45))
            BEGIN
               SELECT Team_Name
               FROM Season
               Where Team_Name = name;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Querry_All_Team_Name was Successful")
        except:
            raise Exception("Create Procedure Querry_All_Team_Name Failed")
    else:
        raise Exception("Procedure Querry_All_Team_Name does exists")

'''
Function that creates procedure that queries teams based ABV
'''
def create_querry_all_teams_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('querry_all_team_abv'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE querry_all_team_ABV(abv VARCHAR(3))
            BEGIN
               SELECT Team_ABV
               FROM Season
               Where Team_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Querry_All_Team_ABV was Successful")
        except:
            raise Exception("Create Procedure Querry_All_Team_ABV Failed")
    else:
        raise Exception("Procedure Querry_All_Team_ABV does exists")

'''
Function that creates all procedures
'''
def create_team_query():
    create_querry_all_team_sid()
    create_querry_all_team_tid()
    create_querry_all_teams_name()
    create_querry_all_teams_ABV()

'''
Drop Procedures
'''
'''

'''
def drop_querry_all_team_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('querry_all_team_sid'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS querry_all_team_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Querry_All_Team_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Querry_All_Team_Sid Failed")
    else:
        raise Exception("Procedure Querry_All_Team_Sid does not Exists")

'''

'''
def drop_querry_all_team_tid():

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('querry_all_team_tid'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS querry_all_team_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Querry_All_Team_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Querry_All_Team_Tid Failed")
    else:
        raise Exception("Procedure Querry_All_Team_Tid does not Exists")

'''

'''
def drop_querry_all_team_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('querry_all_team_name'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS querry_all_team_name
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Querry_All_Team_Name was Successful")
        except:
            raise Exception("Deletion of Procedure Querry_All_Team_Name Failed")
    else:
        raise Exception("Procedure Querry_All_Team_Name does not Exists")

'''

'''
def drop_querry_all_team_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('querry_all_team_abv'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS querry_all_team_abv
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Querry_All_Team_ABV was Successful")
        except:
            raise Exception("Deletion of Procedure Querry_All_Team_ABV Failed")
    else:
        raise Exception("Procedure Querry_All_Team_ABV does not Exists")

'''

'''
def drop_team_query():
    drop_querry_all_team_sid()
    drop_querry_all_team_tid()
    drop_querry_all_team_name()
    drop_querry_all_team_ABV()

def main():
    create_team_query()
    drop_team_query()
main()