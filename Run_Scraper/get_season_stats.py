#####################################################
# File:   get_team_stats.py
# Author: Bryan Delas Penas 
# Email:  bryan.delaspenas0405@gmail.com
# Date:   12/21/2020
# 
# Description: 
# This code gathers the season data for each team 
import sys 
import os
import pathlib 
from pathlib import Path

sys.path.append(str(pathlib.Path().absolute()) + '\\python_scrapers')

# Import modules 
from Season_Stats_Scraper import  get_team_name, get_standings
from helper import create_output_directory

'''
Generates a CSV file of team names for a season 
'''
def csv_team_name(year):
    # Check if the needed directory has been made  
    directory_source = "Season"
    directory_parent = "Team_Names"
    
    # Get the first file path
    first_path = first_path = os.path.join(pathlib.Path().absolute(), "Output", directory_source , directory_parent)
   
    # Call the scraper
    df = get_team_name(year)
    
    # Create a file name
    file_name = "\\" + str(year) + "_" + "Team_Names.csv"

    df.to_csv(first_path + file_name, index = False)

'''
Function that creates the csv for standings
'''
def csv_standings(year, format):
    
    valid = ['Standard', 'Expanded_Standings', 'Team_Vs_Team']

    # Change format to be uppercase 
    format = format.title()

    # There should only be three formats for the parameter format
    if format not in valid:
        print("Error: Please look at api.md for proper parameters")
        return None
    
    else:
       pass

    # Check if the proper directories has been made
    directory_source = "Output"
    directory_grand_parent = "Season"
    directory_parent = "Standings"
    directory_child = format

    first_path =  os.path.join(pathlib.Path().absolute(), directory_source , directory_grand_parent)

    if(not os.path.isdir(first_path)):
        # Create the directory with the final_path
        os.mkdir(first_path)
    else:
        pass
    
    # Create the final path that has format name
    second_path = os.path.join(first_path, directory_parent)
    if(not os.path.isdir(second_path)):
        
        # Create the directory with the final_path
        os.mkdir(second_path)
    else:
        pass

    # Create the final path that has format name
    final_path = os.path.join(second_path, directory_child)
    if(not os.path.isdir(final_path)):
        
        # Create the directory with the final_path
        os.mkdir(final_path)
    else:
        pass
        
    # If the format is standard get_standings will return two dataframes 
    if format == 'Standard':
        df_east, df_west = get_standings(year, format)

        # Output path for the two csv file
        west_output_path = os.path.join(final_path, "East")
        east_output_path = os.path.join(final_path, "West")

        if(not os.path.isdir(west_output_path)): 
            os.mkdir(west_output_path)
        else:
            pass

        if (not os.path.isdir(east_output_path)): 
            os.mkdir(east_output_path) 
        else:
            pass
        
        # Create a unique name for the two file 
        season_east = "\\"+ str(year)+ "season"+ "_" + "east" + "_" + format + ".csv"
        season_west = "\\"+ str(year)+ "season"+ "_" + "west" + "_" + format + ".csv"
    
        # Create the two csv file
        df_east.to_csv(west_output_path + season_east, index = False)
        df_west.to_csv(east_output_path + season_west, index = False)
    
    else:
        df = get_standings(year, format)
        
        # Create a unique name for the file 
        season = "\\"+ str(year)+ "season"+ "_" + format + ".csv"
        
        # Create the csv file
        df.to_csv(final_path + season, index = False)
    
'''
Functions that calls the three functions above that creates the csv 
'''
def get_season_csv():
    
    # Check if the proper directories has been made
    directory_parent = "Season"
    create_output_directory(directory_parent)
    
    #year = 1980
    # Iterate through the 1980 and 2020 season
    for year in range(1980, 2021):
        print(year)
        
        # Team Name
        csv_team_name(year)
        
        # Standing Stats
        csv_standings(year, 'STANDARD')
        csv_standings(year, 'expanded_standings')
        csv_standings(year, 'TEAM_VS_TEAM')

'''
Main function generates csv files for the functions above
'''
def main():
    get_season_csv()
    
if __name__ == "__main__":
    main()