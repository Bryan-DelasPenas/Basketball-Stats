# Python Scrapers API

## General Basketball Definitions 

### Efficiency Stats
<strong>Per-Game:</strong> is the amount of any catergory the player gets and divide by the amount of games played
<strong>Per-Minute:</strong> Is calculated by the total of any category(points, rebounds, etc.) and divided by total minutes played. Common notion is 36 or 40 minute stats<br>
<strong>Per-Possession:</strong> Instead of taking the number of minutes a player played to a 36 minute number, it compares the number of possessions a player was on the floor for the stat<br>
<strong>Totals:</strong> Is the total amount of any category<br>

### Equations 
<strong>Assit Percentage</strong> or AST% =<br>
```
    100 * Assits / (((Minutes Played / (Team Minutes Played)) * Team Field Goals) - Field Goals)
```
<strong>Block Percentage</strong> or BLK% =<br>
```
    100 * (Block * (Team Minutes Played / 5)) / 
    (Minutes Played * (Opponent Field Goals Attempts - Opponent 3 Points Attempts))
```
<strong>Defensive Rebound Percentage</strong> or DRB% =<br>
```
    100 * (Defensive Rebound * (Team Minutes Played / 5)) / 
    (Minutes Played * (Team Defensive Rebound + Opponent Offensive Rebound))
```
<strong>Effective Field Goal Perventage</strong> or eFG% =<br>
```
    (Field Goals + 0.5 * 3 Points) / Field Goals Attempted
```
<strong>Games Behind</strong> or GB =<br>
```
    ((First Place Team Wins - Wins) + (Losses - First Place Team Losses)) / 2
```
<strong>Game Score</strong> or Game Score =<br>
```
    Points + 0.4 * Field Goals - 0.7 * Field Goals Attempts - 0.4*(Free Throw Attempt - Free Throw) + 0.7 * Offensive Rebounds 
    + 0.3 * Defensive Rebounds + Steals + 0.7 * Assits + 0.7 * Block - 0.4 * Personal Foul - Turn Overs
```
<strong>Margin of Victory</strong> or MOV =<br>
```
    Points - Opponent Points
```
<strong>Offensive Rebound Percentage</strong> or ORB% =<br>
```
    100 * (Offensive Rebound * (Team Minutes Played / 5)) 
    / (Minutes Played * (Team Offensive Rebound + Opponent Defensive Rebound))
```
<strong>Pace Factor</strong> or Pace =<br>
```
    48 * ((Team Possession + Opponent Possession) / (2 * (Team Minutes Played / 5)))
```
<strong>Possession</strong> or Poss =<br>
```
    0.5 * ((Team Field Goals Attempts + 0.4 * Team Free Throw Attempts - 1.07 * (Team Offensive Rebounds / (Team Offensive Rebounds + Opponnent Defensive Rebounds)) 
    * (Team Field Goals Attempts - Team Field Goals) + Team Turnover) + (Opponent Field Goal Attempts + 0.4 * Opponent Free Throw Attempts - 1.07 * 
    (Opponent Offensive Rebound / (Opponent Offensive + Team Defensive)) * (Opponent Field Goals Attempts - Opponnent Field Goals) + Opponent Turnover))
```
<strong>Steal Percentage</strong> or STL% =<br>
```
    100 * (Steal * (Team Minutes Played / 5)) / (Minutes Played * Opponent Possession)
```
<strong>Turnover Percentage</strong> or TOV% =<br>
```
    100 * Turnover / (Field Goals Attempts + 0.44 * Free Throw Attempts + Turnover)
```
<strong>Total Rebound Percentage</strong> or TRB% =<br>
```
    100 * (Total Rebound * (Team Minute Played / 5)) / (Minute Played * (Team Total Rebound + Opponent Total Rebound))
```
<strong>True Shooting Attempts:</strong> or TSA<br>
```
    (Field Goals Attempted + 0.44) / FTA
```
<strong>True Shooting:</strong> or TS% =<br>
```
    (Points) / (2 * True Shooting Attempts)
```
<strong>Usage Percentage</strong> or US% =<br>
```
    100 * ((Field Goals Attempted + 0.44 * Free Throw Attempted + Turn Overs) * (Team Minutes Played / 5)) 
    / (Minutes Played * (Team Field Goals + 0.44 * Team Free Throw Attempts + Team Turn Overs))
```
<strong>Win-Lost Percentage</strong> or W/L% =<br>
```
    Wins / (Wins + Loses)
```

## Season Stats Scraper
### `get_team_name(season)` 
<strong>Parameters:</strong><br>
    - `season` - NBA season(only from 1980 to current year)<br>
<strong>Returns:</strong><br>
A Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Team', 'Team ABV'] 
```
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int corresponding to a team<br>
    - `Team` is the name of the Team<br>
    - `Team ABV` is the team abbreviation<br>

### `get_standings(season, data_format)`
<strong>Parameters:</strong><br>
    `season`      - NBA season(only from 1980 to current year)<br>
    `data_format` - One of `'Expanded Standing' | 'Standard' |'Team_Vs_Team'` where default value is `Standard`<br>
<strong>Returns:</strong><br>

#### For Expanded Standings
For `'Expanded Standings'` and `'season'` of 1980 and 1981, it will return a Pandas Dataframe with the following columns
```
    ['Season', 'Team ID', 'Team ABV', 'Team', 'Overall', 'Home Record', 'Road Record', 'Eastern Conference Record', 'Western Conference Record',
    'Atlantic Division Record', 'Central Division Record', 'Midwesterm Division Record', 'Pacific Division Record', 'Pre Allstar Record', 'Post Allstar Record',
    '3 Point Margin', '10 Point Margin', 'Oct Record', 'Nov Record', 'Dec Record', 'Jan Record', 'Feb Record', 'Mar Record']
