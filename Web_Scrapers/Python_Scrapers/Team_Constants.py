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

    ("Marvin Bagley", "1999-03-14")          : "Marvin Bagley III",
    ("LaMark Baker", "1969-11-11")           : "Mark Baker",
    ("Mohamed Bamba", "1998-05-12")          : "Mo Bamba",
    ("Troy Brown", "1999-07-28")             : "Troy Brown Jr.",
    ("Vernon Carey", "2001-02-25")           : "Vernon Carey Jr.",       
    ("Wendell Carter", "1999-04-16")         : "Wendell Carter Jr.", 
    ("Luigi Datome", "1987-11-27")           : "Gigi Datome",
    ("Mark Davis", "1963-06-08")             : "Mark Giles Davis",
    ("Mark Davis", "1973-04-26")             : "Mark Anthony Davis",
    ("Mike Dunleavy", "1980-09-15")          : "Mike Dunleavy Jr.",
    ("Larry Drew", "1990-03-05")             : "Larry Drew II",
    ("Patrick Ewing", "1984-05-20")          : "Patrick Ewing Jr.",
    ("Kiwane Garris", "1974-09-24")          : "Kiwane Lemorris Garris",
    ("Tim Hardaway", "1992-03-16")           : "Tim Hardaway Jr.",
    ("Cedric Henderson", "1975-03-11")       : "Cedric Earl Henderson",
    ("Gerald Henderson", "1987-12-09")       : "Gerald Henderson Jr.",
    ("Jaren Jackson","1999-09-15")           : "Jaren Jackson Jr.",
    ("Mike James", "1975-06-23")             : "Michael Lamont James",
    ("Mike James", "1990-08-18")             : "Michael Perry James",
    ("Chris Johnson", "1985-07-15")          : "Chris Johnson (1985)",
    ("Chris Johnson", "1990-04-29")          : "Chris Johnson (1990)",
    ("Eddie Johnson", "1955-02-24")          : "Edward Lee Johnson",
    ("Eddie Johnson", "1959-05-01")          : "Edward Arnet Johnson",
    ("George Johnson", "1948-12-18")         : "George Thomas Johnson",
    ("George Johnson", "1956-12-08")         : "George Lee Johnson",
    ("Ken Johnson", "1962-11-07")            : "Kenneth Johnson",
    ("Ken Johnson", "1978-02-01")            : "Kenyatta Johnson",
    ("Bobby Jones", "1951-12-18")            : "Robert Jones",
    ("Bobby Jones", "1984-01-09")            : "Bobby Ray Jones",
    ("Charles Jones", "1962-01-12")          : "Charles Alexander Jones",
    ("Charles Jones", "1975-07-17")          : "Charles Rahmel Jones",
    ("Derrick Jones", "1997-02-15")          : "Derrick Jones Jr.",
    ("Mark Jones", "1961-04-10")             : "Mark Anthony Jones",
    ("Walt Lemon", "1992-07-26")             : "Walt Lemon Jr.",
    ("Kira Lewis", "2001-04-06")             : "Kira Lewis Jr.",
    ("Kenyon Martin", "2001-01-06")           : "Kenyon Martin Jr.",
    ("Frank Mason", "1994-04-03")            : "Frank Mason III",
    ("Didier Ilunga-Mbenga", "1980-12-30")   : "D.J. Mbenga",
    ("Tony Mitchell", "1992-04-07")          : "Tony LaShae Mitchell",
    ("Larry Nance", "1993-01-01")            : "Larry Nance Jr.",
    ("Kelly Oubre", "1995-12-09")            : "Kelly Oubre Jr.",
    ("Gary Payton", "1992-12-01")            : "Gary Payton II",
    ("Kevin Porter", "2000-05-04")           : "Kevin Porter Jr.",
    ("Michael Porter", "1998-06-29")         : "Michael Porter Jr.",
    ("Efthimi Rentzias", "1976-01-11")       : "Efthimios Rentzias",
    ("Glen Rice", "1991-01-01")              : "Glen Rice Jr.",
    ("Glenn Robinson", "1994-01-08")         : "Glenn Robinson III",
    ("Walker Russell", "1982-10-06")         : "Walker Russell Jr.",
    ("Charles Smith", "1965-07-16")          : "Charles Daniel Smith",
    ("Charles Smith", "1967-11-29")          : "Charles Edward Smith",
    ("Charles Smith", "1975-08-22")          : "Charles Cornelius Smith",
    ("Chris Smith", "1970-05-17")            : "Chris G. Smith",
    ("Dennis Smith", "1997-11-25")           : "Dennis Smith Jr.",
    ("Michael Smith", "1965-05-19")          : "Michael Smith (1965)",
    ("Michael Smith", "1972-03-28")          : "Michael Smith (1972)",
    ("Jeffery Taylor", "1989-05-23")         : "Jeff Matthew Taylor",
    ("Xavier Tillman", "1999-01-12")         : "Xavier Tillman Sr.",
    ("Gary Trent", "1999-01-18")             : "Gary Trent Jr.",
    ("Marcus Williams", "1985-12-03")        : "Marcus Darell Williams",
    ("Marcus Williams", "1986-11-18")        : "Marcus Eliot Williams",
    ("Reggie Williams", "1986-09-14")        : "Reginald Leon Williams",
    ("James Webb", "1993-08-19")             : "James Webb III",
    ("Chris Wright", "1988-11-30")           : "Chris Wright (1988)",
    ("Chris Wright", "1989-11-04")           : "Chris Wright (1989)",
    ("Omer Ask", "1986-07-04")               : "Omer Asik",
    ("Vitor Luiz Faverani", "1988-05-05")    : "Vitor Faverani",
    ("Horacio Llamas Grey", "1973-07-17")    : "Horacio Llamas",
    ("Dee Brown", "1968-11-29")              : "DeCovan Brown",
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

    ("Jeff Ayres", "1987-04-29")                     : "Jeff Pendergraph",
    ("J.J. Barea", "1984-06-26")                     : "Jose Barea",
    ("Clint Capela", "1994-05-18")                   : "Caint Capela",
    ("Nando De Colo", "1987-06-23")                  : "Nando DeColo",
    ("Vinny Del Negro", "1966-08-09")                : "Vinny DelNegro",
    ("Khalid El-Amin", "1979-04-25")                 : "Khalid ElAmin",
    ("Alfredrick Hughes", "1962-07-19")              : "Rick Hughes",
    ("Didier Ilunga-Mbenga", "1980-12-30")           : "D.J. Mbenga",
    ("Michael Kidd-Gilchrist", "1993-09-26")         : "Michael KiddGilchrist",
    ("Maxi Kleber", "1992-01-29")                    : "Maxi Klebir",
    ("Horacio Llamas Grey", "1973-07-17")            : "Horacio Llamas",
    ("John Lucas III", "1982-11-21")                 : "John Lucas",
    ("Sheldon Mac", "1992-12-21")                    : "Sheldon McClellan",
    ("Frank Ntilikina", "1998-07-28")                : "Larank Ntilikina",
    ("Cedi Osman", "1995-04-08")                     : "De Osman",
    ("Sasha Pavlovic", "1983-11-15")                 : "alsha Pavlovic",
    ("Mouhamed Sene", "1986-05-12")                  : "Sa Sene",
    ("Edy Tavares", "1992-03-22")                    : "Walter Tavares",
    ("Nick Van Exel", "1971-11-27")                  : "Nick VanExel",
    ("Keith Van Horn", "1975-10-23")                 : "Keith VanHorn",
    ("Logan Vander Velden", "1971-04-03")            : "Logan Vander",
    ("Marcus Vinicius", "1984-05-31")                : "Marcus Vincius",
    ("Henry Walker", "1987-10-09")                   : "Bill Walker",
    ("Mo Williams", "1982-12-19")                    : "Maurice Williams",
    ("Metta World Peace", "1979-11-13")              : "Ron Artes",
    ("Wayne Engelstad", "1965-12-06")                : "Wayne Englestad"
}

