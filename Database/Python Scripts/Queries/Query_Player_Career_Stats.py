import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd
import pathlib
import sys

sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')
from Helper_DB import test_connection, create_connection, check_procedure

'''
Create Procedures based on regular or playoffs
'''

'''
Create Procedure based on Player_ID 
'''
'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID
'''
def create_query_player_career_stats_one_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_one_pid'):
        try: 
            # Create a parameterized query 
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_one_pid(IN select_one LONGTEXT, IN tbl_name longtext, 
            IN val_one LONGTEXT, IN val_two LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, Stat_Form,',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE Stat_Form = ? 
                    AND PLAYER_ID = ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                SET @val_two = val_two;
                EXECUTE stmt1 USING @val_one, @val_two;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Career_Stats_One_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Career_Stats_One_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Career_Stats_One_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and two addtional input, from a inputed table, based on player_ID
'''
def create_query_player_career_stats_two_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_two_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_two_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN tbl_name longtext, 
            IN val_one LONGTEXT, IN val_two LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, Stat_Form,',select_one, ',', select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE Stat_Form = ? 
                    AND PLAYER_ID = ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                SET @val_two = val_two;
                EXECUTE stmt1 USING @val_one, @val_two;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Career_Stats_Two_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Career_Stats_Two_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Career_Stats_Two_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and three addtional input, from a inputed table, based on player_ID
