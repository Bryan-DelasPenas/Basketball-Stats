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
from Regular_Expression import season_id_regex, team_id_regex, team_name_regex, team_abv_regex, reg_string_regex

'''
Function call query_all_team_advanced_sid
'''
def call_query_all_team_advanced_sid(season_id):
    # Regex for season_id parameter 
    if(season_id_regex(season_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_all_team_advanced_sid(%s)
    """, [season_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Wins', 'Team_Loses', 'Win_Lose_Percentage', 'Team_Finish', 'Simple_Rating_System',
    'Pace', 'Relative_Pace', 'Offensive_Rating', 'Relative_Offensive_Rating', 'Defensive_Rating', 'Relative_Defensive_Rating', 'Playoffs_Finish', 'Coaches'])
    
    return df_result

'''
Function call query_all_team_advanced_tid
'''
def call_query_all_team_advanced_tid(team_id):
    # Regex for team_id parameter 
    if(team_id_regex(team_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_all_team_advanced_tid(%s)
    """, [team_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Wins', 'Team_Loses', 'Win_Lose_Percentage', 'Team_Finish', 'Simple_Rating_System',
    'Pace', 'Relative_Pace', 'Offensive_Rating', 'Relative_Offensive_Rating', 'Defensive_Rating', 'Relative_Defensive_Rating', 'Playoffs_Finish', 'Coaches'])
    
    return df_result

'''
Function call query_all_team_advanced_sid_tid
'''
def call_query_all_team_advanced_sid_tid(season_id, team_id):
    # Regex for season_id parameter
    if(season_id_regex(season_id)):
        return None

    # Regex for team_id parameter 
    if(team_id_regex(team_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_all_team_advanced_sid_tid(%s)
    """, [season_id, team_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Wins', 'Team_Loses', 'Win_Lose_Percentage', 'Team_Finish', 'Simple_Rating_System',
    'Pace', 'Relative_Pace', 'Offensive_Rating', 'Relative_Offensive_Rating', 'Defensive_Rating', 'Relative_Defensive_Rating', 'Playoffs_Finish', 'Coaches'])
    
    return df_result

'''
Function call query_all_team_advanced_name
'''
def call_query_all_team_advanced_name(team_name):
    # Check parameter team_name with regex
    if(team_name_regex(team_name)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Call the Query
    result = conn.execute(
    """
    CALL query_all_team_advanced_name(%s)
    """, team_name
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Wins', 'Team_Loses', 'Win_Lose_Percentage', 'Team_Finish', 'Simple_Rating_System',
    'Pace', 'Relative_Pace', 'Offensive_Rating', 'Relative_Offensive_Rating', 'Defensive_Rating', 'Relative_Defensive_Rating', 'Playoffs_Finish', 'Coaches'])
   
    return df_result

'''
Function call query_all_team_advanced_ABV
'''
def call_query_all_team_advanced_ABV(team_abv):
    # Check parameter team_abv parameter with regex
    if(team_abv_regex(team_abv)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Call the Query
    result = conn.execute(
    """
    CALL query_all_team_advanced_abv(%s)
    """, team_abv
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Wins', 'Team_Loses', 'Win_Lose_Percentage', 'Team_Finish', 'Simple_Rating_System',
    'Pace', 'Relative_Pace', 'Offensive_Rating', 'Relative_Offensive_Rating', 'Defensive_Rating', 'Relative_Defensive_Rating', 'Playoffs_Finish', 'Coaches'])
   