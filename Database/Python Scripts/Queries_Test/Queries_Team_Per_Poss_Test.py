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
from Query_Team_Per_Poss import create_team_per_poss_query, drop_team_per_poss_query
'''
Class that will Team_Stat_Queries, Assuming that the data has been inserted correctly 
'''
class TestQueryTeamPerPoss(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_team_per_poss_query()

        # Create Procedures
        create_team_per_poss_query()

    def test_create_query_all_team_per_poss_sid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_2020.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})
       
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_per_poss_sid(%s, %s)
        """, [0, 2020]
        ).fetchall()
        
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
        'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
        'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
        'Personal_Foul', 'Points', 'Opponent'])
        
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_create_query_all_team_per_poss_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_per_poss_tid(%s, %s)
        """, [0, 2]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
        'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
        'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
        'Personal_Foul', 'Points', 'Opponent'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_team_per_poss_sid_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_2020_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_per_poss_sid_tid(%s, %s, %s)
        """, [0, 2020, 2]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
        'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
        'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
        'Personal_Foul', 'Points', 'Opponent'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_team_per_poss_name(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_per_poss_name(%s, %s)
        """, [0, "Boston Celtics"]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
        'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
        'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
        'Personal_Foul', 'Points', 'Opponent'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_team_per_poss_ABV(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Per_Poss_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Field_Goals_Made' : float, 'Field_Goals_Attempted' : float, 'Field_Goals_Percentage' : float, 'Three_Points_Made' : float, 
        'Three_Points_Attempted' : float, 'Three_Points_Percentage' : float, 'Two_Points_Made' : float, 'Two_Points_Attempted' : float, 'Two_Points_Percentage' : float, 
        'Free_Throws_Made' : float, 'Free_Throws_Attempted' : float, 'Free_Throws_Percentage' : float, 'Offensive_Rebound' : float, 'Defensive_Rebound' : float, 'True_Rebounds' : float,
        'Assists' : float, 'Steals' : float, 'Blocks' : float, 'Turn_Over' : float, 'Personal_Foul' : float, 'Points' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_per_poss_abv(%s, %s)
        """, [0, 'BOS']
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
        'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
        'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
        'Personal_Foul', 'Points', 'Opponent'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
if __name__ == '__main__':
    unittest.main()