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
from Team_Stats_Scraper import get_roster, get_roster_stats, get_team_stats, get_team_misc, get_team_advanced
from Season_Stats_Scraper import get_season_stats
from Team_Constants import TEAM_DICT
from helper import create_output_child_directory, create_output_directory


'''
Helper function that creates folders for each season 
'''
def create_team_stats_folder_two(location_parent, location):
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

def create_team_stats_folder_three(location_grand,location_parent, location):
    # The file path
    output_path = os.path.join(pathlib.Path().absolute(), "Output", "Team", location_grand, location_parent, location)
    
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
def csv_team_roster(year):

    # Directory name 
    directory_source = "Team"
    directory_parent = 'Roster'
    directory_child = "Team_Roster"

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
    create_team_stats_folder_two(directory_parent, directory_child)
    
    final_path = os.path.join(second_path, str(year))
    
    #
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
    
    # For checking format
    playoff_valid = ['PER_GAME', ' PER_POSS','TOTALS','PER_MINUTE', 'ADVANCED']
    regular_valid = ['PER_GAME', ' PER_POSS','TOTALS','PER_MINUTE', 'ADVANCED', 'ADJUSTED']

   # Directory name 
    directory_source = "Team"
    directory_grand_parent = 'Roster'
    directory_parent = "Roster_Stats"
    
    # Change format to be uppercase 
    format = format.upper()

    # Check if you are looking for playoff stats 
    if(playoffs):
        if(format in playoff_valid):
            pass
        else:
            print("Wrong Format")
            return None
        
        # This is for file name
        string_playoffs = "Playoffs"
  
        # This is for directory 
        directory_child = "Playoff_Stat"
        
    else:
        if(format in regular_valid):
            pass
        else:
            print("Wrong Format")
            return None
        
        # This is for file name
        string_playoffs = "Regular"

        # This is for the directory 
        directory_child = "Regular_Stat"
        
   # Init variables 
    first_path = None
    second_path = None
    third_path = None
    final_path = None

    # Our file path 
    first_path = os.path.join(pathlib.Path().absolute(), "Output", directory_source , directory_grand_parent)
    if(not os.path.isdir(first_path)):
        
        # Create the directory with the final_path
        os.mkdir(first_path)
    else:
        pass
    
    # Create the second path that has format name
    second_path = os.path.join(first_path, directory_parent)
    if(not os.path.isdir(second_path)):
        
        # Create the directory with the final_path
        os.mkdir(second_path)
    else:
        pass
    
    # Create the thrid path that has format name
    third_path = os.path.join(second_path, directory_child)
    if(not os.path.isdir(third_path)):
        
        # Create the directory with the final_path
        os.mkdir(third_path)
    else:
        pass

    # Create the season folders if needed to 
    create_team_stats_folder_three(directory_grand_parent, directory_parent, directory_child)
    
    # Creates another path for the year
    fourth_path = os.path.join(third_path, str(year))

    final_path = os.path.join(fourth_path, format.title())
    if(not os.path.isdir(final_path)):
        
        # Create the directory with the final_path
        os.mkdir(final_path)
    else:
        pass
    
    print(final_path)

    # Dataframe for season stats
    df = get_season_stats(year) 
    if playoffs:
        csv_roster_playoff_stats(year, format,df, final_path)

    else:
        csv_roster_regular_stats(year, format,df, final_path)

def csv_roster_playoff_stats(year, format, season_df, file_path):

    string_type = format.title()
    
    #Iterate through the len of the team column 
    for team in range(0, len(season_df['TEAM'])):
        
        # Call the get_team_stats that returns a dataframe a certin team stats from a given year, 2 is due to TEAM being the 3 column
        team_df = get_roster_stats(season_df.iloc[team, 2], year, True, format) 
        
        if(team_df is not None):
            
            # Create a unique name for the file 
            file_name = "\\"+ str(year)+ "season"+ "_" + str(season_df.iloc[team, 2]) + "_" + "Playoffs" + "_" + string_type + ".csv"
                
            # Generate the CSV file in the propery directory 
            team_df.to_csv(file_path + file_name, index = False)
    
def csv_roster_regular_stats(year, format, season_df, file_path):
    string_type = format.title()
    
    #Iterate through the len of the team column 
    for team in range(0, len(season_df['TEAM'])):
        
        # Call the get_team_stats that returns a dataframe a certin team stats from a given year, 2 is due to TEAM being the 3 column
        team_df = get_roster_stats(season_df.iloc[team, 2], year, False, format) 
        
        if(team_df is not None):
            
            # Create a unique name for the file 
            file_name = "\\"+ str(year)+ "season"+ "_" + str(season_df.iloc[team, 2]) + "_" + "Regular" + "_" + string_type + ".csv"
                
            # Generate the CSV file in the propery directory 
            team_df.to_csv(file_path + file_name, index = False)

'''
Function that creates the csv for team misc stats
'''
def csv_team_stats_ent(year, format):
    
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
    create_team_stats_folder_two(directory_parent, directory_child)
    
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

    year = 1981
    # Iterate through 1980 to 2020
    #for year in range(1980, 2021):

        # Roster Non-Playoff stats
    csv_roster_stats(year, False, 'PER_GAME')
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
        #csv_team_roster(year)

        # Team Stats
        #csv_team_stats(year, 'Team_Misc')
        #csv_team_stats(year, 'Team_Advanced')
    
def main():
    get_team_csv()
    
if __name__ == "__main__":
    main()