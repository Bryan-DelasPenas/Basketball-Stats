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
from Query_Player_Career_Advanced import drop_player_career_advanced_query, create_player_career_advanced_query

class TestQueryPlayerCareerAdvanced(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_player_career_advanced_query()

        # Create Procedures
        create_player_career_advanced_query()
    
    def test_query_player_career_advanced_pid(self):
    
    '''   
    def test_query_player_career_advanced_pname(self):
    
    def test_query_player_career_advanced_both_pid(self):
    
    def test_query_player_career_advanced_both_pname(self):
    '''
if __name__ == '__main__':
    unittest.main()