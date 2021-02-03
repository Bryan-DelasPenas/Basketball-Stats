USE BasketballDB;

CREATE TABLE IF NOT EXISTS Season(
    Season_ID INT NOT NULL UNIQUE, 

    PRIMARY KEY (Season_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021)
);

CREATE TABLE IF NOT EXISTS Team(
    Season_ID INT NOT NULL, 
    Team_ID   INT NOT NULL UNIQUE,
    Team_Name VARCHAR(45) NOT NULL,
    Team_ABV  VARCHAR(3) NOT NULL,

    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),

    UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS Player(
    Player_ID   INT NOT NULL,
    Birth_Date  VARCHAR(30) NOT NULL,
    Player_Name VARCHAR(45) NOT NULL,
    PRIMARY KEY(Player_ID),
    CHECK(Player_ID BETWEEN 1 and 3278)
);

CREATE TABLE IF NOT EXISTS Standings(
    Season_ID INT NOT NULL,
    Team_ID   INT NOT NULL,
    Team_Name VARCHAR(45) NOT NULL,
    Team_ABV  VARCHAR(3) NOT NULL,

    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),

    UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS Standard_Standings(
    Season_ID INT NOT NULL, 
    Team_ID   INT NOT NULL,
    Team_Name VARCHAR(45) NOT NULL UNIQUE,
    Team_ABV  VARCHAR(3) NOT NULL UNIQUE,

    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Standings(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Standings(Team_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),

    UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS Conference_Standings(
    Season_ID 				  INT NOT NULL,
    Team_ID   				  INT NOT NULL, 
    Team_ABV  				  VARCHAR(3) NOT NULL,
    Team_Name 				  VARCHAR(45) NOT NULL,
    Wins  					  INT NOT NULL,
    Loses 					  INT NOT NULL,
    Win_Lose_Percentage 	  FLOAT NOT NULL,
    Games_Behind 			  VARCHAR(2) NOT NULL,    
    Points_Per_Game 		  FLOAT NOT NULL, 
    Opponents_Points_Per_Game FLOAT NOT NULL,
    Simple_Rating_System 	  FLOAT NOT NULL, 
    East_Or_West              BOOLEAN NOT NULL,

    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Standard_Standings(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Standard_Standings(Team_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),

    UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS Expanded_Standings(
    Season_ID 					INT NOT NULL,
    Team_ID 					INT NOT NULL,
    Team_ABV 					VARCHAR(3) NOT NULL,
    Team_Name 					VARCHAR(45) NOT NULL,
    Overall 					VARCHAR(45) NOT NULL,
    Home_Record 				VARCHAR(45) NOT NULL,
    Road_Record 				VARCHAR(45) NOT NULL,
    Eastern_Conference_Record 	VARCHAR(5),
    Western_Conference_Record 	VARCHAR(5),
    Atlantic_Division_Record 	VARCHAR(5), 
    Central_Division_Record 	VARCHAR(5), 
    Midwestern_Divsion_Record 	VARCHAR(5),
    Pacific_Divsion_Record 		VARCHAR(5),
    Southeastern_Divsion_Record VARCHAR(5),
    Southwestern_Divsion_Record VARCHAR(5),
    Northwestern_Divsion_Record VARCHAR(5),
    Pre_Allstar_Record 			VARCHAR(5),
    Post_Allstar_Record 		VARCHAR(5),
    Three_Point_Margin 			VARCHAR(5),
    Ten_Point_Margin 			VARCHAR(5),
    Oct_Record 					VARCHAR(5),
    Nov_Record 					VARCHAR(5),
    Dec_Record 					VARCHAR(5),
    Jan_Record 					VARCHAR(5),
    Feb_Record 					VARCHAR(5),
    Mar_Record 					VARCHAR(5),
    Apr_Record 					VARCHAR(5),
    May_Record 					VARCHAR(5),
    Jul_Record 					VARCHAR(5),
    Aug_Record 					VARCHAR(5),

    PRIMARY KEY(Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Standings(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Standings(Team_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),

    UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS Team_Vs_Team(
    Season_ID INT NOT NULL, 
    Team_ID   INT NOT NULL,
    Team_ABV  VARCHAR(3) NOT NULL,
    Team_Name VARCHAR(45) NOT NULL,
    ATL 	  VARCHAR(3),
    BOS 	  VARCHAR(3),
    BRK 	  VARCHAR(3),
    CHI 	  VARCHAR(3),
    CHA 	  VARCHAR(3),
    CHO 	  VARCHAR(3),
    CLE 	  VARCHAR(3),
    DAL 	  VARCHAR(3),
    DEN 	  VARCHAR(3),
    DET 	  VARCHAR(3),
    GSW 	  VARCHAR(3),
    HOU 	  VARCHAR(3),
    IND 	  VARCHAR(3),
    KCK 	  VARCHAR(3),
    LAC 	  VARCHAR(3),
    LAL 	  VARCHAR(3),
    MEM 	  VARCHAR(3),
    MIA 	  VARCHAR(3),
    MIL 	  VARCHAR(3),
    MIN 	  VARCHAR(3),
    NJN 	  VARCHAR(3),
    NOH 	  VARCHAR(3),
    NOJ 	  VARCHAR(3),
    NOK 	  VARCHAR(3),
    NOP 	  VARCHAR(3),    
    NYK 	  VARCHAR(3),
    OKC 	  VARCHAR(3),
    ORL 	  VARCHAR(3),
    PHI 	  VARCHAR(3),
    PHO 	  VARCHAR(3),
    POR 	  VARCHAR(3),
    SAC 	  VARCHAR(3), 
    SAS 	  VARCHAR(3), 
    SDC 	  VARCHAR(3),
    SEA 	  VARCHAR(3),
    TOR 	  VARCHAR(3), 
    UTA 	  VARCHAR(3), 
    VAN 	  VARCHAR(3),
    WAS 	  VARCHAR(3), 
    WSB 	  VARCHAR(3),

    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Standings(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Standings(Team_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),

    UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS Roster(
    Season_ID           INT NOT NULL,
    Team_ID             INT NOT NULL,
    Player_ID           INT NOT NULL,
    Team_ABV            VARCHAR(3) NOT NULL,
    Team_Name           VARCHAR(45) NOT NULL,
    Player_Number       INT NOT NULL,
    Player_Name         VARCHAR(45) NOT NULL,
    Player_Postion      VARCHAR(2) NOT NULL,
    Player_Height       VARCHAR(4) NOT NULL,
    Player_Weight       INT NOT NULL, 
    Birth_Date          VARCHAR(30) NOT NULL, 
    Player_Nationality  VARCHAR(2),
    Player_Experanice   VARCHAR(2) NOT NULL,
    Player_College_Name VARCHAR(45), 

    PRIMARY KEY (Season_ID, Team_ID, Player_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID),
    FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    CHECK(Player_ID BETWEEN 1 and 3278),

    UNIQUE(Season_ID, Team_ID, Player_ID)
);

CREATE TABLE IF NOT EXISTS Team_Stats(
    Season_ID           INT NOT NULL,
    Team_ID             INT NOT NULL,
    Team_ABV            VARCHAR(3) NOT NULL,
    Team_Name           VARCHAR(45) NOT NULL,

    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    UNIQUE(Season_ID, Team_ID)
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
    Coaches                       VARCHAR(45),

    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),

    UNIQUE(Season_ID, Team_ID)
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

    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),

    UNIQUE(Season_ID, Team_ID)
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
    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),

    UNIQUE(Season_ID, Team_ID, Opponent)
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

    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),

    UNIQUE(Season_ID, Team_ID, Opponent)
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

    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),

    UNIQUE(Season_ID, Team_ID, Opponent)
    );

CREATE TABLE IF NOT EXISTS Player_Stats(
    Season_ID           INT NOT NULL,
    Team_ID             INT NOT NULL,
    Player_ID           INT NOT NULL,
    Team_ABV            VARCHAR(3) NOT NULL,
    Team_Name           VARCHAR(45) NOT NULL,
    Birth_Date  		VARCHAR(30) NOT NULL,
    Player_Name 		VARCHAR(45) NOT NULL,

    PRIMARY KEY (Season_ID, Team_ID, Player_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID),
    FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    CHECK(Player_ID BETWEEN 1 and 3278),

    UNIQUE(Season_ID, Team_ID, Player_ID)
);

CREATE TABLE IF NOT EXISTS Player_Advanced(
    Season_ID                     INT NOT NULL,
    Team_ID                       INT NOT NULL,
    Player_ID                     INT NOT NULL,
    Team_ABV                      VARCHAR(3) NOT NULL,
    Team_Name                     VARCHAR(45) NOT NULL,
    Player_Name                   VARCHAR(45) NOT NULL,
    Player_Age                    VARCHAR(45) NOT NULL, 
    Games_Played       	          INT NOT NULL, 
    Minutes_Played                INT NOT NULL,
    Per_Minute_Production         FLOAT NOT NULL,
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
    Stat_Form                     VARCHAR(45) NOT NULL,  -- Career | Regular | Playoffs

    PRIMARY KEY (Season_ID, Team_ID, Player_ID),
    FOREIGN KEY (Season_ID) REFERENCES Player_Stats(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Player_Stats(Team_ID),
    FOREIGN KEY (Player_ID) REFERENCES Player_Stats(Player_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    CHECK(Player_ID BETWEEN 1 and 3278),

    UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form)

);

CREATE TABLE IF NOT EXISTS Player_Per_Game(
    Season_ID                       INT NOT NULL,
    Team_ID                         INT NOT NULL,
    Player_ID                       INT NOT NULL,
    Team_ABV                        VARCHAR(3) NOT NULL,
    Team_Name                       VARCHAR(45) NOT NULL,
    Player_Name                     VARCHAR(45) NOT NULL, -- Need to Rerun Web Scrapers
    Player_Age                      INT NOT NULL,
    League                          VARCHAR(3),
    Player_Postion                  VARCHAR(2),
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
    Offensive_Rebound               FLOAT,
    Defensive_Rebound               FLOAT,
    True_Rebound                    FLOAT,
    Assists                         FLOAT,
    Steals                          FLOAT,
    Blocks                          FLOAT,
    Turn_Over                       FLOAT,
    Personal_Foul                   FLOAT,
    Points                          FLOAT,
    Stat_Form                       VARCHAR(45) NOT NULL,  -- Career | Regular | Playoffs

    PRIMARY KEY (Season_ID, Team_ID, Player_ID),
    FOREIGN KEY (Season_ID) REFERENCES Player_Stats(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Player_Stats(Team_ID),
    FOREIGN KEY (Player_ID) REFERENCES Player_Stats(Player_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    CHECK(Player_ID BETWEEN 1 and 3278),

    UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form)
);

CREATE TABLE IF NOT EXISTS Player_Per_Minute(
    Season_ID                       INT NOT NULL,
    Team_ID                         INT NOT NULL,
    Player_ID                       INT NOT NULL,
    Team_ABV                        VARCHAR(3) NOT NULL,
    Team_Name                       VARCHAR(45) NOT NULL,
    Player_Name                     VARCHAR(45) NOT NULL, -- Need to Rerun Web Scrapers
    Player_Age                      INT NOT NULL,
    League                          VARCHAR(3),
    Player_Postion                  VARCHAR(2),
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
    Offensive_Rebound               FLOAT,
    Defensive_Rebound               FLOAT,
    True_Rebound                    FLOAT,
    Assists                         FLOAT,
    Steals                          FLOAT,
    Blocks                          FLOAT,
    Turn_Over                       FLOAT,
    Personal_Foul                   FLOAT,
    Points                          FLOAT,
    Stat_Form                       VARCHAR(45) NOT NULL,  -- Career | Regular | Playoffs

    PRIMARY KEY (Season_ID, Team_ID, Player_ID),
    FOREIGN KEY (Season_ID) REFERENCES Player_Stats(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Player_Stats(Team_ID),
    FOREIGN KEY (Player_ID) REFERENCES Player_Stats(Player_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    CHECK(Player_ID BETWEEN 1 and 3278),

    UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form)
);

CREATE TABLE IF NOT EXISTS Player_Per_Poss(
    Season_ID                       INT NOT NULL,
    Team_ID                         INT NOT NULL,
    Player_ID                       INT NOT NULL,
    Team_ABV                        VARCHAR(3) NOT NULL,
    Team_Name                       VARCHAR(45) NOT NULL,
    Player_Name                     VARCHAR(45) NOT NULL, -- Need to Rerun Web Scrapers
    Player_Age                      INT NOT NULL,
    League                          VARCHAR(3),
    Player_Postion                  VARCHAR(2),
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
    Offensive_Rebound               FLOAT,
    Defensive_Rebound               FLOAT,
    True_Rebound                    FLOAT,
    Assists                         FLOAT,
    Steals                          FLOAT,
    Blocks                          FLOAT,
    Turn_Over                       FLOAT,
    Personal_Foul                   FLOAT,
    Points                          FLOAT,
    Offensive_Rating                INT,
    Defensive_Rating                INT,
    Stat_Form                       VARCHAR(45) NOT NULL,  -- Career | Regular | Playoffs

    PRIMARY KEY (Season_ID, Team_ID, Player_ID),
    FOREIGN KEY (Season_ID) REFERENCES Player_Stats(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Player_Stats(Team_ID),
    FOREIGN KEY (Player_ID) REFERENCES Player_Stats(Player_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    CHECK(Player_ID BETWEEN 1 and 3278),

    UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form)
);

CREATE TABLE IF NOT EXISTS Player_Per_Totals(
    Season_ID                       INT NOT NULL,
    Team_ID                         INT NOT NULL,
    Player_ID                       INT NOT NULL,
    Team_ABV                        VARCHAR(3) NOT NULL,
    Team_Name                       VARCHAR(45) NOT NULL,
    Player_Name                     VARCHAR(45) NOT NULL, -- Need to Rerun Web Scrapers
    Player_Age                      INT NOT NULL,
    League                          VARCHAR(3),
    Player_Postion                  VARCHAR(2),
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
    Offensive_Rebound               FLOAT,
    Defensive_Rebound               FLOAT,
    True_Rebound                    FLOAT,
    Assists                         FLOAT,
    Steals                          FLOAT,
    Blocks                          FLOAT,
    Turn_Over                       FLOAT,
    Personal_Foul                   FLOAT,
    Points                          FLOAT,
    Triple_Double                   INT,
    Stat_Form                       VARCHAR(45) NOT NULL,  -- Career | Regular | Playoffs

    PRIMARY KEY (Season_ID, Team_ID, Player_ID),
    FOREIGN KEY (Season_ID) REFERENCES Player_Stats(Season_ID),
    FOREIGN KEY (Team_ID) REFERENCES Player_Stats(Team_ID),
    FOREIGN KEY (Player_ID) REFERENCES Player_Stats(Player_ID),
    CHECK(Season_ID BETWEEN 1980 AND 2021),
    CHECK(Team_ID BETWEEN 1 and 31),
    CHECK(Player_ID BETWEEN 1 and 3278),

    UNIQUE(Season_ID, Team_ID, Player_ID, Stat_Form)
);
