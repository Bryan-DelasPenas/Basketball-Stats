USE BasketBallDB;

INSERT INTO Season(Season_ID)
VALUES(1980);

INSERT INTO Team(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 2, "Boston Celtics", "BOS");

INSERT INTO Team(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 23, "Philadelphia 76Ers", "PHI");

INSERT INTO Standings(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 2, "Boston Celtics", "BOS"); 

INSERT INTO Standings(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 23, "Philadelphia 76Ers", "PHI"); 

INSERT INTO Standard_Standings(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 2, "Boston Celtics", "BOS");

INSERT INTO Standard_Standings(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 23, "Philadelphia 76Ers", "PHI");

INSERT INTO East_Standings(Season_ID, Team_ID, Team_ABV, Team_Name, Wins, Loses, Win_Lose_Percentage, Games_Behind, Points_Per_Game, Opponents_Points_Per_Game, Simple_Rating_System)
VALUES(1980, 2, "BOS", "Boston Celtics", 61, 21, 0.744, 0, 113.5, 105.7, 7.36);

INSERT INTO East_Standings(Season_ID, Team_ID, Team_ABV, Team_Name, Wins, Loses, Win_Lose_Percentage, Games_Behind, Points_Per_Game, Opponents_Points_Per_Game, Simple_Rating_System)
VALUES(1980, 23, "PHI", "Philadelphia 76Ers", 59, 23, 0.72, 2, 109.1, 104.9, 4.04);