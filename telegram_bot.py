from pathlib import Path

import telebot
# Создаем экземпляр бота
token = Path('token').read_text()
bot = telebot.TeleBot(token)
# Функция, обрабатывающая команду /start
dataset = False


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Напиши мне название датасета')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    print(message)
    bot.send_message(message.chat.id, 'Датасет: ' + message.text)
    # dataset = True
    print(123)
    bot.send_message(message.chat.id, 'Напиши колонку')
    # bot.send_message(message.chat.id, 'Напиши для чего')


# Запускаем бота
bot.polling(none_stop=True, interval=0)
