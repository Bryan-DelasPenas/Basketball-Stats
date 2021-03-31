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
from Regular_Expression import season_id_regex, team_id_regex, team_name_regex, team_abv_regex, binary_regex

'''
Function calls query_all_team_per_game_sid
'''
def call_query_all_team_per_game_sid(season_id, opp_bool):
    # Check parameter season_id with regex
    if(season_id_regex(season_id)):
        return None

    # Check opp_bool paramter with regex
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
    CALL query_all_team_per_game_sid(%s, %s)
    """, [opp_bool, season_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
    'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
    'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
    'Personal_Foul', 'Points', 'Opponent'])
    
    return df_result

'''
Function calls query_all_team_per_game_tid
'''
def call_query_all_team_per_game_tid(team_id, opp_bool):
    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check opp_bool paramter with regex
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
    CALL query_all_team_per_game_tid(%s, %s)
    """, [opp_bool, team_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
    'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
    'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
    'Personal_Foul', 'Points', 'Opponent'])
    
    return df_result

'''
Function calls query_all_team_per_game_sid_team
'''
def call_query_all_team_per_game_sid_tid(season_id, team_id, opp_bool):
    # Check parameter season_id with regex
    if(season_id_regex(season_id)):
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Check opp_bool paramter with regex
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
    CALL query_all_team_per_game_sid_tid(%s, %s, %s)
    """, [opp_bool, season_id, team_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
    'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
    'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
    'Personal_Foul', 'Points', 'Opponent'])
    
    return df_result

'''
Function calls query_all_team_per_game_name
'''
def call_query_all_team_per_game_name(team_name, opp_bool):
    # Check parameter team_name with regex
    if(team_name_regex(team_name)):
        return None

    # Check opp_bool paramter with regex
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
    CALL query_all_team_per_game_name(%s, %s)
    """, [opp_bool, team_name]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
    'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
    'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
    'Personal_Foul', 'Points', 'Opponent'])
    
    return df_result

'''
Function calls query_all_team_per_game_ABV
'''
def call_query_all_team_per_game_abv(team_abv, opp_bool):
    # Check parameter team_abv with regex
    if(team_abv_regex(team_abv)):
        return None

    # Check opp_bool paramter with regex
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
    CALL query_all_team_per_game_abv(%s, %s)
    """, [opp_bool, team_abv]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
    'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
    'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
    'Personal_Foul', 'Points', 'Opponent'])
    
    return df_result

'''
Function calls query_all_team_per_game_both_sid
'''
def call_query_all_team_per_game_both_sid(season_id):
    # Check parameter season_id with regex
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
    CALL query_all_team_per_game_both_sid(%s)
    """, [season_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
    'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
    'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
    'Personal_Foul', 'Points', 'Opponent'])
    
    return df_result

'''
Function calls query_all_team_per_game_both_tid
'''
def call_query_all_team_per_game_both_tid(team_id):
    # Check parameter team_id with regex
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
    CALL query_all_team_per_game_both_tid(%s)
    """, [team_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
    'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
    'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
    'Personal_Foul', 'Points', 'Opponent'])
    
    return df_result

'''
Function calls query_all_team_per_game_both_sid_tid
'''
def call_query_all_team_per_game_both_sid_tid(season_id, team_id):
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

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_all_team_per_game_both_sid_tid(%s, %s)
    """, [season_id, team_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
    'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
    'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
    'Personal_Foul', 'Points', 'Opponent'])
    
    return df_result

'''
Function calls query_all_team_per_game_both_name
'''
def call_query_all_team_per_game_both_name(team_name):
    # Check parameter team_name with regex
    if(team_name_regex(team_name)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_all_team_per_game_both_name(%s)
    """, [team_name]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
    'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
    'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
    'Personal_Foul', 'Points', 'Opponent'])
    
    return df_result

'''
Function calls query_all_team_per_game_both_ABV
'''
def call_query_all_team_per_game_both_abv(team_abv):
    # Check parameter team_abv with regex
    if(team_abv_regex(team_abv)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()

    # Using the year 2020
    result = conn.execute(
    """
    CALL query_all_team_per_game_both_abv(%s)
    """, [team_abv]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
    'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
    'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
    'Personal_Foul', 'Points', 'Opponent'])
    
    return df_result
