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
from utils import translate

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
        df.columns = ['PLAYER', 'FROM', 'TO','POS', 'HEIGHT', 'WEIGHT', 'BIRTH_DATE','COLLEGE']
        
        # Drop players that are didn't play at 1980
        df_new = df[df['TO'] < 1980].index
        df.drop(df_new, inplace = True)
        
        
        df['PLAYER'] = df['PLAYER'].apply(lambda x: x.replace('*', ''))
        df['PLAYER'] = df['PLAYER'].apply(lambda name: translate(name))
        
        return df

'''
Creates player suffixes for url 
'''
def create_player_suffix(name):
    
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
Creates a valid player suffix based on the parameter name
'''    
def get_player_suffix(name):
 
    # Get the first initial of last name
    initial = name.split(' ')[1][0].lower()
    suffix = '/players/' + initial + '/' + create_player_suffix(name) + '01.html'
    print(suffix)
    # Get the url of the player stats
    page = get(f'https://www.basketball-reference.com{suffix}')

    # Check if the request can go through 
    while page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        h1 = soup.find('h1', attrs={'itemprop': 'name'})
      
        if h1:
            page_name = h1.find('span').text

        # This is for accented characters on the website         
        if(unidecode.unidecode(page_name).lower() == name.lower()):
            
            return suffix
            
        else:
            suffix = suffix[:-6] + str(int(suffix[-6]) + 1 ) + suffix[-5:]
            page = get(f'https://www.basketball-reference.com{suffix}')

    return None
    
    

def get_player_stats(season): 
    return 0


def main():
    print(get_player_suffix('John Wall'))

main()