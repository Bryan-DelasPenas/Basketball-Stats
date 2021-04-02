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
from Regular_Expression import player_id_regex, team_id_regex, season_id_regex, binary_regex, floating_point_regex
from Constants import VALID_TABLE_PLAYER_STATS, VALID_COL_PLAYER_STATS, VALID_TABLE_PRIMARY_PLAYER_STATS

'''
Function calls query_player_stats_one_pid
'''
def call_query_player_stats_one_pid(col_one, table_name, player_id, playoffs):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_one_pid(%s, %s, %s, %s)
    """, [col_one, table_name, playoffs, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one])

    return df_result

'''
Function calls query_player_stats_two_pid
'''
def call_query_player_stats_two_pid(col_one, col_two, table_name, player_id, playoffs):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_two_pid(%s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, playoffs, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two])

    return df_result

'''
Function calls query_player_stats_three_pid
'''
def call_query_player_stats_three_pid(col_one, col_two, col_three, table_name, player_id, playoffs):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_three in VALID_COL_PLAYER_STATS[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_three_pid(%s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, playoffs, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two, col_three])

    return df_result

'''
Function calls query_player_stats_primary_pid
'''
def call_query_player_stats_primary_pid(table_name, player_id, playoffs): 
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PRIMARY_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_primary_pid(%s, %s, %s)
    """, [table_name, playoffs, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', 'Points', 'Assists', 'True_Rebounds', 'Steals', 'Blocks'])

    return df_result
    
'''
Function calls query_player_stats_one_above_pid
'''
def call_query_player_stats_one_above_pid(col_one, table_name, player_id, playoffs, val_one):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Check parameter val_one with regex
    if(floating_point_regex(val_one)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_one_above_pid(%s, %s, %s, %s, %s)
    """, [col_one, table_name, playoffs, player_id, val_one]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one])

    return df_result

'''
Function calls query_player_stats_two_above_pid
'''
def call_query_player_stats_two_above_pid(col_one, col_two, table_name, player_id, playoffs, val_one, val_two):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None
    
    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Check parameter val_one with regex
    if(floating_point_regex(val_one)):
        return None

    # Check parameter val_two with regex
    if(floating_point_regex(val_two)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_two_above_pid(%s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, playoffs, player_id, val_one, val_two]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two])

    return df_result

'''
Function calls query_player_Stats_three_above_pid
'''
def call_query_player_stats_three_above_pid(col_one, col_two, col_three, table_name, player_id, playoffs, val_one, val_two, val_three):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_three in VALID_COL_PLAYER_STATS[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Check parameter val_one with regex
    if(floating_point_regex(val_one)):
        return None

    # Check parameter val_two with regex
    if(floating_point_regex(val_two)):
        return None

    # Check parameter val_three with regex
    if(floating_point_regex(val_three)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_three_above_pid(%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, playoffs, player_id, val_one, val_two, val_three]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two, col_three])

    return df_result

'''
Function calls query_player_stats_one_tid_pid
'''
def call_query_player_stats_one_tid_pid(col_one, table_name, team_id, player_id, playoffs):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_one_tid_pid(%s, %s, %s, %s, %s)
    """, [col_one, table_name, playoffs, team_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one])

    return df_result

'''
Function calls query_player_stats_two_tid_pid
'''
def call_query_player_stats_two_tid_pid(col_one, col_two, table_name, team_id, player_id, playoffs):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_two_tid_pid(%s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, playoffs, team_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two])

    return df_result

'''
Function calls query_player_stats_three_tid_pid
'''
def call_query_player_stats_three_tid_pid(col_one, col_two, col_three, table_name, team_id, player_id, playoffs):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_three in VALID_COL_PLAYER_STATS[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_three_tid_pid(%s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, playoffs, team_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two, col_three])

    return df_result

'''
Function calls query_player_stats_primary_tid_pid
'''
def call_query_player_stats_primary_tid_pid(table_name, team_id, player_id, playoffs):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PRIMARY_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_primary_tid_pid(%s, %s, %s, %s)
    """, [table_name, playoffs, team_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', 'Points', 'Assists', 'True_Rebounds', 'Steals', 'Blocks'])

    return df_result

'''
Function calls query_player_stats_one_above_tid_pid
'''
def call_query_player_stats_one_above_tid_pid(col_one, table_name, team_id, player_id, playoffs, val_one):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Check parameter val_one with regex
    if(floating_point_regex(val_one)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_one_above_tid_pid(%s, %s, %s, %s, %s, %s)
    """, [col_one, table_name, playoffs, team_id, player_id, val_one]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one])

    return df_result

'''
Function calls query_player_stats_two_above_tid_pid
'''
def call_query_player_stats_two_above_tid_pid(col_one, col_two, table_name, team_id, player_id, playoffs, val_one, val_two):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Check parameter val_one with regex
    if(floating_point_regex(val_one)):
        return None

    # Check parameter val_two with regex
    if(floating_point_regex(val_two)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_two_above_tid_pid(%s, %s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, playoffs, team_id, player_id, val_one, val_two]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two])

    return df_result

