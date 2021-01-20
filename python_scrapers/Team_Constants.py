#####################################################
# File: Team_Constants.py 
# Author: Bryan Delas Penas 
# Email:  bryan.delaspenas0405@gmail.com
# Date:   12/17/2020
# 
# This file will contain all teams and former teams from 1979, when the 3 pointer was introduced inside of a dictionary

import pandas as pd
import os
import pathlib
from pathlib import Path
TEAM_TO_ABBRIVATION = {
    'ATLANTA HAWKS':                     'ALT', # Currently the Atlanta Hawks from 1968 to 2020
    'BOSTON CELTICS':                    'BOS', # Currently the Boston Celtics from 1946 to 2020
    'BROOKLYN NETS':                     'BRK', # Currently the Brooklyn Nets from 2012 to 2020 
    'NEW JERSEY NETS':                   'NJN', # Former the Brooklyn Nets from 1977 to 2011 
    'CHARLOTTE HORNETS':                 'CHO', # Currently the Charlotte Hornets from 2014 to 2020 but formely the Charlotee Hornets from 1989 to 2002
    'CHARLOTTE BOBCATS':                 'CHA', # Formerly the Charlotte Bobcats from, 2004 to 2014
    'CHICAGO BULLS':                     'CHI', # Currently the Chicago Bulls from 1966 to 2020
    'CLEVELAND CAVALIERS':               'CLE', # Currently the Cleveland Calvaliers from 1970 to 2020 
    'DALLAS MAVERICKS':                  'DAL', # Currently the Dallas Mavericks from 1980 to 2020 
    'DENVER NUGGETS':                    'DEN', # Currently the Denver Nuggets from 1967 to 2020
    'DETROIT PISTONS':                   'DET', # Currently the Detroit Pistons from 1948 to 2020 
    'GOLDEN STATE WARRIORS':             'GSW', # Currently the Golden State Warriors from 1946 to 2020 
    'HOUSTON ROCKETS':                   'HOU', # Currently the Houston Rockets from 1967 to 2020 
    'INDIANA PACERS':                    'IND', # Currently the Indiana Pacers from 1967 to 2020
    'LOS ANGELES CLIPPERS':              'LAC', # Currently the Los Angeles Clippers from 1970 to 2020 
    'SAN DIEGO CLIPPERS':                'SDC', # Formerly the San Diego Clippers from 1978 to 1984
    'LOS ANGELES LAKERS':                'LAL', # Currently the Los Angeles Lakers from 1960 to 2020
    'MEMPHIS GRIZZLIES':                 'MEM', # Currently the Memphis Grizzlies from 2001 to 2020 
    'VANCOUVER GRIZZLIES':               'VAN', # Formerly the Vancouver Grizzlies from 1995 to 2001   
    'MIAMI HEAT':                        'MIA', # Currently the Miami Heat from 1988 to 2020
    'MILWAUKEE BUCKS':                   'MIL', # Currently the Milwaukee Bucks from 1968 to 2020
    'MINNESOTA TIMBERWOLVES':            'MIN', # Currently the Minnesota Timberwolves from 1989 to 2020 
    'NEW ORLEANS PELICANS':              'NOP', # Currently the New Orleans Pelicans from 2013 to 2020
    'NEW ORLEANS/OKLAHOMA CITY HORNETS': 'NOK', # Formerly the NEW ORLEANS/OKLAHOMA CITY HORNETS from 2005 to 2007
    'NEW ORLEANS HORNETS':               'NOH', # Formerly the New Orleans Hornets from 2002 to 2012- 2013
    'NEW YORK KNICKS':                   'NYK', # Currently the New York Nicks from 1946 to 2020
    'OKLAHOMA CITY THUNDER':             'OKC', # Currently the Oklahoma City Thunder from 2009 to 2020 
    'SEATTLE SUPERSONICS':               'SEA', # Formerly the Searrle Supersonics from 1967 to 2008
    'ORLANDO MAGIC':                     'ORL', # Currently the Orlando Magic from 1989 to 2020 
    'PHILADELPHIA 76ERS':                'PHI', # Currently the Philadelphia 76ers from 1963 to 2020
    'PHOENIX SUNS':                      'PHO', # Currently the Phoenix Suns from 1968 to 2020 
    'PORTLAND TRAIL BLAZERS':            'POR', # Currently the Portland Trail Blazers from 1970 to 2020
    'SACRAMENTO KINGS':                  'SAC', # Currently the Sacramento Kings from 1985 to 2020
    'KANSAS CITY KINGS':                 'KCK', # Formerly the Kansas City Kings from 1975 to 1984
    'SAN ANTONIO SPURS':                 'SAS', # Currently the San Antonio Spurs from 1976 to 2020
    'TORONTO RAPTORS':                   'TOR', # Currently the Toranto Raptors from 1995 to 2020
    'UTAH JAZZ':                         'UTA', # Currently the Utah Jazz from 1979 to 2020 
    'NEW ORLEANS JAZZ' :                 'NOJ',
    'WASHINGTON WIZARDS':                'WAS', # Currently the Washington Wizards from 1998 to 2020 
    'WASHINGTON BULLETS':                'WAB', # Formerly the Washington Bullets from 1974 to 1997
}


