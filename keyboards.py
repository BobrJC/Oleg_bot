from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.dispatcher import Dispatcher
from enum import Enum
my_character_keyboard = InlineKeyboardMarkup(row_width=2)
class_keyboard = InlineKeyboardMarkup(row_width=2)

status_key = InlineKeyboardButton('Статус', callback_data='status')
equip_key = InlineKeyboardButton('Снаряжение', callback_data='equip')
trip_key = InlineKeyboardButton('Поход', callback_data='trip')
warrior_key = InlineKeyboardButton('Воин', callback_data='warrior')
thief_key = InlineKeyboardButton('Вор', callback_data='thief')
bower_key = InlineKeyboardButton('Лучник', callback_data='bower')

my_character_keyboard.add(status_key, equip_key, trip_key)
class_keyboard.add(warrior_key, thief_key, bower_key)

#async def init_keyboard():
#    for key in keys:

