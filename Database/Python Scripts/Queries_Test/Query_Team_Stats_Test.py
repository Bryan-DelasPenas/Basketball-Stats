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
from Query_Team_Stats import create_team_stats_query, drop_team_stats_query
from Call_Query_Team_Stats import *

'''
Class that will Team_Stat_Queries, Assuming that the data has been inserted correctly 
'''
class TestQueryTeamStat(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_team_stats_query()

        # Create Procedures
        create_team_stats_query()
  
    def test_create_query_team_stats_minor_one(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Offensive_Rating_110.csv')
        df_expected = pd.read_csv(path)
        df_result = call_query_team_stats_minor_one("Offensive_Rating", "Team_Misc", 110)
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_team_stats_minor_two(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Offensive_Rating_110_Defensive_Rating_100.csv')
        df_expected = pd.read_csv(path)
        df_result = call_query_team_stats_minor_two("Offensive_Rating", "Defensive_Rating","Team_Misc", 110, 100)
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    

    def test_create_query_team_stats_minor_three(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Offensive_Rating_110_Defensive_100_Net_Rating_9.csv')
        df_expected = pd.read_csv(path)
        df_result = call_query_team_stats_minor_three("Offensive_Rating", "Defensive_Rating", "Net_Rating", "Team_Misc", 110, 100, 9)
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_team_stats_major_one(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_40FG.csv')
        df_expected = pd.read_csv(path)
        
        df_result = call_query_team_stats_major_one("Field_Goals_Made", "Team_Per_Game", 40)

    
    def test_create_query_team_stats_major_two(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_40FG_90FGA.csv')
        df_expected = pd.read_csv(path)
        df_result = call_query_team_stats_major_two("Field_Goals_Made", "Field_Goals_Attempted", "Team_Per_Game", 40, 90)
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_team_stats_major_three(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_40FG_90FGA_48FGP.csv')
        df_expected = pd.read_csv(path)
        df_result = call_query_team_stats_major_three("Field_Goals_Made", "Field_Goals_Attempted", "Field_Goals_Percentage","Team_Per_Game", 40, 90, .48)
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_team_stats_major_op_one(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_OP_40FG.csv')
        df_expected = pd.read_csv(path)
        df_result = call_query_team_stats_major_op_one("Field_Goals_Made","Team_Per_Game", 40)
   
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_create_query_team_stats_major_op_two(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_OP_40FG_90FGA.csv')
        df_expected = pd.read_csv(path)
        df_result = call_query_team_stats_major_op_two("Field_Goals_Made", "Field_Goals_Attempted","Team_Per_Game", 40, 90)

        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_create_query_team_stats_major_op_three(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_OP_40FG_90FGA_48FGP.csv')
        df_expected = pd.read_csv(path)
        df_result = call_query_team_stats_major_op_three("Field_Goals_Made", "Field_Goals_Attempted", "Field_Goals_Percentage","Team_Per_Game", 40, 90, .48)
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_team_stats_major_compare_one(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Compare_40FG.csv')
        df_expected = pd.read_csv(path)
        df_result = call_query_team_stats_major_compare_one("Field_Goals_Made","Team_Per_Game", 40)
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_team_stats_major_compare_two(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Compare_40FG_90FGA.csv')
        df_expected = pd.read_csv(path)
        df_result = call_query_team_stats_major_compare_two("Field_Goals_Made", "Field_Goals_Attempted","Team_Per_Game", 40, 90)
   
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_team_stats_major_compare_three(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Compare_40FG_90FGA_48FGP.csv')
        df_expected = pd.read_csv(path)
        df_result = call_query_team_stats_major_compare_three("Field_Goals_Made", "Field_Goals_Attempted", "Field_Goals_Percentage","Team_Per_Game", 40, 90, .48)
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_team_stats_primary_sid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Primary_Team_Per_Game_2020.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float })
        df_result = call_query_team_stats_primary_sid("Team_Per_Game", 2020, 0)
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_team_stats_primary_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Primary_Team_Per_Game_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float })

        df_result = call_query_team_stats_primary_tid("Team_Per_Game", 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_team_stats_primary_sid_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Primary_Team_Per_Game_2020_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float })

        df_result = call_query_team_stats_primary_sid_tid("Team_Per_Game", 2020, 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)
    

if __name__ == '__main__':
    unittest.main()