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
from Query_Player_Career_Per_Minute import drop_player_career_per_minute_query, create_player_career_per_minute_query

class TestQueryPlayerCareerPerMinute(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_player_career_per_minute_query()

        # Create Procedures
        create_player_career_per_minute_query()
    
    def test_query_player_career_per_minute_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Per_Minute_Reg_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_per_minute_pid(%s, %s)
        """, [0, 2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage',  'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)
      
    def test_query_player_career_per_minute_pname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Per_Minute_Reg_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
         'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_per_minute_pname(%s, %s)
        """, [0, "Kareem Abdul-Jabbar"]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage',  'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)
      
    def test_query_player_career_per_minute_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Per_Minute_Both_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
         'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_per_minute_both_pid(%s)
        """, [2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage',  'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Stat_Form'])
        
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_query_player_career_per_minute_both_pname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Per_Minute_Both_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
         'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_per_minute_both_pname(%s)
        """, ["Kareem Abdul-Jabbar"]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Birth_Date', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage',  'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Stat_Form'])
        
        pd.testing.assert_frame_equal(df_result, df_expected)

if __name__ == '__main__':
    unittest.main()