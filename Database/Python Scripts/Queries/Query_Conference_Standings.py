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
Function that creates procedure to query all conference standings for a given year
'''
def create_query_all_cs_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_cs_sid'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_cs_sid(s_id int)
            BEGIN
               SELECT *
               FROM Conference_Standings
               Where Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_CS_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_All_CS_Sid Failed")
    else:
        raise Exception("Procedure Query_All_CS_Sid does exists")

'''
Function that creates procedure to query all conference standings for a given team
'''
def create_query_all_cs_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_cs_tid'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_cs_tid(t_id int)
            BEGIN
               SELECT *
               FROM Conference_Standings
               Where Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_CS_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_CS_Tid Failed")
    else:
        raise Exception("Procedure Query_All_CS_Tid does exists")

'''
Function that creates procedure to query all conference standings based on team Name
'''
def create_query_all_cs_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_cs_name'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_cs_name(name varchar(45))
            BEGIN
               SELECT *
               FROM Conference_Standings
               Where Team_Name = name;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_CS_Name was Successful")
        except:
            raise Exception("Create Procedure Query_All_CS_Name Failed")
    else:
        raise Exception("Procedure Query_All_CS_Name does exists")

'''
Function that creates procedure to query all conference standings based on team ABV
'''
def create_query_all_cs_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_cs_abv'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_cs_abv(abv varchar(3))
            BEGIN
               SELECT *
               FROM Conference_Standings
               Where Team_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_CS_ABV was Successful")
        except:
            raise Exception("Create Procedure Query_All_CS_ABV Failed")
    else:
        raise Exception("Procedure Query_All_CS_ABV does exists")

'''
Function that creates procedure to query all conference standings based on a wins less than the parameter
'''
def create_query_all_cs_win():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_cs_win'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_cs_win(wins_amount int)
            BEGIN
               SELECT *
               FROM Conference_Standings
               Where Wins >= wins_amount;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_CS_Win was Successful")
        except:
            raise Exception("Create Procedure Query_All_CS_Win Failed")
    else:
        raise Exception("Procedure Query_All_CS_Win does exists")

'''
Function that create procedure to query all conference standings based on win-lost percentage
'''
def create_query_all_cs_wl():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_cs_wl'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_cs_wl(wl FLOAT)
            BEGIN
               SELECT *
               FROM Conference_Standings
               Where Win_Lose_Percentage >= wl;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_CS_WL was Successful")
        except:
            raise Exception("Create Procedure Query_All_CS_WL Failed")
    else:
        raise Exception("Procedure Query_All_CS_WL does exists")

'''
Function that creates procedure to query all conference standings based on a season_id and east or west
'''
def create_query_all_cs_sid_ew():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_cs_sid_ew'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_cs_sid_ew(s_id int, e_w bit)
            BEGIN
               SELECT *
               FROM Conference_Standings
               Where Season_ID = s_id
               AND East_Or_West = e_w;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_CS_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_All_CS_Sid Failed")
    else:
        raise Exception("Procedure Query_All_CS_Sid does exists")

'''
Function that creates procedure to query Season_ID, Team_ID, Team_Name, Wins based on Season_ID, Team_ID, Team_Name, Wins
'''
def create_query_cs_win():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_cs_win'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_cs_win(s_id int, t_id int)
            BEGIN
               SELECT Season_ID, Team_ID, Team_ABV, Team_Name, Wins
               FROM Conference_Standings
               Where Season_ID = s_id
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_CS_Win was Successful")
        except:
            raise Exception("Create Procedure Query_CS_Win Failed")
    else:
        raise Exception("Procedure Query_CS_Win does exists")


'''
Function that creates all procedure query for Conference_Standings
'''
def create_cs_query():
    create_query_all_cs_sid()
    create_query_all_cs_tid()
    create_query_all_cs_name()
    create_query_all_cs_ABV()
    create_query_all_cs_win()
    create_query_all_cs_wl()
    create_query_all_cs_sid_ew()
    create_query_cs_win()

'''
Drop Procedures
'''
'''
Function that drops query_all_cs_sid
'''
def drop_query_all_cs_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_cs_sid'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_cs_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_CS_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_CS_Sid Failed")
    else:
        raise Exception("Procedure Query_All_CS_Sid does not Exists")

'''
Function that drops query_all_cs_tid
'''
def drop_query_all_cs_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_cs_tid'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_cs_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_CS_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_CS_Tid Failed")
    else:
        raise Exception("Procedure Query_All_CS_Tid does not Exists")

'''
Function that drops query_all_cs_name
'''
def drop_query_all_cs_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_cs_name'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_cs_name
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_CS_Name was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_CS_Name Failed")
    else:
        raise Exception("Procedure Query_All_CS_Name does not Exists")

'''
Function that drops query_all_cs_ABV
'''
def drop_query_all_cs_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_cs_abv'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_cs_abv
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_CS_ABV was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_CS_ABV Failed")
    else:
        raise Exception("Procedure Query_All_CS_ABV does not Exists")

'''
Function that drops query_all_cs_win
'''
def drop_query_all_cs_win():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_cs_win'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_cs_win
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_CS_Win was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_CS_Win Failed")
    else:
        raise Exception("Procedure Query_All_CS_Win does not Exists")

'''
Function that drops query_all_cs_wl()
'''
def drop_query_all_cs_wl():
     # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_cs_wl'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_cs_wl
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_CS_WL was Successful")
        except:
            raise Exception("Deletion of Procedure Query_CS_WL Failed")
    else:
        raise Exception("Procedure Query_CS_WL does not Exists") 

'''
Function that drops query_all_cs_sid_ew
'''
def drop_query_all_cs_sid_ew():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_cs_sid_ew'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_cs_sid_ew
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_CS_Sid_EW was Successful")
        except:
            raise Exception("Deletion of ProcedureQuery_All_CS_Sid_EW Failed")
    else:
        raise Exception("Procedure Query_All_CS_Sid_EW does not Exists")

'''
Function that drops query_cs_win
'''
def drop_query_cs_win():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_cs_win'):
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_cs_win
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_CS_Win was Successful")
        except:
            raise Exception("Deletion of Procedure Query_CS_Win Failed")
    else:
        raise Exception("Procedure Query_CS_Win does not Exists")


'''
Function that drops all procedures for Conference_Standings
'''
def drop_cs_query():
    drop_query_all_cs_sid()
    drop_query_all_cs_tid()
    drop_query_all_cs_name()
    drop_query_all_cs_ABV()
    drop_query_all_cs_win()
    drop_query_all_cs_wl()
    drop_query_all_cs_sid_ew()
    drop_query_cs_win()
   

'''
Main Function for Testing
'''
def main():
   
    create_cs_query()
    drop_cs_query()

main()