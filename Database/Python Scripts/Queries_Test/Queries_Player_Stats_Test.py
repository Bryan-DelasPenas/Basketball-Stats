import pandas as pd
import numpy as np
import sys 
import pathlib
import os
import unittest
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts' + '\\Queries')
import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine

from Helper_DB import create_connection, test_connection, check_table
from Query_Player_Stats import drop_player_stats_query, create_player_stats_query

class TestQueryPlayerTotals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_player_stats_query()

        # Create Procedures
        create_player_stats_query()
    
    def test_query_player_stats_one_pid(self):
        return None
    
    def test_query_player_stats_two_pid(self):
        return None

    def test_query_player_stats_three_pid(self):
        return None

    def test_query_player_stats_primary_pid(self): 
        return None

    def test_query_player_stats_one_above_pid(self): 
        return None

    def test_query_player_stats_two_above_pid(self):
        return None

    def test_query_player_stats_three_above_pid(self):
        return None

    def test_query_player_stats_one_tid_pid(self):
        return None

    def test_query_player_stats_two_tid_pid(self):
        return None

    def test_query_player_stats_three_tid_pid(self):
        return None

    def test_query_player_stats_primary_tid_pid(self):
        return None
    
    def test_query_player_stats_one_above_tid_pid(self):
        return None

    def test_query_player_stats_two_above_tid_pid(self):
        return None

    def test_query_player_stats_three_above_tid_pid(self):
        return None

    def test_query_player_stats_one_sid_pid(self):
        return None

    def test_query_player_stats_two_sid_pid(self):
        return None

    def test_query_player_stats_three_sid_pid(self):
        return None

    def test_query_player_stats_primary_sid_pid(self):
        return None

    def test_query_player_stats_one_above_sid_pid(self):
        return None

    def test_query_player_stats_two_above_sid_pid(self):
        return None

    def test_query_player_stats_three_above_sid_pid(self):
        return None
    
    def test_query_player_stats_one_both_pid(self):
        return None

    def test_query_player_stats_two_both_pid(self):
        return None

    def test_query_player_stats_three_both_pid(self):
        return None

    def test_query_player_stats_primary_both_pid(self):
        return None

    def test_query_player_stats_one_both_above_pid(self):
        return None

    def test_query_player_stats_two_both_above_pid(self):
        return None

    def test_query_player_stats_three_both_above_pid(self):
        return None

    def test_query_player_stats_one_both_tid_pid(self):
        return None

    def test_query_player_stats_two_both_tid_pid(self):
        return None

    def test_query_player_stats_three_both_tid_pid(self):
        return None

    def test_query_player_stats_primary_both_tid_pid(self):
        return None

    def test_query_player_stats_one_both_above_tid_pid(self):
        return None

    def test_query_player_stats_two_both_above_tid_pid(self):
        return None

    def test_query_player_stats_three_both_above_tid_pid(self):
        return None
    
    def test_query_player_stats_one_both_sid_pid(self):
        return None

    def test_query_player_stats_two_both_sid_pid(self):
        return None

    def test_query_player_stats_three_both_sid_pid(self):
        return None

    def test_query_player_stats_primary_both_sid_pid(self):
        return None

    def test_query_player_stats_one_both_above_sid_pid(self):
        return None

    def test_query_player_stats_two_both_above_sid_pid(self):
        return None

    def test_query_player_stats_three_both_above_sid_pid(self):
        return None


if __name__ == '__main__':
    unittest.main()