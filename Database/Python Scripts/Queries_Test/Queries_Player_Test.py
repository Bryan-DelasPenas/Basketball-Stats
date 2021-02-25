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
from Create_Tables_DB import create_season_table, create_team_table

'''
Class that will Player_Queries, Assuming that the data has been inserted correctly and the procedures are created
'''
class TestQueryPlayer(unittest.TestCase):

    def test_create_query_all_player_pid(self):
        data = [2, "April 16, 1947", "Kareem Abdul-Jabbar"]
        df_expected = pd.DataFrame(data, columns=['Player_ID', 'Birth_Date', 'Player_Name'])

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        result = conn.execute(
        """
        CALL query_all_player_pid(%s)
        """, 2
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Birth_Date', 'Player_Name'])
    
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_create_query_all_player_name_dob(self):
        data = [2, "April 16, 1947", "Kareem Abdul-Jabbar"]
        df_expected = pd.DataFrame(data, columns=['Player_ID', 'Birth_Date', 'Player_Name'])

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        result = conn.execute(
        """
        CALL query_all_player_name_dob(%s, %s)
        """, ["Kareem Abdul-Jabbar", "April 16, 1947"]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Player_ID', 'Birth_Date', 'Player_Name'])
    
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_create_query_player_name(self):
        player_id_expected = 2

        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()

        # Using the year 2020
        result = conn.execute(
        """
        CALL query_player_name(%s)
        """, 'Kareem Abdul-Jabbar'
        ).fetchall()
       
        self.assertEqual(result[0][0], player_id_expected)
       
if __name__ == '__main__':
    unittest.main()
    