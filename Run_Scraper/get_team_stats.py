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
from Team_Stats_Scraper import get_season_team_stats, get_team_stats

'''
Generates a CSV file of teams per game stats since 1980
'''
def csv_pergame_stats():
    
    # Iterate through 1980 to 2020
    for year in range(1980, 2021):
        df = get_season_team_stats(year, 'PER_GAME')
        df = df.round(2)
        
        # Output path for the csv file
        output_path = r"C:\Users\Bryan\Desktop\Basketball-Stats\Output\Season_Stats\Team_Pergame_Stats"

        # Create a unique name for the file 
        season =  "\\"+ str(year)+ "season"+ "_" +"pergame" + ".csv"

        # Create the csv file
        df.to_csv(output_path + season, index = False)

'''
Generates a CSV file of teams per possion stats since 1980
'''
def csv_perposs_stats():

   # Iterate through 1980 to 2020
    for year in range(1980, 2021):
        df = get_season_team_stats(year, 'PER_POSS')
        df = df.round(2)
        
        # Output path for the csv file
        output_path = r"C:\Users\Bryan\Desktop\Basketball-Stats\Output\Season_Stats\Team_Perposs_Stats"

        # Create a unique name for the file 
        season =  "\\"+ str(year)+ "season"+ "_" +"perposs" + ".csv"

        # Create the csv file
        df.to_csv(output_path + season, index = False)

'''
Generates a CSV file of teams total stats since 1980
'''
def csv_total_stats():
 
 # Iterate through 1980 to 2020
    for year in range(1980, 2021):
        df = get_season_team_stats(year, 'TOTAL')
        df = df.round(2)
        
        # Output path for the csv file
        output_path = r"C:\Users\Bryan\Desktop\Basketball-Stats\Output\Season_Stats\Team_Total_Stats"

        # Create a unique name for the file 
        season =  "\\"+ str(year)+ "season"+ "_" + "Total" + ".csv"

        # Create the csv file
        df.to_csv(output_path + season, index = False)

'''
Functions that calls the three functions above that creates the csv 
'''
def season_csv():
    csv_pergame_stats()
    csv_perposs_stats()
    csv_total_stats()

'''
Helper function that creates folders for each season 
'''
def create_season_folder():
    # Our file path 
    output_path = r"C:\Users\Bryan\Desktop\Basketball-Stats\Output\Team_Stats"

    # If this is false, creates file else just print message
    if(os.path.isdir(r"C:\Users\Bryan\Desktop\Basketball-Stats\Output\Team_Stats\1980") == False):
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
def get_team_pergame_stats():

    # Create the season folders if needed to 
    create_season_folder()
    
    # Iterate through 1980 to 2020
    for year in range(1980, 2021):
        df = get_season_team_stats(2019, 'PER_GAME') 
        # Our file path 
        output_path = r"C:\Users\Bryan\Desktop\Basketball-Stats\Output\Team_Stats"

        # Update the path replaces "2019" with season
        update_path = os.path.join(output_path, str(year))

        # Create the final path that has "Pergame"
        final_path = os.path.join(update_path, "Pergame")
    
        if(os.path.isdir(final_path) == False):
            # Create the directory with the final_path
            print("Now creating the pergame directory for this year")
            os.mkdir(final_path)
        else:
            print("The file name pergame was created for this year")
    
        # Iterate through the len of the team column 
        for team in range(0, len(df['TEAM'])):
        
            # Call the get_team_stats that returns a dataframe a certin team stats from a given year
            team_df = get_team_stats(df.iloc[team, 0], year) 
    
            # Create a unique name for the file 
            file_name = "\\"+ str(year)+ "season"+ "_" + str(df.iloc[team, 0]) + "_" + "Pergame" + ".csv"

            # Generate the CSV file in the propery directory 
            team_df.to_csv(final_path + file_name, index = False)

'''
Main function generates csv files for the functions above
'''
def main():
    #season_csv()
    get_team_pergame_stats()
    return 0

if __name__ == "__main__":
    main()