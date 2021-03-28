import pandas as pd
import numpy as np
import sys 
import pathlib
import os
import re
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')

import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine

from Helper_DB import create_connection, test_connection, check_table
from Regular_Expression import season_id_regex, team_id_regex, team_name_regex, team_abv_regex, floating_point_regex, reg_string_regex, binary_regex
from Constants import VALID_TABLE_TEAM_STATS_MINOR, VALID_COL_TEAM_STATS_MINOR, STRING_STATS_TEAM_STATS_MINOR, VALID_TABLE_TEAM_STATS_MAJOR, VALID_COL_TEAM_STATS_MAJOR 

'''
Function calls query_team_stats_minor_one
'''
def call_query_team_stats_minor_one(col_one, table_name, val_one):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MINOR):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_TEAM_STATS_MINOR[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check if contents of col_one is string  
    if(col_one in STRING_STATS_TEAM_STATS_MINOR):
        
        # Check for regex for parameter val_one
        if(reg_string_regex(val_one)):
            return None

    # Col_One contents is float or int 
    else:
        # Check Regex for parameter val_one
        if(floating_point_regex(val_one)):
            return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_minor_one(%s, %s, %s)
    """, [col_one, table_name, val_one]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', col_one])
    return df_result

'''
Function calls query_team_stats_minor_two
'''
def call_query_team_stats_minor_two(col_one, col_two, table_name, val_one, val_two):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MINOR):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_TEAM_STATS_MINOR[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_TEAM_STATS_MINOR[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Check if contents of col_one is string  
    if(col_one in STRING_STATS_TEAM_STATS_MINOR):
        
        # Check for regex for parameter val_one
        if(reg_string_regex(val_one)):
            return None

    # Col_One contents is float or int 
    else:
        # Check Regex for parameter val_one
        if(floating_point_regex(val_one)):
            return None

    # Check if contents of col_two is string  
    if(col_two in STRING_STATS_TEAM_STATS_MINOR):
        
        # Check for regex for parameter val_two
        if(reg_string_regex(val_two)):
            return None

    # Col_two contents is float or int 
    else:
        # Check Regex for parameter val_one
        if(floating_point_regex(val_two)):
            return None

    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_minor_two(%s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, val_one, val_two]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', col_one, col_two])
    return df_result

'''
Function calls query_team_stats_minor_three
'''
def call_query_team_stats_minor_three(col_one, col_two, col_three, table_name, val_one, val_two, val_three):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MINOR):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_TEAM_STATS_MINOR[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_TEAM_STATS_MINOR[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

     # Next check if col_three is in table_name
    if(not col_three in VALID_COL_TEAM_STATS_MINOR[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check if contents of col_one is string  
    if(col_one in STRING_STATS_TEAM_STATS_MINOR):
        
        # Check for regex for parameter val_one
        if(reg_string_regex(val_one)):
            return None

    # Col_One contents is float or int 
    else:
        # Check Regex for parameter val_one
        if(floating_point_regex(val_one)):
            return None

    # Check if contents of col_two is string  
    if(col_two in STRING_STATS_TEAM_STATS_MINOR):
        
        # Check for regex for parameter val_two
        if(reg_string_regex(val_two)):
            return None

    # Col_two contents is float or int 
    else:
        # Check Regex for parameter val_two
        if(floating_point_regex(val_two)):
            return None

    # Check if contents of col_three is string  
    if(col_three in STRING_STATS_TEAM_STATS_MINOR):
        
        # Check for regex for parameter val_three
        if(reg_string_regex(val_three)):
            return None

    # Col_three contents is float or int 
    else:
        # Check Regex for parameter val_three
        if(floating_point_regex(val_three)):
            return None

    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_minor_three(%s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, val_one, val_two, val_three]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', col_one, col_two, col_three])
    return df_result

'''
Function calls query_team_stats_major_one
'''
def call_query_team_stats_major_one(col_one, table_name, val_one):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MAJOR):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check Regex for parameter val_one
    if(floating_point_regex(val_one)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_major_one(%s, %s, %s)
    """, [col_one, table_name, val_one]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Opponent', col_one])
    return df_result

'''
Function calls query_team_stats_major_two
'''
def call_query_team_stats_major_two(col_one, col_two, table_name, val_one, val_two):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MAJOR):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Check Regex for parameter val_one
    if(floating_point_regex(val_one)):
        return None

    # Check Regex for parameter val_one
    if(floating_point_regex(val_two)):
        return None

    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_major_two(%s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, val_one, val_two]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Opponent', col_one, col_two])
    return df_result