```
For `'Expanded Standings'` and `'season'` between 1988 and 1997, it will return a Pandas Dataframe with the following columns 
```
    ['Season', 'Team ID, 'Team ABV' 'Team',  'Overall', 'Home Record', 'Road Record', 'Eastern Conference Record', 'Western Conference Record', 'Atlantic Division Record',
    'Central Division Record', 'Midwesterm Division Record', 'Pacific Division Record', 'Pre Allstar Record', 'Post Allstar Record','3 Point Margin', '10 Point Margin', 
    'Nov Record', 'Dec Record', 'Jan Record', 'Feb Record', 'Mar Record', 'Apr Record']
```
For `'Expanded Standings'` and `'season'` of 1999, it will return a Pandas Dataframe with the following columns 
```
    [''Season', 'Team ID, 'Team ABV', 'Team', 'Overall', 'Home Record', 'Road Record', 'Eastern Conference Record', 'Western Conference Record', 'Atlantic Division Record',
    'Central Division Record', 'Midwesterm Division Record', 'Pacific Division Record', '3 Point Margin', '10 Point Margin', 'Feb Record', 'Mar Record', 'Apr Record', 
    'May Record']
```
For `'Expanded Standings'` and `'season'` of 2000, it will return a Pandas Dataframe with the following columns 
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'Overall', 'Home Record', 'Road Record', 'Eastern Conference Record', 'Western Conference Record', 'Atlantic Division Record',
    'Central Division Record', 'Midwesterm Division Record', 'Pacific Division Record', 'Pre Allstar Record', 'Post Allstar Record','3 Point Margin', '10 Point Margin', 
    'Nov Record', 'Dec Record', 'Jan Record', 'Feb Record', 'Mar Record', 'Apr Record']
```
For `'Expanded Standings'` and `'season'` of 2005 or 2006, it will return a Pandas Dataframe with the following columns 
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'Overall', 'Home Record', 'Road Record', 'Eastern Conference Record', 'Western Conference Record', 'Atlantic Division Record',
    'Central Division Record', 'Southeastern Division Record', 'Northwestern Division Record', 'Pacific Division Record', 'Southwestern Division Record', 
    'Pre Allstar Record', 'Post Allstar Record','3 Point Margin', '10 Point Margin', 'Nov Record', 'Dec Record', 'Jan Record', 'Feb Record', 'Mar Record', 'Apr Record']
```
For `'Expanded Standings'` and `'season'` of 2012, it will return a Pandas Dataframe with the following columns 
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'Overall', 'Home Record', 'Road Record', 'Eastern Conference Record', 'Western Conference Record', 'Atlantic Division Record',
    'Central Division Record', 'Southeastern Division Record', 'Northwestern Division Record', 'Pacific Division Record', 'Southwestern Division Record', 
    'Pre Allstar Record', 'Post Allstar Record','3 Point Margin', '10 Point Margin', 'Dec Record', 'Jan Record', 'Feb Record', 'Mar Record', 'Apr Record']
```
For `'Expanded Standings'` and `'season'` of 2007 between 2019 excluding 2012, it will return a Pandas Dataframe with the following columns
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'Overall', 'Home Record', 'Road Record', 'Eastern Conference Record', 'Western Conference Record', 'Atlantic Division Record',
    'Central Division Record', 'Southeastern Division Record', 'Northwestern Division Record', 'Pacific Division Record', 'Southwestern Division Record', 
    'Pre Allstar Record', 'Post Allstar Record','3 Point Margin', '10 Point Margin', 'Oct Record', 'Nov Record', 'Dec Record', 'Jan Record', 'Feb Record', 
    'Mar Record', 'Apr Record']
```
For `'Expanded Standings'` and `'season'` of 2020, it will return a Pandas Dataframe with the following columns
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'Overall', 'Home Record', 'Road Record', 'Eastern Conference Record', 'Western Conference Record', 'Atlantic Division Record',
    'Central Division Record', 'Southeastern Division Record', 'Northwestern Division Record', 'Pacific Division Record', 'Southwestern Division Record', 
    'Pre Allstar Record', 'Post Allstar Record', '3 Point Margin', '10 Point Margin', 'Oct Record', 'Nov Record', 'Dec Record', 'Jan Record', 'Feb Record', 'Mar Record', 
    'Jul Record', 'Aug Record']
```
For `'Expanded Standings'` and `'season'` of 2021, it will return a Pandas Dataframe with the following columns
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'Overall', 'Home Record', 'Road Record', 'Eastern Conference Record', 'Western Conference Record', 'Atlantic Division Record',
    'Central Division Record', 'Southeastern Division Record', 'Northwestern Division Record', 'Pacific Division Record', 'Southwestern Division Record', 
    'Pre Allstar Record', 'Post Allstar Record','3 Point Margin', '10 Point Margin', 'Dec Record', 'Jan Record', 'Feb Record', 'Mar Record']
