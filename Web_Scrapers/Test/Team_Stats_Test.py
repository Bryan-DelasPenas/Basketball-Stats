import sys 
import pathlib
import pandas as pd
import numpy as np
sys.path.append(str(pathlib.Path().absolute()) + '\\Web_Scrapers' +'\\Python_Scrapers')
import os
import unittest
from Team_Stats_Scraper import get_roster, get_team_stats, get_opp_stats, get_team_misc, get_team_advanced

class TestTeamScraper(unittest.TestCase):
    
    def test_get_roster(self):
        regular_path = regular_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Team', "Roster", "2020", "2020season_DAL_roster.csv")
        df = get_roster("DAL", 2020)
        expected_df = pd.read_csv(regular_path)

        pd.testing.assert_frame_equal(df, expected_df)

    def test_get_team_stats(self):
        regular_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Team', "Team_Stats", "Team_Averages")

        regular_pergame = os.path.join(regular_path, "Per_Game", "2020season_Per_Game.csv")
        regular_perposs = os.path.join(regular_path, "Per_Poss", "2020season_Per_Poss.csv")
        regular_totals = os.path.join(regular_path, "Total", "2020season_Total.csv")

        df_pergame = get_team_stats(2020, "Per_Game")
        df_perposs = get_team_stats(2020, "Per_Poss")
        df_totals = get_team_stats(2020, "Total")

        expected_df_pergame = pd.read_csv(regular_pergame)
        expected_df_perposs = pd.read_csv(regular_perposs)
        expected_df_totals = pd.read_csv(regular_totals)

        pd.testing.assert_frame_equal(df_pergame, expected_df_pergame)
        pd.testing.assert_frame_equal(df_perposs, expected_df_perposs)
        pd.testing.assert_frame_equal(df_totals, expected_df_totals)

    def test_get_opp_stats(self):
        regular_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Team', "Team_Stats", "Opponent_Averages")

        regular_pergame = os.path.join(regular_path, "Opp_Per_Game", "2020season_Per_Game.csv")
        regular_perposs = os.path.join(regular_path, "Opp_Per_Poss", "2020season_Per_Poss.csv")
        regular_totals = os.path.join(regular_path, "Opp_Total", "2020season_Total.csv")

        df_pergame = get_opp_stats(2020, "Per_Game")
        df_perposs = get_opp_stats(2020, "Per_Poss")
        df_totals = get_opp_stats(2020, "Total")

        expected_df_pergame = pd.read_csv(regular_pergame)
        expected_df_perposs = pd.read_csv(regular_perposs)
        expected_df_totals = pd.read_csv(regular_totals)

        pd.testing.assert_frame_equal(df_pergame, expected_df_pergame)
        pd.testing.assert_frame_equal(df_perposs, expected_df_perposs)
        pd.testing.assert_frame_equal(df_totals, expected_df_totals)

    def test_get_team_misc(self):
        regular_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Team', "Team_Stats", "Team_Averages", "Team_Misc", "2020season_Team_Misc.csv") 
        df = get_team_misc(2020)
        expected_df = pd.read_csv(regular_path)

        pd.testing.assert_frame_equal(df, expected_df)
    
    def test_get_team_advanced(self):
        regular_path = os.path.join(pathlib.Path().absolute(), 'Output', "Team", "Team_Stats", "Team_Advanced", "2020", "2020_Team_Advanced_DAL_.csv")
        df = get_team_advanced("DAL", 2020)
        expected_df = pd.read_csv(regular_path)
        
        pd.testing.assert_frame_equal(df, expected_df)

if __name__ == '__main__':
    unittest.main()