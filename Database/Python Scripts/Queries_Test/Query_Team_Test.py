import pandas as pd
import numpy as np
import sys 
import pathlib
import os
import unittest
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')

import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine

from Helper_DB import create_connection, test_connection, check_table
from Create_Tables_DB import create_season_table, create_team_table

'''
Class that will Team_Queries, Assuming that the data has been inserted correctly and the procedures are created
'''
class TestQueryTeam(unittest.TestCase):

    def test_create_query_all_team_sid(self):

        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Output', 'Season', 'Team_Names', '2020_Team_Names.csv')

        df_expected = pd.read_csv(path)
        df_expected = df_expected.rename(columns={'Season' : 'Season_ID', 'Team ID' : 'Team_ID', 'Team' : 'Team_Name', 'Team ABV' : 'Team_ABV'})
     
        # Add Total After Trade
        df_expected.loc[len(df_expected.index)] = [2020, 31, "Total After Trade", "TOT"]
        
        # Sort by Team_ID
        df_expected = df_expected.sort_values(by=['Team_ID'])

        # Reset and drop the index
        df_expected = df_expected.reset_index()
        df_expected = df_expected.drop(['index'], axis=1)

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_sid(%s)
        """, 2020
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
        
    
    def test_create_query_all_team_tid(self):
        data = []
        # Iterate through all completed seasons
        for i in range(1980, 2021):
            data.append([np.int64(i), np.int64(2), 'Boston Celtics', 'BOS'])
        
        # Create a empty dataframe with the following columns
        df_expected = pd.DataFrame(data, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
       
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_tid(%s)
        """, 2
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
    
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_create_query_all_team_name(self):
        data = []
        # Iterate through all completed seasons
        for i in range(1980, 2021):
            data.append([np.int64(i), np.int64(2), 'Boston Celtics', 'BOS'])
        
        # Create a empty dataframe with the following columns
        df_expected = pd.DataFrame(data, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
       
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_name(%s)
        """, 'Boston Celtics'
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
    
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_create_query_all_ABV(self):
        data = []
        # Iterate through all completed seasons
        for i in range(1980, 2021):
            data.append([np.int64(i), np.int64(2), 'Boston Celtics', 'BOS'])
        
        # Create a empty dataframe with the following columns
        df_expected = pd.DataFrame(data, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
       
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_name(%s)
        """, 'Boston Celtics'
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
    
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_team_name(self):
        team_id_expected = 2

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_name(%s)
        """, 'Boston Celtics'
        ).fetchall()
       
        self.assertEqual(result[0][0], team_id_expected)
    
    def test_create_query_team_abv(self):
        team_id_expected = 2

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_abv(%s)
        """, 'BOS'
        ).fetchall()
       
        self.assertEqual(result[0][0], team_id_expected)
  
if __name__ == '__main__':
    unittest.main()