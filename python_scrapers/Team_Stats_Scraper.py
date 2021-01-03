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
from utils import remove_accents

'''
Create a dataframe for team roster
'''
def get_roster(team, season):
    # Get the url of the page for starting purposes,
    page = get(f'https://www.basketball-reference.com/teams/{team}/{season}.html')

    # Init the dataframe  
    df = None 

    # Check the status code, if the code is 200, it means the request went through
    if page.status_code == 200: 
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')
        
        # Insert this data into a pandas dataframe
        df = pd.read_html(str(table))[0]

        # Column for the dataframe 
        df.columns = ['NUMBER', 'PLAYER', 'POS', 'HEIGHT', 'WEIGHT', 'BIRTH_DATE', 'NATIONALITY', 'EXPERIENCE', 'COLLEGE']

        df['PLAYER'] = df['PLAYER'].apply(lambda name: remove_accents(name, team, season))

        # Converts birth date to datetime 
        df['BIRTH_DATE'] = df['BIRTH_DATE'].apply(lambda x: pd.to_datetime(x))
        df['NATIONALITY'] = df['NATIONALITY'].str.upper()
        
        return df

'''
Creates a dataframe for team's pergame with players 
'''
def get_team_stats(team,season, playoffs = False, data_format = 'PER_GAME'): 
    
    # Check if playoff stats are requested
    if playoffs == True: 
        if data_format =='TOTAL':
            select = 'div_playoffs_total'
        
        elif data_format =='PER_GAME':
            select = 'div_playoffs_per_game'
        
        elif data_format == 'PER_MINUTE':
            select = 'div_playoffs_per_minute'

        elif data_format == 'PER_POSS':
            select = 'div_playoffs_per_poss'

        elif data_format == 'ADVANCED':
            select = 'div_playoffs_advanced'

    else:

        # This is the format for the data, 
        # 6 options: Total, Per game and Per 36 and per 100, advanced, adjusted shooting
        if data_format =='TOTAL':
            select = 'div_totals'
        
        elif data_format =='PER_GAME':
            select = 'div_per_game'
        
        elif data_format == 'PER_MINUTE':
            select = 'div_per_minute'

        elif data_format == 'PER_POSS':
            select = 'div_per_poss'

        elif data_format == 'ADVANCED':
            select = 'div_advanced'

        elif data_format == 'ADJUSTED':
            select = 'div_adj-shooting'
   
    # Get the url of the page for starting purposes, using widgets.sports-references.com
    page = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fteams%2F{team}%2F{season}.html&div={select}') 
    
    # Init the dataframe 
    df = None 

    # Check the status code, if the code is 200, it means the request went through
    if page.status_code == 200: 
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')

        # Check if the table exist example; if playoff is passed as parameter and team didn't make playoffs    
        if(table == None):
            print("Error: table not found")
            return None
        
        else:
            # Insert this data into a pandas dataframe
            df = pd.read_html(str(table))[0]
        
            # This is due to Adjusted table being a muti-index for the columns
            if(data_format == 'ADJUSTED'):
                df.columns = ['Rk', 'PLAYER','AGE','G','MP', ' ','FG','2P','3P','eFG','FT','TS','FTr','3PAr',' ','FG+','2P+','3P+','eFG+','FT+','TS+','FTr+','3PAr+',' ','FG Add','TS Add']
                
                # Drop rows where values are all missing
                df = df.dropna(how='all')

                # Drop columns where all values are missing 
                df = df.dropna(axis='columns',how='all')
        
            else:
                # Changes the second column to players 
                df.columns.values[1] = "PLAYER"
            
            df['PLAYER'] = df['PLAYER'].apply(lambda name: remove_accents(name, team, season))
            df.rename(columns = {'Age': 'AGE'})
            
            # Drop rk(Rank) which is the first column 
            df = df.drop(['Rk'], axis=1)
        
            return df



