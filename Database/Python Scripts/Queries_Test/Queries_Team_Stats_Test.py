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
    
    def test_create_query_team_stats_major_one(self):
         # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_40FG.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_major_one(%s, %s, %s)
        """, ["Field_Goals_Made", "Team_Per_Game", 40]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Opponent', 'Field_Goals_Made'])

    def test_create_query_team_stats_major_two(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_40FG_90FGA.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_major_two(%s, %s, %s, %s, %s)
        """, ["Field_Goals_Made", "Field_Goals_Attempted","Team_Per_Game", 40, 90]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Opponent', 'Field_Goals_Made', 'Field_Goals_Attempted'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_team_stats_major_three(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_40FG_90FGA_48FGP.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_major_three(%s, %s, %s, %s, %s, %s, %s)
        """, ["Field_Goals_Made", "Field_Goals_Attempted", "Field_Goals_Percentage","Team_Per_Game", 40, 90, .48]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Opponent', 'Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_team_stats_major_op_one(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_OP_40FG.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_major_op_one(%s, %s, %s)
        """, ["Field_Goals_Made","Team_Per_Game", 40]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Opponent', 'Field_Goals_Made'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_create_query_team_stats_major_op_two(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_OP_40FG_90FGA.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_major_op_two(%s, %s, %s, %s, %s)
        """, ["Field_Goals_Made", "Field_Goals_Attempted","Team_Per_Game", 40, 90]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Opponent', 'Field_Goals_Made', 'Field_Goals_Attempted'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_create_query_team_stats_major_op_three(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_OP_40FG_90FGA_48FGP.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_major_op_three(%s, %s, %s, %s, %s, %s, %s)
        """, ["Field_Goals_Made", "Field_Goals_Attempted", "Field_Goals_Percentage","Team_Per_Game", 40, 90, .48]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_Name', 'Opponent', 'Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_query_team_stats_major_compare_one(self):
         # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Compare_40FG.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_major_compare_one(%s, %s, %s)
        """, ["Field_Goals_Made","Team_Per_Game", 40]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Opponent', 'Team_Name', 'Field_Goals_Made'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_query_team_stats_major_compare_two(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Compare_40FG_90FGA.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_major_compare_two(%s, %s, %s, %s, %s)
        """, ["Field_Goals_Made", "Field_Goals_Attempted","Team_Per_Game", 40, 90]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Opponent', 'Team_Name', 'Field_Goals_Made', 'Field_Goals_Attempted'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_team_stats_major_compare_three(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Compare_40FG_90FGA_48FGP.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_major_Compare_three(%s, %s, %s, %s, %s, %s, %s)
        """, ["Field_Goals_Made", "Field_Goals_Attempted", "Field_Goals_Percentage","Team_Per_Game", 40, 90, .48]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Opponent', 'Team_Name', 'Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goals_Percentage'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_team_stats_primary_sid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Primary_Team_Per_Game_2020.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float })

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_primary_sid(%s, %s, %s)
        """, ["Team_Per_Game", 2020, 0]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Opponent', 'Team_Name', 'Points', 'Assists', 'True_Rebounds', 'Steals', 'Blocks'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_team_stats_primary_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Primary_Team_Per_Game_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float })

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_primary_tid(%s, %s, %s)
        """, ["Team_Per_Game", 2, 0]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Opponent', 'Team_Name', 'Points', 'Assists', 'True_Rebounds', 'Steals', 'Blocks'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_team_stats_primary_sid_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Stats_Primary_Team_Per_Game_2020_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Points' : float, 'Assists' : float, 'True_Rebounds' : float, 'Steals' : float, 'Blocks' : float })

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_team_stats_primary_sid_tid(%s, %s, %s, %s)
        """, ["Team_Per_Game", 2020, 2, 0]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Opponent', 'Team_Name', 'Points', 'Assists', 'True_Rebounds', 'Steals', 'Blocks'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)

if __name__ == '__main__':
    unittest.main()