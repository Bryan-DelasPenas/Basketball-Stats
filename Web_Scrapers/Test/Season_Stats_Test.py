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
        standard_path = os.path.join(pathlib.Path().absolute(), 'Output', "Season", "Standings")
    
     
        df_east, df_west = get_standings(2020)
    
        east_path = os.path.join(standard_path, "East", "2020season_east_Standard.csv")
        west_path = os.path.join(standard_path, "West", "2020season_west_Standard.csv")

        # Read in the csv
        expected_df_east = pd.read_csv(east_path)
        expected_df_west = pd.read_csv(west_path)
    
        # Error messages
        message_one = "Dataframe east is incorrect"
        message_two = "Dataframe west is incorrect"

        # Standard 
        self.assertCountEqual(list(df_east), list(expected_df_east), message_one)
        self.assertCountEqual(list(df_west), list(expected_df_west), message_two)

        
if __name__ == '__main__':
    unittest.main()