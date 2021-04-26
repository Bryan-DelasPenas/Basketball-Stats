import pandas as pd
import sys
from bs4 import BeautifulSoup
from requests import get

from Team_Constants import TEAM_TO_ABBRIVATION, TEAM_ID
from utils import strip_accents
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
        df['Team ABV'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])
    
        # Create a new column for Team ID
        df['Team ID'] = df['Team ABV'].apply(lambda x: TEAM_ID[x])

        # Uppercase only the first letter in the team names 
        df['Team'] = df['Team'].str.title()

        df['Season'] = season

        # Drop all useless stats
        df = df.drop(['Rk','G','MP','FG','FGA','FG%','3P','3PA', '3P%', '2P', '2PA','2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'], axis =1)
        
        # Move team ID to the second element and Season to be the first
        df = df[ ['Team ID'] + [ col for col in df.columns if col != 'Team ID' ] ]
        df = df[ ['Season'] + [ col for col in df.columns if col != 'Season' ] ]
        
    return df 

''' 
Creates a dataframe that returns standings 
'''
def get_standings(season, data_format = 'standard'):

    # Converts data_format into lower case string 
    data_format = data_format.lower()
   
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
                df_east['Team ABV'] = df_east['Eastern Conference'].apply(lambda x: TEAM_TO_ABBRIVATION[x])
                df_west['Western Conference'] = df_west['Western Conference'].apply(lambda x: x.replace('*', '').upper())
                df_west['Team ABV'] = df_west['Western Conference'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

                # Create a new column for Team ID
                df_east['Team ID'] = df_east['Team ABV'].apply(lambda x: TEAM_ID[x])
                df_west['Team ID'] = df_west['Team ABV'].apply(lambda x: TEAM_ID[x])

                # Create a new column called season
                df_east['Season'] = season
                df_west['Season'] = season

                # Moves the TEAM column to be the first element
                df_east = df_east[ ['Team ABV'] + [ col for col in df_east.columns if col != 'Team ABV' ] ]
                df_east = df_east[ ['Team ID'] + [ col for col in df_east.columns if col != 'Team ID' ] ]
                df_east = df_east[ ['Season'] + [ col for col in df_east.columns if col != 'Season' ] ]
                df_west = df_west[ ['Team ABV'] + [ col for col in df_west.columns if col != 'Team ABV' ] ]
                df_west = df_west[ ['Team ID'] + [ col for col in df_west.columns if col != 'Team ID' ] ]
                df_west = df_west[ ['Season'] + [ col for col in df_west.columns if col != 'Season' ] ]

                # Change column to team name
                df_east = df_east.rename(columns={'Eastern Conference': 'Team'})
                df_west = df_west.rename(columns={'Western Conference': 'Team'})

                # Upper case first letter of word
                df_east['Team'] = df_east['Team'].apply(lambda x: x.title())
                df_west['Team'] = df_west['Team'].apply(lambda x: x.title())

                df_east = df_east.astype({'W': int, 'L': int, 'W/L%':float, 'PS/G':float, 'PA/G': float, 'SRS':float})
                df_west = df_west.astype({'W': int, 'L': int, 'W/L%':float, 'PS/G':float, 'PA/G': float, 'SRS':float})

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
                df_east['Team ABV'] = df_east['Eastern Conference'].apply(lambda x: TEAM_TO_ABBRIVATION[x])
                df_west['Western Conference'] = df_west['Western Conference'].apply(lambda x: x.replace('*', '').upper())
                df_west['Team ABV'] = df_west['Western Conference'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

                # Create a new column for Team ID
                df_east['Team ID'] = df_east['Team ABV'].apply(lambda x: TEAM_ID[x])
                df_west['Team ID'] = df_west['Team ABV'].apply(lambda x: TEAM_ID[x])

                # Create a new column called season
                df_east['Season'] = season
                df_west['Season'] = season

                # Rearrange columns
                df_east = df_east[ ['Team ABV'] + [ col for col in df_east.columns if col != 'Team ABV' ] ]
                df_east = df_east[ ['Team ID'] + [ col for col in df_east.columns if col != 'Team ID' ] ]
                df_east = df_east[ ['Season'] + [ col for col in df_east.columns if col != 'Season' ] ]
                df_west = df_west[ ['Team ABV'] + [ col for col in df_west.columns if col != 'Team ABV' ] ]
                df_west = df_west[ ['Team ID'] + [ col for col in df_west.columns if col != 'Team ID' ] ]
                df_west = df_west[ ['Season'] + [ col for col in df_west.columns if col != 'Season' ] ]
                
                # Change column to team name
                df_east = df_east.rename(columns={'Eastern Conference': 'Team'})
                df_west = df_west.rename(columns={'Western Conference': 'Team'})

                # Upper case first letter of word
                df_east['Team'] = df_east['Team'].apply(lambda x: x.title())
                df_west['Team'] = df_west['Team'].apply(lambda x: x.title())

                df_east = df_east.astype({'W': int, 'L': int, 'W/L%':float, 'PS/G':float, 'PA/G': float, 'SRS':float})
                df_west = df_west.astype({'W': int, 'L': int, 'W/L%':float, 'PS/G':float, 'PA/G': float, 'SRS':float})
               
                # Round each entry to the second decimal place
                df_east = df_east.round(2)
                df_west = df_west.round(2)
                
                return df_east, df_west

        else: 
            print('Error 404: Page could not be found')

'''
Creates a dataframe that returns the award voting 
'''
def get_award_voting(season, format = 'MVP'):
    # Get the url of the page for starting purposes, using widgets.sports-references.com
    page = get(f'https://www.basketball-reference.com/awards/awards_{season}.html') 

    # Init the dataframe 
    df = None 

    # Check the status code, if the code is 200, it means the request went through
    if page.status_code == 200: 
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')

        # MVP = Most Valuable Player
        if(format == 'MVP'):
            # Search in the page for 
            table = soup.find('table', attrs={'id':'mvp'})
    
        # ROY = Rookie of the Year
        elif(format == 'ROY'):
            table = soup.find('table', attrs={'id':'roy'})

        # Insert this data into a pandas dataframe
        df = pd.read_html(str(table))[0]

        # Remove muti set for the columns 
        df.columns = ['Rank', 'Player', 'Age', 'Tm', 'First', 'Pts Won', 'Pts Max', 'Share', 'G', 'MP', 'PTS', 'TRB','AST', 'STL', 'BLK', 'FG%', '3P%', 'FT%', 'WS', 'WS/48']
        df = df.drop(['Age', 'First', 'G', 'MP', 'PTS', 'TRB','AST', 'STL', 'BLK', 'FG%', '3P%', 'FT%', 'WS', 'WS/48'], axis =1)
        
        # Remove accented chars in player name 
        df['Player'] = df['Player'].apply(lambda name: strip_accents(name))
        df['Season'] = season
        df['Type'] = format

        # Move team ID to the second element and Season to be the first
        df = df[ ['Player'] + [ col for col in df.columns if col != 'Player' ] ]
        df = df[ ['Tm'] + [ col for col in df.columns if col != 'Tm' ] ]
        df = df[ ['Season'] + [ col for col in df.columns if col != 'Season' ] ]
        
        print(df)
        return df


def main():
    get_award_voting(2020, 'DPOY')

main()