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
from Regular_Expression import player_id_regex, player_name_regrex, date_regex

'''
Function that calls query_all_player_pid
'''
def call_query_all_player_pid(player_id):
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
    CALL query_all_player_pid(%s)
    """, player_id
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Player_ID', 'Birth_Date', 'Player_Name'])

    return df_result

'''
Function that calls query_all_player_name_dob
'''
def call_query_all_player_name_dob(player_name, dob):
    
    # Compares player_name with regex
    if(player_name_regrex(player_name)):
        return None

    # Compares date with regex
    if(date_regex(dob)):
        return None
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_player_name_dob(%s, %s)
    """, [player_name, dob]
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Player_ID', 'Birth_Date', 'Player_Name'])

    return df_result

'''
Function that calls query_player_name
'''
def call_query_player_name(player_name):

    player_name_regrex(player_name)

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Execute the Query 
    result = conn.execute(
    """
    CALL query_all_player_name(%s)
    """, player_name
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Player_ID', 'Birth_Date', 'Player_Name'])

    return df_result
