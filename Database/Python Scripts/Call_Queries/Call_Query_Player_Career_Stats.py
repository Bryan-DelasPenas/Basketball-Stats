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
from Regular_Expression import player_id_regex, player_name, binary_regex

'''
Function calls query_player_career_stats_one_pid
'''
def call_query_player_career_stats_one_pid(col_one, table_name, playoffs, player_id):
    return None

'''
Function calls query_player_career_stats_two_pid
'''
def call_query_player_career_stats_two_pid(col_one, col_two, table_name, playoffs, player_id):
    return None

'''
Function calls query_player_career_stats_three_pid
'''
def call_query_player_career_stats_three_pid(col_one, col_two, col_three, table_name, playoffs, player_id):
    return None

'''
Function calls query_player_career_stats_primary_pid
'''
def call_query_player_career_stats_primary_pid(player_id):
    return None

'''
Function calls query_player_career_stats_one_both_pid
'''
def call_query_player_career_stats_one_both_pid(col_one, table_name, playoffs, player_id, val_one):
    return None

'''
Function calls query_player_career_stats_two_both_pid
'''
def call_query_player_career_stats_two_both_pid(col_one, col_two, table_name, playoffs, player_id, val_one, val_two):
    return None

'''
Function calls query_player_career_stats_three_both_pid
'''
def call_query_player_career_stats_three_both_pid(col_one, col_two, col_three, table_name, playoffs, player_id, val_one, val_two, val_three):
    return None

'''
Function calls query_player_career_stats_primary_both_pid
'''
def call_query_player_career_stats_primary_both_pid(player_id):
    return None