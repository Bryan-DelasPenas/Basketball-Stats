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
    if(not re.match(r'\b(19[89][0-9]|20[0-1][0-9]|2020)\b', season_id_string)):
        print("Please enter a valid int from 1980 - 2020")
        return True

'''
Regex for team_id parameter
'''
def team_id_regex(team_id):
    # Convert team_id to a string 
    # Check if the parameter team_id is between 1 - 31
    team_id_string = str(team_id)
    if(not re.match(r'\b^([1-9]|[12][0-9]|3[01])$\b', team_id_string)):
        print("Please enter a valid int from 1 - 31")
        return True 

'''
Regex for player_id parameter
'''
def player_id_regex(player_id):
    # Convert player_id to a string
    # Check if the parameter team_id is between 1 - 3281
    player_id_string = str(player_id)
    if(not re.match(r'\b^([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-3][0-1][0-9][0-9]|32[0-7][0-9]|328[0-1])$\b', player_id_string)):
        print("Please enter a valid int from 1 - 3281")
        return True

'''
Regex for amount of games parameter
'''
def games_amount_regex(games_amount):
    # Convert games_amount_regex to a string
    # Check if the parameter games_amount is between 0 - 82
    # Return True if fails check, returns False if passes
    games_amount_string = str(games_amount)
    if(not re.match(r'\b[1-7][0-9]|8[0-2]\b', games_amount_string)):
        print("Please enter a valid number between 0 - 82")
        return True

'''
Regex for any binary parameter
'''
def binary_regex(binary_value):
    # Converts binary_values to a string
    # Check if the parameter binary_value is 0 or 1
    # Return True if fails check, returns False if passes
    binary_value_string = str(binary_value)
    if(not re.match("^[01]$", binary_value_string)):
        print("Please enter a 0 or 1")
        return True
    
'''
Regex for float
'''
'''
Regex for any percentage 0.00% - 0.99%
'''
def percentage_regex(percentage):
    # Convert percentage to a string
    # Check if the parameter percentage is between 0.00 - 0.99
    percentage_string = str(percentage)
    if(not re.match(r'\b^(?:0*(?:\.\d+)?|1(\.0*)?)$\b', percentage_string)):
        print("Please enter a valid percentage between 0.00 - 1.00")
        return True

'''
Regex for any floating point number with + or - in the start
'''
def floating_point_regex(floating_point):
    # Convert floating_point into a valid string in Python
    # Check if the parameter floating_point is valid 
    floating_point_string = str(floating_point)
    if(not re.match(r'^[-+]?[0-9]*\.?[0-9]+$', floating_point_string)):
        print("Please enter a valid floating point number")
        return True

'''
Regex for Date
'''
'''
Regex for format YYYY-MM-DD where YYYY is between 1980 and 2021
'''
def date_regex(date):
    # Convert date into a valid string in Python
    # Check if the parameter date is valid
    date_string = str(date)
    if(not re.match(r'(19[89][0-9]|20[0-1][0-9]|2020)[- \/.](0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])', date_string)):
        print("Please enter a valid date from years 1980 - 2021")
        return True

'''
Regex for strings
'''
'''
Regex for team_name parameter
'''
def team_name_regex(team_name):
    # Convert team_name into a valid string in Python
    # Check if the parameter team_name is valid, no numbers and special chars
    team_name_string = str(team_name)
    if(not re.match("^[A-Za-z]+((\s)?([A-Za-z])+)*$", team_name_string)):
        print("Please enter a valid name with only letters and space")
        return True

'''
Regex for team_abv parameter
'''
def team_abv_regex(abv):
    # Convert abv into a valid string in Python
    # Check if the parameter abv is valid, only 3 captial letters
    abv_string = str(abv)
    if(not re.match("^[A-Z]{3}$", abv_string)):
        print("Please enter only 3 captial letters")
        return True

'''
Regex for player_name parameter
'''
def player_name_regrex(player_name):
    # Convert player_name into a valid string in Python
    # Check if the parameter player_name is valid, with spaces and special chars
    player_name_string = str(player_name)
    if(not re.match("^[A-Za-z]+((\s)?((\'|\-|\.)?([A-Za-z])+))*$", player_name_string)):
        print("Please enter a valid player name that may contain special chars")
        return True