'''
Function calls query_team_stats_major_three
'''
def call_query_team_stats_major_three(col_one, col_two, col_three, table_name, val_one, val_two, val_three):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MAJOR):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

     # Next check if col_three is in table_name
    if(not col_three in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check Regex for parameter val_one
    if(floating_point_regex(val_one)):
        return None

    # Check Regex for parameter val_two
    if(floating_point_regex(val_two)):
        return None

    # Check Regex for parameter val_three
    if(floating_point_regex(val_three)):
        return None

    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_major_three(%s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, val_one, val_two, val_three]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Opponent', col_one, col_two, col_three])
    return df_result

'''
Function calls query_team_stats_major_op_one
'''
def call_query_team_stats_major_op_one(col_one, table_name, val_one):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MAJOR):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check Regex for parameter val_one
    if(floating_point_regex(val_one)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_major_op_one(%s, %s, %s)
    """, [col_one, table_name, val_one]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name',  'Opponent', col_one])
    return df_result

'''
Function calls query_team_stats_major_op_two
'''
def call_query_team_stats_major_op_two(col_one, col_two, table_name, val_one, val_two):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MAJOR):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Check Regex for parameter val_one
    if(floating_point_regex(val_one)):
        return None

    # Check Regex for parameter val_one
    if(floating_point_regex(val_two)):
        return None

    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_major_two(%s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, val_one, val_two]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name',  'Opponent', col_one, col_two])
    return df_result

'''
Function calls query_team_stats_major_op_three
'''
def call_query_team_stats_major_op_three(col_one, col_two, col_three, table_name, val_one, val_two, val_three):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MAJOR):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

     # Next check if col_three is in table_name
    if(not col_three in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check Regex for parameter val_one
    if(floating_point_regex(val_one)):
        return None

    # Check Regex for parameter val_two
    if(floating_point_regex(val_two)):
        return None

    # Check Regex for parameter val_three
    if(floating_point_regex(val_three)):
        return None

    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_major_three(%s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, val_one, val_two, val_three]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name',  'Opponent',col_one, col_two, col_three])
    return df_result

'''
Function calls query_team_stats_major_compare_one
'''
def call_query_team_stats_major_compare_one(col_one, table_name, val_one):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MAJOR):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check Regex for parameter val_one
    if(floating_point_regex(val_one)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_major_compare_one(%s, %s, %s)
    """, [col_one, table_name, val_one]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name',  'Opponent', col_one])
    return df_result

'''
Function calls query_team_stats_major_compare_two
'''
def call_query_team_stats_major_compare_two(col_one, col_two, table_name, val_one, val_two):
     # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MAJOR):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Check Regex for parameter val_one
    if(floating_point_regex(val_one)):
        return None

    # Check Regex for parameter val_one
    if(floating_point_regex(val_two)):
        return None

    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_major_compare_two(%s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, val_one, val_two]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name',  'Opponent', col_one, col_two])
    return df_result

'''
Function calls query_team_stats_major_compare_three
'''
def call_query_team_stats_major_compare_three(col_one, col_two, col_three, table_name, val_one, val_two, val_three):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MAJOR):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

     # Next check if col_three is in table_name
    if(not col_three in VALID_COL_TEAM_STATS_MAJOR[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check Regex for parameter val_one
    if(floating_point_regex(val_one)):
        return None

    # Check Regex for parameter val_two
    if(floating_point_regex(val_two)):
        return None

    # Check Regex for parameter val_three
    if(floating_point_regex(val_three)):
        return None

    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_major_compare_three(%s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, val_one, val_two, val_three]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name',  'Opponent',col_one, col_two, col_three])
    return df_result

'''
Function calls query_team_stats_primary_sid
'''
def call_query_team_stats_primary_sid(table_name, season_id, opp_bool):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MAJOR):
        print("Table Name is not valid")
        return None

    # Check season_id to regex 
    if(season_id_regex(season_id)):
        return None

    # Check opp_bool to regex
    if(binary_regex(opp_bool)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_primary_sid(%s, %s, %s)
    """, [table_name, season_id, opp_bool]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Opponent', 'Team_Name', 'Points', 'Assists', 'True_Rebounds', 'Steals', 'Blocks'])
   
'''
Function calls query_team_stats_primary_tid
'''
def call_query_team_stats_primary_tid(table_name, team_id, opp_bool):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MAJOR):
        print("Table Name is not valid")
        return None

    # Check team_id to regex 
    if(team_id_regex(team_id)):
        return None

    # Check opp_bool to regex
    if(binary_regex(opp_bool)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_primary_tid(%s, %s, %s)
    """, [table_name, team_id, opp_bool]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Opponent', 'Team_Name', 'Points', 'Assists', 'True_Rebounds', 'Steals', 'Blocks'])
   
'''
Function calls query_team_stats_primary_sid_tid
'''
def call_query_team_stats_primary_sid_tid(table_name, season_id, team_id, opp_bool):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_TEAM_STATS_MAJOR):
        print("Table Name is not valid")
        return None

    # Check season_id to regex
    if(season_id_regex(season_id)):
        return None

    # Check team_id to regex 
    if(team_id_regex(team_id)):
        return None

    # Check opp_bool to regex
    if(binary_regex(opp_bool)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_team_stats_primary_sid_tid(%s, %s, %s, %s)
    """, [table_name, season_id, team_id, opp_bool]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Opponent', 'Team_Name', 'Points', 'Assists', 'True_Rebounds', 'Steals', 'Blocks'])
   
