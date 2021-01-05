#############################################################################
# File:   Season_Stats_Scraper.py 
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

        # Rounds every entry to two decimal places
        df = df.round(2)

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
        
        # Rounds every entry to two decimal places
        df = df.round(2)

        return df 

''' 
Creates a datafrane that returns standings 
'''
def get_standings(season, data_format = 'standard'):

    # Converts data_format into lower case string 
    data_format = data_format.lower()
    
    if data_format == 'standard':

        r = get(f'https://www.basketball-reference.com/leagues/NBA_{season}_standings.html')
        df_east = None
        df_west = None

        # Check the status code, if the code is 200, it means the request went through
        if r.status_code == 200: 
            soup = BeautifulSoup(r.content, 'html.parser')

            # Search for eastern conference and western conference table
            table_east = soup.find('table', attrs={'id': 'confs_standings_E'})
            table_west = soup.find('table', attrs={'id': 'confs_standings_W'} )
            
            # Create a dataframe for both east and west conference
            df_east = pd.read_html(str(table_east))[0]
            df_west = pd.read_html(str(table_west))[0]
            
            # Format the team column to remove * and upper cases it and Create a new column called 'TEAM' convert it to the constant from Team_Constants.py
            df_east['Eastern Conference'] = df_east['Eastern Conference'].apply(lambda x: x.replace('*', '').upper())
            df_east['TEAM'] = df_east['Eastern Conference'].apply(lambda x: TEAM_TO_ABBRIVATION[x])
            df_west['Western Conference'] = df_west['Western Conference'].apply(lambda x: x.replace('*', '').upper())
            df_west['TEAM'] = df_west['Western Conference'].apply(lambda x: TEAM_TO_ABBRIVATION[x])
            
            # Moves the TEAM column to be the first element
            df_east = df_east[ ['TEAM'] + [ col for col in df_east.columns if col != 'TEAM' ] ]
            df_west = df_west[ ['TEAM'] + [ col for col in df_west.columns if col != 'TEAM' ] ]

            # Drop Team 
            df_east = df_east.drop(['Eastern Conference'], axis=1)
            df_west = df_west.drop(['Western Conference'], axis=1)

            # Round each entry to the second decimal place
            df_east = df_east.round(2)
            df_west = df_west.round(2)

            return df_east, df_west
        else: 
            print('Error 404: Page could not be found')

    elif data_format == 'expanded_standings':
        select = 'div_expanded_standings'
        r = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_2020_standings.html&div={select}')
        df = None

        # Check the status code, if the code is 200, it means the request went through
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            table = soup.find('table')
            df = pd.read_html(str(table))[0]
            
            # Special case for 2020 due to COVID19
            if season == 2020:
                
                # Dataframe's columns for the 2020 season
                df.columns = ['Rk', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 
                           'SOUTHEASTERN DIVISION RECORD', 'NORTHWESTERN DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'SOUTHWESTERN DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD',
                           '3 POINT MARGIN', '10 POINT MARGIN', 'OCT RECORD', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'JUL RECORD', 'AUG RECORD']
            
            # Due to COVID19 the season start in DEC
            elif season == 2021:
                
                # Dataframe's columns for the 2021 season
                df.columns = ['Rk', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 
                           'SOUTHEASTERN DIVISION RECORD', 'NORTHWESTERN DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'SOUTHWESTERN DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD',
                           '3 POINT MARGIN', '10 POINT MARGIN',  'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD']
            
            # For any other season, 1980 - 2019
            else: 
                
                # Dataframe's columns for 1980 - 2019 seasons
                df.columns = ['Rk', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 
                           'SOUTHEASTERN DIVISION RECORD', 'NORTHWESTERN DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'SOUTHWESTERN DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD',
                           '3 POINT MARGIN', '10 POINT MARGIN', 'OCT RECORD', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']
                        
            # Format the team column to remove * and upper cases it and Create a new column called 'TEAM' convert it to the constant from Team_Constants.py
            df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
            df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

            # Moves the TEAM column to be the first element
            df = df[ ['TEAM'] + [ col for col in df.columns if col != 'TEAM' ] ]

            # Drop rk(Rank) and Team 
            df = df.drop(['Rk', 'Team'], axis=1)
            
            # Round each entry to the second decimal place
            df = df.round(2)

            return df
        else: 
            print('Error 404: Page could not be found')

    elif data_format == 'team_vs_team':
        select = 'div_team_vs_team'
        r = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_2020_standings.html&div={select}')
        df = None

        # Check the status code, if the code is 200, it means the request went through
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            table = soup.find('table')
            df = pd.read_html(str(table))[0]
             
            # Format the team column to remove * and upper cases it and Create a new column called 'TEAM' convert it to the constant from Team_Constants.py
            df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
            df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

            # Moves the TEAM column to be the first element
            df = df[ ['TEAM'] + [ col for col in df.columns if col != 'TEAM' ] ]

            # Drop rk(Rank) and Team 
            df = df.drop(['Rk', 'Team'], axis=1)
            
            # Round each entry to the second decimal place
            df = df.round(2)

            return df
       
        else: 
            print('Error 404: Page could not be found')