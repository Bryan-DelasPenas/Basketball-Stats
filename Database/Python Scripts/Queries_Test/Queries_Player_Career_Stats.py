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

class TestQueryPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_player_career_stats_query()

        # Create Procedures
        create_player_career_stats_query()

    def test_create_query_player_career_stats_one_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Career_Kareem_Abdul_Jabbar_Field_Goals_Made.csv')
        df_expected = pd.read_csv(path)
        print(type(df_expected['Stat_Form'][0]))

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
        print()
        print(type(df_result['Stat_Form'][0]))
        pd.testing.assert_frame_equal(df_result, df_expected)
    '''
    def test_create_query_player_career_stats_two_pid(self):
    def test_create_query_player_career_stats_three_pid(self):

    def test_create_query_player_career_stats_one_both_pid(self):
    def test_create_query_player_career_stats_two_both_pid(self):
    def test_create_query_player_career_stats_three_both_pid(self):
    '''

if __name__ == '__main__':
    unittest.main()