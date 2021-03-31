import pandas as pd
import numpy as np
import sys 
import pathlib
import os
import unittest
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts' + '\\Queries')
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts' + '\\Call_Queries')

import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine

from Helper_DB import create_connection, test_connection, check_table
from Query_Team_Advanced import create_team_advanced_query, drop_team_advanced_query
from Call_Query_Team_Advanced import *

'''
Class that will Team_Stat_Queries, Assuming that the data has been inserted correctly 
'''
class TestQueryTeamAdvanced(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_team_advanced_query()

        # Create Procedures
        create_team_advanced_query()


    def test_create_query_all_team_advanced_sid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Advanced_2020.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Simple_Rating_System' : float, 'Pace' : float, 'Relative_Pace' : float, 'Offensive_Rating' : float, 'Relative_Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Relative_Defensive_Rating' : float})

        df_result = call_query_all_team_advanced_sid(2020)
        pd.testing.assert_frame_equal(df_result, df_expected)
    

    def test_create_query_all_team_advanced_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Advanced_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Simple_Rating_System' : float, 'Pace' : float, 'Relative_Pace' : float, 'Offensive_Rating' : float, 'Relative_Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Relative_Defensive_Rating' : float})

        df_result = call_query_all_team_advanced_tid(2)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_advanced_sid_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Advanced_2020_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Simple_Rating_System' : float, 'Pace' : float, 'Relative_Pace' : float, 'Offensive_Rating' : float, 'Relative_Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Relative_Defensive_Rating' : float})

        df_result = call_query_all_team_advanced_sid_tid(2020, 2)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_advanced_name(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Advanced_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Simple_Rating_System' : float, 'Pace' : float, 'Relative_Pace' : float, 'Offensive_Rating' : float, 'Relative_Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Relative_Defensive_Rating' : float})

        df_result = call_query_all_team_advanced_name("Boston Celtics")
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_advanced_abv(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Advanced_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Simple_Rating_System' : float, 'Pace' : float, 'Relative_Pace' : float, 'Offensive_Rating' : float, 'Relative_Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Relative_Defensive_Rating' : float})

        df_result = call_query_all_team_advanced_abv('BOS')
        pd.testing.assert_frame_equal(df_result, df_expected)
    
if __name__ == '__main__':
    unittest.main()