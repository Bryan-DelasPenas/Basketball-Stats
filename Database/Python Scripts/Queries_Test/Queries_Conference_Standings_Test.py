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
from Query_Conference_Standings import create_cs_query, drop_cs_query

'''
Class that will Conference_Standings_Queries, Assuming that the data has been inserted correctly and the procedures are created
'''
class TestQueryConferenceStandings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_cs_query()

        # Create Procedures
        create_cs_query()

    def test_create_query_all_cs_sid(self):
        
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_CS_2020.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_cs_sid(%s)
        """, 2020
        ).fetchall()
       
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
                'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])
      
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_cs_tid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_CS_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_cs_tid(%s)
        """, 2
        ).fetchall()
       
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
                'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])
      
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_create_query_all_cs_name(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_CS_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_cs_name(%s)
        """, "Boston Celtics"
        ).fetchall()
       
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
                'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])
      
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_create_query_all_cs_ABV(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_CS_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_cs_abv(%s)
        """, "BOS"
        ).fetchall()
       
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
                'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])
      
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_create_query_all_cs_win(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_CS_60wins.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_cs_win(%s)
        """, 60
        ).fetchall()
       
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
                'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])
      
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_create_query_all_cs_wl(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_CS_80_percent.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_cs_wl(%s)
        """, .8
        ).fetchall()
       
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
                'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])
      
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_create_query_all_cs_sid_ew(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_CS_2020_East.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_cs_sid_ew(%s, %s)
        """, [2020, 0]
        ).fetchall()
       
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins', 'Loses', 'Win_Lose_Percentage', 
                'Games_Behind', 'Points_Per_Game', 'Opponents_Points_Per_Game', 'Simple_Rating_System', 'East_Or_West'])
      
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_create_query_cs_win(self):
        data = [[2020, 2, 'BOS', 'Boston Celtics', 48]]
        df_expected = pd.DataFrame(data, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins'])
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_cs_win(%s, %s)
        """, [2020, 2]
        ).fetchall()
    
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Wins'])
        
        pd.testing.assert_frame_equal(df_result, df_expected)
    
if __name__ == '__main__':
    unittest.main()
    