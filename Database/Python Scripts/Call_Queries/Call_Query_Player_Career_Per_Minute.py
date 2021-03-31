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
from Regular_Expression import player_id_regex, player_name_regrex, binary_regex

'''
Function call query_player_career_per_minute_pid
'''
def call_query_player_career_per_minute_pid(player_id, playoffs):
    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
        return None
    
    # Check paramter playoffs with regex 
    if(binary_regex(playoffs)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_career_per_minute_pid(%s, %s)
    """, [playoffs, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
    'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
    'Two_Points_Attempted', 'Two_Points_Percentage',  'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
    'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Stat_Form'])
    
    return df_result

'''
Function call query_player_career_per_minute_pname
'''
def call_query_player_career_per_minute_pname(player_name, playoffs):
    # Check parameter player_name with regex 
    if(player_name_regrex(player_name)):
        return None

    # Check parameter playoffs with regex 
    if(binary_regex(playoffs)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_career_per_minute_pname(%s, %s)
    """, [playoffs, player_name]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
    'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
    'Two_Points_Attempted', 'Two_Points_Percentage',  'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
    'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Stat_Form'])

    return df_result

'''
Function call query_player_career_per_minute_both_pid
'''
def call_query_player_career_per_minute_both_pid(player_id):
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
    CALL query_player_career_per_minute_both_pid(%s)
    """, [player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
    'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
    'Two_Points_Attempted', 'Two_Points_Percentage',  'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
    'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Stat_Form'])

    return df_result

'''
Function call query_player_career_per_minute_both_pname
'''
def call_query_player_career_per_minute_both_pname(player_name):
    # Check parameter player_name with regex
    if(player_name_regrex(player_name)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_career_per_minute_both_pname(%s)
    """, [player_name]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
    'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
    'Two_Points_Attempted', 'Two_Points_Percentage',  'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
    'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Stat_Form'])
    
    return df_result