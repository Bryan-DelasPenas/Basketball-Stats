import sys 
import pathlib
import pandas as pd
sys.path.append(str(pathlib.Path().absolute()) + '\\Web_Scrapers' +'\\Python_Scrapers')
import os
import unittest
from Team_Stats_Scraper import get_season_team_stats, get_team_stats

class TestTeamScraper(unittest.TestCase):
    #def test_get_roster(self):

    def test_get_roster_stats(self):
        regular_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Team', "Roster", "Roster_Stats", "Regular_Stat", "2020") 
        playoff_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Team', "Roster", "Roster_Stats", "Playoff_Stat", "2020")
    
        regular_advanced_path = os.path.join(regular_path, "Advanced", "")
    
    #def test_get_team_stats(self):

    #def test_get_opp_stats(self):

    #def test_get_team_misc(self):


    #def get_team_advanced(self):

if __name__ == '__main__':
    unittest.main()