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
from Query_Team import create_team_query, drop_team_query
from Call_Query_Team import *
'''
Class that will Team_Queries, Assuming that the data has been inserted correctly and the procedures are created
'''
class TestQueryTeam(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_team_query()

        # Create Procedures
        create_team_query()

    def test_create_query_all_team_sid(self):

        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Web_Scrapers', 'Output', 'Season', 'Team_Names', '2020_Team_Names.csv')

        df_expected = pd.read_csv(path)
        df_expected = df_expected.rename(columns={'Season' : 'Season_ID', 'Team ID' : 'Team_ID', 'Team ABV' : 'Team_ABV', 'Team' : 'Team_Name'})
     
        # Add Total After Trade
        df_expected.loc[len(df_expected.index)] = [2020, 31, "Total After Trade", "TOT"]
        
        # Sort by Team_ID
        df_expected = df_expected.sort_values(by=['Team_ID'])

        # Reset and drop the index
        df_expected = df_expected.reset_index()
        df_expected = df_expected.drop(['index'], axis=1)

        df_result = call_query_all_team_sid(2020)
        pd.testing.assert_frame_equal(df_result, df_expected)
        
    
    def test_create_query_all_team_tid(self):
        data = []
        # Iterate through all completed seasons
        for i in range(1980, 2021):
            data.append([np.int64(i), np.int64(2), 'Boston Celtics', 'BOS'])
        
        # Create a empty dataframe with the following columns
        df_expected = pd.DataFrame(data, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
        df_result = call_query_all_team_tid(2)
    
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_create_query_all_team_name(self):
        data = []
        # Iterate through all completed seasons
        for i in range(1980, 2021):
            data.append([np.int64(i), np.int64(2), 'Boston Celtics', 'BOS'])
        
        # Create a empty dataframe with the following columns
        df_expected = pd.DataFrame(data, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
        df_result = call_query_all_team_name('Boston Celtics')
   
        pd.testing.assert_frame_equal(df_result, df_expected)


    def test_create_query_all_ABV(self):
        data = []
        # Iterate through all completed seasons
        for i in range(1980, 2021):
            data.append([np.int64(i), np.int64(2), 'Boston Celtics', 'BOS'])
        
        # Create a empty dataframe with the following columns
        df_expected = pd.DataFrame(data, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Team_ABV'])
        df_result = call_query_all_team_ABV('BOS')
    
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_team_name(self):
        team_id_expected = 2
        result = call_query_team_name("Boston Celtics")

        self.assertEqual(result, team_id_expected)
    
    
    def test_create_query_team_abv(self):
        team_id_expected = 2
        result = calls_query_team_abv('BOS')
    
        self.assertEqual(result, team_id_expected)
     
if __name__ == '__main__':
    unittest.main()