import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

from Helper_DB import test_connection, create_connection, check_table

'''
Team Querries
'''
'''
Select * querries
'''
'''
Input: format = the primary keys of the 
       id_one = first value of the primary key
       id_two = second value of the primary key if range is wanted(using Between)
Returns all columns inside of Teams based on a single primary key
'''
def querry_all_team_single_pk(format, id_one, id_two = None):
    
    # Lower case format 
    format = format.lower()

    # Check if it is either Season ID 
    if(format == "season"):
        selector = "Season_ID"

    elif(format == "team"):
        selector = "Team_ID"

    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists 
    if(check_table('Team')):
        
        # Only one pk value was inputed
        if(id_two is None):
            try:
                # Create a parameterized querry 
                querry = conn.execute(
                """
                SELECT *
                FROM Team
                WHERE %s = %s
                """, selector, id_one)
                trans.commit()
                print("Querry_Team_Single_Pk was successful ")
      
            except:
                raise Exception("Querry_Team_Single_Pk failed")

        # Two pk values was inputed 
        else:
            try:
                # Create a parameterized querry 
                querry = conn.execute(
                """
                SELECT *
                FROM Team
                WHERE %s BETWEEN %s AND %s
                """, selector, id_one, id_two)
                trans.commit()
                print("Querry_Team_Single_Pk was successful ")
            except:
                raise Exception("Querry_Team_Single_Pk failed")
    else:
        raise Exception("Table does not exists")
    
    df = pd.DataFrame(querry.fetchall())
    df.columns = querry.keys()

'''
Input: s_id_one = first season_id value
       s_id_two = second season_id value passed if wanting a range(using Between)
       t_id_one = first team_id value
       t_id_two = second team_id value pass if wanting a range(using Between)
Returns all column inside of Teams based on two primary keys
'''
def querry_all_team_double_pk(s_id_one, t_id_one, s_id_two = None, t_id_two = None):
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists 
    if(check_table('Team')):

        # s_id_two == None and t_id_two != None
        if(s_id_two is None and t_id_two is not None):
            try:
                # Create a parameterized querry 
                querry = conn.execute(
                """
                SELECT *
                FROM Team
                WHERE Season_ID = %s 
                AND Team_ID BETWEEN %s, %s 
                """, s_id_one, t_id_one, t_id_two)
                trans.commit()
                print("Querry_Team_Single_Pk was Successful ")
            except:
                raise Exception("Querry_Team_Double_Pk Failed")

        # s_id_two != None and t_id_two == None
        elif(s_id_two is not None and t_id_one is None):
            try:
                # Create a parameterized querry 
                querry = conn.execute(
                """
                SELECT *
                FROM Team
                WHERE Team_ID = %s 
                AND Season_ID BETWEEN %s, %s 
                """, t_id_one, s_id_one, s_id_two)
                trans.commit()
                print("Querry_Team_Single_Pk was Successful ")
            except:
                raise Exception("Querry_Team_Double_Pk Failed")
        
        # s_id_two == None and t_id_two == None
        else:
            try:
                # Create a parameterized querry 
                querry = conn.execute(
                """
                SELECT *
                FROM Team
                WHERE Season_ID = %s 
                AND Team_ID = %s 
                """, t_id_one, s_id_one)
                trans.commit()
                print("Querry_Team_Single_Pk was Successful ")
            except:
                raise Exception("Querry_Team_Double_Pk Failed")
    else:
        raise Exception("Table Team not Found")



def querry_all_teams_name_or_abv(format, string):
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    # Check if the table exists 
    #if(check_table('Team')):

