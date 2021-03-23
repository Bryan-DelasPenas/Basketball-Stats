import pandas as pd
import numpy as np
import sys 
import pathlib
import os
import re
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts' + '\\Queries')

import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine

from Helper_DB import create_connection, test_connection, check_table
from Common_Regular_Expression import season_id_regrex, team_id_regrex

'''
Function to call query_all_cs_tid
'''
def call_query_all_cs_sid(season_id):
    
    # Compare with regualar expression
    season_id_regrex(season_id)

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
    team_id_regrex(team_id)
    
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
def call_query_all_cs_name():
    return None

def call_query_all_cs_ABV():
    return None

def call_query_all_cs_win():
    return None

def call_query_all_cs_wl():
    return None

def call_query_all_cs_sid_ew():
    return None

def call_query_cs_win():
    return None

def main():
    call_query_all_cs_tid(1)
main()