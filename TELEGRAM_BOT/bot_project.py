import telebot
from telebot import types

bot = telebot.TeleBot('6126472660:AAEM_qLOIT2D--wsLB07YCvqXsgDamJayI4')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

bot.infinity_polling()
