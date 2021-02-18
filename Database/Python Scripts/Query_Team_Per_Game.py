import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_procedure

'''
Create Procedures
'''

'''
Create Procedure for Team's or Opponent's Per Game 
'''
'''
Function that creates procedure that queries all team_per_game based on Season_ID
'''
def create_query_all_team_per_game_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_game_sid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_game_sid(opp int, s_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Game
               Where Opponent = opp 
               AND Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Game_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Game_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Sid does exists")

'''
Function that creates procedure that queries all team_advanced based on Team_ID
'''
def create_query_all_team_per_game_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_game_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_game_tid(opp int, t_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Game
               WHERE Opponent = opp  
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Game_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Game_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Tid does exists")

'''
Function that creates procedure that queries all team_advanced based on Team_ID and Season_ID
'''
def create_query_all_team_per_game_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_game_sid_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_game_sid_tid(opp int, s_id int, t_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Game
               WHERE Opponent = opp 
               AND Season_ID = s_id 
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Game_Sid_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Game_Sid_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Sid_Tid does  exists")

'''
Function that creates procedure that queries all team_advanced based on Team Name
'''
def create_query_all_team_per_game_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_game_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_game_name(opp int, name VARCHAR(45))
            BEGIN
               SELECT *
               FROM Team_Per_Game
               WHERE Opponent = opp 
               AND Team_Name = name;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Game_Name was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Game_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Name does exists")

'''
Function that creates procedure that queries all team_advanced based Team ABV
'''
def create_query_all_team_per_game_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_game_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_game_ABV(opp int, abv VARCHAR(3))
            BEGIN
               SELECT *
               FROM Team_Per_Game
               WHERE Opponent = opp 
               AND Team_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Game_ABV was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Game_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_ABV does exists")


'''
Create Procedure for both
'''
'''
Function that creates procedure that queries all team_per_game based on Season_ID
'''
def create_query_all_team_per_game_both_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_game_both_sid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_game_both_sid(s_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Game
               Where Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Game_Both_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Game_Both_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Both_Sid does exists")

'''
Function that creates procedure that queries all team_advanced based on Team_ID
'''
def create_query_all_team_per_game_both_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_game_both_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_game_both_tid(t_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Game
               Where Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Game_Both_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Game_Both_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Both_Tid does exists")

'''
Function that creates procedure that queries all team_advanced based on Team_ID and Season_ID
'''
def create_query_all_team_per_game_both_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_game_both_sid_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_game_both_sid_tid(s_id int, t_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Game
               Where Season_ID = s_id 
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Game_Both_Sid_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Game_Both_Sid_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Both_Sid_Tid does exists")

'''
Function that creates procedure that queries all team_advanced based on Team Name
'''
def create_query_all_team_per_game_both_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_game_both_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_game_both_name(name VARCHAR(45))
            BEGIN
               SELECT *
               FROM Team_Per_Game
               Where Team_Name = name;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Game_Both_Name was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Game_Both_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Both_Name does exists")

'''
Function that creates procedure that queries all team_advanced based Team ABV
'''
def create_query_all_team_per_game_both_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_game_both_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_game_both_ABV(abv VARCHAR(3))
            BEGIN
               SELECT *
               FROM Team_Per_Game
               Where Team_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Game_Both_ABV was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Game_Both_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Both_ABV does exists")

'''
Function that creates all procedures for Team_Per_Game
'''
def create_team_per_game_query():
    create_query_all_team_per_game_sid()
    create_query_all_team_per_game_tid()
    create_query_all_team_per_game_sid_tid()
    create_query_all_team_per_game_name()
    create_query_all_team_per_game_ABV()

    create_query_all_team_per_game_both_sid()
    create_query_all_team_per_game_both_tid()
    create_query_all_team_per_game_both_sid_tid()
    create_query_all_team_per_game_both_name()
    create_query_all_team_per_game_both_ABV()

'''
Drop Procedures
'''

'''
Drop Procedures based on Team
'''
'''
Function that drops query_all_team_per_game_sid
'''
def drop_query_all_team_per_game_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_game_sid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_game_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Game_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Game_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Sid does not Exists")

'''
Function that drops query_all_team_per_game_Tid
'''
def drop_query_all_team_per_game_tid():

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_game_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_game_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Game_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Game_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Tid does not Exists")

'''
Function that drop query_all_team_per_game_Sid_Tid
'''
def drop_query_all_team_per_game_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_game_sid_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_game_sid_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Game_Sid_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Game_Sid_Tid  Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Sid_Tid does not Exists")

'''
Function that drops query_all_team_Name
'''
def drop_query_all_team_per_game_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_game_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_game_name
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Game_Name was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Game_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Name does not Exists")

'''
Function that drops query_all_team_per_game_ABV
'''
def drop_query_all_team_per_game_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_game_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_game_abv
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Game_ABV was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Game_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_ABV does not Exists")


'''
Drop Procedure based on Both
'''
'''
Function that drops query_all_team_per_game_sid
'''
def drop_query_all_team_per_game_both_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_game_both_sid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_game_both_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Game_Both_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Game_Both_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Both_Sid does not Exists")

'''
Function that drops query_all_team_per_game_Tid
'''
def drop_query_all_team_per_game_both_tid():

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_game_both_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_game_both_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Game_Both_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Game_Both_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Both_Tid does not Exists")

'''
Function that drop query_all_team_per_game_Sid_Tid
'''
def drop_query_all_team_per_game_both_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_game_both_sid_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_game_both_sid_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Game_Both_Sid_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Game_Both_Sid_Tid  Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Both_Sid_Tid does not Exists")

'''
Function that drops query_all_team_Name
'''
def drop_query_all_team_per_game_both_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_game_both_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_game_both_name
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Game_Both_Name was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Game_Both_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Both_Name does not Exists")

'''
Function that drops query_all_team_per_game_ABV
'''
def drop_query_all_team_per_game_both_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_game_both_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_game_both_abv
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Game_Both_ABV was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Game_Both_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Game_Both_ABV does not Exists")

'''
Function that drops  all procedure team_advanced stored procedures 
'''
def drop_team_per_game_query():
    drop_query_all_team_per_game_sid()
    drop_query_all_team_per_game_tid()
    drop_query_all_team_per_game_sid_tid()
    drop_query_all_team_per_game_name()
    drop_query_all_team_per_game_ABV()

    drop_query_all_team_per_game_both_sid()
    drop_query_all_team_per_game_both_tid()
    drop_query_all_team_per_game_both_sid_tid()
    drop_query_all_team_per_game_both_name()
    drop_query_all_team_per_game_both_ABV()

'''
Main Function, for testing
'''
def main():
    create_team_per_game_query()
    drop_team_per_game_query()
main()