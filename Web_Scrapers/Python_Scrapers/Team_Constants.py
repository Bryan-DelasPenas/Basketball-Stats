import pandas as pd
import os
import pathlib
from pathlib import Path

'''
Takes in Team Name and converts name into Three letter string
'''
TEAM_TO_ABBRIVATION = {
    'ATLANTA HAWKS':                     'ATL', # Currently the Atlanta Hawks from 1968 to 2020
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
    'WASHINGTON BULLETS':                'WSB', # Formerly the Washington Bullets from 1974 to 1997
}

'''
Does the opposite of TEAM_TO_ABV, takes in an ABV and turns into a team name
'''
ABV_TO_TEAM = {
    'ATL': 'ATLANTA HAWKS', 
    'BOS': 'BOSTON CELTICS',
    'BRK': 'BROOKLYN NETS',  
    'NJN': 'NEW JERSEY NETS', 
    'CHO': 'CHARLOTTE HORNETS',
    'CHH': 'CHARLOTTE HORNETS',
    'CHA': 'CHARLOTTE BOBCATS',
    'CHI': 'CHICAGO BULLS',
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
    'WSB': 'WASHINGTON BULLETS',
    'TOT': 'TOTAL AFTER TRADE'
}

'''
This is for teams id for later use in the database
'''
TEAM_ID = {
    'ATL': 1, 
    'BOS': 2,
    'BRK': 3,  
    'NJN': 3, 
    'CHO': 4,
    'CHA': 4,
    'CHH': 4,
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
    'WSB': 30,
    'TOT': 31,
}

'''
This dict is used for getting team_advanced stats as they use the most updated team name except
'''
TEAM_DICT = {
    'CHO': 'CHA',
    'SDC': 'LAC',
    'VAN': 'MEM',
    'SEA': 'OKC',
    'NOJ': 'UTA',
    'WSB': 'WAS',
    'NOP': 'NOH',
    'NOK': 'NOH',
    'KCK': 'SAC',
    'BRK': 'NJN',
}

