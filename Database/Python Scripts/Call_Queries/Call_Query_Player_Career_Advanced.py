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
from Regular_Expression import player_id_regex, player_name_regex, binary_regex

'''
Function call query_player_career_advanced_pid
'''
def call_query_all_player_career_advanced_pid(player_id, playoffs):
    # Check parameter player_id with regex
    if(player_id_regex(player_id)):
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
    CALL query_player_career_advanced_pid(%s, %s)
    """, [playoffs, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
    'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
    'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
    'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_player_career_advanced_pname
'''
def call_query_all_player_career_advanced_pname(player_name, playoffs):
    # Check parameter player_name with regex 
    if(player_name_regex(player_name)):
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
    CALL query_player_career_advanced_pname(%s, %s)
    """, [playoffs, player_name]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
    'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
    'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
    'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_player_career_advanced_both_pid
'''
def call_query_all_player_career_advanced_both_pid(player_id):
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
    CALL query_player_career_advanced_both_pid(%s)
    """, [player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
    'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
    'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
    'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])
    return df_result

'''
Function call query_player_career_advanced_both_pname
'''
def call_query_all_player_career_advanced_both_pname(player_name):
    # Check parameter player_name with regex
    if(player_name_regex(player_name)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_player_career_advanced_both_pname(%s)
    """, [player_name]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
    'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
    'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
    'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result