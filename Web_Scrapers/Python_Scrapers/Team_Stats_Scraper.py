import pandas as pd
import numpy as np
import sys
from bs4 import BeautifulSoup
from requests import get

from Team_Constants import TEAM_TO_ABBRIVATION, TEAM_ID, ABV_TO_TEAM, RIGHT_NAME_DICT, PLAYER_ID
from utils import strip_accents, translate


'''
Create a dataframe for team roster
'''
def get_roster(team, season, orginal = False):
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
        df.columns = ['Number', 'Player', 'Pos', 'Height', 'Weight', 'Birth Date', 'Nationality', 'Experience', 'College']

        # Create a new column called team
        df['Team ABV'] = team
        
        # Create a new column called season
        df['Season'] = season
        
        # Create a new column named team
        df['Team'] = team
        df['Team'] = df['Team'].apply(lambda x:ABV_TO_TEAM[x].title())

        # Create a new column for Team ID
        df['Team ID'] = df['Team ABV'].apply(lambda x: TEAM_ID[x])

        # Removes accents 
        df['Player'] = df['Player'].apply(lambda name: strip_accents(name))

        # Rearranges the elements
        df = df[ ['Team'] + [ col for col in df.columns if col != 'Team' ] ]
        df = df[ ['Team ABV'] + [ col for col in df.columns if col != 'Team ABV' ] ]
        df = df[ ['Team ID'] + [ col for col in df.columns if col != 'Team ID' ] ]
        df = df[ ['Season'] + [ col for col in df.columns if col != 'Season' ] ]

        # Converts birth date to datetime 
    
        df['Nationality'] = df['Nationality'].str.upper()
        
        players = df.values.tolist()
      
        # Iterate through Players 
        if(orginal == False):
            for x in range(len(players)):
                        
                name_tuple = (players[x][5], players[x][9])
                    
                if(name_tuple in RIGHT_NAME_DICT):
                    
                    players[x][5] = RIGHT_NAME_DICT[name_tuple]
              
        # Remake the dataframe with proper names
        final_df = pd.DataFrame(players, columns=['Season', 'Team ID', 'Team ABV', 'Team', 'Number', 'Player', 'Pos', 'Height', 'Weight', 'Birth Date', 
                                                  'Nationality', 'Experience', 'College'])

        final_df['Player ID'] = final_df['Player'].apply(lambda x: PLAYER_ID[x])

        # Rearranges the elements
        final_df = final_df[ ['Team'] + [ col for col in  final_df.columns if col != 'Team' ] ]
        final_df = final_df[ ['Team ABV'] + [ col for col in  final_df.columns if col != 'Team ABV' ] ]
        final_df = final_df[ ['Player ID'] + [ col for col in  final_df.columns if col != 'Player ID' ] ]
        final_df = final_df[ ['Team ID'] + [ col for col in  final_df.columns if col != 'Team ID' ] ]
        final_df = final_df[ ['Season'] + [ col for col in  final_df.columns if col != 'Season' ] ]
        
        return final_df

    else: 
        print('Error 404: Page could not be found')

