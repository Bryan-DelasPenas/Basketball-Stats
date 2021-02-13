import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_table, check_procedure

'''
Function that creates the Season entity table 
'''
def create_season_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Season'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Season(
            Season_ID INT NOT NULL, 

            PRIMARY KEY (Season_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021)
            )
            """)
            trans.commit()
            conn.close()
            print("Season Table creation was successful")
        except:
            raise Exception("Season Table creation failed")
    else:
        raise Exception("Table does already exists")

'''
Function that creates the Team entity table 
'''
def create_team_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Team'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Team(
            Season_ID INT NOT NULL, 
            Team_ID   INT NOT NULL,
            Team_Name VARCHAR(45) NOT NULL,
            Team_ABV  VARCHAR(3) NOT NULL,
            
            UNIQUE(Season_ID, Team_ID),
            PRIMARY KEY (Season_ID, Team_ID),
            FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31)
            )
            """)
            trans.commit()
            conn.close()
            print("Team Table creation was successful")
        except:
            raise Exception("Team Table creation failed")
    else:
        raise Exception("Team Table does already exists")

'''
Function that creates the Player entity table 
'''
def create_player_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player(
            Player_ID   INT NOT NULL,
            Birth_Date  VARCHAR(30) NOT NULL,
            Player_Name VARCHAR(45) NOT NULL,
            PRIMARY KEY(Player_ID),
            CHECK(Player_ID BETWEEN 1 and 3278)
            )
            """)
            trans.commit()
            conn.close()
            print("Player Table creation was successful")
        except:
            raise Exception("Player Table creation failed")
    else:
        raise Exception("Player Table does already exists")

'''
Function that creates Standings enitiy table
'''
def create_standings_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Standings'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Standings(
            Season_ID INT NOT NULL, 
            Team_ID   INT NOT NULL,
            Team_Name VARCHAR(45) NOT NULL,
            Team_ABV  VARCHAR(3) NOT NULL,
            
            UNIQUE(Season_ID, Team_ID),
            PRIMARY KEY (Season_ID, Team_ID),
            FOREIGN KEY (Season_ID, Team_ID) REFERENCES Team(Season_ID, Team_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31)
            )
            """)
            trans.commit()
            conn.close()
            print("Standings Table creation was successful")
        except:
            raise Exception("Standings Table creation failed")
    else:
        raise Exception("Standings Table does already exists")

'''
Function that creates Conference Standings enitiy table
'''
def create_conference_standings_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Conference_Standings'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Conference_Standings(
            Season_ID 				  INT NOT NULL,
            Team_ID   				  INT NOT NULL, 
            Team_ABV  				  VARCHAR(3) NOT NULL,
            Team_Name 				  VARCHAR(45) NOT NULL,
            Wins  					  INT NOT NULL,
            Loses 					  INT NOT NULL,
            Win_Lose_Percentage 	  FLOAT NOT NULL,
            Games_Behind 			  VARCHAR(4) NOT NULL,    
            Points_Per_Game 		  FLOAT NOT NULL, 
            Opponents_Points_Per_Game FLOAT NOT NULL,
            Simple_Rating_System 	  FLOAT NOT NULL, 
            East_Or_West              BOOLEAN NOT NULL,
            
            UNIQUE(Season_ID, Team_ID),
            PRIMARY KEY (Season_ID, Team_ID),
            FOREIGN KEY (Season_ID, Team_ID) REFERENCES Standings(Season_ID, Team_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31)
            )
            """)
            trans.commit()
            conn.close()
            print("Conference_Standings Table creation was successful")
        except:
            raise Exception("Conference_Standings Table creation failed")
    else:
        raise Exception("Conference_Standings Table does already exists")

'''
Function that creates Roster enitiy table
'''
def create_roster_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Roster'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Roster(
            Season_ID           INT NOT NULL,
            Team_ID             INT NOT NULL,
            Player_ID           INT NOT NULL,
            Team_ABV            VARCHAR(3) NOT NULL,
            Team_Name           VARCHAR(45) NOT NULL,
            Player_Number       VARCHAR(45),
            Player_Name         VARCHAR(45) NOT NULL,
            Player_Postion      VARCHAR(10) NOT NULL,
            Player_Height       VARCHAR(4) NOT NULL,
            Player_Weight       INT NOT NULL, 
            Birth_Date          VARCHAR(30) NOT NULL, 
            Player_Nationality  VARCHAR(2),
            Player_Experience   VARCHAR(2) NOT NULL,
            Player_College_Name VARCHAR(100), 


            UNIQUE(Season_ID, Team_ID, Player_ID),
            PRIMARY KEY (Season_ID, Team_ID, Player_ID),
            FOREIGN KEY (Season_ID, Team_ID) REFERENCES Team(Season_ID, Team_ID),
            FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31),
            CHECK(Player_ID BETWEEN 1 and 3278)
            )
            """)
            trans.commit()
            conn.close()
            print("Roster Table creation was successful")
        except:
            raise Exception("Roster Table creation failed")
    else:
        raise Exception("Roster Table does already exists")

