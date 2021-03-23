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
from Regular_Expression import season_id_regex, team_id_regex, team_name_regex, team_abv_regex, games_amount_regex, percentage_regex, binary_regex
from Constants import VALID_SID_TEAM_IDS
'''
Function to call query_all_cs_sid
'''
def call_query_all_cs_sid(season_id):
    # Compare with regualar expression
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
    CALL query_all_cs_sid(%s)
    """, season_id
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
            'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])

    # Return the dataframe
    return df_result

'''
Function to call query_all_cs_tid
'''
def call_query_all_cs_tid(team_id):
    # Compare team_id with 
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
    CALL query_all_cs_tid(%s)
    """, team_id
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
            'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])

    # Return the dataframe
    return df_result

'''
Function to call query_all_cs_name
'''
def call_query_all_cs_name(team_name):
    # Compare team_name with regular expression 
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
    CALL query_all_cs_name(%s)
    """, team_name
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
            'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])

    # Return the dataframe
    return df_result

'''
Function to call query_all_cs_ABV
'''
def call_query_all_cs_ABV(team_abv):
    # Compare team_name with regular expression 
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
    CALL query_all_cs_abv(%s)
    """, team_abv
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
            'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])

    # Return the dataframe
    return df_result

'''
Function to call query_all_cs_win
'''
def call_query_all_cs_win(wins_amount):
    # Compare team_name with regular expression 
    if(games_amount_regex(wins_amount)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_cs_win(%s)
    """, wins_amount
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
            'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])

    # Return the dataframe
    return df_result

'''
Function to call query_all_cs_wl
'''
def call_query_all_cs_wl(win_percentage):
    # Compare team_name with regular expression 
    if(percentage_regex(win_percentage)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_cs_wl(%s)
    """, win_percentage
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
            'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])

    # Return the dataframe
    return df_result

'''
Function to call query_all_cs_sid_ew
'''
def call_query_all_cs_sid_ew(season_id, east_or_west):
    # Compare with regualar expression
    if(season_id_regex(season_id)):
        return None

    # Compare wit regular expresion
    if(binary_regex(east_or_west)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_cs_sid_ew(%s,%s)
    """, [season_id, east_or_west]
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
            'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])

    # Return the dataframe
    return df_result

'''
Function to call query_cs_win
'''
def call_query_cs_win(season_id, team_id):
    # Compare with regualar expression
    if(season_id_regex(season_id)):
        return None

    # Compare with regualar expression
    if(team_id_regex(team_id)):
        return None

    # Check if valid team_id from a given year
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
    CALL query_cs_win(%s, %s)
    """, [season_id, team_id]
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins'])  

    return df_result
