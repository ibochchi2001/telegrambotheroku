import telebot
from telebot import types
import bs4,requests

bot = telebot.TeleBot("718228299:AAF8CMQLYXHzIEqtyLjIflkYdnJYfzhsxF4")


@bot.message_handler(commands=['start'])
def hendle_start(message):
    some_text = "Hello"
    bot.send_message(message.from_user.id, some_text)
@bot.message_handler(commands=['vaqt'])
def vaqt(message):
    s=requests.get('https://islom.uz')
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p3=b.select('#tc1')
    Tong=p3[0].getText()
    
    p4=b.select('#tc2')
    Quyosh=p4[0].getText()
    
    p5=b.select('#tc3')
    Peshin=p5[0].getText()
    
    p6=b.select('#tc4')
    Asr=p6[0].getText()
    
    p7=b.select('#tc5')
    Shom=p7[0].getText()
    p8=b.select('#tc6')
    Xufton=p8[0].getText()
    bot.send_message(message.from_user.id, "**Vaqt**\nTong {}\nQuyosh: {}\nPeshin: {}\nAsr: {}\nShom: {}\nXufton: {}".format(Tong,Quyosh,Peshin,Asr,Shom,Xufton))

bot.polling(none_stop="True", interval=0)