'''
Function that creates Team_Stats enitiy table
'''
def create_team_stats_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Team_Stats'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Team_Stats(
            Season_ID           INT NOT NULL,
            Team_ID             INT NOT NULL,
            Team_ABV            VARCHAR(3) NOT NULL,
            Team_Name           VARCHAR(45) NOT NULL,

            UNIQUE(Season_ID, Team_ID),
            PRIMARY KEY (Season_ID, Team_ID),
            FOREIGN KEY (Season_ID, Team_ID) REFERENCES Team(Season_ID, Team_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31)
            )
            """)
            trans.commit()
            conn.close()
            print("Team_Stats Table creation was successful")
        except:
            raise Exception("Team_Stats Table creation failed")
    else:
        raise Exception("Team_Stats Table does already exists")

'''
Function that creates Team_Advanced enitiy table
'''
def create_team_advanced_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Team_Advanced'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Team_Advanced(
            Season_ID           		  INT NOT NULL,
            Team_ID             		  INT NOT NULL,
            Team_ABV                      VARCHAR(3) NOT NULL,
            Team_Name                     VARCHAR(45) NOT NULL,
            Team_Wins                     INT NOT NULL,
            Team_Loses                    INT NOT NULL,
            Win_Lose_Percentage           FLOAT NOT NULL,
            Team_Finish                   VARCHAR(45),
            Simple_Rating_System          FLOAT NOT NULL,
            Pace                          FLOAT NOT NULL,
            Relative_Pace                 FLOAT NOT NULL,
            Offensive_Rating              FLOAT NOT NULL,
            Relative_Offensive_Rating     FLOAT NOT NULL,
            Defensive_Rating              FLOAT NOT NULL,
            Relative_Defensive_Rating     FLOAT NOT NULL,
            Playoffs_Finish               VARCHAR(45),
            Coaches                       VARCHAR(100),

            UNIQUE(Season_ID, Team_ID),
            PRIMARY KEY (Season_ID, Team_ID),
            FOREIGN KEY (Season_ID, Team_ID) REFERENCES Team_Stats(Season_ID, Team_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31)
            )
            """)
            trans.commit()
            conn.close()
            print("Team_Advanced Table creation was successful")
        except:
            raise Exception("Team_Advanced Table creation failed")
    else:
        raise Exception("Team_Advanced Table does already exists")

'''
Function that create Team_Misc enitiy table
'''
def create_team_misc_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Team_Misc'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Team_Misc(
            Season_ID           		  INT NOT NULL,
            Team_ID             		  INT NOT NULL,
            Team_ABV                      VARCHAR(3) NOT NULL,
            Team_Name                     VARCHAR(45) NOT NULL,
            Team_Average_Age              FLOAT NOT NULL,
            Team_Wins                     INT NOT NULL,
            Team_Loses                    INT NOT NULL,
            Pythagorean_Wins              INT NOT NULL,
            Pythagorean_Loses             INT NOT NULL,
            Margin_Of_Victory             FLOAT NOT NULL,
            Strength_Of_Schedule          FLOAT NOT NULL,
            Simple_Rating_System          FLOAT NOT NULL,
            Offensive_Rating              FLOAT NOT NULL,
            Defensive_Rating              FLOAT NOT NULL,
            Net_Rating                    FLOAT NOT NULL,
            Pace                          FLOAT NOT NULL,
            Free_Throw_Attempt_Rate       FLOAT NOT NULL,
            Three_Point_Attempt_Rate      FLOAT NOT NULL, 
            True_Shooting_Percentage      FLOAT NOT NULL,
            Offensive_Rebound_Percentage  FLOAT NOT NULL,
            Defensive_Rebound_Percentage  FLOAT NOT NULL,
            Arena                         VARCHAR(45) NOT NULL,
            Attend                        INT,
            Attend_Per_Game               INT, 

            UNIQUE(Season_ID, Team_ID),
            PRIMARY KEY (Season_ID, Team_ID),
            FOREIGN KEY (Season_ID, Team_ID) REFERENCES Team_Stats(Season_ID, Team_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31)
            )
            """)
            trans.commit()
            conn.close()
            print("Team_Misc Table creation was successful")
        except:
            raise Exception("Team_Misc Table creation failed")
    else:
        raise Exception("Team_Misc Table does already exists")

'''
Function that create Team_Per_Game enitiy table
'''
def create_team_per_game_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Team_Per_Game'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Team_Per_Game(
            Season_ID           		    INT NOT NULL,
            Team_ID             		    INT NOT NULL,
            Team_ABV                        VARCHAR(3) NOT NULL,
            Team_Name                       VARCHAR(45) NOT NULL,
            Games_Played       	            INT NOT NULL, 
            Minutes_Played                  INT NOT NULL,
            Field_Goals_Made                FLOAT,
            Field_Goals_Attempted           FLOAT,
            Field_Goals_Percentage          FLOAT,
            Three_Points_Made               FLOAT,
            Three_Points_Attempted          FLOAT,
            Three_Points_Percentage         FLOAT,
            Two_Points_Made                 FLOAT, 
            Two_Points_Attempted            FLOAT,
            Two_Points_Percentage           FLOAT,
            Free_Throws_Made                FLOAT,
            Free_Throws_Attempted           FLOAT,
            Free_Throws_Percentage          FLOAT,
            Offensive_Rebound               FLOAT,
            Defensive_Rebound               FLOAT,
            True_Rebound                    FLOAT,
            Assists                         FLOAT,
            Steals                          FLOAT,
            Blocks                          FLOAT,
            Turn_Over                       FLOAT,
            Personal_Foul                   FLOAT,
            Points                          FLOAT,
            Opponent                        BOOLEAN NOT NULL,
        
            UNIQUE(Season_ID, Team_ID, Opponent),
            PRIMARY KEY (Season_ID, Team_ID, Opponent),
            FOREIGN KEY (Season_ID, Team_ID) REFERENCES Team_Stats(Season_ID, Team_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31)
            )
            """)
            trans.commit()
            conn.close()
            print("Team_Per_Game creation was successful")
        except:
            raise Exception("Team_Per_Game Table creation failed")
    else:
        raise Exception("Team_Per_Game Table does already exists")

