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
from Query_Player_Totals import drop_player_totals_query, create_player_totals_query

class TestQueryPlayerTotals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_player_totals_query()

        # Create Procedures
        create_player_totals_query()
    
    def test_query_all_player_totals_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Totals_Kareem_Abdul_Jabbar_Reg_Pid.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_player_totals_pid(%s, %s)
        """, [0, 2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Triple_Double','Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_totals_sid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Totals_Kareem_Abdul_Jabbar_1985_Reg.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_player_totals_sid_pid(%s, %s, %s)
        """, [0, 1985, 2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Triple_Double','Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_totals_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Totals_Kareem_Abdul_Jabbar_Reg_Lakers.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_player_totals_tid_pid(%s, %s, %s)
        """, [0, 14, 2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Triple_Double','Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_totals_pname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Totals_Kareem_Abdul_Jabbar_Reg_Pid.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_player_totals_pname(%s, %s)
        """, [0, "Kareem Abdul-Jabbar"]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points','Triple_Double', 'Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_totals_pname_sid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Totals_Kareem_Abdul_Jabbar_1985_Reg.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
  
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_player_totals_pname_sid(%s, %s, %s)
        """, [0, "Kareem Abdul-Jabbar", 1985]
        ).fetchall()
    
        df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points','Triple_Double', 'Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_totals_pname_tid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Totals_Kareem_Abdul_Jabbar_Reg_Lakers.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_player_totals_pname_tid(%s, %s, %s)
        """, [0, "Kareem Abdul-Jabbar", 14]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Triple_Double', 'Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_totals_both_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Totals_Kareem_Abdul_Jabbar_Both.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_player_totals_both_pid(%s)
        """, [2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Triple_Double','Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_totals_both_sid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Totals_Kareem_Abdul_Jabbar_1985_Both.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_player_totals_both_sid_pid(%s, %s)
        """, [1985, 2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points','Triple_Double', 'Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_totals_both_tid_pid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Totals_Kareem_Abdul_Jabbar_Both_Lakers.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_player_totals_both_tid_pid(%s, %s)
        """, [14, 2]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Triple_Double','Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)
    
    def test_query_all_player_totals_both_pname(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Totals_Kareem_Abdul_Jabbar_Both.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_player_totals_both_pname(%s)
        """, ["Kareem Abdul-Jabbar"]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Triple_Double','Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_totals_both_pname_sid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Totals_Kareem_Abdul_Jabbar_1985_Both.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_player_totals_both_pname_sid(%s, %s)
        """, ["Kareem Abdul-Jabbar", 1985]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Triple_Double','Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)

    def test_query_all_player_totals_both_pname_tid(self):
        path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Queries_Test', 'Expected_Data', 'Query_All_Player_Totals_Kareem_Abdul_Jabbar_Both_Lakers.csv')
        df_expected = pd.read_csv(path)
        df_expected = df_expected.astype({'Field_Goals_Made':float, 'Field_Goals_Attempted':float, 'Field_Goals_Percentage':float, 'Three_Points_Made':float, 
        'Three_Points_Attempted':float, 'Three_Points_Percentage':float, 'Two_Points_Made':float, 'Two_Points_Attempted':float, 'Two_Points_Percentage':float, 
        'Effective_Field_Goal_Percentage':float, 'Free_Throws_Made':float, 'Free_Throws_Attempted':float, 'Free_Throws_Percentage':float, 
        'Offensive_Rebounds':float, 'Defensive_Rebounds':float, 'True_Rebounds':float, 'Assists':float, 'Steals':float, 'Blocks':float, 'Turn_Over':float, 
        'Personal_Fouls':float, 'Points':float})
        
        # Connect to sql database
        engine = create_connection()
        
        # Test the connection of the database
        conn = test_connection(engine)
        trans = conn.begin()
        
        result = conn.execute(
        """
        CALL query_all_player_totals_both_pname_tid(%s, %s)
        """, ["Kareem Abdul-Jabbar",14]
        ).fetchall()
       
        df_result = pd.DataFrame(result, columns=['Season_ID','Team_ID','Player_ID', 'Team_ABV','Team_Name','Player_Name', 'Birth_Date','Player_Age','League', 'Player_Postion', 'Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Triple_Double','Stat_Form'])
        pd.testing.assert_frame_equal(df_result, df_expected)

if __name__ == '__main__':
    unittest.main()