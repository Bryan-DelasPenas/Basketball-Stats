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
from Team_Constants import RIGHT_NAME_DICT
from helper import create_output_directory, create_output_child_directory

'''
Get csvs of player stats
'''
def csv_player_stats(name, birth_date, format, playoff, player_path):
    print(format)
    
    df = get_player_stats(name, birth_date,format, playoff)

    if(df is None):
        return None

    if(playoff):
        playoff_string = "Playoff_Stats"

    else:
        playoff_string = "Regular_Stats"

    directory_child = format.title()

    first_path = os.path.join(player_path, playoff_string)
    
    if(not os.path.isdir(first_path)):
        
        # Create the directory with the final_path
        os.mkdir(first_path)
    
    output_path = os.path.join(first_path, directory_child)
    if(not os.path.isdir(output_path)):

        os.mkdir(output_path)

    file_name = '//'+ name + '_' + format + '.csv'

    df.to_csv(output_path + file_name, index = False)
    
    return 0

'''
Get csvs for career stats
'''

'''
Calls all functions above and puts into its own csvs
'''
def get_player_csv():
    csv_path = path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player_Name','player_names.csv')

    source_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player')

    if(not os.path.isdir(source_path)):
        
        # Create the directory with the final_path
        os.mkdir(source_path)

    # Convert csv to dataframe
    df = pd.read_csv(path)
    
    record = df.values.tolist()


    # Iterate through the list 
    for i in range(1179, 1181):
        print(i)
        print(record[i][0])
        player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', record[i][0])
        name_tuple = (record[i][0], record[i][1])

        # Check for special cases, like Jr.
        if(name_tuple in RIGHT_NAME_DICT):
            new_string = RIGHT_NAME_DICT[name_tuple]
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_string)

        # Check if the directory of player name was made
        if(not os.path.isdir(player_path)):
            # Create the directory with the final_path
            os.mkdir(player_path)
        
        '''
        # Regualar Season Stat
        csv_player_stats(record[i][0], record[i][1], 'Per_Game', False, player_path)
        csv_player_stats(record[i][0], record[i][1], 'Per_Minute', False, player_path)
        csv_player_stats(record[i][0], record[i][1], 'Per_Poss', False, player_path)
        csv_player_stats(record[i][0], record[i][1], 'Totals', False, player_path)
        csv_player_stats(record[i][0], record[i][1], 'Advanced', False, player_path)
        '''
        '''
        # Playoffs Season Stat
        csv_player_stats(record[i][0], record[i][1], 'Per_Game', True, player_path)
        csv_player_stats(record[i][0], record[i][1], 'Per_Minute', True, player_path)
        csv_player_stats(record[i][0], record[i][1], 'Per_Poss', True, player_path)
        csv_player_stats(record[i][0], record[i][1], 'Totals', True, player_path)
        csv_player_stats(record[i][0], record[i][1], 'Advanced', True, player_path)
        '''

'''
Main function
'''
def main():
    
    start_time = time.time()
    #csv_player_stats("Kareem Abdul-Jabbar", 'April 16, 1947', 'PER_GAME', False, False)
    get_player_csv()
    print("--- %s seconds ---" % (time.time() - start_time))
main()