'''
Function that create Team_Per_Poss enitiy table
'''
def create_team_per_poss_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Team_Per_Poss'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Team_Per_Poss(
            Season_ID           		    INT NOT NULL,
            Team_ID             		    INT NOT NULL,
            Team_ABV                        VARCHAR(3) NOT NULL,
            Team_Name                       VARCHAR(45) NOT NULL,
            Games_Played       	            INT NOT NULL, 
            Minutes_Played                  INT NOT NULL,
            Field_Goals_Made                FLOAT,
            Field_Goals_Attempted           FLOAT,
            Field_Goals_Percentage          FLOAT,
            Three_Points_Made               FLOAT,
            Three_Points_Attempted          FLOAT,
            Three_Points_Percentage         FLOAT,
            Two_Points_Made                 FLOAT, 
            Two_Points_Attempted            FLOAT,
            Two_Points_Percentage           FLOAT,
            Free_Throws_Made                FLOAT,
            Free_Throws_Attempted           FLOAT,
            Free_Throws_Percentage          FLOAT,
            Offensive_Rebound               FLOAT,
            Defensive_Rebound               FLOAT,
            True_Rebound                    FLOAT,
            Assists                         FLOAT,
            Steals                          FLOAT,
            Blocks                          FLOAT,
            Turn_Over                       FLOAT,
            Personal_Foul                   FLOAT,
            Points                          FLOAT,
            Opponent                        BOOLEAN NOT NULL,

            UNIQUE(Season_ID, Team_ID, Opponent),
            PRIMARY KEY (Season_ID, Team_ID, Opponent),
            FOREIGN KEY (Season_ID, Team_ID) REFERENCES Team_Stats(Season_ID, Team_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31)
            )
            """)
            trans.commit()
            conn.close()
            print("Team_Per_Poss creation was successful")
        except:
            raise Exception("Team_Per_Poss Table creation failed")
    else:
        raise Exception("Team_Per_Poss Table does already exists")

'''
Function that create Team_Totals enitiy table
'''
def create_team_totals_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Team_Totals'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Team_Totals(
            Season_ID           		    INT NOT NULL,
            Team_ID             		    INT NOT NULL,
            Team_ABV                        VARCHAR(3) NOT NULL,
            Team_Name                       VARCHAR(45) NOT NULL,
            Games_Played       	            INT NOT NULL, 
            Minutes_Played                  INT NOT NULL,
            Field_Goals_Made                FLOAT,
            Field_Goals_Attempted           FLOAT,
            Field_Goals_Percentage          FLOAT,
            Three_Points_Made               FLOAT,
            Three_Points_Attempted          FLOAT,
            Three_Points_Percentage         FLOAT,
            Two_Points_Made                 FLOAT, 
            Two_Points_Attempted            FLOAT,
            Two_Points_Percentage           FLOAT,
            Free_Throws_Made                FLOAT,
            Free_Throws_Attempted           FLOAT,
            Free_Throws_Percentage          FLOAT,
            Offensive_Rebound               FLOAT,
            Defensive_Rebound               FLOAT,
            True_Rebound                    FLOAT,
            Assists                         FLOAT,
            Steals                          FLOAT,
            Blocks                          FLOAT,
            Turn_Over                       FLOAT,
            Personal_Foul                   FLOAT,
            Points                          FLOAT,
            Opponent                        BOOLEAN NOT NULL,

            UNIQUE(Season_ID, Team_ID, Opponent),
            PRIMARY KEY (Season_ID, Team_ID, Opponent),
            FOREIGN KEY (Season_ID, Team_ID) REFERENCES Team_Stats(Season_ID, Team_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31)
            )
            """)
            trans.commit()
            conn.close()
            print("Team_Totals creation was successful")
        except:
            raise Exception("Team_Totals Table creation failed")
    else:
        raise Exception("Team_Totals Table does already exists")

'''
Function that creates Player_Stats enitiy table
'''
def create_player_stats_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player_Stats'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player_Stats(
            Season_ID           INT NOT NULL,
            Team_ID             INT NOT NULL,
            Player_ID           INT NOT NULL,
            Team_ABV            VARCHAR(3) NOT NULL,
            Team_Name           VARCHAR(45) NOT NULL,
            Birth_Date  		VARCHAR(30) NOT NULL,
            Player_Name 		VARCHAR(45) NOT NULL,
            
            CONSTRAINT Player_Stats_UNIQUE_Chk UNIQUE(Season_ID, Team_ID, Player_ID),
            PRIMARY KEY (Season_ID, Team_ID, Player_ID),
            FOREIGN KEY (Season_ID, Team_ID) REFERENCES Team(Season_ID, Team_ID),
            FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID),
            CONSTRAINT Player_Stats_Season_ID_Chk CHECK (Season_ID BETWEEN 1980 AND 2021),
            CONSTRAINT Player_Stats_Team_ID_Chk CHECK(Team_ID BETWEEN 1 and 31),
            CONSTRAINT Player_Stats_Player_ID_Chk CHECK(Player_ID BETWEEN 1 and 3278)
            )
            """)
            trans.commit()
            conn.close()
            print("Player_Stats creation was successful")
        except:
            raise Exception("Player_Stats Table creation failed")
    else:
        raise Exception("Player_Stats Table does already exists")

'''
Function that creates Player_Advanced enitiy table
'''
def create_player_advanced_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player_Advanced'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player_Advanced(
            Season_ID                     INT NOT NULL,
            Team_ID                       INT NOT NULL,
            Player_ID                     INT NOT NULL,
            Team_ABV                      VARCHAR(3) NOT NULL,
            Team_Name                     VARCHAR(45) NOT NULL,
            Player_Name                   VARCHAR(45) NOT NULL,
            Birth_Date                    VARCHAR(45) NOT NULL,
            Player_Age                    VARCHAR(45) NOT NULL, 
            League                        VARCHAR(3),
            Player_Postion                VARCHAR(20),
            Games_Played       	          INT, 
            Minutes_Played                INT,
            Per_Minute_Production         FLOAT,
            True_Shooting_Percent         FLOAT, 
            Three_Points_Attempted        FLOAT,
            Free_Throws_Per_Field_Goals   FLOAT,
            Offensive_Rebound_Percentage  FLOAT,
            Defensive_Rebound_Percentage  FLOAT,
            True_Rebound_Percentage       FLOAT, 
            Assit_Percentage              FLOAT,
            Steal_Percentage              FLOAT,
            Block_Percentage              FLOAT,
            Turn_Over_Percentage          FLOAT,
            Usage_Percentage              FLOAT,
            Offensive_Win_Shares          FLOAT, 
            Defensive_Win_Shares          FLOAT, 
            Win_Shares                    FLOAT,
            Win_Shares_Fourty_Eight       FLOAT,
            Offensive_Box_Score           FLOAT,
            Defensive_Box_Score           FLOAT,
            Box_Plus_Minus                FLOAT,
            Value_Over_Replacement        FLOAT,
            Stat_Form                     BOOLEAN NOT NULL,  -- Career | Regular | Playoffs

            UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form),
            PRIMARY KEY (Season_ID, Team_ID, Player_ID),
            FOREIGN KEY (Season_ID, Team_ID, Player_ID) REFERENCES Player_Stats(Season_ID, Team_ID, Player_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31),
            CHECK(Player_ID BETWEEN 1 and 3278)
            )
            """)
            trans.commit()
            conn.close()
            print("Player_Advanced creation was successful")
        except:
            raise Exception("Player_Advanced Table creation failed")
    else:
        raise Exception("Player_Advanced Table does already exists")

'''
Function that creates Player_Per_Game enitiy table
'''
def create_player_per_game_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player_Per_Game'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player_Per_Game(
            Season_ID                       INT NOT NULL,
            Team_ID                         INT NOT NULL,
            Player_ID                       INT NOT NULL,
            Team_ABV                        VARCHAR(3) NOT NULL,
            Team_Name                       VARCHAR(45) NOT NULL,
            Player_Name                     VARCHAR(45) NOT NULL, -- Need to Rerun Web Scrapers
            Birth_Date                      VARCHAR(45) NOT NULL,
            Player_Age                      INT NOT NULL,
            League                          VARCHAR(3),
            Player_Postion                  VARCHAR(10),
            Games_Played       	            INT NOT NULL, 
            Games_Started                   INT,
            Minutes_Played                  INT NOT NULL,
            Field_Goals_Made                FLOAT,
            Field_Goals_Attempted           FLOAT,
            Field_Goals_Percentage          FLOAT,
            Three_Points_Made               FLOAT,
            Three_Points_Attempted          FLOAT,
            Three_Points_Percentage         FLOAT,
            Two_Points_Made                 FLOAT, 
            Two_Points_Attempted            FLOAT,
            Two_Points_Percentage           FLOAT,
            Effective_Field_Goal_Percentage FLOAT,
            Free_Throws_Made                FLOAT,
            Free_Throws_Attempted           FLOAT,
            Free_Throws_Percentage          FLOAT,
            Offensive_Rebounds              FLOAT,
            Defensive_Rebounds              FLOAT,
            True_Rebounds                   FLOAT,
            Assists                         FLOAT,
            Steals                          FLOAT,
            Blocks                          FLOAT,
            Turn_Over                       FLOAT,
            Personal_Fouls                  FLOAT,
            Points                          FLOAT,
            Stat_Form                       VARCHAR(45) NOT NULL,  -- Career | Regular | Playoffs

            UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form),
            PRIMARY KEY (Season_ID, Team_ID, Player_ID),
            FOREIGN KEY (Season_ID, Team_ID, Player_ID) REFERENCES Player_Stats(Season_ID, Team_ID, Player_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31),
            CHECK(Player_ID BETWEEN 1 and 3278)
            )
            """)
            trans.commit()
            conn.close()
            print("Player_Per_Game creation was successful")
        except:
            raise Exception("Player_Per_Game Table creation failed")
    else:
        raise Exception("Player_Per_Game Table does already exists")

'''
Function that create Player_Per_Minute enitiy table
'''
def create_player_per_minute_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player_Per_Minute'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player_Per_Minute(
            Season_ID                       INT NOT NULL,
            Team_ID                         INT NOT NULL,
            Player_ID                       INT NOT NULL,
            Team_ABV                        VARCHAR(3) NOT NULL,
            Team_Name                       VARCHAR(45) NOT NULL,
            Player_Name                     VARCHAR(45) NOT NULL, -- Need to Rerun Web Scrapers
            Birth_Date                      VARCHAR(45) NOT NULL,
            Player_Age                      INT NOT NULL,
            League                          VARCHAR(3),
            Player_Postion                  VARCHAR(10),
            Games_Played       	            INT NOT NULL, 
            Games_Started                   INT,
            Minutes_Played                  INT NOT NULL,
            Field_Goals_Made                FLOAT,
            Field_Goals_Attempted           FLOAT,
            Field_Goals_Percentage          FLOAT,
            Three_Points_Made               FLOAT,
            Three_Points_Attempted          FLOAT,
            Three_Points_Percentage         FLOAT,
            Two_Points_Made                 FLOAT, 
            Two_Points_Attempted            FLOAT,
            Two_Points_Percentage           FLOAT,
            Free_Throws_Made                FLOAT,
            Free_Throws_Attempted           FLOAT,
            Free_Throws_Percentage          FLOAT,
            Offensive_Rebounds              FLOAT,
            Defensive_Rebounds              FLOAT,
            True_Rebounds                   FLOAT,
            Assists                         FLOAT,
            Steals                          FLOAT,
            Blocks                          FLOAT,
            Turn_Over                       FLOAT,
            Personal_Fouls                  FLOAT,
            Points                          FLOAT,
            Stat_Form                       VARCHAR(45) NOT NULL,  -- Career | Regular | Playoffs

            UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form),
            PRIMARY KEY (Season_ID, Team_ID, Player_ID),
            FOREIGN KEY (Season_ID, Team_ID, Player_ID) REFERENCES Player_Stats(Season_ID, Team_ID, Player_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31),
            CHECK(Player_ID BETWEEN 1 and 3278)
            )
            """)
            trans.commit()
            conn.close()
            print("Player_Per_Minute creation was successful")
        except:
            raise Exception("Player_Per_Minute Table creation failed")
    else:
        raise Exception("Player_Per_Minute Table does already exists")

'''
Function that creates Player_Per_Poss enitiy table
'''
def create_player_per_poss_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player_Per_Poss'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player_Per_Poss(
            Season_ID                       INT NOT NULL,
            Team_ID                         INT NOT NULL,
            Player_ID                       INT NOT NULL,
            Team_ABV                        VARCHAR(3) NOT NULL,
            Team_Name                       VARCHAR(45) NOT NULL,
            Player_Name                     VARCHAR(45) NOT NULL, -- Need to Rerun Web Scrapers
            Birth_Date                      VARCHAR(45) NOT NULL,
            Player_Age                      INT NOT NULL,
            League                          VARCHAR(3),
            Player_Postion                  VARCHAR(10),
            Games_Played       	            INT NOT NULL, 
            Games_Started                   INT,
            Minutes_Played                  INT NOT NULL,
            Field_Goals_Made                FLOAT,
            Field_Goals_Attempted           FLOAT,
            Field_Goals_Percentage          FLOAT,
            Three_Points_Made               FLOAT,
            Three_Points_Attempted          FLOAT,
            Three_Points_Percentage         FLOAT,
            Two_Points_Made                 FLOAT, 
            Two_Points_Attempted            FLOAT,
            Two_Points_Percentage           FLOAT,
            Free_Throws_Made                FLOAT,
            Free_Throws_Attempted           FLOAT,
            Free_Throws_Percentage          FLOAT,
            Offensive_Rebounds              FLOAT,
            Defensive_Rebounds              FLOAT,
            True_Rebounds                   FLOAT,
            Assists                         FLOAT,
            Steals                          FLOAT,
            Blocks                          FLOAT,
            Turn_Over                       FLOAT,
            Personal_Fouls                  FLOAT,
            Points                          FLOAT,
            Offensive_Rating                INT,
            Defensive_Rating                INT,
            Stat_Form                       VARCHAR(45) NOT NULL,  -- Career | Regular | Playoffs

            UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form),
            PRIMARY KEY (Season_ID, Team_ID, Player_ID),
            FOREIGN KEY (Season_ID, Team_ID, Player_ID) REFERENCES Player_Stats(Season_ID, Team_ID, Player_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31),
            CHECK(Player_ID BETWEEN 1 and 3278)
            )
            """)
            trans.commit()
            conn.close()
            print("Player_Per_Poss creation was successful")
        except:
            raise Exception("Player_Per_Poss Table creation failed")
    else:
        raise Exception("Player_Per_Poss Table does already exists")

'''
Function that creates Player_Totals enitiy table
'''
def create_player_totals_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player_Totals'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player_Totals(
            Season_ID                       INT NOT NULL,
            Team_ID                         INT NOT NULL,
            Player_ID                       INT NOT NULL,
            Team_ABV                        VARCHAR(3) NOT NULL,
            Team_Name                       VARCHAR(45) NOT NULL,
            Player_Name                     VARCHAR(45) NOT NULL, 
            Birth_Date                      VARCHAR(45) NOT NULL,
            Player_Age                      INT NOT NULL,
            League                          VARCHAR(3),
            Player_Postion                  VARCHAR(10),
            Games_Played       	            INT, 
            Games_Started                   INT,
            Minutes_Played                  INT,
            Field_Goals_Made                FLOAT,
            Field_Goals_Attempted           FLOAT,
            Field_Goals_Percentage          FLOAT,
            Three_Points_Made               FLOAT,
            Three_Points_Attempted          FLOAT,
            Three_Points_Percentage         FLOAT,
            Two_Points_Made                 FLOAT, 
            Two_Points_Attempted            FLOAT,
            Two_Points_Percentage           FLOAT,
            Effective_Field_Goal_Percentage FLOAT,
            Free_Throws_Made                FLOAT,
            Free_Throws_Attempted           FLOAT,
            Free_Throws_Percentage          FLOAT,
            Offensive_Rebounds              FLOAT,
            Defensive_Rebounds              FLOAT,
            True_Rebounds                   FLOAT,
            Assists                         FLOAT,
            Steals                          FLOAT,
            Blocks                          FLOAT,
            Turn_Over                       FLOAT,
            Personal_Fouls                  FLOAT,
            Points                          FLOAT,
            Triple_Double                   INT,
            Stat_Form                       VARCHAR(45) NOT NULL, 

            UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form),
            PRIMARY KEY (Season_ID, Team_ID, Player_ID),
            FOREIGN KEY (Season_ID, Team_ID, Player_ID) REFERENCES Player_Stats(Season_ID, Team_ID, Player_ID),
            CHECK(Season_ID BETWEEN 1980 AND 2021),
            CHECK(Team_ID BETWEEN 1 and 31),
            CHECK(Player_ID BETWEEN 1 and 3278)
            )
            """)
            trans.commit()
            conn.close()
            print("Player_Totals creation was successful")
        except:
            raise Exception("Player_Totals Table creation failed")
    else:
        raise Exception("Player_Totals Table does already exists")

'''
Function that creates Player_Career_Stats enitiy table
'''
def create_player_career_stats_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player_Career_Stats'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player_Career_Stats(
            Player_ID           INT NOT NULL,
            Birth_Date  		VARCHAR(30) NOT NULL,
            Player_Name 		VARCHAR(45) NOT NULL,
            
            PRIMARY KEY (Player_ID),
            FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID),
            CONSTRAINT CHECK(Player_ID BETWEEN 1 and 3278)
            )
            """)
            trans.commit()
            conn.close()
            print("Player_Career_Stats creation was successful")
        except:
            raise Exception("Player_Career_Stats Table creation failed")
    else:
        raise Exception("Player_Career_Stats Table does already exists")

'''
Function that creates Player_Career_Advanced enitiy table
'''
def create_player_career_advanced_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player_Career_Advanced'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player_Career_Advanced(
            Player_ID                     INT NOT NULL,
            Player_Name                   VARCHAR(45) NOT NULL,
            Birth_Date                    VARCHAR(45) NOT NULL,
            Games_Played       	          INT, 
            Minutes_Played                INT,
            Per_Minute_Production         FLOAT,
            True_Shooting_Percent         FLOAT, 
            Three_Points_Attempted        FLOAT,
            Free_Throws_Per_Field_Goals   FLOAT,
            Offensive_Rebound_Percentage  FLOAT,
            Defensive_Rebound_Percentage  FLOAT,
            True_Rebound_Percentage       FLOAT, 
            Assit_Percentage              FLOAT,
            Steal_Percentage              FLOAT,
            Block_Percentage              FLOAT,
            Turn_Over_Percentage          FLOAT,
            Usage_Percentage              FLOAT,
            Offensive_Win_Shares          FLOAT, 
            Defensive_Win_Shares          FLOAT, 
            Win_Shares                    FLOAT,
            Win_Shares_Fourty_Eight       FLOAT,
            Offensive_Box_Score           FLOAT,
            Defensive_Box_Score           FLOAT,
            Box_Plus_Minus                FLOAT,
            Value_Over_Replacement        FLOAT,
            Stat_Form                     BOOLEAN NOT NULL,  --  Regular | Playoffs
            
            UNIQUE(Player_ID, Stat_Form),
            PRIMARY KEY (Player_ID),
            FOREIGN KEY (Player_ID) REFERENCES Player_Career_Stats(Player_ID), 
            CHECK(Player_ID BETWEEN 1 and 3278)
            )
            """)
            trans.commit()
            conn.close()
            print("Player_Career_Advanced creation was successful")
        except:
            raise Exception("Player_Career_Advanced Table creation failed")
    else:
        raise Exception("Player_Career_Advanced Table does already exists")

