import pandas as pd
import os
import pathlib
from pathlib import Path

'''
UPDATE_NAME = {
    3: 
    4:
    13:
    15:
    19:
    21:
    26:
    29:
    30:
}
'''

def create_sid_team_id_dict():
    
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

def played_for_team():
    temp_dict = {}
    path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Call_Queries', 'Played_For_Teams')
    team_csv = os.listdir(path)

    for team in team_csv:
        # Convert file name into dataframes
        df = pd.read_csv(path + "\\" + team)

        team_abv_list = df['Team_ABV'].tolist()
        player_name_list = df['Player_Name'].tolist()

        temp_dict[team_abv_list[0]] = player_name_list 

    return temp_dict

PLAYED_FOR_TEAM_ABV = played_for_team()
VALID_SID_TEAM_IDS = create_sid_team_id_dict()
