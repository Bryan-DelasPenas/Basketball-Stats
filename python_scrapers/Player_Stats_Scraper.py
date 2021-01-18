########################################################
# File: Team_Constants.py 
# Author: Bryan Delas Penas 
# Email:  bryan.delaspenas0405@gmail.com
# Date:   12/20/2020
# 

import pandas as pd
import sys
from bs4 import BeautifulSoup
from requests import get
import unicodedata, unidecode
import codecs 
import re 
import os
from utils import translate
import pathlib
from pathlib import Path
import numpy as np
import time

from os import chdir
from glob import glob
import pandas as pdlib

from Team_Stats_Scraper import remove_char

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
        table = str(soup.find('table'))
        
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

    # Special Case: for name = Jeff Aryes since he changed his name in 2013
    if(name == "Jeff Ayres" and birth_date == "April 29, 1987" ):
        sub_name = "Jeff Pendergraph"
        # Get the first initial of last name
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'
    
    # Special Case: for J.J Barea, for some reason the url is bareajo01 instead of bareajj01
    elif(name == "J.J. Barea"):
        sub_name = "Jose Barea"
        # Get the first initial of last name
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'
    
    # Special Case: for Clint Capela, for some reason the url is capelca01 instead of capelc101
    elif(name == "Clint Capela"):
        sub_name = "Caint Capela"
        # Get the first initial of last name
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'
    
    # Special Case: They just combined the middle name with the last name 
    elif(name == "Nando De Colo"):
        sub_name = "Nando DeColo"
        # Get the first initial of last name
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    elif(name == "Vinny Del Negro"):
        sub_name = "Vinny DelNegro"
        # Get the first initial of last name
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'
        
    elif(name == "Khalid El-Amin"):
        sub_name = "Khalid ElAmin"
        # Get the first initial of last name
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'
    
    # Special case, he does not start at 01 but 02
    elif(name == "P.J. Hairston" or name == "Markus Howard" or name == "Xavier Munford" or name == "Cherokee Parks" or name == "Tony Smith"):
        initial = name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(name) + '02.html'
    
    # Special Case: His name is Rick in the URL 
    elif(name == "Alfredrick Hughes"):
        sub_name = "Rick Hughes"
        # Get the first initial of last name
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    # Special Case: His name on the page_name is D.J. Mbenga
    elif(name == "Didier Ilunga-Mbenga"):
        name = "D.J. Mbenga"
        # Get the first initial of last name
        initial = name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(name) + '01.html'
    
    # Special Case: jonesja03 does not exist so it will crash the program
    elif(name == "Jalen Jones" or name == "Jalen Smith"):
        initial = name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(name) + '04.html'
    
    # Special Case: - in the name 
    elif(name == "Michael Kidd-Gilchrist"):
        sub_name = "Michael KiddGilchrist"
        # Get the first initial of last name
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'
    
    # Special Case: Kleber -> Klebir
    elif(name == "Maxi Kleber"):
        sub_name = "Maxi Klebir"
        # Get the first initial of last name
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'
    
    # Special Case: Remove Grey from his name 
    elif(name == "Horacio Llamas Grey"):
        name = "Horacio Llamas"
        initial = name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(name) + '01.html'

    # Special Case: Now this name has the III but others don't?
    elif(name == "John Lucas III"):
        sub_name = "John Lucas"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    # Special Case: Changed his name 
    elif(name == "Sheldon Mac"):
        sub_name = "Sheldon McClellan"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'
    
    # Special Case: Name in url is LA instead of Fr
    elif(name == "Frank Ntilikina"):
        sub_name = "Larank Ntilikina"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'
 
    # Special Case: For some reason, osmande01 instead of osmance01
    elif(name == "Cedi Osman"):
        sub_name = "De Osman"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    # Special Case: For some reason, pavloa01 instead of pavlosa01
    elif(name == "Sasha Pavlovic"):
        sub_name = "alsha Pavlovic"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    # Special Case: For some reason instead of senemo01 its senesa01
    elif(name == "Mouhamed Sene"):
        sub_name = "Sa Sene"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    # Special Case: Doesn't Use offical name as page name
    elif(name == "Edy Tavares"):
        sub_name = "Walter Tavares"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    # Special Case: Url uses Nick VanExel
    elif(name == "Nick Van Exel"):
        sub_name = "Nick VanExel"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    # Special Case: Url uses Nick VanExel
    elif(name == "Keith Van Horn"):
        sub_name = "Keith VanHorn"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    # Special Case: Users Vander instead of Velden
    elif(name == "Logan Vander Velden"):
        sub_name = "Logan Vander"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    # Special Case: Url uses Vincius instead of Vinicius
    elif(name == "Marcus Vinicius"):
        sub_name = "Marcus Vincius"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    elif(name == "Henry Walker"):
        sub_name = "Bill Walker"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    elif(name == "Mo Williams"):
        sub_name = "Maurice Williams"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

    elif(name == "Metta World Peace"):
        sub_name = "Ron Artes"
        initial = sub_name.split(' ')[1][0].lower()
        suffix = '/players/' + initial + '/' + create_player_suffix(sub_name) + '01.html'

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

        # Special Case: Marvin Bagley does not have III in his name for some reason 
        if(name == "Marvin Bagley"):
            name = "Marvin Bagley III"

        # Special Case: LeMark Baker should be Mark Baker 
        elif(name == "LaMark Baker"):
            name = "Mark Baker"

        # Special Case: Mohamed Bamba should be Mo Bamba 
        elif(name == "Mohamed Bamba"):
            name = "Mo Bamba"
 
        # Special Case: In the table with all players names, it does not have Jr
        elif(name == "Troy Brown"):
            name = "Troy Brown Jr."

        # Special Case: In the table with all players names, it does not have Jr
        elif(name == "Vernon Carey"):
            name = "Vernon Carey Jr."

         # Special Case: In the table with all players names, it does not have Jr
        elif(name == "Wendell Carter"):
            name = "Wendell Carter Jr."

         # Special Case: Lugigi is converted to Gigi
        elif(name == "Luigi Datome"):
            name = "Gigi Datome"

        # Special Case: Larry Drew is missing II
        elif(name == "Larry Drew" and birth_date == "March 5, 1990"):
            name = "Larry Drew II"

        # Special Case: For some reason for Kiwane Lemorris Garris instead of Kiwane Garris
        elif(name == "Kiwane Garris"):
            name = "Kiwane Lemorris Garris"

        # Special Case: Tim Hardaway JR is not there
        elif(name == "Tim Hardaway" and birth_date == "March 16, 1992"):
            name = "Tim Hardaway Jr."
        
        # Special Case: For some reason Nene Hilario is just Nene
        elif(name == "Nene Hilario"):
            name = "Nene"

        # Special Case: Add junior 
        elif(name == "Jaren Jackson" and birth_date == "September 15, 1999"):
            name = "Jaren Jackson Jr."

        # Special Case: Add Junior
        elif(name == "Derrick Jones" and birth_date == "February 15, 1997"):
            name = "Derrick Jones Jr."

        # Special Case: Add Junior 
        elif(name == "Walt Lemon" and birth_date == "July 26, 1992"):
            name = "Walt Lemon Jr."

        # Speicial Case: Add Junior
        elif(name == "Kira Lewis" and birth_date == "April 6, 2001"):
            name = "Kira Lewis Jr."

        # Special Case: Add Jr.
        elif(name == "Kenyon Martin" and birth_date == "January 6, 2001"):
            name = "Kenyon Martin Jr."

        # Special Case: Add III to end of name 
        elif(name == "Frank Mason" and birth_date == "April 3, 1994"):
            name = "Frank Mason III"

        # Speical Case: Add JR
        elif(name == "Larry Nance" and birth_date == "January 1, 1993"):
            name = "Larry Nance Jr."

        # Special Case: Add Jr.
        elif(name == "Kelly Oubre" and birth_date == "December 9, 1995"):
            name = "Kelly Oubre Jr."

        # Special Case: Add II 
        elif(name == "Gary Payton" and birth_date == "December 1, 1992"):
            name = "Gary Payton II"

        # Special Case: Add Jr.
        elif(name == "Kevin Porter" and birth_date == "May 4, 2000"):
            name = "Kevin Porter Jr."

        # Special Case: Add Jr.
        elif(name == "Michael Porter" and birth_date == "June 29, 1998"):
            name = "Michael Porter Jr."

        elif(name == "Efthimi Rentzias"):
            name = "Efthimios Rentzias"
        
        # Special Case: Add Jr.
        elif(name == "Glen Rice" and birth_date == "January 1, 1991"):
            name = "Glen Rice Jr."

        # Special Case: Add III
        elif(name == "Glenn Robinson" and birth_date == "January 8, 1994" ):
            name = "Glenn Robinson III"

        # Special Case: Add Jr.
        elif(name == "Dennis Smith" and birth_date == "November 25, 1997"):
            name = "Dennis Smith Jr."

        # Special Case: Jeffery to Jeff
        elif(name == "Jeffery Taylor" and birth_date == "May 23, 1989"):
            name = "Jeff Taylor"

        # Special Case: Add Sr. even thou there is no jr? 
        elif(name == "Xavier Tillman" and birth_date == "January 12, 1999"):
            name = "Xavier Tillman Sr."

        # Special Case: Add Jr. 
        elif(name == "Gary Trent" and birth_date == "January 18, 1999"):
            name = "Gary Trent Jr."

        # Special Case: III
        elif(name == "James Webb" and birth_date == "August 19, 1993"):
            name = "James Webb III"

        # Special Case: Due to having a middle name we remove it early, we add it back here
        if(middle_flag):
            name = ""
            name = name_list[0] + " " + name_list[1] + " " + name_list[2] 

        #print(page_name,":" ,name)
       
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

    # Type of stat you want
    selector = format.lower()
    
    # Check if the stat wanted is playoff
    if playoffs:
        selector = 'playoffs_' + selector

    # Get the url of the table
    page = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url={suffix}&div=div_{selector}')
    
    # Check if the request went through 
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')

        if(table == None):
            #print("Error: table not found")
            return None

        df = pd.read_html(str(table))[0]
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
    
        # Turn into a int 
        df['Season'] = df['Season'].apply(pd.to_numeric)
            
        # Drop players that are didn't play at 1980
        df_new = df[df['Season'] < 1980].index
        df.drop(df_new, inplace = True)

        return df

