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

from utils import strip_accents
'''
Removes accent from characters TODO: Let off at M, still need N - Z
'''
def translate(name):
    
    special_char = ('Ã³', 'Ã–', 'ÅŸ', 'Ä±', 'Ãº', 'Ã§', 'Å¡', 'Å†', 'Å¡', 'Ä‡', 'Ä', 'Å¾', 'Ã¡', 'Å½','ÄŒ', 'Ä','Ã©', 'Ã', 'A°', 'Aª', 'a°', 'A¼', 'A¨', 'A²', 'È™',
                    'A¶', 'Å«', 'A¤')
    
    # 
    if any(x in name for x in special_char):
        if('Biedrin' in name):
            name = name.replace('Å¡', 'n')

        # Case for: Vlatko Cancar
        elif('Vlatko' in name):
            name = "Vlatko Cancar"

        #Case for: Guillermo diaz
        elif('Guillermo' in name):
            name = "Guillermo Diaz"

        elif('Faverani' in name):
            name = "Vitor Luiz Faverani"

        elif('Cristiano' in name):
            name = 'Cristiano Felicio'

        elif('Francisco Garc' in name):
            name = 'Francisco Garcia'

        elif('Jasikevi' in name):
            name = 'Sarunas Jasikevicius'

        elif('Kuko' in name):
            name = 'Toni Kukoc'

        elif('iulionis' in name):
            name = 'Sarunas Marciulionis'

        else:
            name = name.replace('Ã³', 'o')
            name = name.replace('Ã–', 'O')
            name = name.replace('ÅŸ', 's')
            name = name.replace('Ä±', 'i')
            name = name.replace('Ãº', 'u')
            name = name.replace('Ã§', 'c')
            name = name.replace('Å†', 's')
            name = name.replace('Å¡', 's')
            name = name.replace('Ä‡', 'c')
            name = name.replace('Ä', 'a')
            name = name.replace('Ã¡', 'a')
            name = name.replace('Å¾', 'z')
            name = name.replace('Å½', 'Z')
            name = name.replace('aŒ', 'C')
            name = name.replace('Ã©', 'e')
            name = name.replace('Ã', 'A')
            name = name.replace('A°', 'o')
            name = name.replace('Aª', 'e')
            name = name.replace('a°', 'I')
            name = name.replace('A¼', 'u')
            name = name.replace('A¨', 'e')
            name = name.replace('È™', 's')
            name = name.replace('A²', 'o')
            name = name.replace('A¶', 'o')
            name = name.replace('Å«', 'u')
            name = name.replace('A¤', 'a')
    print(name)
    return name
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
        
        #print(df)

def get_player_stats(season): 
    return 0

def main():
    get_player_name('m')
main()
