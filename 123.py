import telebot
import os
import constants

bot = telebot.TeleBot(constants.token)

print(bot.get_me())

def log (message , answer):
    print("\n ----------")
    from datetime import  datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                       message.text))
    print(answer)

@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = "Я ничего не умею :C"
    log(message,answer)
    bot.send_message(message.chat.id, """Я ничего не умею :C""")

@bot.message_handler(commands=['settings'])
def handle_text(message):
    answer = "Я и так идиален ! "
    log(message, answer)
    bot.send_message(message.chat.id, "Я и так идиален ! ")
@bot.message_handler(commands=['start'])
def handle_text(message):
    answer = "Я и так был уже запужен"
    log(message,answer)
    bot.send_message(message.chat.id, "Я и так уже был запущен")

@bot.message_handler(commands=['stop'])
def handle_text(message):
    answer = "На что ты надеялся?"
    log(message,answer)
    bot.send_message(message.from_user.id, "На что ты надеялся? ")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Шо,каво"
    if message.text == "а":
        bot.send_message(message.from_user.id, "Зачем ты мне букву а отправил?")
        answer = "Зачем ты мне букву а отправил?"
        log(message,answer)
    elif message.text == "0":
        answer = "Это что,твой iq?"
        log(message,answer)
        bot.send_message(message.from_user.id, "Это что,твой iq?")
    else:
        bot.send_message(message.from_user.id, answer)





if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://salombot.herokuapp.com/") # этот url нужно заменить на url вашего Хероку приложения
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.  
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    bot.remove_webhook()
    bot.polling(none_stop=True)
