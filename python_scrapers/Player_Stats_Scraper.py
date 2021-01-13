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
import time

from os import chdir
from glob import glob
import pandas as pdlib

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
    
    print(suffix)

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

        # Special Case: Due to having a middle name we remove it early, we add it back here
        if(middle_flag):
            name = ""
            name = name_list[0] + " " + name_list[1] + " " + name_list[2] 

        print(page_name,":" ,name)
       
        # This is for accented characters on the website         
        if(unidecode.unidecode(page_name).lower() == name.lower() and birth_date == final_date):

            return suffix
        
        else:
            suffix = suffix[:-6] + str(int(suffix[-6]) + 1 ) + suffix[-5:]
            page = get(f'https://www.basketball-reference.com{suffix}')

    return None
    
    
'''

'''
def get_player_stats(name, birth_date,format='PER_GAME', playoffs=False, career=False): 
    
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

        df = pd.read_html(str(table))[0]
        df.rename(columns={'Lg': 'League'}, inplace=True)

        if 'FG.1' in df.columns:
            df.rename(columns={'FG.1': 'FG%'}, inplace=True)
        if 'eFG' in df.columns:
            df.rename(columns={'eFG': 'eFG%'}, inplace=True)
        if 'FT.1' in df.columns:
            df.rename(columns={'FT.1': 'FT%'}, inplace=True)

        career_index = df[df['Season']=='Career'].index[0]
        
        if career:
            df = df.iloc[career_index+2:, :]
        else:
            df = df.iloc[:career_index, :]

        df = df.reset_index().drop('index', axis=1)
        return df

'''

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

def main():
    print(get_player_suffix("Khalid El-Amin", "April 25, 1979"))
main()