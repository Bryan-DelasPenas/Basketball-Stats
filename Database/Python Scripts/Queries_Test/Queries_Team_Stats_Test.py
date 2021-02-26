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

'''
Class that will Team_Stat_Queries, Assuming that the data has been inserted correctly and the procedures are created
'''
class TestQueryTeamStat(unittest.TestCase):

    def test_create_query_team_stats_minor_one(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Offensive_Rating_110.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_minor_one(%s, %s, %s)
        """, ["Offensive_Rating", "Team_Misc", 110]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Offensive_Rating'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_team_stats_minor_two(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Offensive_Rating_110_Defensive_Rating_100.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_minor_two(%s, %s, %s, %s, %s)
        """, ["Offensive_Rating", "Defensive_Rating","Team_Misc", 110, 100]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Offensive_Rating', 'Defensive_Rating'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_team_stats_minor_three(self):
        
         # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Offensive_Rating_110_Defensive_100_Net_Rating_9.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_minor_three(%s, %s, %s, %s, %s, %s, %s)
        """, ["Offensive_Rating", "Defensive_Rating", "Net_Rating", "Team_Misc", 110, 100, 9]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Offensive_Rating', 'Defensive_Rating', "Net_Rating"])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    '''
    def test_create_query_team_stats_major_one(self):

    def test_create_query_team_stats_major_two(self):

    def test_create_query_team_stats_major_three(self):

    def test_create_query_team_stats_major_op_one(self):

    def test_create_query_team_stats_major_op_two(self):

    def test_create_query_team_stats_major_op_three(self):
    
    def test_create_query_team_stats_primary_pid(self):
    '''
if __name__ == '__main__':
    unittest.main()