# Does the opposite of TEAM_TO_ABV, takes in an ABV and turns into a team name
ABV_TO_TEAM = {
    'ALT': 'ATLANTA HAWKS', 
    'BOS': 'BOSTON CELTICS',
    'BRK': 'BROOKLYN NETS',  
    'NJN': 'NEW JERSEY NETS', 
    'CHO': 'CHARLOTTE HORNETS',
    'CHA': 'CHARLOTTE BOBCATS',
    'CHI': 'CHARLOTTE BOBCATS',
    'CLE': 'CLEVELAND CAVALIERS',
    'DAL': 'DALLAS MAVERICKS',
    'DEN': 'DENVER NUGGETS', 
    'DET': 'DETROIT PISTONS', 
    'GSW': 'GOLDEN STATE WARRIORS', 
    'HOU': 'HOUSTON ROCKETS',
    'IND': 'INDIANA PACERS', 
    'LAC': 'LOS ANGELES CLIPPERS', 
    'SDC': 'SAN DIEGO CLIPPERS', 
    'LAL': 'LOS ANGELES LAKERS', 
    'MEM': 'MEMPHIS GRIZZLIES',
    'VAN': 'VANCOUVER GRIZZLIES',                    
    'MIA': 'MIAMI HEAT',
    'MIL': 'MILWAUKEE BUCKS',             
    'MIN': 'MINNESOTA TIMBERWOLVES',              
    'NOP': 'NEW ORLEANS PELICANS',
    'NOK': 'NEW ORLEANS/OKLAHOMA CITY HORNETS', 
    'NOH': 'NEW ORLEANS HORNETS',
    'NYK': 'NEW YORK KNICKS', 
    'OKC': 'OKLAHOMA CITY THUNDER',
    'SEA': 'SEATTLE SUPERSONICS',
    'ORL': 'ORLANDO MAGIC', 
    'PHI': 'PHILADELPHIA 76ERS', 
    'PHO': 'PHOENIX SUNS', 
    'POR': 'PORTLAND TRAIL BLAZERS', 
    'SAC': 'SACRAMENTO KINGS', 
    'KCK': 'KANSAS CITY KINGS',
    'SAS': 'SAN ANTONIO SPURS', 
    'TOR': 'TORONTO RAPTORS', 
    'UTA': 'UTAH JAZZ', 
    'NOJ': 'NEW ORLEANS JAZZ',
    'WAS': 'WASHINGTON WIZARDS', 
    'WAB': 'WASHINGTON BULLETS',

}

