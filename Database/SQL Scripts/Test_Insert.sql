USE BasketBallDB;

INSERT INTO Season(Season_ID)
VALUES(1980);

INSERT INTO Season(Season_ID)
VALUES(1981);

INSERT INTO Team(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 2, "Boston Celtics", "BOS");

INSERT INTO Team(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 23, "Philadelphia 76Ers", "PHI");

INSERT INTO Team(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1980, 14, "Los Angeles Lakers", "LAL");

INSERT INTO Team(Season_ID, Team_ID, Team_Name, Team_ABV)
VALUES(1981, 2, "Boston Celtics", "BOS");

INSERT INTO Player(Player_ID, Birth_Date, Player_Name)
VALUE(102, "September 2, 1948", "Tiny Archibald");

INSERT INTO Player(Player_ID, Birth_Date, Player_Name)
VALUE(246, "December 7, 1956", "Larry Bird");

INSERT INTO Conference_Standings(Season_ID, Team_ID, Team_ABV, Team_Name, Wins, Loses, Win_Lose_Percentage, Games_Behind, Points_Per_Game, Opponents_Points_Per_Game, Simple_Rating_System, East_Or_West)
VALUES(1980, 2, "BOS", "Boston Celtics", 61, 21, 0.744, 0, 113.5, 105.7, 7.36, True);

INSERT INTO Conference_Standings(Season_ID, Team_ID, Team_ABV, Team_Name, Wins, Loses, Win_Lose_Percentage, Games_Behind, Points_Per_Game, Opponents_Points_Per_Game, Simple_Rating_System, East_Or_West)
VALUES(1980, 23, "PHI", "Philadelphia 76Ers", 59, 23, 0.72, 2, 109.1, 104.9, 4.04, True);

INSERT INTO Roster(Season_ID, Team_ID, Player_ID, Team_ABV, Team_Name, Player_Number, Player_Name, Player_Postion, Player_Height, 
						Player_Weight, Birth_Date, Player_Nationality, Player_Experanice, Player_College_Name)
VALUES(1980, 2, 102, "BOS", "Boston Celtics", 7 , "Tiny Archibald", "PG", "6-1", 150, "September 2, 1948", "US", "8", "Texas-El Paso");

INSERT INTO Roster(Season_ID, Team_ID, Player_ID, Team_ABV, Team_Name, Player_Number, Player_Name, Player_Postion, Player_Height, 
Player_Weight, Birth_Date, Player_Nationality, Player_Experanice, Player_College_Name)
VALUES(1980, 2, 246, "BOS", "Boston Celtics", 33, "Larry Bird", "PF", "6-9", 220, "December 7, 1956", "US", "R", "Indiana State University");

INSERT INTO Team_Stats(Season_ID, Team_ID, Team_ABV, Team_Name)
VALUE(1980, 2, "BOS", "Boston Celtics");

INSERT INTO Team_Stats(Season_ID, Team_ID, Team_ABV, Team_Name)
VALUES(1980, 23, "PHI", "Philadelphia 76Ers"); 

INSERT INTO Team_Advanced(Season_ID, Team_ID, Team_ABV, Team_Name, Team_Wins, Team_Loses, Win_Lose_Percentage, Team_Finish, Simple_Rating_System, Pace, Relative_Pace, 
						  Offensive_Rating, Relative_Offensive_Rating, Defensive_Rating, Relative_Defensive_Rating, Playoffs_Finish, Coaches)
VALUES(1980, 2, "BOS", "Boston Celtics", 61, 21, 0.744, "1st of 5th", 7.37, 102.6, -0.5, 109.4, 4.1, 101.9, -3.4, "Lost E Conf. Finals", "B.Fitch"); 

INSERT INTO Team_Advanced(Season_ID, Team_ID, Team_ABV, Team_Name, Team_Wins, Team_Loses, Win_Lose_Percentage, Team_Finish, Simple_Rating_System, Pace, Relative_Pace, 
						  Offensive_Rating, Relative_Offensive_Rating, Defensive_Rating, Relative_Defensive_Rating, Playoffs_Finish, Coaches)
VALUES(1980, 23, "PHI", "Philadelphia 76Ers", 59, 23, .72, "2nd of 5th", 4.04, 103.0, -0.1, 105, -0.3, 101.0, -4.3, "Lost Finals", "B.Cunningham (59-23)");

-- Regular Team Per Game
INSERT INTO Team_Per_Game(Season_ID, Team_ID, Team_ABV, Team_Name,  Games_Played, Minutes_Played, Field_Goals_Made, Field_Goals_Attempted, Field_Goals_Percentage,
    Three_Points_Made, Three_Points_Attempted, Three_Points_Percentage, Two_Points_Made, Two_Points_Attempted, Two_Points_Percentage, Free_Throws_Made,
    Free_Throws_Attempted, Free_Throws_Percentage, Offensive_Rebound, Defensive_Rebound, True_Rebound, Assists, Steals, Blocks, Turn_Over, Personal_Foul, Points, Opponent)
VALUES(1980, 2, "BOS", "Boston Celtics", 82, 242.4, 44.1, 90.1, .490, 2.0, 5.1, .384, 42.1, 84.9, .496, 23.3, 29.9, .779, 15.0, 30.0, 44.9, 26.8, 9.9, 3.8, 18.8, 24.1, 113.5, False);
    
INSERT INTO Team_Per_Game(Season_ID, Team_ID, Team_ABV, Team_Name,  Games_Played, Minutes_Played, Field_Goals_Made, Field_Goals_Attempted, Field_Goals_Percentage,
    Three_Points_Made, Three_Points_Attempted, Three_Points_Percentage, Two_Points_Made, Two_Points_Attempted, Two_Points_Percentage, Free_Throws_Made,
    Free_Throws_Attempted, Free_Throws_Percentage, Offensive_Rebound, Defensive_Rebound, True_Rebound, Assists, Steals, Blocks, Turn_Over, Personal_Foul, Points, Opponent)
VALUES(1980, 23, "PHI", "Philadelphia 76Ers", 82, 242.1, 43.0, 87.3, .492, 0.3, 1.5, .216, 42.6, 85.7, .497, 22.9, 29.6, .772, 14.5, 32.1, 46.6, 27.1, 9.7, 8.0, 20.8, 22.7, 109.1, False);

INSERT INTO Team_Misc(Season_ID, Team_ID, Team_ABV, Team_Name, Team_Average_Age, Team_Wins, Team_Loses, Pythagorean_Wins, Pythagorean_Loses, Margin_Of_Victory, Strength_Of_Schedule,
    Simple_Rating_System, Offensive_Rating, Defensive_Rating, Net_Rating, Pace, Free_Throw_Attempt_Rate, Three_Point_Attempt_Rate,  True_Shooting_Percentage, Offensive_Rebound_Percentage, 
    Defensive_Rebound_Percentage, Arena, Attend, Attend_Per_Game)
VALUES(1980, 2, "BOS", "Boston Celtics", 27.3,61,21,60,22,7.79,-0.42,7.37,109.4,101.9,+7.5,102.6,.332,.057,.550,34.8,67.8,'Boston Garden',596349,14664);

INSERT INTO Team_Per_Poss(Season_ID, Team_ID, Team_ABV, Team_Name,  Games_Played, Minutes_Played, Field_Goals_Made, Field_Goals_Attempted, Field_Goals_Percentage,
    Three_Points_Made, Three_Points_Attempted, Three_Points_Percentage, Two_Points_Made, Two_Points_Attempted, Two_Points_Percentage, Free_Throws_Made,
    Free_Throws_Attempted, Free_Throws_Percentage, Offensive_Rebound, Defensive_Rebound, True_Rebound, Assists, Steals, Blocks, Turn_Over, Personal_Foul, Points, Opponent)
VALUES(1980, 2, "BOS", "Boston Celtics",82,19880,42.6,86.9,.490,1.9,5.0,.384,40.6,81.9,.496,22.4,28.8,.779,14.4,28.9,43.3,25.9,9.5,3.6,18.1,23.2,109.4, False);
    
INSERT INTO Team_Per_Poss(Season_ID, Team_ID, Team_ABV, Team_Name,  Games_Played, Minutes_Played, Field_Goals_Made, Field_Goals_Attempted, Field_Goals_Percentage,
    Three_Points_Made, Three_Points_Attempted, Three_Points_Percentage, Two_Points_Made, Two_Points_Attempted, Two_Points_Percentage, Free_Throws_Made,
    Free_Throws_Attempted, Free_Throws_Percentage, Offensive_Rebound, Defensive_Rebound, True_Rebound, Assists, Steals, Blocks, Turn_Over, Personal_Foul, Points, Opponent)
VALUES(1980, 23, "PHI", "Philadelphia 76Ers",82,19855,3523,7156,.492,27,125,.216,3496,7031,.497,1876,2431,.772,1187,2635,3822,2226,792,652,1708,1860,8949, False);

INSERT INTO Team_Totals(Season_ID, Team_ID, Team_ABV, Team_Name,  Games_Played, Minutes_Played, Field_Goals_Made, Field_Goals_Attempted, Field_Goals_Percentage,
    Three_Points_Made, Three_Points_Attempted, Three_Points_Percentage, Two_Points_Made, Two_Points_Attempted, Two_Points_Percentage, Free_Throws_Made,
    Free_Throws_Attempted, Free_Throws_Percentage, Offensive_Rebound, Defensive_Rebound, True_Rebound, Assists, Steals, Blocks, Turn_Over, Personal_Foul, Points, Opponent)
VALUES(1980, 2, "BOS", "Boston Celtics",82,19880,42.6,86.9,.490,1.9,5.0,.384,40.6,81.9,.496,22.4,28.8,.779,14.4,28.9,43.3,25.9,9.5,3.6,18.1,23.2,109.4, False);
    
INSERT INTO Team_Totals(Season_ID, Team_ID, Team_ABV, Team_Name,  Games_Played, Minutes_Played, Field_Goals_Made, Field_Goals_Attempted, Field_Goals_Percentage,
    Three_Points_Made, Three_Points_Attempted, Three_Points_Percentage, Two_Points_Made, Two_Points_Attempted, Two_Points_Percentage, Free_Throws_Made,
    Free_Throws_Attempted, Free_Throws_Percentage, Offensive_Rebound, Defensive_Rebound, True_Rebound, Assists, Steals, Blocks, Turn_Over, Personal_Foul, Points, Opponent)
VALUES(1980, 23, "PHI", "Philadelphia 76Ers", 82,19855,41.3,84.0,.492,0.3,1.5,.216,41.0,82.5,.497,22.0,28.5,.772,13.9,30.9,44.8,26.1,9.3,7.7,20.0,21.8,105.0, False);

