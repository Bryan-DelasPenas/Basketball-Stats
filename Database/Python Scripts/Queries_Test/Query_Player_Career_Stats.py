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
from Query_Player_Career_Stats import drop_player_career_stats_query, create_player_career_stats_query
from Call_Query_Player_Career_Stats import *

class TestQueryPlayerCareerStats(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_player_career_stats_query()

        # Create Procedures
        create_player_career_stats_query()

    def test_query_player_career_stats_one_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_FGM.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
         
        df_result = call_query_player_career_stats_one_pid('Field_Goals_Made', 'Player_Career_Totals', 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)
  
    
    def test_query_player_career_stats_two_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_FGM_FGA.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
        
        df_result = call_query_player_career_stats_two_pid('Field_Goals_Made', 'Field_Goals_Attempted','Player_Career_Totals', 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_career_stats_three_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_FGM_FGA_FGP.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
       
        df_result = call_query_player_career_stats_three_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Player_Career_Totals', 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_player_career_stats_primary_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_Primary_Totals.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float})
        
        df_result = call_query_player_career_stats_primary_pid('Player_Career_Totals', 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_career_stats_one_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_Both_FGM.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
  
        df_result = call_query_player_career_stats_one_both_pid('Field_Goals_Made', 'Player_Career_Totals', 2)
        pd.testing.assert_frame_equal(df_result, df_expected)
    

    def test_query_player_career_stats_two_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_Both_FGM_FGA.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
        
        df_result = call_query_player_career_stats_two_both_pid('Field_Goals_Made', 'Field_Goals_Attempted','Player_Career_Totals', 2)
        pd.testing.assert_frame_equal(df_result, df_expected)
    

    def test_query_player_career_stats_three_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_Both_FGM_FGA_FGP.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
        
        df_result =  call_query_player_career_stats_three_both_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Player_Career_Totals', 2)
        pd.testing.assert_frame_equal(df_result, df_expected)


    def test_query_player_career_stats_primary_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_Primary_Both_Totals.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float})
        
        df_result = call_query_player_career_stats_primary_both_pid('Player_Career_Totals', 2)
        pd.testing.assert_frame_equal(df_result, df_expected)

    

if __name__ == '__main__':
    unittest.main()