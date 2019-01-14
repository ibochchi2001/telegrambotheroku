import telebot
from telebot import types
import bs4,requests

bot = telebot.TeleBot("717226876:AAHKv0oOw8wZ0PTEai2G0kqfARjoKVi7mQU")


@bot.message_handler(commands=['start'])
def hendle_start(message):
    f_name = message.first_name
    some_text = "Assalomu alaykum"+f_name+"!"
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
    bot.send_message(message.from_user.id, "*Namoz vaqtlari*\n\n_Tong: _ `{}`\n_Quyosh: _ `{}`\n_Peshin: _ `{}`\n_Asr: _ `{}`\n_Shom: _ `{}`\n_Xufton: _ `{}`".format(Tong,Quyosh,Peshin,Asr,Shom,Xufton), parse_mode="markdown")

bot.polling(none_stop="True", interval=0)
