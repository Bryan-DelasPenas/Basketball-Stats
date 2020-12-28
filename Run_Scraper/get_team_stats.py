#####################################################
# File:   get_team_stats.py
# Author: Bryan Delas Penas 
# Email:  bryan.delaspenas0405@gmail.com
# Date:   12/21/2020
# 
# Description: 
# This code gathers the season data for each team 
import sys 
sys.path.append('\\Users\\Bryan\\Desktop\\Basketball-Stats\\python_scrapers')
import os
import pathlib 
from pathlib import Path
from Team_Stats_Scraper import get_season_team_stats, get_team_stats

'''
Generates a CSV file of teams per game stats since 1980
'''
def csv_season_stats(year, format):
    
    if(format == 'PER_GAME'):
        file_name = "Team_Pergame_Stats"
        string_type = "pergame"

    elif(format == 'PER_POSS'):
        file_name = "Team_Perposs_Stats"
        string_type = "perposs"

    elif(format == 'TOTAL'):
        file_name = "Team_Total_Stats"
        string_type = "total"
    
    else:
        print("Please select insert the right format")
        return 0

    df = get_season_team_stats(year, format)
    df = df.round(2)
        
    # Output path for the csv file
    output_path = os.path.join(pathlib.Path().absolute(), "Output", "Season_Stats", file_name)
        
    # Create a unique name for the file 
    season =  "\\"+ str(year)+ "season"+ "_" + string_type + ".csv"

    # Create the csv file
    df.to_csv(output_path + season, index = False)

'''
Functions that calls the three functions above that creates the csv 
'''
def get_season_csv():
    
    # Iterate through the 1980 and 2020 season
    for year in range(1980, 2021):
        csv_season_stats(year, 'PER_GAME')
        csv_season_stats(year, 'PER_POSS')
        csv_season_stats(year, 'TOTAL')
      

'''
Helper function that creates folders for each season 
'''
def create_season_folder():
    # The file path
    output_path = os.path.join(pathlib.Path().absolute(), "Output", "Team_Stats")
    
    # If this is false, creates file else just print message
    if(os.path.isdir(os.path.join(output_path, "1980")) == False):
        print("Creating files from 1980 to 2020")
        
        # Iterate through 1980 - 2020
        for season in range(1980, 2021):

            # Creates folder 
            os.mkdir(os.path.join(output_path, str(season)))
        return True

    else:
        print("Files are already created")
        return False

'''
Function that creates a folder for each team, and creates a csv for there stats
'''
def csv_team_stats(format):

    # Create the season folders if needed to 
    create_season_folder()
    
    if(format == 'PER_GAME'):
        file_type = "Pergame"
        string_type = "pergame"

    elif(format == 'PER_POSS'):
        file_type = "Perposs"
        string_type = "perposs"

    elif(format == 'TOTAL'):
        file_type = "Total"
        string_type = "total"
    
    else:
        print("Please select insert the right format")
        return 0


    # Iterate through 1980 to 2020
    for year in range(1980, 2021):
        print(year)
        df = get_season_team_stats(year, format) 

        output_path = None
        final_path = None

        # Our file path 
        output_path = os.path.join(pathlib.Path().absolute(), "Output", "Team_Stats")
        print(output_path)

        # Create the final path that has format name
        final_path = os.path.join(output_path, str(year), file_type)
        print("final path is" + " " + final_path)

        if(os.path.isdir(final_path) == False):
            # Create the directory with the final_path
            #print("Now creating the pergame directory for this year")
            os.mkdir(final_path)
        else:
            #print("The file name pergame was created for this year")
            pass
        # Iterate through the len of the team column 
        for team in range(0, len(df['TEAM'])):
        
            # Call the get_team_stats that returns a dataframe a certin team stats from a given year
            team_df = get_team_stats(df.iloc[team, 0], year, format) 
    
            # Create a unique name for the file 
            file_name = "\\"+ str(year)+ "season"+ "_" + str(df.iloc[team, 0]) + "_" + string_type + ".csv"

            # Generate the CSV file in the propery directory 
            team_df.to_csv(final_path + file_name, index = False)
        

def get_team_csv(): 
    csv_team_stats('PER_GAME')
    csv_team_stats('PER_POSS')
    csv_team_stats('TOTAL')

'''
Main function generates csv files for the functions above
'''
def main():
    #get_season_csv()
    get_team_csv()

    
    return 0

if __name__ == "__main__":
    main()