'''
If the name is correct but the page name is not correct 
'''
SPECIAL_NAME_DICT = {
    ("Nene Hilario", "1982-09-13")            : "Nene",
    ("Dee Brown", "1968-11-29")               : "Dee Brown",
    ("Mark Davis","1963-06-08")               : "Mark Davis",
    ("Mark Davis", "1973-04-26")              : "Mark Davis",
    ("Mike Dunleavy", "1980-09-15")           : "Mike Dunleavy",
    ("Patrick Ewing", "1984-05-20")           : "Patrick Ewing", 
    ("Cedric Henderson", "1975-03-11")        : "Cedric Henderson",
    ("Gerald Henderson", "1987-12-09")        : "Gerald Henderson",
    ("Mike James", "1975-06-23")              : "Mike James",
    ("Mike James", "1990-08-18")              : "Mike James",
    ("Chris Johnson", "1985-07-15")           : "Chris Johnson",
    ("Chris Johnson", "1990-04-29")           : "Chris Johnson",
    ("Eddie Johnson", "1955-02-24")           : "Eddie Johnson",
    ("Eddie Johnson", "1959-05-01")           : "Eddie Johnson",
    ("George Johnson", "1948-12-18")          : "George Johnson",
    ("George Johnson", "1956-12-08")          : "George Johnson",
    ("Ken Johnson", "1962-11-07")             : "Ken Johnson",
    ("Ken Johnson", "1978-02-01")             : "Ken Johnson",
    ("Bobby Jones", "1951-12-18")             : "Bobby Jones",
    ("Bobby Jones", "1984-01-09")             : "Bobby Jones",
    ("Charles Jones", "1957-04-03")           : "Charles Jones",
    ("Charles Jones", "1962-01-12")           : "Charles Jones",
    ("Charles Jones", "1975-07-17")           : "Charles Jones",
    ("Mark Jones", "1961-04-10")              : "Mark Jones",
    ("Mark Jones", "1975-05-25")              : "Mark Jones",
    ("Tony Mitchell", "1989-08-07")           : "Tony Mitchell",
    ("Tony Mitchell","1992-04-07")            : "Tony Mitchell",
    ("Walker Russell", "1960-10-26")          : "Walker Russell",
    ("Walker Russell", "1982-10-06")          : "Walker Russell",
    ("Charles Smith", "1965-07-16")           : "Charles Smith",
    ("Charles Smith", "1967-11-29")           : "Charles Smith",
    ("Charles Smith", "1975-08-22")           : "Charles Smith",
    ("Chris Smith", "1970-05-17")             : "Chris Smith",
    ("Chris Smith", "1987-10-13")             : "Chris Smith",
    ("Michael Smith", "1965-05-19")           : "Michael Smith",
    ("Michael Smith", "1972-03-28")           : "Michael Smith",
    ("Jeff Taylor", "1989-05-23")             : "Jeff Taylor",
    ("Jeffery Taylor", "1989-05-23")          : "Jeff Taylor",
    ("Marcus Williams", "1985-12-03")         : "Marcus Williams",
    ("Marcus Williams", "1986-11-18")         : "Marcus Williams",
    ("Reggie Williams", "1964-03-05")         : "Reggie Williams",
    ("Reggie Williams", "1986-09-14")         : "Reggie Williams",
    ("Chris Wright", "1988-11-30")            : "Chris Wright",
    ("Chris Wright", "1989-11-04")            : "Chris Wright",
    ("Vitor Faverani", "1988-05-05" )         : "Vitor Luiz Faverani"
}

