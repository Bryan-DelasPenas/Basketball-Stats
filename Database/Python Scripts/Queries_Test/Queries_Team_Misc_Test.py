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
from Query_Team_Misc import create_team_misc_query, drop_team_misc_query
'''
Class that will Team_Stat_Queries, Assuming that the data has been inserted correctly 
'''
class TestQueryTeamMisc(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_team_misc_query()

        # Create Procedures
        create_team_misc_query()

    def test_create_query_all_team_misc_sid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Misc_2020.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Team_Average_Age' : float, 'Margin_Of_Victory' : float, 'Strength_Of_Schedule' : float, 'Simple_Rating_System' : float, 'Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Net_Rating' : float, 'Pace' : float, 'Three_Point_Attempt_Rate' : float, 'True_Shooting_Percentage' : float, 
        'Offensive_Rebound_Percentage' : float, 'Defensive_Rebound_Percentage' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_misc_sid(%s)
        """, 2020
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Average_Age', 'Team_Wins', 'Team_Loses', 'Pythagorean_Wins', 'Pythagorean_Loses', 
        'Margin_Of_Victory', 'Strength_Of_Schedule', 'Simple_Rating_System', 'Offensive_Rating', 'Defensive_Rating', 'Net_Rating', 'Pace', 'Free_Throw_Attempt_Rate', 
        'Three_Point_Attempt_Rate', 'True_Shooting_Percentage', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 'Arena', 'Attend', 'Attend_Per_Game'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_team_misc_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Misc_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Team_Average_Age' : float, 'Margin_Of_Victory' : float, 'Strength_Of_Schedule' : float, 'Simple_Rating_System' : float, 'Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Net_Rating' : float, 'Pace' : float, 'Three_Point_Attempt_Rate' : float, 'True_Shooting_Percentage' : float, 
        'Offensive_Rebound_Percentage' : float, 'Defensive_Rebound_Percentage' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_misc_tid(%s)
        """, 2
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Average_Age', 'Team_Wins', 'Team_Loses', 'Pythagorean_Wins', 'Pythagorean_Loses', 
        'Margin_Of_Victory', 'Strength_Of_Schedule', 'Simple_Rating_System', 'Offensive_Rating', 'Defensive_Rating', 'Net_Rating', 'Pace', 'Free_Throw_Attempt_Rate', 
        'Three_Point_Attempt_Rate', 'True_Shooting_Percentage', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 'Arena', 'Attend', 'Attend_Per_Game'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_team_misc_sid_tid(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Misc_2020_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Team_Average_Age' : float, 'Margin_Of_Victory' : float, 'Strength_Of_Schedule' : float, 'Simple_Rating_System' : float, 'Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Net_Rating' : float, 'Pace' : float, 'Three_Point_Attempt_Rate' : float, 'True_Shooting_Percentage' : float, 
        'Offensive_Rebound_Percentage' : float, 'Defensive_Rebound_Percentage' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_misc_sid_tid(%s, %s)
        """, [2020, 2]
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Average_Age', 'Team_Wins', 'Team_Loses', 'Pythagorean_Wins', 'Pythagorean_Loses', 
        'Margin_Of_Victory', 'Strength_Of_Schedule', 'Simple_Rating_System', 'Offensive_Rating', 'Defensive_Rating', 'Net_Rating', 'Pace', 'Free_Throw_Attempt_Rate', 
        'Three_Point_Attempt_Rate', 'True_Shooting_Percentage', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 'Arena', 'Attend', 'Attend_Per_Game'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_team_misc_name(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Misc_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Team_Average_Age' : float, 'Margin_Of_Victory' : float, 'Strength_Of_Schedule' : float, 'Simple_Rating_System' : float, 'Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Net_Rating' : float, 'Pace' : float, 'Three_Point_Attempt_Rate' : float, 'True_Shooting_Percentage' : float, 
        'Offensive_Rebound_Percentage' : float, 'Defensive_Rebound_Percentage' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_misc_name(%s)
        """, "Boston Celtics"
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Average_Age', 'Team_Wins', 'Team_Loses', 'Pythagorean_Wins', 'Pythagorean_Loses', 
        'Margin_Of_Victory', 'Strength_Of_Schedule', 'Simple_Rating_System', 'Offensive_Rating', 'Defensive_Rating', 'Net_Rating', 'Pace', 'Free_Throw_Attempt_Rate', 
        'Three_Point_Attempt_Rate', 'True_Shooting_Percentage', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 'Arena', 'Attend', 'Attend_Per_Game'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_team_misc_ABV(self):
        # Create path to csv file    
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Team_Misc_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        df_expected = df_expected.astype({'Team_Average_Age' : float, 'Margin_Of_Victory' : float, 'Strength_Of_Schedule' : float, 'Simple_Rating_System' : float, 'Offensive_Rating' : float, 
        'Defensive_Rating' : float, 'Net_Rating' : float, 'Pace' : float, 'Three_Point_Attempt_Rate' : float, 'True_Shooting_Percentage' : float, 
        'Offensive_Rebound_Percentage' : float, 'Defensive_Rebound_Percentage' : float})

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_all_team_misc_abv(%s)
        """, 'BOS'
        ).fetchall()
     
        df_result = pd.DataFrame(result, columns=['Season_ID', 'Team_ID', 'Team_ABV', 'Team_Name', 'Team_Average_Age', 'Team_Wins', 'Team_Loses', 'Pythagorean_Wins', 'Pythagorean_Loses', 
        'Margin_Of_Victory', 'Strength_Of_Schedule', 'Simple_Rating_System', 'Offensive_Rating', 'Defensive_Rating', 'Net_Rating', 'Pace', 'Free_Throw_Attempt_Rate', 
        'Three_Point_Attempt_Rate', 'True_Shooting_Percentage', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 'Arena', 'Attend', 'Attend_Per_Game'])
   
        pd.testing.assert_frame_equal(df_result, df_expected)
    
if __name__ == '__main__':
    unittest.main()