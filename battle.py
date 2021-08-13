from asyncio.tasks import sleep
from base import get_player
from persons import *
import asyncio
import main
from aiogram.utils.markdown import text
import sqlite3 as sql
import aioschedule
def create_table():
    create_users_table = """
    CREATE TABLE IF NOT EXISTS opponents(
         id INTEGER PRIMARY KEY,
         level INTEGER,
         chat_id INTEGER
    );
    """
    data = sql.connect('battle.db')
    cursor = data.cursor()
    cursor.execute(create_users_table)
create_table()


def add_oponent(id: int, level: int, chat_id: int):
    data = sql.connect('battle.db')
    cursor = data.cursor()
    cursor.execute("""
    SELECT *
    FROM opponents
    WHERE id = ?;
    """, (id, ))
    if cursor.fetchall() == []:
        cursor.execute("""
        INSERT INTO opponents (id, level, chat_id)
        VALUES (?, ?, ?)
        """, (id, level, chat_id))
        data.commit()
        return True
    else:
        data.commit()
        return False
    

async def find_opponent():
    data = sql.connect('battle.db')
    cursor = data.cursor()
    cursor.execute("""
    SELECT * 
    FROM opponents
    ORDER BY level; 
    """)
    opponents = cursor.fetchall()
    if opponents == []:
        data.commit()
        return
    for i in range(len(opponents) - 1):
        if opponents[i + 1][1] <= opponents[i][1] + 2:
            await start_battle(get_player(opponents[i][0]), get_player(opponents[i + 1][0]), opponents[i][2], opponents[i + 1][2])
            cursor.execute("""
            DELETE FROM opponents
            WHERE id = ? AND id = ?
            """, (opponents[i][0], opponents[i + 1][0]))
    data.commit()

async def start_battle(first_fighter: player, second_fighter: person, first_chat_id: int, second_chat_id: int):
    first_msg = await main.bot.send_message(first_chat_id, f'Начинается битва между {first_fighter.get_name()} и {second_fighter.get_name()}')
    if first_chat_id != second_chat_id:
        second_msg = await main.bot.send_message(second_chat_id, f'Начинается битва между {first_fighter.get_name()} и {second_fighter.get_name()}')
    while first_fighter.is_alife() and second_fighter.is_alife():
        battle_msg = text(
        f'Персонаж {first_fighter.get_name()}',
        f'Здоровье: {first_fighter.get_hp()}',
        f'Принаял урона (пока нет)\n',
        f'Персонаж {second_fighter.get_name()}',
        f'Здоровье: {second_fighter.get_hp()}',
        f'Принаял урона (пока нет)'
        )
        second_fighter.take_damage(first_fighter.get_attack())
        first_fighter.take_damage(second_fighter.get_attack())
        await asyncio.sleep(2)
        await first_msg.edit_text(battle_msg)
        if first_chat_id != second_chat_id:
            await second_msg.edit_text(battle_msg)
    if first_fighter.is_alife():
        await main.bot.send_message(first_chat_id, f'Победил {first_fighter.get_name()}')
        if first_chat_id != second_chat_id:
            await main.bot.send_message(second_chat_id, f'Победил {first_fighter.get_name()}')
    elif second_fighter.is_alife():
        await main.bot.send_message(first_chat_id, f'Победил {second_fighter.get_name()}')
        if first_chat_id != second_chat_id:
            await main.bot.send_message(second_chat_id, f'Победил {second_fighter.get_name()}')
    else:
        await main.bot.send_message(first_chat_id, 'Ничья!')
        if first_chat_id != second_chat_id:
            await main.bot.send_message(second_chat_id, 'Ничья!')
        
async def check_battle():
    print('Started')
    aioschedule.every(1).minutes.do(find_opponent)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
