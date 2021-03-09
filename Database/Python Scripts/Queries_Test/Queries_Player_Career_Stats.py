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
from Query_Player_Career_Stats import drop_player_career_stats_query, create_player_career_stats_query

class TestQueryPlayerCareerStats(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_player_career_stats_query()

        # Create Procedures
        create_player_career_stats_query()

    def test_create_query_player_career_stats_one_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_FGM.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_stats_one_pid(%s, %s, %s, %s)
        """, ['Field_Goals_Made', 'Player_Career_Totals', 2, 0]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Stat_Form', 'Field_Goals_Made'])
        pd.testing.assert_frame_equal(df_result, df_expected)
  
    def test_create_query_player_career_stats_two_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_FGM_FGA.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_stats_two_pid(%s, %s, %s, %s, %s)
        """, ['Field_Goals_Made', 'Field_Goals_Attempted','Player_Career_Totals', 2, 0]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Stat_Form', 'Field_Goals_Made', 'Field_Goals_Attempted'])
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_player_career_stats_three_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_FGM_FGA_FGP.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_stats_three_pid(%s, %s, %s, %s, %s, %s)
        """, ['Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Player_Career_Totals', 2, 0]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Stat_Form', 'Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage'])
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_player_career_stats_one_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_Both_FGM.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_stats_one_both_pid(%s, %s, %s)
        """, ['Field_Goals_Made', 'Player_Career_Totals', 2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Field_Goals_Made'])
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_player_career_stats_two_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_Both_FGM_FGA.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_stats_two_both_pid(%s, %s, %s, %s)
        """, ['Field_Goals_Made', 'Field_Goals_Attempted','Player_Career_Totals', 2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Field_Goals_Made', 'Field_Goals_Attempted'])
        pd.testing.assert_frame_equal(df_result, df_expected)
    def test_create_query_player_career_stats_three_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_Both_FGM_FGA_FGP.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_career_stats_three_both_pid(%s, %s, %s, %s, %s)
        """, ['Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Player_Career_Totals', 2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Player_Name', 'Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage'])
        pd.testing.assert_frame_equal(df_result, df_expected)

if __name__ == '__main__':
    unittest.main()