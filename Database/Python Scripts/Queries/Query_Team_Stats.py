import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd
import pathlib
import sys

sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')
from Helper_DB import test_connection, create_connection, check_procedure

'''
Create procedures for minor team stats aka Team_Advanced and Team_Misc
'''
'''
Function that creates procdure for team that queries Season_ID, Team_Name and one addtional input, from a inputed table, based on Season_ID or Team_ID
'''
def create_query_team_stats_minor_one():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_minor_one'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_minor_one(IN select_one LONGTEXT, IN tbl_name longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Team_Name, ',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE ', select_one,' >= '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Minor_One was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Minor_One Failed")
    else:
        raise Exception("ProcedureQuery_Team_Stat_Minor_One does exists")

'''
Function that creates procedure for team that queries Season_ID, Team_Name, and two addtional inputs, from a inputed table, based on Season_ID or Team_ID 
'''
def create_query_team_stats_minor_two():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_minor_two'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_minor_two(IN select_one LONGTEXT, IN select_two longtext, 
            IN tbl_name longtext, IN val_one longtext, IN val_two longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Team_Name, ',select_one, ',' ,select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE ', select_one,' >= '  ,val_one,
                    ' AND ', select_two, ' >= ', val_two );
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Minor_Two was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Minor_Two Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Minor_Two does exists")

'''
Function that creates procedure for team that queries Season_ID, Team_Name, and three addtional inputs, from a input table, based on Season_ID or Team_ID
'''
def create_query_team_stats_minor_three():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_minor_three'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_minor_three(IN select_one LONGTEXT, IN select_two longtext, IN select_three longtext, 
            IN tbl_name longtext, IN val_one LONGTEXT, IN val_two longtext, IN val_three longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Team_Name, ',select_one, ',' ,select_two, ',', select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE ', select_one,' >= '  ,val_one,
                    ' AND ', select_two, ' >= ', val_two, 
                    ' AND ', select_three, '>= ', val_three);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Minor_Three was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Minor_Three Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Minor_Three does exists")

'''
Create procedures for major team stats aka Team_Per_Game and Team_Per_Poss and Team_Totals
'''
'''
Function that creates procedure for team that queries Season_ID, Team_Name, Opponent, and one addtional inputs, from a input table, based on Season_ID or Team_ID
'''
def create_query_team_stats_major_one():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_major_one'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_major_one(IN select_one LONGTEXT, IN tbl_name longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Team_Name, Opponent, ',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE Opponent = 0 
                    AND ', select_one,' >= '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Major_One was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Major_OP_One Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_OP_One does exists")

'''
Function that creates procedure for team that queries Season_ID, Team_Name, Opponent, and two addtional inputs, from a input table, based on Season_ID or Team_ID
'''
def create_query_team_stats_major_two():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_major_two'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_major_two(IN select_one LONGTEXT, In select_two LONGTEXT, IN tbl_name longtext, IN val_one longtext, IN val_two Longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Team_Name, Opponent, ',select_one, ',' ,select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE Opponent = 0 
                    AND ', select_one,' >= '  , val_one, 
                    ' AND ', select_two, ' >= ', val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Major_Two was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Major_Two Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_Two does exists")

'''
Function that creates procedure for team that queries Season_ID, Team_Name, Opponent, and three addtional inputs, from a input table, based on Season_ID or Team_ID
'''
def create_query_team_stats_major_three():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_major_three'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_major_three(IN select_one LONGTEXT, In select_two LONGTEXT, In select_three LONGTEXT,
            IN tbl_name longtext, IN val_one longtext, IN val_two LongText, IN val_three Longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Team_Name, Opponent, ',select_one, ',' ,select_two, ',',select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE Opponent = 0 
                    AND ', select_one,' >= '  , val_one,
                    ' AND ', select_two,' >= ', val_two, 
                    ' AND ', select_three,' >= ',val_three);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Major_Three was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Major_Three Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_Three does exists")