'''
Creates a dataframe of everyteam's teams for the season
'''
def get_team_stats(season, data_format ='PER_GAME'): 
    
    # This is the format for the data, 
    # 3 options: Total, Per game and Per poss
    data_format = data_format.upper()

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
        df['Team ABV'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

        # Create a new column for Team ID
        df['Team ID'] = df['Team ABV'].apply(lambda x: TEAM_ID[x])

        # Create a new column called season
        df['Season'] = season

        # Changes back Team column to title format 
        df['Team'] = df['Team'].apply(lambda x: x.title())

        # Moves the TEAM column to be the thrid element and TEAM_ID to be second and SEASON to be first
        df = df[ ['Team ABV'] + [ col for col in df.columns if col != 'Team ABV' ] ]
        df = df[ ['Team ID'] + [ col for col in df.columns if col != 'Team ID' ] ]
        df = df[ ['Season'] + [ col for col in df.columns if col != 'Season' ] ]

        # Drop rk(Rank) and Team 
        df = df.drop(['Rk'], axis=1)
        
        # Rounds every entry to two decimal places
        df = df.round(2)

        return df
 
'''
Creates a dataframe that contains the stats of teams' oppenets 
'''
def get_opp_stats(season, data_format ='PER_GAME'):

    data_format = data_format.upper()

    # This is the format for the data, 
    # 3 options: Total, Per game and Per poss
    if data_format=='TOTAL':
        select = 'div_opponent-stats-base'
    
    elif data_format=='PER_GAME':
        select = 'div_opponent-stats-per_game'
    
    elif data_format=='PER_POSS':
        select = 'div_opponent-stats-per_poss'

    page = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season}.html&div={select}')
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
        df['Team ABV'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

        # Change back team to title format 
        df['Team'] = df['Team'].apply(lambda x: x.title())
        
        # Create a new column for Team ID
        df['Team ID'] = df['Team ABV'].apply(lambda x: TEAM_ID[x])

        # Create a new column called season
        df['Season'] = season

        # Moves the TEAM column to be the thrid element and TEAM_ID to be second and SEASON to be first
        df = df[ ['Team ABV'] + [ col for col in df.columns if col != 'Team ABV' ] ]
        df = df[ ['Team ID'] + [ col for col in df.columns if col != 'Team ID' ] ]
        df = df[ ['Season'] + [ col for col in df.columns if col != 'Season' ] ]
        
        # Drop rank and team from the dataframe
        df = df.drop(['Rk'], axis=1)
        
        # Rounds every entry to two decimal places
        df = df.round(2)

        return df

'''
Create a dataframe for team's misc stats 
'''
def get_team_misc(season):
    # Get the url of the page for starting purposes,
    page = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season}.html&div=div_misc_stats')
    
    # Init the dataframe 
    df = None
    
    # Check the status code, if the code is 200, it means the request went through
    if page.status_code == 200: 
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')

        # Insert this data into a pandas dataframe
        df = pd.read_html(str(table))[0]
        
        df.columns = ['Rk', 'Team', 'Age','W','L','PW','PL', 'MOV', 'SOS', 'SRS', 'ORtg','DRtg', 'NRtg','Pace', 'FTr', '3PAr', 'TS%', 
                      'eFG%', 'TOV%', 'ORB%', 'FT/FGA', 'eFG%', 'TOV%', 'DRB%', 'FT/FGA', 'Arena', 'Attend.', 'Attend./G']
        
        league_avg_index = df[df['Team']=='League Average'].index[0]
        df = df[:league_avg_index]

        # Format the team column to remove * and upper cases it and Create a new column called 'TEAM' convert it to the constant from Team_Constants.py
        df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
        df['Team ABV'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])

        # Create a new column for Team ID
        df['Team ID'] = df['Team ABV'].apply(lambda x: TEAM_ID[x])

        # Change back into title format
        df['Team'] = df['Team'].str.title()

        # Create a new column called season
        df['Season'] = season
 
        # Moves the TEAM column to be the thrid element and TEAM_ID to be second and SEASON to be first
        df = df[ ['Team ABV'] + [ col for col in df.columns if col != 'Team ABV' ] ]
        df = df[ ['Team ID'] + [ col for col in df.columns if col != 'Team ID' ] ]
        df = df[ ['Season'] + [ col for col in df.columns if col != 'Season' ] ]

        # For some reason, there is duplicate column names, this code removes it 
        df = df.loc[:,~df.columns.duplicated()]

        # Drop Not needed columns 
        df = df.drop(['Rk', 'eFG%', 'TOV%', 'FT/FGA'], axis=1)

        # Rounds every entry to two decimal places
        df = df.round(2)

        return df

'''
Create dataframe for team advanced stats
'''
def get_team_advanced(team, season):
    
    # Get the url of the page for starting purposes
    page = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fteams%2F{team}%2F&div=div_{team}')
    
    # Init the dataframe 
    df = None
    
    # Check the status code, if the code is 200, it means the request went through
    if page.status_code == 200: 
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')

        # Insert this data into a pandas dataframe
        df = pd.read_html(str(table))[0]

        # Drop columns where all values are missing 
        df = df.dropna(axis='columns',how='all')

        # Drop Lg column
        df = df.drop(['Lg'], axis=1)
        
        # Lamba function to get the proper end year
        df['Season'] = df['Season'].apply(lambda x: remove_char(x, 2) if len(x) != 4 else x)
        df['Season'] = df['Season'].apply(lambda x: remove_char(x, 2) if len(x) != 4 else x)
        df['Season'] = df['Season'].apply(lambda x: remove_char(x, 2) if len(x) != 4 else x)
        df['Season'] = df['Season'].replace(['1900'], '2000')
        
        df['Season'] = df['Season'].apply(pd.to_numeric)

        # Drop players that are didn't play at 1980
        df_new = df[df['Season'] < 1980].index
        df.drop(df_new, inplace = True)
      
        # Apply changes to team and adds TEAM column to df
        df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
        df['Team ABV'] = df['Team'].apply(lambda x: TEAM_TO_ABBRIVATION[x])
        
        # Create a new column for Team ID
        df['Team ID'] = df['Team ABV'].apply(lambda x: TEAM_ID[x])

        # Change back into title format
        df['Team'] = df['Team'].str.title()

        # Moves the TEAM column to be the thrid element and TEAM_ID to be second and SEASON to be first
        df = df[ ['Team ABV'] + [ col for col in df.columns if col != 'Team ABV' ] ]
        df = df[ ['Team ID'] + [ col for col in df.columns if col != 'Team ID' ] ]
        df = df[ ['Season'] + [ col for col in df.columns if col != 'Season' ] ]
        
        # Looks for the season you want   
        final_df = df[df['Season']==(season)]
       
        # Rounds every entry to two decimal places
        final_df = final_df.round(2)
        final_df = final_df.drop(["Top WS"], axis=1)
        final_df = final_df.reset_index(drop=True)
        return final_df

'''
Helper Function that changes season_start-season_end to season_end
'''
def remove_char(string, postion):
    # Characters before the i-th indexed 
    # is stored in a variable a 
    a = string[ : postion]  
      
    # Characters after the nth indexed 
    # is stored in a variable b 
    b = string[postion + 1: ] 
      
    # Returning string after removing 
    # nth indexed character. 
    return a + b 

def main():
    print(get_team_advanced("BOS", 2000))
main()