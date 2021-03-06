import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd
import pathlib
import sys

sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')
from Helper_DB import test_connection, create_connection, check_procedure

'''
Create Procedures for reg or playoff
'''
'''
Create Procedure that queries all from Player_Advanced based on Player_ID
'''
def create_query_all_player_advanced_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_advanced_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_advanced_pid(format int, p_id int)
            BEGIN
               SELECT *
               FROM Player_Advanced
               WHERE Stat_Form = format 
               AND Player_ID = p_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_All_Player_Advanced_Pid was Successful")
        except:
            raise Exception("Create Procedure Query_Player_All_Player_Advanced_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_All_Player_Advanced_Pid does exists")

'''
Create Procedure that queries all from Player_Advanced based on Season_ID and Player_ID
'''
def create_query_all_player_advanced_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_advanced_sid_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_advanced_sid_pid(format int, s_id int, p_id int)
            BEGIN
               SELECT *
               FROM Player_Advanced
               WHERE Stat_Form = format 
               AND Season_ID = s_id 
               AND Player_ID = p_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_All_Player_Advanced_Sid_Pid was Successful")
        except:
            raise Exception("Create Procedure Query_Player_All_Player_Advanced_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_All_Player_Advanced_Sid_Pid does exists")

'''
Create Procedure that queries all from Player_Advanced based on Team_ID and Player_ID
'''
def create_query_all_player_advanced_tid_pid():
   # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_advanced_tid_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_advanced_tid_pid(format int, t_id int, p_id int)
            BEGIN
               SELECT *
               FROM Player_Advanced
               WHERE Stat_Form = format 
               AND Team_ID = t_id 
               AND Player_ID = p_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_All_Player_Advanced_Tid_Pid was Successful")
        except:
            raise Exception("Create Procedure Query_Player_All_Player_Advanced_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_All_Player_Advanced_Tid_Pid does exists")

'''
Create Procedure that queries all from Player_Advanced based on Player_Name
'''
def create_query_all_player_advanced_pname():
     # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_advanced_pname'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_advanced_pname(format int, pname LONGTEXT)
            BEGIN
               SELECT *
               FROM Player_Advanced
               WHERE Stat_Form = format 
               AND Player_Name = pname;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_All_Player_Advanced_Pname was Successful")
        except:
            raise Exception("Create Procedure Query_Player_All_Player_Advanced_Pname Failed")
    else:
        raise Exception("Procedure Query_Player_All_Player_Advanced_Pname does exists")

'''
Create Procedure that queries all from Player_Advanced based on Season_ID and Player_Name
'''
def create_query_all_player_advanced_pname_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_advanced_pname_sid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_advanced_pname_sid(format int, pname LONGTEXT, s_id INT)
            BEGIN
               SELECT *
               FROM Player_Advanced
               WHERE Stat_Form = format 
               AND Player_Name = pname 
               AND Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_All_Player_Advanced_Pname_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_Player_All_Player_Advanced_Pname_Sid Failed")
    else:
        raise Exception("Procedure Query_Player_All_Player_Advanced_Pname_Sid does exists")

'''
Create Procedure that queries all from Player_Advanced based on Player_Name and Team_ID
'''
def create_query_all_player_advanced_pname_tid():
     # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_advanced_pname_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_advanced_pname_tid(format INT,pname LONGTEXT, t_id INT)
            BEGIN
               SELECT *
               FROM Player_Advanced
               WHERE Stat_Form = format
               AND Player_Name = pname 
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_All_Player_Advanced_Pname_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_Player_All_Player_Advanced_Pname_Tid Failed")
    else:
        raise Exception("Procedure Query_Player_All_Player_Advanced_Pname_Tid does exists")

'''
Create Procedures for reg or playoff
'''
'''
Create Procedure that queries all from Player_Advanced based on Player_ID
'''
def create_query_all_player_advanced_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_advanced_both_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_advanced_both_pid(p_id int)
            BEGIN
               SELECT *
               FROM Player_Advanced
               WHERE Player_ID = p_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_All_Player_Advanced_Both_Pid was Successful")
        except:
            raise Exception("Create Procedure Query_Player_All_Player_Advanced_Both_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_All_Player_Advanced_Both_Pid does exists")

