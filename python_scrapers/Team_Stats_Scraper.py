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

'''
Creates a dataframe that returns the teams name 
'''
def get_team_name(season):
    # Get the url of the page for starting purposes, using widgets.sports-references.com
    page = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season}.html&div=div_team-stats-per_poss') 

    # Init the dataframe 
    df = None 

    # Check the status code, if the code is 200, it means the request went through
    if page.status_code == 200: 
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')
        
        # Insert this data into a pandas dataframe
        df = pd.read_html(str(table))[0]
        
        # Remove * from playoff teams 
        df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
 
        # Uppercase only the first letter in the team names 
        df = df['Team'].str.title()
    return df 

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

        # Converts birth date to datetime 
        df['BIRTH_DATE'] = df['BIRTH_DATE'].apply(lambda x: pd.to_datetime(x))
        df['NATIONALITY'] = df['NATIONALITY'].str.upper()
        
        return df

'''
Creates a dataframe of everyteam's teams for the season
'''
def get_season_team_stats(season, data_format ='PER_GAME'): 
    
    # This is the format for the data, 
    # 3 options: Total, Per game and Per poss
    if data_format=='TOTAL':
        select = 'div_team-stats-base'
    
    elif data_format=='PER_GAME':
        select = 'div_team-stats-per_game'
    
    elif data_format=='PER_POSS':
        select = 'div_team-stats-per_poss'

    # Get the url of the page for starting purposes, using widgets.sports-references.com
    page = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season}.html&div={select}') 

    # Init the dataframe 
    df = None 

    # Check the status code, if the code is 200, it means the request went through
    if page.status_code == 200: 
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')
        
        # Insert this data into a pandas dataframe
        df = pd.read_html(str(table))[0]
        
        # Since total and per game have league averages we have to add this segement of code 
        if(data_format != 'PER_POSS'):
            league_avg_index = df[df['Team']=='League Average'].index[0]
            df = df[:league_avg_index]
        else:
            pass
        # Format the team column to remove * and upper cases it and Create a new column called 'TEAM' convert it to the constant from Team_Constants.py
        df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
        df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

        # Moves the TEAM column to be the first element
        df = df[ ['TEAM'] + [ col for col in df.columns if col != 'TEAM' ] ]

        # Drop rk(Rank) and Team 
        df = df.drop(['Rk', 'Team'], axis=1)
       
    return df
    
'''
Creates a dataframe for a specific team stats, overloaded function for get_season_stats. TODO: Rewrite this function
'''
def get_team_stats(team,season, data_format ='PER_GAME'): 
    
    # This is the format for the data, 
    # 3 options: Total, Per game and Per poss
    if data_format=='TOTAL':
        select = 'div_team-stats-base'
    
    elif data_format=='PER_GAME':
        select = 'div_team-stats-per_game'
    
    elif data_format=='PER_POSS':
        select = 'div_team-stats-per_poss'

    # Get the url of the page for starting purposes, using widgets.sports-references.com
    page = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season}.html&div={select}') 
    
    # Init the dataframe 
    df = None 

    # Check the status code, if the code is 200, it means the request went through
    if page.status_code == 200: 
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')
        
        # Insert this data into a pandas dataframe
        df = pd.read_html(str(table))[0]
        
        # Since total and per game have league averages we have to add this segement of code 
        if(data_format != 'PER_POSS'):
            league_avg_index = df[df['Team']=='League Average'].index[0]
            df = df[:league_avg_index]
        
        else:
            pass
        
        # Format the team column to remove * and upper cases it and Create a new column called 'TEAM' convert it to the constant from Team_Constants.py
        df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
        df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

        # Moves the TEAM column to be the first element
        df = df[ ['TEAM'] + [ col for col in df.columns if col != 'TEAM' ] ]

        # Drop rk(Rank) and Team 
        df = df.drop(['Rk', 'Team'], axis=1)
        
        # Adds a new column called season which should be the season parameter minus 1 - season parameter
        df.loc[:, 'SEASON'] = f'{season - 1} - {str(season)[2:]}'
        
        # Look for the team you pass as a parameter
        df = df[df['TEAM'] == team]
        
        # Moves the TEAM column to be the first element
        df = df[ ['SEASON'] + [ col for col in df.columns if col != 'SEASON' ] ]

        return df

