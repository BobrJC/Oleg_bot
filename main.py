from weapons import generate_weapon
from aiogram import Bot, types
import asyncio
from base import get_player, update_player, add_player
from persons import *
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
    player.set_state('well done!')
    update_player(player)
    await bot.send_message(name.chat.id, 'Имя установлено! ')
    

async def print_status(user_id):
    player = get_player(user_id)
    await bot.send_message(user_id,
        f'''
        Состояние: {player.get_state}
        До следующей прогулки:
        '''
    )

@dp.callback_query_handler(lambda c: c.data)
async def process_callback_kb(callback_query: types.CallbackQuery):
    data = callback_query.data
    user_id = callback_query.from_user.id
    if data == 'status':
        await bot.answer_callback_query(callback_query.id)
    elif data == 'equip':
        await bot.answer_callback_query(callback_query.id)
    elif data == 'trip':
        await bot.answer_callback_query(callback_query.id)
    elif data == 'warrior' or data == 'thief' or data == 'bower':
        if get_player(user_id) == []:
            player = player_class_parser(data)(user_id, data, '', 1000, 50, 100, state='name')
            weap = generate_weapon(player.get_available_weapon(), 1)
            player.set_eqip(json.dumps({'weapon' : weap.dict()}))
            print(player.get_all_atributes())
            add_player(player)
            await bot.send_message(callback_query.message.chat.id, 'Назови своего персонажа!')
        else:
            await bot.send_message(callback_query.message.chat.id, f'{callback_query.from_user.first_name}, у тебя уже есть класс!')
        await bot.answer_callback_query(callback_query.id)
    

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    print(get_player(message.from_user.id))
    if message.text == '/start':
        if get_player(message.from_user.id) != []:
            await bot.send_message(message.chat.id, 'Ты уже в игре!')
        else:
            await message.reply(f'Я Олег. Начнем игру.')
            await bot.send_message(message.chat.id, 'За какой класс ты бы хотел играть?', reply_markup = keyboards.class_keyboard)
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
        await bot.send_message(message.from_user.id, 'AAA')

@dp.message_handler(content_types=['text'])
async def get_text_messages(message):
    if message.text.lower() == 'привет':
        await bot.send_message(message.chat.id, 'Привет!')
    elif message.text.lower() == 'мой персонаж':

        player = get_player(message.from_user.id)
        print(player.get_all_atributes())
        info = text(f'Имя: {player.get_name()}',
                    f'Класс: {player.get_class()}',
                    f'Здоровье: {player.get_hp()}/{player.get_max_hp()}',
                    f'Защита: {player.get_armor()}',
                    f'Атака: {player.get_attack()}',
                    f'Деньги: {player.get_money()}',
                    f'Снаряжение: {player.get_equipment()}               ',
                    f'Инвентарь: {player.get_items()}', sep = '\n')
        await bot.send_message(message.chat.id, info, reply_markup = keyboards.my_character_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)