'''
Converts wrong name into the proper name, example is adding JR. to names
'''
RIGHT_NAME_DICT = {

    ("Marvin Bagley", "March 14, 1999")      : "Marvin Bagley III",
    ("LaMark Baker", "November 11, 1969")    : "Mark Baker",
    ("Mohamed Bamba", "May 12, 1998")        : "Mo Bamba",
    ("Troy Brown", "July 28, 1999")          : "Troy Brown Jr.",
    ("Vernon Carey", "February 25, 2001")    : "Vernon Carey Jr.",       
    ("Wendell Carter", "April 16, 1999")     : "Wendell Carter Jr.", 
    ("Luigi Datome", "November 27, 1987")    : "Gigi Datome",
    ("Mark Davis", "June 8, 1963")           : "Mark Giles Davis",
    ("Mark Davis", "April 26, 1973")         : "Mark Anthony Davis",
    ("Mike Dunleavy", "September 15, 1980")  : "Mike Dunleavy Jr.",
    ("Larry Drew", "March 5, 1990")          : "Larry Drew II",
    ("Patrick Ewing", "May 20, 1984")        : "Patrick Ewing Jr.",
    ("Kiwane Garris", "September 24, 1974")  : "Kiwane Lemorris Garris",
    ("Tim Hardaway", "March 16, 1992")       : "Tim Hardaway Jr.",
    ("Cedric Henderson", "March 11, 1975")   : "Cedric Earl Henderson",
    ("Gerald Henderson", "December 9, 1987") : "Gerald Henderson Jr.",
    ("Jaren Jackson","September 15, 1999")   : "Jaren Jackson Jr.",
    ("Mike James", "June 23, 1975")          : "Michael Lamont James",
    ("Mike James", "August 18, 1990")        : "Michael Perry James",
    ("Chris Johnson", "July 15, 1985")       : "Chris Johnson (1985)",
    ("Chris Johnson", "April 29, 1990")      : "Chris Johnson (1990)",
    ("Eddie Johnson", "February 24, 1955")   : "Edward Lee Johnson",
    ("Eddie Johnson", "May 1, 1959")         : "Edward Arnet Johnson",
    ("George Johnson", "December 18, 1948")  : "George Thomas Johnson",
    ("George Johnson", "December 8, 1956")   : "George Lee Johnson",
    ("Ken Johnson", "November 7, 1962")      : "Kenneth Johnson",
    ("Ken Johnson", "February 1, 1978")      : "Kenyatta Johnson",
    ("Bobby Jones", "December 18, 1951")     : "Robert Jones",
    ("Bobby Jones", "January 9, 1984")       : "Bobby Ray Jones",
    ("Charles Jones", "January 12, 1962")    : "Charles Alexander Jones",
    ("Charles Jones", "July 17, 1975")       : "Charles Rahmel Jones",
    ("Derrick Jones", "February 15, 1997")   : "Derrick Jones Jr.",
    ("Mark Jones", "April 10, 1961")         : "Mark Anthony Jones",
    ("Walt Lemon", "July 26, 1992")          : "Walt Lemon Jr.",
    ("Kira Lewis", "April 6, 2001")          : "Kira Lewis Jr.",
    ("Kenyon Martin", "January 6, 2001")     : "Kenyon Martin Jr.",
    ("Frank Mason", "April 3, 1994")         : "Frank Mason III",
    ("Didier Ilunga-Mbenga", "December 30, 1980")    : "D.J. Mbenga",
    ("Tony Mitchell", "April 7, 1992")       : "Tony LaShae Mitchell",
    ("Larry Nance", "January 1, 1993")       : "Larry Nance Jr.",
    ("Kelly Oubre", "December 9, 1995")      : "Kelly Oubre Jr.",
    ("Gary Payton", "December 1, 1992")      : "Gary Payton II",
    ("Kevin Porter", "May 4, 2000")          : "Kevin Porter Jr.",
    ("Michael Porter", "June 29, 1998")      : "Michael Porter Jr.",
    ("Efthimi Rentzias", "January 11, 1976") : "Efthimios Rentzias",
    ("Glen Rice", "January 1, 1991")         : "Glen Rice Jr.",
    ("Glenn Robinson", "January 8, 1994")    : "Glenn Robinson III",
    ("Walker Russell", "October 6, 1982")    : "Walker Russell Jr.",
    ("Charles Smith", "July 16, 1965")       : "Charles Daniel Smith",
    ("Charles Smith", "November 29, 1967")   : "Charles Edward Smith",
    ("Charles Smith", "August 22, 1975")     : "Charles Cornelius Smith",
    ("Chris Smith", "May 17, 1970")          : "Chris G. Smith",
    ("Dennis Smith", "November 25, 1997")    : "Dennis Smith Jr.",
    ("Michael Smith", "May 19, 1965")        : "Michael Smith (1965)",
    ("Michael Smith", "March 28, 1972")      : "Michael Smith (1972)",
    ("Jeffery Taylor", "May 23, 1989")       : "Jeff Matthew Taylor",
    ("Xavier Tillman", "January 12, 1999")   : "Xavier Tillman Sr.",
    ("Gary Trent", "January 18, 1999")       : "Gary Trent Jr.",
    ("Marcus Williams", "December 3, 1985")  : "Marcus Darell Williams",
    ("Marcus Williams", "November 18, 1986") : "Marcus Eliot Williams",
    ("Reggie Williams", "September 14, 1986"): "Reginald Leon Williams",
    ("James Webb", "August 19, 1993")        : "James Webb III",
    ("Chris Wright", "September 30, 1988")   : "Chris Wright (1988)",
    ("Chris Wright", "November 4, 1989")     : "Chris Wright (1989)",
    ("Omer Ask", "July 4, 1986")             : "Omer Asik",
    ("Vitor Luiz Faverani", "May 5, 1988")   : "Vitor Faverani",
    ("Horacio Llamas Grey", "July 17, 1973") : "Horacio Llamas",
    ("Dee Brown", "November 29, 1968")       : "DeCovan Brown",
}