# This is for teams id for later use in the database
TEAM_ID = {
    'ALT': 1, 
    'BOS': 2,
    'BRK': 3,  
    'NJN': 3, 
    'CHO': 4,
    'CHA': 4,
    'CHI': 5,
    'CLE': 6,
    'DAL': 7,
    'DEN': 8, 
    'DET': 9, 
    'GSW': 10, 
    'HOU': 11,
    'IND': 12, 
    'LAC': 13, 
    'SDC': 13, 
    'LAL': 14, 
    'MEM': 15,
    'VAN': 15,                    
    'MIA': 16,
    'MIL': 17,             
    'MIN': 18,              
    'NOP': 19,
    'NOK': 19, 
    'NOH': 19,
    'NYK': 20, 
    'OKC': 21,
    'SEA': 21,
    'ORL': 22, 
    'PHI': 23, 
    'PHO': 24, 
    'POR': 25, 
    'SAC': 26, 
    'KCK': 26,
    'SAS': 27, 
    'TOR': 28, 
    'UTA': 29, 
    'NOJ': 29,
    'WAS': 30, 
    'WAB': 30,
}

# This dict is used for getting team_advanced stats as they use the most updated team name except
# for some reason New Jersey Nets and Sacramento Kings
TEAM_DICT = {
    'CHO': 'CHA',
    'SDC': 'LAC',
    'VAN': 'MEM',
    'SEA': 'OKC',
    'NOJ': 'UTA',
    'WAB': 'WAS',
    'NOP': 'NOH',
    'NOK': 'NOH'

}

RIGHT_NAME_DICT = {

    ("Troy Brown", "July 28, 1999")        : "Troy Brown Jr.",
    ("Vernon Carey", "February 25, 2001")  : "Vernon Carey Jr.",       
    ("Wendell Carter","April 16, 1999")    : "Wendell Carter Jr.", 
    ("Larry Drew","March 5, 1990")         : "Larry Drew II",
    ("Tim Hardaway","March 16, 1992")      : "Tim Hardaway Jr.",
    ("Jaren Jackson","September 15, 1999") : "Jaren Jackson Jr.",
    ("Derrick Jones","February 15, 1997")  : "Derrick Jones Jr.",
    ("Walt Lemon","July 26, 1992")         : "Walt Lemon Jr.",
    ("Kira Lewis","April 6, 2001")         : "Kira Lewis Jr.",
    ("Kenyon Martin","January 6, 2001")    : "Kenyon Martin Jr.",
    ("Frank Mason","April 3, 1994")        : "Frank Mason III",
    ("Larry Nance","January 1, 1993")      : "Larry Nance Jr.",
    ("Kelly Oubre","December 9, 1995")     : "Kelly Oubre Jr.",
    ("Gary Payton","December 1, 1992")     : "Gary Payton II",
    ("Kevin Porter","May 4, 2000")         : "Kevin Porter Jr.",
    ("Michael Porter","June 29, 1998")     : "Michael Porter Jr.",
    ("Glen Rice","January 1, 1991")        : "Glen Rice Jr.",
    ("Glenn Robinson","January 8, 1994")   : "Glen Robinson III",
    ("Dennis Smith","November 25, 1997")   : "Dennis Smith Jr.",
    ("Xavier Tillman","January 12, 1999")  : "Xavier Tillman Sr.",
    ("Gary Trent","January 18, 1999")      : "Gary Trent Jr.",
    ("James Webb", "August 19, 1993")      : "James Webb III"
}

'''
Creates a dictionary with player name as key and value as a int
'''
def get_player_id():

    # Create a new dictionary with the following as key value pair
    # player name : id_num 
    player_id = {}

    csv_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player', 'Player_Name','player_names.csv')
    
    # Convert csv to dataframe
    df = pd.read_csv(csv_path)
    
    record = df.values.tolist()

    # Iterate through the list 
    for i in range( len(record)):
    
        name_tuple = (record[i][0], record[i][1])

        if(name_tuple in RIGHT_NAME_DICT):
            record[i][0] = RIGHT_NAME_DICT[name_tuple]
        player_id[record[i][0]] = i
    
    return player_id


# Global Decloration of Player_id
PLAYER_ID = get_player_id()
