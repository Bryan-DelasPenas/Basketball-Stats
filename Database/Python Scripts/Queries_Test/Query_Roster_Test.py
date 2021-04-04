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
from Query_Roster import create_roster_query, drop_roster_query
from Call_Query_Roster import *

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

    def test_query_all_roster_sid(self):
        
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_2020.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str})

        df_result = call_query_all_roster_sid(2020)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_all_roster_tid(self):
        
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Birth_Date' : str})
       
        df_result = call_query_all_roster_tid(2)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_all_roster_pid(self):
        
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Birth_Date' : str, 'Player_Number': str, 'Player_Experience' : str})
        
        df_result = call_query_all_roster_pid(2)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_all_roster_pname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Birth_Date': str, 'Player_Number': str, 'Player_Experience' : str})
        
        df_result = call_query_all_roster_pname("Kareem Abdul-Jabbar")
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    

    def test_query_all_roster_tname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Birth_Date': str, 'Player_Number': str, 'Player_Experience' : str})
        
        df_result = call_query_all_roster_tname("Boston Celtics")
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    

    def test_query_all_roster_abv(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Birth_Date': str, 'Player_Number': str, 'Player_Experience' : str})
        
        df_result = call_query_all_roster_abv("BOS")
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_all_roster_college(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_UCLA.csv')
        df_expected = pd.read_csv(path)
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Birth_Date': str, 'Player_Number': str, 'Player_Experience' : str})
            
        df_result = call_query_all_roster_college("UCLA")
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_all_roster_sid_tid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_2020_Boston_Celtics.csv')
        df_expected = pd.read_csv(path)
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Birth_Date': str, 'Player_Number': str, 'Player_Experience' : str})
        
        df_result = call_query_all_roster_sid_tid(2020, 2)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)

    
    def test_query_all_roster_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_LAL_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Birth_Date': str, 'Player_Number': str, 'Player_Experience' : str})

        df_result = call_query_all_roster_tid_pid(14, 2)
        df_result = df_result.astype({'Birth_Date': str})

        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_query_all_roster_sid_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Roster_1980_LAL_Kareem_Abdul_Jabbar.csv')
        df_expected = pd.read_csv(path)
        # Change Player Num and Player Exp to strings
        df_expected = df_expected.astype({'Birth_Date': str, 'Player_Number': str, 'Player_Experience' : str})
        
        df_result = call_query_all_roster_sid_tid_pid(1980, 14, 2)
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
if __name__ == '__main__':
    unittest.main()
    