import pandas as pd
import sys
import os
import pathlib 
from pathlib import Path
from requests import get
import unicodedata, unidecode
import time

sys.path.append(str(pathlib.Path().absolute()) + '\\Python_Scrapers')

from Create_Player_Name import players_names_csv
from get_season_stats import get_season_csv
from get_team_stats import get_team_csv
from get_player_stats import get_player_csv

'''
Run every single scraper 
'''
def main():
    start_time = time.time()
    
    get_season_csv()
    get_team_csv()
    get_player_csv()

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    players_names_csv()
    main()