'''
This is mainly used for the insert script for the database
'''
REVERSE_RIGHT_DICT = {
    "Marvin Bagley III"       : "Marvin Bagley",
    "Mark Baker"              : "LaMark Baker",
    "Mo Bamba"                : "Mohamed Bamba" ,
    "Troy Brown Jr"          : "Troy Brown" ,
    "Vernon Carey Jr"        : "Vernon Carey",       
    "Wendell Carter Jr"      : "Wendell Carter" , 
    "Gigi Datome"             : "Luigi Datome",
    "Mark Giles Davis"        : "Mark Davis",
    "Mark Anthony Davis"      : "Mark Davis",
    "Mike Dunleavy Jr"       : "Mike Dunleavy",
    "Larry Drew II"           : "Larry Drew", 
    "Patrick Ewing Jr"       : "Patrick Ewing", 
    "Kiwane Lemorris Garris"  : "Kiwane Garris",
    "Tim Hardaway Jr"        : "Tim Hardaway",
    "Cedric Earl Henderson"   : "Cedric Henderson",
    "Gerald Henderson Jr"    : "Gerald Henderson",
    "Jaren Jackson Jr"       : "Jaren Jackson", 
    "Michael Lamont James"    : "Mike James",
    "Michael Perry James"     : "Mike James",
    "Chris Johnson (1985)"    : "Chris Johnson",
    "Chris Johnson (1990)"    : "Chris Johnson",
    "Edward Lee Johnson"      : "Eddie Johnson",
    "Edward Arnet Johnson"    : "Eddie Johnson", 
    "George Thomas Johnson"   : "George Johnson",
    "George Lee Johnson"      : "George Johnson",
    "Kenneth Johnson"         : "Ken Johnson",
    "Kenyatta Johnson"        : "Ken Johnson", 
    "Robert Jones"            : "Bobby Jones",
    "Bobby Ray Jones"         : "Bobby Jones",
    "Charles Alexander Jones" : "Charles Jones",
    "Charles Rahmel Jones"    : "Charles Jones",
    "Derrick Jones Jr"       : "Derrick Jones",
    "Mark Anthony Jones"      : "Mark Jones",
    "Walt Lemon Jr"          : "Walt Lemon",
    "Kira Lewis Jr"          : "Kira Lewis",
    "Kenyon Martin Jr"       : "Kenyon Martin",
    "Frank Mason III"         : "Frank Mason",
    "D.J. Mbenga"             : "Didier Ilunga-Mbenga",
    "Tony LaShae Mitchell"    : "Tony Mitchell",
    "Larry Nance Jr"         : "Larry Nance",
    "Kelly Oubre Jr"         : "Kelly Oubre",
    "Gary Payton II"          : "Gary Payton",
    "Kevin Porter Jr"        : "Kevin Porter",
    "Michael Porter Jr"      : "Michael Porter",
    "Glen Rice Jr"           : "Glen Rice",
    "Glenn Robinson III"      : "Glenn Robinson",
    "Walker Russell Jr"      : "Walker Russell",
    "Charles Daniel Smith"    : "Charles Smith",
    "Charles Edward Smith"    : "Charles Smith",
    "Charles Cornelius Smith" : "Charles Smith",
    "Chris G. Smith"          : "Chris Smith", 
    "Dennis Smith Jr"        : "Dennis Smith",
    "Michael Smith (1965)"    : "Michael Smith",
    "Michael Smith (1972)"    : "Michael Smith",
    "Jeff Matthew Taylor"     : "Jeffery Taylor",
    "Xavier Tillman Sr"      : "Xavier Tillman",
    "Gary Trent Jr"          : "Gary Trent",
    "Marcus Darell Williams"  :  "Marcus Williams",
    "Marcus Eliot Williams"   :  "Marcus Williams",
    "Reginald Leon Williams"  : "Reggie Williams",
    "James Webb III"          : "James Webb",
    "Chris Wright (1988)"     : "Chris Wright",
    "Chris Wright (1989)"     : "Chris Wright",
    #"Omer Asik"               : "Omer Ask",
    "Horacio Llamas"          : "Horacio Llamas Grey",
    "DeCovan Brown"           : "Dee Brown", 
   
}

