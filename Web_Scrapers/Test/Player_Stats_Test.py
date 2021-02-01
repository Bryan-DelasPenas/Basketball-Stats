import sys 
import pathlib
sys.path.append(str(pathlib.Path().absolute()) + '\\Web_Scrapers' +'\\Python_Scrapers')
import os
import unittest
import pandas as pd

from Player_Stats_Scraper import get_player_suffix, get_player_stats, get_career_stats

class TestPlayerScraper(unittest.TestCase):

    def test_get_player_suffix(self):
        suffix_string = str(get_player_suffix("J.J. Barea", "June 26, 1984"))
        expected_string = "/players/b/bareajo01.html"
        expected_substring = "bareajo01"
        
        message_one = "Substring not in suffix"        
        message_two = "Suffixes are not equal"

        # Check if substring is in expected string
        self.assertIn(expected_substring, suffix_string, message_one)

        # Check if the string is equal
        self.assertEqual(suffix_string, expected_string, message_two)

    def test_get_player_stats(self):
        regular_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', "Kareem Abdul-Jabbar", "Regular_Stats") 
        playoff_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', "Kareem Abdul-Jabbar", "Playoff_Stats")

        # Regular Paths
        regular_advanced = os.path.join(regular_path, "Advanced","Kareem Abdul-Jabbar_Regular_Advanced.csv")
        regular_pergame = os.path.join(regular_path,"Per_Game","Kareem Abdul-Jabbar_Regular_Per_Game.csv")
        regular_perminute = os.path.join(regular_path,"Per_Minute","Kareem Abdul-Jabbar_Regular_Per_Minute.csv")
        regular_perposs = os.path.join(regular_path, "Per_Poss","Kareem Abdul-Jabbar_Regular_Per_Poss.csv")
        regular_totals = os.path.join(regular_path, "Totals","Kareem Abdul-Jabbar_Regular_Totals.csv")
        
        # Playoff Paths
        playoff_advanced = os.path.join(playoff_path, "Advanced","Kareem Abdul-Jabbar_Playoff_Advanced.csv")
        playoff_pergame = os.path.join(playoff_path,"Per_Game","Kareem Abdul-Jabbar_Playoff_Per_Game.csv")
        playoff_perminute = os.path.join(playoff_path,"Per_Minute","Kareem Abdul-Jabbar_Playoff_Per_Minute.csv")
        playoff_perposs = os.path.join(playoff_path, "Per_Poss","Kareem Abdul-Jabbar_Playoff_Per_Poss.csv")
        playoff_totals = os.path.join(playoff_path, "Totals","Kareem Abdul-Jabbar_Playoff_Totals.csv")
        
        # Regular Advanced
        df_regular_advanced = get_player_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Advanced", False)
        expected_df_regular_advanced = pd.read_csv(regular_advanced)
    
        # Regular Per_Game
        df_regular_pergame = get_player_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Per_Game", False)
        expected_df_regular_pergame = pd.read_csv(regular_pergame)

        # Regular Per_Minute
        df_regular_perminute = get_player_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Per_Minute", False)
        expected_df_regular_perminute = pd.read_csv(regular_perminute)

        # Regular Per_Poss
        df_regular_perposs = get_player_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Per_Poss", False)
        expected_df_regular_perposs = pd.read_csv(regular_perposs)

        # Regular Totals
        df_regular_totals = get_player_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Totals", False)
        expected_df_regular_totals = pd.read_csv(regular_totals)

        # Playoff Advanced
        df_playoff_advanced = get_player_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Advanced", True)
        expected_df_playoff_advanced = pd.read_csv(playoff_advanced)
    
        # Playoff Per_Game
        df_playoff_pergame = get_player_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Per_Game", True)
        expected_df_playoff_pergame = pd.read_csv(playoff_pergame)

        # Playoff Per_Minute
        df_playoff_perminute = get_player_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Per_Minute", True)
        expected_df_playoff_perminute = pd.read_csv(playoff_perminute)

        # Playoff Per_Poss
        df_playoff_perposs = get_player_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Per_Poss", True)
        expected_df_playoff_perposs = pd.read_csv(playoff_perposs)

        # Playoff Totals
        df_playoff_totals = get_player_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Totals", True)
        expected_df_playoff_totals = pd.read_csv(playoff_totals)

        # Check Columns Name 
        # Checks regular advanced 
        pd.testing.assert_frame_equal(df_regular_advanced, expected_df_regular_advanced)
        
        # Checks regular per_game
        pd.testing.assert_frame_equal(df_regular_pergame, expected_df_regular_pergame)
        
        # Checks regular per_minute 
        pd.testing.assert_frame_equal(df_regular_perminute, expected_df_regular_perminute)
        
        # Checks regular per_poss
        pd.testing.assert_frame_equal(df_regular_perposs, expected_df_regular_perposs)
       
        # Checks regular totals
        pd.testing.assert_frame_equal(df_regular_totals, expected_df_regular_totals)
       
        # Checks playoff advanced 
        pd.testing.assert_frame_equal(df_playoff_advanced, expected_df_playoff_advanced)
        
        # Checks playoff per_game
        pd.testing.assert_frame_equal(df_playoff_pergame, expected_df_playoff_pergame)
        
        # Checks playoff per_minute
        pd.testing.assert_frame_equal(df_playoff_perminute, expected_df_playoff_perminute)
        
        # Checks playoff per_poss
        pd.testing.assert_frame_equal(df_playoff_perposs, expected_df_playoff_perposs)
       
        # Checks playoff totals
        pd.testing.assert_frame_equal(df_playoff_totals, expected_df_playoff_totals)
    
    def test_get_careeer_stats(self):
        regular_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', "Kareem Abdul-Jabbar", "Career_Regular_Stats") 
        playoff_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', "Kareem Abdul-Jabbar", "Career_Playoff_Stats")

        # Regular Paths
        regular_advanced = os.path.join(regular_path, "Advanced","Kareem Abdul-Jabbar_career_regular_Advanced.csv")
        regular_pergame = os.path.join(regular_path,"Per_Game","Kareem Abdul-Jabbar_career_regular_Per_Game.csv")
        regular_perminute = os.path.join(regular_path,"Per_Minute","Kareem Abdul-Jabbar_career_regular_Per_Minute.csv")
        regular_perposs = os.path.join(regular_path, "Per_Poss","Kareem Abdul-Jabbar_career_regular_Per_Poss.csv")
        regular_totals = os.path.join(regular_path, "Totals","Kareem Abdul-Jabbar_career_regular_Totals.csv")
        
        # Playoff Paths
        playoff_advanced = os.path.join(playoff_path, "Advanced","Kareem Abdul-Jabbar_career_playoff_Advanced.csv")
        playoff_pergame = os.path.join(playoff_path,"Per_Game","Kareem Abdul-Jabbar_career_playoff_Per_Game.csv")
        playoff_perminute = os.path.join(playoff_path,"Per_Minute","Kareem Abdul-Jabbar_career_playoff_Per_Minute.csv")
        playoff_perposs = os.path.join(playoff_path, "Per_Poss","Kareem Abdul-Jabbar_career_playoff_Per_Poss.csv")
        playoff_totals = os.path.join(playoff_path, "Totals","Kareem Abdul-Jabbar_career_playoff_Totals.csv")
        
        # Regular Advanced
        df_regular_advanced = get_career_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Advanced", False)
        expected_df_regular_advanced = pd.read_csv(regular_advanced)

        # Regular Per_Game
        df_regular_pergame = get_career_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Per_Game", False)
        expected_df_regular_pergame = pd.read_csv(regular_pergame)

        # Regular Per_Minute
        df_regular_perminute = get_career_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Per_Minute", False)
        expected_df_regular_perminute = pd.read_csv(regular_perminute)

        # Regular Per_Poss
        df_regular_perposs = get_career_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Per_Poss", False)
        expected_df_regular_perposs = pd.read_csv(regular_perposs)

        # Regular Totals
        df_regular_totals = get_career_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Totals", False)
        expected_df_regular_totals = pd.read_csv(regular_totals)

        # Playoff Advanced
        df_playoff_advanced = get_career_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Advanced", True)
        expected_df_playoff_advanced = pd.read_csv(playoff_advanced)
    
        # Playoff Per_Game
        df_playoff_pergame = get_career_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Per_Game", True)
        expected_df_playoff_pergame = pd.read_csv(playoff_pergame)

        # Playoff Per_Minute
        df_playoff_perminute = get_career_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Per_Minute", True)
        expected_df_playoff_perminute = pd.read_csv(playoff_perminute)

        # Playoff Per_Poss
        df_playoff_perposs = get_career_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Per_Poss", True)
        expected_df_playoff_perposs = pd.read_csv(playoff_perposs)

        # Playoffr Totals
        df_playoff_totals = get_career_stats("Kareem Abdul-Jabbar", "April 16, 1947", "Totals", True)
        expected_df_playoff_totals = pd.read_csv(playoff_totals)

        # Check Columns Name 
        # Checks regular advanced 
        pd.testing.assert_frame_equal(df_regular_advanced, expected_df_regular_advanced)
        
        # Checks regular per_game
        pd.testing.assert_frame_equal(df_regular_pergame, expected_df_regular_pergame)
        
        # Checks regular per_minute 
        pd.testing.assert_frame_equal(df_regular_perminute, expected_df_regular_perminute)
        
        # Checks regular per_poss
        pd.testing.assert_frame_equal(df_regular_perposs, expected_df_regular_perposs)
       
        # Checks regular totals
        pd.testing.assert_frame_equal(df_regular_totals, expected_df_regular_totals)
       
        # Checks playoff advanced 
        pd.testing.assert_frame_equal(df_playoff_advanced, expected_df_playoff_advanced)
        
        # Checks playoff per_game
        pd.testing.assert_frame_equal(df_playoff_pergame, expected_df_playoff_pergame)
        
        # Checks playoff per_minute
        pd.testing.assert_frame_equal(df_playoff_perminute, expected_df_playoff_perminute)
        
        # Checks playoff per_poss
        pd.testing.assert_frame_equal(df_playoff_perposs, expected_df_playoff_perposs)
       
        # Checks playoff totals
        pd.testing.assert_frame_equal(df_playoff_totals, expected_df_playoff_totals)
    
if __name__ == '__main__':
    unittest.main()