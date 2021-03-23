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

PLAYED_FOR_TEAM = {
    1: []
}

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

VALID_SID_TEAM_IDS = create_team_id_dict()
