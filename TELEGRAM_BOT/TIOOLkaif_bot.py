import telebot
from telebot import types

bot = telebot.TeleBot('6495102677:AAFeEXaCeBq9nMDSMGoHB1xVSQDPIW-wx4M')

@bot.message_handler(commands=['start'])
def count(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Каталог и цены', url='https://docs.google.com/spreadsheets/d/1-I46WOgFGU2LXGMEYQI_v7-bXkZvrfEjht33Hx8QvVY/edit')
    btn2 = types.InlineKeyboardButton('По поводу заказа', callback_data='person')
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(message.chat.id, 'Одноразки TIOOL \nОстровцы Октябрьский', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'person':
        bot.send_message(callback.message.chat.id, 'Для заказа или по вопросам пишите: ')
        bot.send_message(callback.message.chat.id, '@TIOOLvake')

bot.infinity_polling()
