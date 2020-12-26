import sys 
sys.path.append('\\Users\\Bryan\\Desktop\\Basketball-Stats\\python_scrapers')
import os
import unittest
from Team_Stats_Scraper import get_season_team_stats, get_team_stats

class TestTeamScraper(unittest.TestCase):

    '''
    Test function for get_season_team_stats
    '''
    def get_season_team_stats(self):
        series = get_season_team_stats(2019)
        expected_index = ['G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
        self.assertCountEqual(list(series.index), expected_index)
    
    '''
    Test function for get team_stats
    '''
    def get_team_stats(self):
        series = get_team_stats('BOS', 2018)
        expected_index = ['G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
        self.assertCountEqual(list(series.index), expected_index)

if __name__ == '__main__':
    unittest.main()