'''
Function calls query_player_stats_three_above_tid_pid
'''
def call_query_player_stats_three_above_tid_pid(col_one, col_two, col_three, table_name, team_id, player_id, playoffs, val_one, val_two, val_three):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_three in VALID_COL_PLAYER_STATS[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Check parameter val_one with regex
    if(floating_point_regex(val_one)):
        return None

    # Check parameter val_two with regex
    if(floating_point_regex(val_two)):
        return None

    # Check parameter val_three with regex
    if(floating_point_regex(val_three)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_three_above_tid_pid(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, playoffs, team_id, player_id, val_one, val_two, val_three]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two, col_three])

    return df_result

'''
Function calls query_player_ststs_one_sid_pid
'''
def call_query_player_stats_one_sid_pid(col_one, table_name, season_id, player_id, playoffs):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter team_id with regex
    if(season_id_regex(season_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_one_sid_pid(%s, %s, %s, %s, %s)
    """, [col_one, table_name, playoffs, season_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one])

    return df_result

'''
Function calls query_player_stats_two_sid_pid 
'''
def call_query_player_stats_two_sid_pid(col_one, col_two, table_name, season_id, player_id, playoffs):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter team_id with regex
    if(season_id_regex(season_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_two_sid_pid(%s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, playoffs, season_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two])

    return df_result

'''
Function calls query_player_stats_three_sid_pid
'''
def call_query_player_stats_three_sid_pid(col_one, col_two, col_three, table_name, season_id, player_id, playoffs): 
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_three in VALID_COL_PLAYER_STATS[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter team_id with regex
    if(season_id_regex(season_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_three_sid_pid(%s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, playoffs, season_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two, col_three])

    return df_result

'''
Function calls query_stats_primary_sid_pid
'''
def call_query_player_stats_primary_sid_pid(table_name, season_id, player_id, playoffs):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PRIMARY_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Check parameter playoffs regex
    if(binary_regex(playoffs)):
        return None

    # Check parameter team_id with regex
    if(season_id_regex(season_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_primary_sid_pid(%s, %s, %s, %s)
    """, [table_name, playoffs, season_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', 'Points', 'Assists', 'True_Rebounds', 'Steals', 'Blocks'])

    return df_result

'''
Function calls query_stats_one_both_pid
'''
def call_query_player_stats_one_both_pid(col_one, table_name, player_id):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_one_both_pid(%s, %s, %s)
    """, [col_one, table_name, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', col_one])

    return df_result

'''
Function calls query_stats_two_both_pid
'''
def call_query_player_stats_two_both_pid(col_one, col_two, table_name, player_id):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_two_both_pid(%s, %s, %s, %s)
    """, [col_one, col_two, table_name, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', col_one, col_two])

    return df_result

'''
Function calls query_stats_three_both_pid 
'''
def call_query_player_stats_three_both_pid(col_one, col_two, col_three, table_name, player_id): 
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_three in VALID_COL_PLAYER_STATS[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_three_both_pid(%s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', col_one, col_two, col_three])

    return df_result

'''
Function calls query_stats_primary_both_pid
'''
def call_query_player_stats_primary_both_pid(table_name, player_id):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PRIMARY_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_primary_both_pid(%s, %s)
    """, [table_name, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', 'Points', 'Assists', 'True_Rebounds', 'Steals', 'Blocks'])

    return df_result

'''
Function calls query_player_stats_one_both_above_pid
'''
def call_query_player_stats_one_both_above_pid(col_one, table_name, player_id, val_one):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Check parameter val_one with regex
    if(floating_point_regex(val_one)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_one_both_above_pid(%s, %s, %s, %s)
    """, [col_one, table_name, player_id, val_one]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one])

    return df_result

'''
Function calls query_player_stats_two_both_above_pid
'''
def call_query_player_stats_two_both_above_pid(col_one, col_two, table_name, player_id, val_one, val_two):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None
    
    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Check parameter val_one with regex
    if(floating_point_regex(val_one)):
        return None

    # Check parameter val_two with regex
    if(floating_point_regex(val_two)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_two_both_above_pid(%s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, player_id, val_one, val_two]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two])

    return df_result

'''
Function calls query_player_stats_three_both_above_pid
'''
def call_query_player_stats_three_both_above_pid(col_one, col_two, col_three, table_name, player_id, val_one, val_two, val_three):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_three in VALID_COL_PLAYER_STATS[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Check parameter val_one with regex
    if(floating_point_regex(val_one)):
        return None

    # Check parameter val_two with regex
    if(floating_point_regex(val_two)):
        return None

    # Check parameter val_three with regex
    if(floating_point_regex(val_three)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_three_both_above_pid(%s, %s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, player_id, val_one, val_two, val_three]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two, col_three])

    return df_result

'''
Function calls query_player_stats_one_both_tid_pid
'''
def call_query_player_stats_one_both_tid_pid(col_one, table_name, team_id, player_id):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_one_both_tid_pid(%s, %s, %s, %s)
    """, [col_one, table_name, team_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one])

    return df_result

'''
Function calls query_player_stats_two_both_tid_pid
'''
def call_query_player_stats_two_both_tid_pid(col_one, col_two, table_name, team_id, player_id):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_two_both_tid_pid(%s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, team_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two])

    return df_result

'''
Function calls query_player_stats_three_both_tid_pid
'''
def call_query_player_stats_three_both_tid_pid(col_one, col_two, col_three, table_name, team_id, player_id):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_three in VALID_COL_PLAYER_STATS[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_three_both_tid_pid(%s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, team_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two, col_three])

    return df_result

'''
Function calls query_player_stats_primary_both_tid_pid
'''
def call_query_player_stats_primary_both_tid_pid(table_name, team_id, player_id):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PRIMARY_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_primary_both_tid_pid(%s, %s, %s)
    """, [table_name, team_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', 'Points', 'Assists', 'True_Rebounds', 'Steals', 'Blocks'])

    return df_result

'''
Function calls query_player_stats_one_both_above_tid_pid
'''
def call_query_player_stats_one_both_above_tid_pid(col_one, table_name, team_id, player_id, val_one):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Check parameter val_one with regex
    if(floating_point_regex(val_one)):
        return None

     # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_one_both_above_tid_pid(%s, %s, %s, %s, %s)
    """, [col_one, table_name, team_id, player_id, val_one]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one])

    return df_result

'''
Function calls _query_player_stats_two_both_above_tid_pid
'''
def call_query_player_stats_two_both_above_tid_pid(col_one, col_two, table_name, team_id, player_id, val_one, val_two):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Check parameter val_one with regex
    if(floating_point_regex(val_one)):
        return None

    # Check parameter val_two with regex
    if(floating_point_regex(val_two)):
        return None

     # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_two_both_above_tid_pid(%s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, team_id, player_id, val_one, val_two]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two])

    return df_result

''' 
Function calls query_player_stats_three_both_above_tid_pid(
'''
def call_query_player_stats_three_both_above_tid_pid(col_one, col_two, col_three, table_name, team_id, player_id, val_one, val_two, val_three):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Next check if col_one is in table_name
    if(not col_three in VALID_COL_PLAYER_STATS[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Check parameter val_one with regex
    if(floating_point_regex(val_one)):
        return None

    # Check parameter val_two with regex
    if(floating_point_regex(val_two)):
        return None

    # Check parameter val_three with regex
    if(floating_point_regex(val_three)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_three_both_above_tid_pid(%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, team_id, player_id, val_one, val_two, val_three]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two, col_three])

    return df_result

'''
Function calls query_player_stats_one_both_sid_pid
'''
def call_query_player_stats_one_both_sid_pid(col_one, table_name, season_id, player_id):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Check parameter team_id with regex
    if(season_id_regex(season_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_three_both_sid_pid(%s, %s, %s, %s)
    """, [col_one, table_name, season_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one])

    return df_result

'''
Function calls query_player_stats_two_both_sid_pid
'''
def call_query_player_stats_two_both_sid_pid(col_one, col_two, table_name, season_id, player_id):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Check parameter team_id with regex
    if(season_id_regex(season_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_two_both_sid_pid(%s, %s, %s, %s, %s)
    """, [col_one, col_two, table_name, season_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two])

    return df_result

'''
Function calls query_player_stats_three_both_sid_pid
'''
def call_query_player_stats_three_both_sid_pid(col_one, col_two, col_three, table_name, season_id, player_id):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Next check if col_one is in table_name
    if(not col_one in VALID_COL_PLAYER_STATS[table_name]):
        print(col_one + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_two in VALID_COL_PLAYER_STATS[table_name]):
        print(col_two + " is not in table " + table_name)
        return None

    # Next check if col_two is in table_name
    if(not col_three in VALID_COL_PLAYER_STATS[table_name]):
        print(col_three + " is not in table " + table_name)
        return None

    # Check parameter team_id with regex
    if(season_id_regex(season_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_three_both_sid_pid(%s, %s, %s, %s, %s, %s)
    """, [col_one, col_two, col_three, table_name, season_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', col_one, col_two, col_three])

    return df_result

'''
Function calls query_player_stats_primary_both_sid_pid
'''
def call_query_player_stats_primary_both_sid_pid(table_name, season_id, player_id):
    # First Check if the table is valid     
    # Check if table_name is a valid parameter
    if(not table_name in VALID_TABLE_PRIMARY_PLAYER_STATS):
        print("Table Name is not valid")
        return None

    # Check parameter team_id with regex
    if(season_id_regex(season_id)):
        return None

    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None 

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_stats_primary_both_sid_pid(%s, %s, %s)
    """, [table_name, season_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID','Player_ID', 'Player_Name', 'Stat_Form', 'Points', 'Assists', 'True_Rebounds', 'Steals', 'Blocks'])

    return df_result

