import pandas as pd
import os
import pathlib
from pathlib import Path

'''
List containing valid table names for Team_Stats_Minor 
'''
VALID_TABLE_TEAM_STATS_MINOR = [
    'Team_Advanced',
    'Team_Misc'
]

'''
Dict: Values is Table_Name and key is the valid columns
'''
VALID_COL_TEAM_STATS_MINOR = {
    'Team_Advanced' : ['Team_Wins', 'Team_Loses', 'Win_Lose_Percentage', 'Team_Finish', 'Simple_Rating_System',
        'Pace', 'Relative_Pace', 'Offensive_Rating', 'Relative_Offensive_Rating', 'Defensive_Rating', 'Relative_Defensive_Rating''Playoffs_Finish', 'Coaches'],
    
    'Team_Misc' : ['Team_Average_Age', 'Team_Wins', 'Team_Loses', 'Pythagorean_Wins', 'Pythagorean_Loses', 
        'Margin_Of_Victory', 'Strength_Of_Schedule', 'Simple_Rating_System', 'Offensive_Rating', 'Defensive_Rating', 'Net_Rating', 'Pace', 'Free_Throw_Attempt_Rate', 
        'Three_Point_Attempt_Rate', 'True_Shooting_Percentage', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 'Arena']
}

'''
List containing stats that stored in a string for Team_Stats_Minor 
'''
STRING_STATS_TEAM_STATS_MINOR = [
    'Team_Finish'
    'Playoffs_Finish', 
    'Coaches', 
    'Arena'
]

'''
List containing valid tables names for Team_Stats_Major
'''
VALID_TABLE_TEAM_STATS_MAJOR = [
    'Team_Per_Game',
    'Team_Per_Poss',
    'Team_Totals'
]

'''
Dict: Key is the table names and key is valid column names
'''
VALID_COL_TEAM_STATS_MAJOR = {
    'Team_Per_Game' : ['Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
        'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
        'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
        'Personal_Foul', 'Points'],
    
    'Team_Per_Poss' : ['Games_Played', 'Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
        'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
        'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
        'Personal_Foul', 'Points'] ,
    
    'Team_Totals' : ['Minutes_Played', 'Field_Goals_Made', 'Field_Goals_Attempted', 
        'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 'Two_Points_Attempted', 'Two_Points_Percentage', 
        'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 'Offensive_Rebound', 'Defensive_Rebound', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 
        'Personal_Foul', 'Points'],
}

'''
List containing valid table names for career player stats
'''
VALID_TABLE_PLAYER_CAREER_STATS = [
    "Player_Career_Advanced",
    "Player_Career_Per_Game",
    "Player_Career_Per_Minute",
    "Player_Career_Per_Poss",
    "Player_Career_Totals"
]

'''
List containing valid table names for primary queries for player career 
'''
VALID_TABLE_PRIMARY_PLAYER_CAREER_STATS = [
    "Player_Career_Per_Game",
    "Player_Career_Per_Minute",
    "Player_Career_Per_Poss",
    "Player_Career_Totals"
]

'''
Dict: Key is the table names and key is valid column names
'''
VALID_COL_PLAYER_CAREER_STATS = {
    "Player_Career_Advanced" : ['Games_Played', 'Minutes_Played', 'Per_Minute_Production', 
        'True_Shooting_Percent', 'Three_Points_Attempted', 'Free_Throws_Per_Field_Goals', 'Offensive_Rebound_Percentage', 'Defensive_Rebound_Percentage', 
        'True_Rebounds_Percentage', 'Assit_Percentage', 'Steal_Percentage', 'Block_Percentage', 'Turn_Over_Percentage', 'Usage_Percentage', 'Offensive_Win_Shares', 
        'Defensive_Win_Shares', 'Win_Shares', 'Win_Shares_Fourty_Eight', 'Offensive_Box_Score', 'Defensive_Box_Score', 'Box_Plus_Minus', 'Value_Over_Replacement', 'Stat_Form'],
    
    "Player_Career_Per_Game" : ['Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Stat_Form'],
    
    "Player_Career_Per_Minute" : ['Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage',  'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Stat_Form'],
    
    "Player_Career_Per_Poss" : ['Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Offensive_Rating',
        'Defensive_Rating','Stat_Form'],
    
    "Player_Career_Totals" : ['Games_Played', 'Games_Started', 'Minutes_Played', 'Field_Goals_Made', 
        'Field_Goals_Attempted', 'Field_Goals_Percentage', 'Three_Points_Made', 'Three_Points_Attempted', 'Three_Points_Percentage', 'Two_Points_Made', 
        'Two_Points_Attempted', 'Two_Points_Percentage', 'Effective_Field_Goal_Percentage', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throws_Percentage', 
        'Offensive_Rebounds', 'Defensive_Rebounds', 'True_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turn_Over', 'Personal_Fouls', 'Points', 'Triple_Double','Stat_Form']
}

'''
Function that creates VALID_SID_TEAM_IDS
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

'''
Function that cretes PLAYED_FOR_TEAM
'''
def played_for_team():
    temp_dict = {}
    path = os.path.join(pathlib.Path().absolute(), 'Database', 'Python Scripts', 'Call_Queries', 'Played_For_Teams')
    team_csv = os.listdir(path)

    for team in team_csv:
        # Convert file name into dataframes
        df_played = pd.read_csv(path + "\\" + team)
    
        team_id_list = df_played['Team_ID'].tolist()
        player_id_list = df_played['Player_ID'].tolist()

        temp_dict[team_id_list[0]] = player_id_list 
        
    return temp_dict

'''
Dict: That has team_id has key and value is the player_ids
'''
PLAYED_FOR_TEAM_ID = played_for_team()

'''
Dict: That has season for the key and for the values a list of team_ids
Key:Values
season_id: [team_id]
'''
VALID_SID_TEAM_IDS = create_sid_team_id_dict()
