USE BasketBallDB;

INSERT INTO Season(Season_ID)
VALUES('1980');

INSERT INTO Team(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 2, "Boston Celtics", "BOS");

INSERT INTO Team(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 23, "Philadelphia 76Ers", "PHI");

INSERT INTO Team(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 14, "Los Angeles Lakers", "LAL");

INSERT INTO Player(Player_ID, Birth_Date, Player_Name)
VALUE(102, "September 2, 1948", "Tiny Archibald");

INSERT INTO Player(Player_ID, Birth_Date, Player_Name)
VALUE(246, "December 7, 1956", "Larry Bird");

INSERT INTO Standings(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 2, "Boston Celtics", "BOS"); 

INSERT INTO Standings(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 23, "Philadelphia 76Ers", "PHI"); 

INSERT INTO Standings(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 14, "Los Angeles Lakers", "LAL");

INSERT INTO Standard_Standings(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 2, "Boston Celtics", "BOS");

INSERT INTO Standard_Standings(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 23, "Philadelphia 76Ers", "PHI");

INSERT INTO Conference_Standings(Season_ID, Team_ID, Team_ABV, Team_Name, Wins, Loses, Win_Lose_Percentage, Games_Behind, Points_Per_Game, Opponents_Points_Per_Game, Simple_Rating_System, East_Or_West)
VALUES(1980, 2, "BOS", "Boston Celtics", 61, 21, 0.744, 0, 113.5, 105.7, 7.36, True);

INSERT INTO Conference_Standings(Season_ID, Team_ID, Team_ABV, Team_Name, Wins, Loses, Win_Lose_Percentage, Games_Behind, Points_Per_Game, Opponents_Points_Per_Game, Simple_Rating_System, East_Or_West)
VALUES(1980, 23, "PHI", "Philadelphia 76Ers", 59, 23, 0.72, 2, 109.1, 104.9, 4.04, True);

INSERT INTO Expanded_Standings(Season_ID, Team_ID, Team_ABV, Team_Name, Overall, Home_Record, Road_Record, Eastern_Conference_Record, Western_Conference_Record, Atlantic_Division_Record, 
							   Central_Division_Record, Midwestern_Divsion_Record, Pacific_Divsion_Record, Southeastern_Divsion_Record, Southwestern_Divsion_Record, Northwestern_Divsion_Record,
							   Pre_Allstar_Record, Post_Allstar_Record, Three_Point_Margin, Ten_Point_Margin, Oct_Record, Nov_Record, Dec_Record, Jan_Record, Feb_Record,  Mar_Record, Apr_Record, 
                               May_Record, Jul_Record, Aug_Record)
VALUES(1980, 2, "BOS", "Boston Celtics", "61-21", "35-6", "26-15", "45-15", "16-6", "17-7", "28-8", "9-1", "7-5", NULL, NULL, NULL, "40-13", "21-8", "8-7", "34-5", "7-2", "10-2", "12-5", "11-4","9-2", "12-6", NULL, NULL, NULL, NULL);

INSERT INTO Expanded_Standings(Season_ID, Team_ID, Team_ABV, Team_Name, Overall, Home_Record, Road_Record, Eastern_Conference_Record, Western_Conference_Record, Atlantic_Division_Record, 
							   Central_Division_Record, Midwestern_Divsion_Record, Pacific_Divsion_Record, Southeastern_Divsion_Record, Southwestern_Divsion_Record, Northwestern_Divsion_Record,
							   Pre_Allstar_Record, Post_Allstar_Record, Three_Point_Margin, Ten_Point_Margin, Oct_Record, Nov_Record, Dec_Record, Jan_Record, Feb_Record,  Mar_Record, Apr_Record, 
                               May_Record, Jul_Record, Aug_Record)
VALUES(1980, 14, "LAL", "Los Angeles Lakers", "60-22", "37-4", "23-18", "18-4", "42-18", "8-2", "10-2", "23-7", "19-11", NULL, NULL, NULL, "38-17", "22-5", "11-5", "26-6", "7-3", "9-6", "12-4", "10-4", "9-2", "13-3", NULL, NULL, NULL, NULL);

INSERT INTO Team_Vs_Team(Season_ID, Team_ID, Team_ABV, Team_Name, ATL, BOS, BRK, CHI, CHA, CHO, CLE, DAL, DEN, DET,
						GSW, HOU, IND, KCK, LAC, LAL, MEM, MIA, MIL, MIN,  NJN, NOH, NOJ, NOK, NOP, NYK, OKC, ORL, PHI, PHO, POR, SAC, SAS, SDC, SEA, TOR, UTA, VAN, WAS,  WSB)
VALUES(1980, 2, "BOS", "Boston Celtics", "4-2", NULL, NULL, "2-0", NULL, NULL, "4-2", NULL, "2-0", "6-0", "2-0", "6-0", "4-2", "1-1", NULL, "0-2", NULL, NULL, "2-0", NULL, "5-1", NULL, 
NULL, NULL, NULL, "5-1", NULL, NULL, "3-3", "1-1", "2-0", NULL, "4-2", "2-0", "0-2", NULL, "2-0", NULL, NULL, "4-2");

INSERT INTO Roster(Season_ID, Team_ID, Player_ID, Team_ABV, Team_Name, Player_Number, Player_Name, Player_Postion, Player_Height, 
						Player_Weight, Birth_Date, Player_Nationality, Player_Experanice, Player_College_Name)
VALUES(1980, 2, 102, "BOS", "Boston Celtics", 7 , "Tiny Archibald", "PG", "6-1", 150, "September 2, 1948", "US", "8", "Texas-El Paso");

INSERT INTO Roster(Season_ID, Team_ID, Player_ID, Team_ABV, Team_Name, Player_Number, Player_Name, Player_Postion, Player_Height, 
						Player_Weight, Birth_Date, Player_Nationality, Player_Experanice, Player_College_Name)
VALUES(1980, 2, 246, "BOS", "Boston Celtics", 33, "Larry Bird", "PF", "6-9", 220, "December 7, 1956", "US", "R", "Indiana State University");