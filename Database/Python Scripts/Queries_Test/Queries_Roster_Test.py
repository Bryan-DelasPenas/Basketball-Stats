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
from Query_Roster import create_roster_query, drop_roster_query
'''
Class that will Roster_Queries, Assuming that the data has been inserted correctly and the procedures are created
'''
class TestQueryRoster(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_roster_query()

        # Create Procedures
        create_roster_query()

    def test_create_query_all_roster_sid(self):
        
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_2020.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_roster_sid(%s)
        """, 2020
        ).fetchall()
       
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
                'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_roster_tid(self):
        
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_roster_tid(%s)
        """, 2
        ).fetchall()
       
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
                'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_roster_pid(self):
        
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Player_Number': str, 'Player_Experience' : str})
        
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_roster_pid(%s)
        """, 2
        ).fetchall()
        
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
                'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_roster_pname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Player_Number': str, 'Player_Experience' : str})
        
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_roster_pname(%s)
        """, "Kareem Abdul-Jabbar"
        ).fetchall()
        
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
                'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_roster_tname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Player_Number': str, 'Player_Experience' : str})
        
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_roster_tname(%s)
        """, "Boston Celtics"
        ).fetchall()
        
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
                'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_roster_abv(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Player_Number': str, 'Player_Experience' : str})
        
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_roster_abv(%s)
        """, "BOS"
        ).fetchall()
        
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
                'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_roster_college(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_UCLA.csv')
        df_expected = pd.read_csv(path)
        
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Player_Number': str, 'Player_Experience' : str})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_roster_college(%s)
        """, "UCLA"
        ).fetchall()
        
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
                'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_create_query_all_roster_sid_tid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_2020_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Player_Number': str, 'Player_Experience' : str})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_roster_sid_tid(%s, %s)
        """, [2020, 2]
        ).fetchall()
        
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
                'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_create_query_all_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_LAL_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Player_Number': str, 'Player_Experience' : str})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_roster_tid_pid(%s, %s)
        """, [14, 2]
        ).fetchall()
        
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
                'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])
    
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_roster_sid_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_1980_LAL_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Player_Number': str, 'Player_Experience' : str})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_roster_sid_tid_pid(%s, %s, %s)
        """, [1980, 14, 2]
        ).fetchall()
        
        df_result = pd.DataFrame(result, 
        columns=['Season_ID', 'Team_ID', 'Player_ID', 'Team_ABV', 'Team_Name', 'Player_Number', 'Player_Name', 'Player_Postion', 'Player_Height', 'Player_Weight',
                'Birth_Date', 'Player_Nationality', 'Player_Experience', 'Player_College_Name'])

if __name__ == '__main__':
    unittest.main()
    