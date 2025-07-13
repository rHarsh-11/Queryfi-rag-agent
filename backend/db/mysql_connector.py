import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="rootpass",
    database="valuefy"
)

def fetch_from_mysql(query: str):
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    return df