```
For `'Expanded Standings'` and `'season'` it not any above, it will return a Pandas Dataframe with the following columns
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'Overall', 'Home Record', 'Road Record', 'Eastern Conference Record', 'Western Conference Record', 'Atlantic Division Record',
    'Central Division Record', 'Midwesterm Division Record', 'Pacific Division Record', 'Pre Allstar Record', 'Post Allstar Record','3 Point Margin', '10 Point Margin', 
    'Oct Record', 'Nov Record', 'Dec Record', 'Jan Record', 'Feb Record', 'Mar Record', 'Apr Record']
```
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int corresponding to a team<br>
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `Overall` is the overall record of a team<br>
    - `Home Record` is the record when playing at home
    - `Road Record` is the record when not playing at home<br>
    - `Eastern Conference Record` is the record against Eastern Conference Teams<br>
    - `Western Conference Record` is the record against Western Conference Teams<br>
    - `Atlantic Division Record` is the record against Alatantic Division Teams<br>
    - `Central Division Record` is the record against Central Division Teams<br>
    - `Midwesterm Division Record` is the record against Midwestern Division Teams<br>
    - `Pacific Division Record` is the record against Pacific Division Teams<br>
    - `Southeastern Division Record` is the record against Southeastern Division Teams<br>
    - `Southwestern Division Record` is the record against Southwestern Division Teams<br>
    - `Northwestern Division Record`is the record against Northwestern Division Teams<br>
    - `Pre Allstar Record` is a team's record before the Allstar games<br>
    - `Post Allstar Record` is a team's record after Allstar games<br>
    - `3 Point Margin` is a team's record when they win a game with a point difference of 3 or greater <br>
    - `10 Point Margin` is a team's record when they win a game with a point difference of 10 or greater<br>
    - `Oct Record` is a team's record in the month of Oct<br>
    - `Nov Record` is a team's record in the month of Nov<br>
    - `Dec Record` is a team's record in the month of Dec<br>
    - `Jan Record` is a team's record in the month of Jan<br>
    - `Feb Record` is a team's record in the month of Feb<br>
    - `Apr Record` is a team's record in the month of Apr<br>
    - `May Record` is a team's record in the month of May<br>
    - `Jul Record` is a team's record in the month of Jul<br>
    - `Aug Record` is a team's record in the month of Aug<br>

#### Standard 
For `'Standard'`, it will return two Pandas Dataframe, for Eastern Conference and Western Conference respectively but both will have the following columns
```
    ['Season', 'Team ID' , 'Team ABV', 'Team', 'W', 'L', 'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS']
```
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int corresponding to a team<br>
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `W` is the amount of wins a team has<br>
    - `L` is the amount of loses a team has<br>
    - `W/L%` is the percentage of wins divided by loses<br>
    - `GB` is the amount of games behind from first place<br>
    - `PS/G` is the Points per game<br>
    - `PA/G` is the Opponents Points per Game<br>
    - `SRS` is the team rating determined by average point differential and strength of schedule<br>

#### Team vs Team
For `'Team vs Team`', it will return a Pandas Dataframe with the following columns
```
    ['Season', 'Team ID', 'Team ABV', 'Team', 'ABV',....,'ABV' ]
```
<strong>Note:</strong> `ABV` is all the teams' abbreviation in the league for a given season<br> 
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int corresponding to a team<br>
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `ABV,....,ABV` is all the teams for a given season in abbreviation form<br>

## Team Stats Scaper
### `get_roster(team, season)`
<strong>Parameters:</strong><br>
    - `team`   - is a team in the NBA, takes in a team's abbreviation form<br>
    - `season` - NBA season(only from 1980 to current year)<br>
<strong>Returns:</strong><br>
A Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', Number', 'Player', 'Pos', 'Height', 'Weight', 'Birth Date', 'Nationality' , 'Experience', 'College']
```
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int respective to it's column, corresponding to a team<br>
    - `Player ID` is the unique int respective to it's column, corresponding to a player<br> 
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `Number`is the player's jersey number<br>
    - `Player` is the name of the player<br>
    - `Pos` is the player's postion in the basketball court<br>
    - `Height` is the player's height, in feet and inches<br>
    - `Weight` is the player's weight in lbs<br>
    - `Birth Date` is the player's data of birth, in Month Day,Year<br>
    - `Nationality` is the player's country of origin, in abbreviation form<br>
    - `Experience` is the amount years the player's been in the leaue<br>
    - `College` if player went to college, this is the name of the college<br>

### `get_roster_stats(team,season, playoffs, data_format)`
<strong>Parameters:</strong><br>
    - `team`        - is a team in the NBA, takes in a team's abbreviation form<br>
    - `season`      - NBA season(only from 1980 to current year)<br>
    - `playoffs`    - check if the regular season or playoffs<br>
    - `data format` - One of `'Advanced' | 'Per_Game' |'Per_Minute'| Per_Poss | 'Totals'` where default value is `Per_Game`<br>
<strong>Returns:</strong><br>

#### Advanced 
For `'Advanced'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'MP', 'PER', 'TS%', '3PAr', 'FTr', 'ORB%', 'DRB%', 
    'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP']