'''
Creates a dataframe that contains the stats of teams' oppoenets 
'''
def get_opp_stats(season, data_format ='PER_GAME'):

    # This is the format for the data, 
    # 3 options: Total, Per game and Per poss
    if data_format=='TOTAL':
        select = 'div_opponent-stats-base'
    
    elif data_format=='PER_GAME':
        select = 'div_opponent-stats-per_game'
    
    elif data_format=='PER_POSS':
        select = 'div_opponent-stats-per_poss'

    r = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season}.html&div={select}')
    df = None

    # Check the status code, if the code is 200, it means the request went through
    if r.status_code == 200: 
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table')
    
        # Insert this data into a pandas dataframe
        df = pd.read_html(str(table))[0]
        
        # Since total and per game have league averages we have to add this segement of code 
        if(data_format != 'PER_POSS'):
            league_avg_index = df[df['Team']=='League Average'].index[0]
            df = df[:league_avg_index]
        
        else:
            pass
        
        # Format the team column to remove * and upper cases it and Create a new column called 'TEAM' convert it to the constant from Team_Constants.py
        df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
        df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

        # Moves the TEAM column to be the first element
        df = df[ ['TEAM'] + [ col for col in df.columns if col != 'TEAM' ] ]

        # Drop rk(Rank) and Team 
        df = df.drop(['Rk', 'Team'], axis=1)
        
        # Change columns name to add OPP 
        df.columns = list(map(lambda x: 'OPP_'+x, list(df.columns)))
        df.rename(columns={'OPP_TEAM': 'TEAM'}, inplace=True)
        
        return df 

'''
Creates a dataframe of a teams players opp's averages TODO: Rewrite this function 
'''
def get_team_opp_stats(team, season, data_format = 'PER_GAME'):
    # This is the format for the data, 
    # 3 options: Total, Per game and Per poss
    if data_format=='TOTAL':
        select = 'div_opponent-stats-base'
    
    elif data_format=='PER_GAME':
        select = 'div_opponent-stats-per_game'
    
    elif data_format=='PER_POSS':
        select = 'div_opponent-stats-per_poss'

    r = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season}.html&div={select}')
    df = None

    # Check the status code, if the code is 200, it means the request went through
    if r.status_code == 200: 
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table')
    
        # Insert this data into a pandas dataframe
        df = pd.read_html(str(table))[0]
        
        # Since total and per game have league averages we have to add this segement of code 
        if(data_format != 'PER_POSS'):
            league_avg_index = df[df['Team']=='League Average'].index[0]
            df = df[:league_avg_index]
        
        else:
            pass
        
        # Format the team column to remove * and upper cases it and Create a new column called 'TEAM' convert it to the constant from Team_Constants.py
        df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
        df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

        # Moves the TEAM column to be the first element
        df = df[ ['TEAM'] + [ col for col in df.columns if col != 'TEAM' ] ]

        # Drop rk(Rank) and Team 
        df = df.drop(['Rk', 'Team'], axis=1)
        
        # Adds a new column called season which should be the season parameter minus 1 - season parameter
        df.loc[:, 'SEASON'] = f'{season - 1} - {str(season)[2:]}'
        
        # Look for the team you pass as a parameter
        df = df[df['TEAM'] == team]
        
        # Moves the TEAM column to be the first element
        df = df[ ['SEASON'] + [ col for col in df.columns if col != 'SEASON' ] ]

        # Change columns name to add OPP 
        df.columns = list(map(lambda x: 'OPP_'+x, list(df.columns)))
        df.rename(columns={'OPP_TEAM': 'TEAM'}, inplace=True)
        
        return df 

def main():
    print(get_team_opp_stats('GSW',2019))

main()