'''
def create_query_player_career_stats_three_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_three_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_three_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN select_three LONGTEXT, IN tbl_name longtext, 
            IN val_one LONGTEXT, IN val_two LONGTEXT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, Stat_Form,',select_one, ',', select_two, ',', select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE Stat_Form = ? 
                    AND PLAYER_ID = ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                SET @val_two = val_two;
                EXECUTE stmt1 USING @val_one, @val_two;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Career_Stats_Three_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Career_Stats_Three_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Career_Stats_Three_Pid does exists")

'''
Function that creates procedure for that queries Season_ID, Team_Name and five major stats, from a inputed table, based on player_ID
'''
def create_query_player_career_stats_primary_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_primary_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_primary_pid(IN tbl_name VARCHAR(100), IN val_one INT, IN val_two INT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, Stat_Form, Points, Assists, True_Rebounds, Steals, Blocks
                     FROM ',tbl_name, 
                    ' WHERE Stat_Form = ? 
                     AND PLAYER_ID = ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                SET @val_two = val_two;
                EXECUTE stmt1 USING @val_one, @val_two;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Primary_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Primary_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Primary_Pid does exists") 

'''
Create Procedures based on Player_ID and if the stat is above an input
'''
'''
Function that creates procedure for that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID and an input value 
'''
def create_query_player_career_stats_one_above_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_one_above_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_one_above_pid(IN select_one LONGTEXT, IN tbl_name longtext, 
            IN val_one INT, IN val_two INT, IN val_three INT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, Stat_Form,',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE Stat_Form = ? 
                    AND PLAYER_ID = ?
                    AND ',select_one, ' >= ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                SET @val_two = val_two;
                SET @val_three = val_three;
                EXECUTE stmt1 USING @val_one, @val_two, @val_three;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_One_Above_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_One_Above_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Above_Pid does exists")

'''
Function that creates procedure for that queries Season_ID, Team_Name and two addtional input, from a inputed table, based on player_ID and an input value 
'''
def create_query_player_career_stats_two_above_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_two_above_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_two_above_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN tbl_name longtext, 
            IN val_one INT, IN val_two INT, IN val_three INT, IN val_four INT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, Stat_Form,',select_one, ',',select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE Stat_Form = ? 
                    AND PLAYER_ID = ?
                    AND ',select_one, ' >= ? 
                    AND ',select_two, ' >= ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                SET @val_two = val_two;
                SET @val_three = val_three;
                SET @val_four = val_four;
                EXECUTE stmt1 USING @val_one, @val_two, @val_three, @val_four;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Two_Above_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Two_Above_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Above_Pid does exists")

'''
Function that creates procedure for that queries Season_ID, Team_Name and three addtional input, from a inputed table, based on player_ID and an input value 
'''
def create_query_player_career_stats_three_above_pid():
     # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_three_above_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_three_above_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN select_three LONGTEXT, IN tbl_name longtext, 
            IN val_one INT, IN val_two INT, IN val_three INT, IN val_four INT, IN val_five INT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, Stat_Form,',select_one, ',',select_two, ',',select_three, 
                    ' FROM ', tbl_name, 
                    ' WHERE Stat_Form = ? 
                    AND PLAYER_ID = ?
                    AND ',select_one, ' >= ? 
                    AND ',select_two, ' >= ?
                    AND ',select_three, ' >= ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                SET @val_two = val_two;
                SET @val_three = val_three;
                SET @val_four = val_four;
                SET @val_five = val_five;
                EXECUTE stmt1 USING @val_one, @val_two, @val_three, @val_four, @val_five;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Three_Above_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Three_Above_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Above_Pid does exists")

'''
Create Procedure based on reg and playoffs
'''
'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID
'''
def create_query_player_career_stats_one_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_one_both_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_one_both_pid(IN select_one LONGTEXT, IN tbl_name longtext, IN val_one longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, ',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE PLAYER_ID = ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                EXECUTE stmt1 USING @val_one;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Career_Stats_One_Both_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Career_Stats_One_Both_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Career_Stats_One_Both_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and two addtional input, from a inputed table, based on player_ID
'''
def create_query_player_career_stats_two_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_two_both_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_two_both_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN tbl_name longtext, IN val_one longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, ',select_one, ',',select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE PLAYER_ID = ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                EXECUTE stmt1 USING @val_one;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of Procedure Query_Player_Career_Stats_Two_Both_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Career_Stats_Two_Both_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Career_Stats_Two_Both_Pid does exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and three addtional input, from a inputed table, based on player_ID
'''
def create_query_player_career_stats_three_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_three_both_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_three_both_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN select_three LONGTEXT,
            IN tbl_name longtext, IN val_one longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, ',select_one, ',',select_two, ',',select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE PLAYER_ID = ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                EXECUTE stmt1 USING @val_one;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Career_Stats_Three_Both_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Career_Stats_Three_Both_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Career_Stats_Three_Both_Pid does exists")

'''
Function that creates procedure for that queries Season_ID, Team_Name and Player_ID and 5 major stats category from a inputed table.
'''
def create_query_player_career_stats_primary_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_primary_both_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_primary_both_pid(IN tbl_name VARCHAR(100), IN val_one INT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, Stat_Form, Points, Assists, True_Rebounds, Steals, Blocks
                     FROM ', tbl_name, 
                    ' WHERE PLAYER_ID = ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                EXECUTE stmt1 USING @val_one;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Primary_Both_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Both_Primary_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Primary_Both_Pid does exists") 

'''
Function that creates procedure for that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID and an input value 
'''
def create_query_player_career_stats_one_both_above_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_one_both_above_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_one_both_above_pid(IN select_one LONGTEXT, IN tbl_name longtext, 
            IN val_one INT, IN val_two INT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, Stat_Form,',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE PLAYER_ID = ?
                    AND ',select_one, ' >= ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                SET @val_two = val_two;
                EXECUTE stmt1 USING @val_one, @val_two;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_One_Above_Both_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_One_Both_Above_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_One_Both_Above_Pid does exists")

'''
Function that creates procedure for that queries Season_ID, Team_Name and two addtional input, from a inputed table, based on player_ID and two input value 
'''
def create_query_player_career_stats_two_both_above_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_two_both_above_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_two_both_above_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN tbl_name longtext, 
            IN val_one INT, IN val_two INT, IN val_three INT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, Stat_Form,',select_one, ',',select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE PLAYER_ID = ?
                    AND ',select_one, ' >= ? 
                    AND ',select_two, ' >= ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                SET @val_two = val_two;
                SET @val_three = val_three;
                EXECUTE stmt1 USING @val_one, @val_two, @val_three;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Two_Above_Both_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Two_Both_Above_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Two_Both_Above_Pid does exists")

'''
Function that creates procedure for that queries Season_ID, Team_Name and three addtional input, from a inputed table, based on player_ID and three input value 
'''
def create_query_player_career_stats_three_both_above_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_player_career_stats_three_both_above_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_player_career_stats_three_both_above_pid(IN select_one LONGTEXT, IN select_two LONGTEXT, IN select_three LONGTEXT, IN tbl_name longtext, 
            IN val_one INT, IN val_two INT, IN val_three INT, IN val_four INT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Player_ID, Player_Name, Stat_Form,',select_one, ',',select_two, ',',select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE PLAYER_ID = ?
                    AND ',select_one, ' >= ? 
                    AND ',select_two, ' >= ?
                    AND ',select_three, ' >= ?');
                PREPARE stmt1 FROM @s;
                SET @val_one = val_one;
                SET @val_two = val_two;
                SET @val_three = val_three;
                SET @val_four = val_four;
                EXECUTE stmt1 USING @val_one, @val_two, @val_three, @val_four;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Player_Stats_Three_Above_Both_Pid was Successful")
        except:
            raise Exception("Creation Procedure Query_Player_Stats_Three_Both_Above_Pid Failed")
    else:
        raise Exception("Procedure Query_Player_Stats_Three_Both_Above_Pid does exists")

'''
Create All Query for Player_Career_Stats
'''
def create_player_career_stats_query():
    create_query_player_career_stats_one_pid()
    create_query_player_career_stats_two_pid()
    create_query_player_career_stats_three_pid()
    create_query_player_career_stats_primary_pid()

    create_query_player_career_stats_one_both_pid()
    create_query_player_career_stats_two_both_pid()
    create_query_player_career_stats_three_both_pid()
    create_query_player_career_stats_primary_both_pid()

'''
Drop Procedures
'''

'''
Drop Procedures on regular or playoffs
'''
'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID
'''
def drop_query_player_career_stats_one_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_career_stats_one_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_career_stats_one_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Career_Stats_One_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Career_Stats_One_Pid Failed")
    else:
        print("Procedure Query_Player_Career_Stats_One_Pid does not Exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID
'''
def drop_query_player_career_stats_two_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_career_stats_two_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_career_stats_two_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Career_Stats_Two_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Career_Stats_Two_Pid Failed")
    else:
        print("Procedure Query_Player_Career_Stats_Two_Pid does not Exists")

'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on player_ID
'''
def drop_query_player_career_stats_three_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_career_stats_three_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_career_stats_three_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Career_Stats_Three_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Career_Stats_Three_Pid Failed")
    else:
        print("Procedure Query_Player_Career_Stats_Three_Pid does not Exists")

'''
Drop Procedure query_player_career_stats_primary_pid
'''
def drop_query_player_career_stats_primary_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_career_stats_primary_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_career_stats_primary_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Primary_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Primary_Pid Failed")
    else:
        print("Procedure Query_Player_Stats_Primary_Pid does not Exists")


'''
Drop Procedures based on playoff and reg
'''
'''
Drop Procedure query_player_career_stats_one_both_pid
'''
def drop_query_player_career_stats_one_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_career_stats_one_both_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_career_stats_one_both_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Career_Stats_One_Both_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Career_Stats_One_Both_Pid Failed")
    else:
        print("Procedure Query_Player_Career_Stats_One_Both_Pid does not Exists")

'''
Drop Procedure query_player_career_stats_two_both_pid
'''
def drop_query_player_career_stats_two_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_career_stats_two_both_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_career_stats_two_both_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Career_Stats_Two_Both_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Career_Stats_Two_Both_Pid Failed")
    else:
        print("Procedure Query_Player_Career_Stats_Two_Both_Pid does not Exists")

'''
Drop Procedure query_player_career_stats_three_both_pid
'''
def drop_query_player_career_stats_three_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_career_stats_three_both_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_career_stats_three_both_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Career_Stats_Three_Both_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Career_Stats_Three_Both_Pid Failed")
    else:
        print("Procedure Query_Player_Career_Stats_Three_Both_Pid does not Exists")

'''
Drop Procedure query_player_career_stats_primary_both_pid
'''
def drop_query_player_career_stats_primary_both_pid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_player_career_stats_primary_both_pid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_player_career_stats_primary_both_pid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Player_Stats_Primary_Both_Pid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Player_Stats_Primary_Both_Pid Failed")
    else:
        print("Procedure Query_Player_Stats_Primary_Both_Pid does not Exists")
 
'''
Drop Procedure all Player_Career_Stats
'''
def drop_player_career_stats_query():
    drop_query_player_career_stats_one_pid()
    drop_query_player_career_stats_two_pid()
    drop_query_player_career_stats_three_pid()
    drop_query_player_career_stats_primary_pid()

    drop_query_player_career_stats_one_both_pid()
    drop_query_player_career_stats_two_both_pid()
    drop_query_player_career_stats_three_both_pid()
    drop_query_player_career_stats_primary_both_pid()