'''
Function that creates Player_Career_Per_Game enitiy table
'''
def create_player_career_per_game_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player_Career_Per_Game'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player_Career_Per_Game(
            Player_ID                       INT NOT NULL,
            Player_Name                     VARCHAR(45) NOT NULL,
            Birth_Date                      VARCHAR(45) NOT NULL,
            Games_Played       	            INT NOT NULL, 
            Games_Started                   INT,
            Minutes_Played                  INT NOT NULL,
            Field_Goals_Made                FLOAT,
            Field_Goals_Attempted           FLOAT,
            Field_Goals_Percentage          FLOAT,
            Three_Points_Made               FLOAT,
            Three_Points_Attempted          FLOAT,
            Three_Points_Percentage         FLOAT,
            Two_Points_Made                 FLOAT, 
            Two_Points_Attempted            FLOAT,
            Two_Points_Percentage           FLOAT,
            Effective_Field_Goal_Percentage FLOAT,
            Free_Throws_Made                FLOAT,
            Free_Throws_Attempted           FLOAT,
            Free_Throws_Percentage          FLOAT,
            Offensive_Rebounds              FLOAT,
            Defensive_Rebounds              FLOAT,
            True_Rebounds                   FLOAT,
            Assists                         FLOAT,
            Steals                          FLOAT,
            Blocks                          FLOAT,
            Turn_Over                       FLOAT,
            Personal_Fouls                  FLOAT,
            Points                          FLOAT,
            Stat_Form                       VARCHAR(45) NOT NULL,  

            UNIQUE(Player_ID, Stat_Form),
            PRIMARY KEY (Player_ID),
            FOREIGN KEY (Player_ID) REFERENCES Player_Career_Stats(Player_ID),
            CHECK(Player_ID BETWEEN 1 and 3278)
            )
            """)
            trans.commit()
            conn.close()
            print("Player_Career_Per_Game creation was successful")
        except:
            raise Exception("Player_Career_Per_Game Table creation failed")
    else:
        raise Exception("Player_Career_Per_Game Table does already exists")

'''
Function that creates Player_Career_Per_Minute enitiy table
'''
def create_player_career_per_minute_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player_Career_Per_Minute'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player_Career_Per_Minute(
            Player_ID                       INT NOT NULL,
            Player_Name                     VARCHAR(45) NOT NULL, -- Need to Rerun Web Scrapers
            Birth_Date                      VARCHAR(45) NOT NULL,
            Games_Played       	            INT NOT NULL, 
            Games_Started                   INT,
            Minutes_Played                  INT NOT NULL,
            Field_Goals_Made                FLOAT,
            Field_Goals_Attempted           FLOAT,
            Field_Goals_Percentage          FLOAT,
            Three_Points_Made               FLOAT,
            Three_Points_Attempted          FLOAT,
            Three_Points_Percentage         FLOAT,
            Two_Points_Made                 FLOAT, 
            Two_Points_Attempted            FLOAT,
            Two_Points_Percentage           FLOAT,
            Free_Throws_Made                FLOAT,
            Free_Throws_Attempted           FLOAT,
            Free_Throws_Percentage          FLOAT,
            Offensive_Rebounds              FLOAT,
            Defensive_Rebounds              FLOAT,
            True_Rebounds                   FLOAT,
            Assists                         FLOAT,
            Steals                          FLOAT,
            Blocks                          FLOAT,
            Turn_Over                       FLOAT,
            Personal_Fouls                  FLOAT,
            Points                          FLOAT,
            Stat_Form                       VARCHAR(45) NOT NULL,  -- Career | Regular | Playoffs

            UNIQUE(Player_ID, Stat_Form),
            PRIMARY KEY (Player_ID),
            FOREIGN KEY (Player_ID) REFERENCES Player_Career_Stats(Player_ID),
            CHECK(Player_ID BETWEEN 1 and 3278) 
            )
            """)
            trans.commit()
            conn.close()
            print("Player_Career_Per_Minute creation was successful")
        except:
            raise Exception("Player_Career_Per_Minute Table creation failed")
    else:
        raise Exception("Player_Career_Per_Minute Table does already exists")

