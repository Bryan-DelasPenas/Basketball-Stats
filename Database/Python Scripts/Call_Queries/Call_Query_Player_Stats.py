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
from Regular_Expression import player_id_regex, binary_regex, floating_point_regex
from Constants import VALID_TABLE_PLAYER_CAREER_STATS, VALID_COL_PLAYER_CAREER_STATS, VALID_TABLE_PRIMARY_PLAYER_CAREER_STATS

'''
Function calls query_player_stats_one_pid
'''
def call_query_player_stats_one_pid(col_one, table_name, playoffs, player_id):
    return None

'''
Function calls query_player_stats_two_pid
'''
def call_query_player_stats_two_pid(col_one, col_two, table_name, playoffs, player_id):
    return None

'''
Function calls query_player_stats_three_pid
'''
def call_query_player_stats_three_pid(col_one, col_two, col_three, table_name, playoffs, player_id):
    return None

'''
Function calls query_player_stats_primary_pid
'''
def call_query_player_stats_primary_pid(table_name, playoffs, player_id): 
    return None 

'''
Function calls query_player_stats_one_above_pid
'''
def call_query_player_stats_one_above_pid(col_one, table_name, playoffs, player_id, val_one):
    return None

'''
Function calls query_player_stats_two_above_pid
'''
def call_query_player_stats_two_above_pid(col_one, col_two, table_name, playoffs, player_id, val_one, val_two):
    return None

'''
Function calls query_player_Stats_three_above_pid
'''
def call_query_player_stats_three_above_pid(col_one, col_two, col_three, table_name, playoffs, val_one, val_two, val_three):
    return None

'''
Function calls query_player_stats_one_tid_pid
'''
def call_query_player_stats_one_tid_pid(col_one, table_name, playoffs, team_id, player_id):
    return None

'''
Function calls query_player_stats_two_tid_pid
'''
def call_query_player_stats_two_tid_pid(col_one, col_two, table_name, playoffs, team_id, player_id):
    return None

'''
Function calls query_player_stats_three_tid_pid
'''
def call_query_player_stats_three_tid_pid(col_one, col_two, col_three, table_name, playoffs, team_id, player_id):
    return None 

'''
Function calls query_player_stats_primary_tid_pid
'''
def call_query_player_stats_primary_tid_pid(table_name, playoffs, team_id, player_id):
    return None

'''
Function calls query_player_stats_one_above_tid_pid
'''
def call_query_player_stats_one_above_tid_pid(col_one, table_name, playoffs, team_id, player_id, val_one):
    return None

'''
Function calls query_player_stats_two_above_tid_pid
'''
def call_query_player_stats_two_above_tid_pid(col_one, col_two, table_name, playoffs, team_id, player_id, val_one, val_two):
    return None

'''
Function calls query_player_stats_three_above_tid_pid
'''
def call_query_player_stats_three_above_tid_pid(col_one, col_two, col_three, table_name, playoffs, team_id, player_id, val_one, val_two, val_three):
    return None

'''
Function calls query_player_ststs_one_sid_pid
'''
def call_query_player_stats_one_sid_pid(col_one, table_name, playoffs, sesaon_id, player_id):
    return None

'''
Function calls query_player_stats_two_sid_pid 
'''
def call_query_player_stats_two_sid_pid(col_one, col_two, table_name, playoffs, sesaon_id):
    return None

'''
Function calls query_player_stats_three_sid_pid
'''
def call_query_player_stats_three_sid_pid(): 
    return None 

'''
Function calls query_stats_primary_sid_pid
'''
def call_query_player_stats_primary_sid_pid(table_name, season_id, player_id):
    return None

'''
Function calls query_stats_one_above_sid_pid
'''
def call_query_player_stats_one_above_sid_pid(col_one, table_name, season_id, player_id, val_one):
    return None

'''
Function calls query_stats_two_above_sid_pid
'''
def call_query_player_stats_two_above_sid_pid(col_one, col_two, table_name, season_id, player_id, val_one, val_two):
    return None