'''
Create Procedure that queries all from Player_Advanced based on Season_ID and Player_ID
'''
def create_query_all_player_advanced_both_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_advanced_both_sid_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_advanced_both_sid_pid(s_id int, p_id int)
            BEGIN
               SELECT *
               FROM Player_Advanced
               WHERE Season_ID = s_id 
               AND Player_ID = p_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_All_Player_Advanced_Both__Sid_Pid was Successful")
        except:
            raise Exception("Create Procedure Query_Player_All_Player_Advanced_Both_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_All_Player_Advanced_Both_Sid_Pid does exists")

'''
Create Procedure that queries all from Player_Advanced based on Team_ID and Player_ID
'''
def create_query_all_player_advanced_both_tid_pid():
   # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_advanced_both_tid_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_advanced_both_tid_pid(t_id int, p_id int)
            BEGIN
               SELECT *
               FROM Player_Advanced
               WHERE Team_ID = t_id 
               AND Player_ID = p_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_All_Player_Advanced_Both_Tid_Pid was Successful")
        except:
            raise Exception("Create Procedure Query_Player_All_Player_Advanced_Both_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_All_Player_Advanced_Both_Tid_Pid does exists")

'''
Create Procedure that queries all from Player_Advanced based on Player_Name
'''
def create_query_all_player_advanced_both_pname():
     # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_advanced_both_pname'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_advanced_both_pname(pname LONGTEXT)
            BEGIN
               SELECT *
               FROM Player_Advanced
               WHERE Player_Name = pname;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_All_Player_Advanced_Both_Pname was Successful")
        except:
            raise Exception("Create Procedure Query_Player_All_Player_Advanced_Both_Pname Failed")
    else:
        raise Exception("Procedure Query_Player_All_Player_Advanced_Both_Pname does exists")

'''
Create Procedure that queries all from Player_Advanced based on Season_ID and Player_Name
'''
def create_query_all_player_advanced_both_pname_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_advanced_both_pname_sid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_advanced_both_pname_sid(pname LONGTEXT, s_id INT)
            BEGIN
               SELECT *
               FROM Player_Advanced
               WHERE Player_Name = pname 
               AND Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_All_Player_Advanced_Both_Pname_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_Player_All_Player_Advanced_Both_Pname_Sid Failed")
    else:
        raise Exception("Procedure Query_Player_All_Player_Advanced_Both_Pname_Sid does exists")

'''
Create Procedure that queries all from Player_Advanced based on Player_Name and Team_ID
'''
def create_query_all_player_advanced_both_pname_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_player_advanced_both_pname_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_player_advanced_both_pname_tid(pname LONGTEXT, t_id INT)
            BEGIN
               SELECT *
               FROM Player_Advanced
               WHERE Player_Name = pname 
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_All_Player_Advanced_Both_Pname_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_Player_All_Player_Advanced_Both_Pname_Tid Failed")
    else:
        raise Exception("Procedure Query_Player_All_Player_Advanced_Both_Pname_Tid does exists")


'''
Create All Player_Advanced 
'''
def create_player_advanced_query():
    create_query_all_player_advanced_pid()
    create_query_all_player_advanced_sid_pid()
    create_query_all_player_advanced_tid_pid()
    create_query_all_player_advanced_pname()
    create_query_all_player_advanced_pname_sid()
    create_query_all_player_advanced_pname_tid()

    create_query_all_player_advanced_both_pid()
    create_query_all_player_advanced_both_sid_pid()
    create_query_all_player_advanced_both_tid_pid()
    create_query_all_player_advanced_both_pname()
    create_query_all_player_advanced_both_pname_sid()
    create_query_all_player_advanced_both_pname_tid()
'''
Drop Procedures
'''

'''
Drop Procedure that query_all_player_advanced_pid
'''
def drop_query_all_player_advanced_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_advanced_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_advanced_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Advanced_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Advanced_Pid Failed")
    else:
        print("Procedure Query_All_Player_Advanced_Pid does not Exists")

'''
Drop Procedure that query_all_player_advanced_sid_pid
'''
def drop_query_all_player_advanced_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_advanced_sid_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_advanced_sid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Advanced_Sid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Advanced_Sid_Pid Failed")
    else:
        print("Procedure Query_All_Player_Advanced_Sid_Pid does not Exists")

