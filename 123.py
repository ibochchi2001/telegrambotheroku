import telebot
from telebot import types

bot = telebot.TeleBot("718228299:AAF8CMQLYXHzIEqtyLjIflkYdnJYfzhsxF4")


@bot.message_handler(commands=['start'])
def hendle_start(message):
    some_text = "Hello"
    bot.send_message(message.from_user.id, some_text)
@bot.message_handler(commands=['vaqt'])
def vaqt(message):
    bot.send_message(message.chat.id, "Vaqt")

bot.polling(none_stop="True", interval=0)
