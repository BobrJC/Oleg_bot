import sqlite3 as sql
import persons

create_users_table = """
CREATE TABLE IF NOT EXISTS players(
 id INTEGER PRIMARY KEY,
 name TEXT,
 level INTEGER,
 max_hp INTEGER,
 hp INTEGER,
 armor INTEGER,
 attack INTEGER,
 equipment TEXT,
 items TEXT
 money INTEGER
 state TEXT
);
"""

def create_table():
    data = sql.connect('base.db')
    cursor = data.cursor()
    cursor.execute(create_users_table)
create_table()


def get_player(id):
    data = sql.connect('base.db')
    cursor = data.cursor()
    cursor.execute(f"SELECT * from players WHERE id = {id}")
    result = cursor.fetchall()
    if result != []:
        result = result[0]
        player = persons.player(result[1], result[2], result[3], result[4], result[5], 
                                result[6], result[7], result[8], result[9], result[10])
#        res_dic = {'name' : result[1], 
#                'level' : result[2], 
#                'max_hp' : result[3],
#                'hp' : result[4],
#                'armor' : result[5],
#                'attack' : result[6],
#                'equipment' : result[7],
#                'items' : result[8],
#                'money' : result[9],
#                'state' : result[10]}
        return player
    else:
        print('err, no user with that id')

def add_player(id, player):
    data = sql.connect('base.db')
    cursor = data.cursor()
    cursor.execute(f"SELECT id from players WHERE id = {id}")
    result = cursor.fetchall()
    if result == []:
        params = (player.get_name(), player.get_level(), player.get_max_hp(), player.get_hp(), player.get_armor(), player.get_attack(), player.get_money(), player.get_state())
        cursor.execute(f'''INSERT into players (id, name, level, max_hp, hp, armor, attack, equipment, items, money, state)
                                        VALUES ({id}, ?, ?, ?, ?, ?, ?, 'none', 'none', ?, ?);''', params)
    else:   
        return True
    data.commit()
