USE BasketballDB;

CREATE TABLE IF NOT EXISTS Season(
    Season_ID INT NOT NULL, 

    PRIMARY KEY (Season_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021)
);

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
);

CREATE TABLE IF NOT EXISTS Player(
    Player_ID   INT NOT NULL,
    Birth_Date  VARCHAR(30) NOT NULL,
    Player_Name VARCHAR(45) NOT NULL,
    PRIMARY KEY(Player_ID),
    CHECK(Player_ID BETWEEN 1 and 3281)
);

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
    FOREIGN KEY (Season_ID, Team_ID) REFERENCES Team(Season_ID, Team_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31)
);

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
    CHECK(Player_ID BETWEEN 1 and 3281)
);

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
);

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
);

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
);

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
);

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
);

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
);

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
    CONSTRAINT Player_Stats_Player_ID_Chk CHECK(Player_ID BETWEEN 1 and 3281)
);

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
    Stat_Form                     BOOLEAN,  

    UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form),
    PRIMARY KEY (Season_ID, Team_ID, Player_ID),
    FOREIGN KEY (Season_ID, Team_ID, Player_ID) REFERENCES Player_Stats(Season_ID, Team_ID, Player_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    CHECK(Player_ID BETWEEN 1 and 3281)
);

CREATE TABLE IF NOT EXISTS Player_Per_Game(
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
    Stat_Form                       BOOLEAN,  

	UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form),
    PRIMARY KEY (Season_ID, Team_ID, Player_ID, Stat_Form),
    FOREIGN KEY (Season_ID, Team_ID, Player_ID) REFERENCES Player_Stats(Season_ID, Team_ID, Player_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    CHECK(Player_ID BETWEEN 1 and 3281)
);

CREATE TABLE IF NOT EXISTS Player_Per_Minute(
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
    Offensive_Rebounds               FLOAT,
    Defensive_Rebounds               FLOAT,
    True_Rebounds                    FLOAT,
    Assists                         FLOAT,
    Steals                          FLOAT,
    Blocks                          FLOAT,
    Turn_Over                       FLOAT,
    Personal_Fouls                   FLOAT,
    Points                          FLOAT,
    Stat_Form                       BOOLEAN,  

	UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form),
    PRIMARY KEY (Season_ID, Team_ID, Player_ID, Stat_Form),
    FOREIGN KEY (Season_ID, Team_ID, Player_ID) REFERENCES Player_Stats(Season_ID, Team_ID, Player_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    CHECK(Player_ID BETWEEN 1 and 3281)
);

CREATE TABLE IF NOT EXISTS Player_Per_Poss(
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
    Offensive_Rebounds               FLOAT,
    Defensive_Rebounds               FLOAT,
    True_Rebounds                    FLOAT,
    Assists                         FLOAT,
    Steals                          FLOAT,
    Blocks                          FLOAT,
    Turn_Over                       FLOAT,
    Personal_Fouls                   FLOAT,
    Points                          FLOAT,
    Offensive_Rating                INT,
    Defensive_Rating                INT,
	Stat_Form                       BOOLEAN,  

	UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form),
    PRIMARY KEY (Season_ID, Team_ID, Player_ID, Stat_Form),
    FOREIGN KEY (Season_ID, Team_ID, Player_ID) REFERENCES Player_Stats(Season_ID, Team_ID, Player_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    CHECK(Player_ID BETWEEN 1 and 3281)
);

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
    Offensive_Rebounds               FLOAT,
    Defensive_Rebounds               FLOAT,
    True_Rebounds                    FLOAT,
    Assists                         FLOAT,
    Steals                          FLOAT,
    Blocks                          FLOAT,
    Turn_Over                       FLOAT,
    Personal_Fouls                   FLOAT,
    Points                          FLOAT,
    Triple_Double                   INT,
    Stat_Form                       BOOLEAN,  

	UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form),
    PRIMARY KEY (Season_ID, Team_ID, Player_ID, Stat_Form),
    FOREIGN KEY (Season_ID, Team_ID, Player_ID) REFERENCES Player_Stats(Season_ID, Team_ID, Player_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    CHECK(Player_ID BETWEEN 1 and 3281)
);

CREATE TABLE IF NOT EXISTS Player_Career_Stats(
	Player_ID           INT NOT NULL,
    Birth_Date  		VARCHAR(30) NOT NULL,
    Player_Name 		VARCHAR(45) NOT NULL,
	
    PRIMARY KEY (Player_ID),
    FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID),
    CONSTRAINT CHECK(Player_ID BETWEEN 1 and 3281)
);

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
    Stat_Form                     BOOLEAN,  --  Regular | Playoffs
	
	UNIQUE(Player_ID, Stat_Form),
	PRIMARY KEY (Player_ID),
	FOREIGN KEY (Player_ID) REFERENCES Player_Career_Stats(Player_ID), 
	CHECK(Player_ID BETWEEN 1 and 3281)
);

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
    Stat_Form                       BOOLEAN,  

	UNIQUE(Player_ID, Stat_Form),
    PRIMARY KEY (Player_ID, Stat_Form),
    FOREIGN KEY (Player_ID) REFERENCES Player_Career_Stats(Player_ID),
    CHECK(Player_ID BETWEEN 1 and 3281)
);

CREATE TABLE IF NOT EXISTS Player_Career_Per_Minute(
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
    Stat_Form                       BOOLEAN,  

	UNIQUE(Player_ID, Stat_Form),
    PRIMARY KEY (Player_ID, Stat_Form),
    FOREIGN KEY (Player_ID) REFERENCES Player_Career_Stats(Player_ID),
    CHECK(Player_ID BETWEEN 1 and 3281) 
);

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
    Stat_Form                       BOOLEAN,  

	UNIQUE(Player_ID, Stat_Form),
    PRIMARY KEY (Player_ID, Stat_Form),
    FOREIGN KEY (Player_ID) REFERENCES Player_Career_Stats(Player_ID),
    CHECK(Player_ID BETWEEN 1 and 3281) 
);

CREATE TABLE IF NOT EXISTS Player_Career_Totals(
	Player_ID                       INT NOT NULL,
    Player_Name                     VARCHAR(45) NOT NULL, 
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
    Offensive_Rebounds               FLOAT,
    Defensive_Rebounds               FLOAT,
    True_Rebounds                    FLOAT,
    Assists                         FLOAT,
    Steals                          FLOAT,
    Blocks                          FLOAT,
    Turn_Over                       FLOAT,
    Personal_Fouls                   FLOAT,
    Points                          FLOAT,
    Triple_Double                   INT,
    Stat_Form                       BOOLEAN,  

	UNIQUE(Player_ID, Stat_Form),
    PRIMARY KEY (Player_ID, Stat_Form),
    FOREIGN KEY (Player_ID) REFERENCES Player_Career_Stats(Player_ID),
    CHECK(Player_ID BETWEEN 1 and 3281)
);