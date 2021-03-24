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
Function calls query_team_stats_minor_one
'''
def call_query_team_stats_minor_one(col_one, table_name, val_one):
    return None
    
'''
Function calls query_team_stats_minor_two
'''
def call_query_team_stats_minor_two(col_one, col_two, table_name, val_one, val_two):
    return None

'''
Function calls query_team_stats_minor_three
'''
def call_query_team_stats_minor_three(col_one, col_two, col_three, table_name, val_one, val_two, val_three):
    return None

'''
Function calls query_team_stats_major_one
'''
def call_query_team_stats_major_one(col_one, table_name, val_one):
    return None

'''
Function calls query_team_stats_major_two
'''
def call_query_team_stats_major_two(col_one, col_two, table_name, val_one, val_two):
    return None

'''
Function calls query_team_stats_major_three
'''
def call_query_team_stats_major_three(col_one, col_two, col_three, table_name, val_one, val_two, val_three):
    return None

'''
Function calls query_team_stats_major_op_one
'''
def call_query_team_stats_major_op_one(col_one, table_name, val_one):
    return None

'''
Function calls query_team_stats_major_op_two
'''
def call_query_team_stats_major_op_two(col_one, col_two, table_name, val_one, val_two):
    return None

'''
Function calls query_team_stats_major_op_three
'''
def call_query_team_stats_major_op_three(col_one, col_two, col_three, table_name, val_one, val_two, val_three):
    return None

'''
Function calls query_team_stats_primary_sid
'''
def call_query_team_stats_primary_sid(table_name, season_id, opp_bool):
    return None

'''
Function calls query_team_stats_primary_tid
'''
def call_query_team_stats_primary_tid(table_name, team_id, opp_bool):
    return None

'''
Function calls query_team_stats_primary_sid_tid
'''
def call_query_team_stats_primary_sid_tid(table_name, season_id, team_id):
    return None

'''
Function calls query_team_stats_major_compare_one
'''
def call_query_team_stats_major_compare_one(col_one, table_name, val_one):
    return None

'''
Function calls query_team_stats_major_compare_two
'''
def call_query_team_stats_major_compare_two(col_one, col_two, table_name, val_one, val_two):
    return None
'''
Function calls query_team_stats_major_compare_three
'''
def call_query_team_stats_major_compare_three(col_one, col_two, col_three, table_name, val_one, val_two, val_three):
    return None
