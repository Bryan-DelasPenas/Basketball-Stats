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
from Query_Player_Advanced import drop_player_advanced_query, create_player_advanced_query
from Call_Query_Player_Advanced import *

class TestQueryPlayerAdvanced(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_player_advanced_query()

        # Create Procedures
        create_player_advanced_query()
    
    def test_query_all_player_advanced_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Advanced_Kareem_Abdul_Jabbar_Reg_Pid.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str, 'Per_Minute_Production' : float, 'True_Shooting_Percent':float, 'Three_Points_Attempted':float, 'Free_Throws_Per_Field_Goals':float, 
        'Offensive_Rebound_Percentage':float, 'Defensive_Rebound_Percentage':float, 'True_Rebounds_Percentage':float, 'Assit_Percentage':float, 'Steal_Percentage':float, 
        'Block_Percentage':float, 'Turn_Over_Percentage' :float, 'Usage_Percentage':float, 'Offensive_Win_Shares':float, 'Defensive_Win_Shares':float, 'Win_Shares':float, 
        'Win_Shares_Fourty_Eight':float, 'Offensive_Box_Score':float, 'Defensive_Box_Score':float, 'Box_Plus_Minus':float, 'Value_Over_Replacement':float})
       
        df_result = call_query_all_player_advanced_pid(2, 0)
        # Change Dates into strings 
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_all_player_advanced_sid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Advanced_Kareem_Abdul_Jabbar_1985_Reg.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str, 'Per_Minute_Production' : float, 'True_Shooting_Percent':float, 'Three_Points_Attempted':float, 'Free_Throws_Per_Field_Goals':float, 
        'Offensive_Rebound_Percentage':float, 'Defensive_Rebound_Percentage':float, 'True_Rebounds_Percentage':float, 'Assit_Percentage':float, 'Steal_Percentage':float, 
        'Block_Percentage':float, 'Turn_Over_Percentage' :float, 'Usage_Percentage':float, 'Offensive_Win_Shares':float, 'Defensive_Win_Shares':float, 'Win_Shares':float, 
        'Win_Shares_Fourty_Eight':float, 'Offensive_Box_Score':float, 'Defensive_Box_Score':float, 'Box_Plus_Minus':float, 'Value_Over_Replacement':float})
        
        df_result = call_query_all_player_advanced_sid_pid(1985, 2, 0)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_all_player_advanced_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Advanced_Kareem_Abdul_Jabbar_Reg_Lakers.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str, 'Per_Minute_Production' : float, 'True_Shooting_Percent':float, 'Three_Points_Attempted':float, 'Free_Throws_Per_Field_Goals':float, 
        'Offensive_Rebound_Percentage':float, 'Defensive_Rebound_Percentage':float, 'True_Rebounds_Percentage':float, 'Assit_Percentage':float, 'Steal_Percentage':float, 
        'Block_Percentage':float, 'Turn_Over_Percentage' :float, 'Usage_Percentage':float, 'Offensive_Win_Shares':float, 'Defensive_Win_Shares':float, 'Win_Shares':float, 
        'Win_Shares_Fourty_Eight':float, 'Offensive_Box_Score':float, 'Defensive_Box_Score':float, 'Box_Plus_Minus':float, 'Value_Over_Replacement':float})
      
        df_result = call_query_all_player_advanced_tid_pid(14, 2, 0)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_all_player_advanced_pname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Advanced_Kareem_Abdul_Jabbar_Reg_Pid.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str, 'Per_Minute_Production' : float, 'True_Shooting_Percent':float, 'Three_Points_Attempted':float, 'Free_Throws_Per_Field_Goals':float, 
        'Offensive_Rebound_Percentage':float, 'Defensive_Rebound_Percentage':float, 'True_Rebounds_Percentage':float, 'Assit_Percentage':float, 'Steal_Percentage':float, 
        'Block_Percentage':float, 'Turn_Over_Percentage' :float, 'Usage_Percentage':float, 'Offensive_Win_Shares':float, 'Defensive_Win_Shares':float, 'Win_Shares':float, 
        'Win_Shares_Fourty_Eight':float, 'Offensive_Box_Score':float, 'Defensive_Box_Score':float, 'Box_Plus_Minus':float, 'Value_Over_Replacement':float})
        
        df_result = call_query_all_player_advanced_pname("Kareem Abdul-Jabbar", 0)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_advanced_pname_sid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Advanced_Kareem_Abdul_Jabbar_1985_Reg.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str, 'Per_Minute_Production' : float, 'True_Shooting_Percent':float, 'Three_Points_Attempted':float, 'Free_Throws_Per_Field_Goals':float, 
        'Offensive_Rebound_Percentage':float, 'Defensive_Rebound_Percentage':float, 'True_Rebounds_Percentage':float, 'Assit_Percentage':float, 'Steal_Percentage':float, 
        'Block_Percentage':float, 'Turn_Over_Percentage' :float, 'Usage_Percentage':float, 'Offensive_Win_Shares':float, 'Defensive_Win_Shares':float, 'Win_Shares':float, 
        'Win_Shares_Fourty_Eight':float, 'Offensive_Box_Score':float, 'Defensive_Box_Score':float, 'Box_Plus_Minus':float, 'Value_Over_Replacement':float})
  
        df_result = call_query_all_player_advanced_pname_sid( "Kareem Abdul-Jabbar", 1985, 0)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_advanced_pname_tid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Advanced_Kareem_Abdul_Jabbar_Reg_Lakers.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str, 'Per_Minute_Production' : float, 'True_Shooting_Percent':float, 'Three_Points_Attempted':float, 'Free_Throws_Per_Field_Goals':float, 
        'Offensive_Rebound_Percentage':float, 'Defensive_Rebound_Percentage':float, 'True_Rebounds_Percentage':float, 'Assit_Percentage':float, 'Steal_Percentage':float, 
        'Block_Percentage':float, 'Turn_Over_Percentage' :float, 'Usage_Percentage':float, 'Offensive_Win_Shares':float, 'Defensive_Win_Shares':float, 'Win_Shares':float, 
        'Win_Shares_Fourty_Eight':float, 'Offensive_Box_Score':float, 'Defensive_Box_Score':float, 'Box_Plus_Minus':float, 'Value_Over_Replacement':float})

        df_result = call_query_all_player_advanced_pname_tid("Kareem Abdul-Jabbar", 14, 0)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_all_player_advanced_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Advanced_Kareem_Abdul_Jabbar_Both.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str, 'Per_Minute_Production' : float, 'True_Shooting_Percent':float, 'Three_Points_Attempted':float, 'Free_Throws_Per_Field_Goals':float, 
        'Offensive_Rebound_Percentage':float, 'Defensive_Rebound_Percentage':float, 'True_Rebounds_Percentage':float, 'Assit_Percentage':float, 'Steal_Percentage':float, 
        'Block_Percentage':float, 'Turn_Over_Percentage' :float, 'Usage_Percentage':float, 'Offensive_Win_Shares':float, 'Defensive_Win_Shares':float, 'Win_Shares':float, 
        'Win_Shares_Fourty_Eight':float, 'Offensive_Box_Score':float, 'Defensive_Box_Score':float, 'Box_Plus_Minus':float, 'Value_Over_Replacement':float})
        
        df_result = call_query_all_player_advanced_both_pid(2)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)


    def test_query_all_player_advanced_both_sid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Advanced_Kareem_Abdul_Jabbar_1985_Both.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str, 'Per_Minute_Production' : float, 'True_Shooting_Percent':float, 'Three_Points_Attempted':float, 'Free_Throws_Per_Field_Goals':float, 
        'Offensive_Rebound_Percentage':float, 'Defensive_Rebound_Percentage':float, 'True_Rebounds_Percentage':float, 'Assit_Percentage':float, 'Steal_Percentage':float, 
        'Block_Percentage':float, 'Turn_Over_Percentage' :float, 'Usage_Percentage':float, 'Offensive_Win_Shares':float, 'Defensive_Win_Shares':float, 'Win_Shares':float, 
        'Win_Shares_Fourty_Eight':float, 'Offensive_Box_Score':float, 'Defensive_Box_Score':float, 'Box_Plus_Minus':float, 'Value_Over_Replacement':float})
        
        df_result = call_query_all_player_advanced_both_sid_pid(1985, 2)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_advanced_both_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Advanced_Kareem_Abdul_Jabbar_Both_Lakers.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str, 'Per_Minute_Production' : float, 'True_Shooting_Percent':float, 'Three_Points_Attempted':float, 'Free_Throws_Per_Field_Goals':float, 
        'Offensive_Rebound_Percentage':float, 'Defensive_Rebound_Percentage':float, 'True_Rebounds_Percentage':float, 'Assit_Percentage':float, 'Steal_Percentage':float, 
        'Block_Percentage':float, 'Turn_Over_Percentage' :float, 'Usage_Percentage':float, 'Offensive_Win_Shares':float, 'Defensive_Win_Shares':float, 'Win_Shares':float, 
        'Win_Shares_Fourty_Eight':float, 'Offensive_Box_Score':float, 'Defensive_Box_Score':float, 'Box_Plus_Minus':float, 'Value_Over_Replacement':float})
     
        df_result = call_query_all_player_advanced_both_tid_pid(14, 2)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_query_all_player_advanced_both_pname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Advanced_Kareem_Abdul_Jabbar_Both.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str, 'Per_Minute_Production' : float, 'True_Shooting_Percent':float, 'Three_Points_Attempted':float, 'Free_Throws_Per_Field_Goals':float, 
        'Offensive_Rebound_Percentage':float, 'Defensive_Rebound_Percentage':float, 'True_Rebounds_Percentage':float, 'Assit_Percentage':float, 'Steal_Percentage':float, 
        'Block_Percentage':float, 'Turn_Over_Percentage' :float, 'Usage_Percentage':float, 'Offensive_Win_Shares':float, 'Defensive_Win_Shares':float, 'Win_Shares':float, 
        'Win_Shares_Fourty_Eight':float, 'Offensive_Box_Score':float, 'Defensive_Box_Score':float, 'Box_Plus_Minus':float, 'Value_Over_Replacement':float})
       
        df_result = call_query_all_player_advanced_both_pname("Kareem Abdul-Jabbar")
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_advanced_both_pname_sid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Advanced_Kareem_Abdul_Jabbar_1985_Both.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str, 'Per_Minute_Production' : float, 'True_Shooting_Percent':float, 'Three_Points_Attempted':float, 'Free_Throws_Per_Field_Goals':float, 
        'Offensive_Rebound_Percentage':float, 'Defensive_Rebound_Percentage':float, 'True_Rebounds_Percentage':float, 'Assit_Percentage':float, 'Steal_Percentage':float, 
        'Block_Percentage':float, 'Turn_Over_Percentage' :float, 'Usage_Percentage':float, 'Offensive_Win_Shares':float, 'Defensive_Win_Shares':float, 'Win_Shares':float, 
        'Win_Shares_Fourty_Eight':float, 'Offensive_Box_Score':float, 'Defensive_Box_Score':float, 'Box_Plus_Minus':float, 'Value_Over_Replacement':float})
        
        df_result = call_query_all_player_advanced_both_pname_sid("Kareem Abdul-Jabbar", 1985)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_advanced_both_pname_tid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Advanced_Kareem_Abdul_Jabbar_Both_Lakers.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str, 'Per_Minute_Production' : float, 'True_Shooting_Percent':float, 'Three_Points_Attempted':float, 'Free_Throws_Per_Field_Goals':float, 
        'Offensive_Rebound_Percentage':float, 'Defensive_Rebound_Percentage':float, 'True_Rebounds_Percentage':float, 'Assit_Percentage':float, 'Steal_Percentage':float, 
        'Block_Percentage':float, 'Turn_Over_Percentage' :float, 'Usage_Percentage':float, 'Offensive_Win_Shares':float, 'Defensive_Win_Shares':float, 'Win_Shares':float, 
        'Win_Shares_Fourty_Eight':float, 'Offensive_Box_Score':float, 'Defensive_Box_Score':float, 'Box_Plus_Minus':float, 'Value_Over_Replacement':float})
    
        df_result = call_query_all_player_advanced_both_pname_tid("Kareem Abdul-Jabbar",14)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)

if __name__ == '__main__':
    unittest.main()