'''
Special cases when the name does not match the URL generated
'''
RIGHT_PLAYER_SUFIX = {

    ("Jeff Ayres", "April 29, 1987")                 : "Jeff Pendergraph",
    ("J.J. Barea", "June 26, 1984")                  : "Jose Barea",
    ("Clint Capela", "May 18, 1994")                 : "Caint Capela",
    ("Nando De Colo", "June 23, 1987")               : "Nando DeColo",
    ("Vinny Del Negro", "August 9, 1966")            : "Vinny DelNegro",
    ("Khalid El-Amin", "April 25, 1979")             : "Khalid ElAmin",
    ("Alfredrick Hughes", "July 19, 1962")           : "Rick Hughes",
    ("Didier Ilunga-Mbenga", "December 30, 1980")    : "D.J. Mbenga",
    ("Michael Kidd-Gilchrist", "September 26, 1993") : "Michael KiddGilchrist",
    ("Maxi Kleber", "January 29, 1992")              : "Maxi Klebir",
    ("Horacio Llamas Grey", "July 17, 1973")         : "Horacio Llamas",
    ("John Lucas III", "November 21, 1982")          : "John Lucas",
    ("Sheldon Mac", "December 21, 1992")             : "Sheldon McClellan",
    ("Frank Ntilikina", "July 28, 1998")             : "Larank Ntilikina",
    ("Cedi Osman", "April 8, 1995")                  : "De Osman",
    ("Sasha Pavlovic", "November 15, 1983")          : "alsha Pavlovic",
    ("Mouhamed Sene", "May 12, 1986")                : "Sa Sene",
    ("Edy Tavares", "March 22, 1992")                : "Walter Tavares",
    ("Nick Van Exel", "November 27, 1971")           : "Nick VanExel",
    ("Keith Van Horn", "October 23, 1975")           : "Keith VanHorn",
    ("Logan Vander Velden", "April 3, 1971")         : "Logan Vander",
    ("Marcus Vinicius", "May 31, 1984")              : "Marcus Vincius",
    ("Henry Walker", "October 9, 1987")              : "Bill Walker",
    ("Mo Williams", "December 19, 1982")             : "Maurice Williams",
    ("Metta World Peace", "November 13, 1979")       : "Ron Artes"

}

'''
If the name is correct but the page name is not correct 
'''
SPECIAL_NAME_DICT = {
    ("Nene Hilario", "September 13, 1982")    : "Nene",
    ("Dee Brown", "November 29, 1968")        : "Dee Brown",
    ("Mark Davis","June 8, 1963")             : "Mark Davis",
    ("Mark Davis", "April 26, 1973")          : "Mark Davis",
    ("Mike Dunleavy", "September 15, 1980")   : "Mike Dunleavy",
    ("Patrick Ewing", "May 20, 1984")         : "Patrick Ewing", 
    ("Cedric Henderson", "March 11, 1975")    : "Cedric Henderson",
    ("Gerald Henderson", "December 9, 1987")  : "Gerald Henderson",
    ("Mike James", "June 23, 1975")           : "Mike James",
    ("Mike James", "August 18, 1990")         : "Mike James",
    ("Chris Johnson", "July 15, 1985")        : "Chris Johnson",
    ("Chris Johnson", "April 29, 1990")       : "Chris Johnson",
    ("Eddie Johnson", "February 24, 1955")    : "Eddie Johnson",
    ("Eddie Johnson", "May 1, 1959")          : "Eddie Johnson",
    ("George Johnson", "December 18, 1948")   : "George Johnson",
    ("George Johnson", "December 8, 1956")    : "George Johnson",
    ("Ken Johnson", "November 7, 1962")       : "Ken Johnson",
    ("Ken Johnson", "February 1, 1978")       : "Ken Johnson",
    ("Bobby Jones", "December 18, 1951")      : "Bobby Jones",
    ("Bobby Jones", "January 9, 1984")        : "Bobby Jones",
    ("Charles Jones", "April 3, 1957")        : "Charles Jones",
    ("Charles Jones", "January 12, 1962")     : "Charles Jones",
    ("Charles Jones", "July 17, 1975")        : "Charles Jones",
    ("Mark Jones", "April 10, 1961")          : "Mark Jones",
    ("Mark Jones", "May 25, 1975")            : "Mark Jones",
    ("Tony Mitchell", "August 7, 1989")       : "Tony Mitchell",
    ("Tony Mitchell","April 7, 1992")         : "Tony Mitchell",
    ("Walker Russell", "October 26, 1960")    : "Walker Russell",
    ("Walker Russell", "October 6, 1982")     : "Walker Russell",
    ("Charles Smith", "July 16, 1965")        : "Charles Smith",
    ("Charles Smith", "November 29, 1967")    : "Charles Smith",
    ("Charles Smith", "August 22, 1975")      : "Charles Smith",
    ("Chris Smith", "May 17, 1970")           : "Chris Smith",
    ("Chris Smith", "October 13, 1987")       : "Chris Smith",
    ("Michael Smith", "May 19, 1965")         : "Michael Smith",
    ("Michael Smith", "March 28, 1972")       : "Michael Smith",
    ("Jeff Taylor", "May 23, 1989")           : "Jeff Taylor",
    ("Jeffery Taylor", "May 23, 1989")        : "Jeff Taylor",
    ("Marcus Williams", "December 3, 1985")   : "Marcus Williams",
    ("Marcus Williams", "November 18, 1986")  : "Marcus Williams",
    ("Reggie Williams", "March 5, 1964")      : "Reggie Williams",
    ("Reggie Williams", "September 14, 1986") : "Reggie Williams",
    ("Chris Wright", "September 30, 1988")    : "Chris Wright",
    ("Chris Wright", "November 4, 1989")      : "Chris Wright",
    ("Vitor Faverani", "May 5, 1988" )        : "Vitor Luiz Faverani"
}

