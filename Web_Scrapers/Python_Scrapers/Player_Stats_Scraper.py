import pandas as pd
import sys
from bs4 import BeautifulSoup
from requests import get
import unicodedata, unidecode
import os
import pathlib
import time

from Team_Stats_Scraper import remove_char
from Team_Constants import ABV_TO_TEAM, TEAM_ID, RIGHT_NAME_DICT, PLAYER_ID, RIGHT_PLAYER_SUFIX, SPECIAL_NAME_DICT
from utils import translate

'''
Check if string can be converted to ABV
'''
def check_abv(string):
    if(string in ABV_TO_TEAM):
        new_string = ABV_TO_TEAM[string]
        return new_string
    else:
        pass

'''
Checks if team abv is valid
'''
def check_team_id(name):
    
    if(name in TEAM_ID):
        new_num = TEAM_ID[name]
        return new_num
    else:
        pass

'''
Creates a dataframe of player's name active from 1980 - 2020
'''
def get_player_name(letter):
    
    # Get the url of the website
    page = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fplayers%2F{letter}%2F&div=div_players')

    # Init the dataframe
    df = None

    # Check the status code, if the code is 200, it means the request went through
    if page.status_code == 200: 
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')

        # Insert this data into a pandas dataframe
        df = pd.read_html(str(table))[0]
        
        # Column for the dataframe 
        df.columns = ['Player', 'From', 'To','Pos', 'Height', 'Weight', 'Birth_Date','College']
        
        # Drop players that are didn't play at 1980
        df_new = df[df['To'] < 1980].index
        df.drop(df_new, inplace = True)
        
        # Remove * and translate accented char to normal ones
        df['Player'] = df['Player'].apply(lambda x: x.replace('*', ''))
        df['Player'] = df['Player'].apply(lambda name: translate(name))
        
        # Drop unneeded columns
        df = df.drop(['Pos', 'From', 'To','Height', 'Weight', 'College'], axis=1)

        return df

'''
Creates player suffixes for url 
'''
def create_player_suffix(name):

    name = name.replace(".","")
     
    # First name is two letters
    first = name[:2].lower()

    # last name
    last = name.split(' ')[1:]
        
    names = ''.join(last)
    second = ""

    # Check if the length is less than or equal to 5
    if len(names) <= 5:

        # Lower case second example Wall = wall
        second += names[:].lower()

    # Check for names that are greater than 5
    else:

        # Example Doncic becomes Donci
        second += names[:5].lower()

    return second + first

