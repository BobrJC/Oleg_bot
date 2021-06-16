from aiogram import Bot, types
import base
import persons
import constants
import keyboards
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot('1480433265:AAEErBjIfDoNieqrxPh2REmUEdF4u82wiRg')
dp = Dispatcher(bot)

@dp.callback_query_handler(lambda c: c.data)
async def process_callback_kb(callback_query: types.CallbackQuery):
    data = callback_query.data
    if data == 'status':
        await callback_query.message.answer('Привет!')
        await bot.answer_callback_query(callback_query.id)
    elif data == 'equip':
        await bot.answer_callback_query(callback_query.id)
    elif data == 'trip':
        await bot.answer_callback_query(callback_query.id)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    if message.text == '/start':
        new_player = persons.player(1000, 100, 50)
        if base.add_player(message.from_user.id, new_player):
            await bot.send_message(message.chat.id, 'Ты уже в игре!')
        else:
            await message.reply(f'Я Олег. Начнем игру. Назови своего персонажа.')
    else:
        await bot.reply_to(message, f'Этот бот -  игра, он находится в разработке.')

@dp.message_handler(content_types=['status'])
async def command_status(message):
    await bot.send_message(message.chat.id, 'Привет!')



@dp.message_handler(lambda message: base.get_player(message.from_user.id).get_state() == 'name', content_types=['text'])
async def give_player_name(name):
    player = base.get_player(name.from_user.id)
    player.set_name(name)


@dp.message_handler(content_types=['text'])
async def get_text_messages(message):
    if message.text.lower() == 'привет':
        await bot.send_message(message.chat.id, 'Привет!')
    elif message.text.lower() == 'мой персонаж':
        player = base.get_player(message.from_user.id)
        info = text(f'Имя: {player.get_name()}',
                    f'Снаряжение: {player.get_eqip()}               ',
                    f'Инвентарь: {player.get_items()}', sep = '\n')
        await bot.send_message(message.chat.id, info, reply_markup = keyboards.my_character_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)