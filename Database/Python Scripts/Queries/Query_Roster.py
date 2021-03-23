import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd
import pathlib
import sys

sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')
from Helper_DB import test_connection, create_connection, check_procedure

'''
Create Procedure
'''
'''
Function that creates procedure that queries Roster based on Season_ID
'''
def create_query_all_roster_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_roster_sid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_roster_sid(s_id int)
            BEGIN
               SELECT *
               FROM Roster
               Where Season_ID = s_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Roster_Sid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Roster_Sid Failed")
    else:
        raise Exception("Procedure Query_All_Roster_Sid does exists")

'''
Function that creates procedure that queries Roster based on Team_ID
'''
def create_query_all_roster_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_roster_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_roster_tid(t_id int)
            BEGIN
               SELECT *
               FROM Roster
               Where Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Roster_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Roster_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Roster_Tid does exists")

'''
Function that creates procedure that queries Roster based on Player_ID
'''
def create_query_all_roster_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_roster_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_roster_pid(p_id int)
            BEGIN
               SELECT *
               FROM Roster
               Where Player_ID = p_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Roster_Pid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Roster_Pid Failed")
    else:
        raise Exception("Procedure Query_All_Roster_Pid exists")

'''
Function that creates procedure that queries Roster based on Player_Name
'''
def create_query_all_roster_pname():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_roster_pname'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_roster_pname(pname varchar(45))
            BEGIN
               SELECT *
               FROM Roster
               Where Player_Name = pname;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Roster_Pname was Successful")
        except:
            raise Exception("Create Procedure Query_All_Roster_Pname Failed")
    else:
        raise Exception("Procedure Query_All_Roster_Pname does exists")

'''
Function that creates procedure that queries Roster based on Team_Name
'''
def create_query_all_roster_tname():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_roster_tname'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_roster_tname(tname varchar(45))
            BEGIN
               SELECT *
               FROM Roster
               Where Team_Name = tname;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Roster_Tname was Successful")
        except:
            raise Exception("Create Procedure Query_All_Roster_Tname Failed")
    else:
        raise Exception("Procedure Query_All_Roster_Tname does exists")

'''
Function that creates procedure that queries Roster based on Player_ABV
'''
def create_query_all_roster_abv():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_roster_abv'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_roster_abv(abv varchar(3))
            BEGIN
               SELECT *
               FROM Roster
               Where Team_ABV = abv;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Roster_ABV was Successful")
        except:
            raise Exception("Create Procedure Query_All_Roster_ABV Failed")
    else:
        raise Exception("Procedure Query_All_Roster_ABV does exists")

'''
Function that creates procedure that queries Roster based on Player_College_Name
'''
def create_query_all_roster_college():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_roster_college'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_roster_college(college varchar(100))
            BEGIN
               SELECT *
               FROM Roster
               Where Player_College_Name = college;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Roster_College was Successful")
        except:
            raise Exception("Create Procedure Query_All_Roster_College Failed")
    else:
        raise Exception("Procedure Query_All_Roster_College does exists")

'''
Function that creates procedure that queries Roster based on Season_ID and Team_ID
'''
def create_query_all_roster_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_roster_sid_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_roster_sid_tid(s_id int, t_id int)
            BEGIN
               SELECT *
               FROM Roster
               Where Season_ID = s_id
               AND Team_ID = t_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Roster_Sid_Tid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Roster_Sid_Tid Failed")
    else:
        raise Exception("Procedure Query_All_Roster_Sid_Tid does exists")

'''
Function that creates procedure that queries Roster based on Player_ID and Team_ID
'''
def create_query_all_roster_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_roster_tid_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_roster_tid_pid(t_id int, p_id int)
            BEGIN
               SELECT *
               FROM Roster
               Where Team_ID = t_id
               AND Player_ID = p_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Roster_Tid_Pid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Roster_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_All_Roster_Tid_Pid does exists")

