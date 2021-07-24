from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.dispatcher import Dispatcher
from enum import Enum
my_character_keyboard = InlineKeyboardMarkup(row_width=2)
class_keyboard = InlineKeyboardMarkup(row_width=2)
class keys(Enum):
    status_key = InlineKeyboardButton('Статус', callback_data='status')
    equip_key = InlineKeyboardButton('Снаряжение', callback_data='equip')
    trip_key = InlineKeyboardButton('Поход', callback_data='trip')
    warrior_key = InlineKeyboardButton('Воин', callback_data='warrior')
    thief_key = InlineKeyboardButton('Вор', callback_data='thief')
    bower_key = InlineKeyboardButton('Лучник', callback_data='bower')

my_character_keyboard.add(keys.status_key, keys.equip_key, keys.trip_key)
class_keyboard.add(keys.warrior_key, keys.thief_key, keys.bower_key)

#async def init_keyboard():
#    for key in keys:

