import pandas as pd
import os
import pathlib
from pathlib import Path


def create_team_id_dict():
    
    team_id_dict = {}
    path = os.path.join(pathlib.Path().absolute(), "Web_Scrapers",'Output', 'Season', 'Team_Names')
    team_files = os.listdir(path)
    count = 1980
    for team in team_files:
        
        # Convert file name into dataframes
        df = pd.read_csv(path + "\\" + team)
      
        # Create a list
        team_id_list = df['Team ID'].tolist()

        # Add it to the dict and increase count by 1
        team_id_dict[count] = team_id_list
        count+= 1
    return team_id_dict

def create_team_name_dict():
    
    team_name_dict = {}
    path = os.path.join(pathlib.Path().absolute(), "Web_Scrapers",'Output', 'Season', 'Team_Names')
    team_files = os.listdir(path)
    count = 1980
    for team in team_files:
        
        # Convert file name into dataframes
        df = pd.read_csv(path + "\\" + team)
      
        # Create a list
        team_name_list = df['Team'].tolist()

        # Add it to the dict and increase count by 1
        team_name_dict[count] = team_name_list
        count+= 1
    return team_name_dict

def create_team_abv_dict():
    
    team_abv_dict = {}
    path = os.path.join(pathlib.Path().absolute(), "Web_Scrapers",'Output', 'Season', 'Team_Names')
    team_files = os.listdir(path)
    count = 1980
    for team in team_files:
        
        # Convert file name into dataframes
        df = pd.read_csv(path + "\\" + team)
      
        # Create a list
        team_abv_list = df['Team ABV'].tolist()

        # Add it to the dict and increase count by 1
        team_abv_dict[count] = team_abv_list
        count+= 1
    return team_abv_dict

VALID_TEAM_IDS= create_team_id_dict()
VALID_TEAM_NAMES = create_team_name_dict()
VALID_TEAM_ABVS = create_team_abv_dict()
print(VALID_TEAM_ABVS)