'''
Function calls query_stats_three_above_sid_pid
'''
def call_query_player_stats_three_above_sid_pid(col_one, col_two, col_three, table_name, season_id, player_id, val_one, val_two, val_three):
    return None

'''
Function calls query_stats_one_both_pid
'''
def call_query_player_stats_one_both_pid(col_one, table_name, player_id):
    return None

'''
Function calls query_stats_two_both_pid
'''
def call_query_player_stats_two_both_pid(col_one, col_two, table_name, player_id):
    return None
    
'''
Function calls query_stats_three_both_pid 
'''
def call_query_player_stats_three_both_pid(col_one, col_two, col_three, table_name, player_id): 
    return None

'''
Function calls query_stats_primary_both_pid
'''
def call_query_player_stats_primary_both_pid(table_name, player_id):
    return None

'''
Function calls query_player_stats_one_both_above_pid
'''
def call_query_player_stats_one_both_above_pid(col_one, table_name, player_id, val_one):
    return None

'''
Function calls query_player_stats_two_both_above_pid
'''
def call_query_player_stats_two_both_above_pid(col_one, col_two, table_name, player_id, val_one, val_two):
    return None

'''
Function calls query_player_stats_three_both_above_pid
'''
def call_query_player_stats_three_both_above_pid(col_one, col_two, col_three, table_name, player_id, val_one, val_two, val_three):
    return None
    
'''
Function calls query_player_stats_one_both_tid_pid
'''
def call_query_player_stats_one_both_tid_pid(col_one, table_name, team_id, player_id):
    return None

'''
Function calls query_player_stats_two_both_tid_pid
'''
def call_query_player_stats_two_both_tid_pid(col_one, col_two, table_name, team_id, player_id):
    return None

'''
Function calls query_player_stats_three_both_tid_pid
'''
def call_query_player_stats_three_both_tid_pid(col_one, col_two, col_three, table_name, team_id, player_id):
    return None

'''
Function calls query_player_stats_primary_both_tid_pid
'''
def call_query_player_stats_primary_both_tid_pid(table_name, player_id):
    return None

'''
Function calls query_player_stats_one_both_above_tid_pid
'''
def call_query_player_stats_one_both_above_tid_pid(col_one, table_name, team_id, player_id, val_one):
    return None

'''
Function calls _query_player_stats_two_both_above_tid_pid
'''
def call_query_player_stats_two_both_above_tid_pid(col_one, col_two, table_name, team_id, player_id, val_one, val_two):
    return None

''' 
Function calls query_player_stats_three_both_above_tid_pid(
'''
def call_query_player_stats_three_both_above_tid_pid(col_one, col_two, col_three, table_name, team_id, player_id, val_one, val_two, val_three):
    return None
    
'''
Function calls query_player_stats_one_both_sid_pid
'''
def call_query_player_stats_one_both_sid_pid(col_one, table_name, season_id, player_id):
    return None
    
'''
Function calls query_player_stats_two_both_sid_pid
'''
def call_query_player_stats_two_both_sid_pid(col_one, col_two, table_name, season_id, player_id):
    return None

'''
Function calls query_player_stats_three_both_sid_pid
'''
def call_query_player_stats_three_both_sid_pid(col_one, col_two, col_three, table_name, season_id, player_id):
    return None

'''
Function calls query_player_stats_primary_both_sid_pid
'''
def call_query_player_stats_primary_both_sid_pid(table_name, season_id, player_id):
    return None

'''
Function calls uery_player_stats_one_both_above_sid_pid(
'''
def call_query_player_stats_one_both_above_sid_pid(col_one, table_name, season_id, player_id, val_one):
    return None

'''
Function calls query_player_stats_two_both_above_sid_pid
'''
def call_query_player_stats_two_both_above_sid_pid(col_one, col_two, table_name, season_id, player_id, val_one, val_two):
    return None

'''
Function calls query_player_stats_three_both_above_sid_pid
'''
def call_query_player_stats_three_both_above_sid_pid(col_one, col_two, col_three, table_name, season_id, player_id, val_one, val_two, val_three):
    return None