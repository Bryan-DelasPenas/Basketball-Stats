# Run Scraper API
## Get Season Stats
### csv_team_name(year)
<strong>Parameters:</strong><br>
    - `year` - NBA season(only from 1980 to current year)<br>
</strong>Returns:</strong><br>
None, creates a file path `Team_Names` in `Season`, and stores csv file of team names for a given `year` in the sub directory<br>

### csv_standings(year, format)
<strong>Parameters:</strong><br>
    - `year`  - NBA season(only from 1980 to current year)<br>
    -`format` - One of `'Expanded Standing' | 'Standard' |'Team_Vs_Team'`<br>
</strong>Returns:</strong><br>
None, creates a file path `/Standing` in `Season` and a sub directory of `'Expanded Standing' | 'Standard' |'Team_Vs_Team'`,<br>
and stores csv based on the `format` for a given `year` in the subdirectory<br>

### get_season_csv()
<strong>Parameters:</strong><br>
    - `None`<br>
</strong>Returns:</strong><br>
None, creates `/Season` in `/Output` directory and calls the two functions above<br>

## Get Team Stats
### create_team_stats_folder_two(location_parent, location)
<strong>Parameters:</strong><br>
    - `location_parent` - is the file path that is the parent directory of location<br>
    - `location`        - is the file path that you want to create<br>
</strong>Returns:</strong><br>
None, creates a new sub directory which `location_parent` is the parent directory<br>

### create_team_stats_folder_three(location_grand,location_parent, location)
<strong>Parameters:</strong><br>
    - `location_grand`  - is the file path that is the parent directory of location_parent<br>
    - `location_parent` - is the file path that is the parent directory of location<br>
    - `location`        - is the file path that you want to create<br>
</strong>Returns:</strong><br>
None, creates a new sub directory which `location_parent` is the parent directory and `location_grand` is the grandfather directory<br>

### csv_team_roster(year)
<strong>Parameters:</strong><br>
    - `year` - NBA season(only from 1980 to current year)<br>
</strong>Returns:</strong><br>
None, creates a file path `Roster_Stats` in `Roster`. Then creates mutiple directories based on year,<br> 
and creates a csv containing team's roster inside of the year directory<br> 

### csv_roster_stats(year, playoffs ,format) 
<strong>Parameters:</strong><br>
    - `year`       - a string that represents NBA season(only from 1980 to current year)<br>
    - 'birth_date  - a string represents date of birth<br>
    - `format`     - a string represents what format, it could be one of the following `'Advanced' | 'Per_Game' |'Per_Minute'| Per_Poss | 'Totals'`<br>

</strong>Returns:</strong><br>
None, creates a sub directory based on playoffs, called `Regular_Stat` or `Playoff_Stat` and called either the two functions below<br>

### csv_roster_playoff_stats(year, format, season_df, file_path)
<strong>Parameters:</strong><br>
    - `year`       - a string that represents NBA season(only from 1980 to current year)<br>
    - `format`     - a string represents what format, it could be one of the following `'Advanced' | 'Per_Game' |'Per_Minute'| Per_Poss | 'Totals'`<br>
    - `season_df`  - a dataframe of containing Teams for a given season<br>
    - `file_path   - a string represents file path for roster playoff stats<br>
</strong>Returns:</strong><br>
None, inserts a csv of playoff stats based on `format` inside of the corresponding `year` directory<br> 

### csv_roster_regular_stats(year, format, season_df, file_path) 
<strong>Parameters:</strong><br>
    - `year`       - a string that represents NBA season(only from 1980 to current year)<br>
    - `format`     - a string represents what format, it could be one of the following `'Advanced' | 'Per_Game' |'Per_Minute'| Per_Poss | 'Totals'`<br>
    - `season_df`  - a dataframe of containing Teams for a given season<br>
    - `file_path   - a string represents file path for roster regular stats<br>
</strong>Returns:</strong><br>
None, inserts a csv of regular stats based on `format` inside of the corresponding `year` directory<br> 

### csv_team_stats_other(year, format)
<strong>Parameters:</strong><br>
    - `year`       - a string that represents NBA season(only from 1980 to current year)<br>
    - `format`     - a string represents what format, aka `'Team_Advanced'`<br>
</strong>Returns:</strong><br>
Creates a sub directory called `Team_Advanced` inside of `Team_Averages`. Then creates a sub directory `year` that contain advanced stats about the team<br>

### csv_team_stats_main(year, format)
<strong>Parameters:</strong><br>
    - `year`       - a string that represents NBA season(only from 1980 to current year)<br>
    - `format`     - a string represents what format, it could be one of the following `'Per_Game' | 'Per_Poss' | 'Team_Misc' |'Totals'`<br>
</strong>Returns:</strong><br>
Creates a sub directory named whatever `format` is inside of `Team_Averages` that contain `format` stats about the team

### csv_opponent_stats(year, format)
<strong>Parameters:</strong><br>
    - `year`       - a string that represents NBA season(only from 1980 to current year)<br>
    - `format`     - a string represents what format, it could be one of the following `'Per_Game' | 'Per_Poss' | 'Team_Misc' |'Totals'`<br>
</strong>Returns:</strong><br>
Creates a sub directory named whatever `format` is inside of `Team_Averages` that contain oppenents `format` stats against that team

### get_team_csv()
<strong>Parameters:</strong><br>
    `None`<br>
</strong>Returns:</strong><br>
Calls all functions above<br>

## Get Player Stats
### csv_player_stats(name, birth_date, format, playoff, player_path) 
<strong>Parameters:</strong><br>
    - `name`       - a string represents name of the player<br>
    - 'birth_date` - a string represents date of birth<br>
    - `format`     - a string represents what format, it could be one of the following `'Advanced' | 'Per_Game' |'Per_Minute'| Per_Poss | 'Totals'`<br>
    - `playoff`    - a boolean that represents if getting playoff stats<br>
    - `player_path - a string represents file path for a player<br>
</strong>Returns:</strong><br>
None, creates sub directory in `Player` that is named after `format`, then creates either `Regular_Stats` or `Playoffs_Stats`.<br>
In the sub directory creates a csv of players stats for every year they played.<br>

### csv_career_stats(name, birth_date, format, playoff, player_path)
<strong>Parameters:</strong><br>
    - `name`       - a string represents name of the player<br>
    - 'birth_date  - a string represents date of birth<br>
    - `format`     - a string represents what format, it could be one of the following `'Advanced' | 'Per_Game' |'Per_Minute'| Per_Poss | 'Totals'`<bn>
    - `playoff`    - a boolean that represents if getting playoff stats<br>
    - `player_path - a string represents file path for a player<br>
</strong>Returns:</strong><br>
None, creates sub directory in `Player` that is named after `format`, then creates either `Career_Regular_Stats` or `Career_Playoffs_Stats`.<br>
In the sub directory creates a csv of player's career.<br>

### get_player_csv()
<strong>Parameters:</strong><br>
    - `None`<br>
</strong>Returns:</strong><br>
None, creates `/Player` in `/Output` and inside of `/Player` creates sub directories based on player's name. Also calls the functions above to get the csv<br>
