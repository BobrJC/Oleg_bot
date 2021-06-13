import sqlite3 as sql


create_users_table = """
CREATE TABLE IF NOT EXISTS players(
 id INTEGER PRIMARY KEY,
 name TEXT NOT NULL,
 equipment TEXT,
 items TEXT
);
"""

def create_table():
    data = sql.connect('base.db')
    cursor = data.cursor()
    cursor.execute(create_users_table)
create_table()
def add_player(id):
    data = sql.connect('base.db')
    cursor = data.cursor()
    cursor.execute(f"SELECT id from players WHERE id = {id}")
    result = cursor.fetchall()
    if result != [(id,)]:
        cursor.execute(f"INSERT into players (id, name, equipment, items) VALUES ({id}, 'none', 'none', 'none');")
    else:
        return True
    data.commit()
