import telebot
import base
bot = telebot.TeleBot('1480433265:AAEErBjIfDoNieqrxPh2REmUEdF4u82wiRg')

def init_player(id):
    f = open('palyers.txt', 'a')
    print(id)
    f.write(str(id) + '\n')
    f.close()

def parse_players():
    players_ids_tuple = ()
    f = open('players.txt', 'r')
    for ids in f:
        players_ids_tuple.append(ids)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.text == '/start':
        if base.add_player(message.from_user.id):
            bot.send_message(message.from_user.id, 'Ты уже в игре!')
        bot.reply_to(message, f'Я Олег. Начнем игру')
    else:
        bot.reply_to(message, f'Этот бот -  игра, он находится в разработке.')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

bot.polling(none_stop=True)

