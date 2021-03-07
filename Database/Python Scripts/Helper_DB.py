import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd

'''
Creates database connection and returns the engine
'''
def create_connection():
    connection_url = 'mysql+pymysql://bryan:bdelasp1@localhost:3306/BasketBallDB'
    engine = sal.create_engine(connection_url)
    
    return engine

'''
Function that tests the connection of the database
'''
def test_connection(engine):
    # Test the connection of the database
    try:
        conn = engine.connect()
        return conn

    except:
        raise Exception("Did not connect to BasketBall Database")

'''
Function that test to see if the table has been created
'''
def check_table(tablename):
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
    trans = conn.begin()
    
    # Test to see if the table exists
    test = conn.execute(
    """
    SHOW TABLES 
    LIKE %s
    """, tablename
    ).fetchall()    
    trans.commit()
    conn.close()
    # Check if the list is empty 
    if test:
        print("Table exists")
        return True
    
    else:
        print("Table does not exists")
        return False

'''
Function that checks to see if the stored procedure is inside the querry
'''
def check_procedure(procedure):
    # Connect to sql database
    engine = create_connection()
    
    # Test the connection of the database
    conn = test_connection(engine)
 
    trans = conn.begin()

    test = conn.execute(
    """
    SHOW PROCEDURE STATUS LIKE %s

    """, procedure
    ).fetchall()
    trans.commit()
    conn.close()
    if test:
        print("Procedure Exists")
        return True
    else:
        print("Procedure does not Exist")
        return False
