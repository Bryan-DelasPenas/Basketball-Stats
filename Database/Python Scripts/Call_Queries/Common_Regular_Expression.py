import re

'''
Regex for ints
'''
'''
Regex for season_id parameter
'''
def season_id_regex(season_id):
    # Convert season_id to a string 
    # Check if the parameter season_id is between 1980 - 2020
    season_id_string = str(season_id)
    if(not re.match("(19[89][0-9]|20[0-1][0-9]|2020)", season_id_string)):
        print("Please enter a valid int from 1980 - 2020")
        return None

'''
Regex for team_id parameter
'''
def team_id_regex(team_id):
    # Convert team_id to a string 
    # Check if the parameter team_id is between 1 - 31
    team_id_string = str(team_id)
    if(not re.match("^([1-9]|[12][0-9]|3[01])$", team_id_string)):
        print("Please enter a valid int from 1 - 31")
        return None 

'''
Regex for player_id parameter
'''
def player_id_regex(player_id):
    # Convert player_id to a string
    # Check if the parameter team_id is between 1 - 3281
    player_id_string = str(player_id)
    if(not re.match("^([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-3][0-1][0-9][0-9]|32[0-7][0-9]|328[0-1])$", player_id_string)):
        print("Please enter a valid int from 1 - 3281")
        return None

'''
Regex for amount of games parameter
'''
def games_amount_regex(games_amount):
    # Convert games_amount_regex to a string
    # Check if the parameter games_amount is between 0 - 82
    games_amount_string = str(games_amount)
    if(not re.match("[1-7][0-9]|8[0-2]", games_amount_string)):
        print("Please enter a valid number between 0 - 82")
        return None

'''
Regex for strings
'''
'''
Regex for team_name parameter
'''
def team_name_regex(team_name):
    # Convert team_name into a valid string in Python
    # Check if the parameter team is valid, no numbers and special chars
    team_name_string = str(team_name)
    if(not re.match("^[A-Za-z]+((\s)?([A-Za-z])+)*$", team_name_string)):
        print("Please enter a valid name with only letters and space")
        return None

'''
Regrex for team_abv parameter
'''
def team_abv_regex(abv):
    # Convert abv into a valid string in Python
    # Check if the parameter abv is valid, only 3 captial letters
    abv_string = str(abv)
    if(not re.match("^[A-Z]{3}$", abv_string)):
        print("Please enter only 3 captial letters")
        return None

'''
Regrex for player_name parameter
'''
def player_name_regrex(player_name):
    # Convert player_name into a valid string in Python
    # Check if the parameter player_name is valid, with spaces and special chars
    player_name_string = str(player_name)
    if(not re.match("^[A-Za-z]+((\s)?((\'|\-|\.)?([A-Za-z])+))*$", player_name_string)):
        print("Please enter a valid player name that may contain special chars")
        return None

def main():
    games_amount_regex(-1)
main()