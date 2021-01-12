import pandas as pd
import sys
import os
import pathlib 
from pathlib import Path
from requests import get
import unicodedata, unidecode
sys.path.append(str(pathlib.Path().absolute()) + '\\python_scrapers')

from Player_Stats_Scraper import get_player_name
from helper import create_output_directory, create_output_child_directory

'''
Get csvs for players name and other data
'''
def players_names_csv():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
    
    # Check if the proper directories has been made
    source_directory = "Output"
    directory_parent = "Player_Stats"
    directory_child = "Player_Name"
    
    # Create the directories if needed
    create_output_directory(directory_parent)
    create_output_child_directory(directory_parent,directory_child)
    
    # Create the output path and the file name 
    output_path = os.path.join(pathlib.Path().absolute(), source_directory ,directory_parent, directory_child)
    file_name = '\\' + "player_names" + ".csv" 
    
    for letter in letters:
        df = get_player_name(letter)
        
        file_name = '\\' + letter +'_'+"player_names" + ".csv"
        df.to_csv(output_path + file_name, index = False)

def main():
    players_names_csv()

#main()