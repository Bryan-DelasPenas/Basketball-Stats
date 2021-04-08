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
from Regular_Expression import season_id_regex, team_id_regex, team_name_regex, team_abv_regex

'''
Function that calls query_all_team_sid
'''
def call_query_all_team_sid(season_id):
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
    CALL query_all_team_sid(%s)
    """, season_id
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
    
    # Return the dataframe
    return df_result

'''
Function that calls query_all_team_tid
'''
def call_query_all_team_tid(team_id):
    # Compare with regualar expression
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
    CALL query_all_team_tid(%s)
    """, team_id
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
    
    # Return the dataframe
    return df_result

'''
Function that calls query_all_team_name
'''
def call_query_all_team_name(team_name):
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
    CALL query_all_team_name(%s)
    """, team_name
    ).fetchall()
    
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])

    # Return the dataframe
    return df_result

'''
Function that calls query_all_team_abv
'''
def call_query_all_team_abv(team_abv):
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
    CALL query_all_team_abv(%s)
    """, team_abv
    ).fetchall()
     
    # Convert Query Result into a dataframe  
    df_result = pd.DataFrame(result, 
    columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
    
    # Return the dataframe
    return df_result

'''
Function that calls query_all_team_name
'''
def call_query_team_name(team_name):
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
    CALL query_team_name(%s)
    """, team_name
    ).fetchall()
     
    return result[0][0]

'''
Function that calls query_all_team_abv
'''
def call_query_team_abv(team_abv):
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
    CALL query_team_abv(%s)
    """, team_abv
    ).fetchall()
     
    # Return the dataframe
    return result[0][0]
