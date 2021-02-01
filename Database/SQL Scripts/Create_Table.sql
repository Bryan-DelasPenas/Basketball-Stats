USE BasketballDB;

CREATE TABLE Season(
	Season_ID INT NOT NULL UNIQUE, 
	PRIMARY KEY (season_ID)
);

CREATE TABLE Team(
	Season_ID INT NOT NULL, 
    Team_ID   INT NOT NULL UNIQUE,
    Team_Name VARCHAR(45) NOT NULL,
    Team_ABV  VARCHAR(3) NOT NULL,
	PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
    UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE Player(
	Player_ID     INT NOT NULL,
    Date_Of_Birth DATE NOT NULL,
    player_name   VARCHAR(45) NOT NULL,
	PRIMARY KEY(Player_ID)
);

CREATE TABLE Standings(
	Season_ID   INT NOT NULL,
    Team_ID   	INT NOT NULL,
    Team_Name   VARCHAR(45) NOT NULL,
	Team_ABV	VARCHAR(3) NOT NULL,
	PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID),
	FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID),
	UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE Standard_Standings(
	Season_ID 	INT NOT NULL, 
	Team_ID 	INT NOT NULL,
    Team_Name   VARCHAR(45) NOT NULL UNIQUE,
	Team_ABV	VARCHAR(3) NULL UNIQUE,
    PRIMARY KEY (Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES Standings(Season_ID),
	FOREIGN KEY (Team_ID) REFERENCES Standings(Team_ID),
	UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE East_Standings(
	Season_ID 			      INT NOT NULL,
    Team_ID   				  INT NOT NULL, 
    Team_ABV  				  VARCHAR(3) NOT NULL,
    Team_Name 				  VARCHAR(45) NOT NULL,
	Wins      				  INT NOT NULL,
    Loses               	  INT NOT NULL,
    Win_Lose_Percentage 	  FLOAT NOT NULL,
    Games_Behind        	  INT NOT NULL,    -- May have to change the output in the csv 
    Points_Per_Game     	  FLOAT NOT NULL, 
    Opponents_Points_Per_Game FLOAT NOT NULL,
    Simple_Rating_System      FLOAT NOT NULL, 
    PRIMARY KEY (Season_ID, Team_ID),
	FOREIGN KEY (Season_ID) REFERENCES Standard_Standings(Season_ID),
	FOREIGN KEY (Team_ID) REFERENCES Standard_Standings(Team_ID),
    UNIQUE(Season_ID, Team_ID)
);

CREATE TABLE West_Standings(
	Season_ID 			      INT NOT NULL,
    Team_ID   				  INT NOT NULL, 
    Team_ABV  				  VARCHAR(3) NOT NULL,
    Team_Name 				  VARCHAR(45) NOT NULL,
	Wins      				  INT NOT NULL,
    Loses               	  INT NOT NULL,
    Win_Lose_Percentage 	  FLOAT NOT NULL,
    Games_Behind        	  INT NOT NULL,    -- May have to change the output in the csv 
    Points_Per_Game     	  FLOAT NOT NULL, 
    Opponents_Points_Per_Game FLOAT NOT NULL,
    Simple_Rating_System      FLOAT NOT NULL, 
    PRIMARY KEY (Season_ID, Team_ID),
	FOREIGN KEY (Season_ID) REFERENCES Standard_Standings(Season_ID),
	FOREIGN KEY (Team_ID) REFERENCES Standard_Standings(Team_ID),
	UNIQUE(Season_ID, Team_ID)
);