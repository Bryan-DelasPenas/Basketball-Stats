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
from Query_Team_Advanced import create_team_advanced_query, drop_team_advanced_query
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

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_advanced_sid(%s)
        """, 2020
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Wins', 'Team_Loses', 'Win_Lose_Percentage', 'Team_Finish', 'Simple_Rating_System',
        'Pace', 'Relative_Pace', 'Offensive_Rating', 'Relative_Offensive_Rating', 'Defensive_Rating', 'Relative_Defensive_Rating', 'Playoffs_Finish', 'Coaches'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_team_advanced_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Advanced_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Simple_Rating_System' : float, 'Pace' : float, 'Relative_Pace' : float, 'Offensive_Rating' : float, 'Relative_Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Relative_Defensive_Rating' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_advanced_tid(%s)
        """, 2
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Wins', 'Team_Loses', 'Win_Lose_Percentage', 'Team_Finish', 'Simple_Rating_System',
        'Pace', 'Relative_Pace', 'Offensive_Rating', 'Relative_Offensive_Rating', 'Defensive_Rating', 'Relative_Defensive_Rating', 'Playoffs_Finish', 'Coaches'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_team_advanced_sid_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Advanced_2020_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Simple_Rating_System' : float, 'Pace' : float, 'Relative_Pace' : float, 'Offensive_Rating' : float, 'Relative_Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Relative_Defensive_Rating' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_advanced_sid_tid(%s, %s)
        """, [2020, 2]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Wins', 'Team_Loses', 'Win_Lose_Percentage', 'Team_Finish', 'Simple_Rating_System',
        'Pace', 'Relative_Pace', 'Offensive_Rating', 'Relative_Offensive_Rating', 'Defensive_Rating', 'Relative_Defensive_Rating', 'Playoffs_Finish', 'Coaches'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_team_advanced_name(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Advanced_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Simple_Rating_System' : float, 'Pace' : float, 'Relative_Pace' : float, 'Offensive_Rating' : float, 'Relative_Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Relative_Defensive_Rating' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_advanced_name(%s)
        """, "Boston Celtics"
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Wins', 'Team_Loses', 'Win_Lose_Percentage', 'Team_Finish', 'Simple_Rating_System',
        'Pace', 'Relative_Pace', 'Offensive_Rating', 'Relative_Offensive_Rating', 'Defensive_Rating', 'Relative_Defensive_Rating', 'Playoffs_Finish', 'Coaches'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_team_advanced_ABV(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Advanced_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Simple_Rating_System' : float, 'Pace' : float, 'Relative_Pace' : float, 'Offensive_Rating' : float, 'Relative_Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Relative_Defensive_Rating' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_advanced_abv(%s)
        """, 'BOS'
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Wins', 'Team_Loses', 'Win_Lose_Percentage', 'Team_Finish', 'Simple_Rating_System',
        'Pace', 'Relative_Pace', 'Offensive_Rating', 'Relative_Offensive_Rating', 'Defensive_Rating', 'Relative_Defensive_Rating', 'Playoffs_Finish', 'Coaches'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
if __name__ == '__main__':
    unittest.main()