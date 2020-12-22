#####################################################
# File:   get_team_stats.py
# Author: Bryan Delas Penas 
# Email:  bryan.delaspenas0405@gmail.com
# Date:   12/21/2020
# 
#
#
import sys 
sys.path.append('\\Users\\Bryan\\Desktop\\Basketball-Stats\\python_scrapers')

from Team_Stats_Scraper import get_team_stats



def csv_team_stats():
    
    # Iterate through 1980 to 2020
    for year in range(1980, 2021):
        df = get_team_stats(year)
        df = df.round(2)
        
        # Output path for the csv file
        output_path = r"C:\Users\Bryan\Desktop\Basketball-Stats\Output\Team_Stats"

        # Create a unique name for the file 
        season =  "\\"+ str(year)+ "season"+ "_" + ".csv"

        # Create the csv file
        df.to_csv(output_path + season, index = False)


def main():
    csv_team_stats()
main()