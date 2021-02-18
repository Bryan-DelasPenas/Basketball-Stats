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
            CREATE PROCEDURE query_all_team_per_poss_sid(opp int, s_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               Where Opponent = opp 
               AND Season_ID = s_id;
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
Function that creates procedure that queries all team_advanced based on Team_ID
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
            CREATE PROCEDURE query_all_team_per_poss_tid(opp int, t_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               WHERE Opponent = opp  
               AND Team_ID = t_id;
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
Function that creates procedure that queries all team_advanced based on Team_ID and Season_ID
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
            CREATE PROCEDURE query_all_team_per_poss_sid_tid(opp int, s_id int, t_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               WHERE Opponent = opp 
               AND Season_ID = s_id 
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
Function that creates procedure that queries all team_advanced based on Team Name
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
            CREATE PROCEDURE query_all_team_per_poss_name(opp int, name VARCHAR(45))
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               WHERE Opponent = opp 
               AND Team_Name = name;
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
Function that creates procedure that queries all team_advanced based Team ABV
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
            CREATE PROCEDURE query_all_team_per_poss_ABV(opp int, abv VARCHAR(3))
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               WHERE Opponent = opp 
               AND Team_ABV = abv;
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
Create Procedure for both
'''
'''
Function that creates procedure that queries all team_per_poss based on Season_ID
'''
def create_query_all_team_per_poss_both_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_poss_both_sid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_poss_both_sid(s_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               Where Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Poss_Both_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Poss_Both_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Both_Sid does exists")

'''
Function that creates procedure that queries all team_advanced based on Team_ID
'''
def create_query_all_team_per_poss_both_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_poss_both_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_poss_both_tid(t_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               Where Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Poss_Both_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Poss_Both_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Both_Tid does exists")

'''
Function that creates procedure that queries all team_advanced based on Team_ID and Season_ID
'''
def create_query_all_team_per_poss_both_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_poss_both_sid_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_poss_both_sid_tid(s_id int, t_id int)
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               Where Season_ID = s_id 
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Poss_Both_Sid_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Poss_Both_Sid_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Both_Sid_Tid does exists")

'''
Function that creates procedure that queries all team_advanced based on Team Name
'''
def create_query_all_team_per_poss_both_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_poss_both_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_poss_both_name(name VARCHAR(45))
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               Where Team_Name = name;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Poss_Both_Name was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Poss_Both_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Both_Name does exists")

'''
Function that creates procedure that queries all team_advanced based Team ABV
'''
def create_query_all_team_per_poss_both_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_team_per_poss_both_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_all_team_per_poss_both_ABV(abv VARCHAR(3))
            BEGIN
               SELECT *
               FROM Team_Per_Poss
               Where Team_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Team_Per_Poss_Both_ABV was Successful")
        except:
            raise Exception("Create Procedure Query_All_Team_Per_Poss_Both_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Both_ABV does exists")

'''
Function that creates all procedures for Team_Per_Poss
'''
def create_team_per_poss_query():
    create_query_all_team_per_poss_sid()
    create_query_all_team_per_poss_tid()
    create_query_all_team_per_poss_sid_tid()
    create_query_all_team_per_poss_name()
    create_query_all_team_per_poss_ABV()

    create_query_all_team_per_poss_both_sid()
    create_query_all_team_per_poss_both_tid()
    create_query_all_team_per_poss_both_sid_tid()
    create_query_all_team_per_poss_both_name()
    create_query_all_team_per_poss_both_ABV()

'''
Drop Procedures
'''

'''
Drop Procedures based on Team
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
Drop Procedure based on Both
'''
'''
Function that drops query_all_team_per_poss_sid
'''
def drop_query_all_team_per_poss_both_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_poss_both_sid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_poss_both_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Poss_Both_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Poss_Both_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Both_Sid does not Exists")

'''
Function that drops query_all_team_per_poss_Tid
'''
def drop_query_all_team_per_poss_both_tid():

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_poss_both_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_poss_both_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Poss_Both_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Poss_Both_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Both_Tid does not Exists")

'''
Function that drop query_all_team_per_poss_Sid_Tid
'''
def drop_query_all_team_per_poss_both_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_poss_both_sid_tid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_poss_both_sid_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Poss_Both_Sid_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Poss_Both_Sid_Tid  Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Both_Sid_Tid does not Exists")

'''
Function that drops query_all_team_Name
'''
def drop_query_all_team_per_poss_both_name():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_poss_both_name'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_poss_both_name
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Poss_Both_Name was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Poss_Both_Name Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Both_Name does not Exists")

'''
Function that drops query_all_team_per_poss_ABV
'''
def drop_query_all_team_per_poss_both_ABV():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_team_per_poss_both_abv'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_team_per_poss_both_abv
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Team_Per_Poss_Both_ABV was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Team_Per_Poss_Both_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Team_Per_Poss_Both_ABV does not Exists")

'''
Function that drops  all procedure team_advanced stored procedures 
'''
def drop_team_per_poss_query():
    drop_query_all_team_per_poss_sid()
    drop_query_all_team_per_poss_tid()
    drop_query_all_team_per_poss_sid_tid()
    drop_query_all_team_per_poss_name()
    drop_query_all_team_per_poss_ABV()

    drop_query_all_team_per_poss_both_sid()
    drop_query_all_team_per_poss_both_tid()
    drop_query_all_team_per_poss_both_sid_tid()
    drop_query_all_team_per_poss_both_name()
    drop_query_all_team_per_poss_both_ABV()

'''
Main Function, for testing
'''
def main():
    create_team_per_poss_query()
    drop_team_per_poss_query()
main()