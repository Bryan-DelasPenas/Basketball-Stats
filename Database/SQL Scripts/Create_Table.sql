USE BasketballDB;

CREATE TABLE IF NOT EXISTS Season(
	Season_ID INT NOT NULL UNIQUE, 
	PRIMARY KEY (season_ID)
);

CREATE TABLE IF NOT EXISTS Team(
	Season_ID INT NOT NULL, 
    Team_ID  INT NOT NULL UNIQUE,
    Team_Name VARCHAR(45) NOT NULL,
    Team_ABV VARCHAR(3) NOT NULL,
	PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
    UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS Player(
	Player_ID INT NOT NULL,
    Birth_Date VARCHAR(30) NOT NULL,
    Player_Name VARCHAR(45) NOT NULL,
	PRIMARY KEY(Player_ID)
);

CREATE TABLE IF NOT EXISTS Standings(
	Season_ID INT NOT NULL,
    Team_ID INT NOT NULL,
    Team_Name VARCHAR(45) NOT NULL,
	Team_ABV VARCHAR(3) NOT NULL,
	PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
	FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID),
	UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS Standard_Standings(
	Season_ID INT NOT NULL, 
	Team_ID INT NOT NULL,
    Team_Name VARCHAR(45) NOT NULL UNIQUE,
	Team_ABV VARCHAR(3) NOT NULL UNIQUE,
    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Standings(Season_ID),
	FOREIGN KEY (Team_ID) REFERENCES Standings(Team_ID),
	UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS East_Standings(
	Season_ID INT NOT NULL,
    Team_ID   INT NOT NULL, 
    Team_ABV  VARCHAR(3) NOT NULL,
    Team_Name VARCHAR(45) NOT NULL,
	Wins  INT NOT NULL,
    Loses INT NOT NULL,
    Win_Lose_Percentage FLOAT NOT NULL,
    Games_Behind INT NOT NULL,    -- May have to change the output in the csv 
    Points_Per_Game FLOAT NOT NULL, 
    Opponents_Points_Per_Game FLOAT NOT NULL,
    Simple_Rating_System FLOAT NOT NULL, 
    PRIMARY KEY (Season_ID, Team_ID),
	FOREIGN KEY (Season_ID) REFERENCES Standard_Standings(Season_ID),
	FOREIGN KEY (Team_ID) REFERENCES Standard_Standings(Team_ID),
    UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS West_Standings(
	Season_ID INT NOT NULL,
    Team_ID INT NOT NULL, 
    Team_ABV VARCHAR(3) NOT NULL,
    Team_Name VARCHAR(45) NOT NULL,
	Wins INT NOT NULL,
    Loses INT NOT NULL,
    Win_Lose_Percentage FLOAT NOT NULL,
    Games_Behind INT NOT NULL,    -- May have to change the output in the csv 
    Points_Per_Game FLOAT NOT NULL, 
    Opponents_Points_Per_Game FLOAT NOT NULL,
    Simple_Rating_System FLOAT NOT NULL, 
    PRIMARY KEY (Season_ID, Team_ID),
	FOREIGN KEY (Season_ID) REFERENCES Standard_Standings(Season_ID),
	FOREIGN KEY (Team_ID) REFERENCES Standard_Standings(Team_ID),
	UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS Expanded_Standings(
	Season_ID INT NOT NULL,
    Team_ID INT NOT NULL,
    Team_ABV VARCHAR(3) NOT NULL,
    Team_Name VARCHAR(45) NOT NULL,
	Overall VARCHAR(45) NOT NULL,
    Home_Record VARCHAR(45) NOT NULL,
    Road_Record VARCHAR(45) NOT NULL,
    Eastern_Conference_Record VARCHAR(5),
    Western_Conference_Record VARCHAR(5),
    Atlantic_Division_Record VARCHAR(5), 
    Central_Division_Record VARCHAR(5), 
    Midwestern_Divsion_Record VARCHAR(5),
    Pacific_Divsion_Record VARCHAR(5),
    Southeastern_Divsion_Record VARCHAR(5),
    Southwestern_Divsion_Record VARCHAR(5),
    Northwestern_Divsion_Record VARCHAR(5),
    Pre_Allstar_Record VARCHAR(5),
    Post_Allstar_Record VARCHAR(5),
    3_Point_Margin VARCHAR(5),
    10_Point_Margin VARCHAR(5),
    Oct_Record VARCHAR(5),
    Nov_Record VARCHAR(5),
    Dec_Record VARCHAR(5),
    Jan_Record VARCHAR(5),
    Feb_Record VARCHAR(5),
    Mar_Record VARCHAR(5),
    Apr_Record VARCHAR(5),
    May_Record VARCHAR(5),
    Jul_Record VARCHAR(5),
    Aug_Record VARCHAR(5),
    PRIMARY KEY(Season_ID, Team_ID),
	FOREIGN KEY (Season_ID) REFERENCES Standings(Season_ID),
	FOREIGN KEY (Team_ID) REFERENCES Standings(Team_ID),
	UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS Team_Vs_Team(
	Season_ID INT NOT NULL, 
	Team_ID INT NOT NULL,
    Team_ABV VARCHAR(3) NOT NULL,
    Team_Name VARCHAR(45) NOT NULL,
    ATL VARCHAR(3),
    BOS VARCHAR(3),
    BRK VARCHAR(3),
	CHI VARCHAR(3),
	CHA VARCHAR(3),
    CHO VARCHAR(3),
    CLE VARCHAR(3),
    DAL VARCHAR(3),
    DEN VARCHAR(3),
    DET VARCHAR(3),
    GSW VARCHAR(3),
    HOU VARCHAR(3),
    IND VARCHAR(3),
    KCK VARCHAR(3),
    LAC VARCHAR(3),
    LAL VARCHAR(3),
    MEM VARCHAR(3),
    MIA VARCHAR(3),
    MIL VARCHAR(3),
    MIN VARCHAR(3),
    NJN VARCHAR(3),
    NOH VARCHAR(3),
    NOJ VARCHAR(3),
	NOK VARCHAR(3),
    NOP VARCHAR(3),    
    NYK VARCHAR(3),
    OKC VARCHAR(3),
    ORL VARCHAR(3),
    PHI VARCHAR(3),
    PHO VARCHAR(3),
    POR VARCHAR(3),
    SAC VARCHAR(3), 
    SAS VARCHAR(3), 
    SDC VARCHAR(3),
    SEA VARCHAR(3),
    TOR VARCHAR(3), 
    UTA VARCHAR(3), 
    VAN VARCHAR(3),
    WAS VARCHAR(3), 
    WSB VARCHAR(3),
    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Standings(Season_ID),
	FOREIGN KEY (Team_ID) REFERENCES Standings(Team_ID),
	UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS Roster(
	Season_ID INT NOT NULL,
    Team_ID INT NOT NULL,
    Team_Name VARCHAR(45) NOT NULL,
	Team_ABV VARCHAR(3) NOT NULL,
	PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
	FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID),
	UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE IF NOT EXISTS Team_Roster(
	Season_ID INT NOT NULL,
    Team_ID INT NOT NULL,
    Player_ID INT NOT NULL,
    Team_ABV VARCHAR(3) NOT NULL,
    Team_Name VARCHAR(45) NOT NULL,
    Player_Number INT NOT NULL,
    Player_Name VARCHAR(45) NOT NULL,
    Postion VARCHAR(2) NOT NULL,
    Height VARCHAR(4) NOT NULL,
    Weight INT NOT NULL, 
    Birth_Date VARCHAR(30) NOT NULL, 
    Nationality VARCHAR(2),
    Experanice VARCHAR(2) NOT NULL,
    College_Name VARCHAR(45), 
    PRIMARY KEY (Season_ID, Team_ID, Player_ID),
    FOREIGN KEY (Season_ID) REFERENCES Roster(Season_ID),
	FOREIGN KEY (Team_ID) REFERENCES Roster(Team_ID),
	FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID),
    UNIQUE(Season_ID, Team_ID, Player_ID)
);