'''
Drop Procedure that query_all_player_advanced_tid_pid
'''
def drop_query_all_player_advanced_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_advanced_tid_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_advanced_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Advanced_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Advanced_Tid_Pid Failed")
    else:
        print("Procedure Query_All_Player_Advanced_Tid_Pid does not Exists")

'''
Drop Procedure that query_all_player_advanced_pname
'''
def drop_query_all_player_advanced_pname():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_advanced_pname'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_advanced_pname
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Advanced_Pname was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Advanced_Pname Failed")
    else:
        print("Procedure Query_All_Player_Advanced_Pname does not Exists")

'''
Drop Procedure that query_all_player_advanced_pname_sid
'''
def drop_query_all_player_advanced_pname_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_advanced_pname_sid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_advanced_pname_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Advanced_Pname_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Advanced_Pname_Sid Failed")
    else:
        print("Procedure Query_All_Player_Advanced_Pname_Sid does not Exists")

'''
Drop Procedure that query_all_player_advanced_pname_tid
'''
def drop_query_all_player_advanced_pname_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_advanced_pname_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_advanced_pname_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Advanced_Pname_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Advanced_Pname_Tid Failed")
    else:
        print("Procedure Query_All_Player_Advanced_Pname_Tid does not Exists")

'''
Drop Procedures based on reg and regular
'''
'''
Drop Procedure that query_all_player_advanced_pid
'''
def drop_query_all_player_advanced_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_advanced_both_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_advanced_both_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Advanced_Both_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Advanced_Both_Pid Failed")
    else:
        print("Procedure Query_All_Player_Advanced_Both_Pid does not Exists")

'''
Drop Procedure that query_all_player_advanced_sid_pid
'''
def drop_query_all_player_advanced_both_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_advanced_both_sid_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_advanced_both_sid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Advanced_Both_Sid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Advanced_Both_Sid_Pid Failed")
    else:
        print("Procedure Query_All_Player_Advanced_Both_Sid_Pid does not Exists")

'''
Drop Procedure that query_all_player_advanced_tid_pid
'''
def drop_query_all_player_advanced_both_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_advanced_both_tid_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_advanced_both_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Advanced_Both_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Advanced_Both_Tid_Pid Failed")
    else:
        print("Procedure Query_All_Player_Advanced_Both_Tid_Pid does not Exists")

'''
Drop Procedure that query_all_player_advanced_pname
'''
def drop_query_all_player_advanced_both_pname():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_advanced_both_pname'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_advanced_both_pname
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Advanced_Both_Pname was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Advanced_Both_Pname Failed")
    else:
        print("Procedure Query_All_Player_Advanced_Both_Pname does not Exists")

'''
Drop Procedure that query_all_player_advanced_pname_sid
'''
def drop_query_all_player_advanced_both_pname_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_advanced_both_pname_sid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_advanced_both_pname_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Advanced_Both_Pname_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Advanced_Both_Pname_Sid Failed")
    else:
        print("Procedure Query_All_Player_Advanced_Both_Pname_Sid does not Exists")

'''
Drop Procedure that query_all_player_advanced_pname_tid
'''
def drop_query_all_player_advanced_both_pname_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_player_advanced_both_pname_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_player_advanced_both_pname_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Player_Advanced_Both_Pname_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Player_Advanced_Both_Pname_Tid Failed")
    else:
        print("Procedure Query_All_Player_Advanced_Pname_Both_Tid does not Exists")


'''
Drop all Procedure for Player_Advanced 
'''
def drop_player_advanced_query():
    drop_query_all_player_advanced_pid()
    drop_query_all_player_advanced_sid_pid()
    drop_query_all_player_advanced_tid_pid()
    drop_query_all_player_advanced_pname()
    drop_query_all_player_advanced_pname_sid()
    drop_query_all_player_advanced_pname_tid()

    drop_query_all_player_advanced_both_pid()
    drop_query_all_player_advanced_both_sid_pid()
    drop_query_all_player_advanced_both_tid_pid()
    drop_query_all_player_advanced_both_pname()
    drop_query_all_player_advanced_both_pname_sid()
    drop_query_all_player_advanced_both_pname_tid()

