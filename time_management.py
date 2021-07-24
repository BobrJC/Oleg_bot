import time
import sqlite3 as sql

def get_moment_time():
    return (time.localtime().tm_hour, time.localtime().tm_min) 

def create_table():
    create_users_table = """
    CREATE TABLE IF NOT EXISTS time(
        id INTEGER PRIMARY KEY,
        next_walk TEXT
    );
    """
    data = sql.connect('time.db')
    cursor = data.cursor()
    cursor.execute(create_users_table)
create_table()