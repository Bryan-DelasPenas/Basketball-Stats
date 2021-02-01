import sys 
import pathlib
import pandas as pd
import numpy as np
sys.path.append(str(pathlib.Path().absolute()) + '\\Web_Scrapers' +'\\Python_Scrapers')
import os
import unittest
from Team_Stats_Scraper import get_roster, get_roster_stats, get_team_stats, get_opp_stats, get_team_misc, get_team_advanced

class TestTeamScraper(unittest.TestCase):
    
    def test_get_roster(self):
        regular_path = regular_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Team', "Roster", "Team_Roster", "2020", "2020season_DAL_roster.csv")
        df = get_roster("DAL", 2020)
        expected_df = pd.read_csv(regular_path)

        pd.testing.assert_frame_equal(df, expected_df)


    def test_get_roster_stats(self):
        regular_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Team', "Roster", "Roster_Stats", "Regular_Stat", "2020") 
        playoff_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Team', "Roster", "Roster_Stats", "Playoff_Stat", "2020")
    
        # Regular Player Stats
        regular_advanced = os.path.join(regular_path, "Advanced", "2020season_DAL_Regular_Advanced.csv")
        regular_pergame = os.path.join(regular_path, "Per_Game", "2020season_DAL_Regular_Per_Game.csv")
        regular_perminute = os.path.join(regular_path, "Per_Minute", "2020season_DAL_Regular_Per_Minute.csv")
        regular_perposs = os.path.join(regular_path, "Per_Poss", "2020season_DAL_Regular_Per_Poss.csv")
        regular_totals = os.path.join(regular_path, "Totals", "2020season_DAL_Regular_Totals.csv")

        # Playoff Stats
        playoff_advanced = os.path.join(playoff_path, "Advanced", "2020season_DAL_Playoffs_Advanced.csv")
        playoff_pergame = os.path.join(playoff_path, "Per_Game", "2020season_DAL_Playoffs_Per_Game.csv")
        playoff_perminute = os.path.join(playoff_path, "Per_Minute", "2020season_DAL_Playoffs_Per_Minute.csv")
        playoff_perposs = os.path.join(playoff_path, "Per_Poss", "2020season_DAL_Playoffs_Per_Poss.csv")
        playoff_totals = os.path.join(playoff_path, "Totals", "2020season_DAL_Playoffs_Totals.csv")

        # Regular Advanced
        df_regular_advanced = get_roster_stats("DAL", 2020 , False, 'Advanced')
        expected_df_regular_advanced = pd.read_csv(regular_advanced)
        
        # Regular Per_Game
        df_regular_pergame = get_roster_stats("DAL", 2020 , False, 'Per_Game')
        expected_df_regular_pergame = pd.read_csv(regular_pergame)

        # Regular Per_Minute
        df_regular_perminute = get_roster_stats("DAL", 2020 , False, 'Per_Minute')
        expected_df_regular_perminute = pd.read_csv(regular_perminute)

        # Regular Per_Poss
        df_regular_perposs = get_roster_stats("DAL", 2020 , False, 'Per_Poss')
        expected_df_regular_perposs = pd.read_csv(regular_perposs)

        # Regular Totals
        df_regular_totals = get_roster_stats("DAL", 2020 , False, 'Totals')
        expected_df_regular_totals = pd.read_csv(regular_totals)

        # Playoff Advanced
        df_playoff_advanced =  get_roster_stats("DAL", 2020 , True, 'Advanced')
        expected_df_playoff_advanced = pd.read_csv(playoff_advanced)
    
        # Playoff Per_Game
        df_playoff_pergame = get_roster_stats("DAL", 2020 , True, 'Per_Game')
        expected_df_playoff_pergame = pd.read_csv(playoff_pergame)

        # Playoff Per_Minute
        df_playoff_perminute = get_roster_stats("DAL", 2020 , True, 'Per_Minute')
        expected_df_playoff_perminute = pd.read_csv(playoff_perminute)

        # Playoff Per_Poss
        df_playoff_perposs = get_roster_stats("DAL", 2020 , True, 'Per_Poss')
        expected_df_playoff_perposs = pd.read_csv(playoff_perposs)

        # Playoff Totals
        df_playoff_totals = get_roster_stats("DAL", 2020 , True, 'Totals')
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