'''
Creates a valid player suffix based on the parameter name and birth date
'''    
def get_player_suffix(name, birth_date):
   
    # Flag for middle name
    middle_flag = False
    name_tuple = (name, birth_date)
 
    # Special Case: for name = Jeff Aryes since he changed his name in 2013
    if(name_tuple in RIGHT_PLAYER_SUFIX):
        sub_name = RIGHT_PLAYER_SUFIX[name_tuple]
        
        # Get the first initial of last name
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'
    
    # Special case, he does not start at 01 but 02
    elif(name == "P.J. Hairston" or name == "Markus Howard" or name == "Xavier Munford" or name == "Cherokee Parks" or name == "Tony Smith"):
        initial = name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(name) + '02.html'
    
    # Special Case: jonesja03 does not exist so it will crash the program
    elif(name == "Jalen Jones" or name == "Jalen Smith"):
        initial = name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(name) + '04.html'
    
    # Special Case: removes ' in names like O'Neil
    elif("'" in name):
        sub_name = name.replace("'","")
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    else:
        
        count = 0
        for character in name:
            if(character.isspace()):
                count += 1

        if count == 2:
            name_list = name.split(' ')
            name = name_list[0] + ' ' +name_list[2]
            middle_flag = True
        elif count == 1:
            pass 

        # Get the first initial of last name
        initial = name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(name) + '01.html'
    
    # Get the url of the player stats
    page = get(f'https://www.basketball-reference.com{suffix}')
    
    #print(suffix)

    # Check if the request can go through 
    while page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        h1 = soup.find('h1', attrs={'itemprop': 'name'})
        h2 = soup.find("span", itemprop='birthDate')
        list1 = []

        if h1:
            page_name = h1.find('span').text
           
            # Removes starting and ending \n
            date = h2.text.strip('\n')

            # Removes middle \n
            date = date.replace('\n','')
            date = date.replace(' ','')
            date = date.strip()

            # This is to get the birthdate of the player 
            final_date = ""

            # Iterate through the string
            for index in range(len(date)):
                
                # Last case of the comma, just adds to the end
                if(index == len(date) - 1):
                    final_date += date[index]
                
                # Check if the char is a comma, adds space after new char
                elif(date[index] == ','):
                    final_date += date[index] + " "
                
                # Check if the current char is not a digit and checks the next iteration if is a digit
                elif(date[index + 1].isdigit() and not date[index].isdigit() ):
                    final_date += date[index] + " "
                
                # Everything else
                else:
                    final_date += date[index]
        
        name_tuple = (name, birth_date)
        # Special Case: For some reason Nene Hilario is just Nene
        if(name_tuple in SPECIAL_NAME_DICT):
            name = SPECIAL_NAME_DICT[name_tuple]

        elif(name_tuple in RIGHT_NAME_DICT):
            name = RIGHT_NAME_DICT[name_tuple]

        # Special Case: Due to having a middle name we remove it early, we add it back here
        if(middle_flag):
            name = ""
            name = name_list[0] + " " + name_list[1] + " " + name_list[2] 
        #print(page_name, ":", name)
        #print(final_date, ":", birth_date)
        # This is for accented characters on the website         
        if(unidecode.unidecode(page_name).lower() == name.lower() and birth_date == final_date):
            return suffix
        
        else:
            suffix = suffix[:-6] + str(int(suffix[-6]) + 1 ) + suffix[-5:]
            
            page = get(f'https://www.basketball-reference.com{suffix}')

    return None
        
