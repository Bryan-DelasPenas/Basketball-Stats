import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

import sys
import os
import pathlib 
from pathlib import Path

sys.path.append(str(pathlib.Path().absolute()) + '\\Web_Scrapers' +'\\Python_Scrapers')
from Team_Constants import RIGHT_NAME_DICT, PLAYER_ID

'''
Creates database connection and returns the engine
'''
def create_connection():
    connection_url = 'mysql+pymysql://bryan:bdelasp1@localhost:3306/BasketBallDB'
    engine = sal.create_engine(connection_url)
    
    return engine

'''
Function that tests the connection of the database
'''
def test_connection(engine):
    # Test the connection of the database
    try:
        conn = engine.connect()
        print("Connected to BasketBall Database")
        return conn

    except:
        raise Exception("Did not connect to BasketBall Database")

'''
Function that test to see if the table has been created
'''
def check_table(tablename):
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Test to see if the table exists
    test = conn.execute(
    """
    SHOW TABLES 
    LIKE %s
    """, tablename
    ).fetchall()    
    trans.commit()
    
    # Check if the list is empty 
    if test:
        print("Table exists")
        return True
    
    else:
        print("Table does not exists")
        return False

'''
Function that inserts Season Entities into database
'''
def insert_season(season_id):
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists 
    if(check_table('Season')):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            INSERT INTO Season(Season_ID)
            VALUES(%s)
            """, season_id)
            trans.commit()
            print("Insertion into Season was successful")
        except:
            raise Exception("Insertion into Season failed")
    else:
        raise Exception("Table does not exists")

'''
Function that inserts Teams Entities into database
'''
def insert_team(df):
    # Rename the dataframe 
    df = df.rename(columns={"Season" : "Season_ID",  "Team ID" : "Team_ID" , "Team" : "Team_Name", "Team ABV" : "Team_ABV"})
    
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()

    if(check_table('Team')):
        # Test to see if the insertion works 
        try:
            df.to_sql('team', con = engine, if_exists='append', index = False)
            trans.commit()
            print("Insertion into Team was successful")
        
        except:
            raise Exception("Insertion into Team failed")
    else:
        raise Exception("Table does not exists")

'''
Function that inserts Player Entities into database
'''
def insert_player(df):    
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()
    
    if(check_table('Team')):
        # Test to see if the insertion works 
        try:
            df.to_sql('player', con = engine, if_exists='append', index = False)
            trans.commit()
            print("Insertion into Player was successful")
        
        except:
            raise Exception("Insertion into Player failed")
    else:
        raise Exception("Table does not exist")

'''
Function that inserts Standings Entities into database
'''
def insert_standings(df):
    # Rename the dataframe 
    df = df.rename(columns={"Season" : "Season_ID",  "Team ID" : "Team_ID" , "Team" : "Team_Name", "Team ABV" : "Team_ABV"})
    
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()

    if(check_table('Standings')):
        # Test to see if the insertion works 
        try:
            df.to_sql('standings', con = engine, if_exists='append', index = False)
            trans.commit()
            print("Insertion into Team was successful")
        
        except:
            raise Exception("Insertion into Team failed")
    else:
        raise Exception("Table does not exists")

'''
Function that inserts Conference Standings into database
'''
def insert_conference_standings(df):
     # Rename the dataframe 
    df = df.rename(columns={"Season" : "Season_ID",  "Team ID" : "Team_ID" , "Team ABV" : "Team_ABV", "Team" : "Team_Name",
                            "W" : "Wins", "L" : "Loses", "W/L%" : "Win_Lose_Percentage", "GB" : "Games_Behind", "PS/G" : "Points_Per_Game", 
                            "PA/G" : "Opponents_Points_Per_Game", "SRS" : "Simple_Rating_System"})
    
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()
    if(check_table('Conference_Standings')):
        # Test to see if the insertion works 
        try:
            df.to_sql('conference_standings', con = engine, if_exists='append', index = False)
            trans.commit()
            print("Insertion into Team was successful")
        
        except:
            raise Exception("Insertion into Team failed")
    else:
        raise Exception("Table does not exists")

'''
Function that inserts Expanded Standings into database
'''
def insert_expanded_standings():
    return None

'''
Function that inserts Team Vs Team into database
'''
def insert_team_vs_team():
    return None

'''
Function that inserts Roster into database
'''
def insert_roster(df):
    # Rename the dataframe 
    df = df.rename(columns={"Season" : "Season_ID",  "Team ID" : "Team_ID", "Player ID" : "Player_ID", "Team ABV" : "Team_ABV", "Team" : "Team_Name", "Number" : "Player_Number",
                            "Player": "Player_Name", "Pos" : "Player_Postion", "Height" : "Player_Height", "Weight" : "Player_Weight", "Birth Date" : "Birth_Date", 
                            "Nationality" : "Player_Nationality", "Experience" : "Player_Experience", "College" : "Player_College_Name"})
    
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()

    if(check_table('Roster')):
        # Test to see if the insertion works 
        try:
            df.to_sql('roster', con = engine, if_exists='append', index = False)
            trans.commit()
            print("Insertion into Roster was successful")
        
        except:
            raise Exception("Insertion into Roster failed")
    else:
        raise Exception("Roster does not exists")

'''
Function that inserts Team_Stats into database
'''
def insert_team_stats(df):
    # Rename the dataframe 
    df = df.rename(columns={"Season" : "Season_ID",  "Team ID" : "Team_ID" , "Team ABV" : "Team_ABV", "Team" : "Team_Name"})
    
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()

    if(check_table('Team_Stats')):
        # Test to see if the insertion works 
        try:
            df.to_sql('team_stats', con = engine, if_exists='append', index = False)
            trans.commit()
            print("Insertion into Team_Stats was successful")
        
        except:
            raise Exception("Insertion into Team_Stats failed")
    else:
        raise Exception("Table does not exists")

'''
Function that inserts Team_Advanced into database
'''
def insert_team_advanced(df):
    
    df = df.rename(columns={"Season" : "Season_ID",  "Team ID" : "Team_ID" , "Team ABV" : "Team_ABV", "Team" : "Team_Name", "W" : "Team_Wins", "L": "Team_Loses",
                            "W/L%" : "Win_Lose_Percentage", "Finish" : "Team_Finish", "SRS" : "Simple_Rating_System", "Pace" : "Pace", "Rel Pace" : "Relative_Pace",
                            "ORtg" : "Offensive_Rating", "Rel ORtg" : "Relative_Offensive_Rating", "DRtg" : "Defensive_Rating", "Rel DRtg" : "Relative_Defensive_Rating",
                            "Playoffs" : "Playoffs_Finish", "Coaches" : "Coaches"})
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()

    if(check_table('Team_Advanced')):
        # Test to see if the insertion works 
        try:
            df.to_sql('team_advanced', con = engine, if_exists='append', index = False)
            trans.commit()
            print("Insertion into Team_Advanced was successful")
        
        except:
            raise Exception("Insertion into Team_Advanced failed")
    else:
        raise Exception("Table does not exists")

'''
Function that inserts Team_Misc into database
'''
def insert_team_misc(df):
    df = df.rename(columns={"Season" : "Season_ID",  "Team ID" : "Team_ID", "Team ABV" : "Team_ABV", "Team" : "Team_Name", "Age" : "Team_Average_Age", "W" : "Team_Wins",
                            "L" : "Team_Loses", "PW" : "Pythagorean_Wins", "PL" : "Pythagorean_Loses", "MOV" : "Margin_Of_Victory", "SOS" : "Strength_Of_Schedule",
                            "SRS" : "Simple_Rating_System", "ORtg": "Offensive_Rating", "DRtg" : "Defensive_Rating", "NRtg" : "Net_Rating", "Pace" : "Pace", "FTr" : "Free_Throw_Attempt_Rate",
                            "3PAr" : "Three_Point_Attempt_Rate", "TS%" : "True_Shooting_Percentage", "ORB%" : "Offensive_Rebound_Percentage", "DRB%" : "Defensive_Rebound_Percentage",
                            "Arena" : "Arena", "Attend." : "Attend", "Attend./G" : "Attend_Per_Game"})
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()

    if(check_table('Team_Misc')):
        # Test to see if the insertion works 
        try:
            df.to_sql('team_misc', con = engine, if_exists='append', index = False)
            trans.commit()
            print("Insertion into Team_Misc was successful")
        
        except:
            raise Exception("Insertion into Team_Misc failed")
    else:
        raise Exception("Table does not exists")

'''
Function that inserts Team_Per_Game into database
'''
def insert_team_per_game(df, opponent):
    df = df.rename(columns={"Season" : "Season_ID",  "Team ID" : "Team_ID", "Team ABV" : "Team_ABV", "Team" : "Team_Name", "G" : "Games_Played", "MP" : "Minutes_Played",
                            "FG" : "Field_Goals_Made", "FGA" : "Field_Goals_Attempted", "FG%" : "Field_Goals_Percentage", "3P" : "Three_Points_Made", "3PA" : "Three_Points_Attempted",
                            "3P%" : "Three_Points_Percentage", "2P" : "Two_Points_Made", "2PA" : "Two_Points_Attempted", "2P%" : "Two_Points_Percentage", "FT" : "Free_Throws_Made", 
                            "FTA" : "Free_Throws_Attempted", "FT%" : "Free_Throws_Percentage", "ORB" : "Offensive_Rebound", "DRB" : "Defensive_Rebound", "TRB" : "True_Rebound", 
                            "AST" : "Assists", "STL" : "Steals", "BLK" : "Blocks", "TOV" : "Turn_Over", "PF" : "Personal_Foul", "PTS" : "Points"})
    
    df['Opponent'] = opponent
    
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()

    if(check_table('Team_Per_Game')):
        # Test to see if the insertion works 
        try:
            df.to_sql('team_per_game', con = engine, if_exists='append', index = False)
            trans.commit()
            print("Insertion into Team_Per_Game was successful")
        
        except:
            raise Exception("Insertion into Team_Per_Game failed")
    else:
        raise Exception("Table does not exists")

'''
Function that inserts Team_Per_Poss into database
'''
def insert_team_per_poss(df, opponent):
    df = df.rename(columns={"Season" : "Season_ID",  "Team ID" : "Team_ID", "Team ABV" : "Team_ABV", "Team" : "Team_Name", "G" : "Games_Played", "MP" : "Minutes_Played",
                            "FG" : "Field_Goals_Made", "FGA" : "Field_Goals_Attempted", "FG%" : "Field_Goals_Percentage", "3P" : "Three_Points_Made", "3PA" : "Three_Points_Attempted",
                            "3P%" : "Three_Points_Percentage", "2P" : "Two_Points_Made", "2PA" : "Two_Points_Attempted", "2P%" : "Two_Points_Percentage", "FT" : "Free_Throws_Made", 
                            "FTA" : "Free_Throws_Attempted", "FT%" : "Free_Throws_Percentage", "ORB" : "Offensive_Rebound", "DRB" : "Defensive_Rebound", "TRB" : "True_Rebound", 
                            "AST" : "Assists", "STL" : "Steals", "BLK" : "Blocks", "TOV" : "Turn_Over", "PF" : "Personal_Foul", "PTS" : "Points"})
    
    df['Opponent'] = opponent
    
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()

    if(check_table('Team_Per_Poss')):
        # Test to see if the insertion works 
        try:
            df.to_sql('team_per_poss', con = engine, if_exists='append', index = False)
            trans.commit()
            print("Insertion into Team_Per_Poss was successful")
        
        except:
            raise Exception("Insertion into Team_Per_Poss failed")
    else:
        raise Exception("Table does not exists")

'''
Function that inserts Team_totals into database
'''
def insert_team_totals(df, opponent):
    df = df.rename(columns={"Season" : "Season_ID",  "Team ID" : "Team_ID", "Team ABV" : "Team_ABV", "Team" : "Team_Name", "G" : "Games_Played", "MP" : "Minutes_Played",
                            "FG" : "Field_Goals_Made", "FGA" : "Field_Goals_Attempted", "FG%" : "Field_Goals_Percentage", "3P" : "Three_Points_Made", "3PA" : "Three_Points_Attempted",
                            "3P%" : "Three_Points_Percentage", "2P" : "Two_Points_Made", "2PA" : "Two_Points_Attempted", "2P%" : "Two_Points_Percentage", "FT" : "Free_Throws_Made", 
                            "FTA" : "Free_Throws_Attempted", "FT%" : "Free_Throws_Percentage", "ORB" : "Offensive_Rebound", "DRB" : "Defensive_Rebound", "TRB" : "True_Rebound", 
                            "AST" : "Assists", "STL" : "Steals", "BLK" : "Blocks", "TOV" : "Turn_Over", "PF" : "Personal_Foul", "PTS" : "Points"})
    
    df['Opponent'] = opponent
    
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()

    if(check_table('Team_Totals')):
        # Test to see if the insertion works 
        try:
            df.to_sql('team_totals', con = engine, if_exists='append', index = False)
            trans.commit()
            print("Insertion into Team_Totals was successful")
        
        except:
            raise Exception("Insertion into Team_Totals failed")
    else:
        raise Exception("Table does not exists")

def insert_player_stats():
    return None

def insert_player_advanced():
    return None

def insert_player_per_game():
    return None

def insert_player_per_minute():
    return None

def insert_player_per_poss():
    return None

def insert_player_per_totals():
    return None

'''
Calls insert_season to insert years 1980 - 2020
'''
def insert_all_season():
    for i in range(1980, 2021):
        insert_season(i)

'''
Calls insert_team to insert all teams from 1980 - 2020
'''
def insert_all_team():
    path = os.path.join(pathlib.Path().absolute(), "Output", "Season", "Team_Names")
    
    # Iterate through the years directory
    for i in range(1980, 2021):
        print(i)
        final_path = os.path.join(path, str(i) + "_Team_Names.csv")
        df = pd.read_csv(final_path)

        # Add Total After Trade
        df.loc[len(df.index)] = [i, 31, "Total After Trade", "TOT"]
        
        insert_team(df)
    
'''
Calls insert_players to insert all player active 1980 - 2020
'''
def insert_all_players():
    path = os.path.join(pathlib.Path().absolute(), "Output", "Player_Name", "player_names.csv")
    df = pd.read_csv(path)

    df = df.values.tolist()

    for x in range(len(df)):
        name_tuple = (df[x][0], df[x][1])

        if(name_tuple in RIGHT_NAME_DICT):
            df[x][0] = RIGHT_NAME_DICT[name_tuple]


        df[x].append(PLAYER_ID[df[x][0]])

    final_df = pd.DataFrame(df, columns=['Player_Name', 'Birth_Date', 'Player_ID'])
    final_df = final_df[ ['Player_Name'] + [ col for col in final_df.columns if col != 'Player_Name' ] ]
    final_df = final_df[ ['Birth_Date'] + [ col for col in final_df.columns if col != 'Birth_Date' ] ]
    final_df = final_df[ ['Player_ID'] + [ col for col in final_df.columns if col != 'Player_ID' ] ]

    insert_player(final_df)
    
'''
Calls insert_standings to insert all standings from 1980 - 2020
'''
def insert_all_standings():
    path = os.path.join(pathlib.Path().absolute(), "Output", "Season", "Team_Names")
    
    # Iterate through the years directory
    for i in range(1980, 2021):
        print(i)
        final_path = os.path.join(path, str(i) + "_Team_Names.csv")
        df = pd.read_csv(final_path)

        insert_standings(df)

'''
Calls insert_conference_standings from 1980 - 2020
'''
def insert_all_conference_standings():
    east_path = os.path.join(pathlib.Path().absolute(), "Output", "Season", "Standings", "Standard", "East")
    west_path = os.path.join(pathlib.Path().absolute(), "Output", "Season", "Standings", "Standard", "West")
    
    # Iterate through the years
    for i in range(1980, 2021):
        print(i)
        final_east_path = os.path.join(east_path, str(i) + "season_east_Standard.csv")
        final_west_path = os.path.join(west_path, str(i) + "season_west_Standard.csv")
        
        df_east = pd.read_csv(final_east_path)
        df_west = pd.read_csv(final_west_path)

        # 0 = east
        # 1 = west
        df_east['East_Or_West'] = 0
        df_west['East_Or_West'] = 1
       
        insert_conference_standings(df_east)
        insert_conference_standings(df_west)

'''
Calls insert_roster from 1980 - 2020
'''
def insert_all_roster():
    path = os.path.join(pathlib.Path().absolute(), "Output","Team", "Roster", "Team_Roster")

    for i in range(1980, 2021):
        second_path = os.path.join(path, str(i))
       
        csv_files = os.listdir(second_path)

        for x in range(len(csv_files)):
            final_path = os.path.join(second_path, csv_files[x])
            df = pd.read_csv(final_path)
            insert_roster(df)

'''
Call insert_standings from 1980 - 2020
'''
def insert_all_team_stats():
    path = os.path.join(pathlib.Path().absolute(), "Output", "Season", "Team_Names")
    
    # Iterate through the years directory
    for i in range(1980, 2021):
        print(i)
        final_path = os.path.join(path, str(i) + "_Team_Names.csv")
        df = pd.read_csv(final_path)
        df = df[['Season', 'Team ID', 'Team', 'Team ABV']]
        
        insert_team_stats(df)

'''
Call insert_team_advanced from 1980 - 2020
'''
def insert_all_team_advanced():
    path = os.path.join(pathlib.Path().absolute(), "Output","Team", "Team_Stats", "Team_Advanced")

    for i in range(1980, 2021):
        second_path = os.path.join(path, str(i))
       
        csv_files = os.listdir(second_path)

        for x in range(len(csv_files)):
            final_path = os.path.join(second_path, csv_files[x])
            df = pd.read_csv(final_path)
            insert_team_advanced(df)

'''
Call insert_team_misc from 1980 - 2020
'''
def insert_all_team_misc():
    path = os.path.join(pathlib.Path().absolute(), "Output", "Team", "Team_Stats", "Team_Averages", "Team_Misc")
    
    # Iterate through the years directory
    for i in range(1980, 2021):
        print(i)
        final_path = os.path.join(path, str(i) + "season_Team_Misc.csv")
        df = pd.read_csv(final_path)
        
        insert_team_misc(df)

'''
Call insert_team_per_game from 1980 - 2020
'''
def insert_all_team_per_game():
    regular_path = os.path.join(pathlib.Path().absolute(), "Output", "Team", "Team_Stats", "Team_Averages", "Per_Game")
    opponent_path = os.path.join(pathlib.Path().absolute(), "Output", "Team", "Team_Stats", "Opponent_Averages", "Opp_Per_Game")

    # Iterate through the years directory
    for i in range(1980, 2021):
        print(i)
        final_regular_path = os.path.join(regular_path, str(i) + "season_Per_Game.csv")
        final_opponent_path = os.path.join(opponent_path, str(i) + "season_Per_Game.csv")
        
        regular_df = pd.read_csv(final_regular_path)
        opponent_df = pd.read_csv(final_opponent_path)

        insert_team_per_game(regular_df, 0)
        insert_team_per_game(opponent_df, 1)

'''
Calls insert_team_per_poss from 1980 - 2020
'''
def insert_all_team_per_poss():
    regular_path = os.path.join(pathlib.Path().absolute(), "Output", "Team", "Team_Stats", "Team_Averages", "Per_Poss")
    opponent_path = os.path.join(pathlib.Path().absolute(), "Output", "Team", "Team_Stats", "Opponent_Averages", "Opp_Per_Poss")

    # Iterate through the years directory
    for i in range(1980, 2021):
        print(i)
        final_regular_path = os.path.join(regular_path, str(i) + "season_Per_Poss.csv")
        final_opponent_path = os.path.join(opponent_path, str(i) + "season_Per_Poss.csv")
        
        regular_df = pd.read_csv(final_regular_path)
        opponent_df = pd.read_csv(final_opponent_path)

        insert_team_per_poss(regular_df, 0)
        insert_team_per_poss(opponent_df, 1)

'''
Calls insert_team_totals from 1980 - 2020
'''
def insert_all_team_totals():
    regular_path = os.path.join(pathlib.Path().absolute(), "Output", "Team", "Team_Stats", "Team_Averages", "Total")
    opponent_path = os.path.join(pathlib.Path().absolute(), "Output", "Team", "Team_Stats", "Opponent_Averages", "Opp_Total")

    # Iterate through the years directory
    for i in range(1980, 2021):
        print(i)
        final_regular_path = os.path.join(regular_path, str(i) + "season_Total.csv")
        final_opponent_path = os.path.join(opponent_path, str(i) + "season_Total.csv")
        
        regular_df = pd.read_csv(final_regular_path)
        opponent_df = pd.read_csv(final_opponent_path)

        insert_team_totals(regular_df, 0)
        insert_team_totals(opponent_df, 1)

'''
Main function
'''
def main():
    insert_all_season()
    insert_all_team()
    insert_all_players()
    insert_all_standings()
    insert_all_conference_standings()
    insert_all_roster()
    insert_all_team_stats()
    insert_all_team_advanced()
    insert_all_team_misc()
    insert_all_team_per_game()
    insert_all_team_per_poss()
    insert_all_team_totals()
    
if __name__ == "__main__":
    main()