import psycopg2
from psycopg2 import OperationalError
import numpy as np
import pandas as pd

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection
    
    connection = create_connection(
    'd676an9rvgsvr6', 
    'tzgtszqowqbeyo', 
    '586035937444c59190c595f740d92824a2a5430d959386b79866d7b623c52c7b', 
    'ec2-54-172-173-58.compute-1.amazonaws.com', 
    '5432')
    
    def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    
    
