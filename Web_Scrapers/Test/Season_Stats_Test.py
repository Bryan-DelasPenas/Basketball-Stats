import pandas as pd
import sys 
import pathlib
sys.path.append(str(pathlib.Path().absolute()) + '\\Web_Scrapers' +'\\Python_Scrapers')
import os
import unittest

from Season_Stats_Scraper import get_team_name, get_standings

class TestSeasonScraper(unittest.TestCase):
    def test_get_name(self):
        path = os.path.join(pathlib.Path().absolute(), 'Output', "Season", "Team_Names", "1980_Team_Names.csv")
        df = get_team_name(2020)
        expected_df = pd.read_csv(path)
        message = "Team names is incorrect"

        self.assertCountEqual(list(df), list(expected_df), message)

    def test_get_standings(self):
        standard_path = os.path.join(pathlib.Path().absolute(), 'Output', "Season", "Standings", "Standard")
        expanded_path = os.path.join(pathlib.Path().absolute(), 'Output', "Season", "Standings","Expanded_Standings", "2020season_Expanded_Standings.csv")                                                         
        vs_path = os.path.join(pathlib.Path().absolute(), 'Output', "Season", "Standings", "Team_vs_Team", "2020season_Team_Vs_Team.csv")
        
        
        df_east, df_west = get_standings(2020)
        df_expanded = get_standings(2020, "Expanded_Standings")
        df_vs = get_standings(2020, "Team_vs_Team")

        east_path = os.path.join(standard_path, "East", "2020season_east_Standard.csv")
        west_path = os.path.join(standard_path, "West", "2020season_west_Standard.csv")

        # Read in the csv
        expected_df_east = pd.read_csv(east_path)
        expected_df_west = pd.read_csv(west_path)
        expected_df_expanded = pd.read_csv(expanded_path)
        expected_df_vs = pd.read_csv(vs_path)

        # Error messages
        message_one = "Dataframe east is incorrect"
        message_two = "Dataframe west is incorrect"
        message_three = "Expected_Standings is incorrect"
        message_four = "Team_vs_Team is incorrect"

        # Standard 
        self.assertCountEqual(list(df_east), list(expected_df_east), message_one)
        self.assertCountEqual(list(df_west), list(expected_df_west), message_two)

        # Expanded_Standings
        self.assertCountEqual(list(df_expanded), list(expected_df_expanded), message_three)

        # Team_Vs_Team
        self.assertCountEqual(list(df_vs), list(expected_df_vs), message_four)
        
if __name__ == '__main__':
    unittest.main()