```
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int respective to it's column, corresponding to a team<br>
    - `Player ID` is the unique int respective to it's column, corresponding to a player<br> 
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `Player` is the name of the player<br>
    - `Age` is the age of the player<br>
    - `G` is the amount of games played<br>
    - `MP`is the amount of minutes played<br>
    - `PER`is the measurment of a player's per-minute production<br>
    - `TS%` is the measurement of shooting efficiency<br>
    - `3PAr` is the percentage of FG Attempts from the 3 Point line<br>
    - `FTr` is the number of FT Attempts per Field Goal Attempts<br>
    - `ORB%` is an estimated percentage of available offensive rebounds a player takes when in game<br>
    - `DRB%` is an estimated percentage of available defensive rebounds a player takes when in game<br>
    - `TRB%` is an estimated percentage of available  rebounds a player takes when in game<br>
    - `AST%` is an estimated percentage of teammate Field Goals a palyer assited while in game<br>
    - `STL%` is an estimate percentage of opponent possessions that end with a steal by player while in game<br>
    - `BLK%` is an estimate of the percentage of opponent Field Goal Attempts blocked by player while in game<br>
    - `TOV%` is an estimate of turnovers commited per 100 plays<br>
    - `USG%` is an estimate of percentage of team plays used by a player while in game<br>
    - `OWS` is an estimate of the number of wins contributed by a player due to his offense<br>
    - `DWS` is an estimate of the number of wins contributed by a player due to his defense<br>
    - `WS` is an estimate of the number of wins contributed by a player<br>
    - `WS/48` is an estimate of the number of wins contributed by a player per 48 minute<br>
    - `OBPM` is a box score estimate of the offensive points per 100 possessions a player contributed<br>
    - `DBPM` is a box score estimate of the defensive points per 100 possessions a player contributed<br>
    - `BPM` is a box score estimate of the points per 100 possessions a player contributed<br>
    - `VORP` is a box score estimate of the points per 100 Team possessions that a play contributed<br>

#### Per_Game
For `'Per_Game'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
#### Per_Minute
For `'Per_Minute'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
#### Per_Poss
For `'Per_Poss'` a Pandas Dataframe with the following columns<br>
```
     ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Ortg', 'Drtg']
```
#### Totals
For `'Totals'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
<strong>Note:</strong><br>
For the following stats `Per_Game`, `Per_Minute`, `Per_Poss` and `Totals` have almost identical columns except `Per_Game` & `Totals` have<br>
```
    ['eFG%]
```
While `Per_Minute` && `Per_Poss` do not have it, Also `Per_Poss` contains<br>
```
    ['Ortg', 'Drtg']
```

<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int respective to it's column, corresponding to a team<br>
    - `Player ID` is the unique int respective to it's column, corresponding to a player<br> 
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `Player` is the name of the player <br>
    - `Age` is the age of the player<br>
    - `G` is the amount of games the player played<br>
    - `GS` is the amount of games the player started<br>
    - `MP` is the amount of minutes the player played<br>
    - `FG` is the amount Field Goals made<br>
    - `FGA` is the amount of Field Goals Attempted<br>
    - `FG%` is the percentage of Field Goals Made / Field Goals Attempted<br>
    - `3P` is the amount of 3 Point Shots Made<br>
    - `3PA` is the amount of 3 Point Shots Attempted<br>
    - `3P%` is the percentage of 3 Points Made / 3 Point Shot Attempted<br>
    - `2P` is the amount of 2 Point Made<br>
    - `2PA` is the amount of 2 Points Attempted<br>
    - `2P%` is the percentage of 2 Point Made / 2 Points Attemped<br>
    - `eFG%` is the percentage calculated by (FG + 0.5 * 3P) / FGA.<br>
    - `FT` is the amount of Free Throws Made<br>
    - `FTA` is the amount of Free Throws Attempted<br>
    - `FT%` is the percentage of Free Throws Made / Free Throws Attempted<br>
    - `ORB` is the amount of Offensive Rebound<br>
    - `DRB` is the amount of Defensive Rebound<br>
    - `TRB` is the amount of Rebound<br>
    - `AST` is the amount of Assist<br>
    - `STL` is the amount of Steals<br>
    - `BLK` is the amount of Blocks<br>
    - `TOV` is the amount of Turn Overs<br>
    - `PF` is the amount of Personal Fouls<br>
    - `PTS` is the amount of Points Scored<br>
    - `Ortg` is the Offensive Rating<br>
    - `Drtg` is the Defensive Rating<br>

### `get_team_stats_main(season, data_format)`
<strong>Parameters:</strong><br>
    - `season`      - NBA season(only from 1980 to current year)<br>
    - `data format` - One of `'Per_Game' |'Per_Minute'| 'Totals'` where default value is `Per_Game`<br>
<strong>Returns:</strong><br>

