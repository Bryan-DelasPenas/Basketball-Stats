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

from Team_Stats_Scraper import get_team_stats

'''
Generates a CSV file of teams per game stats since 1980
'''
def csv_pergame_stats():
    
    # Iterate through 1980 to 2020
    for year in range(1980, 2021):
        df = get_team_stats(year, 'PER_GAME')
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
        df = get_team_stats(year, 'PER_POSS')
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
        df = get_team_stats(year, 'TOTAL')
        df = df.round(2)
        
        # Output path for the csv file
        output_path = r"C:\Users\Bryan\Desktop\Basketball-Stats\Output\Season_Stats\Team_Total_Stats"

        # Create a unique name for the file 
        season =  "\\"+ str(year)+ "season"+ "_" + "Total" + ".csv"

        # Create the csv file
        df.to_csv(output_path + season, index = False)
'''
Main function generates csv files for the functions above
'''
def main():
    csv_pergame_stats()
    csv_perposs_stats()
    csv_total_stats()
main()