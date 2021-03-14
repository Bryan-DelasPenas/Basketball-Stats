import pandas as pd
import numpy as np
import sys 
import pathlib
import os
import unittest
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts')
sys.path.append(str(pathlib.Path().absolute()) + '\\Database' +'\\Python Scripts' + '\\Queries')
import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine

from Helper_DB import create_connection, test_connection, check_table
from Query_Player_Advanced import drop_player_advanced_query, create_player_advanced_query

class TestQueryPlayerAdvanced(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Drop Procedures 
        drop_player_advanced_query()

        # Create Procedures
        create_player_advanced_query()

if __name__ == '__main__':
    unittest.main()