'''
Create Procedure for opponents stats
'''
'''
Function that creates procedure for team that queries op Season_ID, Team_Name and one addtional inputs from a input table, based on Season_ID or Team_ID
'''
def create_query_team_stats_major_op_one():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_major_op_one'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_major_op_one(IN select_one LONGTEXT, IN tbl_name longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Team_Name, Opponent, ',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE Opponent = 0 
                    AND ', select_one,' >= '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Major_OP_One was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Major_OP_One Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_OP_One does exists")

'''
Function that creates procedure for team that queries op Season_ID, Team_Name and two addtional inputs from a input table, based on Season_ID or Team_ID
'''
def create_query_team_stats_major_op_two():
        # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_major_op_two'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_major_op_two(IN select_one LONGTEXT, In select_two LONGTEXT, IN tbl_name longtext, IN val_one longtext, IN val_two Longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Team_Name, Opponent, ',select_one, ',' ,select_two,
                    ' FROM ', tbl_name, 
                    ' WHERE Opponent = 1 
                    AND ', select_one,' >= '  , val_one, 
                    ' AND ', select_two, ' >= ', val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Major_OP_Two was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Major_OP_Two Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_OP_Two does exists")

'''
Function that creates procedure for team that queries op Season_ID, Team_Name and three addtional inputs from a input table, based on Season_ID or Team_ID
'''
def create_query_team_stats_major_op_three():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_major_op_three'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_major_op_three(IN select_one LONGTEXT, In select_two LONGTEXT, In select_three LONGTEXT,
            IN tbl_name longtext, IN val_one longtext, IN val_two LongText, IN val_three Longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Team_Name, Opponent, ',select_one, ',' ,select_two, ',',select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE Opponent = 1 
                    AND ', select_one,' >= '  , val_one,
                    ' AND ', select_two,' >= ', val_two, 
                    ' AND ', select_three,' >= ',val_three);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Major_OP_Three was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Major_OP_Three Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_OP_Three does exists")

'''
Procedures for the five major stats
'''
'''
Function that creates procedure for team stats that queries the five major stats based on Season_ID
'''
def create_query_team_stats_primary_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_primary_sid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_primary_sid(IN tbl_name VARCHAR(100), IN val_one INT, IN val_two INT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Opponent, Team_Name, Points, Assists, True_Rebounds, Steals, Blocks
                    FROM ', tbl_name, 
                    ' WHERE Season_ID = ', val_one, 
                    ' AND Opponent = ',val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stats_Primary_Sid was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stats_Primary_Sid Failed")
    else:
        raise Exception("Procedure Query_Team_Stats_Primary_Sid does exists") 

'''
Function that creates procedure for team stats that queries the five major stats based on Team_ID
'''
def create_query_team_stats_primary_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_primary_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_primary_tid(IN tbl_name VARCHAR(100), IN val_one INT, IN val_two INT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Opponent, Team_Name, Points, Assists, True_Rebounds, Steals, Blocks
                    FROM ', tbl_name, 
                    ' WHERE Team_ID = '  , val_one,
                    ' AND Opponent = ',val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stats_Primary_Tid was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stats_Primary_Tid Failed")
    else:
        raise Exception("Procedure Query_Team_Stats_Primary_Tid does exists") 

'''
Function that creates procedure for team stats that queries the five major stats based on Season_ID and Team_ID
'''
def create_query_team_stats_primary_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_primary_sid_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_primary_sid_tid(IN tbl_name VARCHAR(100), IN val_one INT, IN val_two INT, IN val_three INT)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Opponent, Team_Name, Points, Assists, True_Rebounds, Steals, Blocks
                    FROM ', tbl_name, 
                    ' WHERE Season_ID = ', val_one, 
                    ' AND Team_ID = '  , val_two,
                    ' AND Opponent = ',val_three);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stats_Primary_Sid_Tid was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stats_Primary_Sid_Tid Failed")
    else:
        raise Exception("Procedure Query_Team_Stats_Primary_Sid_Tid does exists") 

'''
Create Procedure for to compare a team's averages and the opponent's averages 
'''
'''
Create Procedure for to compare a team's averages and the opponent's averages based based on Season_ID, Team_Name and one additional input
'''
def create_query_team_stats_major_compare_one():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_major_compare_one'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_major_compare_one(IN select_one LONGTEXT, IN tbl_name longtext, IN val longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Opponent, Team_Name, ',select_one, 
                    ' FROM ', tbl_name, 
                    ' WHERE ', select_one,' >= '  , val);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Major_Compare_One was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Major_Compare_One Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_Compare_One does exists")

