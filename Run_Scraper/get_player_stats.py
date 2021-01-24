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
    for i in range( len(record)):
        print(i)
        print(record[i][0])
        
        player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', record[i][0])

        if(record[i][0] == "Troy Brown" and record[i][1] == "July 28, 1999"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        elif(record[i][0] == "Vernon Carey" and record[i][1] == "February 25, 2001"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        elif(record[i][0] == "Wendell Carter" and record[i][1] == "April 16, 1999"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        elif(record[i][0] == "Larry Drew" and record[i][1] == "March 5, 1990"):
            new_name =  str(record[i][0]) + " II"
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        elif(record[i][0] == "Tim Hardaway" and record[i][1] == "March 16, 1992"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        elif(record[i][0] == "Jaren Jackson" and record[i][1] == "September 15, 1999"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add Junior
        elif(record[i][0] == "Derrick Jones" and record[i][1] == "February 15, 1997"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add Junior 
        elif(record[i][0] == "Walt Lemon" and record[i][1] == "July 26, 1992"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Speicial Case: Add Junior
        elif(record[i][0] == "Kira Lewis" and record[i][1] == "April 6, 2001"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add Jr.
        elif(record[i][0] == "Kenyon Martin" and record[i][1] == "January 6, 2001"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add III to end of name 
        elif(record[i][0] == "Frank Mason" and record[i][1] == "April 3, 1994"):
            new_name =  str(record[i][0]) + " III"
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)
        
        # Speical Case: Add JR
        elif(record[i][0] == "Larry Nance" and record[i][1] == "January 1, 1993"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add Jr.
        elif(record[i][0] == "Kelly Oubre" and record[i][1] == "December 9, 1995"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add II 
        elif(record[i][0] == "Gary Payton" and record[i][1] == "December 1, 1992"):
            new_name =  str(record[i][0]) + " II"
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add Jr.
        elif(record[i][0] == "Kevin Porter" and record[i][1] == "May 4, 2000"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add Jr.
        elif(record[i][0] == "Michael Porter" and record[i][1] == "June 29, 1998"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add Jr.
        elif(record[i][0] == "Glen Rice" and record[i][1] == "January 1, 1991"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add III
        elif(record[i][0] == "Glenn Robinson" and record[i][1] == "January 8, 1994" ):
            new_name =  str(record[i][0]) + " III"
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add Jr.
        elif(record[i][0] == "Dennis Smith" and record[i][1] == "November 25, 1997"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add Sr. even thou there is no jr? 
        elif(record[i][0] == "Xavier Tillman" and record[i][1] == "January 12, 1999"):
            new_name =  str(record[i][0]) + " Sr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: Add Jr. 
        elif(record[i][0] == "Gary Trent" and record[i][1] == "January 18, 1999"):
            new_name =  str(record[i][0]) + " Jr."
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)
            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        # Special Case: III
        elif(record[i][0] == "James Webb" and record[i][1] == "August 19, 1993"):
            new_name =  str(record[i][0]) + " III"
            player_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', new_name)

            if(not os.path.isdir(player_path)):
                os.mkdir(player_path)

        elif(not os.path.isdir(player_path)):
            # Create the directory with the final_path
            os.mkdir(player_path)

        print(record[i][0])
        
        # Regualar Season Stat
        csv_player_stats(record[i][0], record[i][1], 'Per_Game', False, player_path)
        #csv_player_stats(record[i][0], record[i][1], 'Per_Minute', False, player_path)
        #csv_player_stats(record[i][0], record[i][1], 'Per_Poss', False, player_path)
        #csv_player_stats(record[i][0], record[i][1], 'Totals', False, player_path)
        #csv_player_stats(record[i][0], record[i][1], 'Advanced', False, player_path)
    
        # Playoffs Season Stat
        #csv_player_stats(record[i][0], record[i][1], 'Per_Game', True, player_path)
        #csv_player_stats(record[i][0], record[i][1], 'Per_Minute', True, player_path)
        #csv_player_stats(record[i][0], record[i][1], 'Per_Poss', True, player_path)
        #csv_player_stats(record[i][0], record[i][1], 'Totals', True, player_path)
        #csv_player_stats(record[i][0], record[i][1], 'Advanced', True, player_path)


'''
Main function
'''
def main():
    #players_names_csv()
    start_time = time.time()
    #csv_player_stats("Kareem Abdul-Jabbar", 'April 16, 1947', 'PER_GAME', False, False)
    get_player_csv()
    print("--- %s seconds ---" % (time.time() - start_time))
main()