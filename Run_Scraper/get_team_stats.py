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
from Team_Stats_Scraper import get_season_team_stats, get_team_stats, get_opp_stats, get_team_name

'''

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
Functions that calls the three functions above that creates the csv 
'''
def get_season_csv():
    
    # Iterate through the 1980 and 2020 season
    for year in range(1980, 2021):
        csv_season_stats(year, 'PER_GAME')
        csv_season_stats(year, 'PER_POSS')
        csv_season_stats(year, 'TOTAL')
        csv_team_name(year)
'''
Helper function that creates folders for each season 
'''
def create_team_stats_folder():
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
Function that creates a folder for each team, and creates a csv for there stats and a csv containing team names
'''
def csv_team_stats(format):

    # Create the season folders if needed to 
    create_team_stats_folder()
    
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
    
    # Check if the directory has been made
    directory_parent = "Team_Stats"
    create_output_directory(directory_parent)
    
    
    # Iterate through 1980 to 2020
    for year in range(1980, 2021):
        
        # Dataframe for season stats
        df = get_season_team_stats(year, format) 
        
        output_path = None
        final_path = None

        # Our file path 
        output_path = os.path.join(pathlib.Path().absolute(), "Output", directory_parent)
        # Create the final path that has format name
        final_path = os.path.join(output_path, str(year), file_type)

        if(os.path.isdir(final_path) == False):
            # Create the directory with the final_path
            os.mkdir(final_path)
        else:
            
            pass
        # Iterate through the len of the team column 
        for team in range(0, len(df['TEAM'])):
        
            # Call the get_team_stats that returns a dataframe a certin team stats from a given year
            team_df = get_team_stats(df.iloc[team, 0], year, format) 

            # Create a unique name for the file 
            file_name = "\\"+ str(year)+ "season"+ "_" + str(df.iloc[team, 0]) + "_" + string_type + ".csv"

            # Generate the CSV file in the propery directory 
            team_df.to_csv(final_path + file_name, index = False)
        
'''
Generates a CSV of each team in its own dir for each team
'''
def get_team_csv(): 
    csv_team_stats('PER_GAME')
    csv_team_stats('PER_POSS')
    csv_team_stats('TOTAL')

'''
Creates a new dirctory in the directory Output 
'''
def create_output_directory(format): 
    output_path = os.path.join(pathlib.Path().absolute(), "Output")
    
    # Check if the directory was already made
    if(os.path.isdir(os.path.join(output_path, format)) == False):
        os.mkdir(os.path.join(output_path,format))
        return True
    else:
        return False
    
'''
Creates a new directory in the parent_directory 
'''
def create_output_child_directory(parent_directory, format):
    output_path = os.path.join(pathlib.Path().absolute(), "Output", parent_directory)

    # Check if the directory was made
    if(os.path.isdir(os.path.join(output_path, format)) == False):
        os.mkdir(os.path.join(output_path,format))
        return True
    else:
        return False

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
    directory_parent = "Opponent_Season_Stats"
    create_output_directory(directory_parent)
    create_output_child_directory(directory_parent,file_name)

    # Call the scraper function
    df = get_opp_stats(year, format)
    df = df.round(2)
    
    # Output path for the csv file
    output_path = os.path.join(pathlib.Path().absolute(), "Output", "Opponent_Season_Stats", file_name)
        
    # Create a unique name for the file 
    season =  "\\"+ str(year)+ "season"+ "_" + string_type + ".csv"

    # Create the csv file
    df.to_csv(output_path + season, index = False)

    return 0

'''
Functions that gets the pergame, perposs and total opponent stats from 1980 to 2020
'''
def get_opp_csv():
    # Iterate through the 1980 and 2020 season
    for year in range(1980, 2021):
        csv_season_opp(year, 'PER_GAME')
        csv_season_opp(year, 'PER_POSS')
        csv_season_opp(year, 'TOTAL') 

'''
Main function generates csv files for the functions above
'''
def main():
    get_season_csv()
    #get_team_csv()
    #get_opp_csv()
    
    return 0

if __name__ == "__main__":
    main()