'''
Create Procedure for to compare a team's averages and the opponent's averages based based on Season_ID, Team_Name and two additional input
'''
def create_query_team_stats_major_compare_two():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_major_compare_two'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_major_compare_two(IN select_one LONGTEXT, IN select_two longtext, 
            IN tbl_name longtext, IN val_one longtext, IN val_two Longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Opponent, Team_Name,  ',select_one, ',' ,select_two, 
                    ' FROM ', tbl_name, 
                    ' WHERE ', select_one,' >= '  , val_one, 
                    ' AND ', select_two, ' >= ', val_two);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Major_Compare_Two was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Major_Compare_Two Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_Compare_Two does exists")

'''
Create Procedure for to compare a team's averages and the opponent's averages based based on Season_ID, Team_Name and three additional input
'''
def create_query_team_stats_major_compare_three():
        # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if not check_procedure('query_team_stats_major_compare_three'):
        try: 
            # Create a procedure
            conn.execute(
            """
            CREATE PROCEDURE query_team_stats_major_compare_three(IN select_one LONGTEXT, IN select_two longtext, IN select_three longtext, 
            IN tbl_name longtext, IN val_one longtext, IN val_two Longtext, IN val_three Longtext)
            BEGIN
                SET @s=CONCAT(
                    'SELECT Season_ID, Team_ID, Opponent, Team_Name, ',select_one, ',' ,select_two, ',', select_three,
                    ' FROM ', tbl_name, 
                    ' WHERE ', select_one,' >= ', val_one, 
                    ' AND ', select_two, ' >= ', val_two,
                    ' AND ', select_three,' >= ', val_three );
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            END
            """)
            trans.commit()
            conn.close()
            print("Creation of procedure Query_Team_Stat_Major_Compare_Three was Successful")
        except:
            raise Exception("Creation Procedure Query_Team_Stat_Major_Compare_Three Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_Compare_Three does exists")

'''
Create all Team Stat procedures
'''
def create_team_stats_query():
    create_query_team_stats_minor_one()
    create_query_team_stats_minor_two()
    create_query_team_stats_minor_three()
    
    create_query_team_stats_major_one()
    create_query_team_stats_major_two()
    create_query_team_stats_major_three()

    create_query_team_stats_major_op_one()
    create_query_team_stats_major_op_two()
    create_query_team_stats_major_op_three()

    create_query_team_stats_primary_sid()
    create_query_team_stats_primary_tid()
    create_query_team_stats_primary_sid_tid()

    create_query_team_stats_major_compare_one()
    create_query_team_stats_major_compare_two()
    create_query_team_stats_major_compare_three()

'''
Drop Procedures
'''
'''
Drop Procedure query_team_stats_minor_one
'''
def drop_query_team_stats_minor_one():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_minor_one'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_minor_one
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stat_Minor_One was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stat_Minor_One Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Minor_One does not Exists")
    
'''
Drop Procedure query_team_stats_minor_two
'''
def drop_query_team_stats_minor_two():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_minor_two'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_minor_two
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stat_Minor_Two was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stat_Minor_Two Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Minor_Two does not Exists")

'''
Drop Procedure query_team_stats_minor_three
'''
def drop_query_team_stats_minor_three():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_minor_three'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_minor_three
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stat_Minor_Three was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stat_Minor_Three Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Minor_Three does not Exists")

'''
Drop Procedure query_team_stats_major_one
'''
def drop_query_team_stats_major_one():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_major_one'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_major_one
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stat_Major_One was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stat_Major_One Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_One does not Exists")

'''
Drop Procedure query_team_stats_major_two
'''
def drop_query_team_stats_major_two():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_major_two'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_major_two
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stat_Major_Two was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stat_Major_Two Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_Two does not Exists")

