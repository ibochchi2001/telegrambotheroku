import os
from bs4 import BeautifulSoup
import re
import requests
from flask import Flask, request

import telebot

TOKEN = '665868259:AAEVV_-Zu4gsxyIUpcaj2Y5A9sXpViYSvy0'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)
@bot.message_handler(commands=['vaqt'])
def vaqt():
    url = requests.get("http://islom.uz")
    soup = BeautifulSoup(url.text, "html.parser")

    for span in soup.find_all("div", "p_clock", text=re.compile(r'\d{2}:\d{2}')):
        bot.send_message(message.chat.id, "Vaqt"+span.text.split()[0])
    

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://salombot.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