#### Per Game
For `'Per_Game'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Team ABV', 'Team', 'G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
#### Per Poss
For `'Per_Poss'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Team ABV', 'Team', 'G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
#### Total
For `'Total'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Team ABV', 'Team', 'G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
<strong>Note:</strong><br>
The following stats, `Per_Game`, `Per_Poss`, and `Totals` all have the same columns<br>
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int respective to it's column, corresponding to a team<br>
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `G` is the amount of games the player played<br>
    - `MP` is the amount of minutes the player played<br>
    - `FG` is the amount Field Goals made<br>
    - `FGA` is the amount of Field Goals Attempted<br>
    - `FG%` is the percentage of Field Goals Made / Field Goals Attempted<br>
    - `3P` is the amount of 3 Point Shots Made<br>
    - `3PA` is the amount of 3 Point Shots Attempted<br>
    - `3P%` is the percentage of 3 Points Made / 3 Point Shot Attempted<br>
    - `2P` is the amount of 2 Point Made<br>
    - `2PA` is the amount of 2 Points Attempted<br>
    - `2P%` is the percentage of 2 Point Made / 2 Points Attemped<br>
    - `FT` is the amount of Free Throws Made<br>
    - `FTA` is the amount of Free Throws Attempted<br>
    - `FT%` is the percentage of Free Throws Made / Free Throws Attempted<br>
    - `ORB` is the amount of Offensive Rebound<br>
    - `DRB` is the amount of Defensive Rebound<br>
    - `TRB` is the amount of Rebound<br>
    - `AST` is the amount of Assist<br>
    - `STL` is the amount of Steals<br>
    - `BLK` is the amount of Blocks<br>
    - `TOV` is the amount of Turn Overs<br>
    - `PF` is the amount of Personal Fouls<br>
    - `PTS` is the amount of Points Scored<br>

### `get_opp_stats(season, data_format)`
<strong>Parameters:</strong><br>
    - `season`      - NBA season(only from 1980 to current year)<br>
    - `data format` - One of `'Per_Game' |'Per_Minute'| 'Totals'` where default value is `Per_Game`<br>
<strong>Returns:</strong><br>

#### Per Game
For `'Per_Game'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Team ABV', 'Team', 'G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
#### Per Poss
For `'Per_Poss'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Team ABV', 'Team', 'G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
#### Total
For `'Total'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Team ABV', 'Team', 'G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
<strong>Note:</strong><br>
The following stats, `Per_Game`, `Per_Poss`, and `Totals` all have the same columns<br>
<strong>Also, These are all opponent averages agaist a certain team</strong><br>
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int respective to it's column, corresponding to a team<br>
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `G` is the amount of games the player played<br>
    - `MP` is the amount of minutes the player played<br>
    - `FG` is the amount Field Goals made<br>
    - `FGA` is the amount of Field Goals Attempted<br>
    - `FG%` is the percentage of Field Goals Made / Field Goals Attempted<br>
    - `3P` is the amount of 3 Point Shots Made<br>
    - `3PA` is the amount of 3 Point Shots Attempted<br>
    - `3P%` is the percentage of 3 Points Made / 3 Point Shot Attempted<br>
    - `2P` is the amount of 2 Point Made<br>
    - `2PA` is the amount of 2 Points Attempted<br>
    - `2P%` is the percentage of 2 Point Made / 2 Points Attemped<br>
    - `FT` is the amount of Free Throws Made<br>
    - `FTA` is the amount of Free Throws Attempted<br>
    - `FT%` is the percentage of Free Throws Made / Free Throws Attempted<br>
    - `ORB` is the amount of Offensive Rebound<br>
    - `DRB` is the amount of Defensive Rebound<br>
    - `TRB` is the amount of Rebound<br>
    - `AST` is the amount of Assist<br>
    - `STL` is the amount of Steals<br>
    - `BLK` is the amount of Blocks<br>
    - `TOV` is the amount of Turn Overs<br>
    - `PF` is the amount of Personal Fouls<br>
    - `PTS` is the amount of Points Scored<br>

### `get_team_misc(season)`
<strong>Parameters:</strong><br>
    - `season` - NBA season(only from 1980 to current year)<br>
<strong>Returns:</strong><br>
A Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Team ABV', 'Team', 'Age', 'W', 'L', 'PW', 'PL', 'MOV', 'SOS', 'SRS', 'ORtg', 'DRtg', 'NRtg', 'Pace', 
    'FTr', '3PAr', 'TS%', 'ORB%', 'DRB%', 'Arena', 'Attend.', 'Attend./G']
```
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int respective to it's column, corresponding to a team<br>
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `Age` is the average age of the player<br>
    - `W` is the amount of wins for a team<br>
    - `L` is the amount of loses for a team<br>
    - `PW` is the Pythagorean wins or expected wins based on points scored and allowed<br>
    - `PL` is the Pythagorean loses or expected wins based on points scored and allowed<br>
    - `MOV` is the margin of victory<br>
    - `SOS` is the Strength of Schedule, a rating of how hard a schedule is<br>
    - `SRS` is the Simple Rating System, a team rating that takes into account average point differential and strength of schedule<br>
    - `ORtg` an estiamte of points scored by a team per 100 possessions<br>
    - `DRtg` an estiamte of points allowed per 100 possessions<br>
    - `NRtg` an estimate of points differential per 100 possessions<br>
    - `Pace` an estimate of possessions per 48 minutes<br>
    - `FTr` is the number of FT Attempts per FG Attempt<br>
    - `3PAr` Percentage of FG Attempts from 3-Point Range<br>
    - `TS%` is the measurement of shooting efficiency<br>
    - `ORB%` is an estimated percentage of available offensive rebounds a player takes when in game<br>
    - `DRB%` is an estimated percentage of available defensive rebounds a player takes when in game<br>
    - `Arena` is the Area name for the team<br>
    - `Attend.` is the amount of people who attend the Area the whole season<br>
    - `Attend./G` is the average amount of people who attend a game<br>

### `get_team_advanced(team, season)`
<strong>Parameters:</strong><br>
    - `team`   - A team in the NBA for that season, abbreviation<br>
    - `season` - NBA season(only from 1980 to current year)<br>
<strong>Returns:</strong><br>
A pandas dataframe containing the following columns<br>
```
    ['Season', 'Team ID', 'Team ABV', 'Team', 'W', 'L', 'W/L%', 'Finish', 'SRS', 'Pace', 'Rel Pace', 'ORtg', 'Rel ORtg', 'DRtg', 'Rel DRtg', 'Playoffs', 'Coaches', 'Top WS']
