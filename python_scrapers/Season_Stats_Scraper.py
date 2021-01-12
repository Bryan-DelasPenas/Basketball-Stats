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

from Team_Constants import TEAM_TO_ABBRIVATION, TEAM_ID

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
 
        # Create a new column and put the team abbrivations for it 
        df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])
    
        # Create a new column for Team ID
        df['TEAM ID'] = df['TEAM'].apply(lambda x: TEAM_ID[x])

        # Uppercase only the first letter in the team names 
        df['Team'] = df['Team'].str.title()

        df['SEASON'] = season

        # Drop all useless stats
        df = df.drop(['Rk','G','MP','FG','FGA','FG%','3P','3PA', '3P%', '2P', '2PA','2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'], axis =1)
        
        # Move team ID to the second element and Season to be the first
        df = df[ ['TEAM ID'] + [ col for col in df.columns if col != 'TEAM ID' ] ]
        df = df[ ['SEASON'] + [ col for col in df.columns if col != 'SEASON' ] ]
        
    return df 


''' 
Creates a datafrane that returns standings TODO: PUT SEASON ID and TEAM ID
'''
def get_standings(season, data_format = 'standard'):

    # Converts data_format into lower case string 
    data_format = data_format.lower()
    print(data_format)
    if data_format == 'standard':

        page = get(f'https://www.basketball-reference.com/leagues/NBA_{season}_standings.html')
        df_east = None
        df_west = None

        # Check the status code, if the code is 200, it means the request went through
        if page.status_code == 200: 
            soup = BeautifulSoup(page.content, 'html.parser')
            
            # These seasons have a different table format in basketball reference 
            if season >= 2016:
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

                # Create a new column for Team ID
                df_east['TEAM ID'] = df_east['TEAM'].apply(lambda x: TEAM_ID[x])
                df_west['TEAM ID'] = df_west['TEAM'].apply(lambda x: TEAM_ID[x])

                # Create a new column called season
                df_east['SEASON'] = season
                df_west['SEASON'] = season

                # Moves the TEAM column to be the first element
                df_east = df_east[ ['TEAM'] + [ col for col in df_east.columns if col != 'TEAM' ] ]
                df_east = df_east[ ['TEAM ID'] + [ col for col in df_east.columns if col != 'TEAM ID' ] ]
                df_east = df_east[ ['SEASON'] + [ col for col in df_east.columns if col != 'SEASON' ] ]
                df_west = df_west[ ['TEAM'] + [ col for col in df_west.columns if col != 'TEAM' ] ]
                df_west = df_west[ ['TEAM ID'] + [ col for col in df_west.columns if col != 'TEAM ID' ] ]
                df_west = df_west[ ['SEASON'] + [ col for col in df_west.columns if col != 'SEASON' ] ]

                # Drop Team 
                df_east = df_east.drop(['Eastern Conference'], axis=1)
                df_west = df_west.drop(['Western Conference'], axis=1)

                # Round each entry to the second decimal place
                df_east = df_east.round(2)
                df_west = df_west.round(2)

                return df_east, df_west

            # Seasons between and including 2015 and 1980
            elif season <= 2015 and season >= 1980:
                table_east = soup.find('table', attrs={'id': 'divs_standings_E'})
                table_west = soup.find('table', attrs={'id': 'divs_standings_W'})
                
                # Create a dataframe for both east and west conference
                df_east = pd.read_html(str(table_east))[0]
                df_west = pd.read_html(str(table_west))[0]
                
                # Removes divisions in the index
                df_east = df_east[~df_east['Eastern Conference'].isin(['Atlantic Division', 'Central Division','Southeast Division'])] 
                df_west = df_west[~df_west['Western Conference'].isin(['Northwest Division', 'Pacific Division', 'Southwest Division', 'Midwest Division'])]

                 # Format the team column to remove * and upper cases it and Create a new column called 'TEAM' convert it to the constant from Team_Constants.py
                df_east['Eastern Conference'] = df_east['Eastern Conference'].apply(lambda x: x.replace('*', '').upper())
                df_east['TEAM'] = df_east['Eastern Conference'].apply(lambda x: TEAM_TO_ABBRIVATION[x])
                df_west['Western Conference'] = df_west['Western Conference'].apply(lambda x: x.replace('*', '').upper())
                df_west['TEAM'] = df_west['Western Conference'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

                # Create a new column for Team ID
                df_east['TEAM ID'] = df_east['TEAM'].apply(lambda x: TEAM_ID[x])
                df_west['TEAM ID'] = df_west['TEAM'].apply(lambda x: TEAM_ID[x])

                # Create a new column called season
                df_east['SEASON'] = season
                df_west['SEASON'] = season

                # Moves the TEAM column to be the first element
                df_east = df_east[ ['TEAM'] + [ col for col in df_east.columns if col != 'TEAM' ] ]
                df_east = df_east[ ['TEAM ID'] + [ col for col in df_east.columns if col != 'TEAM ID' ] ]
                df_east = df_east[ ['SEASON'] + [ col for col in df_east.columns if col != 'SEASON' ] ]
                df_west = df_west[ ['TEAM'] + [ col for col in df_west.columns if col != 'TEAM' ] ]
                df_west = df_west[ ['TEAM ID'] + [ col for col in df_west.columns if col != 'TEAM ID' ] ]
                df_west = df_west[ ['SEASON'] + [ col for col in df_west.columns if col != 'SEASON' ] ]
                
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
        print('Nice')
        select = 'div_expanded_standings'
        page = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season}_standings.html&div={select}')
        df = None

        # Check the status code, if the code is 200, it means the request went through
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
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
            
            # For any other season, 2006 - 2019 excluding 2012
            elif season != 2012 and (season >= 2007 and season < 2020): 
                
                # Dataframe's columns for 2006 - 2019 seasons
                df.columns = ['Rk', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 
                           'SOUTHEASTERN DIVISION RECORD', 'NORTHWESTERN DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'SOUTHWESTERN DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD',
                           '3 POINT MARGIN', '10 POINT MARGIN', 'OCT RECORD', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']

            # Lock out stars in DEC
            elif season == 2012:
                 # Dataframe's columns for 2006 - 2019 seasons
                df.columns = ['Rk', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 
                           'SOUTHEASTERN DIVISION RECORD', 'NORTHWESTERN DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'SOUTHWESTERN DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD',
                           '3 POINT MARGIN', '10 POINT MARGIN', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']

            # Started in Nov
            elif season == 2005 or season == 2006: 
                df.columns = ['Rk', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 
                           'SOUTHEASTERN DIVISION RECORD', 'NORTHWESTERN DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'SOUTHWESTERN DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD',
                           '3 POINT MARGIN', '10 POINT MARGIN', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']

            # Started in Nov 
            elif season == 2000:            
                df.columns = ['Rk', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 
                            'MIDWESTERM DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD',
                            '3 POINT MARGIN', '10 POINT MARGIN', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']

            # Due to lock out teams played until May
            elif season == 1999:
                df.columns = ['Rk', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 
                            'MIDWESTERM DIVISION RECORD', 'PACIFIC DIVISION RECORD', '3 POINT MARGIN', '10 POINT MARGIN', 'FEB RECORD', 'MAR RECORD', 'APR RECORD', 'MAY RECORD']
            
            # Season started on Nov these seasons
            elif season >= 1988 and season <= 1997:
                 df.columns = ['Rk', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 
                            'MIDWESTERM DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD',
                            '3 POINT MARGIN', '10 POINT MARGIN', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']

            # 1980 and 1981 both end at March
            elif season == 1980 or season == 1981:
                df.columns = ['Rk', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 
                            'MIDWESTERM DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD',
                            '3 POINT MARGIN', '10 POINT MARGIN', 'OCT RECORD', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD']

            # Every other team
            else:
                df.columns = ['Rk', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 
                            'MIDWESTERM DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD',
                            '3 POINT MARGIN', '10 POINT MARGIN', 'OCT RECORD', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']

            # Format the team column to remove * and upper cases it and Create a new column called 'TEAM' convert it to the constant from Team_Constants.py
            df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
            df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

            # Create a new column for Team ID
            df['TEAM ID'] = df['TEAM'].apply(lambda x: TEAM_ID[x])

            # Create a new column called season
            df['SEASON'] = season

            # Moves the TEAM column to be the thrid element and TEAM_ID to be second and SEASON to be first
            df = df[ ['TEAM'] + [ col for col in df.columns if col != 'TEAM' ] ]
            df = df[ ['TEAM ID'] + [ col for col in df.columns if col != 'TEAM ID' ] ]
            df = df[ ['SEASON'] + [ col for col in df.columns if col != 'SEASON' ] ]

            # Drop rk(Rank) and Team 
            df = df.drop(['Rk', 'Team'], axis=1)
            
            # Round each entry to the second decimal place
            df = df.round(2)

            return df
        else: 
            print('Error 404: Page could not be found')

    elif data_format == 'team_vs_team':
        select = 'div_team_vs_team'
        page = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_2020_standings.html&div={select}')
        df = None

        # Check the status code, if the code is 200, it means the request went through
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            table = soup.find('table')
            df = pd.read_html(str(table))[0]
             
             # Format the team column to remove * and upper cases it and Create a new column called 'TEAM' convert it to the constant from Team_Constants.py
            df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
            df['TEAM'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

            # Create a new column for Team ID
            df['TEAM ID'] = df['TEAM'].apply(lambda x: TEAM_ID[x])

            # Create a new column called season
            df['SEASON'] = season

            # Moves the TEAM column to be the thrid element and TEAM_ID to be second and SEASON to be first
            df = df[ ['TEAM'] + [ col for col in df.columns if col != 'TEAM' ] ]
            df = df[ ['TEAM ID'] + [ col for col in df.columns if col != 'TEAM ID' ] ]
            df = df[ ['SEASON'] + [ col for col in df.columns if col != 'SEASON' ] ]

            # Drop rk(Rank) and Team 
            df = df.drop(['Rk', 'Team'], axis=1)
            
            # Round each entry to the second decimal place
            df = df.round(2)

            return df
       
        else: 
            print('Error 404: Page could not be found')



