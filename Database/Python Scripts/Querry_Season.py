import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_table

'''
Season Queries
'''
'''
Select * queries
'''
'''
Input: season_id = The Season_ID of the eninity
Function Returns Season ID
'''
def querry_all_season(season_id):
     
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists 
    if(check_table('Season')):
        
        # Only one pk value was inputed
        
        try:
            # Create a parameterized querry 
            querry = conn.execute(
            """
            SELECT *
            FROM Season
            WHERE Season_ID = %s
            """,  season_id)
            trans.commit()
            print("Querry_All_Season was Successful ")
            
        except:
            raise Exception("Querry_All_Season Failed")
    else:
        raise Exception("Table was not Found")