#############################################################################
# File:   Team_Stats_Scraper.py 
# Author: Bryan Delas Penas 
# Email:  bryan.delaspenas0405@gmail.com
# Date:   12/17/20 
# Description: 
# This program is going to scrap information from https://www.basketball-reference.com/
# It is going to scrape the team data based on the season and output it into a txt file 
#
# Format: 
# Season Year, NBA TEAM NAME, Games played, Minutes played, Field goals, Field goals attempt, Field gold percentage,  
# 3 point field goals, 3 points attempt, 3 point pecentage, 2 points field goals, 2 point field goal attempt, 2 point percentage 
# TODO: Work on scraping 

import pandas as pd
import sys
from bs4 import BeautifulSoup
from requests import get

from Team_Constants import TEAM_TO_ABBRIVATION

def get_team_stats(season, data_format ='PER_GAME'): 
    
    # This is the format for the data, 
    # 3 options: Total, Per game and Per poss
    if data_format=='TOTAL':
        select = 'div_team-stats-base'
    elif data_format=='PER_GAME':
        select = 'div_team-stats-per_game'
    elif data_format=='PER_POSS':
        select = 'div_team-stats-per_poss'

    # Get the url of the page for starting purposes, using widgets.sports-references.com
    page = r = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season}.html&div={select}') 

    # Init the dataframe 
    df = None 

    # Check the status code, if the code is 200, it means the request went through
    if page.status_code == 200: 
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table')
        
        # Insert this data into a pandas dataframe
        df = pd.read_html(str(table))[0]
        league_avg_index = df[df['Team']=='League Average'].index[0]
        df = df[:league_avg_index]

        # Format the team column to remove * and upper cases it and Create a new column called 'TEAM' convert it to the constant from Team_Constants.py
        df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
        df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

        # Moves the TEAM column to be the first element
        df = df[ ['TEAM'] + [ col for col in df.columns if col != 'TEAM' ] ]

        # Drop rk(Rank) and Team 
        df = df.drop(['Rk', 'Team'], axis=1)
 
    return df

