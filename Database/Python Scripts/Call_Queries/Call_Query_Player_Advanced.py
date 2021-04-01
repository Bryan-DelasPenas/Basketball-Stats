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
from Regular_Expression import player_id_regex, team_id_regex, season_id_regex, player_name_regex, binary_regex

'''
Function call query_all_player_advanced_pid
'''
def call_query_all_player_advanced_pid(player_id, playoffs):
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
    CALL query_all_player_advanced_pid(%s, %s)
    """, [playoffs, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_all_player_advanced_sid_pid
'''
def call_query_all_player_advanced_sid_pid(season_id, player_id, playoffs):
    # Check parameter season_id with regex
    if(season_id_regex(season_id)):
        return None

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
    CALL query_all_player_advanced_sid_pid(%s, %s, %s)
    """, [playoffs, season_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_all_player_advanced_tid_pid
'''
def call_query_all_player_advanced_tid_pid(team_id, player_id, playoffs):
    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

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
    CALL query_all_player_advanced_tid_pid(%s, %s, %s)
    """, [playoffs, team_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_all_player_advanced_pname
'''
def call_query_all_player_advanced_pname(player_name, playoffs):
    # Check parameter player_name
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
    CALL query_all_player_advanced_pname(%s, %s)
    """, [playoffs, player_name]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_all_player_advanced_pname_sid
'''
def call_query_all_player_advanced_pname_sid(player_name, season_id, playoffs):
    # Check parameter player_name
    if(player_name_regex(player_name)):
        return None

    # Check parameter season_id with regex
    if(season_id_regex(season_id)):
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
    CALL query_all_player_advanced_pname_sid(%s, %s, %s)
    """, [playoffs, player_name, season_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_all_player_advanced_pname_tid
'''
def call_query_all_player_advanced_pname_tid(player_name, team_id, playoffs):
    # Check parameter player_name
    if(player_name_regex(player_name)):
        return None

    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
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
    CALL query_all_player_advanced_pname_tid(%s, %s, %s)
    """, [playoffs, player_name, team_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_all_player_advanced_both_pid
'''
def call_query_all_player_advanced_both_pid(player_id):
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
    CALL query_all_player_advanced_both_pid(%s)
    """, [player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_all_player_advanced_both_sid_pid
'''
def call_query_all_player_advanced_both_sid_pid(season_id, player_id):
    # Check parameter season_id with regex
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
    CALL query_all_player_advanced_both_sid_pid(%s, %s)
    """, [season_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_all_player_advanced_both_tid_pid
'''
def call_query_all_player_advanced_both_tid_pid(team_id, player_id):
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
    CALL query_all_player_advanced_both_tid_pid(%s, %s)
    """, [team_id, player_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_all_player_advanced_both_pname
'''
def call_query_all_player_advanced_both_pname(player_name):
    # Check parameter player_name
    if(player_name_regex(player_name)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_all_player_advanced_both_pname(%s)
    """, [player_name]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_all_player_advanced_both_pname_sid
'''
def call_query_all_player_advanced_both_pname_sid(player_name, season_id):
    # Check parameter player_name
    if(player_name_regex(player_name)):
        return None
    
    # Check parameter season_id with regex
    if(season_id_regex(season_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_all_player_advanced_both_pname_sid(%s, %s)
    """, [player_name, season_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result

'''
Function call query_all_player_advanced_both_pname_tid
'''
def call_query_all_player_advanced_both_pname_tid(player_name, team_id):
    # Check parameter player_name
    if(player_name_regex(player_name)):
        return None
    
    # Check parameter team_id with regex
    if(team_id_regex(team_id)):
        return None

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    result = conn.execute(
    """
    CALL query_all_player_advanced_both_pname_tid(%s, %s)
    """, [player_name, team_id]
    ).fetchall()
    
    df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])

    return df_result