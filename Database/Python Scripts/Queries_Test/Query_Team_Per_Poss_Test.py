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
from Query_Team_Per_Poss import create_team_per_poss_query, drop_team_per_poss_query
from Call_Query_Team_Per_Poss import *

'''
Class that will Team_Stat_Queries, Assuming that the data has been inserted correctly 
'''
class TestQueryTeamPerPoss(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_team_per_poss_query()

        # Create Procedures
        create_team_per_poss_query()

    def test_create_query_all_team_per_poss_sid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_2020.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})
      
        df_result = call_query_all_team_per_poss_sid(2020, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_create_query_all_team_per_poss_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})
  
        df_result = call_query_all_team_per_poss_tid(2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_per_poss_sid_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_2020_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})

        df_result = call_query_all_team_per_poss_sid_tid(2020, 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_per_poss_name(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})

        df_result = call_query_all_team_per_poss_name("Boston Celtics", 0)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_per_poss_abv(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})

        df_result = call_query_all_team_per_poss_abv('BOS', 0)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_per_poss_both_sid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_Both_2020.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})
       
        df_result = call_query_all_team_per_poss_both_sid(2020)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_per_poss_both_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_Both_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})

        df_result = call_query_all_team_per_poss_both_tid(2)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_per_poss_both_sid_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_Both_2020_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})

        df_result = call_query_all_team_per_poss_both_sid_tid(2020, 2)
        pd.testing.assert_frame_equal(df_result, df_expected)
    

    def test_create_query_all_team_per_poss_both_name(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_Both_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})
       
        df_result = call_query_all_team_per_poss_both_name("Boston Celtics")
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_team_per_poss_both_abv(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_Both_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})
        
        df_result = call_query_all_team_per_poss_both_abv("BOS")
        pd.testing.assert_frame_equal(df_result, df_expected)
if __name__ == '__main__':
    unittest.main()