'''
Returns csv of player stats from every year they played from 1980
'''
def get_player_stats(name, birth_date,format='PER_GAME', playoffs=False): 
    
    record = lookup(name, birth_date)
    
    # Check if it a valid player and birthdate
    if(record[0][0] == name and record[0][1] == birth_date):
        pass

    else:
        print('Player or birthdate is wrong')
        return None

    # Create suffix for the url
    suffix = get_player_suffix(name, birth_date).replace('/', '%2F')
    #print(suffix)
    # Type of stat you want
    selector = format.lower()
    format = format.upper()
    
    # Check if the stat wanted is playoff
    if playoffs:
        selector = 'playoffs_' + selector

    # Get the url of the table
    page = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url={suffix}&div=div_{selector}')
    
    # Check if the request went through 
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')

        # Check if the table exists
        if(table == None):
            return None
        
        df = pd.read_html(str(table))[0]
        
        if selector == 'adj_shooting':
            df.columns = ['Season', 'Age', 'Team', 'Lg', 'Pos', 'G', 'MP', '', 'Player FG', 'Player 2P', 'Player 3P', 'Player eFG', 'Player FT','Player TS', 'Player FTr', 'Player 3PAr', 
                          '', 'League FG', 'League 2P', 'League 3P', 'League eFG', 'League FT', 'League TS', 'League FTr', 'League 3PAr', '', 'FG+','2P+', '3P+','eFG+','FT+','TS+','FTr+',
                          '3PAr+','','FG Add','TS Add']

            df = df.drop([''],axis=1)
            # Change Nan 3p+ to 0 
            df['3P+'] = df['3P+'].fillna(0)


        df.rename(columns={'Lg': 'League'}, inplace=True)

        if 'FG.1' in df.columns:
            df.rename(columns={'FG.1': 'FG%'}, inplace=True)
        if 'eFG' in df.columns:
            df.rename(columns={'eFG': 'eFG%'}, inplace=True)
        if 'FT.1' in df.columns:
            df.rename(columns={'FT.1': 'FT%'}, inplace=True)

        df = df.reset_index().drop('index', axis=1)
    
        # Drops career stats
        career_index = df[df['Season']=='Career'].index[0]
        df = df.iloc[:career_index, :]
        
        # Lamba function to get the proper end year
        df['Season'] = df['Season'].apply(lambda x: remove_char(x, 2) if len(x) != 4 else x)
        df['Season'] = df['Season'].apply(lambda x: remove_char(x, 2) if len(x) != 4 else x)
        df['Season'] = df['Season'].apply(lambda x: remove_char(x, 2) if len(x) != 4 else x)
        df['Season'] = df['Season'].replace(['1900'], '2000')
       
        # Turn into a int 
        df['Season'] = df['Season'].apply(pd.to_numeric)
            
        if(selector == 'adj_shooting'):
            df = df.rename(columns={'Team': 'Team ABV'})
              
        else:
            df = df.rename(columns={'Tm': 'Team ABV'})
        df['Team'] = df['Team ABV'].apply(lambda x: check_abv(x))
        df['Team ABV'] = df['Team ABV'].replace(['CHH'], 'CHO')
        
        # Create a new column for Team ID
        df['Team ID'] = df['Team ABV'].apply(lambda x: check_team_id(x))
        
        # Uppercases Team name
        df['Team'] = df['Team'].apply(lambda x: str(x).title())
        
        name_tuple = (record[0][0], record[0][1])
        
        if(name_tuple in RIGHT_NAME_DICT):
            record[0][0] = RIGHT_NAME_DICT[name_tuple]

        df['Player ID'] = PLAYER_ID[record[0][0]] 
        df['Player Name'] = record[0][0]
        df['Birth Date'] = record[0][1]
        
        # Rearranges the elements
        df = df[ ['Birth Date'] + [ col for col in df.columns if col != 'Birth Date' ] ]
        df = df[ ['Player Name'] + [ col for col in df.columns if col != 'Player Name' ] ]
        df = df[ ['Team'] + [ col for col in df.columns if col != 'Team' ] ]
        df = df[ ['Team ABV'] + [ col for col in df.columns if col != 'Team ABV' ] ]
        df = df[ ['Player ID'] + [ col for col in df.columns if col != 'Player ID' ] ]
        df = df[ ['Team ID'] + [ col for col in df.columns if col != 'Team ID' ] ]
        df = df[ ['Season'] + [ col for col in df.columns if col != 'Season' ] ]

        df = df.round(2)

        # Check for Did Not Play
        if df['G'].astype(str).str.contains('Did').any():
              
            # Removes all Did not Play
            df_filter = df[df['G'].str.isnumeric() == True]
            
            # Per game only has Did Not Play
            if(format == 'PER_GAME'):

                # Everything in the dataframe is a string, change it into a int
                df = df_filter
                
                df['Season'] = df['Season'].apply(pd.to_numeric)
                df['Team ID'] = df['Team ID'].apply(pd.to_numeric)
                df['Player ID'] = df['Player ID'].apply(pd.to_numeric)
                df['Age'] = df['Age'].apply(pd.to_numeric)
                df['G'] = df['G'].apply(pd.to_numeric)
                df['GS'] = df['GS'].apply(pd.to_numeric)
                df['MP'] = df['MP'].apply(pd.to_numeric)
                df['FG'] = df['FG'].apply(pd.to_numeric)
                df['FGA'] = df['FGA'].apply(pd.to_numeric)
                df['FG%'] = df['FG%'].apply(pd.to_numeric)
                df['3P'] = df['3P'].apply(pd.to_numeric)
                df['3PA'] = df['3PA'].apply(pd.to_numeric)
                df['3P%'] = df['3P%'].apply(pd.to_numeric)
                df['2P'] = df['2P'].apply(pd.to_numeric)
                df['2PA'] = df['2PA'].apply(pd.to_numeric)
                df['2P%'] = df['2P%'].apply(pd.to_numeric)
                df['eFG%'] = df['eFG%'].apply(pd.to_numeric)
                df['FT'] = df['FT'].apply(pd.to_numeric)
                df['FTA'] = df['FTA'].apply(pd.to_numeric)
                df['FT%'] = df['FT%'].apply(pd.to_numeric)
                df['ORB'] = df['ORB'].apply(pd.to_numeric)
                df['DRB'] = df['DRB'].apply(pd.to_numeric)
                df['TRB'] = df['TRB'].apply(pd.to_numeric)
                df['AST'] = df['AST'].apply(pd.to_numeric)
                df['STL'] = df['STL'].apply(pd.to_numeric)
                df['BLK'] = df['BLK'].apply(pd.to_numeric)
                df['TOV'] = df['TOV'].apply(pd.to_numeric)
                df['PF'] = df['PF'].apply(pd.to_numeric)
                df['PTS'] = df['PTS'].apply(pd.to_numeric)
                    
        else:
            pass
        
        # Drop Seasons that is before 1980
        df_new = df[df['Season'] < 1980].index
        df.drop(df_new, inplace = True)
        df = df.reset_index(drop=True)
        
        #
        if(format == "ADVANCED"):
            df = df.drop(['Unnamed: 19', 'Unnamed: 24'], axis=1)
        
        elif(format == "TOTALS" and 'Trp Dbl' in df.columns):
            df = df.drop(['Unnamed: 30'], axis=1)
        
        elif(format == "PER_POSS" and 'Unnamed: 29' in df.columns):
            df = df.drop(['Unnamed: 29'], axis=1)
        return df

