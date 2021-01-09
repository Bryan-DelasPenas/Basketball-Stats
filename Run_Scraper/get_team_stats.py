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
from Team_Stats_Scraper import get_roster, get_team_stats, get_team_misc, get_team_advanced
from Season_Stats_Scraper import get_season_stats
from Team_Constants import TEAM_DICT
from helper import create_output_child_directory, create_output_directory


'''
Helper function that creates folders for each season 
'''
def create_team_stats_folder(location_parent, location):
    # The file path
    output_path = os.path.join(pathlib.Path().absolute(), "Output", "Team",location_parent, location)
    
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
Function that creates csv files of team roster 
'''
def csv_roster(year):

    # Directory name 
    directory_parent = "Team_Stats"
    
    # Dataframe for season stats
    df = get_season_stats(year) 

    output_path = None
    final_path = None

    # Our file path 
    output_path = os.path.join(pathlib.Path().absolute(), "Output", directory_parent)
    # Create the final path that has format name
    final_path = os.path.join(output_path, str(year), "Team_Roster")

    if(os.path.isdir(final_path) == False):
        # Create the directory with the final_path
        os.mkdir(final_path)
    else:
            
        pass
    # Iterate through the len of the team column 
    for team in range(0, len(df['TEAM'])):

        # Call the get_team_stats that returns a dataframe a certin team stats from a given year
        roster_df = get_roster(df.iloc[team, 2], year) 
        
        # Check if the roster_df is not none
        if(roster_df is not None):
            
            # Create a unique name for the file 
            file_name = "\\"+ str(year)+ "season" + "_" + str(df.iloc[team, 2]) + "_" + "roster" + ".csv"

            # Generate the CSV file in the propery directory 
            roster_df.to_csv(final_path + file_name, index = False)
        else:
            pass

'''
Function that creates a folder for each team, and creates a csv for there stats and a csv containing team names
'''
def csv_roster_stats(year, playoffs ,format):

    # The directory parents
    directory_parent = "Team_Stats"
    
    # Change format to be uppercase 
    format = format.upper()

    # Check if you are looking for playoff stats 
    if(playoffs == True):
        string_playoffs = "Playoffs"
        if(format == 'PER_GAME'):
            file_type = "Per_game"
            string_type = "per_game"

        elif(format == 'PER_POSS'):
            file_type = "Per_poss"
            string_type = "per_poss"

        elif(format == 'TOTALS'):
            file_type = "Totals"
            string_type = "totals"

        elif(format == 'PER_MINUTE'):
            file_type = "Per_Minute"
            string_type = "per_minute"

        elif(format == 'ADVANCED'):
            file_type = 'Advanced'
            string_type = "advanced"

        else:
            print("Please select insert the right format")
            return 0

    else:
        string_playoffs = "Regular"
        if(format == 'PER_GAME'):
            file_type = "Per_game"
            string_type = "per_game"

        elif(format == 'PER_POSS'):
            file_type = "Per_poss"
            string_type = "per_poss"

        elif(format == 'TOTALS'):
            file_type = "Totals"
            string_type = "totals"

        elif(format == 'PER_MINUTE'):
            file_type = "Per_Minute"
            string_type = "per_minute"

        elif(format == 'ADVANCED'):
            file_type = 'Advanced'
            string_type = "advanced"

        elif(format == 'ADJUSTED'): 
            file_type = 'Adjusted'
            string_type = "adjusted"

        else:
            print("Please select insert the right format")
            return 0
        
    # Dataframe for season stats
    df = get_season_team_stats(year) 
        
    # Init variables 
    output_path = None
    final_path = None

    # Our file path 
    output_path = os.path.join(pathlib.Path().absolute(), "Output", directory_parent)
    # Create the final path that has format name
    final_path = os.path.join(output_path, str(year), file_type + "_" + string_playoffs)

    if(os.path.isdir(final_path) == False):
        
        # Create the directory with the final_path
        os.mkdir(final_path)
    else:
        pass
    
    print(year)
    # Iterate through the len of the team column 
    for team in range(0, len(df['TEAM'])):
        
        # Call the get_team_stats that returns a dataframe a certin team stats from a given year, 2 is due to TEAM being the 3 column
        team_df = get_team_stats(df.iloc[team, 2], year, playoffs, format) 
        
        if(team_df is not None):
            
            # Create a unique name for the file 
            file_name = "\\"+ str(year)+ "season"+ "_" + str(df.iloc[team, 2]) + "_" + string_playoffs + "_" + string_type + ".csv"
                
            # Generate the CSV file in the propery directory 
            team_df.to_csv(final_path + file_name, index = False)

'''
Function that creates the csv for team misc stats
'''
def csv_team_stats(year, format):
    
    # Check if the needed directory has been made  
    directory_source = "Team"
    directory_parent = 'Team_Stats'
    directory_child = format
    
    # Dataframe for season stats
    df = get_season_stats(year) 
        
    # Init variables 
    first_path = None
    second_path = None
    final_path = None

    # Our file path 
    first_path = os.path.join(pathlib.Path().absolute(), "Output", directory_source , directory_parent)
    if(not os.path.isdir(first_path)):
        
        # Create the directory with the final_path
        os.mkdir(first_path)
    else:
        pass
    
    # Create the final path that has format name
    second_path = os.path.join(first_path, directory_child)
    if(not os.path.isdir(second_path)):
        
        # Create the directory with the final_path
        os.mkdir(second_path)
    else:
        pass
    
    # Create the season folders if needed to 
    create_team_stats_folder(directory_parent, directory_child)
    
    final_path = os.path.join(second_path, str(year))
    
    # Iterate through the len of the team column 
    for team in range(0, len(df['TEAM'])):
        
        # Call the scraper function
        if(format == 'Team_Misc' ):
            df_team = get_team_misc(df.iloc[team, 2], year)
        
        elif(format == 'Team_Advanced'):
            print(df.iloc[team, 2])
            # Try to see if the get_team_advanced is valid
            try:
                df_team = get_team_advanced(df.iloc[team, 2], year)
            except:
                print("Switching to newer team")
                flag = True
            # For past teams like SEA, all there stats are in the OKC page    
            if str(df.iloc[team, 2]) in TEAM_DICT and flag:
                new_team = TEAM_DICT[str(df.iloc[team, 2])]
                df_team = get_team_advanced(new_team, year)
        
        # Check if df_misc exist
        if(df_team is not None):
            
            # Create a unique name for the file 
            file_name = "\\"+ str(year)+ "_"+ format + "_" + str(df.iloc[team, 2]) + "_" + ".csv"
            
            # Generate the CSV file in the propery directory 
            df_team.to_csv(final_path + file_name, index = False)





'''
Generates a CSV of each team in its own dir for each team
'''
def get_team_csv(): 
    
    # Check if the directory has been made
    directory_parent = "Team"
    create_output_directory(directory_parent)

    
    # Iterate through 1980 to 2020
    for year in range(1980, 2021):

        # Roster Non-Playoff stats
        #csv_roster_stats(year, False, 'PER_GAME')
        #csv_roster_stats(year, False, 'PER_POSS')
        #csv_roster_stats(year, False, 'TOTALS')
        #csv_roster_stats(year, False, 'PER_MINUTE')
        #csv_roster_stats(year, False, 'ADVANCED')
        #csv_roster_stats(year, False, 'ADJUSTED')

        # Roster Playoff stats 
        #csv_roster_stats(year, True, 'PER_GAME')
        #csv_roster_stats(year, True, 'PER_POSS')
        #csv_roster_stats(year, True, 'TOTALS')
        #csv_roster_stats(year, True, 'PER_MINUTE')
        #csv_roster_stats(year, True, 'ADVANCED')

        # Roster Stats
    

        # Team Stats
        csv_team_stats(year, 'Team_Misc')
        csv_team_stats(year, 'Team_Advanced')

def main():
    get_team_csv()
    
if __name__ == "__main__":
    main()