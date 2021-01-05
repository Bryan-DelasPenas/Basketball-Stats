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

# Import modules 
from Season_Stats_Scraper import get_season_team_stats, get_opp_stats, get_team_name
from helper import create_output_child_directory, create_output_directory

'''
Generates a CSV file of team names for a season 
'''
def csv_team_name(year):
    # Check if the needed directory has been made  
    directory_parent = "Season_Stats"
    directory_child = "Team_Names"
    create_output_directory(directory_parent)
    create_output_child_directory(directory_parent,directory_child)
    
    df = get_team_name(year)
    # Our file path 
    output_path = os.path.join(pathlib.Path().absolute(), "Output", directory_parent,directory_child)

    file_name = "\\" + str(year) + "teams.csv"

    df.to_csv(output_path + file_name, index = False)

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

    # Check if the directory has been made
    directory_parent = "Season_Stats"
    create_output_directory(directory_parent)
    create_output_child_directory(directory_parent,file_name)

    df = get_season_team_stats(year, format)
    df = df.round(2)
        
    # Output path for the csv file
    output_path = os.path.join(pathlib.Path().absolute(), "Output", directory_parent, file_name)
        
    # Create a unique name for the file 
    season =  "\\"+ str(year)+ "season"+ "_" + string_type + ".csv"

    # Create the csv file
    df.to_csv(output_path + season, index = False)

'''
Function that creates the csvs for opponent stats 
'''
def csv_season_opp(year, format):
    if(format == 'PER_GAME'):
        file_name = "Opp_Pergame_Stats"
        string_type = "pergame"
        

    elif(format == 'PER_POSS'):
        file_name = "Opp_Perposs_Stats"
        string_type = "perposs"

    elif(format == 'TOTAL'):
        file_name = "Opp_Total_Stats"
        string_type = "total"
    
    else:
        print("Please select insert the right format")
        return 0
    
    # Create the directory if not there
    directory_parent = "Season_Stats"
    create_output_directory(directory_parent)
    create_output_child_directory(directory_parent,file_name)

    # Call the scraper function
    df = get_opp_stats(year, format)
    df = df.round(2)
    
    # Output path for the csv file
    output_path = os.path.join(pathlib.Path().absolute(), "Output", directory_parent, file_name)
        
    # Create a unique name for the file 
    season =  "\\"+ str(year)+ "season"+ "_" + string_type + ".csv"

    # Create the csv file
    df.to_csv(output_path + season, index = False)

    return 0

'''
Functions that calls the three functions above that creates the csv 
'''
def get_season_csv():
    
    # Iterate through the 1980 and 2020 season
    for year in range(1980, 2021):
        csv_season_stats(year, 'PER_GAME')
        csv_season_stats(year, 'PER_POSS')
        csv_season_stats(year, 'TOTAL')
        csv_team_name(year)
        csv_season_opp(year, 'PER_GAME')
        csv_season_opp(year, 'PER_POSS')
        csv_season_opp(year, 'TOTAL') 

'''
Main function generates csv files for the functions above
'''
def main():
    get_season_csv()
    
    return 0

if __name__ == "__main__":
    main()