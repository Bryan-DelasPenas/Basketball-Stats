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
from Query_Player_Stats import drop_player_stats_query, create_player_stats_query
from Call_Query_Player_Stats import *

class TestQueryPlayerTotals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_player_stats_query()

        # Create Procedures
        create_player_stats_query()
    
    def test_query_player_stats_one_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Reg_FGM.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
       
        df_result = call_query_player_stats_one_pid('Field_Goals_Made', 'Player_Totals', 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_player_stats_two_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Reg_FGM_FGA.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
        
        df_result = call_query_player_stats_two_pid('Field_Goals_Made', 'Field_Goals_Attempted','Player_Totals', 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_three_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Reg_FGM_FGA_FG%.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
        
        df_result = call_query_player_stats_three_pid('Field_Goals_Made','Field_Goals_Attempted','Field_Goals_Percentage', 'Player_Totals', 2, 0 )
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_primary_pid(self): 
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Reg_Primary_Totals.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float})
        
        df_result = call_query_player_stats_primary_pid('Player_Totals', 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_one_above_pid(self): 
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Reg_FGM_Above600.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
        
        df_result = call_query_player_stats_one_above_pid('Field_Goals_Made', 'Player_Totals', 2, 0, 600)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_two_above_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Reg_FGM_Above600_FGA_Above1200.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
           
        df_result = call_query_player_stats_two_above_pid('Field_Goals_Made', 'Field_Goals_Attempted','Player_Totals', 2, 0, 600, 1200)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_three_above_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Reg_FGM_Above600_FGA_Above1200_FG%_Above50.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
       
        df_result = call_query_player_stats_three_above_pid('Field_Goals_Made','Field_Goals_Attempted','Field_Goals_Percentage' ,'Player_Totals', 2, 0, 600, 1200, .5)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_one_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Reg_FGM.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
       
        df_result = call_query_player_stats_one_pid('Field_Goals_Made', 'Player_Totals', 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_two_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Reg_Lakers_FGM_FGA.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
           
        df_result = call_query_player_stats_two_tid_pid('Field_Goals_Made', 'Field_Goals_Attempted','Player_Totals', 14, 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_three_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Reg_Lakers_FGM_FGA_FG%.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_player_stats_three_tid_pid(%s, %s, %s, %s, %s, %s, %s)
        """, ['Field_Goals_Made','Field_Goals_Attempted','Field_Goals_Percentage' ,'Player_Totals', 0, 14, 2]
        ).fetchall()
       
        df_result = call_query_player_stats_three_tid_pid('Field_Goals_Made','Field_Goals_Attempted','Field_Goals_Percentage' ,'Player_Totals', 14, 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_primary_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Lakers_Kareem_Abdul_Jabbar_Reg_Primary_Totals.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float})
        
        df_result = call_query_player_stats_primary_tid_pid('Player_Totals', 14, 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_one_above_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Lakers_Kareem_Abdul_Jabbar_Reg_FGM_Above600.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})

        df_result = call_query_player_stats_one_above_tid_pid('Field_Goals_Made', 'Player_Totals', 14, 2, 0, 600)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_two_above_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data','Query_Player_Stats_Lakers_Kareem_Abdul_Jabbar_Reg_FGM_Above600_FGA_Above1200.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})

        df_result = call_query_player_stats_two_above_tid_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Player_Totals', 14, 2, 0, 600, 1200)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_player_stats_three_above_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data','Query_Player_Stats_Lakers_Kareem_Abdul_Jabbar_Reg_FGM_Above600_FGA_Above1200_FG%_Above50.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})

        df_result = call_query_player_stats_three_above_tid_pid('Field_Goals_Made','Field_Goals_Attempted','Field_Goals_Percentage', 'Player_Totals', 14, 2, 0, 600, 1200, .5)
        pd.testing.assert_frame_equal(df_result, df_expected)


    def test_query_player_stats_one_sid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_1985_Reg_FGM.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
       
        df_result = call_query_player_stats_one_sid_pid('Field_Goals_Made', 'Player_Totals', 1985, 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_two_sid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_1985_Reg_FGM_FGA.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float })
       
        df_result = call_query_player_stats_two_sid_pid('Field_Goals_Made', 'Field_Goals_Attempted','Player_Totals', 1985, 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_three_sid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_1985_Reg_FGM_FGA_FG%.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float })
       
        df_result = call_query_player_stats_three_sid_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Player_Totals', 1985, 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_primary_sid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_1985_Reg_Primary.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float})
        
        df_result = call_query_player_stats_primary_sid_pid('Player_Totals', 1985, 2, 0)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_player_stats_one_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Both_FGM.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
       
        df_result = call_query_player_stats_one_both_pid('Field_Goals_Made', 'Player_Totals', 2)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_two_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Both_FGM_FGA.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float })
       
        df_result = call_query_player_stats_two_both_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Player_Totals', 2)
        pd.testing.assert_frame_equal(df_result, df_expected)


    def test_query_player_stats_three_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Both_FGM_FGA_FG%.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
       
        df_result = call_query_player_stats_three_both_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Player_Totals', 2)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_primary_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Both_Primary.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float})
       
        df_result = call_query_player_stats_primary_both_pid( 'Player_Totals', 2)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_one_both_above_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Both_FGM_Above600.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
       
        df_result = call_query_player_stats_one_both_above_pid('Field_Goals_Made', 'Player_Totals', 2, 600)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_two_both_above_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Both_FGM_Above600_FGA_Above1200.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
       
        df_result = call_query_player_stats_two_both_above_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Player_Totals', 2, 600, 1200)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_three_both_above_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_Both_FGM_Above600_FGA_Above1200_FG%_Above50.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
       
        df_result = call_query_player_stats_three_both_above_pid('Field_Goals_Made', 'Field_Goals_Attempted',  'Field_Goals_Percentage', 'Player_Totals', 2, 600, 1200, .5)
        pd.testing.assert_frame_equal(df_result, df_expected)


    def test_query_player_stats_one_both_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Lakers_Kareem_Abdul_Jabbar_Both_FGM.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
       
        df_result = call_query_player_stats_one_both_tid_pid('Field_Goals_Made', 'Player_Totals', 14, 2)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_two_both_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Lakers_Kareem_Abdul_Jabbar_Both_FGM_FGA.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
       
        df_result = call_query_player_stats_two_both_tid_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Player_Totals', 14, 2)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_three_both_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Lakers_Kareem_Abdul_Jabbar_Both_FGM_FGA_FG%.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
       
        df_result = call_query_player_stats_three_both_tid_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Player_Totals', 14, 2)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_primary_both_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Lakers_Kareem_Abdul_Jabbar_Both_Primary.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float})
       
        df_result = call_query_player_stats_primary_both_tid_pid( 'Player_Totals', 14, 2)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_one_both_above_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Lakers_Kareem_Abdul_Jabbar_Both_FGM_Above600.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
       
        df_result = call_query_player_stats_one_both_above_tid_pid('Field_Goals_Made', 'Player_Totals', 14, 2, 600)
        pd.testing.assert_frame_equal(df_result, df_expected)

        
    def test_query_player_stats_two_both_above_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Lakers_Kareem_Abdul_Jabbar_Both_FGM_Above600_FGA_Above1200.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
       
        df_result = call_query_player_stats_two_both_above_tid_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Player_Totals', 14, 2, 600, 1200)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_three_both_above_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Lakers_Kareem_Abdul_Jabbar_Both_FGM_Above600_FGA_Above1200_FG%_Above50.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
       
        df_result = call_query_player_stats_three_both_above_tid_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Player_Totals', 14, 2, 600, 1200, .5)
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_player_stats_one_both_sid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_1985_Both_FGM.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float})
       
        df_result = call_query_player_stats_one_both_sid_pid('Field_Goals_Made', 'Player_Totals', 1985, 2)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_two_both_sid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_1985_Both_FGM_FGA.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
       
        df_result = call_query_player_stats_two_both_sid_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Player_Totals', 1985, 2)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_three_both_sid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_1985_Both_FGM_FGA_FG%.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float})
       
        df_result = call_query_player_stats_three_both_sid_pid('Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Player_Totals', 1985, 2)
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_player_stats_primary_both_sid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_Player_Stats_Kareem_Abdul_Jabbar_1985_Both_Primary.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float})
       
        df_result = call_query_player_stats_primary_both_sid_pid('Player_Totals', 1985, 2)
        pd.testing.assert_frame_equal(df_result, df_expected)


if __name__ == '__main__':
    unittest.main()