# Import SQL modules
import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine

import pandas as pd
import pathlib
import sys

# Add path to the sys
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')

# Import helper functions
from Helper_DB import test_connection, create_connection, check_procedure

# Season Procedures 
from Query_Conference_Standings import create_cs_query

# Team Procedures
from Query_Team import create_team_query
from Query_Roster import create_roster_query
from Query_Team_Advanced import create_team_advanced_query
from Query_Team_Misc import create_team_misc_query
from Query_Team_Per_Game import create_team_per_game_query
from Query_Team_Per_Poss import create_team_per_poss_query
from Query_Team_Stats import create_team_stats_query
from Query_Team_Totals import create_team_totals_query

# Player Procedures
from Query_Player import create_player_query
from Query_Player_Advanced import create_player_advanced_query
from Query_Player_Per_Game import create_player_per_game_query
from Query_Player_Per_Minute import create_player_per_minute_query
from Query_Player_Per_Poss import create_player_per_poss_query
from Query_Player_Stats import create_player_stats_query
from Query_Player_Totals import create_player_totals_query

# Player Career Procedures
from Query_Player_Career_Advanced import create_player_career_advanced_query
from Query_Player_Career_Per_Game import create_player_career_per_game_query
from Query_Player_Career_Per_Minute import create_player_career_per_minute_query
from Query_Player_Career_Per_Poss import create_player_career_per_poss_query
from Query_Player_Career_Stats import create_player_career_stats_query
from Query_Player_Career_Totals import create_player_career_totals_query


def create_all():
    # Season Procedures 
    create_cs_query()

    # Team Procedures
    create_team_query()
    create_roster_query()
    create_team_advanced_query()
    create_team_misc_query()
    create_team_per_game_query()
    create_team_per_poss_query()
    create_team_stats_query()
    create_team_totals_query()

    # Player Procedures
    create_player_query()
    create_player_advanced_query()
    create_player_per_game_query()
    create_player_per_minute_query()
    create_player_per_poss_query()
    create_player_stats_query()
    create_player_totals_query()
    
    # Player Career Procedures
    create_player_career_advanced_query()
    create_player_career_per_game_query()
    create_player_career_per_minute_query()
    create_player_career_per_poss_query()
    create_player_career_stats_query()
    create_player_career_totals_query()

def main():
    create_all()

if __name__ == "__main__":
    main()