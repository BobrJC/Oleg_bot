import sqlite3 as sql
from sqlite3.dbapi2 import PrepareProtocol
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

def update_player(id: int, player):
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

def player_class_parser(class_of_player: str) -> persons.person:
    if class_of_player == 'warrior':
        return persons.warrior
    elif class_of_player == 'thief':
        return persons.thief
    elif class_of_player == 'bower':
        return persons.bower
    elif class_of_player == 'new player':
        return persons.player

def get_player(id: int) -> persons.player:
    data = sql.connect('base.db')
    cursor = data.cursor()
    cursor.execute(f"SELECT * from players WHERE id = {id}")
    player_data = cursor.fetchall()[0]
    player_class = player_data[class_of_player]

    if player_data != []:
        player = player_class_parser(player_class)(
                                    player_data[name], player_data[max_hp], 
                                    player_data[armor], player_data[attack],
                                    player_data[level], player_data[hp], 
                                    player_data[equip], player_data[item], 
                                    player_data[money], player_data[state])
        return player
    else:
        print('err, no user with that id')

def add_player(id: int, player):
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
