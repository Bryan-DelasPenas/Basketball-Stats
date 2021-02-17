import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_procedure

'''
Create Procedures based on regular or playoffs
'''

'''
Create Procedures based on player_ID
'''
'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID
'''
def create_query_player_stats_one_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_one_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_one_pid(IN select_one LONGTEXT, IN tbl_name longtext, 
            IN val LONGTEXT, IN val_two LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, Stat_Form,',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' AND Stat_Form = ',val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_One_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_One_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and two addtional input, from a inputed table, based on player_ID
'''
def create_query_player_stats_two_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_two_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_two_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN tbl_name longtext, 
            IN val_one longtext, value_two longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, Stat_Form,',select_one, ',', select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' AND Stat_Form = ',val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Two_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Two_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and three addtional input, from a inputed table, based on player_ID
'''
def create_query_player_stats_three_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_three_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_three_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN select_three LONGTEXT, IN tbl_name longtext, 
            IN val_one longtext, IN val_two LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, Stat_Form,',select_one, ',', select_two, ',', select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' AND Stat_Form = ',val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Three_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Three_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Pid does exists") 

'''
Create procedures based on Team_ID and Player_ID
'''
'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID and Team_ID
'''
def create_query_player_stats_one_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_one_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_one_tid_pid(IN select_one LONGTEXT, IN tbl_name longtext, 
            IN val LONGTEXT, IN val_two LONGTEXT, IN val_three LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, Stat_Form,',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' AND Team_ID = ' , val_two, 
                    ' AND Stat_Form = ',val_three);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_One_Tid_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_One_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Tid_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID and Team_ID
'''
def create_query_player_stats_two_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_two_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_two_tid_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN tbl_name longtext, 
            IN val LONGTEXT, IN val_two LONGTEXT, IN val_three LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, Stat_Form,',select_one, ',', select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' AND Team_ID = ' , val_two, 
                    ' AND Stat_Form = ',val_three);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Two_Tid_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Two_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Tid_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID and Team_ID
'''
def create_query_player_stats_three_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_three_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_three_tid_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN select_three LONGTEXT, IN tbl_name longtext, 
            IN val LONGTEXT, IN val_two LONGTEXT, IN val_three LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, Stat_Form,',select_one, ',', select_two, ',', select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' AND Team_ID = ' , val_two, 
                    ' AND Stat_Form = ',val_three);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Three_Tid_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Three_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Tid_Pid does exists")

'''
Create procedure based on Season_ID and Player_ID
'''
'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID and Season_ID
'''
def create_query_player_stats_one_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_one_sid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_one_sid_pid(IN select_one LONGTEXT, IN tbl_name longtext, 
            IN val LONGTEXT, IN val_two LONGTEXT, IN val_three LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, Stat_Form,',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' AND Season_ID = ' , val_two, 
                    ' AND Stat_Form = ',val_three);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_One_Sid_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_One_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Sid_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID and Season_ID
'''
def create_query_player_stats_two_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_two_sid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_two_sid_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN tbl_name longtext, 
            IN val LONGTEXT, IN val_two LONGTEXT, IN val_three LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, Stat_Form,',select_one, ',', select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' AND Season_ID = ' , val_two, 
                    ' AND Stat_Form = ',val_three);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Two_Tid_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Two_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Tid_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID and Season_ID
