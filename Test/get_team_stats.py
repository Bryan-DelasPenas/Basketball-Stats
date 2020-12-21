#####################################################
# File: Team_Constants.py 
# Author: Bryan Delas Penas 
# Email:  bryan.delaspenas0405@gmail.com
# Date:   12/21/2020
# 
#
#
import sys 
sys.path.append('\\Users\\Bryan\\Desktop\\Basketball-Stats\\python_scrapers')

from Team_Stats_Scraper import get_team_stats

def main():
    print(get_team_stats(2020))
main()