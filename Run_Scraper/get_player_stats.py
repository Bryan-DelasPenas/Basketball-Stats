import pandas as pd
import sys
import os
import pathlib 
from pathlib import Path
from requests import get
import unicodedata, unidecode
import time
sys.path.append(str(pathlib.Path().absolute()) + '\\Python_Scrapers')


from Player_Stats_Scraper import get_player_name, get_player_stats
from helper import create_output_directory, create_output_child_directory

'''
Get csvs for players name and other data
'''
def players_names_csv():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
    
    # Check if the proper directories has been made
    source_directory = "Output"
    directory_parent = "Player"
    directory_child = "Player_Name"
    
    # Create the directories if needed
    create_output_directory(directory_parent)
    create_output_child_directory(directory_parent,directory_child)
    
    # Create the output path and the file name 
    output_path = os.path.join(pathlib.Path().absolute(), source_directory ,directory_parent, directory_child)
    file_name = '\\' + "player_names" + ".csv" 
    
    for letter in letters:
        df = get_player_name(letter)
        
        file_name = '\\' + "player_names" + ".csv"
        
        if letter == 'a':
            df.to_csv(output_path + file_name, mode='a', index = False)
        else:
            df.to_csv(output_path + file_name, mode='a',header=False, index = False)

'''

'''
def csv_player_stats(name, birth_date, format, playoff, career):

    directory_child = format.title()
   
    output_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', name, directory_child)
    if(not os.path.isdir(output_path)):
        
        # Create the directory with the final_path
        os.mkdir(output_path)
    
    df = get_player_stats(name, birth_date,format, playoff, career)
    file_name = '//'+ name + '_' + format + '.csv'

    df.to_csv(output_path + file_name, index = False)
    
    return 0

def get_player_csv():
    csv_path = path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', 'Player_Name','player_names.csv')
    
    # Convert csv to dataframe
    df = pd.read_csv(path)
    
    record = df.values.tolist()

    # Iterate through the list TODO: run till length there is going to be an error at line 1130 
    for i in range(1130, len(record)):
        print(i)
        print(record[i][0])
        player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', record[i][0])
    
        if(not os.path.isdir(player_path)):
            # Create the directory with the final_path
            os.mkdir(player_path)

        csv_player_stats(record[i][0], record[i][1], 'PER_GAME', False, False)


def main():
    #players_names_csv()
    start_time = time.time()
    #csv_player_stats("Nikola Jokic", 'February 19, 1995', 'PER_GAME', False, False)
    get_player_csv()
    print("--- %s seconds ---" % (time.time() - start_time))
main()