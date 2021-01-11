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
from Season_Stats_Scraper import  get_team_name, get_standings
from helper import create_output_child_directory, create_output_directory

'''
Generates a CSV file of team names for a season 
'''
def csv_team_name(year):
    # Check if the needed directory has been made  
    directory_parent = "Season_Stats"
    directory_child = "Team_Names"
    create_output_child_directory(directory_parent,directory_child)
    
    df = get_team_name(year)
    # Our file path 
    output_path = os.path.join(pathlib.Path().absolute(), "Output", directory_parent,directory_child)

    file_name = "\\" + str(year) + "teams.csv"

    df.to_csv(output_path + file_name, index = False)


'''
Function that creates the csvs for opponent stats 
'''
def csv_season_opp(year, format):
    
    # Change format to be uppercase 
    format = format.upper()
    
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
Function that creates the csv for standings
'''
def csv_standings(year, format):
    
    # Change format to be uppercase 
    format = format.upper()

    # There should only be three formats for the parameter format
    if format == 'STANDARD':
        file_name = "Standard_Standings"
        string_type = "standard_stadings"

    elif format == 'EXPANDED_STANDINGS':
        file_name = "Expanded_Standings"
        string_type = "expanded_standings"

    elif format == 'TEAM_VS_TEAM':
        file_name = "Team_vs_Team"
        string_type = "team_vs_team"

    else:
        print("Error: Please look at api.md for proper parameters")
        return None

    # Check if the proper directories has been made
    directory_parent = "Season_Stats"
    create_output_child_directory(directory_parent,file_name)

    # If the format is standard get_standings will return two dataframes 
    if format == 'STANDARD':
        df_east, df_west = get_standings(year, format)

        # Output path for the two csv file
        output_path = os.path.join(pathlib.Path().absolute(), "Output", directory_parent, file_name)

        # Create a unique name for the two file 
        season_east = "\\"+ str(year)+ "season"+ "_" + "east" + "_" + string_type + ".csv"
        season_west = "\\"+ str(year)+ "season"+ "_" + "west" + "_" + string_type + ".csv"
    
        # Create the two csv file
        df_east.to_csv(output_path + season_east, index = False)
        df_west.to_csv(output_path + season_west, index = False)
    
    else:
        df = get_standings(year, format)
        
        # Output path for the csv file
        output_path = os.path.join(pathlib.Path().absolute(), "Output", directory_parent, file_name)
            
        # Create a unique name for the file 
        season = "\\"+ str(year)+ "season"+ "_" + string_type + ".csv"

        # Create the csv file
        df.to_csv(output_path + season, index = False)

'''
Functions that calls the three functions above that creates the csv 
'''
def get_season_csv():
    # Check if the proper directories has been made
    directory_parent = "Season_Stats"
    create_output_directory(directory_parent)

    # Iterate through the 1980 and 2020 season
    for year in range(1980, 2021):
        
        # Season Stats
        csv_season_stats(year, 'PER_GAME')
        csv_season_stats(year, 'PER_POSS')
        csv_season_stats(year, 'TOTAL')

        # Team Name
        csv_team_name(year)
        
        # Team Misc
        csv_team_misc(year)

        # Standing Stats
        csv_standings(year, 'STANDARD')
        csv_standings(year, 'EXPANDED_STANDINGS')
        csv_standings(year, 'TEAM_VS_TEAM')

        # Opponent Stats
        csv_season_opp(year, 'PER_GAME')
        csv_season_opp(year, 'PER_POSS')
        csv_season_opp(year, 'TOTAL') 

'''
Main function generates csv files for the functions above
'''
def main():
    get_season_csv()
    
if __name__ == "__main__":
    main()