'''
Function that creates procedure that queries Roster based on Season_ID, Team_ID, Player_ID
'''
def create_query_all_roster_sid_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_all_roster_sid_tid_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_all_roster_sid_tid_pid(s_id int, t_id int, p_id int)
            BEGIN
               SELECT *
               FROM Roster
               Where Season_ID = s_id
               AND Team_ID = t_id
               AND Player_ID = p_id;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_All_Roster_Sid_Tid_Pid was Successful")
        except:
            raise Exception("Create Procedure Query_All_Roster_Sid_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_All_Roster_Sid_Tid_Pid does exists")

'''
Function that creates all roster query
'''
def create_roster_query():
    create_query_all_roster_sid()
    create_query_all_roster_tid()
    create_query_all_roster_pid()
    create_query_all_roster_pname()
    create_query_all_roster_tname()
    create_query_all_roster_abv()
    create_query_all_roster_college()
    create_query_all_roster_sid_tid()
    create_query_all_roster_tid_pid()
    create_query_all_roster_sid_tid_pid()

'''
Drop Procedure
'''
'''
Function that drops query_all_roster_sid
'''
def drop_query_all_roster_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_roster_sid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_roster_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Roster_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Roster_Sid Failed")
    else:
        print("Procedure Query_All_Roster_Sid does not Exists")

'''
Function that drops query_all_roster_sid
'''
def drop_query_all_roster_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_roster_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_roster_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Roster_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Roster_Tid Failed")
    else:
        print("Procedure Query_All_Roster_Tid does not Exists")

'''
Function that drops query_all_roster_pid
'''
def drop_query_all_roster_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_roster_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_roster_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Roster_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Roster_Pid Failed")
    else:
        print("Procedure Query_All_Roster_Pid does not Exists")

'''
Function that drop query query_all_roster_pname
'''
def drop_query_all_roster_pname():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_roster_pname'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_roster_pname
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Roster_Pname was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Roster_Pname Failed")
    else:
        print("Procedure Query_All_Roster_Pname does not Exists")

'''
Function that drop query query_all_roster_tname
'''
def drop_query_all_roster_tname():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_roster_tname'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_roster_tname
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Roster_Tname was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Roster_Tname Failed")
    else:
        print("Procedure Query_All_Roster_Tname does not Exists") 

'''
Function that drop query query_all_roster_abv
'''
def drop_query_all_roster_abv():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_roster_abv'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_roster_abv
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Roster_Abv was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Roster_Abv Failed")
    else:
        print("Procedure Query_All_Roster_Tname does not Exists") 

'''
Function that drop query query_all_roster_college
'''
def drop_query_all_roster_college():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_roster_college'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_roster_college
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Roster_College was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Roster_College Failed")
    else:
        print("Procedure Query_All_Roster_College does not Exists") 

'''
Function that drop query query_all_roster_sid_tid
'''
def drop_query_all_roster_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_roster_sid_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_roster_sid_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Roster_Sid_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Roster_Sid_Tid Failed")
    else:
        print("Procedure Query_All_Roster_Sid_Tid does not Exists")

'''
Function that drop query query_all_roster_tid_pid
'''
def drop_query_all_roster_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_roster_tid_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_roster_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Roster_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Roster_Tid_Pid Failed")
    else:
        print("Procedure Query_All_Roster_Tid_Pid does not Exists")

'''
Function that drop query query_all_roster_sid_tid
'''
def drop_query_all_roster_sid_tid_pid():
     # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_all_roster_sid_tid_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_all_roster_sid_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_All_Roster_Sid_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_All_Roster_Sid_Tid_Pid Failed")
    else:
        print("Procedure Query_All_Roster_Sid_Tid_Pid does not Exists")

'''
Function that drop query for roster
'''
def drop_roster_query():
    drop_query_all_roster_sid()
    drop_query_all_roster_tid()
    drop_query_all_roster_pid()
    drop_query_all_roster_pname()
    drop_query_all_roster_tname()
    drop_query_all_roster_abv()
    drop_query_all_roster_college()
    drop_query_all_roster_sid_tid()
    drop_query_all_roster_tid_pid()
    drop_query_all_roster_sid_tid_pid()