'''
Drop Procedure query_team_stats_major_three
'''
def drop_query_team_stats_major_three():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_major_three'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_major_three
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stat_Major_Three was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stat_Major_Three Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_Three does not Exists")

'''
Drop Procedure query_team_stats_major_one
'''
def drop_query_team_stats_major_op_one():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_major_op_one'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_major_op_one
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stat_Major_OP_One was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stat_Major_OP_One Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_OP_One does not Exists")

'''
Drop Procedure query_team_stats_major_two
'''
def drop_query_team_stats_major_op_two():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_major_op_two'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_major_op_two
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stat_Major_OP_Two was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stat_Major_OP_Two Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_OP_Two does not Exists")

'''
Drop Procedure query_team_stats_major_three
'''
def drop_query_team_stats_major_op_three():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_major_op_three'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_major_op_three
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stat_Major_OP_Three was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stat_Major_OP_Three Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_OP_Three does not Exists")

'''
Drop Procedure query_team_stats_primary_sid
'''
def drop_query_team_stats_primary_sid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_primary_sid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_primary_sid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stats_Primary_Sid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stats_Primary_Sid Failed")
    else:
        raise Exception("Procedure Query_Team_Stats_Primary_Sid does not Exists")

'''
Drop Procedure query_team_stats_primary_tid
'''
def drop_query_team_stats_primary_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_primary_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_primary_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stats_Primary_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stats_Primary_Tid Failed")
    else:
        raise Exception("Procedure Query_Team_Stats_Primary_Tid does not Exists")

'''
Drop Procedure query_team_stats_primary_sid_tid
'''
def drop_query_team_stats_primary_sid_tid():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_primary_sid_tid'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_primary_sid_tid
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stats_Primary_Sid_Tid was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stats_Primary_Sid_Tid Failed")
    else:
        raise Exception("Procedure Query_Team_Stats_Primary_Sid_Tid does not Exists")

'''
Drop Procedure query_team_stats_major_one
'''
def drop_query_team_stats_major_compare_one():
      # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_major_compare_one'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_major_compare_one
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stat_Major_Compare_One was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stat_Major_Compare_One Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_Compare_One does not Exists")

'''
Drop Procedure query_team_stats_major_two
'''
def drop_query_team_stats_major_compare_two():
      # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_major_compare_two'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_major_compare_two
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stat_Major_Compare_Two was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stat_Major_Compare_Two Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_Compare_Two does not Exists")

'''
Drop Procedure query_team_stats_major_three
'''
def drop_query_team_stats_major_compare_three():
      # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    if check_procedure('query_team_stats_major_compare_three'):
        try: 
            # Create a procedure
            conn.execute(
            """
            DROP PROCEDURE IF EXISTS query_team_stats_major_compare_three
            """)
            trans.commit()
            conn.close()
            print("Deletion of procedure Query_Team_Stat_Major_Compare_Three was Successful")
        except:
            raise Exception("Deletion of Procedure Query_Team_Stat_Major_Compare_Three Failed")
    else:
        raise Exception("Procedure Query_Team_Stat_Major_Compare_Three does not Exists")

'''
Drop All procedures for Team_Stat
'''
def drop_team_stats_query():
    drop_query_team_stats_minor_one()
    drop_query_team_stats_minor_two()
    drop_query_team_stats_minor_three()

    drop_query_team_stats_major_one()
    drop_query_team_stats_major_two()
    drop_query_team_stats_major_three()

    drop_query_team_stats_major_op_one()
    drop_query_team_stats_major_op_two()
    drop_query_team_stats_major_op_three()

    drop_query_team_stats_primary_sid()
    drop_query_team_stats_primary_tid()
    drop_query_team_stats_primary_sid_tid()

    drop_query_team_stats_major_compare_one()
    drop_query_team_stats_major_compare_two()
    drop_query_team_stats_major_compare_three()

'''
Main function for testing 
'''
def main():
  
    create_team_stats_query()
    #drop_team_stats_query()
main()