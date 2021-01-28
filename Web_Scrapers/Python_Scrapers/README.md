# Python Scrapers API

## General Basketball Definitions 

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
    'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%','USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP']
```
<strong>Where:</strong><br>
    - `Season` is the NBA season<br>
    - `Team ID` is the unique int respective to it's column, corresponding to a team<br>
    - `Player ID` is the unique int respective to it's column, corresponding to a player<br> 
    - `Team ABV` is the team abbreviation<br>
    - `Team` is the name of the Team<br>
    - `Player` is the name of the player<br>

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

### `get_team_stats(season, data_format)`

### `get_opp_stats(season, data_format)`

### `get_team_misc(season)`

### `get_team_advanced(team, season)`

### `remove_char(string, postion)`

## Player Stats Scraper 
### `check_abv(string)`

### `check_team_id(name)`

### `get_player_name(letter)`

### `create_player_suffix(name)`

### `get_player_suffix(name, birth_date)`

### `get_player_stats(name, birth_date,format, playoffs)`

### `lookup(name, birth_date)`

### `get_career_stats(name, birth_date, format, playoffs)`

## Create Player Name
### `players_names_csv()`

## Team Constants 
### `TEAM_TO_ABBRIVATION`

### `ABV_TO_TEAM` 

### `TEAM_ID`

### `TEAM_DICT` 

### `RIGHT_NAME_DICT` 

### `get_player_id()`

### `PLAYER_ID`

## Utils
### `strip_accents(text)`

### `translate(name)`