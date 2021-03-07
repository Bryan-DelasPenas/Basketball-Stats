import sys 
import os
import pathlib 
import time

sys.path.append(str(pathlib.Path().absolute()) + '\\Web_Scrapers' + '\\Python_Scrapers')

# Import modules 
from Team_Stats_Scraper import get_roster, get_team_stats, get_team_misc, get_opp_stats, get_team_advanced
from Team_Constants import TEAM_DICT
from helper import create_output_directory


'''
Helper function that creates folders for each season 
'''
def create_team_stats_folder_two(location_parent, location):
    # The file path
    output_path = os.path.join(pathlib.Path().absolute(), 'Web_Scrapers', "Output", "Team",location_parent, location)
    
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
Helper function to create a folder 
'''
def create_team_stats_folder(location):
    # The file path
    output_path = os.path.join(pathlib.Path().absolute(), 'Web_Scrapers', "Output", "Team", location)
    
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

    # Dataframe for season stats
    df = get_team_stats(year) 

    # Init variables 
    first_path = None
    final_path = None

    # Our file path 
    first_path = os.path.join(pathlib.Path().absolute(), 'Web_Scrapers', "Output", directory_source , directory_parent)
    if(not os.path.isdir(first_path)):
        
        # Create the directory with the final_path
        os.mkdir(first_path)
    else:
        pass
     
    final_path = os.path.join(first_path, str(year))
    if(not os.path.isdir(final_path)):
        create_team_stats_folder("Roster")
    
    # Iterate through the len of the team column 
    for team in range(0, len(df['Team ABV'])):

        # Call the get_roster that returns a dataframe a certin team stats from a given year
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
Function that creates the csv for team misc stats
'''
def csv_team_stats_other(year, format):
    
    # Check if the needed directory has been made  
    directory_source = "Team"
    directory_parent = 'Team_Stats'
    directory_child = format.title()
    
    # Dataframe for season stats
    df = get_team_stats(year) 
        
    # Init variables 
    first_path = None
    second_path = None
    final_path = None

    # Our file path 
    first_path = os.path.join(pathlib.Path().absolute(), 'Web_Scrapers', "Output", directory_source , directory_parent)
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
    format = format.title()
    
    # Iterate through the len of the team column 
    for team in range(0, len(df['Team ABV'])):
        
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
Function that get major teams averages 
'''
def csv_team_stats_main(year, format):
    
    valid = ['Per_Game', 'Per_Poss', 'Total', 'Team_Misc']
    format = format.title()
    
    # Check if the format 
    if(format not in valid):
        print("Please choose the right format")
        return None
    
    else:
        pass
    directory_source = "Team"
    directory_grand_parent = 'Team_Stats'
    directory_parent = "Team_Averages"
    directory_child = format.title()
    
    # Init variables 
    first_path = None
    second_path = None
    final_path = None

    # Our file path 
    first_path = os.path.join(pathlib.Path().absolute(), 'Web_Scrapers', "Output", directory_source , directory_grand_parent)
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
    final_path = os.path.join(second_path, directory_child)
    if(not os.path.isdir(final_path)):
        
        # Create the directory with the final_path
        os.mkdir(final_path)
    else:
        pass
    
    # Check for Team_Misc, it calls a different scraper
    if format == 'Team_Misc':
        df = get_team_misc(year)
    
    else:
        df = get_team_stats(year, format)
    
    # Create a unique name for the file 
    season =  "\\"+ str(year)+ "season" + "_" + format.title() + ".csv"

    # Create the csv file
    df.to_csv(final_path + season, index = False)

''' 
Function that gets major opponents averages 
'''
def csv_opponent_stats(year, format):
    valid = {'Per_Game': 'Opp_Per_Game', 'Per_Poss': 'Opp_Per_Poss', 'Total': 'Opp_Total'}
    format = format.title()
    
    # Check if the format 
    if(format not in valid):
        print("Please choose the right format")
        return None
    
    else:
        pass

    # Directory Names
    directory_source = "Team"
    directory_grand_parent = 'Team_Stats'
    directory_parent = "Opponent_Averages"
    directory_child = valid[format]
    
    # Init variables 
    first_path = None
    second_path = None
    final_path = None

    # Our file path 
    first_path = os.path.join(pathlib.Path().absolute(), 'Web_Scrapers', "Output", directory_source , directory_grand_parent)
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
    final_path = os.path.join(second_path, directory_child)
    if(not os.path.isdir(final_path)):
        
        # Create the directory with the final_path
        os.mkdir(final_path)
    else:
        pass
    
    df = get_opp_stats(year, format)
    
    # Create a unique name for the file 
    season =  "\\"+ str(year)+ "season" + "_" + format.title() + ".csv"

    # Create the csv file
    df.to_csv(final_path + season, index = False)

'''
Generates a CSV of each team in its own dir for each team
'''
def get_team_csv(): 
    
    # Check if the directory has been made
    directory_parent = "Team"
    create_output_directory(directory_parent)

    # Iterate through 1980 to 2020
    for year in range(1980, 2021):
        print(year)
    
        # Roster Names
        csv_team_roster(year)
        
        # Team Stats Main
        csv_team_stats_main(year, 'Per_Game')
        csv_team_stats_main(year, 'Per_Poss')
        csv_team_stats_main(year, 'Total')
       
        # Opponent Stats 
        csv_opponent_stats(year, 'PeR_GaMe')
        csv_opponent_stats(year, 'Per_Poss')
        csv_opponent_stats(year, 'Total')
        
        # Team Stats Other
        csv_team_stats_other(year, 'Team_Advanced')
        csv_team_stats_main(year, 'Team_Misc')

def main():

    start_time = time.time()
    get_team_csv()
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()