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
import codecs
import unicodedata, unidecode

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
        soup = BeautifulSoup(page.text, 'html.parser')
        table = str(soup.find('table'))
        
        # Insert this data into a pandas dataframe
        df = pd.read_html(str(table))[0]
        
        # Column for the dataframe 
        df.columns = ['PLAYER', 'FROM', 'TO','POS', 'HEIGHT', 'WEIGHT', 'BIRTH_DATE','COLLEGE']
        
        # Drop players that are didn't play at 1980
        df_new = df[df['TO'] < 1980].index
        df.drop(df_new, inplace = True)
        
        df['PLAYER'] = df['PLAYER'].apply(lambda name: translate(name))
        return df
        #print(df)

def get_player_stats(season): 
    return 0

def main():
    print(get_player_name('z'))
main()
