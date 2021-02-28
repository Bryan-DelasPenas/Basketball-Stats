import pandas as pd
import os
import pathlib
from pathlib import Path

from bs4 import BeautifulSoup
from requests import get
import unicodedata, unidecode

from utils import strip_accents


'''
Creates a dataframe of player's name active from 1980 - 2020
'''
def get_player_name(letter):
    
    # Get the url of the website
    page = get(f'https://www.basketball-reference.com/players/{letter}/')

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
        df['Player'] = df['Player'].apply(lambda name: strip_accents(name))
        
        # Drop unneeded columns
        df = df.drop(['Pos', 'From', 'To','Height', 'Weight', 'College'], axis=1)
        
        return df

'''
Get csvs for players name and other data
'''
def players_names_csv():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # Check if the proper directories has been made
    source_directory = "Output"
    directory_parent = "Player_Name"
    
    
    # Create the directories if needed

    # Create the output path and the file name 
    first_path = os.path.join(pathlib.Path().absolute(), source_directory)
    
    if(not os.path.isdir(first_path)):
        
        # Create the directory with the final_path
        os.mkdir(first_path)
    else:
        pass
    
    second_path = os.path.join(first_path, directory_parent)
    if(not os.path.isdir(second_path)):
        os.mkdir(second_path)
    else:
       pass    
    file_name = '\\' + "player_names" + ".csv" 
    
    if(not os.path.isfile(second_path + file_name)):
    
        for letter in letters:
            print(letter)
            df = get_player_name(letter)
            
            file_name = '\\' + "player_names" + ".csv"
            
            if letter == 'a':
                df.to_csv(second_path + file_name, mode='a', index = False)
            else:
                df.to_csv(second_path + file_name, mode='a',header=False, index = False)
    
    else:
        pass

def main():
    players_names_csv()
main()