'''
Looks up a players name and birth_date from player_names.csv
'''
def lookup(name, birth_date):
    
    # Path to csv file
    path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', 'Player_Name','player_names.csv')

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
def career_stats(name, birth_date, format, playoffs = False):

    # Gets the player stats dataframe 
    df = get_player_stats(name, birth_date, format, playoffs)
    
    format = format.title()

    # Create the  career_df and set it equal for now
    career_df = df 
    if(format == 'Totals'):
        return None

    elif(format == "Advanced"):
        return None

    elif(format == "Per_Poss"):
        return None

    elif(format == 'Adjusted Shooting' and not playoffs):
        return None
    
    # This should be for per game and per minute
    else:
        career_df = career_df.drop(['Season', 'Age', 'Tm', 'League', 'Pos'], axis=1)
        
        # Get the total amount of games of player's career
        career_df['G'] = df['G'].sum()

        # Get the total GS of player's career
        career_df['GS'] = df['GS'].sum()

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
            career_df['FG%'] = (df['FG'].mean() / df['FGA'].mean()) * 100
        
        # Get the average 3P
        career_df['3P'] = df['3P'].mean()

        # Get the average 3PA
        career_df['3PA'] = df['3PA'].mean() 

        # Calc the 3P perentage
        # Check if they actually made a single three or attempted a single three
        if(df['3P'].mean() == 0 or df['3PA'].mean() == 0):
            career_df['3P%'] = 0
        else:
            career_df['3P%'] = (df['3P'].mean() / df['3PA'].mean()) * 100

        # Get the average 2P 
        career_df['2P'] = df['2P'].mean()

        # Get the average 2PA attempt
        career_df['2PA'] = df['2PA'].mean()

        # Get the 2P%
        if(career_df['2P'].mean() == 0 or df['2PA'].mean() == 0):
            career_df['2P%'] = 0
        else:
            career_df['2P%'] = (df['2P'].mean() / df['2PA'].mean()) * 100

        # Get the effective FG%
        career_df['eFG%'] = ((df['FG'].mean() + (0.5 * df['3P'].mean()) ) / df['FGA'].mean()) * 100
        
        # Get the FT 
        career_df['FT'] = df['FT'].mean()

        # Get the FTA 
        career_df['FTA'] = df['FTA'].mean()
       
        # Get FT%
        if(df['FT'].mean() == 0 or df['FTA'].mean() == 0):
            career_df['FT%'] = 0
        else:
            career_df['FT%'] = (df['FT'].mean() / df['FTA'].mean()) * 100

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

        # Make it a single index 
        career_df = career_df.drop_duplicates(subset=['G'])
        career_df = career_df.round(1)
        
        # Per Minute does not eFG% 
        if(format == 'Per_Minute'):
            career_df = career_df.drop(['eFG%'], axis=1)

        print(career_df)
        return None

def main():
    start_time = time.time()
    career_stats("Kareem Abdul-Jabbar", "April 16, 1947", 'per_minute')
    print("--- %s seconds ---" % (time.time() - start_time))
main()
