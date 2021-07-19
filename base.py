import sqlite3 as sql
import persons
from constants import *

def create_table():
    create_users_table = """
    CREATE TABLE IF NOT EXISTS players(
         id INTEGER PRIMARY KEY,
         class TEXT,
         name TEXT,
         max_hp INTEGER,
         armor INTEGER,
         attack INTEGER,
         level INTEGER,
         hp INTEGER,
         equipment TEXT,
         items TEXT,
         money INTEGER,
         state TEXT
    );
    """
    data = sql.connect('base.db')
    cursor = data.cursor()
    cursor.execute(create_users_table)
create_table()

def update_player(id, player):
    data = sql.connect('base.db')
    cursor = data.cursor()
    params = tuple(player.get_all_atributes().values()) + (id,)
    cursor.execute(f'''UPDATE players SET 
                    class = ?,
                    name = ?, 
                    max_hp = ?,
                    armor = ?,
                    attack = ?,
                    level = ?,
                    hp = ?,
                    equipment = ?,
                    items = ?,
                    money = ?,
                    state = ?
                    WHERE id = ?''', params)
    print(params)
    data.commit()

def get_player(id):
    data = sql.connect('base.db')
    cursor = data.cursor()
    cursor.execute(f"SELECT * from players WHERE id = {id}")
    player_data = cursor.fetchall()
    if player_data != []:
        player_data = player_data[0]
        print(player_data)
        if player_data[class_of_player] == 'warrior':
            player = persons.warrior(player_data[name], player_data[max_hp], 
                             player_data[armor], player_data[attack],
                             player_data[level], player_data[hp], 
                             player_data[equip], player_data[item], 
                             player_data[money], player_data[state])
        elif player_data[class_of_player] == 'thief':
            player = persons.thief(player_data[name], player_data[max_hp], 
                             player_data[armor], player_data[attack],
                             player_data[level], player_data[hp], 
                             player_data[equip], player_data[item], 
                             player_data[money], player_data[state])
        elif player_data[class_of_player] == 'bower':
            player = persons.bower(player_data[name], player_data[max_hp], 
                             player_data[armor], player_data[attack],
                             player_data[level], player_data[hp], 
                             player_data[equip], player_data[item], 
                             player_data[money], player_data[state])
        elif player_data[class_of_player] == 'new player':
            player = persons.player(player_data[name], player_data[max_hp], 
                             player_data[armor], player_data[attack],
                             player_data[level], player_data[hp], 
                             player_data[equip], player_data[item], 
                             player_data[money], player_data[state])
        return player
    else:
        print('err, no user with that id')

def add_player(id, player):
    data = sql.connect('base.db')
    cursor = data.cursor()
    cursor.execute(f"SELECT id from players WHERE id = {id}")
    result = cursor.fetchall()
    if result == []:
        params = player.get_all_atributes()
        print(', '.join(params))
        cursor.execute(f'''INSERT into players (id, {', '.join(params)})
                                        VALUES ({id}, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', list(params.values()))
        print(params)
    else:   
        return True
    data.commit()
