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
Function that inserts Season entities into database
'''
def insert_season(season_id):
    
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()
  
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

'''
Function that inserts Teans entities into database
'''
def insert_team(df):
    # Rename the dataframe 
    df = df.rename(columns={"Season" : "Season_ID",  "Team ID" : "Team_ID" , "Team" : "Team_Name", "Team ABV" : "Team_ABV"})
    
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()

    # Test to see if the insertion works 
    try:
        df.to_sql('team', con = engine, if_exists='append', index = False)
        trans.commit()
        print("Insertion into Team was successful")
    
    except:
        raise Exception("Insertion into Team failed")
    

def insert_player(df):    
    # Connect to sql database 
    engine = create_connection()

    # Test the connection of the database
    conn = test_connection(engine)
    
    trans = conn.begin()
    
    # Test to see if the insertion works 
    try:
        df.to_sql('player', con = engine, if_exists='append', index = False)
        trans.commit()
        print("Insertion into Team was successful")
    
    except:
        raise Exception("Insertion into Team failed")

def insert_standings():
    return None

def insert_standard_standings():
    return None

def insert_conference_standings():
    return None

def insert_expanded_standings():
    return None

def insert_team_vs_team():
    return None

def insert_roster():
    return None

def insert_team_stats():
    return None

def insert_team_advanced():
    return None

def insert_team_misc():
    return None

def insert_team_per_game():
    return None

def insert_team_per_poss():
    return None

def insert_team_totals():
    return None

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
Main function
'''
def main():
    insert_all_season()
    insert_all_team()
    insert_all_players()

if __name__ == "__main__":
    main()