import os
import pathlib 
from pathlib import Path
import sys
import time
sys.path.append(str(pathlib.Path().absolute()) + '\\Web_Scrapers' + '\\Python_Scrapers')

# Import modules 
from Season_Stats_Scraper import  get_team_name, get_standings, get_award_voting
from helper import create_output_directory, create_years_dir

'''
Generates a CSV file of team names for a season 
'''
def csv_team_name(year):
    # Check if the needed directory has been made  
    directory_source = "Season"
    directory_parent = "Team_Names"
    
    # Get the first file path
    first_path = first_path = os.path.join(pathlib.Path().absolute(), "Web_Scrapers", "Output", directory_source , directory_parent)
    if(not os.path.isdir(first_path)):
        
        # Create the directory with the final_path
        os.mkdir(first_path)
    else:
        pass
    # Call the scraper
    df = get_team_name(year)
    
    # Create a file name
    file_name = "\\" + str(year) + "_" + "Team_Names.csv"

    df.to_csv(first_path + file_name, index = False)

'''
Function that creates the csv for standings
'''
def csv_standings(year, format):
    
    valid_format = ['Standard']

    # Change format to be uppercase 
    format = format.title()

    # There should only be three formats for the parameter format
    if format not in valid_format:
        print("Error: Please look at WebScraper_UserManual for the right parameters")
        return None
    
    # Check if the proper directories has been made
    directory_source = "Web_Scrapers\Output"
    directory_grand_parent = "Season"
    directory_parent = "Standings"

    first_path =  os.path.join(pathlib.Path().absolute(), directory_source , directory_grand_parent)

    if(not os.path.isdir(first_path)):
        # Create the directory with the final_path
        os.mkdir(first_path)

    # Create the final path that has format name
    second_path = os.path.join(first_path, directory_parent)
    if(not os.path.isdir(second_path)):
        
        # Create the directory with the final_path
        os.mkdir(second_path)
  
    # If the format is standard get_standings will return two dataframes 
    if format == 'Standard':
        df_east, df_west = get_standings(year, format)

        # Output path for the two csv file
        west_output_path = os.path.join(second_path, "East")
        east_output_path = os.path.join(second_path, "West")

        if(not os.path.isdir(west_output_path)): 
            os.mkdir(west_output_path)
       
        if (not os.path.isdir(east_output_path)): 
            os.mkdir(east_output_path) 
    
        # Create a unique name for the two file 
        season_east = "\\"+ str(year)+ "season"+ "_" + "east" + "_" + format + ".csv"
        season_west = "\\"+ str(year)+ "season"+ "_" + "west" + "_" + format + ".csv"
    
        # Create the two csv file
        df_east.to_csv(west_output_path + season_east, index = False)
        df_west.to_csv(east_output_path + season_west, index = False)
    
'''
Function that creates the csv for award voting
'''
def csv_award_voting(year, format):
    valid_format = ['MVP', 'ROY']
    # Change format to be uppercase 
    format = format.upper()
    
    # There should only be three formats for the parameter format
    if format not in valid_format:
        print("Error: Please look at WebScraper_UserManual for the right parameters")
        return None

    # ... src/Web_Scrapers/Output/Season
    first_path =  os.path.join(pathlib.Path().absolute(),"Web_Scrapers\Output\Season")
    if(not os.path.isdir(first_path)):
        
        # Create the directory with the first_path
        os.mkdir(first_path)

    # ... src/Web_Scrapers/Output/Season/Award_Voting
    second_path = os.path.join(first_path, "Award_Voting")
    if(not os.path.isdir(second_path)):
        
        # Create the directory with the second_path
        os.mkdir(second_path)

    # ... src/Web_Scrapers/Output/Season/Award_Voting/{format}
    format_path = os.path.join(second_path, format)
    if(not os.path.isdir(format_path)):
        
        # Create the directory with the final_path
        os.mkdir(format_path)

    # Create 1980 - 2020 dir 
    create_years_dir(format_path)

    final_path = os.path.join(format_path, str(year))
    df = get_award_voting(year, format)

    file_name = "\\"+ str(year)+ "season"+ "_" + str(format) + ".csv" 
    df.to_csv(final_path + file_name, index = False)

'''
Functions that calls the three functions above that creates the csv 
'''
def get_season_csv():
    
    # Check if the proper directories has been made
    directory_parent = "Season"
    create_output_directory(directory_parent)
    
    # Iterate through the 1980 and 2020 season
    for year in range(1980, 2021):
        print(year)
        
        # Team Name
        csv_team_name(year)
        
        # Standing Stats
        csv_standings(year, 'STANDARD')

'''
Main Function
'''
def main():

    start_time = time.time()
    csv_award_voting(2020, 'MVP')
    #get_season_csv()
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()