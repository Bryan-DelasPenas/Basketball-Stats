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
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Advanced_Reg_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Per_Minute_Production': float, 'True_Shooting_Percent': float, 'Three_Points_Attempted': float, 
        'Free_Throws_Per_Field_Goals': float, 'Offensive_Rebound_Percentage': float, 'Defensive_Rebound_Percentage': float, 'True_Rebounds_Percentage': float, 
        'Assit_Percentage': float, 'Steal_Percentage': float, 'Block_Percentage': float, 'Turn_Over_Percentage': float, 'Usage_Percentage': float, 
        'Offensive_Win_Shares': float, 'Defensive_Win_Shares': float, 'Win_Shares': float, 'Win_Shares_Fourty_Eight': float, 'Offensive_Box_Score': float, 
        'Defensive_Box_Score': float, 'Box_Plus_Minus': float, 'Value_Over_Replacement': float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_advanced_pid(%s, %s)
        """, [0, 2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)
      
    def test_query_player_career_advanced_pname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Advanced_Reg_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Per_Minute_Production': float, 'True_Shooting_Percent': float, 'Three_Points_Attempted': float, 
        'Free_Throws_Per_Field_Goals': float, 'Offensive_Rebound_Percentage': float, 'Defensive_Rebound_Percentage': float, 'True_Rebounds_Percentage': float, 
        'Assit_Percentage': float, 'Steal_Percentage': float, 'Block_Percentage': float, 'Turn_Over_Percentage': float, 'Usage_Percentage': float, 
        'Offensive_Win_Shares': float, 'Defensive_Win_Shares': float, 'Win_Shares': float, 'Win_Shares_Fourty_Eight': float, 'Offensive_Box_Score': float, 
        'Defensive_Box_Score': float, 'Box_Plus_Minus': float, 'Value_Over_Replacement': float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_advanced_pname(%s, %s)
        """, [0, "Kareem Abdul-Jabbar"]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)
      
    def test_query_player_career_advanced_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Advanced_Both_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Per_Minute_Production': float, 'True_Shooting_Percent': float, 'Three_Points_Attempted': float, 
        'Free_Throws_Per_Field_Goals': float, 'Offensive_Rebound_Percentage': float, 'Defensive_Rebound_Percentage': float, 'True_Rebounds_Percentage': float, 
        'Assit_Percentage': float, 'Steal_Percentage': float, 'Block_Percentage': float, 'Turn_Over_Percentage': float, 'Usage_Percentage': float, 
        'Offensive_Win_Shares': float, 'Defensive_Win_Shares': float, 'Win_Shares': float, 'Win_Shares_Fourty_Eight': float, 'Offensive_Box_Score': float, 
        'Defensive_Box_Score': float, 'Box_Plus_Minus': float, 'Value_Over_Replacement': float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_advanced_both_pid(%s)
        """, [2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])
        
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_query_player_career_advanced_both_pname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Advanced_Both_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Per_Minute_Production': float, 'True_Shooting_Percent': float, 'Three_Points_Attempted': float, 
        'Free_Throws_Per_Field_Goals': float, 'Offensive_Rebound_Percentage': float, 'Defensive_Rebound_Percentage': float, 'True_Rebounds_Percentage': float, 
        'Assit_Percentage': float, 'Steal_Percentage': float, 'Block_Percentage': float, 'Turn_Over_Percentage': float, 'Usage_Percentage': float, 
        'Offensive_Win_Shares': float, 'Defensive_Win_Shares': float, 'Win_Shares': float, 'Win_Shares_Fourty_Eight': float, 'Offensive_Box_Score': float, 
        'Defensive_Box_Score': float, 'Box_Plus_Minus': float, 'Value_Over_Replacement': float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_advanced_both_pname(%s)
        """, ["Kareem Abdul-Jabbar"]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'])
        
        pd.testing.assert_frame_equal(df_result, df_expected)

if __name__ == '__main__':
    unittest.main()