'''
def create_query_player_stats_three_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_three_sid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_three_sid_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN select_three LONGTEXT, IN tbl_name longtext, 
            IN val LONGTEXT, IN val_two LONGTEXT, IN val_three LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, Stat_Form,',select_one, ',', select_two, ',', select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' AND Season_ID = ' , val_two, 
                    ' AND Stat_Form = ',val_three);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Three_Sid_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Three_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Sid_Pid does exists")


'''
Create procedure for playoffs and reg
'''

'''
Create procedure based on Player_ID
'''
'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID 
'''
def create_query_player_stats_one_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_one_both_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_one_both_pid(IN select_one LONGTEXT, IN tbl_name longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, ',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_One_Both_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_One_Both_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Both_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and two addtional input, from a inputed table, based on player_ID 
'''
def create_query_player_stats_two_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_two_both_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_two_both_pid(IN select_one LONGTEXT, select_two LONGTEXT ,IN tbl_name longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, ',select_one, ',' ,select_two, 
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Two_Both_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Two_Both_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Both_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and three addtional input, from a inputed table, based on player_ID 
'''
def create_query_player_stats_three_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_three_both_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_three_both_pid(IN select_one LONGTEXT, IN tbl_name longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, ',select_one, ',' ,select_two, ',', select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Three_Both_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Three_Both_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Both_Pid does exists")

'''
Create procedure based on Team_ID and Player_ID
'''
'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID and Team_ID
'''
def create_query_player_stats_one_both_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_one_both_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_one_both_tid_pid(IN select_one LONGTEXT, IN tbl_name longtext, 
            IN val_one longtext, IN val_two LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, ',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' WHERE Team_ID = ', val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_One_Both_Tid_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_One_Both_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Both_Tid_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and two addtional input, from a inputed table, based on player_ID and Team_ID
'''
def create_query_player_stats_two_both_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_two_both_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_two_both_tid_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN tbl_name longtext, 
            IN val_one longtext, IN val_two LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, ',select_one, ',',select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' WHERE Team_ID = ', val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Two_Both_Tid_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Two_Both_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Both_Tid_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and three addtional input, from a inputed table, based on player_ID and Team_ID
'''
def create_query_player_stats_three_both_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_three_both_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_three_both_tid_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN select_three LONGTEXT, IN tbl_name longtext, 
            IN val_one longtext, IN val_two LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, ',select_one, ',',select_two, ',',select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' WHERE Team_ID = ', val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Three_Both_Tid_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Three_Both_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Both_Tid_Pid does exists")

'''
Create procedure based on Season_ID and Player_ID
'''
'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID and Season_ID
'''
def create_query_player_stats_one_both_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_one_both_sid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_one_both_sid_pid(IN select_one LONGTEXT, IN tbl_name longtext, 
            IN val_one longtext, IN val_two LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, ',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' WHERE Season_ID = ', val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_One_Both_Sid_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_One_Both_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Both_Sid_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and two addtional input, from a inputed table, based on player_ID and Season_ID
'''
def create_query_player_stats_two_both_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_two_both_sid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_two_both_sid_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN tbl_name longtext, 
            IN val_one longtext, IN val_two LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, ',select_one, ',',select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' WHERE Season_ID = ', val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Two_Both_Sid_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Two_Both_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Both_Sid_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and three addtional input, from a inputed table, based on player_ID and Season_ID
'''
def create_query_player_stats_three_both_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_stats_three_both_sid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            CREATE PROCEDURE query_player_stats_three_both_sid_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN select_three LONGTEXT, IN tbl_name longtext, 
            IN val_one longtext, IN val_two LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Player_ID, Player_Name, ',select_one, ',',select_two, ',',select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE Player_ID = '  , val_one,
                    ' WHERE Team_ID = ', val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Three_Both_Sid_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Three_Both_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Both_Sid_Pid does exists")

'''
Create all Player_Stats Procedures
'''
def create_player_stats_query():
    create_query_player_stats_one_pid()
    create_query_player_stats_two_pid()
    create_query_player_stats_three_pid()

    create_query_player_stats_one_tid_pid()
    create_query_player_stats_two_tid_pid()
    create_query_player_stats_three_tid_pid()

    create_query_player_stats_one_sid_pid()
    create_query_player_stats_two_sid_pid()
    create_query_player_stats_three_sid_pid()

    create_query_player_stats_one_both_pid()
    create_query_player_stats_two_both_pid()
    create_query_player_stats_three_both_pid()

    create_query_player_stats_one_both_tid_pid()
    create_query_player_stats_two_both_tid_pid()
    create_query_player_stats_three_both_tid_pid()

    create_query_player_stats_one_both_sid_pid()
    create_query_player_stats_two_both_sid_pid()
    create_query_player_stats_three_both_sid_pid()

'''
Drop procedures
'''
'''
Drop Procedures reg or playoffs
'''

'''
Drop procedures based on Player_ID
'''
'''
Drop Procedure query_player_stats_one_pid
'''
def drop_query_player_stats_one_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_one_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_one_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_One_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_One_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Pid does not Exists")

'''
Drop Procedure query_player_stats_two_pid
'''
def drop_query_player_stats_two_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_two_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_two_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Two_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Two_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Pid does not Exists")

'''
Drop Procedure query_player_stats_three_pid
'''
def drop_query_player_stats_three_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_three_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_three_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Three_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Three_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Pid does not Exists")

'''
Drop Procedures based on Team_ID and Player_ID
'''
'''
Drop Procedure query_player_stats_one_tid_pid
'''
def drop_query_player_stats_one_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_one_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_one_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_One_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_One_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Tid_Pid does not Exists")

'''
Drop Procedure query_player_stats_two_tid_pid
'''
def drop_query_player_stats_two_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_two_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_two_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Two_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Two_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Tid_Pid does not Exists")

'''
Drop Procedure query_player_stats_three_tid_pid
'''
def drop_query_player_stats_three_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_three_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_three_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Three_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Three_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Tid_Pid does not Exists")


'''
Drop Procedure based on Team_ID and Player_ID
'''
'''
Drop Procedure query_player_stats_one_tid_pid
'''
def drop_query_player_stats_one_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_one_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_one_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_One_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_One_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Tid_Pid does not Exists")

'''
Drop Procedure query_player_stats_two_tid_pid
'''
def drop_query_player_stats_two_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_two_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_two_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Two_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Two_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Tid_Pid does not Exists")

'''
Drop Procedure query_player_stats_three_tid_pid
'''
def drop_query_player_stats_three_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_three_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_three_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Three_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Three_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Tid_Pid does not Exists")

'''
Drop Procedure based on Season_ID and Player_ID
'''
'''
Drop Procedure query_player_stats_one_sid_pid
'''
def drop_query_player_stats_one_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_one_sid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_one_sid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_One_Sid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_One_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Sid_Pid does not Exists")

'''
Drop Procedure query_player_stats_two_sid_pid
'''
def drop_query_player_stats_two_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_two_sid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_two_sid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Two_Sid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Two_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Sid_Pid does not Exists")

'''
Drop Procedure query_player_stats_three_sid_pid
'''
def drop_query_player_stats_three_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_three_sid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_three_sid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Three_Sid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Three_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Sid_Pid does not Exists")


'''
Drop Procedures on reg and playoffs
'''

'''
Drop Procedures based on Player_ID
'''
'''
Drop Procedure query_player_stats_one_both_pid
'''
def drop_query_player_stats_one_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_one_both_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_one_both_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_One_Both_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_One_Both_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Both_Pid does not Exists")

'''
Drop Procedure query_player_stats_two_both_pid
'''
def drop_query_player_stats_two_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_two_both_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_two_both_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Two_Both_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Two_Both_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Both_Pid does not Exists")

'''
Drop Procedure query_player_stats_three_both_pid
'''
def drop_query_player_stats_three_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_three_both_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_three_both_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Three_Both_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Three_Both_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Both_Pid does not Exists")

'''
Drop Procedures based on Team_ID and Player_ID
'''
'''
Drop Procedure query_player_stats_one_both_tid_pid
'''
def drop_query_player_stats_one_both_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_one_both_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_one_both_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_One_Both_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_One_Both_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Both_Tid_Pid does not Exists")

'''
Drop Procedure query_player_stats_two_both_tid_pid
'''
def drop_query_player_stats_two_both_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_two_both_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_two_both_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Two_Both_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Two_Both_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Both_Tid_Pid does not Exists")

'''
Drop Procedure query_player_stats_three_both_tid_pid
'''
def drop_query_player_stats_three_both_tid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_three_both_tid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_three_both_tid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Three_Both_Tid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Three_Both_Tid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Both_Tid_Pid does not Exists")

'''
Drop Procedures based on Season_ID and Player_ID
'''
'''
Drop Procedure query_player_stats_one_both_sid_pid
'''
def drop_query_player_stats_one_both_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_one_both_sid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_one_both_sid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_One_Both_Sid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_One_Both_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Both_Sid_Pid does not Exists")

'''
Drop Procedure query_player_stats_two_both_sid_pid
'''
def drop_query_player_stats_two_both_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_two_both_sid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_two_both_sid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Two_Both_Sid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Two_Both_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Both_Sid_Pid does not Exists")

'''
Drop Procedure query_player_stats_three_both_tid_pid
'''
def drop_query_player_stats_three_both_sid_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_stats_three_both_sid_pid'):
        try: 
            # Create a parameterized query for insertion
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_stats_three_both_sid_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Three_Both_Sid_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Three_Both_Sid_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Both_Sid_Pid does not Exists")

'''
Drop All Procedures for Player_Stats
'''
def drop_player_stats_query():
    drop_query_player_stats_one_pid()
    drop_query_player_stats_two_pid()
    drop_query_player_stats_three_pid()

    drop_query_player_stats_one_tid_pid()
    drop_query_player_stats_two_tid_pid()
    drop_query_player_stats_three_tid_pid()
    
    drop_query_player_stats_one_sid_pid()
    drop_query_player_stats_two_sid_pid()
    drop_query_player_stats_three_sid_pid()

    drop_query_player_stats_one_both_pid()
    drop_query_player_stats_two_both_pid()
    drop_query_player_stats_three_both_pid()

    drop_query_player_stats_one_both_tid_pid()
    drop_query_player_stats_two_both_tid_pid()
    drop_query_player_stats_three_both_tid_pid()

    drop_query_player_stats_one_both_sid_pid()
    drop_query_player_stats_two_both_sid_pid()
    drop_query_player_stats_three_both_sid_pid()

'''
Main function for testing 
'''
def main():
 
    create_player_stats_query()
    drop_player_stats_query()
main()