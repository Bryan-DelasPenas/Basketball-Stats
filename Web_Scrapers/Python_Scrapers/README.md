# Python Scrapers API

## Season Stats Scraper
### `get_team_name(season)` 

### `get_standings(season, data_format)`

## Team Stats Scraper
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
### strip_accents(text)

### translate(name)