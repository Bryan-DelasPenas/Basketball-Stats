# Python Scrapers API

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
<strong>Parameters:<strong><br>
    `season`      - NBA season(only from 1980 to current year)<br>
    `data_format` - One of `'Expanded Standing' | 'Standard' |'Team_Vs_Team'` where default value is `Standard`<br>
<strong>Returns:<strong><br>

#### For Expanded Standings
For `'Expanded Standings'` and `'season'` of 1980 and 1981, it will return a Pandas Dataframe with the following columns
```
    ['Season', 'Team ID', 'Team ABV', 'Team', 'Overall', 'Home Record', 'Road Record', 'Eastern Conference Record', 'Western Conference Record',
    'Atlantic Division Record', 'Central Division Record', 'Midwesterm Division Record', 'Pacific Division Record', 'Pre Allstar Record', 'Post Allstar Record',
    '3 Point Margin', '10 Point Margin', 'Oct Record', 'Nov Record', 'Dec Record', 'Jan Record', 'Feb Record', 'Mar Record']
```

For `'Expanded Standings'` and `'season'` between 1988 and 1997, it will return a Pandas Dataframe with the following columns 
```
    ['Season', 'Team ID, 'Team ABV' 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 'MIDWESTERM DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD','3 POINT MARGIN', '10 POINT MARGIN', 
    'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']
```

For `'Expanded Standings'` and `'season'` of 1999, it will return a Pandas Dataframe with the following columns 
```
    [''Season', 'Team ID, 'Team ABV', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 'MIDWESTERM DIVISION RECORD', 'PACIFIC DIVISION RECORD', '3 POINT MARGIN', '10 POINT MARGIN', 'FEB RECORD', 'MAR RECORD', 'APR RECORD', 
    'MAY RECORD']
```

For `'Expanded Standings'` and `'season'` of 2000, it will return a Pandas Dataframe with the following columns 
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 'MIDWESTERM DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD','3 POINT MARGIN', '10 POINT MARGIN', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']
```

For `'Expanded Standings'` and `'season'` of 2005 or 2006, it will return a Pandas Dataframe with the following columns 
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 'SOUTHEASTERN DIVISION RECORD', 'NORTHWESTERN DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'SOUTHWESTERN DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD','3 POINT MARGIN', '10 POINT MARGIN', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']
```

For `'Expanded Standings'` and `'season'` of 2012, it will return a Pandas Dataframe with the following columns 
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 'SOUTHEASTERN DIVISION RECORD', 'NORTHWESTERN DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'SOUTHWESTERN DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD','3 POINT MARGIN', '10 POINT MARGIN', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']
```

For `'Expanded Standings'` and `'season'` of 2007 between 2019 excluding 2012, it will return a Pandas Dataframe with the following columns
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 'SOUTHEASTERN DIVISION RECORD', 'NORTHWESTERN DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'SOUTHWESTERN DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD','3 POINT MARGIN', '10 POINT MARGIN', 'OCT RECORD', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']
```

For `'Expanded Standings'` and `'season'` of 2020, it will return a Pandas Dataframe with the following columns
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 'SOUTHEASTERN DIVISION RECORD', 'NORTHWESTERN DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'SOUTHWESTERN DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD', '3 POINT MARGIN', '10 POINT MARGIN', 'OCT RECORD', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'JUL RECORD', 
    'AUG RECORD']
```

For `'Expanded Standings'` and `'season'` of 2021, it will return a Pandas Dataframe with the following columns
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 'SOUTHEASTERN DIVISION RECORD', 'NORTHWESTERN DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'SOUTHWESTERN DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD', '3 POINT MARGIN', '10 POINT MARGIN',  'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD']
```

For `'Expanded Standings'` and `'season'` it not any above, it will return a Pandas Dataframe with the following columns
```
    ['Season', 'Team ID, 'Team ABV', 'Team', 'OVERALL', 'HOME RECORD', 'ROAD RECORD', 'EASTERN CONFERENCE RECORD', 'WESTERN CONFERENCE RECORD', 'ATLANTIC DIVISION RECORD','CENTRAL DIVISION RECORD', 'MIDWESTERM DIVISION RECORD', 'PACIFIC DIVISION RECORD', 'PRE ALLSTAR RECORD', 'POST ALLSTAR RECORD','3 POINT MARGIN', '10 POINT MARGIN', 'OCT RECORD', 'NOV RECORD', 'DEC RECORD', 'JAN RECORD', 'FEB RECORD', 'MAR RECORD', 'APR RECORD']
```

#### Standard 
For `'Standard'`, it will return two Pandas Dataframe, for Eastern Conference and Western Conference respectively but both will have the following columns
```
    ['Season', 'Team ID' , 'Team ABV', 'Team', 'W', 'L', 'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS']
```
#### Team vs Team

### `get_roster(team, season)`

### `get_roster_stats(team,season, playoffs = False, data_format)`

### `get_team_stats(season, data_format)`

### `get_opp_stats(season, data_format`

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