import pandas as pd
import os
import pathlib
from pathlib import Path

from Player_Stats_Scraper import get_player_name

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