'''
This is for players who didn't play in the reg season but in the playoffs for a given year
'''
DATABASE_DICT = {
        'Dorell Wright' : [[2016, 16, 3244, 'MIA', 'Miami Heat', 'December 2, 1985', 'Dorell Wright']],    
        'Dwayne Jones': [[2013, 10, 1540, 'GSW', 'Golden State Warriors', 'June 9, 1983', 'Dwayne Jones']],
        'Ed Sherod': [[1982, 3, 2618, 'NJN', 'New Jersey Nets', 'September 13, 1959', 'Ed Sherod']],
        'Jaylen Adams': [[2020, 25, 14, 'POR', 'Portland Trail Blazers', 'May 4, 1996', 'Jaylen Adams']],
        'John Holland': [[2016, 2, 1312, 'BOS', 'Boston Celtics', 'November 6, 1988', 'John Holland']],
        'Larry Krystkowiak': [[1991, 17, 1659, 'MIL', 'Milwaukee Bucks', 'September 23, 1964', 'Larry Krystkowiak']],
        'Mike Brown': [[1998, 24, 390, 'PHO', 'Phoenix Suns', 'July 19, 1963', 'Mike Brown']],
        'Mike Mitchell': [[1990, 27, 2013, 'SAS', 'San Antonio Spurs', 'January 1, 1956', 'Mike Mitchell']],
        'Scott Machado': [[2013, 10, 1797, 'GSW', 'Golden State Warriors', 'June 8, 1990', 'Scott Machado']],
        'Tracy McGrady': [[2013, 27, 1935, 'SAS', 'San Antonio Spurs', 'May 24, 1979', 'Tracy McGrady']],
        'Ty Lawson': [[2018, 30, 1709, 'WAS', 'Washington Wizards', 'November 3, 1987', 'Ty Lawson']]
}

'''
Creates a dictionary with player name as key and value as a int
'''
def get_player_id():

    # Create a new dictionary with the following as key value pair
    # player name : id_num 
    player_id = {}

    csv_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player_Name','player_names.csv')
    
    # Convert csv to dataframe
    df = pd.read_csv(csv_path)
    
    record = df.values.tolist()

    # Iterate through the list 
    for i in range( len(record)):
    
        name_tuple = (record[i][0], record[i][1])

        if(name_tuple in RIGHT_NAME_DICT):
            record[i][0] = RIGHT_NAME_DICT[name_tuple]
        player_id[record[i][0]] = i + 1
    
    return player_id


'''
Global Dict for Player's ID
'''
PLAYER_ID = get_player_id()
print(PLAYER_ID)