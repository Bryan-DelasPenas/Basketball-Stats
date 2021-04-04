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
from Query_Team_Misc import create_team_misc_query, drop_team_misc_query
from Call_Query_Team_Misc import *

'''
Class that will Team_Stat_Queries, Assuming that the data has been inserted correctly 
'''
class TestQueryTeamMisc(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_team_misc_query()

        # Create Procedures
        create_team_misc_query()

    def test_create_query_all_team_misc_sid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Misc_2020.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Team_Average_Age' : float, 'Margin_Of_Victory' : float, 'Strength_Of_Schedule' : float, 'Simple_Rating_System' : float, 'Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Net_Rating' : float, 'Pace' : float, 'Three_Point_Attempt_Rate' : float, 'True_Shooting_Percentage' : float, 
        'Offensive_Rebound_Percentage' : float, 'Defensive_Rebound_Percentage' : float})

        df_result = call_query_all_team_misc_sid(2020)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_misc_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Misc_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Team_Average_Age' : float, 'Margin_Of_Victory' : float, 'Strength_Of_Schedule' : float, 'Simple_Rating_System' : float, 'Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Net_Rating' : float, 'Pace' : float, 'Three_Point_Attempt_Rate' : float, 'True_Shooting_Percentage' : float, 
        'Offensive_Rebound_Percentage' : float, 'Defensive_Rebound_Percentage' : float})

        df_result = call_query_all_team_misc_tid(2)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_misc_sid_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Misc_2020_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Team_Average_Age' : float, 'Margin_Of_Victory' : float, 'Strength_Of_Schedule' : float, 'Simple_Rating_System' : float, 'Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Net_Rating' : float, 'Pace' : float, 'Three_Point_Attempt_Rate' : float, 'True_Shooting_Percentage' : float, 
        'Offensive_Rebound_Percentage' : float, 'Defensive_Rebound_Percentage' : float})

        df_result = call_query_all_team_misc_sid_tid(2020, 2)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_misc_name(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Misc_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Team_Average_Age' : float, 'Margin_Of_Victory' : float, 'Strength_Of_Schedule' : float, 'Simple_Rating_System' : float, 'Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Net_Rating' : float, 'Pace' : float, 'Three_Point_Attempt_Rate' : float, 'True_Shooting_Percentage' : float, 
        'Offensive_Rebound_Percentage' : float, 'Defensive_Rebound_Percentage' : float})

        df_result = call_query_all_team_misc_name("Boston Celtics")
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_all_team_misc_ABV(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Misc_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Team_Average_Age' : float, 'Margin_Of_Victory' : float, 'Strength_Of_Schedule' : float, 'Simple_Rating_System' : float, 'Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Net_Rating' : float, 'Pace' : float, 'Three_Point_Attempt_Rate' : float, 'True_Shooting_Percentage' : float, 
        'Offensive_Rebound_Percentage' : float, 'Defensive_Rebound_Percentage' : float})

        df_result = call_query_all_team_misc_abv('BOS')
        pd.testing.assert_frame_equal(df_result, df_expected)
    

if __name__ == '__main__':
    unittest.main()