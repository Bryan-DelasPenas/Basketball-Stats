import pandas as pd
import numpy as np
import sys 
import pathlib
import os
import unittest
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts' + '\\Queries')

import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine

from Helper_DB import create_connection, test_connection, check_table
from Regular_Expression import season_id_regex, team_id_regex, team_name_regex, team_abv_regex, reg_string_regex

'''
Function call query_all_team_misc_sid
'''
def call_query_all_team_misc_sid(season_id):
    # Check parameter season_id with regex
    if(season_id_regex(season_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Call Query
    result = conn.execute(
    """
    CALL query_all_team_misc_sid(%s)
    """, season_id
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Average_Age', 'Team_Wins', 'Team_Loses', 'Pythagorean_Wins', 'Pythagorean_Loses', 
    'Margin_Of_Victory', 'Strength_Of_Schedule', 'Simple_Rating_System', 'Offensive_Rating', 'Defensive_Rating', 'Net_Rating', 'Pace', 'Free_Throw_Attempt_Rate', 
    'Three_Point_Attempt_Rate', 'True_Shooting_Percentage', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 'Arena', 'Attend', 'Attend_Per_Game'])
   
    return df_result

'''
Function call query_all_team_misc_tid
'''
def call_query_all_team_misc_tid(team_id):
    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Call Query
    result = conn.execute(
    """
    CALL query_all_team_misc_tid(%s)
    """, team_id
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Average_Age', 'Team_Wins', 'Team_Loses', 'Pythagorean_Wins', 'Pythagorean_Loses', 
    'Margin_Of_Victory', 'Strength_Of_Schedule', 'Simple_Rating_System', 'Offensive_Rating', 'Defensive_Rating', 'Net_Rating', 'Pace', 'Free_Throw_Attempt_Rate', 
    'Three_Point_Attempt_Rate', 'True_Shooting_Percentage', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 'Arena', 'Attend', 'Attend_Per_Game'])
    
    return df_result

'''
Function call query_all_team_misc_sid_tid
'''
def call_query_all_team_misc_sid_tid(season_id, team_id):
    # Check parameter season_id with regex
    if(season_id_regex(season_id)):
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Call Query
    result = conn.execute(
    """
    CALL query_all_team_misc_sid_tid(%s, %s)
    """, [season_id, team_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Average_Age', 'Team_Wins', 'Team_Loses', 'Pythagorean_Wins', 'Pythagorean_Loses', 
    'Margin_Of_Victory', 'Strength_Of_Schedule', 'Simple_Rating_System', 'Offensive_Rating', 'Defensive_Rating', 'Net_Rating', 'Pace', 'Free_Throw_Attempt_Rate', 
    'Three_Point_Attempt_Rate', 'True_Shooting_Percentage', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 'Arena', 'Attend', 'Attend_Per_Game'])
    
    return df_result

'''
Function call query_all_team_misc_name
'''
def call_query_all_team_misc_name(team_name):
    # Check team_name parameter with regex
    if(team_name_regex(team_name)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Call Query
    result = conn.execute(
    """
    CALL query_all_team_misc_name(%s)
    """, team_name
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Average_Age', 'Team_Wins', 'Team_Loses', 'Pythagorean_Wins', 'Pythagorean_Loses', 
    'Margin_Of_Victory', 'Strength_Of_Schedule', 'Simple_Rating_System', 'Offensive_Rating', 'Defensive_Rating', 'Net_Rating', 'Pace', 'Free_Throw_Attempt_Rate', 
    'Three_Point_Attempt_Rate', 'True_Shooting_Percentage', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 'Arena', 'Attend', 'Attend_Per_Game'])
   
    return df_result

'''
Function call query_all_team_misc_ABV
'''
def call_query_all_team_misc_abv(team_abv):
    # Check team_abv parameter with regex
    if(team_abv_regex(team_abv)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Call Query
    result = conn.execute(
    """
    CALL query_all_team_misc_abv(%s)
    """, team_abv
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Average_Age', 'Team_Wins', 'Team_Loses', 'Pythagorean_Wins', 'Pythagorean_Loses', 
    'Margin_Of_Victory', 'Strength_Of_Schedule', 'Simple_Rating_System', 'Offensive_Rating', 'Defensive_Rating', 'Net_Rating', 'Pace', 'Free_Throw_Attempt_Rate', 
    'Three_Point_Attempt_Rate', 'True_Shooting_Percentage', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 'Arena', 'Attend', 'Attend_Per_Game'])
   
    return df_result
