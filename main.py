from aiogram import Bot, types
import asyncio
from base import get_player, update_player, add_player
from persons import player
from constants import states
import keyboards
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from Token import token
bot = Bot(token)
dp = Dispatcher(bot)
async def sleeping(message):
    await asyncio.sleep(5)
    await bot.send_message(message, 'я доспал!')

async def give_player_name(name):
    player = get_player(name.from_user.id)
    player.set_name(name.text)
    player.set_state('class')
    update_player(name.from_user.id, player)
    await bot.send_message(name.chat.id, 'Имя установлено! ')
    await bot.send_message(name.chat.id, 'Выберите класс!', reply_markup = keyboards.class_keyboard)

async def give_player_class(user_id, class_of_player):
    player = get_player(user_id)
    player.set_class_of_player(class_of_player)
    player.set_state('well done!')
    update_player(user_id, player)
    await bot.send_message(user_id, 'Класс установлен!')

@dp.callback_query_handler(lambda c: c.data)
async def process_callback_kb(callback_query: types.CallbackQuery):
    data = callback_query.data
    user_id = callback_query.from_user.id
    if data == 'status':
        await sleeping(user_id)
        await bot.answer_callback_query(callback_query.id)
    elif data == 'equip':
        await bot.answer_callback_query(callback_query.id)
    elif data == 'trip':
        await bot.answer_callback_query(callback_query.id)
    elif data == 'warrior' or data == 'thief' or data == 'bower':
        await give_player_class(user_id, data)
        await bot.answer_callback_query(callback_query.id)
    

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    if message.text == '/start':
        new_player = player(None, 1000, 100, 50)
        if add_player(message.from_user.id, new_player):
            await bot.send_message(message.chat.id, 'Ты уже в игре!')
        else:
            await message.reply(f'Я Олег. Начнем игру. Назови своего персонажа.')
    else:
        await message.reply(f'Этот бот -  игра, он находится в разработке.')

@dp.message_handler(content_types=['status'])
async def command_status(message):
    await bot.send_message(message.chat.id, 'Привет!')

@dp.message_handler(lambda message: 
                    get_player(message.from_user.id).get_state() in states,
                    content_types=['text'])
async def parse_states(message):
    state = get_player(message.from_user.id).get_state()
    if state == 'name':
        await give_player_name(message)
    elif state == 'class' and message.text.lower() == 'лягущка':
        await give_player_class(message)

@dp.message_handler(content_types=['text'])
async def get_text_messages(message):
    if message.text.lower() == 'привет':
        await bot.send_message(message.chat.id, 'Привет!')
    elif message.text.lower() == 'мой персонаж':
        player = get_player(message.from_user.id)
        info = text(f'Имя: {player.get_name()}',
                    f'Класс: {player.get_class()}',
                    f'Здоровье: {player.get_hp()}/{player.get_max_hp()}',
                    f'Защита: {player.get_armor()}',
                    f'Атака: {player.get_attack()}',
                    f'Деньги: {player.get_money()}',
                    f'Снаряжение: {player.get_eqip()}               ',
                    f'Инвентарь: {player.get_items()}', sep = '\n')
        await bot.send_message(message.chat.id, info, reply_markup = keyboards.my_character_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)