```
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int respective to it's column, corresponding to a team<br>
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `W` is the amount of wins for a team<br>
    - `L` is the amount of loses for a team<br>
    - `W/L%` is the percentage of wins divided by loses<br>
    - `Finish` is the Regular Season finish within the team's respective Division <br>
    - `SRS` is the team rating determined by average point differential and strength of schedule<br>
    - `Pace` an estimate of possessions per 48 minutes<br>
    - `Rel Pace` an estimate of a Team's possessions per 48 minutes relative to the league<br>
    - `ORtg` an estimate of <br>
    - `Rel Ortg` is the Team's offensive rating relative to the league<br>
    - `DRtg` an estiamte of points allowed per 100 possessions<br>
    - `Rel DRtg` is the Team's defensive rating relative to the league<br>
    - `Playoffs` is where the team was eliminated if they made the playoffs<br>
    - `Coaches` is the coache of the team<br>
    - `Top WS` is the player <br>

### `remove_char(string, postion)`
<strong>Parameters:</strong><br>
    - `string`   - a string that needs to have a char removes<br>
    - `postion`  - a int that represents the index of the string<br>
<strong>Returns:</strong><br>
A sub-string of the orginal `string` that has a char removed at whatever `postion` is<br>

## Create Player Name
### `player_names_csv()`
<strong>Parameters:</strong><br>
    - `None`<br>
<strong>Returns:</strong><br>
None, creates a csv containing all Players active from 1980 - current year

## Player Stats Scraper 
### `check_abv(string)`
<strong>Parameters:</strong><br>
    - `string`   - a string that represent a team's abbreviation<br>
<strong>Returns:</strong><br>
Returns a `new_string`, which is a string value from `TEAM_TO_ABBRIVATION[string]`

### `check_team_id(name)`
<strong>Parameters:</strong><br>
    - `string`   - a string that represent a team's name<br>
<strong>Returns:</strong><br>
Returns a `new_num`, which is a int value from `TEAM_ID[name]`

### `get_player_name(letter)`
<strong>Parameters:</strong><br>
    - `string`   - Takes in a letter, iterated to get all players name in the English Alphabet<br>
<strong>Returns:</strong><br>
Creates a Pandas Dataframe containing the following columns
```
    ['Player', 'Birth Date']
```
<strong>Where:</strong><br>
    - `Player` is the name of the player<br>
    - `Birth Date` is the date of birth of the player<br>

### `create_player_suffix(name)`
<strong>Parameters:</strong><br>
    - `name`   - Takes in a player's name, first and last<br>
<strong>Returns:</strong><br>
Returns a string suffix of the player's first name and last<br> 
<strong>Example:</strong> Nikola Jokic = jokicni<br>

### `get_player_suffix(name, birth_date)`
<strong>Parameters:</strong><br>
    - `name`      - Takes in the player's name, first and last<br>
    - `birth_date - Takes in the player's date of birth<br>
<strong>Returns:</strong><br>
Returns a string suffix for the url of the player's page by calling `create_player_suffix` and adding 01. If not valid, iterate until 05<br>
<strong>Example:</strong> Nikola Jokic = jokicni01<br>

### `get_player_stats(name, birth_date,format, playoffs)`
<strong>Parameters:</strong><br>
    - `team`        - is a team in the NBA, takes in a team's abbreviation form<br>
    - `season`      - NBA season(only from 1980 to current year)<br>
    - `playoffs`    - check if the regular season or playoffs<br>
    - `data format` - One of `'Advanced' | 'Per_Game' |'Per_Minute'| Per_Poss | 'Totals'` where default value is `Per_Game`<br>
<strong>Returns:</strong><br>

#### Advanced 
For `'Advanced'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'MP', 'PER', 'TS%', '3PAr', 'FTr', 'ORB%', 'DRB%', 
    'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP']
```
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int respective to it's column, corresponding to a team<br>
    - `Player ID` is the unique int respective to it's column, corresponding to a player<br> 
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `Player` is the name of the player<br>
    - `Age` is the age of the player<br>
    - `G` is the amount of games played<br>
    - `MP`is the amount of minutes played<br>
    - `PER`is the measurment of a player's per-minute production<br>
    - `TS%` is the measurement of shooting efficiency<br>
    - `3PAr` is the percentage of FG Attempts from the 3 Point line<br>
    - `FTr` is the number of FT Attempts per Field Goal Attempts<br>
    - `ORB%` is an estimated percentage of available offensive rebounds a player takes when in game<br>
    - `DRB%` is an estimated percentage of available defensive rebounds a player takes when in game<br>
    - `TRB%` is an estimated percentage of available  rebounds a player takes when in game<br>
    - `AST%` is an estimated percentage of teammate Field Goals a palyer assited while in game<br>
    - `STL%` is an estimate percentage of opponent possessions that end with a steal by player while in game<br>
    - `BLK%` is an estimate of the percentage of opponent Field Goal Attempts blocked by player while in game<br>
    - `TOV%` is an estimate of turnovers commited per 100 plays<br>
    - `USG%` is an estimate of percentage of team plays used by a player while in game<br>
    - `OWS` is an estimate of the number of wins contributed by a player due to his offense<br>
    - `DWS` is an estimate of the number of wins contributed by a player due to his defense<br>
    - `WS` is an estimate of the number of wins contributed by a player<br>
    - `WS/48` is an estimate of the number of wins contributed by a player per 48 minute<br>
    - `OBPM` is a box score estimate of the offensive points per 100 possessions a player contributed<br>
    - `DBPM` is a box score estimate of the defensive points per 100 possessions a player contributed<br>
    - `BPM` is a box score estimate of the points per 100 possessions a player contributed<br>
    - `VORP` is a box score estimate of the points per 100 Team possessions that a play contributed<br>

#### Per_Game
For `'Per_Game'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
#### Per_Minute
For `'Per_Minute'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
#### Per_Poss
For `'Per_Poss'` a Pandas Dataframe with the following columns<br>
```
     ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Ortg', 'Drtg']
```
#### Totals
For `'Totals'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
<strong>Note:</strong><br>
For the following stats `Per_Game`, `Per_Minute`, `Per_Poss` and `Totals` have almost identical columns except `Per_Game` & `Totals` have<br>
```
    ['eFG%]
```
While `Per_Minute` && `Per_Poss` do not have it, Also `Per_Poss` contains<br>
```
    ['Ortg', 'Drtg']
```
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int respective to it's column, corresponding to a team<br>
    - `Player ID` is the unique int respective to it's column, corresponding to a player<br> 
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `Player` is the name of the player <br>
    - `Age` is the age of the player<br>
    - `G` is the amount of games the player played<br>
    - `GS` is the amount of games the player started<br>
    - `MP` is the amount of minutes the player played<br>
    - `FG` is the amount Field Goals made<br>
    - `FGA` is the amount of Field Goals Attempted<br>
    - `FG%` is the percentage of Field Goals Made / Field Goals Attempted<br>
    - `3P` is the amount of 3 Point Shots Made<br>
    - `3PA` is the amount of 3 Point Shots Attempted<br>
    - `3P%` is the percentage of 3 Points Made / 3 Point Shot Attempted<br>
    - `2P` is the amount of 2 Point Made<br>
    - `2PA` is the amount of 2 Points Attempted<br>
    - `2P%` is the percentage of 2 Point Made / 2 Points Attemped<br>
    - `eFG%` is the percentage calculated by (FG + 0.5 * 3P) / FGA.<br>
    - `FT` is the amount of Free Throws Made<br>
    - `FTA` is the amount of Free Throws Attempted<br>
    - `FT%` is the percentage of Free Throws Made / Free Throws Attempted<br>
    - `ORB` is the amount of Offensive Rebound<br>
    - `DRB` is the amount of Defensive Rebound<br>
    - `TRB` is the amount of Rebound<br>
    - `AST` is the amount of Assist<br>
    - `STL` is the amount of Steals<br>
    - `BLK` is the amount of Blocks<br>
    - `TOV` is the amount of Turn Overs<br>
    - `PF` is the amount of Personal Fouls<br>
    - `PTS` is the amount of Points Scored<br>
    - `Ortg` is the Offensive Rating<br>
    - `Drtg` is the Defensive Rating<br>

### `lookup(name, birth_date)`
<strong>Parameters:</strong><br>
    - `name`      - Takes in the player's name, first and last<br>
    - `birth_date - Takes in the player's date of birth<br>
<strong>Returns:</strong><br>
Returns a tuple of `(name, birth_date)` if it exists in `player_names.csv`<br>

### `get_career_stats(name, birth_date, format, playoffs)`
<strong>Parameters:</strong><br>
    - `team`        - is a team in the NBA, takes in a team's abbreviation form<br>
    - `season`      - NBA season(only from 1980 to current year)<br>
    - `playoffs`    - check if the regular season or playoffs<br>
    - `data format` - One of `'Advanced' | 'Per_Game' |'Per_Minute'| Per_Poss | 'Totals'` where default value is `Per_Game`<br>
<strong>Returns:</strong><br>

<strong>Note:</strong><br>
Career Averages are the average of each column, the only one that is different is `Totals`, where it is the sum of every column<br>
For `Advanced`, All winshares are sumed up instead of averaged<br> 

#### Advanced 
For `'Advanced'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'MP', 'PER', 'TS%', '3PAr', 'FTr', 'ORB%', 'DRB%', 
    'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP']
```
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int respective to it's column, corresponding to a team<br>
    - `Player ID` is the unique int respective to it's column, corresponding to a player<br> 
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `Player` is the name of the player<br>
    - `Age` is the age of the player<br>
    - `G` is the amount of games played<br>
    - `MP`is the amount of minutes played<br>
    - `PER`is the measurment of a player's per-minute production<br>
    - `TS%` is the measurement of shooting efficiency<br>
    - `3PAr` is the percentage of FG Attempts from the 3 Point line<br>
    - `FTr` is the number of FT Attempts per Field Goal Attempts<br>
    - `ORB%` is an estimated percentage of available offensive rebounds a player takes when in game<br>
    - `DRB%` is an estimated percentage of available defensive rebounds a player takes when in game<br>
    - `TRB%` is an estimated percentage of available  rebounds a player takes when in game<br>
    - `AST%` is an estimated percentage of teammate Field Goals a palyer assited while in game<br>
    - `STL%` is an estimate percentage of opponent possessions that end with a steal by player while in game<br>
    - `BLK%` is an estimate of the percentage of opponent Field Goal Attempts blocked by player while in game<br>
    - `TOV%` is an estimate of turnovers commited per 100 plays<br>
    - `USG%` is an estimate of percentage of team plays used by a player while in game<br>
    - `OWS` is an estimate of the number of wins contributed by a player due to his offense<br>
    - `DWS` is an estimate of the number of wins contributed by a player due to his defense<br>
    - `WS` is an estimate of the number of wins contributed by a player<br>
    - `WS/48` is an estimate of the number of wins contributed by a player per 48 minute<br>
    - `OBPM` is a box score estimate of the offensive points per 100 possessions a player contributed<br>
    - `DBPM` is a box score estimate of the defensive points per 100 possessions a player contributed<br>
    - `BPM` is a box score estimate of the points per 100 possessions a player contributed<br>
    - `VORP` is a box score estimate of the points per 100 Team possessions that a play contributed<br>

#### Per_Game
For `'Per_Game'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
#### Per_Minute
For `'Per_Minute'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
#### Per_Poss
For `'Per_Poss'` a Pandas Dataframe with the following columns<br>
```
     ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Ortg', 'Drtg']
```
#### Totals
For `'Totals'` a Pandas Dataframe with the following columns<br>
```
    ['Season', 'Team ID', 'Player ID', 'Team ABV', 'Team', 'Player', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
    '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```
<strong>Note:</strong><br>
For the following stats `Per_Game`, `Per_Minute`, `Per_Poss` and `Totals` have almost identical columns except `Per_Game` & `Totals` have<br>
```
    ['eFG%]
```
While `Per_Minute` && `Per_Poss` do not have it, Also `Per_Poss` contains<br>
```
    ['Ortg', 'Drtg']
```
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int respective to it's column, corresponding to a team<br>
    - `Player ID` is the unique int respective to it's column, corresponding to a player<br> 
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `Player` is the name of the player <br>
    - `Age` is the age of the player<br>
    - `G` is the amount of games the player played<br>
    - `GS` is the amount of games the player started<br>
    - `MP` is the amount of minutes the player played<br>
    - `FG` is the amount Field Goals made<br>
    - `FGA` is the amount of Field Goals Attempted<br>
    - `FG%` is the percentage of Field Goals Made / Field Goals Attempted<br>
    - `3P` is the amount of 3 Point Shots Made<br>
    - `3PA` is the amount of 3 Point Shots Attempted<br>
    - `3P%` is the percentage of 3 Points Made / 3 Point Shot Attempted<br>
    - `2P` is the amount of 2 Point Made<br>
    - `2PA` is the amount of 2 Points Attempted<br>
    - `2P%` is the percentage of 2 Point Made / 2 Points Attemped<br>
    - `eFG%` is the percentage calculated by (FG + 0.5 * 3P) / FGA.<br>
    - `FT` is the amount of Free Throws Made<br>
    - `FTA` is the amount of Free Throws Attempted<br>
    - `FT%` is the percentage of Free Throws Made / Free Throws Attempted<br>
    - `ORB` is the amount of Offensive Rebound<br>
    - `DRB` is the amount of Defensive Rebound<br>
    - `TRB` is the amount of Rebound<br>
    - `AST` is the amount of Assist<br>
    - `STL` is the amount of Steals<br>
    - `BLK` is the amount of Blocks<br>
    - `TOV` is the amount of Turn Overs<br>
    - `PF` is the amount of Personal Fouls<br>
    - `PTS` is the amount of Points Scored<br>
    - `Ortg` is the Offensive Rating<br>
    - `Drtg` is the Defensive Rating<br>

## Team Constants 
### `TEAM_TO_ABBRIVATION`
Is a dictonary that takes in a team name as a key and converts it into an abbreviation<br>
<strong>Example</strong> `ATLANTA HAWKS` is converted into `ATL`<br>

### `ABV_TO_TEAM` 
Is a dictonary that takes in an abbreviation as a key and converts it into a team name 
<strong>Example:</strong> `ATL` is converted into `ATLANTA HAWKS`<br>

### `TEAM_ID`
Is a dictonary that takes in an abbreviation as a key and converts it into a int corresponding to a unique nba franchise<br>
<strong>Example:</strong> `CHO` is converted into `4`<br>
<strong>Example:</strong> `CHA` is converted into `4`<br>
They contain the same number as they are the same franchise but changed names over the years<br>

### `TEAM_DICT` 
Is a dictonary that takes in old franchise abbreviation and converts it to its mondern day counter part<br>
<strong>Example:</strong> `SEA` is converted into `OKC`<br>

### `RIGHT_NAME_DICT` 
Is a dictonary that takes in a string tuple `(player_name, birth_date)` that converts wrong names into the proper name<br>
<strong>Example:</strong> `(Tim Hardaway, March 16, 1992)` is converted into `Tim Hardaway Jr.`<br>

### `get_player_id()`
<strong>Parameters:</strong><br>
    - `None`<br>
<strong>Returns:</strong><br>
None, it is a helper function for `PLAYER_ID`, as it inserts all key and values into the dictionary<br>

### `PLAYER_ID`
Is a dictonary that takes in a NBA players `name` as a key and converts into a unique corresponding to the name
<strong>Example:</strong> 'Tim Hardaway` is converted to `1181`

## Utils
### `strip_accents(text)`
<strong>Parameters:</strong><br>
    - `text` - Takes in a string, for the player's name<br>

<strong>Returns:</strong><br>
A `new_string` if the text contains special char or accent<br>
This is used for the `get_roster`, as they have proper UTF-8 notation <br>

### `translate(name)`
<strong>Parameters:</strong><br>
    - `name` - Takes in a string, for the player's name<br>
<strong>Returns:</strong><br>
Creates a `new_string`, if `name` contains special or accented chars, remove it and replace it with english counter part<br>
This is used for every other function concerning player name, as the UTF-8 when scraped, is incorect<br>