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
from Query_Conference_Standings import drop_cs_query

# Team Procedures
from Query_Team import drop_team_query
from Query_Roster import drop_roster_query
from Query_Team_Advanced import drop_team_advanced_query
from Query_Team_Misc import drop_team_misc_query
from Query_Team_Per_Game import drop_team_per_game_query
from Query_Team_Per_Poss import drop_team_per_poss_query
from Query_Team_Stats import drop_team_stats_query
from Query_Team_Totals import drop_team_totals_query

# Player Procedures
from Query_Player import drop_player_query
from Query_Player_Advanced import drop_player_advanced_query
from Query_Player_Per_Game import drop_player_per_game_query
from Query_Player_Per_Minute import drop_player_per_minute_query
from Query_Player_Per_Poss import drop_player_per_poss_query
from Query_Player_Stats import drop_player_stats_query
from Query_Player_Totals import drop_player_totals_query

# Player Career Procedures
from Query_Player_Career_Advanced import drop_player_career_advanced_query
from Query_Player_Career_Per_Game import drop_player_career_per_game_query
from Query_Player_Career_Per_Minute import drop_player_career_per_minute_query
from Query_Player_Career_Per_Poss import drop_player_career_per_poss_query
from Query_Player_Career_Stats import drop_player_career_stats_query
from Query_Player_Career_Totals import drop_player_career_totals_query


def main():
    # Season Procedures 
    drop_cs_query()

    # Team Procedures
    drop_team_query()
    drop_roster_query()
    drop_team_advanced_query()
    drop_team_misc_query()
    drop_team_per_game_query()
    drop_team_per_poss_query()
    drop_team_stats_query()
    drop_team_totals_query()

    # Player Procedures
    drop_player_query()
    drop_player_advanced_query()
    drop_player_per_game_query()
    drop_player_per_minute_query()
    drop_player_per_poss_query()
    drop_player_stats_query()
    drop_player_totals_query()
    
    # Player Career Procedures
    drop_player_career_advanced_query()
    drop_player_career_per_game_query()
    drop_player_career_per_minute_query()
    drop_player_career_per_poss_query()
    drop_player_career_stats_query()
    drop_player_career_totals_query()


if __name__ == "__main__":
    main()