'''
Function that creates Player_Career_Per_Poss enitiy table
'''
def create_player_career_per_poss_table():
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player_Career_Per_Poss'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player_Career_Per_Poss(
            Player_ID                       INT NOT NULL,
            Player_Name                     VARCHAR(45) NOT NULL, 
            Birth_Date                      VARCHAR(45) NOT NULL,
            Games_Played       	            INT NOT NULL, 
            Games_Started                   INT,
            Minutes_Played                  INT NOT NULL,
            Field_Goals_Made                FLOAT,
            Field_Goals_Attempted           FLOAT,
            Field_Goals_Percentage          FLOAT,
            Three_Points_Made               FLOAT,
            Three_Points_Attempted          FLOAT,
            Three_Points_Percentage         FLOAT,
            Two_Points_Made                 FLOAT, 
            Two_Points_Attempted            FLOAT,
            Two_Points_Percentage           FLOAT,
            Free_Throws_Made                FLOAT,
            Free_Throws_Attempted           FLOAT,
            Free_Throws_Percentage          FLOAT,
            Offensive_Rebounds              FLOAT,
            Defensive_Rebounds              FLOAT,
            True_Rebounds                   FLOAT,
            Assists                         FLOAT,
            Steals                          FLOAT,
            Blocks                          FLOAT,
            Turn_Over                       FLOAT,
            Personal_Fouls                  FLOAT,
            Points                          FLOAT,
            Offensive_Rating                INT,
            Defensive_Rating                INT,
            Stat_Form                       VARCHAR(45) NOT NULL,  
            
            UNIQUE(Player_ID, Stat_Form),
            PRIMARY KEY (Player_ID),
            FOREIGN KEY (Player_ID) REFERENCES Player_Career_Stats(Player_ID),
            CHECK(Player_ID BETWEEN 1 and 3278) 
            )
            """)
            trans.commit()
            conn.close()
            print("Player_Career_Per_Poss creation was successful")
        except:
            raise Exception("Player_Career_Per_Poss Table creation failed")
    else:
        raise Exception("Player_Career_Per_Poss Table does already exists")

'''
Function that creates Player_Career_Totals
'''
def create_player_career_totals_table():
     # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists, if not create table
    if not check_table('Player_Career_Totals'):
        # Test to see if the insertion works
        try: 
            # Create a parameterized querry for insertion
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Player_Career_Totals(
            Player_ID                       INT NOT NULL,
            Player_Name                     VARCHAR(45) NOT NULL, -- Need to Rerun Web Scrapers
            Birth_Date                      VARCHAR(45) NOT NULL,
            Games_Played       	            INT, 
            Games_Started                   INT,
            Minutes_Played                  INT,
            Field_Goals_Made                FLOAT,
            Field_Goals_Attempted           FLOAT,
            Field_Goals_Percentage          FLOAT,
            Three_Points_Made               FLOAT,
            Three_Points_Attempted          FLOAT,
            Three_Points_Percentage         FLOAT,
            Two_Points_Made                 FLOAT, 
            Two_Points_Attempted            FLOAT,
            Two_Points_Percentage           FLOAT,
            Effective_Field_Goal_Percentage FLOAT,
            Free_Throws_Made                FLOAT,
            Free_Throws_Attempted           FLOAT,
            Free_Throws_Percentage          FLOAT,
            Offensive_Rebounds              FLOAT,
            Defensive_Rebounds              FLOAT,
            True_Rebounds                   FLOAT,
            Assists                         FLOAT,
            Steals                          FLOAT,
            Blocks                          FLOAT,
            Turn_Over                       FLOAT,
            Personal_Fouls                  FLOAT,
            Points                          FLOAT,
            Triple_Double                   INT,
            Stat_Form                       VARCHAR(45) NOT NULL, 

            UNIQUE(Player_ID, Stat_Form),
            PRIMARY KEY (Player_ID),
            FOREIGN KEY (Player_ID) REFERENCES Player_Career_Stats(Player_ID),
            CHECK(Player_ID BETWEEN 1 and 3278)
            )
            """)
            trans.commit()
            conn.close()
            print("Player_Career_Totals creation was successful")
        except:
            raise Exception("Player_Career_Totals Table creation failed")
    else:
        raise Exception("Player_Career_Totals Table does already exists")

'''
Function that calls all create tables 
'''
def create_all():
    create_season_table()
    create_team_table()
    create_player_table()
    
    # Standings
    create_standings_table()
    create_conference_standings_table()
    
    # Roster
    create_roster_table()
    
    # Team Stats
    create_team_stats_table()
    create_team_advanced_table()
    create_team_misc_table()
    create_team_per_game_table()
    create_team_per_poss_table()
    create_team_totals_table()

    # Player Stats
    create_player_stats_table()
    create_player_advanced_table()
    create_player_per_game_table()
    create_player_per_minute_table()
    create_player_per_poss_table()
    create_player_totals_table()

    # Player Career Stats
    create_player_career_stats_table()
    create_player_career_advanced_table()
    create_player_career_per_game_table()
    create_player_career_per_minute_table()
    create_player_career_per_poss_table()
    create_player_career_totals_table()

'''
Main Function
'''
def main():
    create_all()


if __name__ == "__main__":
    main()