'''
This is for players who didn't play in the reg season but in the playoffs for a given year
'''
DATABASE_DICT = {
        'Dorell Wright' : [[2016, 16, 3250, 'MIA', 'Miami Heat', '1985-12-2', 'Dorell Wright']],    
        'Dwayne Jones': [[2013, 10, 1542, 'GSW', 'Golden State Warriors', '1983-06-09', 'Dwayne Jones']],
        'Ed Sherod': [[1982, 3, 2622, 'NJN', 'New Jersey Nets', '1959-09-13', 'Ed Sherod']],
        'Jaylen Adams': [[2020, 25, 14, 'POR', 'Portland Trail Blazers', '1996-05-04', 'Jaylen Adams']],
        'John Holland': [[2016, 2, 1314, 'BOS', 'Boston Celtics', '1988-11-06', 'John Holland']],
        'Larry Krystkowiak': [[1991, 17, 1661, 'MIL', 'Milwaukee Bucks', '1964-09-23', 'Larry Krystkowiak']],
        'Mike Brown': [[1998, 24, 390, 'PHO', 'Phoenix Suns', '1963-07-19', 'Mike Brown']],
        'Mike Mitchell': [[1990, 27, 2016, 'SAS', 'San Antonio Spurs', '1956-01-01', 'Mike Mitchell']],
        'Scott Machado': [[2013, 10, 1800, 'GSW', 'Golden State Warriors', '1990-06-08', 'Scott Machado']],
        'Tracy McGrady': [[2013, 27, 1938, 'SAS', 'San Antonio Spurs', '1979-05-24', 'Tracy McGrady']],
        'Ty Lawson': [[2018, 30, 1712, 'WAS', 'Washington Wizards', '1987-11-03', 'Ty Lawson']]
}

'''
Creates a dictionary with player name as key and value as a int
'''
def get_player_id():

    # Create a new dictionary with the following as key value pair
    # player name : id_num 
    player_id = {}

    csv_path = os.path.join(pathlib.Path().absolute(), 'Output', 'Player_Name','player_names.csv')
    if(not os.path.isfile(csv_path)):
        
        csv_path = os.path.join(pathlib.Path().absolute(), 'Web_Scrapers','Output', 'Player_Name','player_names.csv')

        # This is for when DB notebook calls DB insert
        if(not os.path.isfile(csv_path)):
            csv_path = os.path.join(pathlib.Path().absolute().parent.parent, 'Web_Scrapers','Output', 'Player_Name','player_names.csv')

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
