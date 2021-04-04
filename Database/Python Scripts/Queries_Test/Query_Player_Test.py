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
from datetime import datetime

from Helper_DB import create_connection, test_connection, check_table
from Query_Player import drop_player_query, create_player_query
from Call_Query_Player import *

'''
Class that will Player_Queries, Assuming that the data has been inserted correctly and the procedures are created
'''
class TestQueryPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_player_query()

        # Create Procedures
        create_player_query()

    def test_create_query_all_player_pid(self):
        data = [[2, "1947-04-16", "Kareem Abdul-Jabbar"]]
        df_expected = pd.DataFrame(data, columns=['Player_ID', 'Birth_Date', 'Player_Name'])
         
        df_result = call_query_all_player_pid(2)
        
        # Change Date into string 
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_create_query_all_player_name_dob(self):
        data = [[2, "1947-04-16", "Kareem Abdul-Jabbar"]]
        df_expected = pd.DataFrame(data, columns=['Player_ID', 'Birth_Date', 'Player_Name'])
         
        df_result = call_query_all_player_name_dob("Kareem Abdul-Jabbar", "1947-04-16")
    
        # Change Date into string 
        df_result = df_result.astype({'Birth_Date': str})
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    
    def test_create_query_player_name(self):
        player_id_expected = 2

        result = call_query_player_name('Kareem Abdul-Jabbar')
        
        # Every query call in python returns a 2d list 
        self.assertEqual(result, player_id_expected)
    
if __name__ == '__main__':
    unittest.main()
    