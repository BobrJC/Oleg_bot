import sqlite3 as sql
from sqlite3.dbapi2 import PrepareProtocol
import persons
from constants import *
import json

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

def update_player(player):
    data = sql.connect('base.db')
    cursor = data.cursor()
    params = tuple(player.get_all_atributes().values())
    print(params)
    cursor.execute(f'''UPDATE players SET 
                    id = ?,
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
                    WHERE id = {params[owner_id]}''', params, )
    #print(params)
    data.commit()

def get_player(id: int) -> persons.player:
    data = sql.connect('base.db')
    cursor = data.cursor()
    cursor.execute(f"SELECT * from players WHERE id = {id}")
    player_data = cursor.fetchall()
    if player_data == []:
        data.commit()
        return player_data
    player_data = player_data[0]
    player_class = player_data[class_of_player]
    if player_data[equip] != None:
        player_equipment = json.loads(player_data[equip])
    else:
        player_equipment = {'weapon' : None}
    #print('get_player:', player_data)
    #print('get_player player_equipment:', player_equipment)
    player = persons.player_class_parser(player_class)(
                                player_data[owner_id], player_class, 
                                player_data[name], player_data[max_hp], 
                                player_data[armor], player_data[attack],
                                player_data[level], player_data[hp],
                                player_data[equip], player_data[item],
                                player_data[money], player_data[state])
    #print(player.get_all_atributes())
    data.commit()
    return player
    

def add_player(player):
    params = tuple(player.get_all_atributes().values())
    #print('PARANS: ', params)
    data = sql.connect('base.db')
    cursor = data.cursor()
    cursor.execute(f'''INSERT into players (id, class, name , max_hp, armor, attack, level, hp, equipment, items, money, state)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', params)
    data.commit()
