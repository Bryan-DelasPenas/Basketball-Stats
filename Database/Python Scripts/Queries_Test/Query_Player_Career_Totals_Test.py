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
from Query_Player_Career_Totals import drop_player_career_totals_query, create_player_career_totals_query
from Call_Query_Player_Career_Totals import *

class TestQueryPlayerCareerTotals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_player_career_totals_query()

        # Create Procedures
        create_player_career_totals_query()
    
    def test_query_player_career_totals_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Totals_Reg_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date': str,'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        df_result = call_query_player_career_totals_pid(2, 0)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    

    def test_query_player_career_totals_pname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Totals_Reg_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date': str, 'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        df_result = call_query_player_career_totals_pname("Kareem Abdul-Jabbar", 0)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_player_career_totals_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Totals_Both_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date': str, 'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        df_result = call_query_player_career_totals_both_pid(2)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_player_career_totals_both_pname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Totals_Both_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date': str, 'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
      
        df_result = call_query_player_career_totals_both_pname("Kareem Abdul-Jabbar")
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    

if __name__ == '__main__':
    unittest.main()