'''
Looks up a players name and birth_date from player_names.csv
'''
def lookup(name, birth_date):
    
    # Path to csv file
    path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player_Name','player_names.csv')

    # Convert csv to dataframe
    df = pd.read_csv(path)
    
    # Search dataframe for name and birthdate
    df_new = df.loc[(df['Player'] == name) & (df['Birth_Date'] == birth_date)]

    # Put into a list and return
    record = df_new.values.tolist()
    return record

'''
Returns a csv a calulated career stats of a player starting from 1980
'''
def get_career_stats(name, birth_date, format='Per_Game', playoffs = False):

    # Gets the player stats dataframe 
    df = get_player_stats(name, birth_date, format, playoffs)
    
    format = format.title()

    # Create the  career_df and set it equal for now
    career_df = df 
    
    # Dataframe does not exist
    if(career_df is None):
        return None

    if(format == 'Totals'):
       
        # Drop unneeded stats 
        career_df = career_df.drop(['Season', 'Age', 'Team ID','Team', 'Team ABV', 'League', 'Pos'], axis=1)

        # Get the total amount of games of player's career
        career_df['G'] = df['G'].sum()

        # Get the total GS of player's career
        career_df['GS'] = df['GS'].sum()

         # Get the average minute played
        career_df['MP'] = df['MP'].sum()

        # Get the average FG
        career_df['FG'] = df['FG'].sum()

        # Get the average FGA
        career_df['FGA'] = df['FGA'].sum()

        # Calc the FG%
        if(career_df['FG'].sum() == 0 or career_df['FGA'].sum() == 0):
            career_df['FG%'] = 0
        else:
            career_df['FG%'] = (df['FG'].sum() / df['FGA'].sum()) 
        # Get the average 3P
        career_df['3P'] = df['3P'].sum()

        # Get the average 3PA
        career_df['3PA'] = df['3PA'].sum() 

        # Calc the 3P perentage
        # Check if they actually made a single three or attempted a single three
        if(df['3P'].sum() == 0 or df['3PA'].sum() == 0):
            career_df['3P%'] = 0
        else:
            career_df['3P%'] = (df['3P'].sum() / df['3PA'].sum()) 

         # Get the average 2P 
        career_df['2P'] = df['2P'].sum()

        # Get the average 2PA attempt
        career_df['2PA'] = df['2PA'].sum()

        # Get the 2P%
        if(career_df['2P'].sum() == 0 or df['2PA'].sum() == 0):
            career_df['2P%'] = 0
        else:
            career_df['2P%'] = (df['2P'].sum() / df['2PA'].sum()) 

        # Get the effective FG%
        if(career_df['FGA'].sum() == 0):
           career_df['eFG%'] = 0
        else: 
            career_df['eFG%'] = ((df['FG'].sum() + (0.5 * df['3P'].sum()) ) / df['FGA'].sum()) 
        
        # Get the FT 
        career_df['FT'] = df['FT'].sum()

        # Get the FTA 
        career_df['FTA'] = df['FTA'].sum()
       
        # Get FT%
        if(df['FT'].sum() == 0 or df['FTA'].sum() == 0):
            career_df['FT%'] = 0
        else:
            career_df['FT%'] = (df['FT'].sum() / df['FTA'].sum()) 

        # Get ORB
        career_df['ORB'] = df['ORB'].sum()

        # Get DRB
        career_df['DRB'] = df['DRB'].sum()

        # Get TRB
        career_df['TRB'] = df['TRB'].sum()

        # Get Ast
        career_df['AST'] = df['AST'].sum()

        # Get STL
        career_df['STL'] = df['STL'].sum()

        # Get BLK 
        career_df['BLK'] = df['BLK'].sum()

        # Get TOV
        career_df['TOV'] = df['TOV'].sum()

        # Get PF
        career_df['PF'] = df['PF'].sum()

        # Get PTS
        career_df['PTS'] = df['PTS'].sum()

        # Get Trp Dbl
        if 'Trp Dbl' in df.columns:
            
            career_df['Trp Dbl'] = df['Trp Dbl'].sum()
        else:
            career_df['Trp Dbl'] = 0
        # Make it a single index 
        career_df = career_df.drop_duplicates(subset=['G'])
        career_df = career_df.round(2)
    
        return career_df

    elif(format == "Advanced"):
        # Drop unneeded stats 
        career_df = career_df.drop(['Season', 'Age', 'Team ABV', 'Team ID','Team', 'League', 'Pos'], axis=1)
        
        # Get the total amount of games of player's career
        career_df['G'] = df['G'].sum()

        # Get the total amount of minutes played for career
        career_df['MP'] = df['MP'].sum()

        # Get the average PER 
        career_df['PER'] = df['PER'].mean()

        # Get the average TS% 
        career_df['TS%'] = df['TS%'].mean()

        # Get the average 3PAr
        career_df['3PAr'] = df['3PAr'].mean()

        # Get the average ORB%
        career_df['ORB%'] = df['ORB%'].mean()

        # Get the average DRB%
        career_df['DRB%'] = df['DRB%'].mean()

        # Get the average TRB%
        career_df['TRB%'] = df['TRB%'].mean()

        # Get the average AST%
        career_df['AST%'] = df['AST%'].mean()

        # Get the average STL%
        career_df['STL%'] = df['STL%'].mean()

        # Get the average BLK%
        career_df['BLK%'] = df['BLK%'].mean()

        # Get the average TOV% 
        career_df['TOV%'] = df['TOV%'].mean()

        # Get the average USG%
        career_df['USG%'] = df['USG%'].mean()

        # Get the average OWS
        career_df['OWS'] = df['OWS'].sum()

        # Get the average DWS
        career_df['DWS'] = df['DWS'].sum()

        # Get the average WS
        career_df['WS'] = df['WS'].sum()

        # Get the average WS/48
        career_df['WS/48'] = df['WS/48'].mean()

        # Get the average OBPM
        career_df['OBPM'] = df['OBPM'].mean()

        # Get the average DBPM
        career_df['DBPM'] = df['DBPM'].mean()

        # Get the average BPM 
        career_df['BPM'] = df['BPM'].mean()

        # Get the average VORP
        career_df['VORP'] = df['VORP'].mean()

        # Make it a single index 
        career_df = career_df.drop_duplicates(subset=['G'])
        career_df = career_df.round(2)
        
        return career_df
    
    # This should be for per game and per minute
    else:
        
        career_df = career_df.drop(['Season', 'Age', 'Team', 'Team ABV', 'Team ID', 'League', 'Pos'], axis=1)
       
        # Get the total amount of games of player's career
        career_df['G'] = df['G'].sum()
    
        # Get the total GS of player's career
        career_df['GS'] = df['GS'].sum()
        
        if(format == 'Per_Poss'):
            career_df['MP'] = df['MP'].sum()

        else:
            # Get the average minute played
            career_df['MP'] = df['MP'].mean()

        # Get the average FG
        career_df['FG'] = df['FG'].mean()

        # Get the average FGA
        career_df['FGA'] = df['FGA'].mean()
        
        # Calc the FG%
        if(df['FG'].mean() == 0 or df['FGA'].mean() == 0):
            career_df['FG%'] = 0
        else:
            career_df['FG%'] = (df['FG'].mean() / df['FGA'].mean())
        
        # Get the average 3P
        career_df['3P'] = df['3P'].mean()

        # Get the average 3PA
        career_df['3PA'] = df['3PA'].mean() 

        # Calc the 3P perentage
        # Check if they actually made a single three or attempted a single three
        if(df['3P'].mean() == 0 or df['3PA'].mean() == 0):
            career_df['3P%'] = 0
        else:
            career_df['3P%'] = (df['3P'].mean() / df['3PA'].mean()) 

        # Get the average 2P 
        career_df['2P'] = df['2P'].mean()

        # Get the average 2PA attempt
        career_df['2PA'] = df['2PA'].mean()

        # Get the 2P%
        if(career_df['2P'].mean() == 0 or df['2PA'].mean() == 0):
            career_df['2P%'] = 0
        else:
            career_df['2P%'] = (df['2P'].mean() / df['2PA'].mean()) 

        # Get the effective FG%
        if(career_df['FGA'].sum() == 0):
           career_df['eFG%'] = 0
        else: 
            career_df['eFG%'] = ((df['FG'].sum() + (0.5 * df['3P'].sum()) ) / df['FGA'].sum()) 
       
        # Get the FT 
        career_df['FT'] = df['FT'].mean()

        # Get the FTA 
        career_df['FTA'] = df['FTA'].mean()
       
        # Get FT%
        if(df['FT'].mean() == 0 or df['FTA'].mean() == 0):
            career_df['FT%'] = 0
        else:
            career_df['FT%'] = (df['FT'].mean() / df['FTA'].mean()) 

        # Get ORB
        career_df['ORB'] = df['ORB'].mean()

        # Get DRB
        career_df['DRB'] = df['DRB'].mean()

        # Get TRB
        career_df['TRB'] = df['TRB'].mean()

        # Get Ast
        career_df['AST'] = df['AST'].mean()

        # Get STL
        career_df['STL'] = df['STL'].mean()

        # Get BLK 
        career_df['BLK'] = df['BLK'].mean()

        # Get TOV
        career_df['TOV'] = df['TOV'].mean()

        # Get PF
        career_df['PF'] = df['PF'].mean()

        # Get PTS
        career_df['PTS'] = df['PTS'].mean()

        # Only Per_poss has these stats
        if(format == 'Per_Poss'):
            career_df['ORtg'] = df['ORtg'].mean()
            career_df['DRtg'] = df['DRtg'].mean()

        # Make it a single index 
        career_df = career_df.drop_duplicates(subset=['G'])
        career_df = career_df.round(2)
      
        # Per Minute does not eFG% 
        if(format == 'Per_Minute' or format == 'Per_Poss'):
            career_df = career_df.drop(['eFG%'], axis=1)

        return career_df
