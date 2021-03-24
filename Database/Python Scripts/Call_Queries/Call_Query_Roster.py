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
from Regular_Expression import season_id_regex, team_id_regex, player_id_regex, team_name_regex, team_abv_regex, player_name_regrex
from Constants import PLAYER_FOR_TEAM_ID, VALID_SID_TEAM_IDS

'''
Function that calls query_all_roster_sid
'''
def call_query_all_roster_sid(season_id):
    if(season_id_regex(season_id)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_roster_sid(%s)
    """, season_id
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
            'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
    # Return the dataframe
    return df_result

'''
Function that calls query_all_roster_tid
'''
def call_query_all_roster_tid(team_id):
    
    # Check for the regular expressions
    if(team_id_regex(team_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_roster_tid(%s)
    """, team_id
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
            'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
    # Return the dataframe
    return df_result

'''
Function that calls query_all_roster_pid
'''
def call_query_all_roster_pid(player_id):
    # Check parameter with a regex function
    if(player_id_regex(player_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_roster_pid(%s)
    """, player_id
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
            'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
    # Return the dataframe
    return df_result

'''
Function that calls query_all_roster_pname
'''
def call_query_all_roster_pname(player_name):
    # Check parameter with regex  
    if(player_name_regrex(player_name)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_roster_pname(%s)
    """, player_name
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
            'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
    # Return the dataframe
    return df_result

'''
Function that calls query_all_roster_tname
'''
def call_query_all_roster_tname(team_name):
    # Check parameter with regex
    if(team_name_regex(team_name)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_roster_tname(%s)
    """, team_name
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
            'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
    # Return the dataframe
    return df_result

'''
Function that calls query_all_roster_abv
'''
def call_query_all_roster_abv(team_abv):
    # Check parameter with regex
    if(team_abv_regex(team_abv)):
        return None

      # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_roster_abv(%s)
    """, team_abv
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
            'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
    # Return the dataframe
    return df_result

'''
Function that calls query_all_roster_college
'''
def call_query_all_roster_college(college_name):
    # Check parameter with regex 
    # Use player_name as it allows for special chars
    if(player_name_regrex(college_name)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_roster_college(%s)
    """, college_name
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
            'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
    # Return the dataframe
    return df_result

'''
Function that calls query_all_roster_sid_tid
'''
def call_query_all_roster_sid_tid(season_id, team_id):
    # Check parameters with regex 
    if(season_id_regex(season_id)):
        return None

    if(team_id_regex(team_id)):
        return None

    # Check if the team exists in season
    if(not team_id in VALID_SID_TEAM_IDS[season_id]):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_roster_sid_tid(%s, %s)
    """, [season_id, team_id]
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
            'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
    # Return the dataframe
    return df_result

'''
Function that calls query_all_roster_tid_pid
'''
def call_query_all_roster_tid_pid(team_id, player_id):
    # Check parameters with regex 
    if(team_id_regex(team_id)):
        return None

    if(player_id_regex(player_id)):
        return None

    # Check if the team exists in season
    if(player_id not in PLAYER_FOR_TEAM_ID[team_id]):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_roster_tid_pid(%s, %s)
    """, [team_id, team_id]
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
            'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
    # Return the dataframe
    return df_result

'''
Function that calls query_all_roster_sid_tid_pid
'''
def call_query_all_roster_sid_tid_pid(season_id, team_id, player_id):
    # Check parameters with regex 
    if(season_id_regex(season_id)):
        return None
    
    if(team_id_regex(team_id)):
        return None

    if(player_id_regex(player_id)):
        return None

    # Check if the team exists in season
    if(not team_id in VALID_SID_TEAM_IDS[season_id]):
        return None

    # Check if the team exists in season
    if(player_id not in PLAYER_FOR_TEAM_ID[team_id]):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_roster_sid_tid_pid(%s, %s, %s)
    """, [season_id, team_id, team_id]
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
            'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
    # Return the dataframe
    return df_result